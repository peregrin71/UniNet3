from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return data


def _ensure_keys(mapping: dict[str, Any], required: list[str], context: str) -> None:
    missing = [key for key in required if key not in mapping]
    if missing:
        raise ValueError(f"Missing keys in {context}: {missing}")


def validate_run_config(config: dict[str, Any]) -> None:
    _ensure_keys(config, ["run_id", "seed", "sampler", "diagnostics"], "run config")
    sampler = config["sampler"]
    diagnostics = config["diagnostics"]
    if not isinstance(sampler, dict):
        raise ValueError("run config 'sampler' must be a mapping")
    if not isinstance(diagnostics, dict):
        raise ValueError("run config 'diagnostics' must be a mapping")
    _ensure_keys(
        sampler, ["nwalkers", "nsteps", "burn_in", "thin", "init_jitter"], "sampler config"
    )
    _ensure_keys(diagnostics, ["posterior_draws"], "diagnostics config")

    if sampler["nwalkers"] < 2:
        raise ValueError("nwalkers must be >= 2")
    if sampler["nsteps"] <= 0:
        raise ValueError("nsteps must be > 0")
    if sampler["burn_in"] < 0:
        raise ValueError("burn_in must be >= 0")
    if sampler["burn_in"] >= sampler["nsteps"]:
        raise ValueError("burn_in must be less than nsteps")
    if sampler["thin"] <= 0:
        raise ValueError("thin must be > 0")


def validate_parameters_config(config: dict[str, Any]) -> None:
    _ensure_keys(config, ["parameters"], "parameters config")
    params = config["parameters"]
    if not isinstance(params, dict) or not params:
        raise ValueError("parameters config must contain non-empty 'parameters' mapping")

    for name, spec in params.items():
        if not isinstance(spec, dict):
            raise ValueError(f"Parameter spec for {name} must be a mapping")
        _ensure_keys(spec, ["role"], f"parameter '{name}'")
        role = spec["role"]
        if role not in {"fit", "fixed", "derived"}:
            raise ValueError(f"Invalid role '{role}' for parameter '{name}'")
        if role == "fit":
            _ensure_keys(spec, ["initial", "bounds"], f"fit parameter '{name}'")
            bounds = spec["bounds"]
            if not isinstance(bounds, list) or len(bounds) != 2:
                raise ValueError(f"Bounds for '{name}' must be [low, high]")
            low, high = bounds
            if low >= high:
                raise ValueError(f"Bounds invalid for '{name}': low >= high")
        if role == "fixed":
            _ensure_keys(spec, ["value"], f"fixed parameter '{name}'")


def validate_prior_config(
    config: dict[str, Any], known_parameters: set[str], context: str = "prior config"
) -> None:
    _ensure_keys(config, ["priors"], context)
    priors = config["priors"]
    if not isinstance(priors, list):
        raise ValueError(f"{context} 'priors' must be a list")
    for index, prior in enumerate(priors):
        if not isinstance(prior, dict):
            raise ValueError(f"{context} prior[{index}] must be a mapping")
        _ensure_keys(
            prior, ["parameter", "distribution", "mean", "sigma"], f"{context} prior[{index}]"
        )
        parameter = prior["parameter"]
        if parameter not in known_parameters:
            raise ValueError(f"{context} prior[{index}] references unknown parameter '{parameter}'")
        distribution = prior["distribution"]
        if distribution not in {"gaussian", "lognormal"}:
            raise ValueError(
                f"{context} prior[{index}] distribution '{distribution}' is unsupported"
            )
        if prior["sigma"] <= 0:
            raise ValueError(f"{context} prior[{index}] sigma must be > 0")


def validate_compatibility_config(config: dict[str, Any]) -> None:
    _ensure_keys(config, ["thresholds"], "compatibility config")
    thresholds = config["thresholds"]
    if not isinstance(thresholds, dict):
        raise ValueError("compatibility 'thresholds' must be a mapping")
    _ensure_keys(
        thresholds,
        ["green_sigma_max", "amber_sigma_max", "red_p_value_max"],
        "compatibility thresholds",
    )
    green = thresholds["green_sigma_max"]
    amber = thresholds["amber_sigma_max"]
    red_p = thresholds["red_p_value_max"]
    if green <= 0 or amber <= 0:
        raise ValueError("Sigma thresholds must be > 0")
    if green >= amber:
        raise ValueError("green_sigma_max must be < amber_sigma_max")
    if red_p <= 0 or red_p >= 1:
        raise ValueError("red_p_value_max must satisfy 0 < value < 1")


def validate_datasets_config(config: dict[str, Any], project_root: Path) -> None:
    _ensure_keys(config, ["datasets"], "datasets config")
    datasets = config["datasets"]
    if not isinstance(datasets, list) or not datasets:
        raise ValueError("datasets config 'datasets' must be a non-empty list")

    seen_ids: set[str] = set()
    for index, dataset in enumerate(datasets):
        if not isinstance(dataset, dict):
            raise ValueError(f"Dataset[{index}] must be a mapping")
        _ensure_keys(
            dataset,
            [
                "dataset_id",
                "family",
                "enabled",
                "is_non_ladder",
                "data_vector_path",
                "covariance_path",
                "observable_columns",
                "model",
            ],
            f"dataset[{index}]",
        )
        dataset_id = dataset["dataset_id"]
        if dataset_id in seen_ids:
            raise ValueError(f"Duplicate dataset_id: {dataset_id}")
        seen_ids.add(dataset_id)

        family = dataset["family"]
        if family not in {"cmb", "bao", "rsd", "weak_lensing"}:
            raise ValueError(f"Dataset '{dataset_id}' has unsupported family '{family}'")

        if not isinstance(dataset["enabled"], bool):
            raise ValueError(f"Dataset '{dataset_id}' enabled must be boolean")
        if not isinstance(dataset["is_non_ladder"], bool):
            raise ValueError(f"Dataset '{dataset_id}' is_non_ladder must be boolean")
        if dataset["enabled"] and not dataset["is_non_ladder"]:
            raise ValueError(
                f"Dataset '{dataset_id}' is enabled but not marked non-ladder; "
                "core runs require non-ladder data"
            )

        data_path = project_root / dataset["data_vector_path"]
        cov_path = project_root / dataset["covariance_path"]
        if not data_path.exists():
            raise ValueError(f"Dataset '{dataset_id}' data_vector_path missing: {data_path}")
        if not cov_path.exists():
            raise ValueError(f"Dataset '{dataset_id}' covariance_path missing: {cov_path}")

        model = dataset["model"]
        if not isinstance(model, dict):
            raise ValueError(f"Dataset '{dataset_id}' model must be a mapping")
        _ensure_keys(model, ["type", "observables"], f"dataset '{dataset_id}' model")
        if model["type"] != "linear":
            raise ValueError(f"Dataset '{dataset_id}' model.type only supports 'linear' in v1")
        observables = model["observables"]
        if not isinstance(observables, list) or not observables:
            raise ValueError(f"Dataset '{dataset_id}' model.observables must be non-empty list")
        for obs in observables:
            _ensure_keys(obs, ["name", "intercept", "coeffs"], f"dataset '{dataset_id}' observable")
            if not isinstance(obs["coeffs"], dict):
                raise ValueError(f"Dataset '{dataset_id}' observable coeffs must be a mapping")

