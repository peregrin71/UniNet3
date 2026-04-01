from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass(frozen=True)
class FitParameterSpec:
    name: str
    initial: float
    low: float
    high: float


def split_parameter_roles(
    parameter_config: dict[str, Any],
) -> tuple[list[FitParameterSpec], dict[str, float], dict[str, Any]]:
    fit_specs: list[FitParameterSpec] = []
    fixed_params: dict[str, float] = {}
    derived_params: dict[str, Any] = {}

    for name, spec in parameter_config["parameters"].items():
        role = spec["role"]
        if role == "fit":
            low, high = float(spec["bounds"][0]), float(spec["bounds"][1])
            fit_specs.append(
                FitParameterSpec(
                    name=name,
                    initial=float(spec["initial"]),
                    low=low,
                    high=high,
                )
            )
        elif role == "fixed":
            fixed_params[name] = float(spec["value"])
        else:
            derived_params[name] = spec

    if not fit_specs:
        raise ValueError("No fit parameters found")

    return fit_specs, fixed_params, derived_params


def theta_within_bounds(theta: np.ndarray, fit_specs: list[FitParameterSpec]) -> bool:
    for value, spec in zip(theta, fit_specs):
        if value < spec.low or value > spec.high:
            return False
    return True


def initial_center(fit_specs: list[FitParameterSpec]) -> np.ndarray:
    return np.asarray([spec.initial for spec in fit_specs], dtype=float)


def theta_to_param_dict(
    theta: np.ndarray, fit_specs: list[FitParameterSpec], fixed_params: dict[str, float]
) -> dict[str, float]:
    params = dict(fixed_params)
    for value, spec in zip(theta, fit_specs):
        params[spec.name] = float(value)
    return params

