# InferenceLight TODO

Date: 2026-04-01

## Next Steps (Resume Checklist)

1. Preprocess real datasets to CSV into `data/processed/...` as documented in `InferenceLightPipelineDesign.md` (Section 13):
   - `cmb/planck_pr3_compressed_vector.csv`
   - `cmb/planck_pr3_compressed_cov.csv`
   - `bao/desi_dr1_bao_gccomb_vector.csv`
   - `bao/desi_dr1_bao_gccomb_cov.csv`
   - `rsd/desi_dr1_rsd_fsigma8_vector.csv`
   - `rsd/desi_dr1_rsd_fsigma8_cov.csv`
   - `weak_lensing/kids1000_s8_vector.csv`
   - `weak_lensing/kids1000_s8_cov.csv`

2. Update `configs/datasets.yaml`:
   - set selected datasets from `enabled: false` to `enabled: true`
   - keep `is_non_ladder: true`
   - ensure observable names in vectors match `model.observables[].name`

3. Run pipeline:
   - Windows: `scripts\bootstrap_venv.bat` then `scripts\run_pipeline.bat`
   - Linux: `bash scripts/bootstrap_venv.sh` then `bash scripts/run_pipeline.sh`

4. Verify outputs in `runs/<run_id>/05_reports/`:
   - `results.md`
   - `compatibility.json`
   - `posterior_summary.csv`

5. Optional tests:
   - Windows: `scripts\run_tests.bat`
   - Linux: `bash scripts/run_tests.sh`

6. Commit and push current pending updates:
   - `git add inference_light`
   - `git commit -m "Update real-run dataset template and preprocessing guide"`
   - `git push`

