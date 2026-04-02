# Reorganization Plan Tracking (`docs_input` only)

## Locked Decisions
- [x] Core policy: keep abstract + pointer stubs in `UNINET_CORE_AXIOMS.md` after migration.
- [x] ID policy: sector IDs only in destination docs.
- [x] Scope policy: apply this pass to `docs_input` only.

## A) No-Loss Scaffolding
- [ ] `MIG-00` Add migration ledger section in core: historical label -> new sector ID -> destination section.
- [ ] `MIG-01` Snapshot all source blocks before edits into a temporary migration appendix/work artifact.
- [ ] `MIG-02` Enforce copy-verify-replace workflow (no replace before successful destination copy verification).
- [ ] `MIG-03` For every move item, execute mandatory sequence:
  - [ ] `COPY` full theorem/corollary/definition text to destination section first.
  - [ ] `COMPARE` destination vs source for full content equivalence (equations, status tags, notes, consequences).
  - [ ] `REMOVE` source text only after compare passes.
- [ ] `MIG-04` Log verification evidence per move item in migration ledger (source anchor, destination anchor, compare result).

## B) Moves to QM Sector (`UNINET_QM_SECTION.md`)
- [ ] `QM-01` Move `Core:1148-1152` (QM regime axiom block) -> `Q8.1`.
- [ ] `QM-02` Move `Core:1153-1159` (QM latency theorem) -> `Q2.3`.
- [ ] `QM-03` Move `Core:695-703` (QM corollary 3.1) -> `Q8.2`.

## C) Moves to GR Sector (`UNINET_GR_SECTION.md`)
- [ ] `GR-01` Move `Core:704-708` (GR corollary 3.2) -> `M4.4`.
- [ ] `GR-02` Move `Core:513-531` (Theorem 1.4 trapping bound) -> `M8.3`.
- [ ] `GR-03` Move `Core:532-540` (Corollary 1.2 boundary-dominant release) -> `M8.4`.
- [ ] `GR-04` Move `Core:866-879` (`R9`) -> GR transport constraints block (`A7` + `M8`).
- [ ] `GR-05` Move `Core:882-891` (`R10`) -> GR transport constraints block (`A7` + `M8`).
- [ ] `GR-06` Move `Core:1050-1064` (Axiom 4.1 projection) -> `M3.1`.
- [ ] `GR-07` Move `Core:1066-1084` (Definition 4.1 worldline/proper time) -> `M4.1`.
- [ ] `GR-08` Move `Core:1086-1102` (Axiom 4.2 buffering-to-energy projection) -> `M7.1`.
- [ ] `GR-09` Move `Core:1104-1114` (Axiom 4.3 lightspeed mapping) -> `M3.4`.
- [ ] `GR-10` Move `Core:1116-1125` (Theorem 4.1 buffering couples to geometry) -> `M7.4`.
- [ ] `GR-11` Move `Core:1127-1141` (Definition 4.2 saturation bound) -> `M8.1B`.
- [ ] `GR-12` Move `Core:1165-1170` (GR regime axiom block) -> `A5.1`.
- [ ] `GR-13` Move `Core:1171-1181` (GR adaptive latency theorem) -> `M4.2`.

## D) Moves to SM Sector (`UNINET_SM_SECTION.md`)
- [ ] `SM-01` Move `Core:709-713` (SM corollary 3.3) -> `S3.2`.
- [ ] `SM-02` Move `Core:757-795` (`R5` chiral structure preservation) -> `S2.1`.
- [ ] `SM-03` Move `Core:798-823` (`R6` CP symmetry/violation) -> `S3.1`.
- [ ] `SM-04` Move `Core:826-840` (`R7` spin-statistics) -> `S4.C`.
- [ ] `SM-05` Move `Core:843-862` (`R8` admissible window) -> `S9.1`.
- [ ] `SM-06` Move `Core:1344-1348` (Corollary 1A.1 gauge-constraint note) -> `S5.3`.
- [ ] `SM-07` Move `Core:1406-1420` (Theorem 1C.1 standing/quasi-standing particle modes) -> `S0.1`.

## E) Moves to Cosmology Sector (`UNINET_COSMOLOGY_LCDM_SECTION.md`)
- [ ] `COS-01` Move `Core:1188-1197` (Dark Energy mechanism/equation/observable) -> `C3.1`.
- [ ] `COS-02` Move `Core:1200-1206` (Dark Matter mechanism/observable) -> `C4.1`.
- [ ] `COS-03` Move `Core:1209-1217` (Inflation mechanism/e-folds/observable) -> `C5.1`.

## F) Core Cleanup After Successful Moves
- [ ] `CORE-01` Replace moved source blocks with abstract + pointer stubs.
- [ ] `CORE-02` Keep universal Tier 0-3 and cross-sector Tier 1A/1B in core, except moved SM-specific blocks.
- [ ] `CORE-03` Add Sector Theorem Index table in core for traceability.

## G) Provenance / Reference Rewiring
- [ ] `REF-01` Update moved-line references in:
  - [ ] `UNINET_AXIOM_TO_PREDICTION_DAG.md`
  - [ ] `UNINET_QM_SECTION.md`
  - [ ] `UNINET_GR_SECTION.md`
  - [ ] `UNINET_SM_SECTION.md`
  - [ ] `UNINET_COSMOLOGY_LCDM_SECTION.md`
- [ ] `REF-02` Update moved-line references in matrices/ledgers:
  - [ ] `UNINET_QM_FALSIFIABILITY_MATRIX.md`
  - [ ] `UNINET_GR_FALSIFIABILITY_MATRIX.md`
  - [ ] `UNINET_SM_FALSIFIABILITY_MATRIX.md`
  - [ ] `UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md`
  - [ ] `UNINET_PARAMETER_LEDGER.md`
  - [ ] `UNINET_PROOF_STATUS_LEDGER.md`
  - [ ] `UNINET_PHILOSOPHICAL_RESULTS_SECTION.md`
- [ ] `REF-03` Update `UNINET_FALSIFIABILITY_STANDARD.md` to allow theorem-ID provenance targets (not only line anchors).

## H) Logical Build-Up Validation
- [ ] `VAL-QM` Validate theorem order in QM: Q1 -> Q2 -> Q3 -> Q4 -> Q5/Q6 -> Q8 -> Q9.
- [ ] `VAL-GR` Validate theorem order in GR: M1 -> M2 -> M3 -> M4 -> M7 -> M8 -> M9.
- [ ] `VAL-SM` Validate theorem order in SM: S0 -> S1 -> S2 -> S3 -> S4 -> S5 -> S9 -> S10.
- [ ] `VAL-COS` Validate theorem order in Cosmology: C1/C2 -> C3 -> C4 -> C5 -> C6+.

## I) Final No-Loss Acceptance
- [ ] `ACC-01` Every moved theorem appears exactly once as full canonical text in destination sector doc.
- [ ] `ACC-02` Core contains pointer stubs (not full duplicates) for moved items.
- [ ] `ACC-03` No stale references to moved core line anchors remain for migrated items.
- [ ] `ACC-04` Theorem accounting check passes: retained + moved equals original inventory.
- [ ] `ACC-05` Migration ledger completeness check passes (one-to-one source -> destination mapping).
- [ ] `ACC-06` Every move item has explicit `COPY -> COMPARE -> REMOVE` evidence recorded and complete.
