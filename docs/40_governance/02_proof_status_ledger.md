# UniNet Proof-Status Ledger v1

Date: 2026-03-30  
Purpose: explicit claim-status registry for clear reader-facing traceability and review transparency.

## 1. Status Vocabulary

1. `proved`: currently theorem-level in core with dependency path.
2. `postulate`: explicit modeling choice, not derived.
3. `deferred`: incomplete map/proof/threshold; not promotable.
4. `external-constraint`: supported via established external theorem/empirical constraint, not internally derived.

## 2. Ledger Schema

1. $claim_id$
2. `claim`
3. `status`
4. $source_anchor_or_doc$
5. $dependency_summary$
6. $promotion_blocker$
7. $owner_doc$

## 3. Ledger

| claim_id | claim | status | source_anchor_or_doc | dependency_summary | promotion_blocker | owner_doc |
|---|---|---|---|---|---|---|
| PS-001 | Graph-local unitary substrate (Tier-0 core) | proved | `../docs_input/UNINET_CORE_AXIOMS.md:211,244,260` | Axiom declarations | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-002 | Discrete cut-balance conservation ($bulk = boundary$) | proved | `../docs_input/UNINET_CORE_AXIOMS.md:387` | A0.4/A0.5/A0.6 + continuity defs | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-003 | Leaky-boundary criterion | proved | `../docs_input/UNINET_CORE_AXIOMS.md:446` | PS-002 + boundary defs | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-004 | Queue drift + near-saturation trapping | proved | `../docs_input/UNINET_CORE_AXIOMS.md:491,513,532` | continuity + GR regime law + queue defs | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-005 | Arrow emergence from non-injective coarse-graining | proved | `../docs_input/UNINET_CORE_AXIOMS.md:671` | unitarity + observer-time monotonicity + coarse-graining non-injectivity | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-006 | QM static latency universality | proved | `../docs_input/UNINET_CORE_AXIOMS.md:1153` | locality reachability ladder + QM regime axiom | none | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-007 | GR adaptive latency packaging | postulate | `../docs_input/UNINET_CORE_AXIOMS.md:1171` | bridge axioms + action-pattern assumptions | full action-level closure for all regimes | `UNINET_GR_SECTION.md` |
| PS-008 | Buffer-to-energy projection bridge | postulate | `../docs_input/UNINET_CORE_AXIOMS.md:1086` | bridge choice for observational map | independent derivation from microscopic layer absent | `../docs_input/UNINET_CORE_AXIOMS.md` |
| PS-009 | SM chirality/CP admissible-window constraints | postulate | `../docs_input/UNINET_CORE_AXIOMS.md:757,798,843` | A0.7 + transfer constraints | full gauge/representation derivation missing | `UNINET_SM_SECTION.md` |
| PS-010 | Full gauge-group emergence $U(1) x SU(2) x SU(3)$ | deferred | `UNINET_SM_SECTION.md` | transfer symmetry + anomaly constraints | explicit constructive derivation | `UNINET_SM_SECTION.md` |
| PS-011 | Cosmology DE/DM/Inflation packaging | postulate | `../docs_input/UNINET_CORE_AXIOMS.md:1188,1200,1209` | buffer dynamics application layer | complete transfer-to-observable kernels | `UNINET_COSMOLOGY_LCDM_SECTION.md` |
| PS-012 | CMB multipole residual template prediction | deferred | `COS-DEF-005` | cosmology packaging | explicit forward Boltzmann transfer map | `UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md` |
| PS-013 | Black-hole Page/firewall/microstate quantitative claims | deferred | `GR-BH-DEF-004/005` | leaky/trapping + coarse-graining theorem | operational estimator + threshold + waveform maps | `UNINET_GR_FALSIFIABILITY_MATRIX.md` |
| PS-014 | Noether promotions beyond current symmetry theorems | deferred | `UNINET_NOETHER_SYMMETRY_SECTION.md` | action + symmetry generators + boundary terms | full Noether pipeline not frozen (`deferred-noether` subtype) | `UNINET_NOETHER_SYMMETRY_SECTION.md` |
| PS-015 | Spin-statistics operational use in SM packaging | external-constraint | `../docs_input/UNINET_CORE_AXIOMS.md:826` | relies on external theorem class | internal derivation out of scope currently | `UNINET_SM_SECTION.md` |
| PS-016 | Buffering induces dynamic weighted geometry, global Lorentzian envelope, and curved Lorentzian emergence (conditional) | proved | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` | Tier-0 + continuity + bridge/closure assumptions + external curvature/causal bridge | remains conditional on explicit assumptions `P-C1` to `P-C5` and `E1` to `E4` | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` |
| PS-017 | UniNet has a non-empty open geometric Regge regime around an isotropic seed (conditional) | proved | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` | isotropic-branch corollary + equilateral seed refinement + continuity/openness of simplicial admissibility | uniform refinement control and one explicit observationally viable seed still not established | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` |
| PS-018 | UniNet effective costs land in the Regge dynamical class | deferred | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` | geometric Regge regime + action identification + source correspondence + variation compatibility | full `R1` bridge not yet proved | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` |
| PS-019 | Non-empty observationally admissible Regge-dynamical regime | deferred | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` | observational windows + geometric Regge regime + Regge dynamical embedding | one explicit seed in $Theta_obs n Theta_Regge,dyn$ not yet constructed | `UNINET_BUFFERING_TO_EFFECTIVE_EDGE_GEOMETRY_PROOF.md` |

## 4. Review Rule

Any manuscript statement should map to one ledger row.  
If not yet mapped, it is treated as `deferred` until added with explicit status and blocker.

## 5. Promotion Queue (Next Critical Steps)

1. Promote PS-007: complete GR action-variation closure with regularity assumptions.
2. Promote PS-010: complete explicit gauge-group emergence proof path.
3. Promote PS-013: freeze Page/ringdown estimators and binary reject thresholds.
4. Promote PS-014: complete Noether action-domain theorem package.
5. Promote PS-018: prove the UniNet-to-Regge dynamical-class bridge (`R1`).
6. Promote PS-019: construct one explicit seed in the observationally admissible Regge-dynamical regime.





