# UniNet GR Section: Full-Rigor Build Plan (Mapping-Complete)

**Date:** 2026-03-30  
**Primary source of truth:** `../docs_input/UNINET_CORE_AXIOMS.md` only  
**Secondary role of `UNINET_MERGED.md`:** inspiration for phrasing/ordering only, not for assumptions.

---

## 1. Entry Criterion and Scope Lock

This GR section is ready to start **now** under the following lock:

1. No new microscopic axioms beyond Tier-0 and bridge postulates BRIDGE-P1..BRIDGE-P3 already in `../docs_input/UNINET_CORE_AXIOMS.md`.
2. Any new assumption at GR level must be marked explicitly as either:
   - `Postulate` (model choice), or
   - `Derived` (with proof and dependency list).
3. No observational fitting in this chapter; only structural derivation and consistency.
4. Symmetry/conservation promotions beyond existing core claims must follow `UNINET_NOETHER_SYMMETRY_PROGRAM.md`.
5. Notation/units and claim-status tags must follow `UNINET_NOTATION_UNITS_STANDARD.md` and `UNINET_PROOF_STATUS_LEDGER.md`.
6. Dual-track formula policy (native + Lagrangian companion where applicable) must follow `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

---

## 2. Mapping-Complete Targets (Mandatory)

The GR document is accepted only if all mappings below are formalized.

1. **M1: Substrate -> Causal Order**
   - Input: graph locality + reachability.
   - Output: precedence relation, cones, horismos.

2. **M2: Causal Order -> Observed Time**
   - Input: order structure ($J^-$, $J^+$).
   - Output: observer-time functional $t_obs$ (time function properties proved).

3. **M3: Microscopic State -> Observed Spacetime**
   - Input: projection maps $Pi_v$.
   - Output: projected event geometry (well-defined quotient/interface map).

4. **M4: Observed Spacetime -> Proper Time and Time Dilation**
   - Input: projected worldlines and Lorentzian norm.
   - Output: proper-time increment law and explicit time-dilation statement.

5. **M5: Dynamics -> Lorentz Invariance (or controlled breaking statement)**
   - Input: pseudo-unitary compatibility conditions.
   - Output: invariant interval statement, with exact regime of validity.

6. **M6: Geometry -> Geodesics in Observed Spacetime**
   - Input: time-separation structure.
   - Output: maximizing-curve/geodesic existence and correspondence conditions.

7. **M7: Sources -> Curvature Dynamics**
   - Input: buffering/flux effort and variational action.
   - Output: discrete Einstein-like equation + consistency identity.

8. **M8: Queueing/Backpressure -> Horizon-Scale Transport**
   - Input: queue definitions, drift identities, and transport constraints (`R9`, `R10`).
   - Output: normal-regime finite release vs near-saturation trapping statements with explicit observables.

9. **M9: Black-Hole Application Layer (Deferred-to-Core Path)**
   - Input: horizon-like cuts, queue trapping/release, coarse-graining arrow theorem.
   - Output: Page-turnover proxy, near-horizon smoothness statement, and multimode ringdown map with explicit promotion gates.

---

## 3. Required Structure of the New GR Document

Recommended target file: `UNINET_GR_SECTION.md`

1. **Contract**
   - Allowed inputs from `../docs_input/UNINET_CORE_AXIOMS.md`
   - Claim taxonomy: `Axiom / Definition / Lemma / Theorem / Postulate / Corollary`

2. **Assumption Ledger**
   - Table with unique IDs and dependency graph.

3. **Kinematics Block (M1, M2, M3)**
   - Formal map to causal order, observed time, projected spacetime.

4. **Clock Block (M4)**
   - Proper time and time dilation theorems.

5. **Symmetry Block (M5)**
   - Lorentz/pseudo-unitary invariance theorem and failure envelope.

6. **Geodesic Block (M6)**
   - Existence/characterization of geodesic-like maximizing curves.

7. **Dynamics Block (M7)**
   - Action, Euler-Lagrange equation, conservation compatibility.

8. **Queueing and Boundary-Layer Block (M8)**
   - Queue drift, backpressure monotonicity, and boundary-dominant release/trapping conditions.

9. **Black-Hole Application Block (M9, deferred-aware)**
   - Page/firewall/ringdown consequence statements with explicit map-to-observable status.

10. **Continuum Correspondence**
   - Precise scaling assumptions and limiting statement.

11. **Failure Modes**
   - Explicit conditions under which mapping breaks.

12. **Checklist and Open Proof Obligations**
   - Every missing proof tagged and deferred intentionally.
13. **Dual-Track Appendix**
   - For each major theorem: native equation form + variational/Lagrangian companion (if in mandatory class).

---

## 4. Proof Obligations by Mapping

### M1: Substrate -> Causal Order
- `Lemma M1.1`: locality implies finite-speed reachability bound.
- `Theorem M1.2`: precedence relation is a partial order.
- `Corollary M1.3`: horismos equals cone boundary in this discrete setting.

### M2: Causal Order -> Observed Time
- `Definition M2.1`: $t_obs$ from past-set volume (or equivalent monotone functional).
- `Theorem M2.2`: $x \prec y \Rightarrow t_{\mathrm{obs}}(x) < t_{\mathrm{obs}}(y)$ under nondegeneracy assumptions.
- `Remark M2.R`: distinguish microscopic tick `n` from emergent observed time.

### M3: Microscopic State -> Observed Spacetime
- `Definition M3.1`: projection interface map and equivalence relation.
- `Theorem M3.2`: map is label-gauge covariant under graph isomorphisms.
- `Theorem M3.3`: causal compatibility of projection (no superluminal inversion).

### M4: Proper Time and Time Dilation
- `Definition M4.1`: proper-time increment from projected timelike increments.
- `Theorem M4.2`: buffering/congestion regime implies reduced accumulated proper time.
- `Corollary M4.3`: operational time-dilation statement (observer-comparison form).

### M5: Lorentz Invariance
- `Definition M5.1`: admissible pseudo-unitary transformation class.
- `Theorem M5.2`: invariance of projected interval under admissible transforms.
- `Proposition M5.3`: when/where deviations are allowed (discrete corrections).

### M6: Geodesics in Observed Spacetime
- `Definition M6.1`: geodesic-like curve (smooth case) / maximizing causal curve (synthetic case).
- `Theorem M6.2`: existence in the adopted regularity class.
- `Theorem M6.3`: correspondence criterion between graph-optimal paths and projected geodesics.

### M7: Source-Curvature Dynamics
- `Definition M7.1`: effort functional and stress-effort map.
- `Theorem M7.2`: Euler-Lagrange discrete field equation.
- `Lemma M7.3`: conservation consistency (Bianchi-type compatibility condition).
  Native target equation: $\mathrm{Curv}[\tau] = \kappa\,\mathrm{StressEffort}[\rho,J]$.
  Variational companion: $\delta(\mathcal{S}_{\mathrm{geo}}[\tau]+\kappa\,\mathcal{S}_{\mathrm{src}}[\rho,J])/\delta\tau=0$.

### M8: Queueing/Backpressure and Horizons
- `Definition M8.1`: normal vs near-saturation queueing regimes in projected GR observables.
- `Theorem M8.2`: queue-drift identity and low-load stability map to finite-release behavior.
- `Theorem M8.3`: near-saturation trapping bound from adaptive-latency and `R9/R10` constraints.
- `Corollary M8.4`: boundary-dominant release criterion with explicit closure-vs-leak branch condition.

### M9: Black-Hole Application Layer
- `Proposition M9.1` (deferred): define an operational Page-turnover proxy consistent with M8 and coarse-graining theorem.
- `Proposition M9.2` (deferred): near-horizon smoothness/no-firewall statement in terms of bounded effective transport law (no singular constitutive jump).
- `Proposition M9.3` (deferred): multimode ringdown coefficient map from leakage/microstate parameters.
- `Boundary Note M9.B`: none of M9 is promoted to core theorem status without explicit forward map and binary reject threshold.

---

## 5. Claim Discipline (Rigorous Review Mode)

1. Every theorem must list exact dependencies.
2. Every nontrivial equality must include domain/regularity assumptions.
3. Every "emergence" claim must be rewritten as an explicit map + theorem.
4. No phenomenological statement in proof sections.
5. Units must be checked line-by-line in the projection/dynamics blocks.
6. If a step is not proved, mark it `Postulate` and isolate it.
7. Every horizon statement must declare whether it is in the exact-closure branch ($\Phi=0$) or leaky branch ($\Phi\neq0$) and quote the throughput bound class.
8. Dynamics/source claims must show native theorem statement plus variational companion form.

---

## 6. Literature Cross-References (Known Steps)

Use these references where the GR section relies on established mathematics/physics.

1. **General Lorentzian causality (time functions, maximizing causal curves):**  
   E. Minguzzi, *Lorentzian causality theory*, Living Rev. Relativ. 22, 3 (2019).  
   https://doi.org/10.1007/s41114-019-0019-x

2. **Closed cone structures, horismos/lightlike generators, smooth time functions:**  
   E. Minguzzi, *Causality theory for closed cone structures with applications* (2019).  
   Preprint: https://arxiv.org/abs/1709.06494  
   DOI: https://doi.org/10.1142/S0129055X19300012

3. **Synthetic Lorentzian geometry via time-separation (non-smooth setting):**  
   M. Kunzinger, C. Samann, *Lorentzian length spaces* (2018).  
   https://doi.org/10.1007/s10455-018-9633-1  
   Preprint: https://arxiv.org/abs/1711.08990

4. **Recent synthetic extensions (if gluing/regularity arguments are used):**  
   T. Beran, F. Rott, *Gluing constructions for Lorentzian length spaces* (2024 issue).  
   https://doi.org/10.1007/s00229-023-01469-4

5. **Proper time, worldlines, Lorentz group (for observed-time and dilation interpretation):**  
   E. Gourgoulhon, *Special Relativity in General Frames* (2013).  
   https://doi.org/10.1007/978-3-642-37276-6

6. **Discrete gravity precedent for curvature from simplicial action:**  
   T. Regge, *General relativity without coordinates* (1961).  
   https://doi.org/10.1007/BF02733251

---

## 7. Done Criteria for "Mapping Complete"

All must be true:

1. M1-M7 are present as formal statements (not prose only).
2. Observer time and proper time are both defined and explicitly distinguished.
3. Time dilation theorem is stated with assumptions and bounds.
4. Lorentz invariance statement includes exact transformation class and correction regime.
5. Geodesic/maximizing-curve section is present in observed spacetime.
6. Every known imported step cites literature in-line.
7. A final dependency DAG from axioms to GR conclusions is included.
8. Queueing/backpressure block is present and consistent with `R9/R10` plus Tier-1 queue theorems.
9. Black-hole application block is present with explicit deferred/core promotion boundaries.

---

## 8. Execution Order

1. Write Sections 1-3 (contract + ledger + kinematics).
2. Write M4/M5 (clock + symmetry) before dynamics.
3. Write M6 geodesics next (to prevent ambiguity in geometry block).
4. Write M7 action/dynamics.
5. Write M8 queueing/backpressure-horizon block and tie to falsifiability rows.
6. Write M9 black-hole application block (deferred-aware).
7. Run a final "claim audit" to remove all unstated assumptions.







