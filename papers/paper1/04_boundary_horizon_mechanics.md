# Chapter 4 - Boundary and Horizon Mechanics

Graph cuts are the operational interface of the framework. They tell us where interior bookkeeping stops being self-sufficient, where external observability begins, and where boundary-mediated stability can replace node-local ontology. This chapter makes that interface explicit and keeps a strict separation between proved cut statements, noether-like symmetry claims, and deferred phenomenological packaging.

Chapters 2 and 3 established what the framework commits to and what those commitments already imply. This chapter focuses on where those implications become operational.
Boundaries are not secondary objects in UniNet. They are the interfaces through which everything observable must pass. Once cuts are taken seriously, boundaries inherit structure: they limit access, enforce bookkeeping, constrain symmetry, and determine what can be stabilized and communicated to the outside. Chapter 4 makes those roles explicit.
Nothing fundamentally new is introduced here. Instead, the causal and bookkeeping structure developed in Chapter 3 is examined at its edges. What does it mean for two interior states to be indistinguishable from the outside? How much independent information can a boundary support? Which symmetries survive when only boundary‑accessible data is available, and which collapse under coarse‑graining?
This chapter is careful about scope. Some results are fully proved, others are marked as noether‑like, and some are explicitly deferred. That discipline is intentional. Boundaries are powerful, but they are also subtle. Where the framework has enough structure to speak cleanly, it does. Where it does not, it says so.
By the end of Chapter 4, boundaries will no longer be passive separators. They will have become active constraints — shaping observability, symmetry, and stability. Horizons, gauge redundancy, and boundary‑mediated dynamics will all appear as consequences of the same underlying cut logic, not as separate principles.

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

External equivalence — a friendly way to think about “the same from the outside”
DEFINITION‑BND‑05 formalizes a very simple idea: from the outside, only the boundary matters.
Once a cut is drawn, an observer no longer has access to the interior directly. Everything they can possibly learn about what lies inside must pass through the boundary. External equivalence captures this by declaring two interior states to be the same whenever they produce the same boundary‑accessible observables. If the boundary cannot tell them apart, then neither can any observer restricted to it.
This definition exists to shift the notion of “sameness” away from microscopic detail and toward operational access. Two interiors may differ wildly in their internal configuration, history, or complexity, and yet be indistinguishable from the outside. In UniNet, that indistinguishability is not an approximation or a failure of description — it is the definition of equivalence.
What matters is that equivalence is cut‑relative. Change the boundary, and the equivalence classes change with it. There is no absolute notion of sameness divorced from access. Identity is always defined with respect to what can be observed, and observation is always boundary‑limited.
By naming cut‑external equivalence explicitly, the framework makes redundancy concrete. What later appears as gauge freedom is already present here as the freedom to rearrange interiors without altering boundary behavior. Nothing “unphysical” is being removed — the boundary simply refuses to notice it. This is the point where symmetry stops being a formal property of equations and becomes a statement about what differences can never matter.

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

Gauge — a friendly way to think about redundancy
THEOREM‑BND‑04 shows that what is usually called gauge symmetry is not an added principle, but a consequence of boundaries.
Once cut‑external observational equivalence is defined, a new kind of symmetry appears automatically. Any transformation of the interior that leaves all boundary‑accessible observables unchanged is invisible from the outside. From the observer’s point of view, such transformations do nothing at all. They change the description, but not the physics. This is exactly what gauge symmetry means in operational terms.
This theorem exists to reverse the usual story. Instead of starting with abstract symmetry groups and then arguing that they represent redundancy, UniNet starts with access. Redundancy appears because observers are restricted to boundaries. Interior details that cannot affect the boundary cannot matter physically, no matter how elaborate they are. Gauge freedom is therefore not a feature of equations — it is a feature of limited observability.
What matters is that this symmetry is cut‑relative. There is no universal gauge group floating above the system. Change the boundary, and the redundancy changes with it. What counts as “the same physical state” depends on what can be seen. Gauge is not absolute; it is contextual.
By promoting cut‑external equivalence to a symmetry principle, THEOREM‑BND‑04 grounds gauge in something concrete. It explains why certain degrees of freedom can be reshuffled freely, why physical predictions remain unchanged, and why symmetry transformations often feel like relabelings rather than actions. Nothing mysterious is being removed — the boundary simply refuses to notice.

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

Boundary bandwidth — a friendly way to think about how much can pass
DEFINITION‑BND‑01 introduces boundary bandwidth: a way to describe how much information a boundary can support as a region grows.
Once boundaries are taken seriously as interfaces, it becomes clear that not all boundaries are alike. Some are small and restrictive. Others grow with the region they enclose and can carry more independent information. Boundary bandwidth captures this by tracking how the size or capacity of the boundary scales relative to the interior.
This definition exists to shift attention away from volume and toward interface. In UniNet, what matters for observability and exchange is not how large a region is on the inside, but how much boundary it presents to the outside. A region with a rapidly growing boundary can expose more structure. A region whose boundary grows slowly will necessarily compress, hide, or merge interior detail.
What matters is that bandwidth is a property of the cut, not of the interior dynamics. No amount of internal complexity can force more independent information through a boundary than the boundary can structurally support. Boundary bandwidth therefore sets a hard limit on distinguishability, communication, and stability — long before any particular physics is layered on top.
By defining boundary bandwidth explicitly, the framework gains a scale‑aware notion of interface. This is the step where questions about dimension, symmetry, and capacity become unavoidable. How a boundary grows determines what kinds of structures can remain visible, what kinds of symmetries can survive coarse‑graining, and how much of the interior can ever matter to the outside.

### `DEFINITION-BND-02` - Effective Dimension from Boundary Growth
Status: `proved`

Define

$$
d_{\mathrm{eff}}
:=
1+\limsup_{r\to\infty}\frac{\log B(r)}{\log r}.
$$

The effective dimension counts the asymptotic growth of independent boundary channels.

Dimension — a friendly way to think about scale
DEFINITION‑BND‑02 introduces effective dimension as something that is read from the boundary, not assumed about the interior.
Once boundary bandwidth is defined, it becomes possible to ask how that bandwidth grows as a region becomes larger. Effective dimension captures this growth rate. It does not count coordinates or directions. It asks a simpler question: as we enlarge a region, how quickly does the amount of boundary available for exchange increase?
This definition exists to avoid assuming spatial dimension upfront. In UniNet, there is no background space waiting to be measured. Instead, dimension emerges from scaling behavior. A boundary that grows slowly with region size behaves as if the system is low‑dimensional. A boundary that grows rapidly behaves as if the system has more room to expose independent structure. Dimension, in this sense, is not a label — it is a consequence.
What matters is that effective dimension is operational. It is defined entirely in terms of observability and access. An observer does not need to know the interior layout of a region to infer its dimensional character; the boundary already encodes that information. How much can be distinguished, transmitted, or stabilized depends directly on how boundary capacity scales.
By defining effective dimension this way, UniNet ties geometry to interface. Dimension is no longer something imposed on the graph, but something inferred from how boundaries behave under enlargement. This makes dimension flexible, scale‑dependent, and context‑sensitive — exactly as one would expect in a framework where spacetime is emergent rather than fundamental.

### `THEOREM-BND-01` - Boundary Growth Controls Volume Growth
Status: `proved`

Under mild regularity assumptions, polynomial boundary growth with exponent $d_{\mathrm{eff}}-1$ implies polynomial volume growth with exponent $d_{\mathrm{eff}}$.

Growth — a friendly way to think about what the boundary controls
THEOREM‑BND‑01 states that how a boundary grows places hard limits on how the interior can grow.
Once boundary bandwidth and effective dimension are defined, it becomes clear that the interior of a region cannot expand arbitrarily while remaining observable or coherent. If the boundary grows slowly, the interior cannot expose independent structure indefinitely. Eventually, distinct interior configurations must collapse into the same boundary description. The boundary, not the volume, sets the pace.
This theorem exists to make a quiet but powerful constraint explicit. In UniNet, interior size is not free. It is regulated by the interface through which it must communicate. A rapidly growing boundary can support richer interior behavior. A slowly growing boundary forces compression, hiding, or merging of internal detail. The interior must adapt to what the boundary can carry.
What matters is that this constraint is structural, not dynamical. It does not depend on the update rule, the presence of forces, or the nature of the internal patterns. It follows from geometry‑free considerations of access and scaling alone. If the boundary cannot keep up, the interior cannot remain fully distinguishable.
By establishing that boundary growth controls volume growth, the framework reverses a familiar intuition. Instead of thinking that large interiors determine what boundaries must do, UniNet shows that boundaries decide how much interior can matter at all. This result underlies later discussions of dimensionality, stability, and symmetry. It explains why some large systems behave effectively low‑dimensional, and why interfaces play such an outsized role in determining physical behavior.

### `DEFINITION-BND-03` - Boundary Observable Algebra
Status: `proved`

For a region $R$, let $\mathcal{O}(\partial R)$ denote the algebra of observables accessible outside the cut: net fluxes, boundary registers, and declared coarse boundary projections.

Boundary observables — a friendly way to think about what can be seen
DEFINITION‑BND‑03 formalizes what a boundary can actually register.
Once boundaries are treated as the sole interface between inside and outside, it becomes necessary to say what information is even available there. The boundary observable algebra is simply the collection of quantities that can be accessed, recorded, or inferred from the boundary alone. It does not describe everything that exists inside — only everything that can possibly matter to an external observer.
This definition exists to make observability concrete. Instead of speaking vaguely about “what the boundary shows,” UniNet specifies that boundaries support a structured set of observables: fluxes, registers, and declared coarse‑grained summaries. Anything outside this set is, by definition, invisible from the outside. It may exist internally, evolve, or interact, but it cannot influence external description unless it enters the boundary algebra.
What matters is that this algebra is closed under what observers are allowed to do. Observers can combine, compare, and process boundary observables, but they cannot step outside them. The algebra therefore defines the full expressive power of boundary‑limited observation. It is not a matter of convenience or choice — it is a hard limit imposed by access.
By defining the boundary observable algebra explicitly, the framework gains a precise place where symmetry, redundancy, and conservation will later act. Symmetries are those transformations that leave this algebra unchanged. Conserved quantities are those that can be tracked consistently within it. Anything that does not register here cannot play a direct role in observable physics.
This is the step where “what can be seen” becomes a formal object — not to restrict the theory, but to keep it honest about what observation can ever mean.

### `DEFINITION-BND-04` - Boundary Redundancy Group
Status: `proved`

The boundary redundancy group $\mathcal{G}(\partial R)$ is the class of interior transformations that leave the boundary observable algebra invariant.

Redundancy — a friendly way to think about what doesn’t matter
DEFINITION‑BND‑04 identifies the boundary redundancy group: the set of interior transformations that leave all boundary observables unchanged.
Once the boundary observable algebra is fixed, a natural question arises. Which changes inside the region actually matter to the outside, and which do not? The boundary redundancy group collects exactly those interior transformations that the boundary cannot detect. Apply any of them, and the boundary story remains the same.
This definition exists to make irrelevance precise. Instead of treating redundancy as a vague notion or an artifact of description, UniNet ties it directly to observability. If a transformation does not alter any boundary‑accessible observable, then it cannot have physical consequences for an external observer. Such transformations are not forbidden — they are simply unobservable.
What matters is that this redundancy is defined relative to a specific cut. Change the boundary, and the redundancy group changes with it. There is no universal notion of “pure gauge” independent of access. Redundancy is contextual. It depends on what is being observed and from where.
By defining the boundary redundancy group explicitly, the framework gains a clean handle on symmetry before introducing any symmetry principles. This group is not yet a statement about conservation or dynamics. It is a statement about indistinguishability. Symmetry will emerge when these redundancies are promoted to invariances — but that promotion only makes sense once the boundary has told us what it can and cannot see.

### `THEOREM-BND-02` - Boundary Capacity Bounds Independent Conserved Flows
Status: `noether-like`

The number of independently resolvable conserved exchange modes is bounded by boundary bandwidth. One cannot stabilize more independent exterior-facing conserved channels than the cut can resolve.

Limits — a friendly way to think about conservation and symmetry
THEOREM‑BND‑02 states that a boundary can only support a limited number of independent conserved channels.
Once boundary observables and redundancy are defined, it becomes possible to ask which quantities can be tracked consistently across a cut. This theorem answers with a constraint: the number of independently conserved exchanges that can be resolved by an external observer is bounded by the capacity of the boundary itself. If the boundary cannot distinguish them, they cannot remain independently conserved in any operational sense.
This result is noether‑like rather than fully variational. It does not begin with an action or a symmetry group. Instead, it starts from access. Conservation here is not about equations remaining invariant, but about whether a quantity can be followed reliably through time at the boundary. If two flows are forced to share the same boundary channel, they will eventually interfere, mix, or collapse into a single effective quantity from the outside.
What matters is that this limitation is structural. It does not depend on the detailed dynamics inside the region, nor on the specific form of the update rule. It follows from boundary capacity alone. The boundary decides how many independent “stories” can be told about what crosses it. Beyond that limit, distinction is lost.
By stating this bound explicitly, UniNet reframes conservation laws as conditional rather than absolute. Conserved quantities are not guaranteed simply because the interior dynamics allow them. They must also fit through the boundary. This explains why some symmetries survive coarse‑graining while others do not, and why stable conserved charges tend to be few rather than many.
THEOREM‑BND‑02 therefore marks the point where symmetry stops being free. It becomes something that must be supported by the interface. Conservation is no longer just a property of motion; it is a property of access.

### `THEOREM-BND-03` - Goldilocks Window for Boundary Symmetry Viability
Status: `deferred`

If effective dimension is too low, faithful boundary symmetries collapse toward abelian or trivial structure. If it is too high, symmetry proliferation becomes unstable under coarse-graining. The current program keeps the constructive promotion of an intermediate stable window deferred.

Taken together, these results say that admissible stable mode structure is not arbitrary. It is jointly constrained by locality, boundary capacity, and coarse-graining stability.

Viability — a friendly way to think about why some symmetries survive
THEOREM‑BND‑03 addresses a subtle question: not which symmetries are allowed, but which ones can actually last.
Once boundary capacity limits independent conserved channels, it becomes clear that symmetry is constrained from both sides. If the boundary is too restrictive, it cannot support rich symmetry structure — everything collapses toward trivial or abelian behavior. If the boundary is too permissive, symmetry proliferates uncontrollably and becomes unstable under coarse‑graining. This theorem identifies a middle ground: a window in which boundary capacity is just right to support nontrivial, stable symmetry.
This result is marked deferred because the full constructive proof depends on additional modeling detail. But the intuition is already unavoidable. Symmetry is not free. It must fit through the boundary. Too little capacity, and symmetry has nowhere to live. Too much capacity, and distinctions fail to stabilize. Only in an intermediate regime can symmetry be both expressive and robust.
What matters is that this is not a statement about aesthetics or simplicity. It is a structural constraint imposed by access. Boundaries decide which symmetries can be resolved, tracked, and conserved over time. The interior may support many formal invariances, but only those that survive boundary projection can matter physically.
By articulating this “Goldilocks window,” UniNet reframes symmetry as something that must be supported by the interface. This helps explain why the symmetries observed in nature are neither trivial nor arbitrarily complex. They are the ones that fit — not because they were chosen, but because they endure.

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

What boundaries are allowed to decide
This chapter has treated boundaries not as surfaces, but as constraints.
Once cuts are taken seriously, boundaries inherit structure. They determine what can be observed, what differences can matter, and how much independent information can survive contact with the outside. Chapter 04 has made those roles explicit. It has shown that observability lives on boundaries, that redundancy is defined by what boundaries cannot see, and that symmetry is shaped — and limited — by what boundaries can support.
Nothing in this chapter introduced new dynamics. Instead, it examined the consequences of access. By defining boundary observables, redundancy groups, bandwidth, and effective dimension, the framework made clear that interfaces are not passive. They actively regulate which conserved quantities remain distinct, which symmetries can stabilize, and which interior details are inevitably lost to coarse‑graining.
Equally important is what this chapter has not claimed. Where results depend on additional structure, they are marked noether‑like or deferred. Boundaries are powerful, but they do not explain everything on their own. What they do explain is why some structures endure while others collapse, and why physical theories tend to exhibit a small number of robust symmetries rather than an explosion of arbitrary ones.
By the end of Chapter 04, boundaries are no longer just bookkeeping devices. They have become decision points. They decide what is visible, what is redundant, what can be conserved, and what can remain stable across scales. Horizons, gauge structure, and boundary‑mediated influence all appear here not as separate principles, but as different faces of the same underlying fact: physics is shaped as much by its interfaces as by its interiors.
What follows in later chapters is not a retreat from this boundary‑aware view, but its application. Whether the framework is read as quantum, relativistic, or cosmological, the same lesson will recur: what survives is what fits through the boundary.
