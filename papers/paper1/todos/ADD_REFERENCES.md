<!--
INSTRUCTIONS FOR RECEIVING LLM:

You are being given a "Related Work" section and a bibliography scaffold to insert into the UniNet manuscript.

Your tasks:
1. Insert the "Related Work" section into the Introduction chapter, after the motivation and before the Axioms.
2. Insert the bibliography scaffold into the References section at the end of the manuscript.
3. Do NOT alter the core axioms, theorems, or dependency DAG.
4. Inline citation placeholders [Ref:XYZ] should remain as-is; they will be resolved later.
5. Maintain the manuscript’s tone: structural, conceptual, and non‑derivative.
-->

# Related Work

UniNet is a first‑principles framework built from a minimal substrate: a simple graph, a local unitary update, and a boundary‑based observability structure.  
Although the architecture is original and self‑contained, it is useful to situate it relative to existing approaches in discrete physics, emergent geometry, and quantum foundations.

## Discrete and Graph‑Based Approaches

Several research programs explore discrete substrates as candidates for fundamental physics.  
These include causal sets [Ref:CausalSets], quantum graphity models [Ref:QuantumGraphity], and lattice‑based approaches in condensed matter and quantum information [Ref:LatticeModels].  
UniNet differs from these in that:

- it does not assume a pre‑given causal order (causality is derived from latency),  
- it does not assume a pre‑given geometry (geometry is a witness, not a primitive),  
- and it does not assume a specific Hamiltonian or field content.

The closest structural neighbor is the study of discrete Schrödinger evolution on graphs [Ref:DiscreteSchrodinger], which UniNet uses as a **witness family**, not as a foundational assumption.

## Regge Calculus and Emergent Geometry

Regge calculus provides a discrete formulation of general relativity using simplicial complexes [Ref:Regge1961].  
UniNet uses Regge calculus only as a **witness source** for emergent geometry:  
a way to demonstrate that a simple graph + local update can support a Regge‑like geometric interpretation under coarse‑graining.

UniNet does not assume:

- a simplicial complex,  
- a metric,  
- or curvature.  

These emerge only in the witness construction.

## Quantum Cellular Automata and Local Unitary Dynamics

Quantum cellular automata (QCA) [Ref:QCA] and quantum walks [Ref:QuantumWalks] explore local unitary evolution on discrete substrates.  
UniNet shares with these approaches the emphasis on locality and unitarity, but differs in:

- its boundary‑based ontology,  
- its cut‑theorem structure,  
- its explicit separation between substrate and witness families,  
- and its derivation of measurement statistics from boundary flux.

## Measurement, Decoherence, and the Born Rule

Traditional approaches to the Born rule include:

- decoherence theory [Ref:ZurekDecoherence],  
- envariance [Ref:ZurekEnvariance],  
- Gleason‑type theorems [Ref:Gleason],  
- and frequency‑operator approaches [Ref:HartleFrequencies].

UniNet’s derivation is distinct:  
the Born rule arises as a **cut‑statistics theorem**, where detectors and observers are simply **regions with boundaries**, and measurement is **flux across a cut**.  
This aligns UniNet more closely with operational and boundary‑based perspectives in algebraic QFT [Ref:HaagAQFT], though UniNet’s substrate is discrete and non‑field‑theoretic.

---

# Bibliography Scaffold

Below is a minimal bibliography scaffold containing canonical references for the topics mentioned above.  
Inline citation keys (e.g., [Ref:Regge1961]) correspond to these entries.

- **[Ref:Regge1961]**  
  T. Regge, *General Relativity Without Coordinates*, Il Nuovo Cimento, 1961.

- **[Ref:CausalSets]**  
  L. Bombelli, J. Lee, D. Meyer, R. Sorkin, *Space-Time as a Causal Set*, Phys. Rev. Lett., 1987.

- **[Ref:QuantumGraphity]**  
  T. Konopka, F. Markopoulou, L. Smolin, *Quantum Graphity*, arXiv:hep-th/0611197.

- **[Ref:LatticeModels]**  
  Standard references on lattice Hamiltonians and discrete models in condensed matter physics.

- **[Ref:DiscreteSchrodinger]**  
  Standard references on discrete Schrödinger operators and graph Laplacians.

- **[Ref:QCA]**  
  B. Schumacher, R. Werner, *Reversible Quantum Cellular Automata*, arXiv:quant-ph/0405174.

- **[Ref:QuantumWalks]**  
  Y. Aharonov et al., *Quantum Walks on Graphs*, various foundational papers.

- **[Ref:ZurekDecoherence]**  
  W. H. Zurek, *Decoherence and the Transition from Quantum to Classical*, Physics Today, 1991.

- **[Ref:ZurekEnvariance]**  
  W. H. Zurek, *Environment-Assisted Invariance, Entanglement, and Probabilities in Quantum Physics*, Phys. Rev. Lett., 2003.

- **[Ref:Gleason]**  
  A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space*, J. Math. Mech., 1957.

- **[Ref:HartleFrequencies]**  
  J. B. Hartle, *Quantum Mechanics of Individual Systems*, Am. J. Phys., 1968.

- **[Ref:HaagAQFT]**  
  R. Haag, *Local Quantum Physics*, Springer, 1992.

---