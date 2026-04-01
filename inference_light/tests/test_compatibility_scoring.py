from __future__ import annotations

from uninet_inference.diagnostics.compatibility_scoring import (
    CompatibilityThresholds,
    score_compatibility,
)


def test_compatibility_classes_cover_green_amber_red() -> None:
    thresholds = CompatibilityThresholds(
        green_sigma_max=1.8, amber_sigma_max=3.0, red_p_value_max=0.01
    )

    payload = {
        "datasets": [
            {
                "dataset_id": "d1",
                "family": "cmb",
                "chi2_median": 1.0,
                "dof": 1,
                "posterior_predictive_p_value": 0.5,
            },
            {
                "dataset_id": "d2",
                "family": "bao",
                "chi2_median": 8.0,
                "dof": 3,
                "posterior_predictive_p_value": 0.2,
            },
            {
                "dataset_id": "d3",
                "family": "rsd",
                "chi2_median": 25.0,
                "dof": 2,
                "posterior_predictive_p_value": 0.001,
            },
        ]
    }

    scored = score_compatibility(payload, thresholds)
    classes = {item["dataset_id"]: item["compatibility_class"] for item in scored["datasets"]}
    assert classes["d1"] == "green"
    assert classes["d2"] == "amber"
    assert classes["d3"] == "red"
    assert scored["traffic_light"] == "Red"
    assert scored["fits_known_physics_at_all"] is False

