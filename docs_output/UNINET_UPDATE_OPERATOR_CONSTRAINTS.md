# UniNet Update Operator Constraints and Candidate Forms (v3)
Date: 2026-03-30
Status: Expository / Non-Axiomatic Consolidation

## 1. Purpose and Scope
This document consolidates **all known constraints on the UniNet update operator** $U$ into a single place. It introduces **no new axioms**. Its purpose is:

1. To make explicit why the update rule is *severely constrained*.
2. To show that only a narrow class of operators survives these constraints.
3. To explain why the surviving forms will look **familiar** to physicists (e.g. deterministic wave evolution).

This document supports *recognition*, not novelty.

---
## 2. Hard Constraints from Tier-0 Axioms

### C0.1 Unitarity
$U^\dagger U = I$
- Exact information conservation.
- Excludes stochastic or collapse-based dynamics at Tier-0.

### C0.2 Graph Locality
- $U$ factorizes into node-local and edge-local operations.
- No propagation beyond one graph edge per tick.
- Enforces finite causal cones.

### C0.3 No Phenomenological Delays
- Latency is derived from locality, not encoded in $U$.
- Forbids hidden clocks or edge-dependent delays.

---
## 3. Structural Constraints from Derived Theorems

### C1. Cut Balance / Boundary Mediation
- Regional change satisfies bulk–boundary balance.
- $U$ must admit a divergence-form flux representation.

### C2. Gauge as Boundary Redundancy
- Transformations preserving boundary observables are redundant.
- $U$ must respect cut-equivalence classes.

### C3. Bandwidth and Stability
- Boundary bandwidth growth limits mode mixing.
- Excludes chaotic or globally entangling unitaries.

---
## 4. Regime-Specific Constraints

### C4. QM Regime (Static Latency)
- Fixed latency: $\delta(u,v)=d_G(u,v)$.
- No queue/backpressure effects on propagation.
- Spectral stability required.

### C5. GR Regime (Adaptive Latency After Projection)
- $U$ remains unitary and local.
- Adaptive delays arise only after coarse-graining and projection.

---
## 5. Standard-Model Admissibility Constraints

### C6. Chiral Block Structure
$\mathcal{H}_v = \mathcal{H}_v^L \oplus \mathcal{H}_v^R$
- Block-structured internal space with bounded mixing.

### C7. Bounded Chirality Mixing
$0 < \bar{\epsilon}_{\mathrm{mix}} \le \epsilon_{\mathrm{mix}}^{\max} \ll 1$

### C8. CP Non-Commutation
$\epsilon_{\mathrm{CP}} = \frac{1}{2}\|[\mathrm{CP},U]\|_{\mathrm{op}} > 0$

### C9. Anomaly Compatibility
- Only anomaly-consistent representations are admissible.

---
## 6. Fundamental One-Dimensionality of the Update

### C10. One-Dimensional Update Parameter
The update rule advances the system along a **single ordering parameter**:

$\psi_{n+1} = U\,\psi_n$

- The index $n$ is an iteration/causal-depth parameter, not a spatial coordinate.
- No spatial or spacetime dimensionality is encoded in $U$ itself.

### C11. Emergent Dimensionality via Relational Structure
Apparent spatial and spacetime dimensionality arises from:
- graph connectivity,
- boundary bandwidth growth,
- relational accessibility of information,
- observer-level coarse-graining.

Embedding geometry directly into $U$ would violate locality and latency-derivation theorems.

---
## 7. Wave / Wavelet Character of Information Transport

### C12. Wave-Carried Information
Given unitarity, locality, and stability under iteration, information propagates as **wave-like amplitude patterns**.

- Deterministic propagation preserves phase.
- Superposition and interference follow from linearity.
- No particle or collapse ontology is required at Tier-0.

The natural carriers are therefore **waves**, and—due to discreteness and boundaries—**localized wave packets (wavelets)**.

### C13. Localization from Boundaries and Bandwidth
Infinite plane waves are excluded by:
- finite graph extent,
- boundary-mediated dynamics,
- finite observer access.

Physically relevant excitations are localized wavelets that propagate, spread, interfere, and recombine.

---
## 8. Chirality as Controlled Symmetry Breaking

### C14. Minimal Chiral Bias
The update operator includes a **small, structured chiral asymmetry**:
- left/right sectors are not exactly symmetric,
- off-diagonal mixing is bounded and nonzero,
- CP non-commutation is small but finite.

This bias:
- breaks perfect standing-wave symmetry,
- avoids dynamically sterile universes,
- seeds parity violation and CP effects,
- while preserving global wave stability.

---
## 9. Observational Pruning of the Admissible Operator Class

### C15. Quantum-Scale Constraints
- Interference stability and coherence times constrain short-scale spectral structure.
- Unstable or decohering operators are excluded.

### C16. Particle-Physics Constraints
- Chirality, CP violation, and anomaly cancellation prune internal structure and mixing.

### C17. Cosmological and Large-Scale Constraints
- Long-wavelength stability and fluctuation growth constrain IR behavior.
- CMB multipoles and large-scale structure statistics further restrict parameters.

Observations **prune** the admissible class; they do not introduce new operator forms.

---
## 10. Consolidated Statement

> *The UniNet update operator is a one-dimensional, local, unitary, deterministic wave-propagation operator. Information is carried by localized wavelets on the graph, with small chiral asymmetries breaking perfect symmetry just enough to generate rich structure. Theory alone restricts the operator to a narrow, familiar equivalence class; empirical observations—from quantum experiments through particle physics and cosmology—further prune this class without altering its fundamental wave-like form.*

---


