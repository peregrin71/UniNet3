# UniNet Update Operator Constraints and Candidate Forms
Date: 2026-03-30
Status: Expository / Non-Axiomatic Consolidation

## 1. Purpose and Scope
This document consolidates **all known constraints on the UniNet update operator** $U$ into a single place. It introduces **no new axioms**. Its purpose is:

1. To make explicit why the update rule is *severely constrained*.
2. To show that only a narrow class of operators survives these constraints.
3. To explain why the surviving forms will look **familiar** to physicists (e.g., deterministic wave evolution).

This document supports *recognition*, not novelty.

---
## 2. Hard Constraints from Tier‑0 Axioms

### C0.1 Unitarity
$U^\dagger U = I$
- Guarantees exact information conservation.
- Eliminates dissipative, stochastic, or collapse‑based updates at Tier‑0.

### C0.2 Graph Locality
- $U$ factorizes into node‑local and edge‑local operations.
- No amplitude may propagate faster than one graph edge per tick.
- Implies finite causal cones and bounded influence speed.

### C0.3 No Phenomenological Delays
- Latency is *derived* from locality, not encoded in $U$.
- Forbids arbitrary edge‑dependent delays or hidden clocks.

---
## 3. Structural Constraints from Derived Theorems

### C1. Cut Balance / Boundary Mediation
- Regional change obeys:
  $Q_{n+1}(R) - Q_n(R) = -\Phi_n(\partial R)$
- $U$ must admit a divergence‑form flux representation.
- Enforces boundary‑mediated influence (no direct interior shortcuts).

### C2. Gauge as Boundary Redundancy
- Internal relabelings that preserve boundary observables are physically redundant.
- $U$ must respect equivalence classes under cut‑observable invariance.

### C3. Bandwidth and Stability
- Boundary bandwidth growth constrains how many independent modes $U$ may mix.
- Excludes highly entangling or chaotic global unitaries.

---
## 4. Regime‑Specific Constraints

### C4. QM Regime (Static Latency)
- Latency is fixed: $\delta(u,v) = d_G(u,v)$.
- Queue/backpressure effects do **not** modify propagation.
- $U$ must be time‑homogeneous and spectrally stable.

### C5. GR Regime (Adaptive Latency)
- Effective delays emerge *after* coarse‑graining.
- $U$ remains unitary and local; only the projection is modified.

---
## 5. Standard‑Model Admissibility Constraints

### C6. Chiral Block Structure
$\mathcal{H}_v = \mathcal{H}_v^L \oplus \mathcal{H}_v^R$
- $U$ must respect block structure with bounded off‑diagonal mixing.

### C7. Bounded Chirality Mixing
$0 < ar{\epsilon}_{mix} \ll 1$
- Excludes both exact parity symmetry and strong non‑perturbative mixing.

### C8. CP Non‑Commutation
$\epsilon_{CP} = rac12 \|[CP, U]\|_{op} > 0$
- Small but non‑zero CP violation required.

### C9. Anomaly Compatibility
- Only anomaly‑free representations are admissible.

---
## 6. What Survives These Constraints

Admissible update operators:
- Are **deterministic and unitary**.
- Are **local and causal**.
- Have **block‑structured internal space**.
- Lie near **symmetry‑protected fixed points**.
- Are stable under coarse‑graining.

They generically resemble:
- Discrete‑time quantum walks
- Split‑step / coin‑shift operators
- Lattice propagators
- Floquet operators near constrained windows

---
## 7. Interpretation Note
UniNet does **not** claim a unique update rule. It claims:

> *Any viable update rule must live in a narrow, familiar equivalence class.*

Novelty enters through **what is observed**, not the underlying deterministic update.

---
## 8. Status Summary
- No new axioms introduced.
- Constraints sourced purely from existing UniNet documents.

---
## 9. Fundamental One‑Dimensionality of the Update

### C10. One-Dimensional Update Parameter
The UniNet update operator is fundamentally **one-dimensional** in the evolution parameter:
$\psi_{n+1} = U\,\psi_n.$

- No spatial dimensions encoded directly into $U$.
- Geometry is emergent, not fundamental.

### C11. Emergent Dimensionality via Relational Structure
Spatial dimensionality arises from:
- graph connectivity,
- bandwidth growth,
- accessible boundary information,
- coarse‑graining structure.

Embedding geometry directly into $U$ violates locality and latency derivation.

---
## 10. Observational Pruning of the Operator Class

### C12. Quantum Constraints
- Interference, spectra, and coherence times prune unstable spectra.

### C13. SM Constraints
- Chirality, CPV, anomaly cancellation eliminate most internal structures.

### C14. Cosmological Constraints
- CMB multipoles, growth of structure, and IR stability constrain long‑wavelength modes.

These **prune** the admissible operator class; they do not change its fundamental form.

---
## 11. Consolidated Statement
> *The UniNet update operator is a one-dimensional, local, unitary, deterministic wave-propagation operator. Theory restricts it to a narrow, familiar equivalence class; observations from quantum to cosmology prune it further without altering its core structure.*

---
**End of document (updated)**
