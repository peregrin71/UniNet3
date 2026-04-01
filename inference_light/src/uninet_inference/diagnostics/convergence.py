from __future__ import annotations

from typing import Any

import numpy as np


def summarize_convergence(chain: np.ndarray, acceptance_fraction: np.ndarray) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "acceptance_fraction_mean": float(np.mean(acceptance_fraction)),
        "acceptance_fraction_min": float(np.min(acceptance_fraction)),
        "acceptance_fraction_max": float(np.max(acceptance_fraction)),
        "nsteps": int(chain.shape[0]),
        "nwalkers": int(chain.shape[1]),
        "ndim": int(chain.shape[2]),
    }

    # Simple split-chain drift indicator for compatibility-first runs.
    midpoint = chain.shape[0] // 2
    early = chain[:midpoint, :, :].mean(axis=(0, 1))
    late = chain[midpoint:, :, :].mean(axis=(0, 1))
    drift = np.abs(late - early)
    summary["split_mean_abs_drift"] = drift.tolist()
    summary["split_mean_abs_drift_max"] = float(np.max(drift))
    return summary

