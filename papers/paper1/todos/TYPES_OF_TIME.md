<!--
INSTRUCTIONS FOR RECEIVING LLM:

Insert this lemma in the Introduction, immediately before the Axioms section.
Insert the interpretation block directly after the lemma.
Add the DAG node to the global dependency graph.
Maintain UniNet’s respectful, structural tone.
-->

# LEMMA-TIME-01 — Distinct Types of Time

**Status:** conceptual lemma (explanatory)

## Statement

Modern physical theories use the word *time* to refer to several conceptually distinct objects.  
Quantum mechanics employs an external evolution parameter; general relativity uses a foliation-dependent coordinate; operational physics uses proper time measured along worldlines.  
These are not the same type of object, even though they share the same name.  
UniNet keeps these notions separate: the substrate provides only update order and causal structure, from which effective notions of time may emerge within specific witness families.

## Interpretation (reader-facing)

The time parameter \(t\) in the Schrödinger equation is an observer-chosen coordinate external to the system.  
In general relativity, “time” arises from a choice of spacetime slicing, which again depends on the observer’s representation.  
Clocks, by contrast, measure proper time along their trajectories.

UniNet does not assume any of these as primitive.  
The substrate has:

- a **local update rule**,  
- **finite propagation latency**,  
- and the **causal partial order** induced by these.

From this structure, familiar time notions—coordinate time, proper time, and dynamical evolution—appear only as *emergent constructs* within witness families.  
This lemma is introduced early to help the reader avoid unconsciously identifying these distinct concepts as if they were the same type.

---

# Dependency DAG Update

## DAG Node: LEMMA-TIME-01

**Tier:** conceptual (non-spine)  
**Status:** explanatory lemma

**Dependencies:**
- `AXIOM-1` (substrate: graph, not spacetime)  
- `AXIOM-2` (discrete update steps)  
- `AXIOM-6` (locality and finite propagation latency)  
- `DEFINITION-LC-01` (light cones / causal order)

**Provides:**
- Early conceptual separation of time types  
- Foundation for understanding emergent time in witness families  
- Clarification for later discussions of QM evolution, GR witnesses, and measurement timing

**Used by:**
- Introduction  
- QM dynamics chapter  
- GR/Regge witness chapter  
- Measurement and Born-rule timing sections  

---