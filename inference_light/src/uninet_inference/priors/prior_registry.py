from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PriorDefinition:
    parameter: str
    distribution: str
    mean: float
    sigma: float
    source_anchor: str
    family: str


def load_prior_definitions(
    regge_config: dict[str, Any], efe_config: dict[str, Any]
) -> list[PriorDefinition]:
    priors: list[PriorDefinition] = []
    for family, config in [("regge", regge_config), ("efe", efe_config)]:
        for entry in config["priors"]:
            priors.append(
                PriorDefinition(
                    parameter=str(entry["parameter"]),
                    distribution=str(entry["distribution"]),
                    mean=float(entry["mean"]),
                    sigma=float(entry["sigma"]),
                    source_anchor=str(entry.get("source_anchor", "")),
                    family=family,
                )
            )
    return priors


def _gaussian_logpdf(value: float, mean: float, sigma: float) -> float:
    z = (value - mean) / sigma
    return -0.5 * z * z - math.log(sigma) - 0.5 * math.log(2.0 * math.pi)


def _lognormal_logpdf(value: float, mean: float, sigma: float) -> float:
    if value <= 0:
        return float("-inf")
    log_value = math.log(value)
    return _gaussian_logpdf(log_value, mean, sigma) - log_value


def evaluate_log_prior(params: dict[str, float], priors: list[PriorDefinition]) -> float:
    logp = 0.0
    for prior in priors:
        if prior.parameter not in params:
            return float("-inf")
        value = float(params[prior.parameter])
        if prior.distribution == "gaussian":
            contrib = _gaussian_logpdf(value, prior.mean, prior.sigma)
        elif prior.distribution == "lognormal":
            contrib = _lognormal_logpdf(value, prior.mean, prior.sigma)
        else:
            return float("-inf")
        if not math.isfinite(contrib):
            return float("-inf")
        logp += contrib
    return logp

