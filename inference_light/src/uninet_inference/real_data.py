from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from uninet_inference.io.schema_validation import load_yaml_file
from uninet_inference.pipeline import run_pipeline


@dataclass
class ProcessedDatasetResult:
    dataset_id: str
    vector_out: str
    covariance_out: str
    source_vector: str
    source_covariance: str
    n_observables: int


def _normalize_covariance(covariance: np.ndarray) -> np.ndarray:
    if covariance.ndim == 0:
        covariance = covariance.reshape(1, 1)
    elif covariance.ndim == 1:
        covariance = np.diag(covariance)
    if covariance.shape[0] != covariance.shape[1]:
        raise ValueError(f"Covariance must be square, got shape {covariance.shape}")
    return covariance


def _read_vector_csv(path: Path) -> tuple[list[str], np.ndarray]:
    names: list[str] = []
    values: list[float] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"Vector CSV has no header: {path}")
        required = {"observable", "value"}
        if not required.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"Vector CSV must include columns {sorted(required)}, got {reader.fieldnames}: {path}"
            )
        for row in reader:
            names.append(str(row["observable"]).strip())
            values.append(float(row["value"]))
    if not names:
        raise ValueError(f"Vector CSV is empty: {path}")
    return names, np.asarray(values, dtype=float)


def _load_covariance(path: Path) -> np.ndarray:
    covariance = np.loadtxt(path, delimiter=",", dtype=float)
    return _normalize_covariance(np.asarray(covariance, dtype=float))


def _find_first_existing(project_root: Path, candidates: list[str], label: str) -> Path:
    for item in candidates:
        candidate = project_root / item
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"No existing {label} file found. Tried: {', '.join(candidates)}"
    )


def _canonicalize_name(value: str) -> str:
    return value.strip().lower()


def _apply_name_map(names: list[str], name_map: dict[str, str]) -> list[str]:
    mapped: list[str] = []
    normalized_map = {_canonicalize_name(k): v for k, v in name_map.items()}
    for name in names:
        mapped.append(normalized_map.get(_canonicalize_name(name), name))
    return mapped


def _subset_to_expected(
    observed_names: list[str],
    observed_values: np.ndarray,
    covariance: np.ndarray,
    expected_names: list[str],
) -> tuple[list[str], np.ndarray, np.ndarray]:
    name_to_index = {_canonicalize_name(name): index for index, name in enumerate(observed_names)}

    indices: list[int] = []
    missing: list[str] = []
    for expected in expected_names:
        key = _canonicalize_name(expected)
        if key not in name_to_index:
            missing.append(expected)
            continue
        indices.append(name_to_index[key])

    if missing:
        raise ValueError(
            "Missing required observables in source vector: "
            f"{missing}. Available: {observed_names}. "
            "Update configs/real_data_sources.yaml observable_name_map or provide a source "
            "vector containing all model observables."
        )

    selected_values = observed_values[indices]
    selected_cov = covariance[np.ix_(indices, indices)]
    selected_names = [expected_names[i] for i in range(len(expected_names))]
    return selected_names, selected_values, selected_cov


def _write_vector_csv(path: Path, names: list[str], values: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["observable", "value"])
        for name, value in zip(names, values.tolist()):
            writer.writerow([name, f"{float(value):.16g}"])


def _write_covariance_csv(path: Path, covariance: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(path, covariance, delimiter=",", fmt="%.16g")


def _load_dataset_config(project_root: Path) -> dict[str, Any]:
    datasets_cfg = load_yaml_file(project_root / "configs" / "datasets.yaml")
    dataset_map = {item["dataset_id"]: item for item in datasets_cfg["datasets"]}
    return {"raw": datasets_cfg, "map": dataset_map}


def _load_source_config(project_root: Path, config_path: Path) -> dict[str, Any]:
    loaded = load_yaml_file(config_path)
    if "datasets" not in loaded or not isinstance(loaded["datasets"], dict):
        raise ValueError(
            f"real data source config must include a mapping at 'datasets': {config_path}"
        )
    return loaded


def preprocess_real_data(
    project_root: Path,
    source_config_path: Path,
    dataset_ids: list[str] | None = None,
) -> list[ProcessedDatasetResult]:
    dataset_config = _load_dataset_config(project_root)
    dataset_map: dict[str, dict[str, Any]] = dataset_config["map"]
    source_config = _load_source_config(project_root, source_config_path)

    selected_ids = dataset_ids if dataset_ids else list(source_config["datasets"].keys())
    results: list[ProcessedDatasetResult] = []

    for dataset_id in selected_ids:
        if dataset_id not in dataset_map:
            raise ValueError(f"Unknown dataset_id in datasets.yaml: {dataset_id}")
        if dataset_id not in source_config["datasets"]:
            raise ValueError(
                f"Missing dataset_id '{dataset_id}' in source config: {source_config_path}"
            )

        dataset_cfg = dataset_map[dataset_id]
        source_cfg = source_config["datasets"][dataset_id]

        vector_candidates = source_cfg.get("vector_path_candidates", [])
        covariance_candidates = source_cfg.get("covariance_path_candidates", [])
        if not vector_candidates or not covariance_candidates:
            raise ValueError(
                f"Dataset '{dataset_id}' requires vector_path_candidates and "
                f"covariance_path_candidates in {source_config_path}"
            )

        source_vector = _find_first_existing(project_root, vector_candidates, "vector")
        source_cov = _find_first_existing(project_root, covariance_candidates, "covariance")

        observed_names, observed_values = _read_vector_csv(source_vector)
        covariance = _load_covariance(source_cov)

        if covariance.shape[0] != len(observed_names):
            raise ValueError(
                f"Dataset '{dataset_id}' source covariance shape {covariance.shape} "
                f"does not match source vector length {len(observed_names)}"
            )

        name_map = source_cfg.get("observable_name_map", {})
        if not isinstance(name_map, dict):
            raise ValueError(f"Dataset '{dataset_id}' observable_name_map must be a mapping")

        mapped_names = _apply_name_map(observed_names, name_map)
        expected_names = [item["name"] for item in dataset_cfg["model"]["observables"]]

        final_names, final_values, final_cov = _subset_to_expected(
            observed_names=mapped_names,
            observed_values=observed_values,
            covariance=covariance,
            expected_names=expected_names,
        )

        vector_out = project_root / dataset_cfg["data_vector_path"]
        covariance_out = project_root / dataset_cfg["covariance_path"]
        _write_vector_csv(vector_out, final_names, final_values)
        _write_covariance_csv(covariance_out, final_cov)

        results.append(
            ProcessedDatasetResult(
                dataset_id=dataset_id,
                vector_out=str(vector_out),
                covariance_out=str(covariance_out),
                source_vector=str(source_vector),
                source_covariance=str(source_cov),
                n_observables=len(final_names),
            )
        )

    return results


def set_datasets_enabled(
    project_root: Path,
    dataset_ids: list[str],
    enabled: bool = True,
    disable_others: bool = False,
) -> None:
    datasets_path = project_root / "configs" / "datasets.yaml"
    datasets_cfg = load_yaml_file(datasets_path)

    targets = set(dataset_ids)
    for item in datasets_cfg["datasets"]:
        if item["dataset_id"] in targets:
            item["enabled"] = bool(enabled)
        elif disable_others:
            item["enabled"] = not bool(enabled)

    with datasets_path.open("w", encoding="utf-8", newline="") as handle:
        yaml.safe_dump(datasets_cfg, handle, sort_keys=False)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preprocess real dataset files into InferenceLight processed CSV format"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root containing configs/, data/, src/, and runs/.",
    )
    parser.add_argument(
        "--source-config",
        type=Path,
        default=Path("configs/real_data_sources.yaml"),
        help="Path to real-data source mapping YAML.",
    )
    parser.add_argument(
        "--dataset-id",
        action="append",
        default=None,
        help="Optional dataset_id to preprocess (repeatable). Defaults to all datasets in source config.",
    )
    parser.add_argument(
        "--enable-datasets",
        action="store_true",
        help="Set enabled=true for processed datasets in configs/datasets.yaml.",
    )
    parser.add_argument(
        "--disable-other-datasets",
        action="store_true",
        help="When enabling datasets, set enabled=false for all datasets not processed in this run.",
    )
    parser.add_argument(
        "--run-pipeline",
        action="store_true",
        help="Run pipeline immediately after preprocessing.",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default=None,
        help="Optional run id override if --run-pipeline is used.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    project_root = args.root.resolve()
    source_config = args.source_config
    if not source_config.is_absolute():
        source_config = project_root / source_config

    processed = preprocess_real_data(
        project_root=project_root,
        source_config_path=source_config,
        dataset_ids=args.dataset_id,
    )

    dataset_ids = [item.dataset_id for item in processed]
    if args.enable_datasets and dataset_ids:
        set_datasets_enabled(
            project_root,
            dataset_ids,
            enabled=True,
            disable_others=bool(args.disable_other_datasets),
        )

    payload: dict[str, Any] = {
        "processed": [item.__dict__ for item in processed],
        "enabled_datasets": dataset_ids if args.enable_datasets else [],
    }

    if args.run_pipeline:
        payload["pipeline_result"] = run_pipeline(
            project_root=project_root,
            run_id_override=args.run_id,
        )

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
