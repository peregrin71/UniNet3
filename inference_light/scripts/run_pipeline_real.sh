#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

bash "${SCRIPT_DIR}/preprocess_real_data.sh" --enable-datasets --disable-other-datasets --dataset-id cmb_planck_compressed_pr3 --dataset-id rsd_desi_dr1_fsigma8 --dataset-id wl_kids1000_s8
bash "${SCRIPT_DIR}/run_pipeline.sh" "$@"
