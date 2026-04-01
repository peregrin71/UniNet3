# UniNet Queueing Rigor Plan

Date: 2026-03-30
Primary source: `../docs_input/UNINET_CORE_AXIOMS.md`
Status: partially implemented (core theorem package merged; viability/falsifiability tightening still pending)
Formalism policy: `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md` (native queue identities remain primary; constrained-action companions optional where explicit).

## 0. Implementation Status Snapshot

Completed in core:

1. Queue definitions (`Definition 1.6`, `Definition 1.7`).
2. Queue drift and trapping results (`Theorem 1.3`, `Theorem 1.4`, `Corollary 1.2`).
3. Effective transport constraints now codified as `R9` and `R10`.

Still pending for full closure:

1. Explicit witness-family construction for non-empty admissible transport set.
2. Formal Viability Gate 1 parameter-volume run.
3. Final red-team pass on observability mappings.

## 1. Scope Lock

1. Keep Tier-0 axioms unchanged.
2. Treat queueing as a derived layer from locality + unitarity + continuity.
3. Add only `Definition/Lemma/Theorem/Corollary` items unless a constitutive law is provably non-derivable.
4. If a non-derivable constitutive relation is needed, mark it explicitly as `Postulate` and isolate it.

## 2. Feasibility Gate 0 (Before New Claims)

Define admissible transport set
\[
\mathcal{A}_U := \{U \mid R1\text{--}R8 \;\wedge\; Q1\text{--}Q5\}
\]
where `Q1--Q5` are queueing transport constraints below.

Mandatory pass condition before theorem promotion:

1. Provide at least one explicit witness family `U_*` with non-empty parameter domain in `\mathcal{A}_U`.
2. Record witness assumptions and regularity class.

## 3. Queueing Transport Constraints (`Q1--Q5`)

These are additional constraints on effective transport behavior (not independent edge-delay axioms). `Q1`, `Q2`, and `Q5` are now explicitly represented by `R9`/`R10`; `Q3`/`Q4` remain as formal regularity checks to close in the witness-family step.

1. `Q1` Monotone slowdown:
\[
\partial_{\rho}\,\tau_{\mathrm{eff}} \ge 0,\qquad
\partial_{\mathrm{Curv}}\,\tau_{\mathrm{eff}} \ge 0.
\]
2. `Q2` Baseline lower bound:
\[
\tau_{\mathrm{eff}}(u\to v) \ge d_G(u,v).
\]
3. `Q3` Positivity/coercivity of effective delay kernel:
\[
\tau_{\mathrm{eff}} \ge 0,\qquad \tau_{\mathrm{eff}}\to\infty\ \text{only in controlled saturation limits}.
\]
4. `Q4` Regularity (stability under small perturbations): Lipschitz bound in `(\rho,\mathrm{Curv})` over admissible regime.
5. `Q5` Saturation behavior near occupancy ceiling:
\[
\rho\to 1 \Rightarrow \text{outward throughput suppression, with explicit asymptotic bound on } |\Phi|.
\]

## 4. Queueing Definitions to Add (Tier 1-Compatible)

1. Local backlog: \(q_v(n):=\rho(v,n)\).
2. Regional backlog: \(Q_n(R)=\sum_{v\in R}\rho_n(v)\).
3. Boundary throughput: \(\Phi_n(\partial R)\).
4. Dwell-time observable: \(T_{\mathrm{dwell}}(R)\) (operational definition tied to support persistence).
5. Escape-time observable: \(T_{\mathrm{esc}}(R)\) (first-passage style in projected regime).
6. Queueing regime classifier using thresholds in \((\rho,|\Phi|,\mathrm{Curv})\).

## 5. Theorem Package to Add

1. `Queue Theorem 1` (Conservation-to-Queue Identity):
\[
Q_{n+1}(R)-Q_n(R)=-\Phi_n(\partial R)
\]
with explicit dependency list.
   Optional variational companion: constrained action with multipliers enforcing discrete continuity before deriving drift identities.
2. `Queue Theorem 2` (Low-Load Transient Stability): bounded backlog under non-bottleneck throughput assumptions.
3. `Queue Theorem 3` (Near-Saturation Trapping): high-\(\rho\), high-curvature regime implies large dwell time.
4. `Queue Corollary 1` (Boundary-Dominant Release): measurable release controlled by boundary layer flux.
5. `Queue Corollary 2` (Closure vs Leak):
   - exact closure branch \(\Phi=0\),
   - quasi-closure branch \(\Phi\neq0\) but small.

## 6. Physical Regime Description (for Intuition Section)

1. Normal regime:
   - low/moderate \(\rho\), finite mixing/escape times,
   - small delay correction to topological baseline.
2. Black-hole regime:
   - interior: strongly suppressed outward transport + unitary scrambling (no information destruction),
   - boundary layer: dominant exchange surface,
   - evaporation-like behavior only in leaky branch via small nonzero \(\Phi\).

## 7. Viability Gate 1 (After Draft Theorems)

Perform parameter-volume check on
\[
(\alpha,\beta,\xi_{\mathrm{leak}},\bar\epsilon_{\mathrm{mix}},\epsilon_{\mathrm{CP}})
\]
under all hard constraints.

Pass criteria:

1. Feasible volume is non-empty and not measure-zero under declared priors.
2. At least one region remains compatible with current core observational constraints.

## 8. Falsifiability Sync

1. Add new anchors in `../docs_input/UNINET_CORE_AXIOMS.md` for each queue theorem.
2. Update rows in `UNINET_GR_FALSIFIABILITY_MATRIX.md` and `UNINET_QM_FALSIFIABILITY_MATRIX.md` to reference those anchors.
3. Keep compatibility-only queue statements as `deferred` until they have binary reject thresholds.

## 9. Execution Order

1. Complete witness-family construction and run Feasibility Gate 0.
2. Finalize hard/soft split for `Q3`/`Q4` regularity checks.
3. Run Viability Gate 1.
4. Keep black-hole interior vs boundary-layer subsection aligned with core theorem branching.
5. Re-run falsifiability and parameter-ledger traceability check after each theorem/constraint edit.



