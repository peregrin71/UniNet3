from __future__ import annotations

from typing import Any, Callable

import numpy as np

from uninet_inference.io.dataset_loader import LoadedDataset
from uninet_inference.model.observable_map import predict_linear_observables

from . import bao_compressed, cmb_compressed, rsd_compressed, wl_compressed
from .common import chi2_value

_LOG_LIKE_BY_FAMILY: dict[str, Callable[[np.ndarray, np.ndarray, np.ndarray], float]] = {
    "cmb": cmb_compressed.loglike,
    "bao": bao_compressed.loglike,
    "rsd": rsd_compressed.loglike,
    "weak_lensing": wl_compressed.loglike,
}


def dataset_prediction(dataset: LoadedDataset, params: dict[str, float]) -> np.ndarray:
    return predict_linear_observables(dataset.model, dataset.observable_names, params)


def dataset_statistics(dataset: LoadedDataset, params: dict[str, float]) -> dict[str, Any]:
    predicted = dataset_prediction(dataset, params)
    chi2 = chi2_value(dataset.observed, predicted, dataset.covariance)
    dof = dataset.observed.shape[0]
    residual = (dataset.observed - predicted).tolist()
    return {
        "dataset_id": dataset.dataset_id,
        "family": dataset.family,
        "chi2": float(chi2),
        "dof": int(dof),
        "residual": residual,
        "predicted": predicted.tolist(),
        "observed": dataset.observed.tolist(),
    }


def log_likelihood_for_dataset(dataset: LoadedDataset, params: dict[str, float]) -> float:
    prediction = dataset_prediction(dataset, params)
    func = _LOG_LIKE_BY_FAMILY[dataset.family]
    return float(func(dataset.observed, prediction, dataset.covariance))


def total_log_likelihood(datasets: list[LoadedDataset], params: dict[str, float]) -> float:
    return float(sum(log_likelihood_for_dataset(dataset, params) for dataset in datasets))

