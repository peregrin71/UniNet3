from __future__ import annotations

import math

import numpy as np


def gaussian_loglike(observed: np.ndarray, predicted: np.ndarray, covariance: np.ndarray) -> float:
    residual = observed - predicted
    inv_covariance = np.linalg.inv(covariance)
    chi2 = float(residual.T @ inv_covariance @ residual)
    sign, logdet = np.linalg.slogdet(covariance)
    if sign <= 0:
        raise ValueError("Covariance matrix must be positive definite")
    n = observed.shape[0]
    return -0.5 * (chi2 + logdet + n * math.log(2.0 * math.pi))


def chi2_value(observed: np.ndarray, predicted: np.ndarray, covariance: np.ndarray) -> float:
    residual = observed - predicted
    inv_covariance = np.linalg.inv(covariance)
    return float(residual.T @ inv_covariance @ residual)

