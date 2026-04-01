#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

if [[ ! -x ".venv/bin/python" ]]; then
  echo "Missing .venv. Run scripts/bootstrap_venv.sh first."
  exit 1
fi

PYTHONPATH="${PROJECT_ROOT}/src" ".venv/bin/python" -m uninet_inference.cli --root "${PROJECT_ROOT}" "$@"

