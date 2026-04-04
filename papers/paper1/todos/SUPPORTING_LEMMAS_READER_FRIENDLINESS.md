<!--
INSTRUCTIONS FOR RECEIVING LLM:

Insert these lemmas in the Introduction, immediately AFTER LEMMA-TIME-02.
Group them under a subsection titled “Conceptual Preliminaries”.
Insert each interpretation block directly after its lemma.
Add all DAG nodes to the global dependency graph.
Maintain UniNet’s gentle, explanatory tone.
-->

# LEMMA-SPACE-01 — Distinct Types of Space

**Status:** conceptual lemma (explanatory)

## Statement

In the usual formulations of QM and GR, the word *space* refers to several distinct structures:  
the configuration space of quantum mechanics, the geometric spacetime manifold of general relativity, and the operational space defined by measurement procedures.  
These are not the same type of object.  
UniNet keeps these notions separate: the substrate provides only graph adjacency and cut structure, from which effective spatial notions emerge within witness families.

## Interpretation (reader-facing)

In quantum mechanics, “space” is the domain on which wavefunctions are defined.  
In general relativity, “space” is a slice of a four-dimensional manifold equipped with a metric.  
Operationally, “space” is what rulers and detectors measure.  
These three concepts behave differently and should not be conflated.

UniNet begins from a substrate with no primitive spatial manifold.  
Regions are defined by cuts; adjacency is defined by graph structure; and geometric space emerges only within specific witness families.  
This lemma helps the reader avoid importing continuum spatial assumptions into a substrate that does not contain them.

---

# LEMMA-LOC-01 — Distinct Types of Locality

**Status:** conceptual lemma (explanatory)

## Statement

In the usual formulations of QM and GR, the term *locality* refers to different concepts:  
operator locality in quantum mechanics, metric locality in general relativity, and signal locality in operational physics.  
These notions are not equivalent.  
UniNet uses graph-locality: updates and influences propagate only along edges with finite latency.  
This notion is distinct from locality in QM or GR and should not be conflated with them.

## Interpretation (reader-facing)

In QM, locality refers to operators acting on tensor factors.  
In GR, locality refers to interactions determined by the metric and its light cones.  
Operationally, locality means “no faster-than-light signalling.”

UniNet’s locality is simpler and more primitive:  
updates propagate along graph edges with finite latency, defining causal cones.  
This substrate-level locality is the foundation from which operational locality and emergent geometric locality arise.  
Recognizing these distinctions prevents confusion when comparing UniNet to QM or GR.

---

# LEMMA-OBS-01 — Observer-Defined vs Substrate-Defined Structures

**Status:** conceptual lemma (explanatory)

## Statement

In the usual formulations of QM and GR, many structures—such as positions, momenta, subsystem partitions, and coordinate choices—are defined by the observer’s representation rather than by the underlying physical substrate.  
UniNet distinguishes sharply between observer-defined constructs and substrate-defined constructs.  
Only the latter are fundamental.

## Interpretation (reader-facing)

In QM, subsystem partitions and tensor-product structures are chosen by the observer.  
In GR, coordinate systems and foliations are chosen by the observer.  
Operationally, measurement settings and reference frames are chosen by the experimenter.

UniNet’s substrate contains none of these.  
It contains only occupancy, adjacency, update rules, and boundary flux.  
All higher-level structures—coordinates, subsystems, fields, and geometric quantities—are emergent and representation-dependent.  
This lemma prepares the reader to interpret UniNet’s formalism without projecting observer-defined structures onto the substrate.

---

# Dependency DAG Updates

## DAG Node: LEMMA-SPACE-01

**Tier:** conceptual (non-spine)  
**Dependencies:**  
- `AXIOM-1` (graph substrate)  
- `DEFINITION-CUT-01` (regions as cuts)  
- `LEMMA-TIME-01` (distinct time types)

**Provides:**  
- Separation of spatial notions  
- Foundation for emergent geometry in witness families

**Used by:**  
- Geometry/witness chapters  
- QM/GR comparison sections  


## DAG Node: LEMMA-LOC-01

**Tier:** conceptual (non-spine)  
**Dependencies:**  
- `AXIOM-1` (graph substrate)  
- `AXIOM-6` (locality and finite latency)  
- `LEMMA-SPACE-01` (distinct space types)

**Provides:**  
- Clarification of locality types  
- Basis for understanding UniNet causal cones

**Used by:**  
- Causality/light-cone sections  
- Bell/non-signalling commentary  


## DAG Node: LEMMA-OBS-01

**Tier:** conceptual (non-spine)  
**Dependencies:**  
- `AXIOM-1` (substrate)  
- `AXIOM-9` (boundary-limited observability)  
- `LEMMA-SPACE-01`  
- `LEMMA-TIME-01`

**Provides:**  
- Distinction between observer-defined and substrate-defined structures  
- Conceptual foundation for suspect-operator theorem

**Used by:**  
- Operator chapter  
- Measurement sections  
- Bell/correlation discussions  

---
