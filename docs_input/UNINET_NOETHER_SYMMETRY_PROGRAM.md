# UniNet Noether and Symmetry Program (Rigor Track)

Date: 2026-03-30  
Purpose: formalize which symmetry claims are already theorem-level, which are Noether-like invariants, and which require additional action-level assumptions before promotion.

## 1. Scope Lock

1. This document is a theorem-status registry, not a new-axiom source.
2. No claim is promoted to "true Noether theorem" unless a symmetry action and variational domain are explicitly defined.
3. Cross-sector references (QM/GR/SM/Cosmology) are allowed only through already-declared core structures.
4. Equation presentation follows `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

## 2. Status Taxonomy

1. `theorem-now`: derivable from current core axioms/definitions.
2. `noether-like`: invariant/constraint structurally analogous to Noether output, but missing a complete action-symmetry proof pipeline.
3. `deferred-noether`: requires additional formal setup (continuous family, differentiability class, boundary terms, or finite parameterization).

## 3. Current Registry

| item_id | claim | status | current basis | promotion blocker |
|---|---|---|---|---|
| NS-001 | Graph relabeling covariance (`S1`) | theorem-now | Graph isomorphism invariance in core symmetries block | none |
| NS-002 | QM time-translation invariance in static regime (`S2`) | theorem-now | Time-independent update and regime assumptions | none |
| NS-003 | Locality-preserving conjugation symmetry (`S3`) | theorem-now | Local unitary conjugation structure | none |
| NS-004 | Pseudo-unitary projected invariance (`S4`) | noether-like | Explicit design-goal symmetry in projected block | Needs full action + generator relation |
| NS-005 | Norm conservation (`C1`) | theorem-now | Unitarity (`U^\dagger U=I`) | none |
| NS-006 | Entropy/closure-style invariants under coarse-graining constraints | noether-like | Core continuity + queue/cut bookkeeping theorems | Needs full observable functional and domain class |
| NS-007 | Source-curvature conservation compatibility (Bianchi-style) | deferred-noether | Present in GR rigor plan obligations | Requires finalized discrete action and variation space |

## 4. Theorem Discipline for "True Noether" Promotion

To promote any `noether-like` or `deferred-noether` item:

1. Specify the action functional and admissible field/state space.
2. Specify the symmetry group action on that space.
3. Prove differentiability/variation assumptions and boundary-term handling.
4. Derive conserved current/charge relation explicitly.
5. State exact scope (QM-only, GR-only, or cross-regime).

## 5. Cross-Sector Integration Targets

1. QM: connect symmetry generators to protocol-level invariants in quantum-walk tests.
2. GR: connect action symmetries to conservation compatibility and boundary-flux statements.
3. SM: connect internal symmetry candidates to representation/anomaly constraints.
4. Cosmology: connect background symmetry assumptions to conserved effective fluid relations.

## 6. Near-Term Deliverables

1. `Noether Ledger v1`: symmetry groups, domains, and claim status for every symmetry statement used in active docs.
2. `Discrete-Action Preconditions Note`: exact mathematical assumptions needed for theorem-level Noether promotion.
3. `Promotion Patch Set`: convert eligible `noether-like` claims to `theorem-now` with explicit proofs.



