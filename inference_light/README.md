# InferenceLight

Compatibility-first Bayesian inference pipeline for UniNet.

See the full quick manual: `USER_MANUAL.md`.

## Quick Start

Windows:

1. `scripts\\bootstrap_venv.bat`
2. `scripts\\run_pipeline.bat`

Linux:

1. `bash scripts/bootstrap_venv.sh`
2. `bash scripts/run_pipeline.sh`

## Real Data Automation

When real raw files are present under `data/raw/...`, you can automate preprocessing + run:

Windows:

1. `scripts\\bootstrap_venv.bat`
2. `scripts\\run_pipeline_real.bat`

Linux:

1. `bash scripts/bootstrap_venv.sh`
2. `bash scripts/run_pipeline_real.sh`

The source-to-processed mapping is configured in `configs/real_data_sources.yaml`.
Use `scripts\\preprocess_real_data.bat --enable-datasets` (or `.sh`) if you want preprocessing only.

## Notes

1. This project is BAT-first by design.
2. The default bundled inputs are local sample data for pipeline bring-up.
3. Real data download and real production tests are intentionally separate steps.
4. Run `scripts\\download_data_stub.bat` (or `.sh`) separately to review the manual data plan.
