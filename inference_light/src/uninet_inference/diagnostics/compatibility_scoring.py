from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CompatibilityThresholds:
    green_sigma_max: float
    amber_sigma_max: float
    red_p_value_max: float


def _sigma_equivalent(chi2: float, dof: int) -> float:
    if dof <= 0:
        return 0.0
    # Chi-square normal approximation.
    return abs(chi2 - dof) / math.sqrt(2.0 * dof)


def _class_rank(label: str) -> int:
    return {"green": 0, "amber": 1, "red": 2}[label]


def classify_dataset(chi2: float, dof: int, p_value: float, thresholds: CompatibilityThresholds) -> dict[str, Any]:
    sigma_equiv = _sigma_equivalent(chi2, dof)

    if sigma_equiv > thresholds.amber_sigma_max or p_value < thresholds.red_p_value_max:
        label = "red"
    elif sigma_equiv > thresholds.green_sigma_max:
        label = "amber"
    else:
        label = "green"

    return {
        "sigma_equivalent": float(sigma_equiv),
        "compatibility_class": label,
    }


def score_compatibility(
    posterior_predictive: dict[str, Any], thresholds: CompatibilityThresholds
) -> dict[str, Any]:
    per_dataset: list[dict[str, Any]] = []

    worst_label = "green"
    for item in posterior_predictive["datasets"]:
        classified = classify_dataset(
            chi2=float(item["chi2_median"]),
            dof=int(item["dof"]),
            p_value=float(item["posterior_predictive_p_value"]),
            thresholds=thresholds,
        )
        merged = dict(item)
        merged.update(classified)
        per_dataset.append(merged)
        if _class_rank(merged["compatibility_class"]) > _class_rank(worst_label):
            worst_label = merged["compatibility_class"]

    traffic_map = {"green": "Green", "amber": "Amber", "red": "Red"}
    traffic_light = traffic_map[worst_label]
    fits_known_physics = worst_label != "red"

    return {
        "datasets": per_dataset,
        "traffic_light": traffic_light,
        "fits_known_physics_at_all": fits_known_physics,
    }

