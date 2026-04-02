# Chapter 4 - Boundary and Horizon Mechanics

Graph cuts are the operational interface of the framework. They tell us where interior bookkeeping stops being self-sufficient, where external observability begins, and where boundary-mediated stability can replace node-local ontology. This chapter makes that interface explicit and keeps a strict separation between proved cut statements, noether-like symmetry claims, and deferred phenomenological packaging.

## 4.1 Graph Cuts to Boundaries as Operational Interface
Chapter 3 already established the bookkeeping reason cuts matter: a region is exactly closed only when boundary flux vanishes, and otherwise requires a boundary register. This chapter adds the operational viewpoint.

### `DEFINITION-BND-05` - Cut-External Observational Equivalence
Status: `proved`

Fix a region $R\subseteq V$ and its boundary $\partial R$. Two interior microstates are externally equivalent across the cut if they induce the same exterior-accessible boundary observables:

$$
\psi_n|_R \sim_{\partial R} \psi'_n|_R
\iff
\mathcal{O}(\partial R;\psi_n)=\mathcal{O}(\partial R;\psi'_n).
$$

### `THEOREM-BND-04` - Gauge Equivalence as Cut-Observable Equivalence
Status: `proved`

The relation $\sim_{\partial R}$ is an equivalence relation, and its class-preserving automorphisms are precisely the boundary redundancy transformations.

In the language of this paper, gauge redundancy is therefore treated as cut-observable redundancy: different interior descriptions count as the same physics whenever they are indistinguishable at the boundary.

The logical order is

$$
\text{cut observables}
\to
\text{boundary redundancy}
\to
\text{gauge-style interpretation},
$$

not the reverse.

## 4.2 Delayed Boundary Representation and Observability Limits
Boundary access is not merely partial. It is delayed, bandwidth-limited, and coarse-grained.

Three ingredients combine:
1. `AXIOM-9` and `COROLLARY-SH-01` say regional closure requires boundary bookkeeping,
2. `DEFINITION-SH-08` and `THEOREM-SH-03` say observation discards microscopic information,
3. `THEOREM-BND-04` says exterior equivalence is organized by cut observables rather than by interior microstate identity.

The result is an operational boundary principle: exterior observers do not see interior microscopic state directly. They see boundary-mediated summaries. Delay in the representation is therefore structural rather than noise-like. It follows from the fact that the only data exiting the region is data that traverses or is registered at the cut.

This also explains why later discussions of horizons, mediator analogies, and cosmological boundary channels must be phrased carefully. The framework is not saying that every boundary is literally a classical surface in spacetime. It is saying that any macroscopic interface available to an observer is, in the first instance, a cut interface.

## 4.3 Stable Horizon Symmetries and Boundary Mode Selection
The boundary-capacity layer ties graph growth, effective dimension, and symmetry viability together.

### `DEFINITION-BND-01` - Boundary Bandwidth Function
Status: `proved`

For a nested family of regions $\{R_r\}$, define the boundary bandwidth by

$$
B(r):=|\partial R_r|,
$$

or by a weighted throughput analogue when edge capacities are part of the description.

### `DEFINITION-BND-02` - Effective Dimension from Boundary Growth
Status: `proved`

Define

$$
d_{\mathrm{eff}}
:=
1+\limsup_{r\to\infty}\frac{\log B(r)}{\log r}.
$$

The effective dimension counts the asymptotic growth of independent boundary channels.

### `THEOREM-BND-01` - Boundary Growth Controls Volume Growth
Status: `proved`

Under mild regularity assumptions, polynomial boundary growth with exponent $d_{\mathrm{eff}}-1$ implies polynomial volume growth with exponent $d_{\mathrm{eff}}$.

### `DEFINITION-BND-03` - Boundary Observable Algebra
Status: `proved`

For a region $R$, let $\mathcal{O}(\partial R)$ denote the algebra of observables accessible outside the cut: net fluxes, boundary registers, and declared coarse boundary projections.

### `DEFINITION-BND-04` - Boundary Redundancy Group
Status: `proved`

The boundary redundancy group $\mathcal{G}(\partial R)$ is the class of interior transformations that leave the boundary observable algebra invariant.

### `THEOREM-BND-02` - Boundary Capacity Bounds Independent Conserved Flows
Status: `noether-like`

The number of independently resolvable conserved exchange modes is bounded by boundary bandwidth. One cannot stabilize more independent exterior-facing conserved channels than the cut can resolve.

### `THEOREM-BND-03` - Goldilocks Window for Boundary Symmetry Viability
Status: `deferred`

If effective dimension is too low, faithful boundary symmetries collapse toward abelian or trivial structure. If it is too high, symmetry proliferation becomes unstable under coarse-graining. The current program keeps the constructive promotion of an intermediate stable window deferred.

Taken together, these results say that admissible stable mode structure is not arbitrary. It is jointly constrained by locality, boundary capacity, and coarse-graining stability.

## 4.4 Leaky Horizons and Implications for Black-Hole Surfaces
The shared cut theorems and the GR queueing scaffold permit a careful horizon interpretation without overclaim.

What is already justified:
1. `THEOREM-SH-02` distinguishes exact closure from controlled leak,
2. the GR queue and trapping package identifies a near-saturation regime with long dwell times and boundary-dominant release,
3. the branch split between exact closure and leaky closure is explicit.

What is not yet justified:
1. a complete quantitative black-hole observable map,
2. a final Page-turnover, firewall, or ringdown closure,
3. blanket claims that the framework has already solved black-hole phenomenology.

The paper-facing statement is therefore:
1. horizon-like surfaces are modeled as cuts with extreme transport asymmetry,
2. exact-closure and leaky branches must be distinguished,
3. quantitative black-hole claims remain deferred until their forward maps and reject thresholds are locked.

## 4.5 Boundary Mediator Interpretation
The boundary-facing statements used later in the paper have different proof maturity and must stay separated.

| Paper ID | Status | Paper-facing reading |
|---|---|---|
| `THEOREM-BND-05` | `proved` | exterior influence of an interior region is fully boundary-mediated once the observation map is fixed |
| `THEOREM-BND-06` | `noether-like` | independently resolvable conserved charges are boundary-rank limited |
| `THEOREM-BND-07` | `noether-like` | too little boundary capacity collapses effective symmetry structure |
| `THEOREM-BND-08` | `deferred` | too much boundary growth destabilizes compact low-rank symmetry packaging |
| `THEOREM-BND-09` | `deferred` | repeated coarse-graining may flow toward a stable dimensional window |
| `THEOREM-BND-10` | `noether-like` | field descriptions can arise as ensemble averages over unresolved boundary-transfer histories |

The mediator analogy belongs here, with care. What is safe to say is that the exterior sees boundary-mediated transfer channels rather than node-local interior ontology. In that restricted sense, the boundary acts as the effective mediator. What is not yet safe to say is that a full particle-physics mediator derivation has already been completed from this block alone.

Literature context is useful here:
1. gauge as redundancy,
2. holographic and bulk-boundary viewpoints,
3. graph isoperimetry and boundary-growth constraints,
4. boundary-mediated limits of bulk reconstruction.

These are context, not substitute proofs.

## 4.6 CMB, Parity, and Chirality Relevance from Boundary Channel Constraints
Boundary constraints intersect parity and chirality packaging in two ways.

First, the Standard-Model-facing admissibility constraints already require a small but nonzero chiral and CP-sensitive transfer structure. Second, the paper's cross-sector comparison suggests that there is at least a plausible scale-level overlap between small symmetry breaking in particle observables and small parity- or birefringence-sensitive cosmology observables.

The safe statement is modest:
1. a non-empty overlap region appears plausible at the scale-comparison level,
2. this is compatible with the current constrained-update program,
3. it does not prove uniqueness, and it does not replace a joint forward model.

So the role of this section is limited but important. It tells the reader why chirality and parity constraints are not isolated sector details. Boundary channel structure provides a place where they can matter across sectors, while the manuscript still keeps the quantitative promotion standard high.

## Chapter 4 Summary
Established in this chapter:
1. boundary observability is organized by cut-observable equivalence,
2. gauge-style redundancy is treated as boundary redundancy,
3. boundary growth and capacity constrain what stable exterior-facing structure is even possible.

Adopted or retained with status tags:
1. noether-like and deferred boundary symmetry claims remain explicitly marked,
2. boundary-mediator language is used only in the limited operational sense justified by the cut theorems.

Open:
1. constructive symmetry-window witnesses,
2. full gauge-group emergence from the boundary block,
3. quantitative black-hole closure,
4. a joint CP/CMB forward model beyond current scale-level compatibility.
