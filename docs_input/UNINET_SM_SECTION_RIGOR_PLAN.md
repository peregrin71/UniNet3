# UniNet SM Section: Full-Rigor Build Plan (Mapping-Complete)

**Date:** 2026-03-30  
**Primary source of truth:** `../docs_input/UNINET_CORE_AXIOMS.md` only  
**Secondary role of `UNINET_MERGED.md`:** inspiration only; no imported assumptions.

---

## 1. Entry Criterion and Scope Lock

Start condition for the SM section:

1. Use only Tier-0 plus transfer constraints `R5-R8` as formal inputs.
2. Any statement about gauge group emergence, family structure, or mass hierarchies must carry claim type:
   - `Derived`,
   - `Conjecture`,
   - `Postulate`,
   - `External theorem constraint`.
3. No claim of full Standard Model recovery unless all subgroup, anomaly, and representation checks are explicit.
4. Symmetry-to-conservation promotion must follow `UNINET_NOETHER_SYMMETRY_PROGRAM.md`.
5. Notation/units and claim-status tags must follow `UNINET_NOTATION_UNITS_STANDARD.md` and `UNINET_PROOF_STATUS_LEDGER.md`.
6. Dual-track formula policy (native transfer constraints + optional variational encoding) must follow `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

---

## 2. Mapping-Complete Targets (Mandatory)

1. **S1: Chiral Hilbert Structure -> Mode Taxonomy**
   - Define physical mode classes from $H_v^L \oplus H_v^R$.

2. **S2: Chiral Transfer Blocks -> Controlled Mixing Sector**
   - Use block-unitarity constraints and $\epsilon_{\mathrm{mix}}$ windows.

3. **S3: CP Operator -> Quantified CP Breaking**
   - Use real chiral phases and $\epsilon_{\mathrm{CP}} = 1/2 ||[CP,U]||_op$.

4. **S4: Exchange Symmetry Constraints -> Fermion/Boson Sectors**
   - Formalize where spin-statistics enters as external theorem constraint.

5. **S5: Effective Gauge Structure Map**
   - Map admissible transfer symmetries to candidate internal gauge algebra.

6. **S6: Representation and Anomaly Consistency**
   - Check anomaly cancellation and chirality consistency conditions.

7. **S7: Flavor/Family Structure and Mixing**
   - Define family labels, mixing matrices, and CP invariants in-model.

8. **S8: Observable Interface**
   - Map internal invariants to measurable quantities ($\epsilon_K$, CKM/PMNS, violation bounds).

9. **S9: Non-emptiness and Tightness of Admissible `U`**
   - Construct at least one explicit admissible class satisfying all SM-side constraints.

10. **S10: Periodic-Mode/Floquet Stability Interface**
   - Formalize periodic mode classes, multiplier-based stability, and lifetime mapping without over-claiming full particle derivation.

---

## 3. Required Structure of the New SM Document

Recommended target file: `UNINET_SM_SECTION.md`

1. Contract and claim taxonomy.
2. Assumption ledger (`R5-R8`, plus any explicit postulates).
3. Chiral/CP block (S1-S3).
4. Statistics and representation block (S4-S6).
5. Flavor/family block (S7).
6. Observable mapping block (S8).
7. Non-emptiness and falsification block (S9).
8. Periodic-mode/Floquet block (S10).
9. Deferred derivations list (honest boundary).
10. Dual-track appendix for admissible-operator constraints.

---

## 4. Proof Obligations by Mapping

### S1-S3
- `Definition S1.1`: mode class and chirality labels.
- `Theorem S2.1`: admissible block-unitary transfer identities.
- `Theorem S3.1`: CP operator norm-preserving property and CP-breaking metric properties.
  Native targets: `\epsilon_{\mathrm{mix}}`, `\epsilon_{\mathrm{CP}}=\frac12\|[\mathsf{CP},U]\|_{\mathrm{op}}`.
  Optional variational companion: constrained/penalized functional over admissible `U` enforcing unitarity, locality, and chirality-window constraints.

### S4
- `Definition S4.1`: exchange action on multi-mode states.
- `Constraint S4.C`: spin-statistics imported theorem boundary and usage conditions.

### S5-S6
- `Definition S5.1`: effective internal connection/algebra induced by transfer symmetries.
- `Theorem or Postulate S5.2`: subgroup emergence claim ($U(1)\times SU(2)\times SU(3)$ status explicitly tagged).
- `Theorem S6.1`: anomaly-cancellation conditions in chosen representation class.

### S7
- `Definition S7.1`: family index and mixing operators.
- `Proposition S7.2`: CP-odd invariants supported by model structure.

### S8-S9
- `Definition S8.1`: map from internal invariants to observables.
- `Theorem/Proposition S9.1`: existence of at least one admissible `U` in constrained windows.

### S10
- `Definition S10.1`: periodic mode class and period map.
- `Definition S10.2`: multiplier/stability map for periodic classes (Floquet-style for discrete update).
- `Proposition S10.3`: lifetime proxy relation from multiplier modulus under explicit regularity assumptions.
- `Boundary Note S10.B`: multiplier/lifetime mapping does not by itself prove full particle identity map.

---

## 5. Claim Discipline

1. Do not conflate "compatible with SM" and "derived SM".
2. Every gauge-group claim must list whether it is:
   - proved, or
   - assumed as selection principle.
3. Keep anomaly cancellation explicit; do not state it qualitatively.
4. Keep CP and CPT distinct in wording.
5. Separate numerical calibration from structural derivation.
6. Any "3-family threshold" claim must be explicitly marked as `external theorem constraint` or `deferred derivation`.
7. Keep chirality/CP deductions in native operator notation; add action/penalty-functional companions only when mathematically explicit.

---

## 6. Literature Cross-References (Known Steps)

1. Lee & Yang (1956), parity violation in weak interactions.  
   https://doi.org/10.1103/PhysRev.104.254
2. Adler-Bell-Jackiw anomaly.  
   S. Adler (1969): https://doi.org/10.1103/PhysRev.177.2426  
   J. Bell, R. Jackiw (1969): https://doi.org/10.1007/BF02823296
3. Kobayashi-Maskawa CP mechanism (3 families).  
   https://doi.org/10.1143/PTP.49.652
4. Nielsen-Ninomiya lattice no-go (chirality constraints context).  
   https://doi.org/10.1016/0370-2693(81)91026-1
5. Weinberg, *The Quantum Theory of Fields* (spin-statistics and gauge structure background).
6. PDG review tables for CP and flavor observables (measurement interface).
7. Standard Floquet-theory references for periodic linear systems (used only for S10 stability/lifetime formalism).

---

## 7. Done Criteria for "SM Mapping Complete"

1. S1-S9 all represented by formal statements and dependency tags.
2. Gauge-group status is explicit (`proved` / `postulated` / `conjectured`).
3. CP metric and chirality windows are mathematically coherent and non-empty.
4. At least one admissible transfer family is exhibited.
5. All unresolved steps are listed in a deferred derivations section.
6. Periodic/Floquet block (S10) is present with explicit non-overclaim boundary.

---

## 8. Execution Order

1. Lock S1-S3 formalism first.
2. Add S4 spin-statistics boundary conditions.
3. Build S5-S6 with explicit status tags.
4. Add S7 flavor structure.
5. Add S10 periodic/Floquet interface.
6. Close with S8-S9 observables and non-emptiness proof.






