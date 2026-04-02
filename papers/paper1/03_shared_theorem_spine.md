# Chapter 3 - Shared Theorem Spine

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

### `LEMMA-SH-02` - Metric Properties of Latency
Status: `proved`

The derived latency satisfies:
1. non-negativity,
2. symmetry,
3. triangle inequality,
4. additivity along realized shortest paths.

So the latency structure inherits genuine metric behavior from graph distance.

### `DEFINITION-SH-03` - Precedence Relation
Status: `proved`

For events $x=(u,n)$ and $y=(v,m)$ in $X:=V\times\mathbb{Z}$, define

$$
x\prec y
\iff
m\ge n+d_G(u,v).
$$

This converts reachability into a causal ordering relation.

### `LEMMA-SH-03` - Partial Order
Status: `proved`

The relation $\prec$ is a partial order on $X$: it is reflexive, transitive, and antisymmetric.

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

### `LEMMA-SH-04` - Horismos Characterization
Status: `proved`

An event $y=(v,m)$ lies on $E^+(x)$ if and only if

$$
m=n+d_G(u,v).
$$

Horismos is therefore exactly minimal-delay reachability.

### `PROPOSITION-SH-01` - Closed Cone Structure
Status: `proved`

The pair $(X,\prec)$ together with the future cones $J^+(x)$ defines a closed cone structure in the discrete causal sense used throughout the manuscript. This is the step that makes later imports of time functions, causal pasts, and geodesic analogues meaningful.

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

### `LEMMA-SH-05` - Existence of Time Functions
Status: `proved`

For any finite causal set with partial order $\prec$, at least one time function exists.

### `DEFINITION-SH-06` - Volume-Based Time
Status: `proved`

Define observer time by past-set size:

$$
t_{\mathrm{obs}}(v,n):=|J^-((v,n))|.
$$

This is monotone along precedence because causal pasts enlarge along causal order.

### `DEFINITION-SH-07` - Time Separation
Status: `proved`

Define the time separation between events by

$$
\tau(x,y):=\max_{\gamma:x\to y}\int_\gamma d\ell,
$$

where the maximization is over causal curves and $d\ell$ is the relevant causal-length element.

### `DEFINITION-SH-08` - Coarse-Graining Observation Map
Status: `proved`

Let

$$
\Phi_{\mathrm{cg}}:\mathcal{H}\to\mathcal{M}
$$

be an observation map that retains macroscopic observables while discarding phase-resolved microscopic data. In general this map is non-injective.

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
