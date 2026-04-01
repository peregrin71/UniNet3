# InferenceLight Download Manifest (No-Fetch)

Date: 2026-04-01  
Status: planning artifact only.  
This file documents where data can be obtained later. It does not trigger downloads.

## Policy

1. No dataset is downloaded by default.
2. No `.venv` creation is part of this manifest workflow.
3. All URLs are tracked here first, then explicitly approved before any fetch step.
4. Use checksums where providers publish them, then record local hash after manual download.

## Planned Dataset Sources

| family | dataset_id | official source | expected package/file | planned target path |
|---|---|---|---|---|
| cmb | act_dr6_lensing_v1p2 | `https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_lh_get.html` | `ACT_dr6_likelihood_v1.2.tgz` | `data/raw/cmb/ACT_dr6_likelihood_v1.2.tgz` |
| cmb | planck_2018_baseline_clik | `https://cobaya.readthedocs.io/en/cosmo_package/likelihood_planck.html` (manual install section) | `COM_Likelihood_Data-baseline_R3.00.tar.gz` | `data/raw/cmb/COM_Likelihood_Data-baseline_R3.00.tar.gz` |
| bao | desi_dr1_bao_vac_v1p0 | `https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params/v1.0/` | folder index (`cobaya/`, `iminuit/`, `README.md`) | `data/raw/bao/desi_dr1_bao_vac_v1.0/` |
| bao | cobaya_bao_data_repo | `https://github.com/CobayaSampler/bao_data` | text files (`desi_2024_*`, `sdss_DR16_*`) | `data/raw/bao/cobaya_bao_data/` |
| rsd | desi_dr1_fullshape_v1p0 | `https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/v1.0/data/` | likelihood/covariance HDF5 products | `data/raw/rsd/desi_dr1_fullshape_v1.0/` |
| weak_lensing | kids1000_cosmic_shear | `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_cosmicshear.php` | `KiDS1000_cosmic_shear_data_release.tgz` | `data/raw/weak_lensing/KiDS1000_cosmic_shear_data_release.tgz` |
| weak_lensing | kids1000_3x2pt_chains | `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_3x2pt_Cosmology.php` | `KiDS1000_3x2pt_fiducial_chains.tar.gz` | `data/raw/weak_lensing/KiDS1000_3x2pt_fiducial_chains.tar.gz` |

## Manual Acquisition Checklist (Future)

1. Confirm license and citation requirements for each source.
2. Download manually to the planned target path.
3. Record checksum in `data/raw/<family>/CHECKSUMS.txt`.
4. Update `configs/datasets.yaml` paths from sample local files to real data files.
5. Run ingestion-only validation first before any sampler run.

## Deferred Metadata Template

For each real dataset file, capture:

1. `source_url`
2. `downloaded_at_utc`
3. `license`
4. `version_tag`
5. `sha256`
6. `notes`

