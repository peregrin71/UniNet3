# InferenceLight User Manual

This is a small practical guide for running the pipeline safely and predictably.

## 1. What Happens by Default

1. No real datasets are downloaded automatically.
2. `download_data_stub.bat` and `download_data_stub.sh` do not fetch data.
3. The bundled `data/raw/*` files are local sample inputs for bring-up only.

## 2. Recommended Workflow (Windows)

1. Review data plan separately:
   - `scripts\download_data_stub.bat`
   - Then read `download_manifest.md`
2. Create environment:
   - `scripts\bootstrap_venv.bat`
3. Run pipeline:
   - `scripts\run_pipeline.bat`
4. Optional tests:
   - `scripts\run_tests.bat`

## 3. Recommended Workflow (Linux)

1. Review data plan separately:
   - `bash scripts/download_data_stub.sh`
   - Then read `download_manifest.md`
2. Create environment:
   - `bash scripts/bootstrap_venv.sh`
3. Run pipeline:
   - `bash scripts/run_pipeline.sh`
4. Optional tests:
   - `bash scripts/run_tests.sh`

## 4. Outputs

Each run writes to `runs/<run_id>/` with:

1. `01_ingest/manifest.json`
2. `02_priors/prior_snapshot.json`
3. `03_sampling/chains.h5`
4. `04_diagnostics/diagnostics.json`
5. `05_reports/results.md`
6. `05_reports/compatibility.json`
7. `05_reports/posterior_summary.csv`

## 5. Using Real Data Later

When you decide to move from sample inputs to real datasets:

1. Use `download_manifest.md` as the source list.
2. Download manually to `data/raw/<family>/...`.
3. Record source/version/checksum metadata.
4. Update `configs/datasets.yaml` paths to the real files.
5. Re-run the pipeline.

## 6. Common Notes

1. This project is BAT-first on Windows.
2. `.venv` and `runs/*` are ignored by git via `.gitignore`.
3. If `run_pipeline` says `.venv` is missing, run `bootstrap_venv` first.

