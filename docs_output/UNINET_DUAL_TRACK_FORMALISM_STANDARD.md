# UniNet Dual-Track Formalism Standard v1

Date: 2026-03-30  
Purpose: keep derivations readable in current UniNet notation while adding an action/Lagrangian formulation where it materially improves rigor and reviewer transparency.

## 1. Core Policy

1. Every major claim keeps a **primary formula** in current UniNet notation.
2. Where possible, add a **Lagrangian/action companion** formula.
3. If both forms are present, include a short equivalence note ("native form <-> Euler-Lagrange/variational form").

## 2. When Lagrangian Form Is Mandatory

1. Field/dynamics claims derived from stationarity or variational principles.
2. Source-curvature coupling claims.
3. Claims explicitly marketed as Noether/symmetry-conservation results.

## 3. When Lagrangian Form Is Optional

1. Pure kinematic definitions (causal order, horismos, metric signatures, bookkeeping definitions).
2. Purely operational observables in falsifiability matrices.
3. Early build-up claims with no frozen action domain yet (must be tagged `deferred` or `postulate`).

## 4. Section-Level Guidance

1. **QM:** keep $\psi_{n+1}=U\psi_n$ primary; optional discrete-action companion for audiences expecting variational framing.
2. **GR:** keep adaptive-latency/source equations primary; include action-based derivation where theorem claims depend on variation.
3. **SM:** keep transfer/chirality/CP constraints primary; optional penalty-functional/action encoding for admissible-operator class.
4. **Cosmology:** keep effective fluid/background equations primary; add effective action forms where assumptions are explicit.
5. **Queueing:** keep continuity/drift identities primary; optional constrained-action form using conservation multipliers.

## 5. Deduction Writing Rule

1. Deduction text should remain readable in current notation.
2. Add a compact Lagrangian companion block under each major theorem when available.
3. Do **not** replace readable deductions with Lagrangian-only proofs unless the claim is in the mandatory class above.

## 6. Reviewer-Facing Presentation Rule

For each theorem candidate:

1. "Native statement" (current notation).
2. "Variational companion" (if applicable).
3. "Status tag" from `UNINET_PROOF_STATUS_LEDGER.md`.
4. "Boundary note" if companion form is incomplete/deferred.





