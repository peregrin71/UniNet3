# Chapter 3 - Shared Theorem Spine

This chapter introduces a **structural admissibility layer** that sits between the minimal substrate axioms and the shared theorem spine. Its role is to make graph-locality *physically meaningful* by ruling out pathological adjacency structures (e.g. long-range shortcuts) that would otherwise undermine causal cones, boundary growth, and later Regge-style geometric packaging.

Nothing in this chapter replaces or strengthens Tier-0 axioms by reinterpretation. Instead, it **explicitly restricts the admissible graph class** used by the shared theorems and downstream sector branches. All such restrictions are declared here to preserve auditability and prevent smuggling.

Chapter 02 fixed the ground rules. This chapter listens to what they already imply.
No new axioms are introduced here. Nothing is added to the framework. Instead, Chapter 03 follows the existing commitments — locality, ordered updates, information preservation, and boundary‑aware bookkeeping — and asks what must be true once those commitments are taken seriously. The results are not optional features or modeling choices; they are structural consequences.
The focus of this chapter is causality, conservation, and time — but approached from the bottom up. Rather than assuming spacetime and deriving causal order, causal order is built directly from reachability and delay on the graph. Rather than assuming global conservation laws, conservation is enforced locally and summed across boundaries. Rather than postulating an arrow of time, the conditions under which a direction appears are identified precisely.
Throughout this chapter, definitions, lemmas, and theorems are introduced not to increase abstraction, but to remove ambiguity. Each result makes explicit something that was already implicit in the axioms: that influence cannot outrun connectivity, that boundaries carry obligations, that observers only ever see partial records, and that irreversibility belongs to description rather than dynamics.
The goal of Chapter 03 is therefore not to model any particular physical regime. It is to establish a shared structural spine — a causal and bookkeeping scaffold that every later interpretation must respect. Quantum behavior, relativistic geometry, and particle‑like motion will appear later as readings of this structure, not as prerequisites for it. This chapter marks the point where the framework stops declaring rules and starts revealing consequences.

---

### Structural Admissibility: Metric Compatibility (No-Shortcut Condition)

The core axioms guarantee *combinatorial locality*: one update step propagates information by at most one graph hop. However, combinatorial locality alone does not prevent adjacency patterns that act as effective long-range shortcuts relative to any emergent geometry.

Several constructions used later in the manuscript require stronger structure:
1. stable causal and light-cone geometry (this chapter),
2. controlled boundary growth and effective dimension (Chapter 4),
3. meaningful edge-length assignment and deficit-angle curvature (Chapter 7),
4. robustness of observer-time and coarse-grained cones under refinement.

To support these without upgrading Tier-0 axioms, the manuscript introduces an explicit **no-shortcut structural admissibility condition**.

---

#### STRUCT-LOC-01 (Postulate)

There exists an edge-length assignment $\ell:E\to[\ell_{\min},\ell_{\max}]$ with $0<\ell_{\min}\le\ell_{\max}<\infty$ such that the induced shortest-path metric $d_{\ell}$ is quasi-isometric to graph distance $d_G$.

Adjacency does not create long-range shortcuts; graph distance faithfully represents physical separation up to bounded distortion.

Formally, there exist constants $a\ge1$ and $b\ge0$ such that for all $u,v\in V$:
$$
\frac{1}{a}\, d_G(u,v) - b \le d_{\ell}(u,v) \le a\, d_G(u,v) + b.
$$

This condition forbids:
1. wormhole-style adjacency,
2. small-world shortcut edges,
3. expander-like growth that collapses cone geometry.

It does **not** assume planarity, triangulation, fixed dimension, or global flatness.

Reachability — a friendly way to think about causality
LEMMA‑SH‑01 states that influence cannot outrun the graph.
If something happens at one node, it can only affect another node after enough update steps have passed to traverse the connecting path. This is not a dynamical assumption; it is a structural consequence of locality. Because updates only depend on immediate neighbors, information spreads outward one edge at a time. No amount of internal complexity can change that.
This lemma exists to make causality unavoidable. It tells us that “before” and “after” are not matters of interpretation but of reachability. Some events simply cannot influence others yet, because the graph has not had time to carry the effect. Others never can, because no path connects them at all.
Nothing about geometry or spacetime is assumed here. There is no speed, no metric, and no notion of distance beyond adjacency. And yet, the essential feature of causality is already present: influence has limits. Once this is accepted, delays, cones, and horizons are no longer optional constructions — they are forced by the graph itself.

---

The no-shortcut condition implies several properties used later in the manuscript:

This chapter is the shared backbone of Paper 1. Everything later in the manuscript depends on some subset of these statements. The sector chapters are therefore not independent theories. They are constrained readings of one common causal, cut-balance, and coarse-graining scaffold.

## 3.1 Reachability, Latency, and Causal Order
### `LEMMA-SH-01` - Reachability via Graph Distance
Status: `proved`

For events $(u,n)$ and $(v,m)$ in $V\times\mathbb{Z}$, information localized at $u$ at tick $n$ can influence $v$ by tick $m$ only if

$$
m\ge n+d_G(u,v).
$$

This is the immediate consequence of graph locality: one update step can enlarge the reachable set by at most one graph hop.

### `DEFINITION-SH-01` - Effective Latency
Status: `proved`

Define the effective latency by

$$
\delta(u,v):=d_G(u,v).
$$

The key point is structural: latency is derived from locality and graph distance rather than introduced as an independent microscopic delay field.

DEFINITION‑SH‑01 gives a name to something that is already unavoidable: waiting.
Once locality is enforced, influence cannot spread instantly. Even though the update rule acts everywhere at once, information still has to travel through the graph one edge at a time. Effective latency is simply the recognition of that fact. It measures how many update steps must pass before something that happens here can possibly matter there.
This definition does not introduce a new physical quantity. It makes explicit a constraint that was already present. Latency is not chosen, tuned, or imposed — it is inherited from the structure of the graph itself. Two nodes that are far apart in the graph cannot interact quickly, no matter how simple or how clever the update rule is.
What matters is that latency is derived, not assumed. There is no independent speed limit written into the model. The graph itself sets the pace. As a result, delay becomes structural rather than dynamical. It does not depend on what is happening inside nodes, how information is buffered, or how patterns evolve internally. It depends only on connectivity.
By naming latency explicitly, the framework gains a clean way to talk about causal separation without introducing geometry or time coordinates. “Sooner” and “later” begin to acquire meaning, even before spacetime does. This is the step where distance quietly turns into delay, and where the graph starts behaving like a causal scaffold rather than a static network.

### `LEMMA-SH-02` - Metric Properties of Latency
Status: `proved`

The derived latency satisfies:
1. non-negativity,
2. symmetry,
3. triangle inequality,
4. additivity along realized shortest paths.

So the latency structure inherits genuine metric behavior from graph distance.

Latency as structure — a friendly way to think about distance
LEMMA‑SH‑02 observes that once latency is defined, it already behaves like a distance.
This is not because we introduced geometry, but because locality quietly enforces it. If information must travel edge by edge, then the number of update steps separating two nodes has all the familiar features of distance: it is never negative, it is the same in both directions, and it adds along paths. These properties are not assumptions — they fall straight out of how influence is allowed to propagate.
What matters here is not the mathematical formalism, but the consequence. Without drawing a coordinate grid or choosing a dimension, the graph has already acquired a notion of separation that behaves consistently. Some nodes are closer than others, not in space, but in time‑to‑matter. The system knows how far apart things are in the only way that matters operationally: how long it takes for one to affect the other.
This lemma exists to make an important point explicit: geometry does not have to be imposed. Once locality and ordered updates are in place, a metric‑like structure appears on its own. Later, this structure can be reinterpreted as spatial distance, proper time, or causal separation, depending on the regime. At this stage, it remains deliberately modest — a bookkeeping fact about delay that already carries the full weight of distance.

### `DEFINITION-SH-03` - Precedence Relation
Status: `proved`

For events $x=(u,n)$ and $y=(v,m)$ in $X:=V\times\mathbb{Z}$, define

$$
x\prec y
\iff
m\ge n+d_G(u,v).
$$

This converts reachability into a causal ordering relation.

Precedence — a friendly way to think about “before” and “after”
DEFINITION‑SH‑03 introduces precedence: a way to say when one event can meaningfully come before another.
Once latency is in place, not all pairs of events are equal. Some events can influence others, but only after enough update steps have passed. The precedence relation simply records this fact. It says that one event precedes another if information from the first could, in principle, have reached the second in time. Nothing more is assumed.
What matters here is that precedence is not about clocks or simultaneity. It does not measure how much time has passed, only whether influence is possible at all. Two events may be ordered, unordered, or forever unrelated, depending on the structure of the graph and the update order. The notion of “before” is therefore conditional, not absolute.
This definition exists to ground causality without geometry. Instead of starting from spacetime and deriving causal order, UniNet does the reverse. Causal order is defined directly from reachability and delay. Spacetime interpretations, if they appear later, must respect this ordering rather than redefine it.
By naming precedence explicitly, the framework gains a clean way to talk about causal structure without committing to a notion of time that flows everywhere equally. What flows is influence, and precedence simply keeps track of where that flow can go.

### `LEMMA-SH-03` - Partial Order
Status: `proved`

The relation $\prec$ is a partial order on $X$: it is reflexive, transitive, and antisymmetric.

Order — a friendly way to think about consistency
LEMMA‑SH‑03 shows that precedence is not just an informal notion of “earlier” and “later,” but a consistent kind of order.
Once precedence is defined in terms of reachability and latency, it obeys a few simple but crucial rules. An event cannot come before itself in a contradictory way. If one event precedes a second, and the second precedes a third, then the first necessarily precedes the third. And if two events can each influence the other, then they are not meaningfully distinct in causal order. These properties together mean that precedence forms a partial order.
This matters because it keeps causality from becoming ambiguous. The framework allows events to be ordered, unordered, or incomparable — but it does not allow loops of influence that would undermine the idea of cause and effect. Some events genuinely have no causal relationship at all, and that is not a failure of the model. It is a feature. Causality is local and conditional, not global and absolute.
By establishing precedence as a partial order, UniNet gains a stable backbone for everything that follows. Causal histories can be traced without contradiction. Futures and pasts can be defined cleanly. And yet, no assumption of a single global timeline is required. Order exists where influence exists, and nowhere else.
This lemma quietly completes the transition from delay to causality. What began as a restriction on how fast information can travel has now become a coherent structure of “before,” “after,” and “neither,” all without introducing spacetime or clocks.

### `DEFINITION-SH-04` - Causal Futures, Pasts, and Horismos
Status: `proved`

For $x=(u,n)$, define

$$
J^+(x):=\{y\in X:x\prec y\},
$$

$$
I^+(x):=\{(v,m):m>n+d_G(u,v)\},
$$

and

$$
E^+(x):=J^+(x)\setminus I^+(x).
$$

The set $E^+(x)$ is the discrete horismos, or cone boundary.

Futures and pasts — a friendly way to think about possibility
DEFINITION‑SH‑04 gives names to three simple but powerful ideas: what can be affected, what could have caused something, and where the boundary between those two lies.
Once precedence is defined, every event naturally comes with a future and a past. The future of an event is the set of other events it could possibly influence, given enough update steps. The past is the set of events that could have influenced it. These sets are not matters of interpretation or perspective — they are fixed by reachability and latency on the graph.
Between the two sits a boundary: the events that are reachable in the minimal possible time. This boundary marks the edge of influence — the first moment at which something can happen elsewhere, but not before. It separates what is merely possible from what is already inevitable.
This definition exists to make causal structure explicit without introducing spacetime. There is no assumption of lightcones, signals, or geometry, and yet the familiar picture is already present. Some events lie safely inside the future, some forever outside it, and some precisely on the edge. The graph itself draws these distinctions.
By naming futures, pasts, and their boundary, the framework gains a clean language for talking about causality at scale. Histories can be traced, horizons can be identified, and limits of influence become visible — all before any notion of space or time is layered on top. What later looks like spacetime structure is already encoded here as a simple fact about who can affect whom, and when.

### `LEMMA-SH-04` - Horismos Characterization
Status: `proved`

An event $y=(v,m)$ lies on $E^+(x)$ if and only if

$$
m=n+d_G(u,v).
$$

Horismos is therefore exactly minimal-delay reachability.

The edge of influence — a friendly way to think about boundaries in time
LEMMA‑SH‑04 clarifies what it means to be right on the edge of causality.
Once futures and pasts are defined, not all reachable events are the same. Some lie deep inside the future, reachable after many update steps. Others lie exactly at the earliest moment influence can arrive — no sooner, no later. This lemma identifies those edge cases and shows that they form a well‑defined boundary: the set of events reached with minimal possible delay.
What matters here is that this boundary is sharp. There is a clear distinction between events that are merely possible later and those that are possible as soon as the graph allows. Nothing can cross this boundary early, and nothing on it is accidental. It is fixed entirely by locality, connectivity, and update order.
This lemma exists to make horizons unavoidable. Wherever there is finite propagation, there is a frontier of influence. Whether one later calls it a light cone, a causal surface, or a horizon, the structure is already present. It is not imposed by geometry or by dynamics, but by the simple fact that information takes time to travel.
By characterizing this boundary precisely, UniNet gains a clean way to talk about limits of influence without ambiguity. The system knows exactly when something can begin to matter elsewhere, and exactly when it cannot. That clarity will later support discussions of horizons, delays, and observer‑dependent access — but at this stage, it remains a straightforward statement about how far influence can reach in the shortest possible time.


### `PROPOSITION-SH-01` - Closed Cone Structure
Status: `proved`

The pair $(X,\prec)$ together with the future cones $J^+(x)$ defines a closed cone structure in the discrete causal sense used throughout the manuscript. This is the step that makes later imports of time functions, causal pasts, and geodesic analogues meaningful.

Cones — a friendly way to think about causal shape
PROPOSITION‑SH‑01 recognizes that everything introduced so far already fits together as a single structure.
Once reachability, latency, precedence, futures, pasts, and their boundaries are all in place, they do not remain isolated definitions. Together, they form what is effectively a cone‑like causal structure. From any event, influence spreads outward in a constrained way, bounded by delay and ordered by precedence. The future opens up gradually, the past closes behind, and the edge between them remains sharp.
What matters here is not the name “cone,” but the closure. The causal sets defined by these rules behave consistently: they contain all events that can be influenced, exclude those that cannot, and respect the partial order already established. Nothing leaks in from outside, and nothing inside violates the ordering. The structure is self‑contained and stable.
This proposition exists to make an important shift explicit. Up to this point, the framework has been building causal structure piece by piece. Here, it becomes clear that these pieces already form a complete geometry of influence — one that does not rely on spacetime, coordinates, or metrics. What later looks like a light cone or causal cone is already present as a purely relational construct.
By recognizing this closed cone structure, UniNet gains a global view of causality without ever appealing to a background manifold. The graph, the update order, and locality are enough. Geometry, if it appears later, must conform to this structure rather than replace it. In that sense, the cone is not an approximation of spacetime — it is the scaffold from which spacetime can emerge.

## 3.2 Cut Balance and Continuity
### `DEFINITION-SH-02` - Local Conservation / Continuity
Status: `proved`

Let $\rho_n(v)$ be node occupancy and let $J_n(u\to v)$ be an antisymmetric edge flux,

$$
J_n(u\to v)=-J_n(v\to u).
$$

Local conservation means

$$
\rho_{n+1}(v)-\rho_n(v)+\sum_{u\sim v}J_n(v\to u)=0.
$$

This is the microscopic continuity law underlying all later bulk-boundary bookkeeping.

Continuity — a friendly way to think about conservation in motion
DEFINITION‑SH‑02 introduces the idea that change is local and accounted for.
If information is preserved and influence only moves along edges, then changes at a node cannot happen in isolation. Whenever something increases here, it must have come from somewhere nearby. Whenever something decreases, it must be leaving toward a neighbor. Local continuity is simply the statement that these flows balance locally, step by step.
This definition exists to rule out a subtle kind of magic: information appearing or disappearing at a point without explanation. In UniNet, nothing changes without a trail. Every local change can be traced to exchanges with adjacent nodes. Continuity is not imposed as a physical law; it is demanded by honesty in bookkeeping.
What matters is that continuity is local, not global. There is no assumption that large regions are conserved by default. Conservation only holds when all the relevant boundaries are included. At the smallest scale, continuity just says that nodes keep track of what comes in and what goes out, and that the difference shows up as change in their internal state.
By naming local continuity explicitly, the framework prepares the ground for bulk–boundary relations without jumping ahead. This is the step where conservation stops being an abstract slogan and becomes something operational: a rule about how change is allowed to occur, edge by edge, node by node. Everything that later looks like a conservation law is built on this simple insistence that changes must add up locally before they can add up globally.

### `THEOREM-SH-01` - Discrete Gauss/Stokes: Bulk Equals Boundary
Status: `proved`

For any region $R\subseteq V$, define

$$
Q_n(R):=\sum_{v\in R}\rho_n(v)
$$

and

$$
\Phi_n(\partial R)
:=
\sum_{\substack{u\in R,\;v\notin R\\ \{u,v\}\in E}}
J_n(u\to v).
$$

Then

$$
Q_{n+1}(R)-Q_n(R)=-\Phi_n(\partial R).
$$

This is the shared bulk-boundary balance theorem for the entire paper.

Bulk and boundary — a friendly way to think about conservation
THEOREM‑SH‑01 states that whatever changes inside a region must show up at its boundary.
Once local continuity is enforced, this result becomes unavoidable. If every node accounts honestly for what comes in and what goes out, then summing that bookkeeping over a region produces a simple truth: interior change cannot happen on its own. Any increase or decrease inside the region is exactly balanced by what crosses the boundary. There is no other place for it to come from, and no other place for it to go.
This theorem exists to make conservation operational. It does not say that regions are conserved by default. It says that conservation holds only when boundary exchange is included. If a description ignores the boundary, it is incomplete by construction. The boundary is not an optional surface added for convenience — it is where the accounting closes.
What matters is that this result is not tied to geometry, fields, or forces. It is a bookkeeping identity forced by locality and information preservation. No matter how complicated the interior dynamics are, no matter how information is buffered or rearranged, the net change inside a region is fully determined by what crosses its cut.
This is the point where cuts become unavoidable. Drawing a boundary is no longer just a conceptual act; it creates an obligation. If something changes inside, the boundary must carry the record. Everything that later looks like Gauss’s law, flux conservation, or holographic behavior begins here, as a simple refusal to let interior change go unaccounted for.

### `COROLLARY-SH-01` - Exact Closure with Boundary Bookkeeping
Status: `proved`

If the boundary register evolves by

$$
b_{n+1}(\partial R)=b_n(\partial R)+\Phi_n(\partial R),
$$

then the closed regional quantity

$$
\widetilde{Q}_n(R):=Q_n(R)+b_n(\partial R)
$$

is exactly conserved:

$$
\widetilde{Q}_{n+1}(R)=\widetilde{Q}_n(R).
$$

So a region is exactly closed only after boundary exchange is included in the bookkeeping.

Closure — a friendly way to think about completeness
COROLLARY‑SH‑01 explains how a region can finally be treated as closed — and what it takes to earn that status.
The bulk–boundary theorem showed that interior change is always balanced by boundary flux. This corollary takes the next step: if the boundary exchange is tracked explicitly, then the combined description becomes complete. Nothing is missing. Nothing leaks away unaccounted for. The region, together with its boundary register, behaves as a genuinely closed system.
This matters because it draws a sharp line between ignoring a boundary and including it. A region is not closed just because we draw a line around it. It is closed only when everything that crosses that line is accounted for. The boundary register is not an approximation or a correction term — it is the missing piece that makes conservation exact again.
What is important here is that closure is conditional. It depends on what is tracked. Interior variables alone are almost never enough. Once boundary exchange is included, however, the bookkeeping settles. Change inside plus change at the boundary adds up to zero, tick after tick. Conservation is restored without appealing to global assumptions or external constraints.
This corollary makes explicit something that has been implicit since Axiom 8: boundaries are not places where physics breaks down. They are places where physics must be handled carefully. When that care is taken, regions behave cleanly and predictably. When it is not, apparent loss or gain is guaranteed to appear.

## 3.3 Graph Cutting Primitive and Boundary Observability
### `AXIOM-8` - Graph Cutting Primitive

A cut $\partial R$ is horizon-like on a tick interval when interior bookkeeping alone is not closed on that interval. Equivalently, nonzero boundary flux is required to close the regional accounting.

### Boundary Leakiness Terminology
Boundary slack at tick $n$ means the constraints permit

$$
\Phi_n(\partial R)\neq 0.
$$

The cut is leaky at tick $n$ precisely when that inequality holds.

### `THEOREM-SH-02` - Leaky-Boundary Criterion
Status: `proved`

For any region $R\subseteq V$ and tick $n$:
1. $Q_{n+1}(R)=Q_n(R)$ if and only if $\Phi_n(\partial R)=0$,
2. if $\Phi_n(\partial R)\neq 0$, the region exchanges information with its exterior,
3. even then, $\widetilde{Q}_n(R)$ remains exactly conserved when boundary bookkeeping is included.

This is the first nontrivial reason cuts matter physically: one can distinguish truly closed regional bookkeeping from quasi-local closure that depends on a boundary register.

Operationally this is also where boundary observability begins to enter. An observer who does not track boundary data does not possess a closed account of the region.

Leakiness — a friendly way to think about openness
THEOREM‑SH‑02 draws a clear line between regions that are truly closed and those that only appear to be.
Once bulk–boundary balance is established, there are only two possibilities. Either nothing crosses a boundary, in which case the interior can be described on its own, or something does cross, in which case the interior is exchanging with its surroundings. This theorem makes that distinction explicit and precise. A boundary is closed exactly when the net boundary flux vanishes. If it does not, the boundary is leaky, and the region is open by definition.
This matters because it removes ambiguity. There is no gradual notion of “mostly closed” at the bookkeeping level. A region either requires boundary tracking or it does not. If information crosses the cut, even intermittently, then any description that ignores that exchange is incomplete. The leak is not a flaw in the model — it is a fact about how the region interacts with the rest of the graph.
What is important here is that leakiness does not mean loss. Even leaky regions still obey exact conservation once boundary registers are included. What changes is where that conservation lives. For closed cuts, it lives entirely in the interior. For leaky cuts, it is distributed between interior and boundary. The theorem tells us exactly when each description applies.
By naming leakiness explicitly, UniNet turns boundaries into diagnostic tools. Horizons are no longer mysterious surfaces; they are cuts with extreme transport properties. Trapping, release, and long dwell times can all be understood as consequences of how leaky a boundary is. The difference between isolation and interaction is no longer philosophical — it is encoded directly in the bookkeeping.

## 3.4 Leaky Versus Closed Boundaries
The distinction between closed and leaky boundaries is simple mathematically and important physically.

1. Closed cut:

$$
\Phi_n(\partial R)=0,
$$

and interior occupancy is constant without any external bookkeeping.

2. Leaky cut:

$$
\Phi_n(\partial R)\neq 0,
$$

and the region must be described together with a boundary register.

This distinction is shared infrastructure for several later chapters:
1. Chapter 4 uses it to make horizon-like boundaries operational.
2. Chapter 7 uses it in queueing, trapping, and release arguments.
3. Chapter 10 uses it when discussing cosmological packaging and boundary-limited forward maps.

The theorem does not yet tell us how a specific observational channel looks. It tells us when interior closure fails and what must be tracked to restore exact conservation.

## 3.5 Observer-Time, Coarse-Graining, and the Arrow Theorem
### `DEFINITION-SH-05` - Time Function
Status: `proved`

A function $t:X\to\mathbb{R}$ is a time function if

$$
x\prec y \implies t(x)<t(y).
$$

Time functions — a friendly way to think about ordering without clocks
DEFINITION‑SH‑05 introduces the idea of a time function: a way to assign numbers to events that respect causal order.
At this point, causality already exists. Precedence tells us which events can influence which others, and which cannot. A time function does not add new structure to that order. It simply labels it. Its only job is to increase whenever precedence increases. If one event can causally follow another, its assigned time must be later. That is the entire requirement.
What matters here is what a time function does not assume. It does not represent physical time, proper time, or what any observer measures on a clock. It does not need to flow uniformly, or even continuously. It is just a consistent way of numbering events so that “after” always gets a larger value than “before.”
This definition exists to make causal order usable without turning it into geometry. Once a time function exists, histories can be parameterized, slices can be compared, and evolution can be discussed without ambiguity — all while remaining faithful to the underlying partial order. Many different time functions may exist for the same causal structure, and none of them is privileged.
By introducing time functions at this stage, UniNet separates two ideas that are often conflated: causal order and experienced time. The former is structural and unavoidable. The latter is emergent and observer‑dependent. A time function is merely a bookkeeping device that respects causality — a scaffold on which later notions of time can be built, but not yet imposed.

### `LEMMA-SH-05` - Existence of Time Functions
Status: `proved`

For any finite causal set with partial order $\prec$, at least one time function exists.

Existence — a friendly way to think about consistency
LEMMA‑SH‑05 states that time functions are not just a conceptual convenience — they actually exist.
Once causal order has been established as a partial order, it is natural to ask whether that order can be labeled consistently. This lemma answers yes. There is always at least one way to assign values to events such that causally later events receive larger values than earlier ones. In other words, the causal structure is coherent enough to support a global ordering parameter, even if that parameter is not unique.
This matters because it shows that the framework is not teetering on an abstraction that cannot be realized. Causality does not merely exist in principle; it can be organized, traced, and parameterized. The graph does not contain hidden contradictions that would prevent histories from being laid out in a consistent way.
What is important here is what the lemma does not say. It does not claim that there is a single preferred time function, or that any particular choice corresponds to physical time as experienced by observers. Many such functions may exist, and different choices may be useful for different purposes. The existence of a time function guarantees consistency, not uniqueness.
By establishing this existence result, UniNet ensures that its causal structure is navigable. One can move forward along causal chains, compare histories, and reason about evolution without ambiguity. Time, at this level, is not something that flows — it is something that can be assigned without breaking causality.

### `DEFINITION-SH-06` - Volume-Based Time
Status: `proved`

Define observer time by past-set size:

$$
t_{\mathrm{obs}}(v,n):=|J^-((v,n))|.
$$

This is monotone along precedence because causal pasts enlarge along causal order.

Observer time — a friendly way to think about “now”
DEFINITION‑SH‑06 introduces observer time: a notion of time tied to what an observer can actually access.
Up to this point, time has been abstract. Precedence and time functions organize events consistently, but they are not yet anchored to experience. Observer time makes that connection. It assigns a time value to an event based on the size of its causal past — how much of the graph could, in principle, have influenced it.
This definition exists to ground time in information, not in clocks. An observer does not measure time by reading off a global parameter, but by accumulating evidence. As more events become causally accessible, the observer’s notion of “now” advances. Time, in this sense, is counted by what has already happened for that observer, not by what could be happening elsewhere.
What matters is that observer time is monotonic by construction. As causal pasts grow, observer time can only increase. This gives a direction to time without introducing irreversibility at the fundamental level. The underlying dynamics may remain reversible, but the observer’s record is not. Once an event enters the causal past, it cannot be removed.
By defining time this way, UniNet separates experienced time from update order cleanly. The tick orders updates everywhere, but observer time reflects access and accumulation locally. Different observers may assign different times to the same event, and that disagreement is not a paradox. It is a consequence of different causal pasts.
Observer time is not yet thermodynamic time, nor psychological time. It is something simpler and more structural: a measure of how much of the world has become available. From this alone, the arrow of time will later emerge — not because the universe prefers a direction, but because observers can only ever gain causal past, never lose it.

### `DEFINITION-SH-07` - Time Separation
Status: `proved`

Define the time separation between events by

$$
\tau(x,y):=\max_{\gamma:x\to y}\int_\gamma d\ell,
$$

where the maximization is over causal curves and $d\ell$ is the relevant causal-length element.

Separation — a friendly way to think about “how far apart” events are
DEFINITION‑SH‑07 introduces time separation: a way to compare events not just by order, but by how much causal structure lies between them.
Once causal order and observer time are defined, it becomes meaningful to ask a more refined question: given two events that can be causally related, how far apart are they along the allowed paths of influence? Time separation answers this by looking at the longest causal chain connecting one event to another. It measures distance in terms of process, not position.
This definition exists to avoid importing spatial intuition too early. Time separation is not a coordinate difference and not a metric on a background space. It is a statement about how much evolution must occur for one event to give rise to another. Two events may be ordered but close, or ordered and very far apart, depending on how many updates and intermediate influences lie between them.
What matters is that time separation is intrinsic to the causal structure itself. It does not depend on how an observer labels time, nor on which time function is chosen. Different observers may assign different times to events, but the maximal causal separation between them remains the same. In that sense, separation is more robust than time labels — it is a property of the causal graph, not of its parameterization.
By defining time separation explicitly, UniNet gains a way to talk about durations without clocks. Processes can be short or long, shallow or deep, without ever referring to spacetime intervals. This prepares the ground for later interpretations where separation may be read as proper time, path length, or action — but at this stage, it remains exactly what it is: a count of how much causally ordered change fits between two events.

### `DEFINITION-SH-08` - Coarse-Graining Observation Map
Status: `proved`

Let

$$
\Phi_{\mathrm{cg}}:\mathcal{H}\to\mathcal{M}
$$

be an observation map that retains macroscopic observables while discarding phase-resolved microscopic data. In general this map is non-injective.

Coarse‑graining — a friendly way to think about forgetting
DEFINITION‑SH‑08 introduces coarse‑graining: the step where rich internal detail is intentionally left behind.
Up to this point, the framework has been careful to preserve information. Dynamics are reversible, updates are local, and nothing is destroyed. Coarse‑graining does not change any of that. What it changes is what is kept. Instead of tracking every microscopic detail, a coarse‑grained description retains only certain aggregate features and discards the rest.
This definition exists to formalize a simple fact about observation: observers never have access to the full internal state. What they record is always a summary. Many different interior configurations may look identical once viewed through the same boundary and reduced to the same set of observables. Coarse‑graining makes that reduction explicit.
What matters is that coarse‑graining is generally non‑invertible. Once details are dropped, there is no unique way to recover them. This does not mean the information is gone — Axiom 7 still holds. It means that reconstructability is lost at the level of description. Multiple microscopic histories collapse into the same observed record.
By defining the coarse‑graining map explicitly, UniNet draws a clean boundary between dynamics and description. The underlying evolution remains reversible, but the observer’s account does not have to be. This is the precise point where irreversibility can enter without contradiction. Not because the universe forgets, but because observers do.
Coarse‑graining is therefore not a flaw or approximation. It is the price of access. And it is the final ingredient needed for the arrow of time to emerge — not from dynamics, but from description.

### `THEOREM-SH-03` - Emergent Arrow from Non-Injective Observation
Status: `proved`

Assume unitarity, the observer-time construction, and the coarse-graining map. For

$$
m_n:=\Phi_{\mathrm{cg}}(U^n\psi_0),
$$

the following hold:
1. microscopic evolution is reversible,
2. macroscopic observation is generally non-invertible because $\Phi_{\mathrm{cg}}$ is non-injective,
3. along monotone observer time, observers restricted to $m_n$ recover an effective forward-only history.

The arrow of time is therefore not a Tier-0 axiom. It is an observational consequence of information hiding under coarse-graining.

The arrow — a friendly way to think about direction
THEOREM‑SH‑03 explains how time acquires a direction without ever being told to.
Up to this point, nothing in the framework prefers a past or a future. Updates are reversible, locality is symmetric, and the fundamental tick carries no arrow. And yet, once coarse‑graining and observer time are introduced, a direction becomes unavoidable. This theorem shows that the arrow of time emerges not from the dynamics, but from how those dynamics are seen.
The key idea is simple. Observation collapses many possible interior histories into the same coarse‑grained record. Once that happens, there is no unique way back. Information has not been destroyed — Axiom 7 still holds — but reconstructability has been lost. From the observer’s point of view, multiple pasts now lead to the same present, while the present still branches into many possible futures. That asymmetry is the arrow.
What matters is where this asymmetry lives. It is not in the update rule. It is not in the graph. It is not in the fundamental notion of time. It appears at the boundary between full microscopic description and partial observational access. As observer time increases, causal pasts grow and records accumulate. Nothing ever leaves the past, but new events continually enter it. That monotonic growth gives time its apparent direction.
This theorem exists to separate two ideas that are often conflated. Microscopic evolution remains reversible. Macroscopic experience does not. The arrow of time is therefore not a fundamental law, but a consequence of boundary‑limited, coarse‑grained observation. Time points forward not because the universe insists on it, but because observers cannot undo what they no longer have access to.

### `COROLLARY-SH-02` - QM Sector Consequence
Status: `proved`

In the QM regime, latency remains fixed at graph distance, so no extra microscopic time-direction postulate is added there. The observed arrow is attributed entirely to coarse-graining and the measurement interface.

### `COROLLARY-SH-03` - GR Sector Consequence
Status: `proved`

In the GR regime, adaptive latency and queue constraints strengthen one-way operational behavior in near-saturation regions through long dwell and boundary-dominant release, without violating microscopic reversibility.

### `COROLLARY-SH-04` - SM Sector Consequence
Status: `proved`

CP asymmetry may modify sector-level channels, but it is not the foundational source of irreversibility. The thermodynamic arrow still rests on `THEOREM-SH-03`.

## 3.6 Shared Theorem Summary Table
The shared spine can be summarized as follows.

| Paper ID | Content | Main dependencies | First major later use |
|---|---|---|---|
| `LEMMA-SH-01` | finite propagation bound | `AXIOM-6` | QM and GR regime split |
| `DEFINITION-SH-01` | derived latency | `LEMMA-SH-01` | causal order and regime chapters |
| `DEFINITION-SH-02` | local continuity | `AXIOM-7` plus graph-local flux representation | cut balance, queueing, GR |
| `THEOREM-SH-01` | bulk-boundary balance | `DEFINITION-SH-02` | boundary chapter, update chapter |
| `THEOREM-SH-02` | leaky-boundary criterion | `THEOREM-SH-01` | boundary and GR sectors |
| `PROPOSITION-SH-01` | closed cone structure | precedence plus horismos definitions | observer-time and geometry-facing chapters |
| `THEOREM-SH-03` | emergent arrow | unitarity plus coarse-graining | QM, GR, SM, philosophy |

## Chapter 3 Summary
Established in this chapter:
1. finite propagation and derived latency,
2. discrete cut balance and exact closure with boundary bookkeeping,
3. causal order, cone structure, and observer-time scaffolding,
4. an emergent arrow of time from non-injective observation.

Open:
1. the stronger operational boundary-observability theorems, deferred to Chapter 4,
2. sector-specific transport, standing-wave, and projection packages, deferred to later chapters.


This chapter has not introduced new physical ingredients. It has only followed the axioms to their natural conclusions.
Starting from locality, ordered updates, and information preservation, the graph was forced to acquire structure. Influence became limited. Delay became unavoidable. Causal order appeared without being assumed. From there, futures and pasts emerged, along with sharp boundaries between what can matter now and what cannot yet matter at all. Conservation followed as a matter of honest bookkeeping, tying interior change to boundary exchange and making closure conditional rather than assumed.
When boundaries were taken seriously, observation became local and mediated. Once coarse‑graining entered, reconstructability was lost even though information was not. And with that final step, time quietly acquired a direction — not because the dynamics demanded it, but because observers could no longer undo what they could no longer see.
Nothing in this chapter relied on spacetime, geometry, fields, or forces. And yet, the essential scaffolding of all of them is already present. Causality has shape. Conservation has a location. Horizons have meaning. Time has direction, but only from a point of view.
What follows in later chapters is not the invention of new structure, but the interpretation of what is already here. Relativity, quantum behavior, and particle‑like motion will be read as different ways this same causal, boundary‑aware substrate presents itself when viewed through different lenses. Chapter 03 is therefore not a detour. It is the point at which the framework stops making assumptions and starts making promises.

---

## Dependency DAG Update (Born Theorem and Flux Lemma)

This update introduces two new formal results:

- `LEMMA-FLUX-01` — Flux proportional to occupancy  
- `THEOREM-BORN-01` — Born rule as a cut–statistics theorem  

It also introduces one explanatory block (non‑DAG).

---

### DAG Node: LEMMA-FLUX-01
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

### DAG Node: THEOREM-BORN-01
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

### DAG Note: Conceptual Block (Measurement as Cut Interaction)
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


### DAG Node: THEOREM-SUS-01
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
### DAG Cross-Links to Add
---

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

#### DAG Placement Summary

- `LEMMA-FLUX-01` sits **just above** the witness family and **just below** the Born theorem.  
- `THEOREM-BORN-01` sits **in the shared spine**, but **below** the core axioms and **above** any sector-specific QM constructions.  
- The conceptual block is **not part of the DAG**.
