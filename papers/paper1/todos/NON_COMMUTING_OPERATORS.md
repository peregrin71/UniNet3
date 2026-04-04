<!--
INSTRUCTIONS FOR RECEIVING LLM:

You are being given a new theorem and commentary to insert into the UniNet manuscript.

Your tasks:
1. Insert the theorem into the "Operator Structure / Observables" section of the QM chapter, after the discussion of boundary observables and before any witness-family operator constructions.
2. Insert the interpretation block immediately after the theorem.
3. Insert the DAG node into the global dependency graph.
4. Maintain UniNet’s tone: respectful, structural, and non‑confrontational.
5. Do NOT modify existing axioms or theorems unless explicitly instructed.
-->

# THEOREM-SUS-01 — Context-Dependent Operator Warning
**Status:** explanatory theorem (no formal proof required)

## Statement

Operators that refer to *observer-defined spacetime structures*—such as positions, times, subsystem partitions, or tensor‑product decompositions—are not fundamental objects in UniNet.  
Their algebraic properties, including non‑commutativity, reflect the structure of the observer’s chosen representation rather than substrate-level physics.

## Interpretation (reader-facing)

Traditional quantum theory is formulated on a continuum spacetime chosen by the observer.  
Operators such as \( \hat{x} \), \( \hat{p} \), \( \hat{H}(x) \), or decompositions like \(H = H_A \otimes H_B\) are defined within that representation.  
Their non‑commutativity is a feature of the *observer’s spacetime description*, not necessarily a fundamental property of nature.

UniNet adopts a different ontology:

- spacetime is not primitive but emergent,  
- regions are defined by cuts,  
- observers access only boundary flux,  
- and no global Hilbert-space factorization is assumed.

Therefore, operators tied to observer-defined spacetime structures should be treated as **effective**, not **fundamental**.  
Their algebraic relations do not constrain UniNet’s substrate.

## Gentle Framing (for inclusion in commentary)

This perspective does not imply that traditional operator methods are incorrect.  
They remain powerful and accurate within the continuum spacetime framework for which they were developed.  
UniNet simply begins from a different starting point: a discrete substrate with boundary-based observability.  
In this setting, the familiar non‑commuting spacetime operators of standard quantum theory arise as *emergent*, representation-dependent constructs rather than primitive elements of the ontology.

---

# Dependency DAG Update

## DAG Node: THEOREM-SUS-01
**Tier:** explanatory (non‑spine)  
**Status:** contextual theorem

**Dependencies:**
- `AXIOM-1` (substrate: graph, not spacetime)  
- `AXIOM-6` (locality)  
- `AXIOM-9` (boundary-limited observability)  
- `DEFINITION-CUT-01` (regions as cuts)  
- `DEFINITION-OBS-01` (observer = region)

**Provides:**
- Clarification of operator status in UniNet  
- Distinction between substrate-level and representation-level operators  
- Conceptual foundation for rejecting tensor-product assumptions in Bell-type arguments  

**Used by:**
- QM operator chapter  
- Bell-correlation commentary  
- Measurement and Born-rule interpretation sections  

---