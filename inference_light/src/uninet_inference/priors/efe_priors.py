from __future__ import annotations

from typing import Any


def describe_efe_prior_set(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [dict(item) for item in config.get("priors", [])]

