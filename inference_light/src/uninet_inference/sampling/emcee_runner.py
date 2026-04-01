from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import emcee
import numpy as np


@dataclass(frozen=True)
class SamplerConfig:
    nwalkers: int
    nsteps: int
    burn_in: int
    thin: int
    init_jitter: float


@dataclass(frozen=True)
class SamplerResult:
    chain: np.ndarray
    log_prob: np.ndarray
    samples: np.ndarray
    acceptance_fraction: np.ndarray


def _initialize_walkers(
    center: np.ndarray,
    nwalkers: int,
    jitter: float,
    rng: np.random.Generator,
) -> np.ndarray:
    ndim = center.shape[0]
    spread = np.maximum(np.abs(center) * jitter, 1e-6)
    walkers = np.zeros((nwalkers, ndim), dtype=float)
    for i in range(nwalkers):
        walkers[i, :] = center + rng.normal(loc=0.0, scale=spread, size=ndim)
    return walkers


def run_sampler(
    log_prob_fn: Callable[[np.ndarray], float],
    initial_center: np.ndarray,
    config: SamplerConfig,
    seed: int,
) -> SamplerResult:
    ndim = initial_center.shape[0]
    if config.nwalkers < 2 * ndim:
        raise ValueError("nwalkers should be at least 2 * ndim for robust ensemble sampling")

    rng = np.random.default_rng(seed)
    initial_state = _initialize_walkers(initial_center, config.nwalkers, config.init_jitter, rng)

    sampler = emcee.EnsembleSampler(config.nwalkers, ndim, log_prob_fn)
    sampler.run_mcmc(initial_state, config.nsteps, progress=False)

    chain = sampler.get_chain()
    log_prob = sampler.get_log_prob()
    samples = sampler.get_chain(discard=config.burn_in, flat=True, thin=config.thin)

    return SamplerResult(
        chain=chain,
        log_prob=log_prob,
        samples=samples,
        acceptance_fraction=sampler.acceptance_fraction,
    )

