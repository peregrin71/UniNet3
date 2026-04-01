from __future__ import annotations

from pathlib import Path

from uninet_inference.pipeline import run_pipeline


def test_pipeline_smoke_outputs_exist() -> None:
    project_root = Path(__file__).resolve().parents[1]
    run_id = "pytest-smoke"

    result = run_pipeline(
        project_root=project_root,
        run_id_override=run_id,
        run_config_overrides={
            "sampler": {
                "nwalkers": 16,
                "nsteps": 60,
                "burn_in": 20,
                "thin": 2,
                "init_jitter": 0.04,
            },
            "diagnostics": {"posterior_draws": 60},
        },
    )
    reports_dir = Path(result["reports_dir"])

    assert (reports_dir / "results.md").exists()
    assert (reports_dir / "compatibility.json").exists()
    assert (reports_dir / "posterior_summary.csv").exists()
