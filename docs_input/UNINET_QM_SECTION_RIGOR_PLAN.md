# UniNet QM Section: Full-Rigor Build Plan (Mapping-Complete)

**Date:** 2026-03-30  
**Primary source of truth:** `../docs_input/UNINET_CORE_AXIOMS.md` only  
**Secondary role of `UNINET_MERGED.md`:** inspiration for structure/wording only.

---

## 1. Entry Criterion and Scope Lock

The QM section can start now under this lock:

1. Base assumptions are limited to Tier-0 axioms plus Tier-1 to Tier-3 derived structures and QM-regime assumptions.
2. No GR field equation is used in the QM section.
3. Any statement about measurement/Born-rule emergence must be tagged as either:
   - `Derived` with proof, or
   - `Postulate` with explicit deferment.
4. Queueing language in QM must remain kinematic (drift bookkeeping), not an independent delay axiom.
5. Notation/units and claim-status tags must follow `UNINET_NOTATION_UNITS_STANDARD.md` and `UNINET_PROOF_STATUS_LEDGER.md`.
6. Dual-track formula policy (native + optional discrete-action companion) must follow `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

---

## 2. Mapping-Complete Targets (Mandatory)

1. **Q1: Substrate Dynamics -> Well-posed Unitary Evolution**
   - Input: `G`, `H`, `U`.
   - Output: existence/uniqueness of discrete-time evolution and norm conservation.

2. **Q2: Unitary Local Dynamics -> Finite Propagation and Fixed Latency**
   - Input: graph locality.
   - Output: reachability bounds and $\delta_{\mathrm{QM}}(u,v)=d_G(u,v)$.

3. **Q3: Local Occupancy Dynamics -> Continuity/Flux Form**
   - Input: $\rho(v,n)=||psi_v(n)||^2$.
   - Output: admissible flux representation and cut-balance law.

4. **Q4: Causal Structure -> Observer-Time Kinematics**
   - Input: precedence relation and cones.
   - Output: time function existence and operational $t_obs$ interpretation.

5. **Q5: State Evolution -> Observable Statistics Interface**
   - Input: projected/coarse observables.
   - Output: exact statement of what is deterministic at Tier-0 vs probabilistic at observed level.

6. **Q6: Interference Structure -> QM Phenomenology Claims**
   - Input: superposition under unitary local updates.
   - Output: explicit theorem/postulate tags for interference, contextuality-like behavior, and apparent randomness.

7. **Q7: Symmetries -> Conserved Quantities**
   - Input: graph relabeling covariance, local unitary conjugations.
   - Output: invariance and conservation statements with domains.

8. **Q8: QM-to-GR Boundary Condition**
   - Input: QM static-latency regime.
   - Output: exact interface conditions when GR block is activated later.

9. **Q9: Queueing Compatibility in QM Regime**
   - Input: Tier-1 queue definitions and drift identity.
   - Output: explicit statement that queue bookkeeping does not renormalize static QM latency; only GR activation introduces adaptive-delay backpressure.

---

## 3. Required Structure of the New QM Document

Recommended target file: `UNINET_QM_SECTION.md`

1. Contract and allowed inputs.
2. Assumption ledger with IDs and claim types.
3. Unitary-local evolution block (Q1-Q3).
4. Causality and observer-time block (Q4).
5. Measurement/statistics interface block (Q5-Q6).
6. Symmetry and invariants block (Q7).
7. Regime boundary block (Q8).
8. Queueing compatibility block (Q9).
9. Open proof obligations and deferred claims.
10. Dual-track formula appendix (native equations first, action companion where applicable).

---

## 4. Proof Obligations by Mapping

### Q1
- `Theorem Q1.1`: existence and uniqueness for $\psi_{n+1}=U \psi_n$.
- `Corollary Q1.2`: norm and global occupancy conservation.
  Native target equation: `\psi_{n+1}=U\psi_n`, `U^\dagger U=I`.
  Optional discrete-action companion: stationarity of a discrete action in `\psi_n,\psi_n^\dagger` yielding unitary update constraints.

### Q2
- `Lemma Q2.1`: locality implies finite-speed support growth.
- `Theorem Q2.2`: fixed topological latency in QM regime.

### Q3
- `Definition Q3.1`: antisymmetric edge flux representation.
- `Theorem Q3.2`: region cut-balance (discrete Gauss/Stokes).

### Q4
- `Definition Q4.1`: observer-time functional from causal order.
- `Theorem Q4.2`: strict monotonicity along causal precedence under nondegeneracy.

### Q5
- `Definition Q5.1`: observable sigma-algebra/coarse-graining map.
- `Proposition Q5.2`: deterministic microstate to probabilistic observational map.

### Q6
- `Theorem or Postulate Q6.1`: Born-like frequency recovery conditions.
- `Proposition Q6.2`: explicit limits of the derivation (what is not yet proved).

### Q7
- `Theorem Q7.1`: graph-isomorphism covariance.
- `Theorem Q7.2`: conserved quantities under allowed symmetries.

### Q8
- `Definition Q8.1`: trigger condition for leaving QM static-latency regime.
- `Proposition Q8.2`: consistency of handoff to GR document.

### Q9
- `Lemma Q9.1`: queue drift identity in QM regime is a conservation statement, not a new propagation law.
- `Proposition Q9.2`: static-latency theorem remains unchanged under admissible queue bookkeeping.
- `Boundary Note Q9.B`: near-saturation trapping claims are GR-only and must be deferred to GR section theorems.

---

## 5. Claim Discipline

1. No sentence containing "emerges" without an equation-level map.
2. If Born-rule emergence is not fully proved, isolate as `Postulate` + required proof route.
3. Separate kinematics, dynamics, and measurement in different sections.
4. Every use of $\rho$, `J`, $\delta$, $t_obs$ must include domain and units.
5. Any queue term must specify whether it is bookkeeping (`Q`, `A`, `S`, `\Phi`) or causal-latency (`\delta`) to prevent category mixing.
6. Keep deductions readable in native notation; add variational companion only where it improves rigor or audience expectations.

---

## 6. Literature Cross-References (Known Steps)

1. Aharonov, Davidovich, Zagury (1993), quantum random walks.  
   Phys. Rev. A 48, 1687. https://doi.org/10.1103/PhysRevA.48.1687
2. Ambainis et al. (2001), discrete-time quantum walks.  
   STOC 2001 / JCSS follow-up.
3. Venegas-Andraca (2012), review of quantum walks.  
   https://doi.org/10.2200/S00443ED1V01Y201206QMC007
4. Zurek (2003), decoherence and classical emergence.  
   Rev. Mod. Phys. 75, 715. https://doi.org/10.1103/RevModPhys.75.715
5. Minguzzi (2019), causality/time-function results used for order-time statements.  
   https://doi.org/10.1007/s41114-019-0019-x

---

## 7. Done Criteria for "QM Mapping Complete"

1. Q1-Q8 all present as formal statements.
2. Micro-deterministic vs observed-probabilistic distinction is explicit and non-ambiguous.
3. Static latency theorem is fully separated from GR adaptive latency.
4. All unresolved measurement claims are marked deferred, not implied as proved.
5. Final dependency DAG is included.
6. Queueing compatibility statement (Q9) is explicit and does not introduce a hidden delay postulate.

---

## 8. Execution Order

1. Build Q1-Q3 first.
2. Build Q4 next.
3. Lock Q5-Q6 language carefully (proof vs postulate).
4. Add Q7 invariants.
5. Write Q8 boundary.
6. Write Q9 queue compatibility.
7. Run claim audit.






