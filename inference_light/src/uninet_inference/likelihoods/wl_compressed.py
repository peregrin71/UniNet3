from __future__ import annotations

import numpy as np

from .common import gaussian_loglike


def loglike(observed: np.ndarray, predicted: np.ndarray, covariance: np.ndarray) -> float:
    return gaussian_loglike(observed, predicted, covariance)

