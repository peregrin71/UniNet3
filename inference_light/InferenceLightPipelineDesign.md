# InferenceLight Pipeline Design

Date: 2026-04-01  
Location: `C:\SB\uninet3\inference_light`  
Primary objective: compatibility-first Bayesian inference for UniNet against known non-cosmic-ladder physics.

## 1. Scope and Decision Goal

### 1.1 Goal

Build a Python inference pipeline that answers:

1. Can the current UniNet model fit known physics datasets at all?
2. What posterior parameter ranges are compatible with those datasets?
3. How strong is the compatibility (clear traffic-light verdict)?

### 1.2 Non-goals (v1)

1. Precision-grade final cosmology (full Planck-style precision stack is not required in v1).
2. Cosmic distance ladder calibration datasets as core fit inputs.
3. Large production-scale optimization.

### 1.3 Design constraints locked

1. Python implementation.
2. Self-contained local virtual environment (`.venv`).
3. Windows launch scripts as `.bat` (no PowerShell runtime requirement).
4. Optional Linux `.sh` scripts in parity with `.bat`.
5. Human-readable `results.md` is mandatory output.

## 2. High-Level Architecture

Pipeline style: staged, file-based, reproducible runs.

Stages:

1. Ingest and validate dataset files.
2. Build priors (Regge-informed + GR EFE-informed).
3. Run Bayesian sampling (`emcee`).
4. Compute diagnostics and posterior predictive compatibility.
5. Produce machine and human outputs (`compatibility.json`, `posterior_summary.csv`, `results.md`).

Core principle:

1. Prefer robust compatibility evidence over maximal statistical sophistication.

## 3. Folder Structure

```text
inference_light/
  InferenceLightPipelineDesign.md
  .venv/                                  # local virtual environment (not committed)
  requirements.in
  requirements-windows.lock
  requirements-linux.lock
  .gitignore

  configs/
    run.yaml
    datasets.yaml
    parameters.yaml
    priors_regge.yaml
    priors_efe.yaml
    compatibility.yaml

  data/
    raw/
      cmb/
      bao/
      rsd/
      weak_lensing/
    processed/

  src/
    uninet_inference/
      io/
        dataset_loader.py
        schema_validation.py
      model/
        uninet_param_map.py
        observable_map.py
      priors/
        regge_priors.py
        efe_priors.py
        prior_registry.py
      likelihoods/
        cmb_compressed.py
        bao_compressed.py
        rsd_compressed.py
        wl_compressed.py
        joint_likelihood.py
      sampling/
        emcee_runner.py
        chain_io.py
      diagnostics/
        convergence.py
        posterior_predictive.py
        compatibility_scoring.py
      reporting/
        results_markdown.py
        summaries.py

  scripts/
    bootstrap_venv.bat
    run_pipeline.bat
    run_tests.bat
    bootstrap_venv.sh
    run_pipeline.sh
    run_tests.sh

  runs/
    <run_id>/
      01_ingest/
      02_priors/
      03_sampling/
      04_diagnostics/
      05_reports/
        results.md
        compatibility.json
        posterior_summary.csv
```

## 4. Input Data and Data Contracts

## 4.1 Core dataset families (non-ladder)

1. CMB compressed likelihood inputs.
2. BAO distance-summary inputs.
3. RSD growth-summary or full-shape compressed inputs.
4. Weak-lensing summary inputs (e.g., KiDS/DES released vectors and covariances).

## 4.2 Required per-dataset assets

1. Data vector file.
2. Covariance matrix file.
3. Metadata (observable definitions, redshift bins, units).
4. Provenance (`source_url`, `version`, `downloaded_at`, `license`).

## 4.3 Schema keys in `datasets.yaml`

1. `dataset_id`
2. `family` (`cmb|bao|rsd|weak_lensing`)
3. `enabled`
4. `data_vector_path`
5. `covariance_path`
6. `observable_columns`
7. `unit_convention`
8. `source_url`
9. `version_tag`
10. `is_non_ladder` (must be `true` for core set)

## 5. Parameters and Bayesian Priors

## 5.1 Parameter roles

From UniNet parameter governance:

1. `fit`: inferred by sampler.
2. `fixed`: constants/locked choices.
3. `derived`: computed from fit/fixed.

## 5.2 Initial fit basis (v1, compatibility-oriented)

Primary cosmology-facing UniNet parameters:

1. `tau_relax`
2. `lambda_DM`
3. `A_cong`
4. `Phi_ratio` (or `N_e` reparameterized)
5. `chi_parity`

Optional extension block (switchable in config):

1. `alpha`, `beta`, `xi_leak`
2. transfer parameters needed for linked parity/CP channel tests

## 5.3 Priors policy

1. Regge-informed priors: soft informative priors on allowed model ratios/scales.
2. GR EFE-informed priors: soft informative priors for EFE-consistent branches.
3. Hard physical bounds still apply as feasibility limits.
4. Priors are declared in config, not hard-coded.

## 6. Inference and Compatibility Logic

## 6.1 Sampler

1. `emcee` backend.
2. Fixed seed support.
3. Parallel walkers configured in `run.yaml`.

## 6.2 Compatibility metrics

Per dataset family:

1. Best-fit residual and normalized chi-square class statistic.
2. Posterior predictive p-value class statistic.
3. Tension score vs internal null baseline.

Global:

1. Aggregated compatibility score.
2. Worst-dataset tension guardrail.

## 6.3 Final decision rule

Traffic-light:

1. `Green`: no severe tension; broad compatibility.
2. `Amber`: moderate tension but not decisive failure.
3. `Red`: decisive incompatibility.

Boolean headline:

1. `fits_known_physics_at_all = true` for `Green` or `Amber`.
2. `fits_known_physics_at_all = false` for `Red`.

## 7. Outputs and Intermediate Artifacts

## 7.1 Intermediate outputs

1. `01_ingest/manifest.json`: exact datasets used and hashes.
2. `02_priors/prior_snapshot.json`: prior definitions frozen for run.
3. `03_sampling/chains.h5`: raw samples.
4. `04_diagnostics/diagnostics.json`: convergence + predictive checks.

## 7.2 Final outputs

1. `posterior_summary.csv`: median, 68%, 95% intervals.
2. `compatibility.json`: per-dataset and overall verdict fields.
3. `results.md`: decision-facing narrative summary.

## 8. Mandatory `results.md` Layout

The generated `results.md` must contain:

1. Run metadata (`run_id`, seed, timestamp, software versions).
2. Dataset manifest and versions.
3. Prior summary (Regge and EFE prior settings actually used).
4. Parameter ranges table:
   - parameter
   - posterior median
   - 68% interval
   - 95% interval
5. Per-dataset compatibility table:
   - dataset id
   - statistic summary
   - tension class
   - pass/fail contribution
6. Final section:
   - `traffic_light`
   - `fits_known_physics_at_all`
   - concise interpretation paragraph.

## 9. Script Policy (BAT-first, Bash optional)

## 9.1 Windows

1. `bootstrap_venv.bat`:
   - create `.venv`
   - install from `requirements-windows.lock`
2. `run_pipeline.bat`:
   - run end-to-end with explicit `.venv\Scripts\python.exe`
3. `run_tests.bat`:
   - execute tests in `.venv`

## 9.2 Linux

1. `bootstrap_venv.sh`:
   - create `.venv`
   - install from `requirements-linux.lock`
2. `run_pipeline.sh`
3. `run_tests.sh`

## 10. Verified Downloadable Dataset Endpoints (2026-04-01)

Verification method:

1. Confirmed public documentation pages.
2. Confirmed direct public directory listings where available.
3. Confirmed direct downloadable file URLs where available.

## 10.1 CMB

1. ACT DR6 lensing likelihood bundle:
   - Product page: `https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_lh_info.html`
   - Download page: `https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_lh_get.html`
   - File URL: `https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/likelihood/data/ACT_dr6_likelihood_v1.2.tgz`
2. Planck baseline likelihood package (documented install path):
   - Cobaya Planck likelihood docs: `https://cobaya.readthedocs.io/en/cosmo_package/likelihood_planck.html`
   - Example PLA download endpoint used in docs: `https://pla.esac.esa.int/pla-sl/data-action?COSMOLOGY.COSMOLOGY_OID=151912`
   - Baseline package name referenced by docs: `COM_Likelihood_Data-baseline_R3.00.tar.gz`

## 10.2 BAO

1. DESI DR1 BAO cosmology VAC:
   - Documentation page: `https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/`
   - Public directory listing (confirmed): `https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params/`
   - Version directory (confirmed): `https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params/v1.0/`
2. DESI/SDSS BAO text files for Cobaya:
   - Repo: `https://github.com/CobayaSampler/bao_data`
   - Example direct raw file (confirmed): `https://raw.githubusercontent.com/CobayaSampler/bao_data/refs/heads/master/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt`

## 10.3 RSD / Full-shape growth

1. DESI DR1 full-shape + BAO clustering products:
   - Documentation page: `https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/`
   - Public directory listing (confirmed): `https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/`
   - Version directory (confirmed): `https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/v1.0/`
   - Inference-ready subdir (confirmed): `https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/v1.0/data/`

## 10.4 Weak lensing

1. KiDS-1000 weak-lensing release pages:
   - Landing page: `https://kids.strw.leidenuniv.nl/DR4/lensing.php`
   - Cosmic shear release page: `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_cosmicshear.php`
   - 3x2pt release page: `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_3x2pt_Cosmology.php`
2. Published tarball endpoints from release pages:
   - `https://kids.strw.leidenuniv.nl/DR4/data_files/KiDS1000_cosmic_shear_data_release.tgz`
   - `https://kids.strw.leidenuniv.nl/DR4/data_files/KiDS1000_3x2pt_fiducial_chains.tar.gz`
3. Linked open-source data/software repository:
   - `https://github.com/KiDS-WL/Cat_to_Obs_K1000_P1/tree/master/data`

## 11. Implementation Milestones

1. M1: create scaffold + configs + schema validators.
2. M2: implement dataset ingestion and prior registry.
3. M3: implement likelihood adapters and joint log posterior.
4. M4: implement emcee runner and diagnostics.
5. M5: implement report generation (`results.md` + machine outputs).
6. M6: run first smoke analysis with one dataset per family.

## 12. Acceptance Criteria

1. End-to-end run completes from `.bat` or `.sh`.
2. `results.md` includes parameter ranges and compatibility verdict.
3. All input datasets used are traceable by URL/version/hash.
4. Final verdict (`fits_known_physics_at_all`) is reproducible with fixed seed.
5. No PowerShell execution is required by default workflow.
