from __future__ import annotations

from typing import Any

import numpy as np


def predict_linear_observables(
    model: dict[str, Any], observable_names: list[str], params: dict[str, float]
) -> np.ndarray:
    if model["type"] != "linear":
        raise ValueError(f"Unsupported model type '{model['type']}'")

    rules = {entry["name"]: entry for entry in model["observables"]}
    predictions: list[float] = []

    for observable in observable_names:
        if observable not in rules:
            raise ValueError(f"Missing model definition for observable '{observable}'")
        rule = rules[observable]
        value = float(rule["intercept"])
        for param_name, coefficient in rule["coeffs"].items():
            if param_name not in params:
                raise ValueError(f"Parameter '{param_name}' missing for observable '{observable}'")
            value += float(coefficient) * float(params[param_name])
        predictions.append(value)

    return np.asarray(predictions, dtype=float)

