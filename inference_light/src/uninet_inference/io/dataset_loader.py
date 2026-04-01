from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


@dataclass(frozen=True)
class LoadedDataset:
    dataset_id: str
    family: str
    observable_names: list[str]
    observed: np.ndarray
    covariance: np.ndarray
    model: dict[str, Any]
    source_url: str
    version_tag: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_vector_csv(path: Path, expected_columns: list[str]) -> tuple[list[str], np.ndarray]:
    if len(expected_columns) < 2:
        raise ValueError("observable_columns must include at least [observable, value]")

    observable_col = expected_columns[0]
    value_col = expected_columns[1]
    names: list[str] = []
    values: list[float] = []

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"Data vector has no header: {path}")
        missing = [col for col in [observable_col, value_col] if col not in reader.fieldnames]
        if missing:
            raise ValueError(f"Data vector missing columns {missing}: {path}")
        for row in reader:
            names.append(str(row[observable_col]).strip())
            values.append(float(row[value_col]))

    if not names:
        raise ValueError(f"Data vector is empty: {path}")
    return names, np.asarray(values, dtype=float)


def _load_covariance(path: Path) -> np.ndarray:
    covariance = np.loadtxt(path, delimiter=",", dtype=float)
    if covariance.ndim == 0:
        covariance = covariance.reshape(1, 1)
    elif covariance.ndim == 1:
        covariance = np.diag(covariance)
    if covariance.shape[0] != covariance.shape[1]:
        raise ValueError(f"Covariance must be square: {path} got shape {covariance.shape}")
    return covariance


def load_enabled_datasets(
    datasets_config: dict[str, Any], project_root: Path
) -> tuple[list[LoadedDataset], dict[str, Any]]:
    loaded: list[LoadedDataset] = []
    manifest_items: list[dict[str, Any]] = []

    for dataset in datasets_config["datasets"]:
        if not dataset["enabled"]:
            continue

        dataset_id = dataset["dataset_id"]
        data_path = project_root / dataset["data_vector_path"]
        covariance_path = project_root / dataset["covariance_path"]

        observable_names, observed = _load_vector_csv(data_path, dataset["observable_columns"])
        covariance = _load_covariance(covariance_path)
        if covariance.shape[0] != observed.shape[0]:
            raise ValueError(
                f"Dataset '{dataset_id}' covariance size {covariance.shape} does not match "
                f"observed vector length {observed.shape[0]}"
            )

        loaded.append(
            LoadedDataset(
                dataset_id=dataset_id,
                family=dataset["family"],
                observable_names=observable_names,
                observed=observed,
                covariance=covariance,
                model=dataset["model"],
                source_url=dataset.get("source_url", ""),
                version_tag=dataset.get("version_tag", ""),
            )
        )

        manifest_items.append(
            {
                "dataset_id": dataset_id,
                "family": dataset["family"],
                "data_vector_path": str(data_path),
                "data_vector_sha256": sha256_file(data_path),
                "covariance_path": str(covariance_path),
                "covariance_sha256": sha256_file(covariance_path),
                "source_url": dataset.get("source_url", ""),
                "version_tag": dataset.get("version_tag", ""),
                "is_non_ladder": bool(dataset["is_non_ladder"]),
            }
        )

    if not loaded:
        raise ValueError("No enabled datasets were loaded")

    manifest = {"datasets": manifest_items}
    return loaded, manifest

