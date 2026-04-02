# UniNet QM Section (Build-Up Draft v1)

Date: 2026-03-30  
Primary source of truth: `../docs_input/UNINET_CORE_AXIOMS.md`  
Companion governance: `UNINET_NOTATION_UNITS_STANDARD.md`, `UNINET_PROOF_STATUS_LEDGER.md`, `UNINET_BOUNDARY_NONCLAIMS.md`, `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`

## 1. Contract and Scope

1. This section packages the QM regime from existing UniNet axioms and derived structures.
2. No GR field equation is used as a premise for QM statements.
3. Measurement-interface claims are explicitly status-tagged; no hidden collapse postulate is introduced.
4. Queue quantities in QM are bookkeeping variables unless GR activation is explicitly invoked.

## 2. Assumption Ledger

| id | statement | status | source anchor | role |
|---|---|---|---|---|
| QM-A1 | Hilbert state space and unitary update | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:265,298` | microscopic dynamics |
| QM-A2 | Graph locality of transfer | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:280` | finite propagation |
| QM-A3 | Static-latency QM regime | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1183,1223` | regime axiom/theorem |
| QM-A4 | Continuity/cut-balance structure | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:400,422` | occupancy/flux balance |
| QM-A5 | Observer-time and coarse-graining map | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:667,697,706` | observed-time interface |
| QM-A6 | Born-like frequency recovery from coarse layer | deferred | `C:/SB/UniNet3/docs_input/UNINET_QM_SECTION_RIGOR_PLAN.md` | measurement derivation gap |
| QM-A7 | Queue bookkeeping does not alter QM latency | proved (scope-limited) | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:526,1223` | category separation |

## 3. Mapping Blocks (Q1-Q9)

### Q1. Substrate Dynamics -> Well-Posed Unitary Evolution

- Core evolution law (`proved`):
  $$
  \psi_{n+1}=U\psi_n,\qquad U^\dagger U=I.
  $$
- Immediate consequence (`proved`): global norm conservation.
- Optional variational companion (not required for kinematic claim): discrete action in $\psi_n,\psi_n^\dagger$ with unitary constraint multipliers.

### Q2. Local Dynamics -> Finite Propagation and Fixed Latency

- Locality gives finite support growth per tick (`Lemma 1.1`).
- QM regime theorem gives fixed topological latency (`proved`):
  $$
  \delta_{\mathrm{QM}}(u,v)=d_G(u,v).
  $$
- No species-dependent superluminal branch is introduced at this layer.

### Q3. Occupancy Dynamics -> Continuity/Flux Form

- Occupancy definition:
  $$
  \rho(v,n)=\|\psi_v(n)\|^2.
  $$
- Cut-balance theorem (`proved`): bulk change equals boundary flux for any region.
- Queue equivalence form is admissible bookkeeping, not a new propagation law.

### Q4. Causal Structure -> Observer-Time Kinematics

- Causal precedence and cone structure from Tier-2 (`proved`).
- Observer-time construction from past-set volume (`proved` as finite causal-set statement).
- Boundary note: continuum smooth-time refinements are imported as `external-constraint`.

### Q5. State Evolution -> Observable Statistics Interface

- Tier-0 microdynamics remains deterministic and unitary (`proved`).
- Observed stochasticity is packaged as coarse-graining effect (`postulate` with theorem support from arrow statement).
- No fundamental collapse term is added in this section.

### Q6. Interference and Context-Dependence Claims

- Interference from linear unitary superposition is `proved` at formal level.
- Protocol-level contextuality/Born-frequency closure is `deferred` until explicit theorem or locked postulate pipeline is added.
- This section therefore claims compatibility, not complete measurement-derivation closure.

### Q7. Symmetries and Conserved Quantities

- `proved`: graph isomorphism covariance (`S1`), QM time-translation invariance in static regime (`S2`), locality-preserving conjugation symmetry (`S3`), norm conservation (`C1`).
- `deferred`: projected pseudo-unitary invariance and entropy-style invariants pending full action-domain proof (`noether-like` subtype).

### Q8. QM -> GR Boundary Condition

- Boundary trigger (packaging statement): QM regime assumptions cease when adaptive-latency activation assumptions are turned on.
- Status: `postulate` interface statement, consistent with GR section contract.
- No mixed-regime hidden assumption is permitted.

### Q9. Queueing Compatibility in QM Regime

- Queue drift identity remains a conservation bookkeeping statement (`proved`).
- Static-latency theorem remains unchanged while GR transport activation is off (`proved` in regime scope).
- Near-saturation trapping claims are GR-only and are not imported as QM results.

## 4. Claim Boundaries

1. This document does not claim a complete internal derivation of the Born rule.
2. This document does not claim collapse physics; it only states the unitary-plus-coarse-graining package.
3. This document does not claim GR adaptive-delay behavior inside pure QM regime statements.

## 5. Literature Hooks for Imported Steps

1. Aharonov-Davidovich-Zagury (1993), quantum random walks.
2. Ambainis et al. (2001), discrete-time quantum walks.
3. Venegas-Andraca (2012), quantum walk review.
4. Zurek (2003), decoherence and classical emergence.
5. Minguzzi (2019), causality/time-function foundations.

## 6. Mapping-Completeness Checklist

| mapping item | status now | blocker if not proved |
|---|---|---|
| Q1 well-posed unitary evolution | proved | none |
| Q2 finite propagation and fixed latency | proved | none |
| Q3 continuity/flux packaging | proved | none |
| Q4 observer-time kinematics | proved | continuum regularity details |
| Q5 micro-deterministic to observed-probabilistic interface | postulate + partial theorem support | explicit theorem-level measurement map |
| Q6 protocol-level measurement closure | deferred | locked protocol theorem/postulate pipeline |
| Q7 symmetry and invariants | mixed (`proved` + `deferred`) | full Noether closure (`noether-like` subtype) |
| Q8 QM-to-GR boundary map | postulate | explicit trigger theorem |
| Q9 queue compatibility | proved in regime scope | none |

## 7. Falsifiability Cross-Links

1. `UNINET_QM_FALSIFIABILITY_MATRIX.md`: `QM-CORE-001`, `QM-CORE-002`.
2. Deferred interfaces: `QM-DEF-003`, `QM-DEF-004`.






