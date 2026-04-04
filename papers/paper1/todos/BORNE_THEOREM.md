<!--
INSTRUCTIONS FOR RECEIVING LLM:

You are being given a Dependency DAG update for the UniNet manuscript.

Your tasks:
1. Insert the DAG nodes below into the global dependency graph.
2. Maintain the DAG’s topological ordering.
3. Ensure no cycles are introduced.
4. Place each node in the correct tier:
   - Axioms (Tier 0)
   - Shared Theorem Spine (Tier 1)
   - Witness-Level Theorems (Tier 2)
   - Sector-Specific Theorems (Tier 3)
5. Do NOT modify existing nodes unless explicitly instructed.
6. Add cross-links where indicated.
-->

# Dependency DAG Update

This update introduces two new formal results:

- `LEMMA-FLUX-01` — Flux proportional to occupancy  
- `THEOREM-BORN-01` — Born rule as a cut–statistics theorem  

It also introduces one explanatory block (non‑DAG).

---

# DAG Node: LEMMA-FLUX-01
**Tier:** 2 (Witness-Level Theorem)  
**Status:** `proved` (Schrödinger witness), `deferred` (general case)

**Dependencies:**
- `AXIOM-6` (locality)  
- `AXIOM-7` (unitarity)  
- `THEOREM-CUT-01` (bulk–boundary balance)  
- `DEFINITION-CG-01` (coarse-graining map $\Phi_{\mathrm{cg}}$)  
- `MODEL-P2` (occupancy measure)  
- `WITNESS-SCH-01` (Schrödinger-like update family)

**Provides:**
- Expected boundary flux operator  
- Quadratic dependence on occupancy  
- Phase-insensitivity at the boundary  

**Used by:**
- `THEOREM-BORN-01`  
- Any future measurement-statistics theorems  
- Sector-specific detection models  

---

# DAG Node: THEOREM-BORN-01
**Tier:** 1.5 (Shared Theorem Spine Addendum)  
**Status:** `proved` (Schrödinger witness), `deferred` (general case)

**Dependencies:**
- `AXIOM-6` (locality)  
- `AXIOM-7` (unitarity)  
- `THEOREM-CUT-01` (bulk–boundary balance)  
- `DEFINITION-CG-01` (coarse-graining)  
- `DEFINITION-STABLE-01` (stable modes: standing or glider)  
- `LEMMA-FLUX-01`  

**Provides:**
- Born rule as a boundary-statistics theorem  
- Frequency interpretation of measurement  
- Operational meaning of $\|\Pi_i \psi\|^2$  
- QM as cut‑interaction statistics  

**Used by:**
- All QM-facing sector chapters  
- Any scattering or detection model  
- Future “observer theory” chapter  
- Interpretational commentary  

---

# DAG Note: Conceptual Block (Measurement as Cut Interaction)
**Tier:** None (explanatory)  
**Status:** `explanatory`  

**Dependencies:** None  
**Provides:**  
- Reader-facing conceptual clarity  
- Motivation for the Born theorem  
- Ontological interpretation of detectors as regions  

**Used by:**  
- QM introduction  
- Pedagogical sections  
- Explanatory figures  

---

# DAG Cross-Links to Add

1. Add an edge:  
   `WITNESS-SCH-01 → LEMMA-FLUX-01`

2. Add an edge:  
   `LEMMA-FLUX-01 → THEOREM-BORN-01`

3. Add an edge:  
   `DEFINITION-STABLE-01 → THEOREM-BORN-01`

4. Add an edge:  
   `THEOREM-BORN-01 → QM-SECTOR-INTRO`

5. Add an edge:  
   `THEOREM-BORN-01 → DETECTION-MODELS-CHAPTER`

6. Add an edge:  
   `THEOREM-BORN-01 → SCATTERING-CHAPTER` (if present)

---

# DAG Placement Summary

- `LEMMA-FLUX-01` sits **just above** the witness family and **just below** the Born theorem.  
- `THEOREM-BORN-01` sits **in the shared spine**, but **below** the core axioms and **above** any sector-specific QM constructions.  
- The conceptual block is **not part of the DAG**.