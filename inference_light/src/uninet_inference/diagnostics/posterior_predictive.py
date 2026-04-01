from __future__ import annotations

from typing import Any

import numpy as np

from uninet_inference.io.dataset_loader import LoadedDataset
from uninet_inference.likelihoods.common import chi2_value
from uninet_inference.likelihoods.joint_likelihood import dataset_prediction
from uninet_inference.model.uninet_param_map import FitParameterSpec, theta_to_param_dict


def _sample_indices(total: int, draws: int, rng: np.random.Generator) -> np.ndarray:
    if draws >= total:
        return np.arange(total, dtype=int)
    return rng.choice(total, size=draws, replace=False)


def compute_posterior_predictive_summary(
    datasets: list[LoadedDataset],
    posterior_samples: np.ndarray,
    fit_specs: list[FitParameterSpec],
    fixed_params: dict[str, float],
    n_draws: int,
    seed: int,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    indices = _sample_indices(posterior_samples.shape[0], n_draws, rng)
    draws = posterior_samples[indices, :]

    median_theta = np.median(posterior_samples, axis=0)
    median_params = theta_to_param_dict(median_theta, fit_specs, fixed_params)

    per_dataset: list[dict[str, Any]] = []
    for dataset in datasets:
        chi2_draws: list[float] = []
        for theta in draws:
            params = theta_to_param_dict(theta, fit_specs, fixed_params)
            pred = dataset_prediction(dataset, params)
            chi2_draws.append(chi2_value(dataset.observed, pred, dataset.covariance))

        pred_median = dataset_prediction(dataset, median_params)
        chi2_median = chi2_value(dataset.observed, pred_median, dataset.covariance)
        chi2_draw_array = np.asarray(chi2_draws, dtype=float)
        p_value = float(np.mean(chi2_draw_array >= chi2_median))

        per_dataset.append(
            {
                "dataset_id": dataset.dataset_id,
                "family": dataset.family,
                "chi2_median": float(chi2_median),
                "dof": int(dataset.observed.shape[0]),
                "chi2_draw_mean": float(np.mean(chi2_draw_array)),
                "chi2_draw_std": float(np.std(chi2_draw_array)),
                "posterior_predictive_p_value": p_value,
            }
        )

    return {"datasets": per_dataset}

