# Relabeling Plan (Reorganized)

Scope: in-place relabel/reclassification only for this pass.
Rule: no theorem/axiom body moves across files in this pass.
Tracking style: each master relabel has its own checkbox, with file:line sub-checkboxes.

## Execution Locks
- [x] LOCK-01 Keep all content in place (`docs_input/UNINET_CORE_AXIOMS.md` stays the source document).
- [x] LOCK-02 Preserve statement bodies; change only labels/order/role tags unless explicitly listed.
- [x] LOCK-03 Update mirrored references in both `docs_input` and `docs`.
- [x] LOCK-04 Include `docs/20_proofs` reference updates in this pass.

## Core Logical Order (Target)
- [x] ORDER-01 Position 1: `AXIOM-1` Graph substrate.
- [x] ORDER-02 Position 2: `AXIOM-2` Relabeling invariance.
- [x] ORDER-03 Position 3: `AXIOM-3` Discrete update ordering parameter $n$.
- [x] ORDER-04 Position 4: `AXIOM-4` One update rule family.
- [x] ORDER-05 Position 5: `AXIOM-5` Update homogeneity.
- [x] ORDER-06 Position 6: `AXIOM-6` Locality.
- [x] ORDER-07 Position 7: `AXIOM-7` No information loss.
- [x] ORDER-08 Position 8: `AXIOM-8` Graph cutting primitive.
- [x] ORDER-09 Position 9: `AXIOM-9` Boundary observability principle.
- [x] ORDER-10 Position 10: `AXIOM-10` Standing-wave particle principle.

## Master Relabels

### MR-01 `Axiom 0.1 -> AXIOM-1` (Graph substrate)
- [x] MR-01 Master complete.
- [ ] MR-01.01 `docs_input/UNINET_CORE_AXIOMS.md:225`
- [ ] MR-01.02 `docs/10_sections/01_gr_section.md:20`
- [ ] MR-01.03 `docs_input/UNINET_GR_SECTION.md:20`
- [ ] MR-01.04 `docs/40_governance/02_proof_status_ledger.md:27`
- [ ] MR-01.05 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:27`
- [ ] MR-01.06 `docs/50_programs/07_parameter_ledger.md:34,35,36`
- [ ] MR-01.07 `docs_input/UNINET_PARAMETER_LEDGER.md:34,35,36`

### MR-02 `S1 (Graph Isomorphism Invariance) -> AXIOM-2` (Relabeling invariance)
- [x] MR-02 Master complete.
- [ ] MR-02.01 `docs_input/UNINET_CORE_AXIOMS.md:932-942`
- [ ] MR-02.02 `docs/10_sections/01_gr_section.md:52`
- [ ] MR-02.03 `docs_input/UNINET_GR_SECTION.md:52`
- [ ] MR-02.04 `docs/10_sections/05_noether_symmetry_section.md:24`
- [ ] MR-02.05 `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:24`

### MR-03 `Axiom 0.2 -> AXIOM-3` (Discrete update ordering)
- [x] MR-03 Master complete.
- [ ] MR-03.01 `docs_input/UNINET_CORE_AXIOMS.md:234`
- [ ] MR-03.02 `docs_input/UNINET_CORE_AXIOMS.md:26` (legacy mis-citation to fix during relabel)
- [ ] MR-03.03 `docs/10_sections/01_gr_section.md:45`
- [ ] MR-03.04 `docs_input/UNINET_GR_SECTION.md:45`
- [ ] MR-03.05 `docs/50_programs/07_parameter_ledger.md:50`
- [ ] MR-03.06 `docs_input/UNINET_PARAMETER_LEDGER.md:50`

### MR-04 `Axiom 0.5 -> AXIOM-6` (Locality)
- [x] MR-04 Master complete.
- [ ] MR-04.01 `docs_input/UNINET_CORE_AXIOMS.md:280`
- [ ] MR-04.02 `docs_input/UNINET_CORE_AXIOMS.md:333,347,755`
- [ ] MR-04.03 `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:355`
- [ ] MR-04.04 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:40`
- [ ] MR-04.05 `docs/10_sections/02_qm_section.md:19`
- [ ] MR-04.06 `docs_input/UNINET_QM_SECTION.md:19`
- [ ] MR-04.07 `docs/30_falsifiability/02_qm_falsifiability_matrix.md:9`
- [ ] MR-04.08 `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:9`
- [ ] MR-04.09 `docs/10_sections/01_gr_section.md:20`
- [ ] MR-04.10 `docs_input/UNINET_GR_SECTION.md:20`
- [ ] MR-04.11 `docs/40_governance/02_proof_status_ledger.md:27`
- [ ] MR-04.12 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:27`

### MR-05 `Axiom 0.4 -> AXIOM-7` (No information loss)
- [x] MR-05 Master complete.
- [ ] MR-05.01 `docs_input/UNINET_CORE_AXIOMS.md:298`
- [ ] MR-05.02 `docs_input/UNINET_CORE_AXIOMS.md:373,672,762,947`
- [ ] MR-05.03 `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:18,355`
- [ ] MR-05.04 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:39`
- [ ] MR-05.05 `docs/30_falsifiability/02_qm_falsifiability_matrix.md:10`
- [ ] MR-05.06 `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:10`
- [ ] MR-05.07 `docs/50_programs/06_philosophical_results_section_plan.md:46`
- [ ] MR-05.08 `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION_PLAN.md:46`
- [ ] MR-05.09 `docs/10_sections/06_philosophical_results_section.md:17,27`
- [ ] MR-05.10 `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:17,27`
- [ ] MR-05.11 `docs/10_sections/02_qm_section.md:18`
- [ ] MR-05.12 `docs_input/UNINET_QM_SECTION.md:18`
- [ ] MR-05.13 `docs/10_sections/01_gr_section.md:20`
- [ ] MR-05.14 `docs_input/UNINET_GR_SECTION.md:20`
- [ ] MR-05.15 `docs/40_governance/02_proof_status_ledger.md:27`
- [ ] MR-05.16 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:27`

### MR-06 `NEW -> AXIOM-4` (One update rule family)
- [x] MR-06 Master complete.
- [x] MR-06.01 `docs_input/UNINET_CORE_AXIOMS.md` (insert canonical axiom block near current update-law assumptions)
- [x] MR-06.02 `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:5-10,15`
- [x] MR-06.03 `docs/00_foundation/02_update_operator_constraints.md:5-10,15`
- [x] MR-06.04 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:39-45` (axiom labels refresh)

### MR-07 `NEW -> AXIOM-5` (Update homogeneity)
- [x] MR-07 Master complete.
- [x] MR-07.01 `docs_input/UNINET_CORE_AXIOMS.md` (insert canonical axiom block near locality decomposition)
- [x] MR-07.02 `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:22-24`
- [x] MR-07.03 `docs/00_foundation/02_update_operator_constraints.md:22-24`
- [x] MR-07.04 `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:137` (node-uniform response terminology alignment)

### MR-08 `Definition 1.4 -> AXIOM-8` (Graph cutting primitive)
- [x] MR-08 Master complete.
- [ ] MR-08.01 `docs_input/UNINET_CORE_AXIOMS.md:465`
- [ ] MR-08.02 `docs_input/UNINET_CORE_AXIOMS.md:1369`
- [ ] MR-08.03 `docs/30_falsifiability/03_gr_falsifiability_matrix.md:14`
- [ ] MR-08.04 `docs_input/UNINET_GR_FALSIFIABILITY_MATRIX.md:14`

### MR-09 `Boundary observability blocks -> AXIOM-9`
- [x] MR-09 Master complete.
- [x] MR-09.01 `docs_input/UNINET_CORE_AXIOMS.md:440` (current Definition 1.3 source)
- [x] MR-09.02 `docs_input/UNINET_CORE_AXIOMS.md:1326,1356-1359,1362-1371` (operational boundary-observable statements)
- [x] MR-09.03 `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:39`
- [x] MR-09.04 `docs/00_foundation/02_update_operator_constraints.md:39`
- [x] MR-09.05 `docs_input/UNINET_QUANTUM_SIMULATOR.md:33`

### MR-10 `Theorem 1C.1 -> AXIOM-10` (Standing-wave particle principle)
- [x] MR-10 Master complete.
- [ ] MR-10.01 `docs_input/UNINET_CORE_AXIOMS.md:1441`
- [ ] MR-10.02 `docs_input/UNINET_SM_SECTION.md:29`
- [ ] MR-10.03 `docs/10_sections/03_sm_section.md:29`
- [ ] MR-10.04 `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:355`

### MR-11 `Axiom 0.3 -> MODEL-P1` (Modeling choice, not minimal core)
- [x] MR-11 Master complete.
- [ ] MR-11.01 `docs_input/UNINET_CORE_AXIOMS.md:265`
- [ ] MR-11.02 `docs/10_sections/02_qm_section.md:18`
- [ ] MR-11.03 `docs_input/UNINET_QM_SECTION.md:18`
- [ ] MR-11.04 `docs/50_programs/07_parameter_ledger.md:37`
- [ ] MR-11.05 `docs_input/UNINET_PARAMETER_LEDGER.md:37`

### MR-11B `Axiom 0.6 -> MODEL-P2` (Operational buffering layer)
- [x] MR-11B Master complete.
- [x] MR-11B.01 `docs_input/UNINET_CORE_AXIOMS.md:314`
- [x] MR-11B.02 `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:355`
- [x] MR-11B.03 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:17,28,41`
- [x] MR-11B.04 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG_v2.md:5`
- [x] MR-11B.05 `docs/30_falsifiability/06_axiom_to_prediction_dag.md:5`
- [x] MR-11B.06 `docs/40_governance/02_proof_status_ledger.md:28`
- [x] MR-11B.07 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:28`

### MR-12 `Axiom 0.7 (+R5-R8 linkage) -> SM-FOUND-A1` (in-place reclassification)
- [x] MR-12 Master complete.
- [ ] MR-12.01 `docs_input/UNINET_CORE_AXIOMS.md:333`
- [ ] MR-12.02 `docs_input/UNINET_CORE_AXIOMS.md:792,833,861,1274`
- [ ] MR-12.03 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:80,81`
- [ ] MR-12.04 `docs/10_sections/03_sm_section.md:18,19,20,21,22,40`
- [ ] MR-12.05 `docs_input/UNINET_SM_SECTION.md:18,19,20,21,22,40`
- [ ] MR-12.06 `docs/40_governance/02_proof_status_ledger.md:35,41`
- [ ] MR-12.07 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:35,41`
- [ ] MR-12.08 `docs/30_falsifiability/04_sm_falsifiability_matrix.md:9,10,11,12`
- [ ] MR-12.09 `docs_input/UNINET_SM_FALSIFIABILITY_MATRIX.md:9,10,11,12`
- [ ] MR-12.10 `docs/30_falsifiability/05_cosmology_lcdm_falsifiability_matrix.md:12`
- [ ] MR-12.11 `docs_input/UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md:12`
- [ ] MR-12.12 `docs/50_programs/07_parameter_ledger.md:37,38,39,40,41,61`
- [ ] MR-12.13 `docs_input/UNINET_PARAMETER_LEDGER.md:37,38,39,40,41,61`

### MR-13 `Axiom 4.1 -> BRIDGE-P1`
- [x] MR-13 Master complete.
- [ ] MR-13.01 `docs_input/UNINET_CORE_AXIOMS.md:1085`
- [ ] MR-13.02 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:44`
- [ ] MR-13.03 `docs/10_sections/01_gr_section.md:23,51,52`
- [ ] MR-13.04 `docs_input/UNINET_GR_SECTION.md:23,51,52`
- [ ] MR-13.05 `docs/10_sections/04_cosmology_lcdm_section.md:19`
- [ ] MR-13.06 `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:19`
- [ ] MR-13.07 `docs/50_programs/07_parameter_ledger.md:47`
- [ ] MR-13.08 `docs_input/UNINET_PARAMETER_LEDGER.md:47`

### MR-14 `Axiom 4.2 -> BRIDGE-P2`
- [x] MR-14 Master complete.
- [ ] MR-14.01 `docs_input/UNINET_CORE_AXIOMS.md:1121`
- [ ] MR-14.02 `docs_input/UNINET_CORE_AXIOMS.md:1272`
- [ ] MR-14.03 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:44`
- [ ] MR-14.04 `docs/40_governance/02_proof_status_ledger.md:34`
- [ ] MR-14.05 `docs_input/UNINET_PROOF_STATUS_LEDGER.md:34`
- [ ] MR-14.06 `docs/10_sections/01_gr_section.md:23`
- [ ] MR-14.07 `docs_input/UNINET_GR_SECTION.md:23`
- [ ] MR-14.08 `docs/10_sections/04_cosmology_lcdm_section.md:19`
- [ ] MR-14.09 `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:19`
- [ ] MR-14.10 `docs/50_programs/07_parameter_ledger.md:48`
- [ ] MR-14.11 `docs_input/UNINET_PARAMETER_LEDGER.md:48`

### MR-15 `Axiom 4.3 -> BRIDGE-P3`
- [x] MR-15 Master complete.
- [ ] MR-15.01 `docs_input/UNINET_CORE_AXIOMS.md:1139`
- [ ] MR-15.02 `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:44`
- [ ] MR-15.03 `docs/10_sections/01_gr_section.md:23`
- [ ] MR-15.04 `docs_input/UNINET_GR_SECTION.md:23`
- [ ] MR-15.05 `docs/10_sections/04_cosmology_lcdm_section.md:19`
- [ ] MR-15.06 `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:19`
- [ ] MR-15.07 `docs/50_programs/07_parameter_ledger.md:49,50,51,54`
- [ ] MR-15.08 `docs_input/UNINET_PARAMETER_LEDGER.md:49,50,51,54`

## Final Validation
- [x] VAL-01 Search returns no stale explicit labels: `Axiom 0.x`, `Axiom 4.x`, `Definition 1.4`, `Theorem 1C.1` where relabeled.
- [x] VAL-02 Search returns no stale core line-anchors tied to replaced labels.
- [x] VAL-03 Core axioms are in target logical order (`ORDER-01` .. `ORDER-10`).
- [x] VAL-04 No content-move occurred across files (in-place policy held).





