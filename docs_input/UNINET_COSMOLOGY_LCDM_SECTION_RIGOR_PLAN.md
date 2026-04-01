# UniNet Cosmology Section: Full-Rigor Build Plan (LCDM-Comparable)

**Date:** 2026-03-30  
**Primary source of truth:** `../docs_input/UNINET_CORE_AXIOMS.md` only  
**Secondary role of `UNINET_MERGED.md`:** inspiration only (no imported assumptions).

---

## 1. Entry Criterion and Scope Lock

The cosmology section can begin now with this lock:

1. Use only already-declared UniNet structures (buffering, flux, projection, field law regime assumptions).
2. Any background-cosmology ansatz (homogeneity/isotropy, coarse-grained fluid form) must be explicitly tagged.
3. Claims must be split into:
   - structural derivation,
   - effective-model postulate,
   - observational test statement.
4. Any congestion/backpressure claim must trace to queueing theorems and transport constraints (`R9`, `R10`).
5. Symmetry/conservation promotions beyond current core claims must follow `UNINET_NOETHER_SYMMETRY_PROGRAM.md`.
6. Notation/units and claim-status tags must follow `UNINET_NOTATION_UNITS_STANDARD.md` and `UNINET_PROOF_STATUS_LEDGER.md`.
7. Dual-track formula policy (native effective equations + Lagrangian companion where applicable) must follow `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

---

## 2. Mapping-Complete Targets (Mandatory)

1. **C1: Microscopic Buffer Dynamics -> Effective Homogeneous Background**
   - Define coarse-graining map from graph observables to background energy components.

2. **C2: Effective Sources -> Friedmann-like Evolution**
   - Provide exact equations used for $H(z)$ and scale-factor dynamics.

3. **C3: Buffer Relaxation -> Dark Energy Sector**
   - Define $rho_DE(t)$ and derive $w(z)$ behavior under stated assumptions.

4. **C4: Long-Wavelength Buffered Modes -> Dark Matter Sector**
   - Show pressureless-limit conditions and clustering behavior assumptions.

5. **C5: Phase/Buffer Early-Time Mechanism -> Inflation Sector**
   - Define trigger, e-fold expression, and termination conditions.

6. **C6: Perturbations -> Observable Spectra**
   - Map model perturbation variables to CMB/LSS observables ($n_s$, $r$, growth, lensing).

7. **C7: Thermodynamic/Conservation Consistency**
   - Ensure continuity, entropy-arrow compatibility, and no hidden source/sink inconsistencies.

8. **C8: LCDM Comparison Layer**
   - Define baseline parameterization and residual metrics vs LCDM.

9. **C9: Falsifiability Layer**
   - Identify decisive observables and explicit failure conditions.

10. **C10: Queueing/Backpressure Mapping**
   - Map queue drift and saturation-throughput suppression to growth and late-time expansion observables without adding new microscopic axioms.

11. **C11: Inflation Exit and Reheating Interface**
   - Define the end-of-inflation trigger, reheating channel assumptions, and observable consistency checks (`N_{\mathrm{eff}}`, thermal-history constraints).

12. **C12: Non-Particle Dark-Sector Detection Interface (Deferred)**
   - Define how long-wavelength buffer modes map (or fail to map) to collider/direct-detection observables.

---

## 3. Required Structure of the New Cosmology Document

Recommended target file: `UNINET_COSMOLOGY_LCDM_SECTION.md`

1. Contract and claim taxonomy.
2. Assumption ledger (background and perturbation assumptions separated).
3. Background dynamics block (C1-C5).
4. Perturbation/observable block (C6).
5. Queueing/backpressure block (C10).
6. Inflation exit/reheating block (C11).
7. Non-particle detection-interface block (C12, deferred-aware).
8. Consistency block (C7).
9. LCDM comparison block (C8).
10. Falsification table and forecast block (C9).
11. Dual-track appendix for background and perturbation equations.

---

## 4. Proof Obligations by Mapping

### C1-C2
- `Definition C1.1`: coarse-graining operator from graph to effective fluid variables.
- `Theorem/Postulate C2.1`: derivation status of Friedmann-like equations in this framework.
  Native targets: effective `H(z)` and continuity equations for buffered components.
  Variational companion (where assumptions are frozen): effective action `\mathcal{S}_{\mathrm{eff}}=\int d^4x\sqrt{-g}\,\mathcal{L}_{\mathrm{eff}}(\rho_{\mathrm{buffer}},\Phi,\ldots)` yielding background equations.

### C3
- `Definition C3.1`: relaxation law and parameter set.
- `Theorem C3.2`: induced equation-of-state evolution under assumptions.

### C4
- `Definition C4.1`: long-wavelength buffered mode class.
- `Proposition C4.2`: pressureless limit and growth behavior conditions.

### C5
- `Definition C5.1`: inflationary phase criterion.
- `Proposition/Theorem C5.2`: e-fold count expression and exit condition.

### C6
- `Definition C6.1`: linear perturbation variables and gauge choice.
- `Theorem/Postulate C6.2`: mapping to observables and transfer functions.

### C7
- `Lemma C7.1`: continuity and conservation consistency check.
- `Lemma C7.2`: entropy/arrow compatibility at coarse-grained level.

### C8-C9
- `Definition C8.1`: LCDM baseline vector and comparison metric (chi-square/BIC/AIC).
- `Proposition C9.1`: explicit falsification thresholds.

### C10
- `Definition C10.1`: effective queue observables used in cosmological coarse-graining (regional backlog, throughput suppression index).
- `Proposition/Theorem C10.2`: sign-robust mapping from queue/backpressure indicators to growth suppression or enhancement channel.
- `Boundary Note C10.B`: identify regimes where queue mapping is only qualitative and keep corresponding rows deferred.

### C11
- `Definition C11.1`: inflation-exit condition in buffer/phase variables.
- `Proposition C11.2`: reheating-channel assumptions and resulting thermal-history consistency conditions.
- `Boundary Note C11.B`: keep reheating claims deferred if no locked map to observables is supplied.

### C12
- `Definition C12.1`: effective coupling map (if any) from long-wavelength buffer modes to detector observables.
- `Proposition C12.2` (deferred): null-detection prediction status under explicit coupling assumptions.
- `Boundary Note C12.B`: no collider/direct-detection claim is promotable without a frozen coupling model.

---

## 5. Claim Discipline

1. Separate background and perturbation claims.
2. Mark every cosmological fit relation as `prediction` or `calibration`, never both.
3. Keep conservation checks explicit when introducing effective sectors.
4. No statement like "solves LCDM tensions" without a defined metric and dataset scope.
5. Keep inflation, dark matter, and dark energy linked only through stated shared variables.
6. Queueing effects must be stated as constrained correction channels, not unconstrained free functions.
7. Collider/direct-detection statements must specify whether they are true predictions or assumptions under a chosen coupling map.
8. Keep readable native equations primary; add effective-action counterparts for dynamics claims when explicit assumptions are available.

---

## 6. Literature Cross-References (Known Steps)

1. Planck Collaboration 2018 cosmological parameters ($Lambda$CDM baseline).  
   https://doi.org/10.1051/0004-6361/201833910
2. Mukhanov, *Physical Foundations of Cosmology* (inflation/perturbations).
3. Dodelson & Schmidt, *Modern Cosmology* (background + perturbation formalism).
4. Ma & Bertschinger (1995), linear perturbation equations in cosmology.  
   https://doi.org/10.1086/176550
5. Weinberg, *Cosmology* (2008), standard baseline equations.
6. Peacock, *Cosmological Physics* (structure growth background).

---

## 7. Done Criteria for "Cosmology Mapping Complete"

1. C1-C9 all present as formal statements with status tags.
2. Every effective fluid term has a microscopic source map.
3. Background and perturbation equations are both present.
4. LCDM comparison metric and dataset scope are explicit.
5. Falsification criteria are quantitative.
6. Deferred pieces are listed with required data/derivation path.
7. Queue/backpressure mapping is explicit and traceable to `R9/R10` and queue theorems.
8. Inflation-exit/reheating and detection-interface status is explicit (`core` vs `deferred`).

---

## 8. Execution Order

1. Build C1-C2 background mapping first.
2. Add C3-C5 sector mechanisms with explicit assumptions.
3. Add C6 perturbation/observable map.
4. Add C10 queue/backpressure map.
5. Add C11 inflation-exit/reheating map.
6. Add C12 detection-interface status map.
7. Add C7 conservation/thermo checks.
8. Close with C8-C9 LCDM comparison and falsifiability.





