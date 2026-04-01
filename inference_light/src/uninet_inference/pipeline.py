from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

from uninet_inference.diagnostics.compatibility_scoring import (
    CompatibilityThresholds,
    score_compatibility,
)
from uninet_inference.diagnostics.convergence import summarize_convergence
from uninet_inference.diagnostics.posterior_predictive import compute_posterior_predictive_summary
from uninet_inference.io.dataset_loader import load_enabled_datasets
from uninet_inference.io.schema_validation import (
    load_yaml_file,
    validate_compatibility_config,
    validate_datasets_config,
    validate_parameters_config,
    validate_prior_config,
    validate_run_config,
)
from uninet_inference.likelihoods.joint_likelihood import total_log_likelihood
from uninet_inference.model.uninet_param_map import (
    initial_center,
    split_parameter_roles,
    theta_to_param_dict,
    theta_within_bounds,
)
from uninet_inference.priors.prior_registry import evaluate_log_prior, load_prior_definitions
from uninet_inference.reporting.results_markdown import build_results_markdown
from uninet_inference.reporting.summaries import summarize_posterior
from uninet_inference.sampling.chain_io import save_chain_h5
from uninet_inference.sampling.emcee_runner import SamplerConfig, run_sampler


def _json_dump(path: Path, payload: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)


def _write_csv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _resolve_run_id(run_id_config: str) -> str:
    if run_id_config != "auto":
        return run_id_config
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"inference_light_{timestamp}"


def _deep_update(target: dict[str, Any], updates: dict[str, Any]) -> dict[str, Any]:
    merged = dict(target)
    for key, value in updates.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _deep_update(merged[key], value)
        else:
            merged[key] = value
    return merged


def run_pipeline(
    project_root: Path,
    run_id_override: str | None = None,
    run_config_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    config_dir = project_root / "configs"

    run_config = load_yaml_file(config_dir / "run.yaml")
    parameters_config = load_yaml_file(config_dir / "parameters.yaml")
    datasets_config = load_yaml_file(config_dir / "datasets.yaml")
    priors_regge_config = load_yaml_file(config_dir / "priors_regge.yaml")
    priors_efe_config = load_yaml_file(config_dir / "priors_efe.yaml")
    compatibility_config = load_yaml_file(config_dir / "compatibility.yaml")

    if run_config_overrides:
        run_config = _deep_update(run_config, run_config_overrides)

    validate_run_config(run_config)
    validate_parameters_config(parameters_config)
    validate_datasets_config(datasets_config, project_root)

    known_parameters = set(parameters_config["parameters"].keys())
    validate_prior_config(priors_regge_config, known_parameters, "regge prior config")
    validate_prior_config(priors_efe_config, known_parameters, "efe prior config")
    validate_compatibility_config(compatibility_config)

    run_id = run_id_override if run_id_override else _resolve_run_id(run_config["run_id"])
    run_dir = project_root / "runs" / run_id
    stage_dirs = {
        "ingest": run_dir / "01_ingest",
        "priors": run_dir / "02_priors",
        "sampling": run_dir / "03_sampling",
        "diagnostics": run_dir / "04_diagnostics",
        "reports": run_dir / "05_reports",
    }
    for path in stage_dirs.values():
        path.mkdir(parents=True, exist_ok=True)

    datasets, manifest = load_enabled_datasets(datasets_config, project_root)
    _json_dump(stage_dirs["ingest"] / "manifest.json", manifest)

    fit_specs, fixed_params, _ = split_parameter_roles(parameters_config)
    prior_defs = load_prior_definitions(priors_regge_config, priors_efe_config)

    prior_snapshot = {
        "regge": priors_regge_config["priors"],
        "efe": priors_efe_config["priors"],
        "all": [asdict(item) for item in prior_defs],
    }
    _json_dump(stage_dirs["priors"] / "prior_snapshot.json", prior_snapshot)

    center = initial_center(fit_specs)
    seed = int(run_config["seed"])
    sampler_settings = SamplerConfig(**run_config["sampler"])

    def _log_probability(theta: np.ndarray) -> float:
        theta = np.asarray(theta, dtype=float)
        if not theta_within_bounds(theta, fit_specs):
            return float("-inf")
        params = theta_to_param_dict(theta, fit_specs, fixed_params)
        log_prior = evaluate_log_prior(params, prior_defs)
        if not math.isfinite(log_prior):
            return float("-inf")
        log_like = total_log_likelihood(datasets, params)
        return float(log_prior + log_like)

    sampler_result = run_sampler(_log_probability, center, sampler_settings, seed)
    save_chain_h5(
        path=stage_dirs["sampling"] / "chains.h5",
        chain=sampler_result.chain,
        log_prob=sampler_result.log_prob,
        samples=sampler_result.samples,
        parameter_names=[spec.name for spec in fit_specs],
        acceptance_fraction=sampler_result.acceptance_fraction,
    )

    convergence = summarize_convergence(sampler_result.chain, sampler_result.acceptance_fraction)
    posterior_predictive = compute_posterior_predictive_summary(
        datasets=datasets,
        posterior_samples=sampler_result.samples,
        fit_specs=fit_specs,
        fixed_params=fixed_params,
        n_draws=int(run_config["diagnostics"]["posterior_draws"]),
        seed=seed + 1,
    )

    thresholds = compatibility_config["thresholds"]
    compatibility = score_compatibility(
        posterior_predictive=posterior_predictive,
        thresholds=CompatibilityThresholds(
            green_sigma_max=float(thresholds["green_sigma_max"]),
            amber_sigma_max=float(thresholds["amber_sigma_max"]),
            red_p_value_max=float(thresholds["red_p_value_max"]),
        ),
    )

    diagnostics_payload = {
        "convergence": convergence,
        "posterior_predictive": posterior_predictive,
        "compatibility_preview": compatibility,
    }
    _json_dump(stage_dirs["diagnostics"] / "diagnostics.json", diagnostics_payload)

    posterior_rows = summarize_posterior(
        sampler_result.samples, [spec.name for spec in fit_specs]
    )
    _write_csv(
        stage_dirs["reports"] / "posterior_summary.csv",
        posterior_rows,
        ["parameter", "median", "p16", "p84", "p2p5", "p97p5"],
    )
    _json_dump(stage_dirs["reports"] / "compatibility.json", compatibility)

    results_markdown = build_results_markdown(
        run_id=run_id,
        seed=seed,
        sampler_config=run_config["sampler"],
        dataset_manifest=manifest,
        prior_snapshot=prior_snapshot,
        posterior_rows=posterior_rows,
        compatibility=compatibility,
    )
    (stage_dirs["reports"] / "results.md").write_text(results_markdown, encoding="utf-8")

    return {
        "run_id": run_id,
        "run_dir": str(run_dir),
        "reports_dir": str(stage_dirs["reports"]),
        "traffic_light": compatibility["traffic_light"],
        "fits_known_physics_at_all": compatibility["fits_known_physics_at_all"],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the UniNet InferenceLight pipeline")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root containing configs/, data/, src/, and runs/.",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default=None,
        help="Optional run id override (defaults to run.yaml setting).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = run_pipeline(project_root=args.root.resolve(), run_id_override=args.run_id)
    print(json.dumps(result, indent=2))
    return 0
