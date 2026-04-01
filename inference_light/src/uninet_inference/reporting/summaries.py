from __future__ import annotations

from typing import Any

import numpy as np


def summarize_posterior(samples: np.ndarray, parameter_names: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, name in enumerate(parameter_names):
        values = samples[:, index]
        q2p5, q16, q50, q84, q97p5 = np.percentile(values, [2.5, 16.0, 50.0, 84.0, 97.5])
        rows.append(
            {
                "parameter": name,
                "median": float(q50),
                "p16": float(q16),
                "p84": float(q84),
                "p2p5": float(q2p5),
                "p97p5": float(q97p5),
            }
        )
    return rows

