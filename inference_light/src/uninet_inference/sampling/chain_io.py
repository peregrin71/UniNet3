from __future__ import annotations

from pathlib import Path

import h5py
import numpy as np


def save_chain_h5(
    path: Path,
    chain: np.ndarray,
    log_prob: np.ndarray,
    samples: np.ndarray,
    parameter_names: list[str],
    acceptance_fraction: np.ndarray,
) -> None:
    with h5py.File(path, "w") as handle:
        handle.create_dataset("chain", data=chain)
        handle.create_dataset("log_prob", data=log_prob)
        handle.create_dataset("samples", data=samples)
        handle.create_dataset("acceptance_fraction", data=acceptance_fraction)
        dtype = h5py.string_dtype(encoding="utf-8")
        handle.create_dataset("parameter_names", data=np.asarray(parameter_names, dtype=dtype))

