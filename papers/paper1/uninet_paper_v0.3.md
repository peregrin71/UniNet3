# Chapter 0 - Abstract and Reader Guide

This paper is written to be readable on a first pass and auditable on a second pass. It aims to minimize hidden assumptions without flattening all claims into the same certainty level. The manuscript therefore separates core axioms from modeling and bridge postulates, theorem-level structure from deferred structure, and compact paper-facing falsifiability rows from the fuller governance machinery carried elsewhere in the paper.

## 0.1 Abstract
UniNet is presented here as a graph-based, local, information-preserving update framework with one declared update-rule family

$$
\psi_{n+1}=U_n\psi_n.
$$

Paper 1 does not claim full closure of quantum mechanics, general relativity, the Standard Model, or cosmology. Its narrower aim is to establish a shared structural spine: finite propagation from graph locality, exact bulk-boundary bookkeeping, a rigorous distinction between closed and leaky cuts, causal order from derived latency, and an emergent arrow of time from non-injective observation. Where additional sector structure is needed, the manuscript states that dependence openly through labeled model postulates, bridge postulates, or deferred obligations. The result is intended to be formal, falsifiability-aware, and explicit about what remains open.

## 0.2 How to Read This Paper
There are two valid reading paths.

The fast path is:
1. read Chapters 1 through 5 for the motivation, the minimal core, the shared theorem spine, and the update-function constraints,
2. read the sector chapter of interest,
3. use the compact falsifiability rows in that chapter to see what the framework actually risks observationally.

The full audit path is:
1. read Chapters 2 and 3 carefully,
2. use the paper's relabeled theorem and definition IDs as canonical references,
3. follow the dependency flow through the manuscript-level DAG,
4. use the governance and appendix material to inspect status tags, parameter locks, and reject criteria.

Logical dependence runs mainly forward:

$$
\text{core axioms}
\to
\text{shared theorem spine}
\to
\text{boundary and update layers}
\to
\text{sector chapters}
\to
\text{governance and philosophy}.
$$

Forward references are allowed for navigation, but not for proof dependence.

## 0.3 Claim-Status Legend
The manuscript uses four primary claim tags and two symmetry-specific qualifiers.

| Tag | Meaning |
|---|---|
| `proved` | theorem-level claim with an explicit dependency path |
| `postulate` | explicit modeling choice, not internally derived |
| `deferred` | incomplete map, proof, or threshold; not promotable yet |
| `external-constraint` | imported theorem class or empirical restriction with explicit scope |
| `noether-like` | invariant structure is present, but full variational current/charge closure is incomplete |
| `deferred-noether` | a stronger Noether-style statement still requires action-domain and boundary formalization |

Language in the paper follows a strict discipline: if a statement is not tagged `proved`, it is not written as settled fact.

## 0.4 Notation, Units, and Status Guide
Core notation:
1. the substrate graph is $G=(V,E)$,
2. discrete substrate updates are indexed by $n\in\mathbb{Z}$,
3. the global state is $\psi_n\in\mathcal{H}$ and node-local state is $\psi_v(n)$,
4. buffering occupancy is $\rho(v,n)=\|\psi_v(n)\|^2$,
5. cut bookkeeping uses $J_n(u\to v)$, $Q_n(R)$, and $\Phi_n(\partial R)$,
6. causal and geometric quantities use $J^\pm(x)$, $E^+(x)$, $t_{\mathrm{obs}}$, and $\tau(x,y)$.

Units policy:
1. dimensionless model variables are stated with unit `1`,
2. physical observables use explicit SI units when projected,
3. the paper distinguishes microscopic model variables, projected observables, and derived map quantities.

Formatting policy:
1. inline math uses `$...$`,
2. display math uses `$$...$$` on separate lines,
3. one canonical symbol is kept per concept unless a relabeling is explained explicitly.

## 0.5 Formula Presentation Rule
Every major claim keeps a primary formula in native UniNet notation. Lagrangian or action-based companion forms are added where the claim depends on variation, source-curvature coupling, or Noether-style promotion.

In practice:
1. kinematic and bookkeeping statements stay in native form,
2. variational companions are mandatory for claims marketed as action- or symmetry-derived,
3. sector falsifiability rows stay operational rather than variational.

Where both forms are present, the manuscript uses the order:
1. native statement,
2. variational companion when applicable,
3. status tag,
4. boundary note if variational closure is still incomplete.

## Chapter 0 Summary
Established in this chapter:
1. the reading contract of the paper,
2. the status-tag vocabulary,
3. the notation and formula-presentation rules.

Open:
1. no scientific claim is settled here beyond the manuscript contract itself.

---

# Chapter 1 - Human Introduction

The human problem behind UniNet is simple to state: modern fundamental physics works exceptionally well, but it still presents several of its most important structures as separate starting points. Geometry, quantum state evolution, gauge packaging, and cosmological sectors usually enter as distinct frameworks with their own privileged primitives. UniNet is an attempt to reduce that starting set, not to add another layer of disconnected formalism.

## 1.1 Why This Framework Exists
Standard presentations of quantum theory, general relativity, and the Standard Model are computationally successful, but they distribute conceptual weight across multiple axiomatic fronts. Quantum theory typically begins with Hilbert-space evolution and measurement rules. General relativity typically begins with spacetime geometry and field equations. The Standard Model typically begins with gauge structure and representation content. Cosmology then adds another effective layer on top.

UniNet asks a narrower question: how much of that visible macroscopic structure can be forced by a smaller microscopic substrate?

The paper does not start by assuming:
1. smooth spacetime as fundamental,
2. a separate collapse law,
3. a separate particle ontology,
4. a separate gauge principle as the first move.

Instead it starts from a graph substrate, a single declared update-rule family, graph locality, and no information loss. The wager is that if these constraints are strong enough, then latency, cuts, boundary bookkeeping, and stable mode structure should not be optional add-ons. They should appear because there is no coherent alternative once transport is local and reversible.

## 1.2 Core Intuition
The core picture is a large graph carrying reversible update dynamics.

At each tick:
1. each node stores internal state,
2. a single update-rule family propagates that state locally,
3. information can accumulate or disperse through buffering occupancy,
4. no information is destroyed by the microscopic evolution.

Once locality is enforced, influence cannot jump arbitrarily across the graph. That immediately creates a minimal latency structure. Once regions are cut out, their interior bookkeeping is not generally closed unless boundary exchange is tracked explicitly. Once observation is coarse-grained, an observer does not see microscopic phase-resolved state; the observer sees delayed, boundary-limited, and compressed macroscopic summaries.

That is why cuts and boundaries are not a side topic in this framework. They are the operational interface between microscopic determinism and macroscopic description.

The resulting picture is deliberately spare:
1. locality gives finite propagation,
2. finite propagation gives latency,
3. latency plus cuts gives causal and boundary structure,
4. coarse-graining over that structure gives an emergent arrow and sector packaging.

## 1.3 What This Paper Does and Does Not Claim
Paper 1 claims a shared theorem spine and an audit discipline. It does not claim complete sector closure.

What the paper does claim:
1. the Tier-0 locality, unitarity, buffering, and update-law core is explicit,
2. the shared causal, cut-balance, and coarse-graining structure is theorem-level where tagged `proved`,
3. sector packaging is traceable to declared assumptions instead of being hidden upstream,
4. falsifiability is part of the manuscript itself rather than an external afterthought.

What the paper does not claim:
1. full Standard Model derivation,
2. full microscopic-to-observable closure in every sector,
3. completed black-hole quantitative closure,
4. completed Noether promotion in all symmetry blocks,
5. unique determination of the admissible update family.

That boundary matters. The point of this paper is not to flatten all uncertainty into one rhetorical register. The point is to separate proved structure from postulated bridges and from deferred forward maps.

## 1.4 Roadmap
The manuscript order is meant to mirror the dependency graph.

1. Chapter 2 separates the foundational core from modeling and bridge choices.
2. Chapter 3 states the shared theorem spine on which every sector depends.
3. Chapter 4 makes graph cuts and boundaries operational.
4. Chapter 5 constrains the update function before any sector-specific reading.
5. Chapter 6 places symmetry and variational formalism in one shared layer.
6. Chapters 7 through 10 package general relativity, quantum mechanics, the Standard Model, and cosmology in that order, each with assumption ledgers, proof obligations, and compact falsifiability rows.
7. Chapter 11 explains how to audit the manuscript against the governance artifacts.
8. Chapter 12 interprets the framework philosophically without upgrading theorem status.
9. Chapter 13 closes with the Paper 2 handoff.

The intended reading discipline is therefore: understand the shared structure first, then read any sector chapter as a constrained specialization rather than as a new starting point.

## Chapter 1 Summary
Established in this chapter:
1. the motivation for a reduced microscopic starting set,
2. the centrality of cuts, boundaries, and delayed observability,
3. the paper's scope boundary between shared structure and sector closure.

Open:
1. the formal shared theorem backbone, which begins in Chapter 3,
2. the constructive standing-wave and Regge/GR packages, which are deferred to later chapters.

---

# Chapter 2 - Core Axioms and Modeling Layer

This chapter fixes the contract of the paper. The core axioms are the minimal substrate commitments. Modeling postulates and bridge postulates are useful, often necessary, and fully legitimate, but they are not allowed to masquerade as microscopic inevitabilities. The distinction is what keeps the manuscript auditable.

Chapter 02 — Fixing the ground before building on it
Before asking what the universe does, this chapter asks what it is allowed to do.
Modern physics is rich with structure, but much of that structure is often introduced early and all at once: spacetime, fields, particles, actions, and symmetries arrive together, tightly coupled. UniNet takes a different approach. Rather than beginning with powerful formalisms, it begins by fixing the minimal conditions under which any consistent description must operate.
The axioms in this chapter are not meant to be ambitious. They are meant to be careful. Each one removes a specific kind of shortcut: hidden infinities, privileged locations, special rules, unexplained loss, or unexamined assumptions about observation. Together, they define a substrate that is local, finite, reversible, and honest about boundaries — without yet committing to geometry, dynamics, or ontology.
Just as important as what is fixed here is what is left open. This chapter deliberately separates core commitments from modeling choices. Representation layers, projection maps, and interpretive bridges are acknowledged, but not elevated. They will appear later, explicitly labeled, when they are actually needed. Nothing in this chapter assumes quantum mechanics, general relativity, or any specific notion of spacetime. Those frameworks are treated as readings of the structure that follows, not as inputs to it.
The purpose of Chapter 02 is therefore not to explain phenomena, but to set the rules of engagement. It establishes the ground on which all later arguments will stand. Once these axioms are accepted, many familiar structures will turn out not to be optional at all. Chapter 03 will follow that thread, showing what must already be true once the ground is fixed this way.

## 2.1 Core Axioms
The canonical core order used in this paper is the following.

| ID | Formal statement | Reading |
|---|---|---|
| `AXIOM-1` | The substrate is a finite, connected, undirected simple graph $G=(V,E)$. | Minimal carrier of adjacency and reachability. |
| `AXIOM-2` | If $\varphi:G\to G'$ is a graph isomorphism, then $\varphi_*(U_G(\psi))=U_{G'}(\varphi_*(\psi))$. | Physics is invariant under relabeling. |
| `AXIOM-3` | Evolution is ordered by a discrete global update parameter $n\in\mathbb{Z}$. | The theory has one declared update ordering variable. |
| `AXIOM-4` | There is one declared update-rule family $\psi_{n+1}=U_n\psi_n$; in static branches one may have $U_n\equiv U$. | The theory does not allow hidden law switching. |
| `AXIOM-5` | There exists one admissible local rule family $F$ such that $(U_n\psi)_v=F\big((\psi_u)_{u\in N[v]},\mathcal{O}_v(n)\big)$ for every node $v$, with the same functional form used across the graph. | Update homogeneity: no hidden per-node laws. |
| `AXIOM-6` | Graph locality: $(U_n\psi)_v$ depends only on data on the closed neighborhood $N[v]$, so one update step reaches at most one hop. | Interactions are local. |
| `AXIOM-7` | Each admissible update is information-preserving: $U_n^\dagger U_n=I$, hence $\|\psi_{n+1}\|=\|\psi_n\|$. | No information loss. |
| `AXIOM-8` | Graph cuts are primitive. For a region $R\subseteq V$, regional closure is not assumed a priori; generically one must track boundary flux through $\partial R$. | Graph cutting is foundational, not optional. |
| `AXIOM-9` | Interior microstates are operationally accessible only through boundary observables. Formally, for a cut $\partial R$, exterior equivalence is determined by $\psi|_R \sim_{\partial R} \psi'|_R \iff \mathcal{O}(\partial R;\psi)=\mathcal{O}(\partial R;\psi')$. | Observers access boundaries, not interiors directly. |
| `AXIOM-10` | Long-lived particle-like excitations are boundary-stabilized standing or quasi-standing modes, represented ideally by $U\phi=\lambda\phi$ with $|\lambda|=1$, or by narrow spectral packets $\psi_n=\sum_r c_r\lambda_r^n\phi_r$. | Particle structure is mode structure, not primitive node-local substance. |

### AXIOM-1
The graph — a friendly way to think about the substrate
UniNet begins with a graph not because graphs are special, but because relations have to live somewhere. A graph is the smallest structure that lets us talk about adjacency, separation, and connection without already assuming geometry or spacetime. It simply says: there are things, and some of them are next to each other.
By requiring the graph to be finite and connected, the framework avoids hidden infinities and disconnected worlds that never interact. Everything that happens is part of one system, and every influence must trace a path. Nothing appears from nowhere, and nothing is forever out of reach. At this stage, the graph carries no metric, no dimension, and no notion of distance beyond adjacency. Those emerge later. Here, the graph only commits us to the idea that physics is relational and that relations are not optional.

### AXIOM-2
Relabeling — a friendly way to think about symmetry
Axiom 2 is the quiet insistence that names do not matter.
In UniNet, nothing physical is allowed to depend on how nodes are labeled or how the graph is drawn on paper. Renaming a node, reordering a list, or choosing a different description of the same connectivity cannot change what happens. If two graphs differ only by relabeling, they are the same system, not two different ones.
This axiom exists to block a very common mistake: smuggling structure into a model through notation. Coordinates, indices, and labels are tools for description, not ingredients of reality. Whatever is physically meaningful must survive any consistent renaming of the graph. If it doesn’t, it wasn’t physical to begin with.
Once this is accepted, symmetry stops being something added later and becomes a baseline discipline. Only relations, adjacencies, and patterns of interaction are allowed to matter. Everything else is bookkeeping. Axiom 2 doesn’t tell the system how to evolve — it tells us how seriously to take our descriptions.

### AXIOM-3
Update order — a friendly way to think about the tick
Axiom 3 states that change happens in steps, and that those steps can be ordered.
The index $n$ is not physical time and it is not something an observer measures. It is simply a way to say that updates occur one after another. Something happens, then something else happens. That much structure is unavoidable if we want to talk about causation at all. Without an ordering, “before” and “after” lose their meaning, and influence becomes impossible to trace.
By committing to a discrete update order, UniNet avoids smuggling in continuous clocks, global simultaneity, or hidden background time. The tick does not say how long anything takes — only that there is a next step. Because updates are local, this minimal ordering is already enough to produce delay, reachability constraints, and causal structure. Information cannot arrive before it has had time to propagate.
Importantly, nothing about the tick prefers a direction. The underlying update can be reversible, and the ordering itself does not distinguish past from future. Any arrow of time that appears later comes from how states are observed and coarse‑grained, not from the update order itself. At this level, the tick is simply the framework’s way of keeping change honest: a shared rhythm that allows influence to move, but does not yet tell us how time feels.

### AXIOM-4
One update rule — a friendly way to think about lawfulness
Axiom 4 insists that there is only one update rule family governing the entire graph.
This does not mean that everything behaves the same way. It means that the rules themselves do not change from place to place or moment to moment. The universe does not get to quietly switch laws when it becomes inconvenient. Whatever complexity appears later must come from the state of the system, not from hidden changes in how updates are applied.
This axiom exists to rule out a subtle but powerful escape hatch: explaining structure by special treatment. Without it, one could always declare that certain regions evolve differently, or that new rules activate when particular conditions are met. Axiom 4 blocks that move. If something interesting happens, it must happen because the same rule is acting on different configurations, not because the rule itself was replaced.
By committing to a single update family, UniNet treats lawfulness as global and impartial. The update rule is not something the system negotiates with — it is the backdrop against which all variation plays out. At this stage, nothing is said about the detailed form of the rule, only that it is shared. Diversity, hierarchy, and apparent exceptions must all emerge downstream, without ever appealing to a different law.

### AXIOM-5
Homogeneity — a friendly way to think about sameness
Axiom 5 states that the update rule is applied uniformly across the graph.
This does not mean that all nodes behave the same way. It means that no node is given special treatment by the rule itself. The same kind of update acts wherever it is applied, regardless of location, label, or role. Any differences that appear must come from differences in state, connectivity, or history — not from a rule that quietly changes its behavior depending on where it is used.
This axiom exists to separate law from circumstance. Without it, one could always explain structure by hiding extra instructions inside particular nodes or regions. Homogeneity blocks that move. It forces the framework to account for complexity honestly, as something that emerges from interaction and accumulation, not from privileged sites or hand‑tuned exceptions.
Once this is accepted, sameness becomes a strength rather than a limitation. Rich behavior does not require special rules; it requires only that the same rule be applied under different conditions. Axiom 5 makes that commitment explicit. It says that whatever patterns, hierarchies, or apparent asymmetries arise later must do so without ever appealing to a different kind of update — only to different configurations of the same one.

### AXIOM-6
Locality — a friendly way to think about influence
Axiom 6 states that updates are local: what happens at a node can only depend on information in its immediate neighborhood.
This axiom exists to rule out influence without contact. Nothing is allowed to jump across the graph, skip over intermediate nodes, or act at a distance. If something changes somewhere, that change must propagate step by step along edges. Every effect traces a path. There are no shortcuts.
Once locality is enforced, delay becomes unavoidable. Information cannot arrive faster than the graph allows it to travel, and influence spreads outward one connection at a time. From this alone, a causal structure emerges. Some events can affect others, some cannot, and some can only do so after enough update steps have passed. No geometry is assumed here — only adjacency — yet the graph already knows how to order influence.
Importantly, locality does not say what happens when information arrives, only when it can. Internal dynamics, buffering, and release can vary, but locality fixes the earliest possible moment at which an effect may appear elsewhere. In that sense, Axiom 6 is where the framework commits to causation without yet committing to spacetime. Everything that later looks like cones, horizons, or discrete geometry is already hiding in this simple refusal to let information jump.

### AXIOM-7
Information preservation — a friendly way to think about reversibility
Axiom 7 states that the fundamental update preserves information.
This does not mean that information is always accessible, visible, or easy to reconstruct. It means something simpler and stricter: nothing is destroyed by the update itself. Whatever changes occur, they rearrange information rather than erase it. The system may hide information behind delays, boundaries, or coarse descriptions, but it never deletes it at the substrate level.
This axiom exists to keep the framework honest about cause and effect. Without it, one could always explain away discrepancies by appealing to loss at the fundamental level. Axiom 7 blocks that escape. If information seems to disappear, it must have gone somewhere — into a buffer, across a cut, or into degrees of freedom no longer tracked by the observer.
Importantly, information preservation does not guarantee reconstructability. Many distinct internal histories may lead to the same observable state once viewed through boundaries and coarse‑graining. The underlying evolution remains reversible even when the description is not. This separation is deliberate. It allows irreversibility, entropy, and arrows of time to emerge later as features of access and description, rather than being imposed as axioms.
At this level, Axiom 7 simply says that the substrate does not forget. Whatever forgetting occurs belongs to observers, not to the dynamics itself.

### AXIOM-8
Cuts — a friendly way to think about boundaries
Axiom 8 states that cuts are primitive.
The moment a region is distinguished from the rest of the graph, a boundary appears, and that boundary is not optional. It is not an approximation, not a later construction, and not something introduced for convenience. A cut marks the point where interior bookkeeping stops being self‑contained and where exchange with the outside must be accounted for explicitly.
This axiom exists to prevent a very common assumption: that regions can be treated as closed unless proven otherwise. In UniNet, the opposite is true. Closure is earned, not assumed. If information crosses a boundary, then any description that ignores that exchange is incomplete by construction. The boundary is where conservation is enforced, where delays become visible, and where interior and exterior descriptions meet.
Once cuts are taken seriously, many familiar ideas fall into place. Horizons are no longer exotic objects; they are simply cuts with extreme transport properties. Observers are no longer privileged viewpoints; they are interfaces defined by what their boundaries allow them to access. Even the distinction between reversible microscopic dynamics and irreversible macroscopic behavior traces back to what is hidden behind a cut and what is allowed to pass through.
Axiom 8 does not introduce new dynamics. It introduces accountability. It insists that whenever we draw a line around part of the system, we must also take responsibility for what crosses that line. Everything that later looks like bulk–boundary relations, holography, or horizon behavior begins with this refusal to treat boundaries as afterthoughts.

### AXIOM-9
Observation — a friendly way to think about access
Axiom 9 states that interior states are accessible only through boundaries.
In UniNet, observers never see the inside of a region directly. Whatever lies within must be inferred from what crosses the boundary or is registered there. This is not a limitation of technology or measurement; it is a structural fact. The moment a cut exists, access is mediated. The boundary becomes the interface through which all observation occurs.
This axiom exists to make a simple idea explicit: knowledge is always local and filtered. No observer has privileged access to the full microscopic state of the system. What can be known depends on where the observer is situated and which boundaries they can interact with. Two different interior configurations that produce the same boundary behavior are indistinguishable from the outside, even if they differ internally.
Once this is accepted, several familiar notions fall into place. Redundancy is no longer mysterious; it is simply the freedom to rearrange interiors without changing what the boundary reveals. Disagreement between observers becomes possible without contradiction, as long as their boundaries do not overlap in causal history. And the distinction between reversible dynamics and irreversible descriptions emerges naturally, as boundary‑limited observation collapses many possible interiors into the same observable record.
Axiom 9 does not introduce measurement as a special process. It removes the assumption that observation ever reaches all the way in. What an observer sees is always a boundary story — partial, delayed, and shaped by what the cut allows to pass.

### AXIOM-10
Persistence — a friendly way to think about things
Axiom 10 states that long‑lived structures are not primitive objects, but stable patterns.
In UniNet, nothing is assumed to be a “thing” simply by declaration. What persists does so because it is supported by the dynamics. Certain configurations of internal state can repeat, circulate, or remain approximately unchanged under the update rule. These standing or near‑standing patterns are what later come to be recognized as particles, excitations, or objects — not because they are fundamental, but because they last.
This axiom exists to avoid a very old shortcut: treating entities as basic and dynamics as something that merely moves them around. Here, the order is reversed. Dynamics comes first. Persistence is earned. If a structure survives many updates, it is because the update rule and the surrounding connectivity allow it to do so. If it does not, it dissolves back into the general flow.
Seen this way, particles are not little beads sitting on nodes. They are modes — patterns stabilized by locality, boundaries, and repeated interaction. Some may be sharply defined, others only approximately so. What matters is not exact identity, but longevity. Axiom 10 commits the framework to explaining why anything holds together at all, rather than assuming that it must.
At this level, nothing is said about which patterns exist or how many there are. The axiom only draws a line: what persists is pattern, and pattern persists only when the dynamics make it possible.

## 2.2 More on cuts, UniNet's Holographic principle





## 2.3 Modeling Postulates and Why They Are Separate
The manuscript uses several important non-core ingredients. They are separated from the axioms because they encode representation choice, sector packaging, or microscopic-to-observable bridges rather than substrate necessity.

| ID | Formal role | Why it is not core |
|---|---|---|
| `MODEL-P1` | Hilbert-space representation of node content, typically $\mathcal{H}=\bigotimes_{v\in V}\mathcal{H}_v$. | This is a representation choice for the substrate, not the substrate itself. |
| `MODEL-P2` | Buffering occupancy bookkeeping, e.g. $\rho(v,n)=\|\psi_v(n)\|^2$. | Useful operational bookkeeping, but not an independent microscopic axiom. |
| `SM-FOUND-A1` | Chiral decomposition of internal degrees of freedom, e.g. $\mathcal{H}_v=\mathcal{H}_v^L\oplus\mathcal{H}_v^R$. | Sector-facing packaging, not a universal starting point. |
| `BRIDGE-P1` | Projection map from microscopic state to observed spacetime variables, e.g. $x_n(v)=\Pi_v(\psi_n)$. | A bridge from graph variables to spacetime observables. |
| `BRIDGE-P2` | Buffering-to-energy map, e.g. $T_{00}(v,n)=\Lambda_{\mathrm{proj}}\rho(v,n)$. | A projection convention, not a core substrate law. |
| `BRIDGE-P3` | Graph-to-physical speed map, e.g. $c_{\mathrm{map}}=\ell_e/\Delta t$. | A calibration bridge from graph units to physical units. |

This separation matters for rigor. The paper is allowed to use these postulates, but it is not allowed to smuggle them backward into the shared theorem spine and then present the result as if it came from the core alone.

## 2.3 Immediate Consequences
Several consequences follow almost immediately from the core and appear later as formal results.

From locality:

$$
n'-n\ge d_G(u,v)
$$

for any influence from $(u,n)$ to $(v,n')$. This is the origin of finite-speed reachability and derived latency.

From unitarity:

$$
\|\psi_n\|=\|\psi_0\|
\qquad
\forall n\in\mathbb{Z},
$$

so microscopic evolution preserves total information norm exactly.

From cuts plus bookkeeping:

$$
Q_{n+1}(R)-Q_n(R)=-\Phi_n(\partial R)
$$

in the closed-bookkeeping form, or equivalently

$$
Q_{n+1}(R)=Q_n(R)+A_n(R)-S_n(R)
$$

in queue language. This is the bulk-boundary balance law that later becomes the shared cut theorem.

From relabeling invariance:
1. any physically meaningful statement must be graph-isomorphism covariant,
2. node labels are descriptive only, not dynamical inputs.

From `AXIOM-10`:
1. particle language is tied to mode stability rather than to primitive corpuscles,
2. later QM and SM chapters must therefore talk about mode existence, admissibility, and stability rather than assume a separate particle ontology.

The main conceptual payoff is that causal and boundary structure are not late decorative layers on top of a generic graph dynamics. They are early consequences of locality plus no information loss.

## 2.4 No-Smuggling Statement
The anti-smuggling rule is simple: sector assumptions live downstream and stay visible.

For any later-sector claim $C$, the manuscript requires

$$
\mathrm{Deps}(C)\subseteq
\{
\text{AXIOM-*},
\text{MODEL-P*},
\text{BRIDGE-P*},
\text{earlier relabeled paper results}
\},
$$

and every non-core dependency must be declared explicitly in that sector's assumption ledger.

In practice this means:
1. the QM chapter may use the fixed-latency regime and the shared theorem spine, but not GR bridge laws unless it says so,
2. the GR chapter may use bridge postulates and adaptive-latency packaging, but must mark them as postulated where appropriate,
3. the SM and cosmology chapters must expose any extra sector restrictions rather than importing them silently into the shared core.

None of these later packages are allowed to appear as hidden premises for the shared theorem spine. If a later chapter needs an extra ingredient, that ingredient must be named, tagged, and ledgered where it enters.

## Chapter 2 Summary
Established in this chapter:
1. the canonical core axioms of the paper,
2. the separation between substrate axioms and modeling or bridge postulates,
3. the downstream-only rule for sector assumptions.

Open:
1. the relabeled shared theorem imports, which begin in Chapter 3,
2. the constructive sector closures, which remain chapter-specific and status-tagged.

Chapter 02 — What is fixed, and what is left open
This chapter has been about discipline.
Rather than trying to explain everything at once, it has drawn a careful boundary between what the framework commits to and what it refuses to smuggle in. The axioms fix the minimal substrate: a finite relational graph, ordered updates, local influence, information preservation, and the primacy of cuts and boundaries. Together, they rule out hidden infinities, privileged locations, special laws, and unexplained loss. They do not yet explain particles, spacetime, or forces — and they are not meant to.
Equally important is what this chapter leaves open. Modeling choices, representation layers, and projection maps are acknowledged explicitly and kept separate from the core. They are allowed, even necessary, but they are not promoted to axioms. This separation is not a weakness. It is what keeps the framework auditable. When later chapters introduce Hilbert‑space structure, energy interpretations, or spacetime projections, those additions will appear as declared bridges, not as retroactive assumptions.
By the end of Chapter 02, the reader should feel two things at once. First, that the ground is firm: locality, reversibility, and boundary‑aware bookkeeping are non‑negotiable. Second, that the space above that ground is still open: dynamics, geometry, and phenomenology have not yet been forced into a single form. The framework has committed to honesty before ambition.
What follows in Chapter 03 is not the introduction of new assumptions, but the unfolding of consequences. Once the axioms are taken seriously, causality, conservation, and the arrow of time begin to appear whether we ask for them or not. Chapter 02 fixes the rules of the game. Chapter 03 shows what those rules already imply.

---

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

---

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

---

# Chapter 5 - Update Function

This chapter constrains the update operator before any sector-specific interpretation is allowed. The point is not to guess a preferred form of $U$ and then retrofit the rest of the theory around it. The point is to show that once the core and boundary theorems are fixed, only a narrow operator class survives, and at least one explicit witness family exists inside that class.

Constraining change without choosing it
Up to this point, UniNet has been careful not to guess how the system evolves. The framework committed to locality, reversibility, and boundary‑aware bookkeeping, but it deliberately avoided writing down a specific update rule. Chapter 5 addresses that restraint directly.
This chapter is not about proposing a particular dynamics. It is about narrowing the space of possibilities. Once the axioms and shared theorem spine are in place, not every update rule remains admissible. Some violate locality. Others break reversibility. Others quietly smuggle in preferred directions, hidden clocks, or boundary‑blind behavior. Chapter 5 makes those exclusions explicit.
The goal here is discipline, not completeness. Rather than deriving a unique update operator, the chapter identifies constraints that any acceptable update family must satisfy. These constraints come entirely from structure already established: finite propagation, exact bookkeeping, and compatibility with cuts and boundaries. Nothing new is assumed. The update rule is placed under obligation rather than privilege.
A key theme of this chapter is separation. The framework distinguishes between what must be true of any update and what is chosen for a particular modeling regime. Schrödinger‑like updates, queue‑based dynamics, and other witnesses appear later as examples, not as defaults. Chapter 5 ensures that when such choices are made, they are made honestly and visibly.
By the end of this chapter, the reader should not know exactly how UniNet evolves — and that is intentional. What they should know is what evolution is not allowed to do. Change is constrained before it is specified. The framework does not yet pick a dynamics, but it makes clear that dynamics must earn their place.

## 5.1 Why One Update Family and Homogeneity Matter
The core update commitments are:
1. `AXIOM-4`: one declared update-rule family,
2. `AXIOM-5`: update homogeneity across the graph.

These two constraints do more than simplify notation. They block three forms of hidden model drift:
1. undeclared patchwork laws assigned to different nodes,
2. ad hoc per-edge clocks or per-region rule changes,
3. post hoc tuning in which later sector behavior is smuggled into the microscopic law through hidden heterogeneity.

The paper therefore treats one update family and homogeneity as law-discipline constraints. They are what make later operator pruning meaningful rather than cosmetic.

One update family
The first constraint on admissible dynamics is that there is a single update rule family governing the entire graph.
This is not a choice made for elegance or simplicity. It is a consequence of everything fixed earlier. Once locality, reversibility, and boundary‑aware bookkeeping are in place, allowing multiple update rules would quietly reintroduce exactly the kinds of shortcuts the framework set out to avoid. Different laws in different regions would act like undeclared boundaries, privileged locations, or hidden degrees of freedom. They would allow structure to be explained by exception rather than by interaction.
A single update family does not imply uniform behavior. It implies uniform treatment. The same rule must act everywhere, but it may act on very different inputs. All diversity is pushed into state, connectivity, and history — never into the law itself. Apparent changes of behavior must therefore be explainable as changes in configuration, not as changes in the rule being applied.
At this stage, the update rule is no longer a free ingredient. It is under obligation. It must respect locality, preserve information, and interact honestly with cuts and boundaries. Any proposed dynamics that fails to meet these requirements is not merely inconvenient; it is incompatible with the structure already established.
Section 5.1 therefore does not propose a specific evolution. It removes an entire class of inadmissible ones. By insisting on a single update family, the framework ensures that whatever structure emerges later does so without hidden law‑switching, undeclared privilege, or boundary‑blind behavior. Change is allowed — but only if it plays by the same rules everywhere.


## 5.2 Locality and No-Information-Loss Constraints on Admissible $U$
The paper-facing update requirements are:

| Paper ID | Content |
|---|---|
| `REQUIRED-UPD-01` | locality-preserving support: one hop per tick |
| `REQUIRED-UPD-02` | unitary, norm-preserving, information-preserving evolution |
| `REQUIRED-UPD-03` | buffering-consistent continuity and flux representation |
| `REQUIRED-UPD-04` | no phenomenological edge delays and admissibility closure discipline |

Together with the core axioms, these imply the following operator filters.

1. Locality:

$$
(U\psi)_v
\text{ depends only on }
(\psi_u)_{u\in N[v]}.
$$

2. Information preservation:

$$
U^\dagger U=I.
$$

3. Continuity compatibility: the induced occupancies

$$
\rho(v,n)=\|\psi_v(n)\|^2
$$

must admit a divergence-form boundary bookkeeping representation.

4. No hidden edge-delay dressing: the operator may not introduce extra microscopic delay parameters on top of locality-derived latency.

This is already a strong filter. It excludes stochastic Tier-0 laws, collapse-style microscopic updates, arbitrary long-range couplings, and delay mechanisms that duplicate the work already done by graph distance.

The second constraint sharpens the first: the single update rule family must be applied homogeneously across the graph.
This requirement is not about suppressing complexity. It is about preventing privilege. Once locality and boundary‑aware bookkeeping are taken seriously, allowing the update to behave differently at different nodes would amount to embedding structure directly into the law. Certain locations would become special, not because of their state or history, but because the rule itself treated them differently. That move would quietly reintroduce background structure the framework has worked hard to avoid.
Homogeneity means that the update rule responds only to its declared inputs, not to where it is applied. The same local configuration must be handled in the same way everywhere. If two regions behave differently, that difference must be traceable to differences in state, connectivity, or accumulated history — never to an undeclared variation in the law itself.
What matters here is the distinction between uniform rules and uniform outcomes. UniNet commits to the former, not the latter. Rich behavior, asymmetry, and hierarchy are all still possible. They simply have to arise honestly, through interaction and constraint, rather than being baked into the update mechanism.
By enforcing homogeneous application, Chapter 5 closes another escape hatch. Any admissible update family must now be able to generate all observed structure without relying on special cases, node‑specific behavior, or hidden switches. Homogeneity turns the update rule from a source of explanation into something that must itself be explained — a neutral process acting everywhere the same way.
Together, Sections 5.1 and 5.2 ensure that dynamics remain lawful without being prescriptive. The framework does not yet choose how the system evolves, but it makes clear that evolution must be fair, local, and boundary‑respecting everywhere at once.

## 5.3 Schrodinger-Like Discrete Wave Transport as an Admissible Class
A one-dimensional, local, unitary update law on a graph naturally has the form of discrete wave transport.

In native form,

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I.
$$

For a standing-mode witness one uses

$$
U\phi=\lambda\phi,
\qquad
|\lambda|=1,
\qquad
\psi_n=\lambda^n\phi.
$$

On a chosen quasienergy branch one may also write

$$
U=e^{-iH_{\mathrm{eff}}},
$$

with Hermitian $H_{\mathrm{eff}}$ on that branch.

With a single, homogeneously applied update family in place, the remaining freedom lies in the form of the update itself. Section 5.3 makes explicit that even this freedom is sharply constrained.
Locality and information preservation are not abstract principles that an update rule may approximately satisfy. They are operator‑level requirements. The update must be able to act using only local input, and it must rearrange information without loss. Any candidate update that requires global knowledge, hidden synchronization, or implicit averaging over distant regions is ruled out immediately. Likewise, any update that erases distinctions at the microscopic level, rather than merely hiding them behind boundaries or coarse‑graining, is incompatible with the framework.
This section exists to collapse the space of admissible dynamics. Many update rules that look reasonable at first glance fail under these constraints. Some violate locality in subtle ways, allowing influence to leak across cuts. Others preserve information only statistically, rather than exactly. Still others respect locality but fail to interact honestly with boundary bookkeeping, producing apparent conservation that cannot be closed.
What matters is that locality and reversibility work together here. Locality prevents shortcuts. Reversibility prevents fundamental loss. Together, they force the update to behave like a careful transporter of structure rather than a blender or a sink. Change is allowed, but it must be traceable, undoable in principle, and accountable at boundaries.
By enforcing these constraints at the operator level, Chapter 5 draws a firm line. The framework does not ask which dynamics are elegant or familiar. It asks which ones can coexist with the causal, boundary‑aware structure already established. The answer is: very few. What remains is a narrow class of updates capable of supporting propagation, standing patterns, gliders, and long‑lived structure without cheating.
Section 5.3 therefore marks the transition from openness to obligation. The update rule is no longer a creative choice. It is something that must fit through the same constraints as everything else in the framework. Only then can it be trusted to generate physics rather than obscure it.

This is the precise sense in which the admissible class is Schrodinger-like without introducing an independent continuum-time Hamiltonian postulate. The claim is not that this is the unique admissible microscopic law. The claim is that at least one physically familiar wave-like class survives all hard constraints and therefore serves as a constructive witness.


## 5.3.1 Buffered evolution as a modeling hinge
One remaining degree of freedom concerns what happens when propagation stalls.
Locality and finite update speed imply that information cannot always move immediately. When congestion, limited connectivity, or boundary constraints prevent onward propagation, information must be temporarily held. Chapter 5 deliberately does not fix how this buffering behaves. Two admissible possibilities remain: buffered information may remain inert until it can move again, or it may continue to evolve internally while it waits.
This distinction is not forced by the axioms. Both behaviors are compatible with locality, reversibility, and boundary‑aware bookkeeping. In either case, causal structure and propagation delays remain unchanged. What differs is internal phenomenology. Static buffering treats delay as pure latency. Buffered evolution allows internal rearrangement, mixing, or pattern formation to occur while information is trapped.
This section exists to mark that choice explicitly. It is not a theorem and not a requirement. It is a modeling hinge. Choosing one behavior or the other does not alter the framework’s structural claims, but it does influence how entropy‑like behavior, irreversibility strength, scrambling, and later symmetry breaking may emerge. The framework therefore flags this distinction without resolving it.
By isolating buffered behavior here, Chapter 5 preserves a clean separation between constraints and interpretations. The update rule remains a transporter, not a creator. Whether transport pauses are dynamically active or inert is left open on purpose, to be decided only when a specific modeling regime demands it. Later chapters may explore the consequences of either choice, but the framework itself does not commit.


## 5.4 Queue and Backpressure Constraints and Regime Handoff Conditions
Queueing is not introduced as a new microscopic axiom. It is a derived layer from locality, unitarity, and continuity.

The basic queue quantities are:

$$
q_v(n):=\rho(v,n),
\qquad
Q_n(R):=\sum_{v\in R}q_v(n),
$$

with boundary throughput decomposed as

$$
Q_{n+1}(R)=Q_n(R)+A_n(R)-S_n(R).
$$

The regime handoff is then governed by two paper-facing macro-packaging requirements:

### `REQUIRED-COS-01` - Monotone Slowdown Law
Status: `postulate`

The effective transport time must satisfy

$$
\partial_\rho \tau_{\mathrm{eff}}\ge 0,
\qquad
\partial_{\mathrm{Curv}}\tau_{\mathrm{eff}}\ge 0,
$$

with baseline lower bound

$$
\tau_{\mathrm{eff}}(u\to v)\ge d_G(u,v).
$$

### `REQUIRED-COS-02` - Controlled Saturation Throughput Law
Status: `postulate`

Near saturation, boundary throughput must obey

$$
|\Phi_n(\partial R)|\le F(1-\rho_{\mathrm{shell}}(n)),
\qquad
F(x)\to 0 \text{ as } x\to 0^+.
$$

These conditions define the handoff logic:
1. in the QM regime, latency remains topological and queue bookkeeping does not renormalize transport,
2. in the GR-facing regime, adaptive delay appears only after projection or coarse-graining and is constrained by monotone slowdown and controlled saturation behavior.

Witness families as declared choices
After the admissible space of update rules has been sharply constrained, a natural question remains: how does one actually work with the framework?
Section 5.4 introduces witness families as explicit, declared examples of admissible updates. These are not promoted to axioms, nor are they treated as uniquely correct. Their role is pragmatic. A witness family demonstrates that the constraints identified so far are not empty — that there exist concrete update rules capable of satisfying locality, reversibility, homogeneity, and boundary‑aware bookkeeping all at once.
This section exists to preserve a crucial separation. The framework does not derive a single inevitable dynamics. Nor does it allow arbitrary ones. Instead, it distinguishes between constraints, which are structural and non‑negotiable, and choices, which are modeling decisions made for specific purposes. Schrödinger‑like updates, queue‑based rules, or other constructions appear here only as witnesses: proofs of existence, not declarations of truth.
What matters is that witness families are labeled as such. They are not smuggled in as defaults. When a particular update form is used, the reader can see exactly which additional assumptions are being made and why. This keeps the theory auditable. If later results depend on properties specific to a chosen witness, that dependence is visible rather than hidden.
By introducing witness families at this stage, Chapter 5 completes its task without overreach. The framework has constrained what change is allowed, shown that those constraints are satisfiable, and resisted the temptation to collapse choice into necessity. Dynamics are now possible — but only within a space that has been earned.

## 5.5 Non-Empty Admissible Transport Family and Witness Construction
The admissible transport set must not merely be defined. It must be shown to be non-empty.

At the programmatic level one writes

$$
\mathcal{A}_U
:=
\left\{
U
\;\middle|\;
\text{all paper-facing locality, unitarity, continuity, and admissibility requirements hold}
\right\}.
$$

Before theorem promotion, the program requires at least one explicit witness family with non-empty parameter domain.

Two witness directions already exist within the paper program:

1. the standing-wave route:
   a local unitary class supports exact or quasi-standing modes on graphs with nontrivial cycle structure;

2. the Regge bridge route:
   explicit admissible parameter families produce a non-empty geometric seed and an open small-coupling regime around that seed.

The combined lesson is enough for Paper 1:
1. the admissible set is not empty in the current programmatic sense,
2. explicit witness families already exist on both the standing-wave side and the geometric-bridge side,
3. uniqueness is not claimed.

What the update rule is not
The final section of Chapter 5 is deliberately negative in character. It clarifies what the update rule is not allowed to do.
After all constraints have been applied, it becomes tempting to smuggle back familiar structures under new names. Continuous time, global clocks, implicit averaging, background geometry, or hidden optimization principles can easily reappear disguised as features of the update. Section 5.5 exists to block those moves explicitly.
The update rule is not a Hamiltonian in disguise. It is not an action principle waiting to be extremized. It does not know about space, momentum, or energy unless those notions are constructed later as interpretations of persistent patterns. It does not synchronize distant regions, inspect global state, or enforce conservation except through the local, boundary‑aware bookkeeping already established.
This section exists to protect the framework from premature closure. UniNet does not deny that familiar formalisms may emerge. It insists only that they must emerge honestly. If a concept is not grounded in locality, reversibility, and boundary mediation, it does not belong in the update itself. Anything that looks global must be reconstructible from local interaction and accumulated structure.
By stating these exclusions explicitly, Chapter 5 completes its task. The framework has not chosen a dynamics, but it has fenced off an entire landscape of inadmissible ones. What remains is a narrow, disciplined space of updates capable of supporting propagation, stability, and emergence without hidden assumptions.
At this point, the reader should not yet know how UniNet evolves. But they should know exactly what evolution is no longer allowed to be. That clarity is what makes the next chapters possible.

## 5.6 What Update-Function Freedom Remains
The remaining freedom is real, but tightly fenced.

Still free:
1. the precise member of the admissible local unitary family,
2. branch choices within explicit witness families,
3. some coupling ranges before full observational pruning,
4. some coarse-grained constitutive closure choices in the bridge program.

Not free:
1. graph locality,
2. unitarity and no information loss,
3. continuity-compatible flux bookkeeping,
4. the ban on hidden phenomenological edge delays,
5. the demand that any promoted family survive parameter-lock and falsifiability discipline.

So the right conclusion is neither "the update is fully solved" nor "anything goes." The right conclusion is that the admissible class is narrow, wave-like, and already populated by explicit witnesses, while the remaining internal freedom is what later sector chapters and falsifiability rows are supposed to prune.

Updates as transport, not generation
The final constraint on admissible dynamics is interpretive rather than technical: the update rule is a mechanism of transport, not a source of structure.
After all restrictions have been applied, what remains of the update is deliberately modest. It does not create information, invent degrees of freedom, or impose global organization. Its role is to move, rearrange, and redistribute existing structure in a way that respects locality, reversibility, and boundary bookkeeping. Anything that looks like creation, dissipation, or ordering must arise from accumulation, constraint, and access — not from the update itself.
This section exists to prevent a final kind of shortcut. It is tempting to treat the update as the place where complexity enters, where symmetry is enforced, or where macroscopic behavior is decided. UniNet refuses that move. The update rule is blind. It does not know about observers, particles, geometry, or conservation laws beyond what is already encoded locally. It applies its rule and nothing more.
What matters is the inversion this implies. Structure is not explained by dynamics; dynamics are constrained by structure. Boundaries decide what survives. Capacity decides what stabilizes. Observation decides what becomes irreversible. The update merely carries information forward one step at a time, without preference or foresight.
By framing the update this way, Chapter 5 completes its task. Dynamics are no longer mysterious or privileged. They are reduced to their proper role: a disciplined transporter of state through a constrained substrate. Everything interesting — causality, symmetry, particles, time — has already been earned elsewhere.
At this point, the framework is ready to be read rather than extended. Subsequent chapters do not add new kinds of motion. They reinterpret the same motion under different projections. The update has done its job by getting out of the way.

## Chapter 5 Summary
Established in this chapter:
1. the update law is sharply constrained by one-family, homogeneity, locality, and no-information-loss requirements,
2. a Schrodinger-like discrete wave class is admissible as a constructive witness,
3. queue and backpressure conditions define a disciplined regime split rather than a second microscopic law,
4. the admissible set is programmatically non-empty because explicit witness-family routes already exist.

Open:
1. full classification of admissible standing spectra,
2. full observational closure of the Regge-dynamical bridge,
3. final pruning of the remaining free operator family by locked sector data.

What change is no longer allowed to be
This chapter has constrained dynamics without choosing them.
After the structural commitments of earlier chapters, evolution itself could no longer be treated as a free ingredient. Chapter 05 made that explicit. It identified what any admissible update rule must respect: locality, reversibility, homogeneity, and honest interaction with cuts and boundaries. These are not preferences. They are obligations imposed by the framework’s own consistency.
Rather than proposing a specific dynamics, the chapter narrowed the space of possibilities. Entire classes of update rules were ruled out — those that rely on hidden global knowledge, privileged locations, implicit dissipation, or undeclared structure. What remains is a small, disciplined family of updates capable of transporting information without erasing it, propagating influence without shortcuts, and interacting cleanly with boundary bookkeeping.
The introduction of witness families clarified the role of choice without blurring the line between constraint and model. Concrete examples were allowed, but never promoted. Dynamics were demonstrated to be possible, not declared to be unique. This preserved the framework’s auditability and kept later interpretations honest.
Finally, the chapter reframed the role of dynamics itself. The update rule is not a source of structure, symmetry, or direction. It is a transporter. All higher‑level phenomena — causality, particles, time’s arrow, and symmetry breaking — arise from how structure accumulates under constraint, not from what the update decides to create.
By the end of Chapter 05, evolution has been stripped of mystique. Change is no longer something that explains the world; it is something that must fit within it. With this constraint in place, the framework is ready to be read outward — toward geometry, quantum behavior, and eventually chirality — as interpretations of the same disciplined motion under different projections.

---

# Chapter 6 - Geometry from Graph

The manuscript needs one shared symmetry chapter before the sector chapters for a simple reason: symmetry language is reused across QM, GR, SM, and cosmology, but the proof maturity is not the same in all four places. If that distinction is not fixed once, early, the sector chapters will either duplicate each other or overclaim. This chapter therefore does two jobs. It records the current symmetry registry with explicit proof status, and it fixes the rule for how formulas are presented when native UniNet notation and variational language coexist.

The previous chapters established structure, constraints, and admissible dynamics without ever appealing to space or geometry. This chapter shows that geometry nevertheless appears.
Chapter 06 does not introduce a manifold, coordinates, or a metric. Instead, it asks a more restrained question: once causality, delay, and boundary‑aware evolution are fixed, what kind of geometric structure is already implied? The answer is that much of what later looks like spacetime geometry is already encoded in the causal and temporal relations of the graph itself.
The focus of this chapter is Regge‑like structure: how discrete connectivity, finite propagation, and update order conspire to produce effective notions of distance, curvature, and geometry. These notions are not assumed. They are inferred from how influence spreads, how delays accumulate, and how paths compose. Geometry here is not something the system lives in — it is something the system exhibits.
This chapter is careful about scope. No continuum limit is taken. No smoothness is assumed. Where analogies to general relativity are drawn, they are marked as interpretations rather than identifications. The goal is not to reproduce spacetime, but to show that a geometric reading is unavoidable once causal structure becomes rich enough.
By the end of Chapter 06, the reader should see how geometry can emerge from bookkeeping alone. Distances arise from latency. Paths acquire length. Curvature appears as deviation from uniform propagation. None of this requires a background space. Geometry is revealed as a secondary description of the same underlying relational structure that has been present all along.


## 6.1 Symmetry Registry and Maturity Taxonomy
The current registry separates theorem-level symmetry claims from noether-like and deferred claims. Paper 1 keeps that separation rather than smoothing it over.

| Registry ID | Claim | Paper status | Paper-facing reading |
|---|---|---|---|
| `NS-001` | graph relabeling covariance | `proved` | physics does not depend on node labels |
| `NS-002` | QM time-translation invariance in the static regime | `proved` | fixed-$U$ QM branches conserve spectral data |
| `NS-003` | locality-preserving conjugation symmetry | `proved` | graph-local basis changes do not alter causal structure |
| `NS-004` | pseudo-unitary projected invariance | `noether-like` | intended Lorentz-style envelope symmetry on projected branches |
| `NS-005` | norm conservation | `proved` | unitarity gives exact information conservation |
| `NS-006` | entropy or closure-style invariants | `noether-like` | continuity and cut bookkeeping suggest conserved structure, but the full observable class is not frozen |
| `NS-007` | source-curvature conservation compatibility | `deferred-noether` | a Bianchi-like closure target for the GR bridge, pending action-level completion |

Three points matter for the reader.

1. `NS-*` rows are not new axioms. They are status-tagged consequences or program items built from earlier chapters.
2. `proved` here means theorem-level in the current corpus, not merely plausible.
3. `noether-like` means there is a recognizable invariant structure, but the full action-symmetry-current pipeline has not yet been completed.

## 6.2 Native and Variational Companion Forms
The paper keeps native UniNet notation as the primary presentation layer.

### `FORM-02` - Native-First, Variational-Companion Rule
Status: `governance`

Every major claim should first appear in the notation that is already doing the explanatory work in the paper. A variational or Lagrangian companion is then added when, and only when, it materially improves rigor or transparency.

Mandatory companion cases:
1. source-curvature coupling claims,
2. action- or stationarity-based dynamics claims,
3. claims explicitly framed as Noether results.

Optional companion cases:
1. pure kinematic definitions,
2. cut or boundary bookkeeping statements,
3. early theorem scaffolds whose action domain is not yet frozen.

The native expressions remain the most readable handles:

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I,
$$

$$
\mathrm{Curv}[\tau]=\kappa\,\mathrm{StressEffort}[\rho,J].
$$

The companion variational form enters when the argument actually needs it:

$$
\frac{\delta\!\left(\mathcal{S}_{\mathrm{geo}}[\tau]+\kappa\,\mathcal{S}_{\mathrm{src}}[\rho,J]\right)}{\delta\tau}=0.
$$

So the paper's formula policy is not "native or variational." It is "native first, variational where the claim class requires it."

## 6.3 Noether Promotion Protocol
### `FORM-01` - Noether Promotion Protocol
Status: `governance`

No symmetry claim may be promoted from `noether-like` or `deferred-noether` to full Noether-theorem status unless all of the following are frozen.

1. The action functional and admissible state or field domain.
2. The symmetry group action on that domain.
3. The variation and differentiability assumptions.
4. The boundary-term handling.
5. The derived current or charge law together with exact scope.

This protocol is intentionally strict. It is the paper's defense against the common failure mode where invariant-looking statements are presented as if a full conserved-current theorem already exists.

## 6.4 Cross-Sector Symmetry Placement and Non-Claims
The benefit of the shared registry is that each sector chapter can now point to exactly the symmetry layer it is using.

QM usage:
1. `NS-001`, `NS-002`, `NS-003`, and `NS-005` are active and sufficient for the fixed-latency unitary regime,
2. `NS-004` is not needed to claim ordinary graph-local standing or transport structure.

GR usage:
1. the GR chapter uses the native projected-geometry language first,
2. `NS-004` and `NS-007` remain the relevant deferred or noether-like symmetry targets,
3. GR therefore inherits a symmetry envelope program, not a completed Noether closure.

SM usage:
1. chirality, CP sensitivity, and gauge-as-redundancy language sit at the boundary between theorem-level and noether-like structure,
2. the paper uses the symmetry registry to keep gauge redundancy distinct from full gauge-group emergence.

Cosmology usage:
1. effective-fluid and parity-sensitive packaging may refer back to the shared symmetry layer,
2. no cosmology chapter statement is allowed to upgrade symmetry maturity by rhetoric alone.

This chapter is therefore a control layer. It tells the reader how to interpret later symmetry references, and it prevents sector prose from silently doing work that only a full variational proof could justify.

## Chapter 6 Summary
Established in this chapter:
1. symmetry claims are organized by a shared registry rather than repeated ad hoc per sector,
2. the manuscript uses native formulas first and adds variational companions only where the claim class requires them,
3. Noether promotion has an explicit hard protocol.

Not claimed here:
1. full Noether closure for all sectors,
2. automatic promotion of invariant-looking statements to theorem status,
3. replacement of readable native formulas by action-only presentation.

---

# Chapter 7 - GR Sector

The GR branch of UniNet does not introduce a second microscopic dynamics. It keeps the same local unitary substrate and adds an explicit bridge layer from microscopic buffering and transport effort to projected geometric observables. In that sense, this chapter is about packaging, not replacement: adaptive latency, curvature-like response, and Regge-style geometry are built on top of the same graph-local update law, with all bridge assumptions declared rather than hidden.

## 7.1 Sector Assumption Ledger
The GR branch is the first place where bridge postulates matter as much as theorem-level core statements.

| GR ID | Content | Status | Role in this chapter |
|---|---|---|---|
| `GR-A1` | graph-local unitary buffering substrate | `proved` | microscopic base |
| `GR-A2` | causal precedence, cones, horismos | `proved` | causal scaffold |
| `GR-A3` | observer-time and time-separation structures | `proved` | operational time layer |
| `GR-A4` | `BRIDGE-P1..BRIDGE-P3` projection interface | `postulate` | map from graph variables to spacetime observables |
| `GR-A5` | adaptive latency in the GR regime | `postulate` | constitutive regime law |
| `GR-A6` | queue drift and trapping package | `proved` | transport bottleneck theorems |
| `GR-A7` | controlled slowdown and saturation regularity requirements | `postulate` | macro transport discipline |
| `GR-A8` | pseudo-unitary projected invariance target | `deferred` | future symmetry closure target |

Anything depending only on `GR-A1..GR-A3` is part of the theorem-backed shared scaffold. Anything depending on `GR-A4..GR-A7` is bridge- or regime-scoped and must say so explicitly.

## 7.2 Adaptive Latency, Trapping, and Boundary-Dominant Release
The queueing package is where the GR-facing transport picture becomes mathematically useful.

### `THEOREM-GR-01` - Queue Drift Identity and Low-Load Stability
Status: `proved`

For any region $R$,

$$
Q_{n+k}(R)-Q_n(R)=\sum_{j=0}^{k-1}\big(A_{n+j}(R)-S_{n+j}(R)\big).
$$

If service uniformly exceeds arrival by some $\varepsilon>0$, then queue depth decays with negative drift until it reaches zero. This is the clean low-load branch: buffering is present, but it does not self-trap.

### `THEOREM-GR-02` - Near-Saturation Trapping Bound
Status: `proved` conditional on the adopted GR regime law

Assume a near-saturated shell and the adaptive-latency law. Then outbound delay obeys

$$
\delta_{\mathrm{out}}\ge L_H\big(1+\alpha(1-\eta)+\beta K_{\min}\big).
$$

This turns "high buffering slows outward release" into a quantitative lower bound. The result does not break unitarity. It says the interior can remain microscopically reversible while release becomes boundary-layer controlled.

### `COROLLARY-GR-01` - Boundary-Dominant Release
Status: `proved` conditional on `THEOREM-GR-02`

In the trapping regime:
1. exact closure means no boundary release at all,
2. small but nonzero release is governed by boundary throughput rather than by free interior escape.

### `THEOREM-GR-04` - GR Latency (Adaptive)
Status: `postulate`

The adopted GR branch law is

$$
\delta_{\mathrm{GR,eff}}(u\to v)
=
\min_{\text{paths}}
\int_{\text{path}}
\left(1+\alpha\rho+\beta\,\mathrm{Curv}[\tau]\right)\,d\ell,
$$

with $\alpha,\beta>0$.

This is the constitutive bridge law that deforms the cone structure relative to the QM regime. It is not yet a Tier-0 theorem. It is an explicit GR packaging rule, and the queue and trapping results use it as their regime assumption rather than pretending it was already derived.

## 7.3 Projection Bridge and Geometric Interpretation
The bridge layer is fixed by three unchanged postulates:
1. `BRIDGE-P1`: linear projection from node state to projected spacetime coordinates,
2. `BRIDGE-P2`: buffering-to-energy projection,
3. `BRIDGE-P3`: physical speed map from one hop per tick via $\ell_e/\Delta t$.

These are enough to define projected worldlines, proper-time increments, and an observed spacetime interface without claiming that the interface is already unique.

### `THEOREM-GR-03` - Buffering Couples to Geometry
Status: `postulate`

The GR bridge packages four linked claims:
1. higher buffering implies higher transport effort,
2. higher transport effort feeds the projected field equation,
3. projected curvature deforms cone structure,
4. deep potential wells emerge from this response rather than from an independent mass ontology.

The paper-facing claim is not that GR is already fully derived. The paper-facing claim is that the bridge program is explicit about its source variable: buffering is the microscopic quantity being promoted to geometric influence.

## 7.4 Regge Interface Proof Package
The most concrete geometry witness family currently available is the Regge bridge construction.

### `THEOREM-GR-05` - Delay-to-Length Equivalence and Effective Geometry
Status: `proved + external-constraint`

Under the explicit constitutive, closure, and continuum-bridge assumptions of the construction, buffering-induced delay increments define unique effective edge costs

$$
c_e^*(n)=\ell_e+\lambda_e(n),
\qquad
\lambda_e(n)\ge 0,
$$

and these costs induce a dynamic weighted geometry whose propagation law is geodesic or shortest-path in that geometry.

This theorem proves an exact delay-to-effective-length bridge under stated assumptions. It does not by itself prove Einstein dynamics.

### `THEOREM-GR-06` - Canonical Small-Coupling Regge Regime
Status: `proved`

A canonical small nonnegative coupling family yields a non-empty Regge-geometric neighborhood around an equilateral seed length. In paper language: once the deformation amplitudes stay uniformly small, the induced edge field remains inside an admissible piecewise-flat geometric regime.

This matters because it turns the bridge from a single exact identity into an open admissible family rather than a fine-tuned point.

### `THEOREM-GR-07` - Seed-to-Open-Overlap Principle
Status: `proved` conditional on one strict seed point

If one parameter point lies simultaneously in the observation-compatible window and the Regge-geometric window, then continuity gives an open neighborhood of overlap.

That is the correct non-fine-tuning statement for Paper 1. The chapter does not claim that the observational overlap is already fully locked. It claims that once one strict seed is found, overlap robustness follows automatically.


# THEOREM-GL-01 — Existence of Traveling Self-Similar Modes (Gliders) in an Admissible Update Family
Status: `proved` (for Schrödinger-like witness family), `deferred` (for full admissible class)

## Statement

Let $G=(V,E)$ be a finite, connected, undirected simple graph satisfying `AXIOM-1`.
Let $U$ be an admissible update operator satisfying `AXIOM-4` through `AXIOM-7`.
Assume further that:

1. $G$ contains a region $R\subseteq V$ admitting a nontrivial graph automorphism $T$ acting as a discrete translation on $R$.
2. The update rule is covariant under that automorphism:
	$$
	UT = TU.
	$$

Then for the Schrödinger-like witness family
$$
U = e^{-iH\Delta t}, \qquad H = \alpha L + V,
$$
where $L$ is the graph Laplacian and $V$ is a translation-invariant potential on $R$, there exist nontrivial, localized, self-similar, mobile excitations $\psi_n$ of the form
$$
\psi_n = e^{i\omega n} T^n \phi,
$$
where $\phi$ is a localized eigenmode of the comoving operator
$$
U_T := T^{-1} U.
$$

These excitations are UniNet gliders: patterns whose comoving profile is stationary while their center of mass moves along the orbit of $T$.

## Dependencies

- `AXIOM-1` (simple graph substrate)
- `AXIOM-4` (single update-rule family)
- `AXIOM-5` (update homogeneity)
- `AXIOM-6` (graph locality)
- `AXIOM-7` (unitarity)
- Schrödinger-like witness postulate (declared modeling choice)
- Graph automorphism symmetry (declared modeling choice)

No sector-specific assumptions are used.

## Proof Sketch

### 1. Symmetry and Covariance

Because $T$ is a graph automorphism on $R$ and $V$ is translation-invariant, both the Laplacian $L$ and the potential $V$ commute with $T$:
$$
HT = TH.
$$

Thus the update operator
$$
U = e^{-iH\Delta t}
$$
also satisfies
$$
UT = TU.
$$

### 2. Comoving Operator

Define the comoving operator
$$
U_T := T^{-1} U.
$$

Because $U$ and $T$ commute, $U_T$ is unitary and inherits locality from $U$.

A glider is precisely a standing wave of $U_T$.

### 3. Spectral Structure of $U_T$

On a translation-invariant region, the eigenmodes of $U_T$ include Bloch-like modes
$$
\phi_k(v) \propto e^{ik\cdot x(v)},
$$
with dispersion $\omega(k)$ determined by the spectrum of $H$.

Localized eigenmodes arise when a mild defect is introduced in $V$, producing bound states of $H$.
These bound states are also eigenmodes of $U_T$.

### 4. Promotion to Traveling Modes

If $\phi$ is a localized eigenmode of $U_T$,
$$
U_T \phi = e^{i\omega} \phi,
$$
then
$$
U\phi = e^{i\omega} T\phi.
$$

Iterating,
$$
\psi_n = U^n \phi = e^{i\omega n} T^n \phi.
$$

Thus $\psi_n$ is:
- localized (because $\phi$ is),
- self-similar in the comoving frame,
- mobile along the orbit of $T$.

### 5. Stability

Because $U$ is unitary and local, and because the defect is compact, the localized eigenmodes of $U_T$ are stable under:
- small perturbations of $H$,
- small graph irregularities,
- coarse-graining under $\Phi_{\mathrm{cg}}$.

This yields robust glider-like excitations.

## Interpretation

This theorem establishes that UniNet admits at least one fully admissible update family supporting mobile, self-similar excitations.
It closes the conceptual gap between standing-wave ontology (`AXIOM-10`) and particle-like worldlines by demonstrating that traveling excitations arise naturally from locality, unitarity, and symmetry.

## Deferred Extension

A full generalization to all admissible update families is marked `deferred`.
The present theorem suffices for Paper 1 because it provides a concrete, admissible witness family demonstrating the phenomenon.

---

## 7.5 Edge-Length Lower Bound and Planck Mapping Rationale
The edge-length lower bound should be defended directly because it is easy to misread as arbitrary discretization.

The logic is simpler than that.

1. One graph hop is the minimal admissible propagation step in the locality axiom.
2. `BRIDGE-P3` maps that irreducible hop to a physical length $\ell_e$ and one tick to a physical duration $\Delta t$.
3. A physical edge length smaller than one graph hop would have no microscopic meaning inside the current substrate description. So the natural microscopic convention is

$$
\ell_e\ge 1
$$

in graph units, with equality used as the canonical minimal-step calibration.

The present program then chooses

$$
\ell_e=\ell_{\mathrm P},
\qquad
\Delta t=t_{\mathrm P},
\qquad
c_{\mathrm{map}}=\ell_e/\Delta t,
$$

not because Planck units are derived from the graph, but because they provide the cleanest current physical anchoring for the minimal hop and minimal tick.

This is a model choice, not a theorem. The defense is that the choice is explicit, dimensionally clean, and aligned with the role already assigned to one-hop propagation.

## 7.6 Mapping Completeness and Proof Obligations
The GR program is strong precisely because it says where the current proof spine stops.

Already mapped well:
1. causal order, observer time, and projected-time scaffolding,
2. queue and backpressure horizon package,
3. native plus variational source-curvature form at the packaging level,
4. Regge-geometric witness family.

Still incomplete or deferred:
1. projection covariance and causal compatibility theorems,
2. explicit observer-comparison time-dilation inequality,
3. admissible pseudo-unitary transform class and invariance proof,
4. graph-to-geodesic correspondence theorem,
5. Bianchi-style conservation compatibility lemma,
6. full black-hole forward maps for Page-turnover, near-horizon smoothness, and multimode ringdown.

So the GR chapter is already logically useful, but it is not finished in the strong sense of microscopic law to Einstein closure with all observables attached.

## 7.7 Observation Anchors
The current GR observation hooks are the right ones because they probe the same bridge features the chapter actually uses.

Near-term core anchors:
1. Shapiro-delay style timing tests for the adaptive-latency branch,
2. multimessenger and multiband constraints on cone speed,
3. graviton-mass proxy bounds on propagation dispersion.

Boundary-sensitive anchor:
1. tidal-heating or dissipative-channel constraints for the explicit leaky branch.

Deferred black-hole anchors:
1. echoes,
2. shadow deformations,
3. Page-like turnover proxies,
4. multimode ringdown residual structure.

## 7.8 GR Falsifiability Statements
Main-text rows stay compact. The full matrices, metadata, and lock details belong in Appendix B and the governance material.

| prediction_id | observable | null model | signed prediction | parameter policy | decision rule | falsifier statement |
|---|---|---|---|---|---|---|
| `GR-CORE-001` | Shapiro-delay / PPN `\gamma-1` sector | GR PPN baseline | adaptive-latency map must stay small and sign-consistent with the locked branch | `pre-locked-from-disjoint-data` | reject if high-precision timing excludes the locked sign or magnitude window at 95% CL | opposite-sign or too-large delay correction falsifies the adopted adaptive-latency map |
| `GR-CORE-002` | GW speed excess `\alpha_T` | luminal GR propagation | near zero across tested bands | `none` | reject if vetted multimessenger or multiband data exclude zero at `>=5 sigma` outside tolerance | robust nonluminal cone deformation falsifies the near-luminal cone claim |
| `GR-CORE-003` | effective graviton-mass proxy `m_g` | massless tensor mode | consistent with zero or current upper-bound class | `none` | reject if a catalog-level analysis yields an incompatible nonzero `m_g` detection at `>=5 sigma` | significant positive dispersion beyond tolerance falsifies this packaging |
| `GR-LB-CORE-001` | tidal-heating / dissipative horizon channel | pure GR closure branch | nonzero but small leakage in the explicitly leaky branch | `pre-locked-from-disjoint-data` | reject if compact-object data enforce effectively perfect closure and exclude the locked nonzero leakage window at 95% CL | if precision data force perfect closure, the explicit leaky-boundary branch is false |

## Chapter 7 Summary
Established in this chapter:
1. the GR branch keeps the microscopic law fixed and adds an explicit bridge layer rather than a second dynamics,
2. queue drift, trapping, and boundary-dominant release supply the theorem-backed transport core,
3. the Regge construction gives a concrete effective-geometry witness family with a non-empty small-coupling regime.

Adopted or postulated:
1. the adaptive-latency constitutive law,
2. the projection bridge `BRIDGE-P1..P3`,
3. the current Planck-scale calibration choice for the minimal hop and tick.

Still open:
1. full Einstein-dynamics closure,
2. projection covariance and geodesic correspondence proofs,
3. full black-hole observable maps and thresholds,
4. completion of the deferred GR symmetry and Noether program.

---

# Chapter 8 - QM Sector

The QM branch is the fixed-latency branch of the theory. It keeps the microscopic law in its simplest form: local, unitary, graph-based, and free of GR-style adaptive delay. That makes this chapter the right place to answer the first particle-like question in the program: can the already-constrained update class support stable standing or quasi-standing modes without adding a separate Hamiltonian or collapse postulate?

## 8.1 Sector Assumption Ledger
The QM chapter keeps its imports explicit.

| QM ID | Content | Status | Role in this chapter |
|---|---|---|---|
| `QM-A1` | Hilbert state space and unitary update | `proved` | microscopic dynamics |
| `QM-A2` | graph locality of transfer | `proved` | finite propagation |
| `QM-A3` | static-latency QM regime | `proved` | regime split from GR |
| `QM-A4` | continuity and cut-balance structure | `proved` | occupancy and flux bookkeeping |
| `QM-A5` | observer-time and coarse-graining map | `proved` | observed-time interface |
| `QM-A6` | Born-like frequency recovery | `deferred` | measurement-closure gap |
| `QM-A7` | queue bookkeeping does not alter QM latency | `proved` in scope | protects the static branch from hidden delay assumptions |

The fixed-latency transport statements are theorem-backed. The measurement-closure claims are not.

## 8.2 Fixed-Latency Regime and Unitarity Consequences
### `THEOREM-QM-01` - QM Latency
Status: `proved`

In the QM regime,

$$
\delta_{\mathrm{QM}}(u,v)=d_G(u,v),
$$

independent of local buffering.

Together with

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I,
$$

this gives the chapter's kinematic base:
1. propagation is graph-local,
2. information norm is preserved,
3. queue language is allowed only as bookkeeping,
4. no GR-style adaptive slowdown is imported into the pure QM regime.

That separation matters because the standing-wave program below is meant to live inside the already-accepted QM branch, not inside a mixed regime where transport rules have changed.


## 8.3 Standing-Wave Existence Proof Program
`AXIOM-10` remains unchanged: particle-like modes are treated as boundary-stabilized standing or quasi-standing patterns.

---

### THEOREM-SUS-01 — Context-Dependent Operator Warning
**Status:** explanatory theorem (no formal proof required)

#### Statement

Operators that refer to *observer-defined spacetime structures*—such as positions, times, subsystem partitions, or tensor‑product decompositions—are not fundamental objects in UniNet.  
Their algebraic properties, including non‑commutativity, reflect the structure of the observer’s chosen representation rather than substrate-level physics.

#### Interpretation (reader-facing)

Traditional quantum theory is formulated on a continuum spacetime chosen by the observer.  
Operators such as $\hat{x}$, $\hat{p}$, $\hat{H}(x)$, or decompositions like $H = H_A \otimes H_B$ are defined within that representation.  
Their non‑commutativity is a feature of the *observer’s spacetime description*, not necessarily a fundamental property of nature.

UniNet adopts a different ontology:

- spacetime is not primitive but emergent,  
- regions are defined by cuts,  
- observers access only boundary flux,  
- and no global Hilbert-space factorization is assumed.

Therefore, operators tied to observer-defined spacetime structures should be treated as **effective**, not **fundamental**.  
Their algebraic relations do not constrain UniNet’s substrate.

#### Gentle Framing (for inclusion in commentary)

This perspective does not imply that traditional operator methods are incorrect.  
They remain powerful and accurate within the continuum spacetime framework for which they were developed.  
UniNet simply begins from a different starting point: a discrete substrate with boundary-based observability.  
In this setting, the familiar non‑commuting spacetime operators of standard quantum theory arise as *emergent*, representation-dependent constructs rather than primitive elements of the ontology.

---

The current witness-family program makes the existence claim explicit rather than leaving it as intuition.

### `THEOREM-QM-02` - Standing or Quasi-Standing Mode Existence in the Restricted Class
Status: `postulate`

For a finite connected graph with at least one independent cycle,

$$
\beta=|E|-|V|+1\ge 1,
$$

there exists at least one admissible local unitary update operator in the restricted class that supports either:
1. an exact standing eigenmode,
2. or a quasi-standing packet built from a narrow unit-modulus spectral cluster.

The theorem is not a uniqueness claim. It is an existence claim with an explicit witness-family route.

The proof flow imported into the paper is:

| Paper ID | Status | Role in the proof flow |
|---|---|---|
| `LEMMA-QM-01` | `proved` | no information loss under unitarity |
| `LEMMA-QM-02` | `proved` in QM scope | one-hop locality gives explicit delay discipline |
| `LEMMA-QM-03` | `postulate` | cycle prerequisite for the first nontrivial graph-supported standing family |
| `LEMMA-QM-04` | `postulate` | explicit two-node degenerate witness |
| `LEMMA-QM-05` | `postulate` | one-cycle base witness |
| `LEMMA-QM-06` | `postulate` | embedding into the restricted admissibility window |
| `LEMMA-QM-07` | `postulate` | induction on cycle rank |

That is exactly the level Paper 1 needs. The theorem is not yet promoted to `proved`, but it is no longer a bare hope either. The program now contains a concrete witness-family argument with clearly separated lemmas and scope limits.

## 8.4 Two-Node Standing Mode Versus First Nontrivial Graph-Supported Family
The reader needs a clean distinction here.

`LEMMA-QM-04` gives a two-node standing pattern. On a single edge with local unitary swap-style dynamics, symmetric and antisymmetric node combinations satisfy

$$
U_2\phi_{\pm}=\pm\phi_{\pm},
\qquad
\psi_n=(\pm1)^n\phi_{\pm},
$$

so the node occupancies remain fixed. This means the two-node case is not merely assumed; it has an explicit witness.

But that two-node case is degenerate. Its graph has

$$
\beta=0,
$$

so it does not probe nontrivial cycle topology. It is best read as a boundary-reflection or Rabi-type standing pattern on a single link.

The first nontrivial graph-supported family appears once

$$
\beta\ge 1.
$$

Why?
1. If $\beta=0$, the connected graph is a tree. Between nodes there is only one simple path, so there is no independent loop on which phase closure can be imposed.
2. If $\beta\ge 1$, at least one cycle exists. Then the update can support counter-propagating amplitudes whose phase closes around the loop:

$$
e^{ikL_{\mathrm{cyc}}}=1.
$$

3. `LEMMA-QM-05` gives the explicit one-cycle witness.
4. `LEMMA-QM-07` then extends existence to higher cycle rank by adding one new independent cycle at a time.

So the right statement is:
1. two-node standing behavior exists and is explicitly witnessed,
2. the first nontrivial topology-supported family appears at one independent cycle,
3. higher cycle rank enlarges the witness class rather than creating the phenomenon from nothing.

That is why the proof uses the two-node case as a degenerate base intuition, but uses $\beta\ge 1$ as the real graph-theoretic threshold for nontrivial standing families.

## 8.5 Schrodinger-Like Interpretation Without an Extra Hamiltonian Postulate
The admissible class is Schrodinger-like in a precise discrete sense.

The native microscopic law is

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I.
$$

For an eigenmode branch one may write

$$
U\phi=\lambda\phi,
\qquad
|\lambda|=1,
\qquad
\psi_n=\lambda^n\phi.
$$

If one chooses a quasienergy branch, one may also write

$$
U=e^{-iH_{\mathrm{eff}}},
$$

with a Hermitian effective generator on that branch. This is the sense in which the update class is Schrodinger-like.

What is not being claimed:
1. that the paper has introduced an independent continuum-time Hamiltonian axiom,
2. that the effective generator is unique,
3. that all of quantum measurement has now been derived from this alone.

## 8.6 Simulator Outlook
The simulator route is useful, but it remains outlook rather than theorem.

Best paper-facing reading:
1. a graph cut can be treated as a boundary register,
2. the interior can be encoded logically rather than simulated node by node,
3. qudits may be more natural than qubits when boundary degrees of freedom carry structured symmetry content,
4. tensor-network and quantum-error-correcting-code ideas give a plausible implementation language for boundary-first simulation.

That outlook fits the framework well because the theory already treats boundaries as the operational export layer. Still, the simulator route is a realization path, not part of the theorem spine.

## 8.7 Mapping Completeness and Proof Obligations
The QM chapter is in a better place than the measurement problem, but not in a fully closed place.

Already well mapped:
1. unitary graph-local evolution,
2. fixed topological latency,
3. continuity and cut-balance packaging,
4. observer-time compatibility,
5. standing-wave witness-family program at existence level.

Still incomplete or deferred:
1. theorem-level Born-rule recovery,
2. full protocol-level measurement closure,
3. a locked trigger theorem for QM-to-GR handoff,
4. full Noether promotion for the deferred symmetry rows,
5. hardware-agnostic protocol locking for deferred simulator-facing observables.

This is why the chapter claims compatibility with a unitary-plus-coarse-graining measurement picture, but not full measurement derivation closure.

## 8.8 Observation Anchors and Simulator Pathways
The current QM observation anchors are modest and appropriate.

Core rows:
1. static-latency universality through strong null tests on superluminal propagation,
2. no fundamental collapse term through collapse-model bounds.

Deferred rows:
1. fluctuation-theorem style coarse-graining tests,
2. protocol-level quantum-walk transport invariants.

That split is healthy. The chapter already has hard null-style tests for the cleanest claims, while the more ambitious measurement and hardware-interface tests remain explicitly deferred until their protocols are locked.

The simulator pathway then becomes more concrete:
1. use boundary registers rather than explicit full-bulk state tracking,
2. test locality-preserving update families on small graph cuts,
3. check standing-mode stability, transport symmetry, and boundary observables before attempting full emergent interpretation.

## 8.9 QM Falsifiability Statements
Main-text rows stay compact. The full matrix, metadata, and forecast details belong in Appendix B and the governance material.

| prediction_id | observable | null model | signed prediction | parameter policy | decision rule | falsifier statement |
|---|---|---|---|---|---|---|
| `QM-CORE-001` | superluminality proxy `\delta_\nu` | Lorentz-invariant propagation | consistent with zero; no species-dependent superluminal branch in the QM regime | `none` | reject if a joint UHE-neutrino analysis excludes zero and yields `|\delta_\nu|>1e-21` after source-lag systematics | robust nonzero superluminality falsifies fixed-latency universality in the QM regime |
| `QM-CORE-002` | collapse-rate proxy `\lambda_{\mathrm{CSL}}` | standard unitary QM with no intrinsic collapse | consistent with zero collapse | `none` | reject if an independent experiment obtains `\lambda_{\mathrm{CSL}}>1e-10\,\mathrm{s}^{-1}` at `>=5 sigma` with reproduced systematics | a reproducible positive collapse rate above threshold falsifies the strict unitary microdynamics package |

Deferred but tracked elsewhere:
1. coarse-graining and fluctuation-theorem residual tests,
2. protocol-level quantum-walk transport asymmetry tests.

## Chapter 8 Summary
Established in this chapter:
1. the QM branch is the fixed-latency, unitary, graph-local branch of the theory,
2. a two-node standing pattern is explicitly witnessed rather than merely assumed,
3. the first nontrivial graph-supported standing family appears once the graph has at least one independent cycle,
4. the standing-wave existence theorem is now backed by an explicit witness-family proof program.

Not claimed here:
1. uniqueness of the admissible standing-mode family,
2. full Born-rule or collapse-free measurement closure,
3. completion of the deferred symmetry and simulator protocol programs.

---

# Chapter 9 - Standard Model Sector

The Standard-Model-facing branch of the paper packages particle-structure claims with strict maturity tags. The goal here is not to claim that UniNet has already derived the full Standard Model. The goal is narrower: show how chiral structure, CP sensitivity, standing-wave particle language, and gauge-as-redundancy constraints carve out a nontrivial admissible sector for the update operator.

## 9.1 Sector Assumption Ledger
The SM-facing chapter keeps its imports explicit.

| SM ID | Content | Status | Role in this chapter |
|---|---|---|---|
| `SM-A1` | chiral decomposition of node Hilbert space | `proved` | mode taxonomy basis |
| `SM-A2` | chiral-structure transfer requirement | `postulate` | admissibility condition |
| `SM-A3` | CP non-commutation metric | `postulate` | CP-asymmetry control |
| `SM-A4` | spin-statistics connection | `external-constraint` | interpretation constraint |
| `SM-A5` | quantitative admissible window | `postulate` | viability bound |
| `SM-A6` | gauge-group constructive emergence | `deferred` | explicit construction pending |

This chapter therefore does not start from a completed particle theory. It starts from a constrained transfer-operator sector and asks what particle-facing structure is admissible there.

## 9.2 Chiral Decomposition and Admissibility Constraints
The SM-facing admissibility window is encoded by four paper-facing requirements.

### `REQUIRED-SM-01` - Chiral Structure Preservation
Status: `postulate`

At each node,

$$
\mathcal{H}_v=\mathcal{H}_v^L\oplus\mathcal{H}_v^R,
$$

and the local transfer block has the form

$$
C_v=
\begin{pmatrix}
C_v^{LL} & C_v^{LR}\\
C_v^{RL} & C_v^{RR}
\end{pmatrix},
$$

with unitary block identities inherited from $C_v^\dagger C_v=I$.

Define the chirality-mixing amplitude

$$
\epsilon_{\mathrm{mix}}(v)
:=
\|C_v^{LR}\|_{\mathrm{op}}+\|C_v^{RL}\|_{\mathrm{op}}.
$$

### `REQUIRED-SM-02` - CP Symmetry or Violation
Status: `postulate`

Define the CP-breaking strength by

$$
\epsilon_{\mathrm{CP}}
:=
\frac{1}{2}\|[\mathsf{CP},U]\|_{\mathrm{op}}.
$$

The SM-like branch requires this quantity to be small but nonzero.

### `REQUIRED-SM-03` - Spin-Statistics Constraint
Status: `external-constraint`

Exchange symmetry is imposed at the interpretation layer:

$$
\Psi^{\mathrm{fermi}}_{\alpha\beta}=-\Psi^{\mathrm{fermi}}_{\beta\alpha},
\qquad
\Psi^{\mathrm{bose}}_{\alpha\beta}=+\Psi^{\mathrm{bose}}_{\beta\alpha}.
$$

This chapter uses the spin-statistics theorem as an external admissibility constraint, not as an internally derived result.

### `REQUIRED-SM-04` - Quantitative Admissible Window
Status: `postulate`

Define the global diagnostics

$$
\bar{\epsilon}_{\mathrm{mix}}
:=
\frac{1}{|V|}\sum_{v\in V}\epsilon_{\mathrm{mix}}(v),
\qquad
\epsilon_{\mathrm{CP}}
:=
\frac{1}{2}\|[\mathsf{CP},U]\|_{\mathrm{op}}.
$$

The SM-like admissible window requires

$$
0<\bar{\epsilon}_{\mathrm{mix}}\le \epsilon_{\mathrm{mix}}^{\max}\ll 1,
\qquad
0<\epsilon_{\mathrm{CP}}\le \epsilon_{\mathrm{CP}}^{\max}\ll 1.
$$

This excludes both the trivial parity-symmetric operator and the strongly mixed non-perturbative operator.

## 9.3 Particle Identity as Boundary-Stabilized Standing-Wave Class
This chapter imports the particle principle from `AXIOM-10` and combines it with the QM standing-wave program.

The paper-facing move is:
1. particle-like excitations are not primitive corpuscles,
2. they are admissible standing or quasi-standing mode classes,
3. sector labels such as chirality and CP sensitivity restrict which mode classes are dynamically allowed.

So the Standard-Model-facing chapter does not introduce an independent particle ontology. It refines the admissible mode taxonomy.

## 9.4 CP and Spin-Statistics Constraints and What Remains External or Deferred
Two boundaries must stay visible.

First, CP structure is part of the transfer-operator admissibility package, but its map to full flavor physics is not yet completely derived. The paper can therefore talk about a quantified CP-breaking control parameter, but it cannot claim full flavor closure.

Second, spin-statistics remains external in this chapter. That means:
1. the paper may use it to constrain admissible sector assignments,
2. it may not claim an internal derivation of the spin-statistics theorem from the current UniNet core.

That distinction is not a weakness. It is exactly the kind of boundary that keeps the chapter auditably honest.

## 9.5 Gauge-as-Redundancy Placement and Symmetry Maturity
The paper already showed in Chapter 4 that gauge-style redundancy can be treated as cut-observable redundancy. This is the right point to apply that insight to the SM-facing sector.

What is already justified:
1. redundancy language may be attached to transformations that preserve boundary observables,
2. some symmetry structure is therefore operationally real before a full gauge-group emergence theorem exists.

What is not yet justified:
1. a theorem that the full internal gauge group

$$
U(1)\times SU(2)\times SU(3)
$$

has been constructively derived,
2. full anomaly and representation closure from the current transfer operator alone.

So the paper distinguishes:
1. gauge-as-redundancy as an operationally meaningful theorem-level placement,
2. gauge-group emergence as a deferred constructive program.

## 9.6 `BOX-SM-01` - CP/CMB Chirality Overlap
Status: `compatibility note`

The paper's cross-sector chirality note is modest on purpose.

Assume a small effective chirality-control parameter $\chi$ influences both particle-sector CP observables and CMB parity or birefringence observables. Then a ballpark overlap window near

$$
\chi\sim 10^{-3}
$$

appears plausible if the relevant transfer coefficients are not wildly hierarchical.

What this box does support:
1. a non-empty overlap region is plausible at the scale-comparison level,
2. the current small-mixing, small-CP branch is not in obvious conflict with parity-sensitive cosmology channels.

What it does not support:
1. uniqueness,
2. a joint forward model,
3. a theorem-level cross-sector fit.

So this box is best read as a consistency check, not as a full prediction.

## 9.7 Mapping Completeness and Proof Obligations
The SM-facing program is partially structured and partially deferred.

Already structured:
1. chiral mode taxonomy,
2. bounded chirality mixing window,
3. quantified CP non-commutation metric,
4. standing-wave particle interpretation,
5. operational gauge-as-redundancy placement.

Still incomplete or deferred:
1. full gauge-group emergence,
2. anomaly and representation closure as an internal theorem package,
3. family and flavor structure derivation,
4. non-emptiness proof for the full SM-side admissible class at the strongest level,
5. Floquet or periodic-mode stability to observable lifetime map.

This is why the chapter can already say something sharp about admissibility, while still refusing to claim full Standard Model derivation.

## 9.8 Observation Anchors
The cleanest current SM-facing observation anchors are:
1. chirality-sensitive weak-decay ratios,
2. flavor-sector CP asymmetries,
3. later, potentially, joint chirality-parity cross-checks with cosmology once a forward map is locked.

The falsifiability index is right to rank the chirality-window test high. Precision pion-decay measurements are one of the quickest ways to reject an over-constrained or badly locked chiral-transfer branch.

## 9.9 SM Falsifiability Statements
Main-text rows stay compact. The full matrices, metadata, and forecast details belong in Appendix B and the governance material.

| prediction_id | observable | null model | signed prediction | parameter policy | decision rule | falsifier statement |
|---|---|---|---|---|---|---|
| `SM-CORE-001` | pion leptonic ratio residual `\Delta R_\pi` | SM V-A charged-current baseline | residual must stay small and sign-consistent with the locked chirality-mixing branch | `pre-locked-from-disjoint-data` | reject if the pre-locked `\epsilon_{\mathrm{mix}}` window is excluded at `>=5 sigma` by precision pion-decay data | if precision pion-decay data rule out the locked chirality-mixing window, the SM-side chiral transfer packaging fails |
| `SM-CORE-002` | `\sin(2\phi_1)` from `B\to J/\psi K_S` | CKM baseline fit | nonzero and inside the locked CP window | `pre-locked-from-disjoint-data` | lock `\epsilon_{\mathrm{CP}}` on kaon-sector data, then reject if the measured `\sin(2\phi_1)` lies outside the 95% predictive interval with `>5 sigma` tension | if locked CP non-commutation fails cross-sector prediction in `B` decays, the CP map is falsified |

Deferred but tracked elsewhere:
1. direct kaon-row promotion with a locked future threshold,
2. the joint CP-CMB chirality linkage as a full Popper prediction.

## Chapter 9 Summary
Established in this chapter:
1. the SM-facing branch constrains the update operator through chiral and CP-sensitive admissibility windows,
2. particle identity is treated as admissible standing-wave mode structure rather than primitive ontology,
3. gauge redundancy is placed operationally before any full gauge-group emergence claim.

Not claimed here:
1. full Standard Model derivation,
2. constructive emergence of

$$
U(1)\times SU(2)\times SU(3),
$$

3. internal derivation of the spin-statistics theorem,
4. complete flavor and family closure.

---

# Chapter 10 - Cosmology Sector

The cosmology branch packages large-scale consequences of existing UniNet structures. It does not introduce new microscopic axioms. Instead it asks what coarse-grained background, growth, parity, and early-universe behavior can be packaged from buffering, flux, projection, and queue-limited transport while keeping all forward-model gaps explicit.

## 10.1 Sector Assumption Ledger
The cosmology-facing imports are:

| COS ID | Content | Status | Role in this chapter |
|---|---|---|---|
| `COS-A1` | buffer dynamics can be coarse-grained into effective cosmological sectors | `postulate` | sector packaging |
| `COS-A2` | projection bridge to observed spacetime and units | `postulate` | observable calibration |
| `COS-A3` | queue-response and saturation constraints shape transport corrections | `postulate` | congestion and backpressure channel |
| `COS-A4` | observer-time and coarse-graining arrow remain consistent macroscopically | `proved + postulate` | thermodynamic directionality |
| `COS-A5` | full multipole transfer kernel to Boltzmann observables | `deferred` | precision CMB closure gap |
| `COS-A6` | detector-level coupling map for non-particle dark sector | `deferred` | direct-detection interface gap |

This chapter is therefore a packaging chapter with explicit theorem support and explicit non-closure boundaries.

## 10.2 Phenomenological Packaging: Dark Energy, Dark Matter, Inflation
The paper uses three paper-facing cosmology packages.

### `PROPOSITION-COS-01` - Dark Energy Packaging
Status: `postulate`

Buffer relaxation is packaged as an effective dark-energy branch. Operationally one writes an evolving equation of state, for example in CPL form,

$$
w(z)=w_0+w_a\frac{z}{1+z}.
$$

The paper-facing sign claim is that the relevant branch can depart slightly from $\Lambda$CDM while remaining small and testable.

### `PROPOSITION-COS-02` - Dark Matter Packaging
Status: `postulate`

Long-wavelength buffered modes are packaged as a dark-matter-like sector. In the relevant regime they can mimic pressureless clustering behavior while still being rooted in the same microscopic substrate.

### `PROPOSITION-COS-03` - Inflation Packaging
Status: `postulate`

An early-time phase or buffering mechanism is packaged as an inflationary branch whose basic phenomenological requirements are:
1. red tilt,
2. low tensor amplitude,
3. a viable exit mechanism, which remains deferred in full detail.

These are not theorem-level derivations. They are explicit cosmological branches built from already-declared microscopic and bridge ingredients.

## 10.3 Early Black Holes and Boundary-Trapping Interpretation
The boundary and GR chapters already provide a suggestive interpretation of extreme trapping regions. Cosmology then inherits a natural early-black-hole story:
1. stronger and more frequent propagating disturbances in the early universe can increase temporary congestion,
2. stronger congestion can increase the probability of incremental inspiral or trapping in boundary-limited regimes,
3. this makes early compact-object or merger activity a plausible downstream consequence rather than an unrelated cosmological add-on.

This remains a phenomenological packaging layer, not a core theorem. The chapter can therefore say that early black-hole activity is compatible with boundary-trapping logic, but it cannot claim a fully quantitative forward model yet.

## 10.4 Last-Parsec Problem Notes
The same caution applies to the last-parsec problem. The framework has a suggestive mechanism:
1. queueing and boundary-limited release can modify transport bottlenecks,
2. bottleneck-sensitive channels may affect inspiral efficiency in dense environments,
3. this could provide an additional route for merger completion.

But the paper does not yet have a quantitative transport-to-astrophysical binary map. So this remains a structured note, not a promoted cosmological theorem.

## 10.5 Computability Note
The framework suggests a useful computational lesson.

Because UniNet has:
1. graph locality,
2. cut balance,
3. boundary-mediated observables,
4. non-injective projection,

higher-scale descriptions are naturally built by discarding interior detail and retaining boundary summaries.

That means boundary cutting can simplify modeling rather than merely truncate it. In paper language: coarse-grained cosmological evolution may become more computationally tractable when one treats large interior regions through boundary summaries instead of insisting on fully resolved microscopic state everywhere.

This is an interpretive and methodological point, not a theorem-level cosmological prediction.

## 10.6 Mapping Completeness and Proof Obligations
The cosmology chapter is intentionally mixed in maturity.

Already structured:
1. effective background packaging,
2. dark-energy, dark-matter, and inflation branch statements,
3. thermodynamic consistency inherited from the arrow theorem,
4. a falsifiability layer with several compact core rows.

Still incomplete or deferred:
1. the full perturbation-to-observable transfer kernel,
2. the queue and backpressure map to scale-dependent growth residuals,
3. inflation exit and reheating map to thermal-history observables,
4. detector-level coupling map for non-particle dark-sector claims,
5. a fully locked joint cosmology plus parity forward model.

This is why the chapter can legitimately package cosmological branches while still refusing to claim complete multipole-level or detector-level closure.

## 10.7 Observation Anchors
The cleanest cosmology observation anchors are:
1. late-time equation-of-state fits,
2. growth suppression or enhancement summaries,
3. primordial tilt and tensor-amplitude constraints,
4. parity and birefringence-sensitive CMB channels.

Some channels are already compact main-text falsifiability rows. Others remain deferred until the forward kernels are frozen.

The CMB parity and birefringence channels are especially useful because they also connect back to the SM-facing chirality discussion. That cross-sector relevance is real, but still only at the level of a constrained small-effect branch rather than a finished joint theory.

## 10.8 Cosmology Falsifiability Statements
Main-text rows stay compact. The full matrices, metadata, and forecast details belong in Appendix B and the governance material.

| prediction_id | observable | null model | signed prediction | parameter policy | decision rule | falsifier statement |
|---|---|---|---|---|---|---|
| `COS-CORE-001` | CPL pair `(w_0,w_a)` | flat `\Lambda`CDM | locked branch predicts `w_0>-1` and `w_a<0` | `pre-locked-from-disjoint-data` | reject if Stage-IV combined posteriors exclude the locked sign pattern at `>=5 sigma` | if precise late-time expansion data force the opposite sign structure, this dark-energy branch is false |
| `COS-CORE-002` | growth-amplitude summary `S_8` or equivalent `f\sigma_8` residual family | Planck-anchored `\Lambda`CDM growth | downward residual shift relative to the baseline | `pre-locked-from-disjoint-data` | reject if high-precision Stage-IV analyses find no residual suppression while excluding the UniNet-predicted shift at `>=5 sigma` | if growth data converge to no suppression at high precision, the congestion signature fails |
| `COS-CORE-003` | primordial pair `(n_s,r)` | minimal inflation baseline constraints | require `n_s<1` and low `r` | `none` | reject if future joint CMB analyses require `n_s\ge 1` at `>=5 sigma` or detect `r` above the locked low-`r` ceiling | if the primordial spectrum is forced to scale-invariant, blue, or high-`r` beyond tolerance, this inflation packaging is false |
| `COS-CORE-004` | birefringence and parity-odd CMB summaries | parity-even `\Lambda`CDM baseline with zero birefringence | nonzero-or-zero only inside a locked small-effect window | `pre-locked-from-disjoint-data` | lock chirality on disjoint non-CMB data, then reject if the predicted parity interval is excluded by precise polarization posteriors at `>=5 sigma` | if the locked small-effect chirality branch predicts a signal pattern that precise CMB polarization excludes, this branch is false |

Deferred but tracked elsewhere:
1. multipole-level residual templates,
2. scale-dependent growth-shape residual templates,
3. direct-detection or collider statements for the non-particle dark-sector branch.

## Chapter 10 Summary
Established in this chapter:
1. cosmological consequences are packaged from already-declared UniNet structures rather than new microscopic axioms,
2. dark-energy, dark-matter, and inflation branches are explicit phenomenological packages,
3. queue and boundary logic provide structured correction channels for late-time and compact-object phenomenology.

Not claimed here:
1. a completed multipole-level transfer theorem,
2. a completed reheating or detector-coupling closure,
3. that current cosmological tensions are already decisively resolved by the framework.

---

# Chapter 11 - Governance, Audit, and Falsifiability Discipline

Paper 1 is intentionally split into two layers: a mathematical layer that states axioms, definitions, theorems, and postulates, and a governance layer that controls how claims are allowed to appear. This chapter defines that second layer. Its purpose is simple. It prevents theorem inflation, parameter circularity, and retrospective storytelling after data are known.

## 11.1 Claim Classes and Artifact Hierarchy
The paper uses four claim-status tags.

| Status | Meaning | Allowed manuscript use |
|---|---|---|
| `proved` | derived from earlier paper material or imported external theorem with declared scope | may be stated as established within that scope |
| `postulate` | explicit modeling or bridge choice | may be used operationally, but not advertised as derived |
| `deferred` | missing proof, forward map, threshold, or closure step | may be tracked, but not promoted rhetorically |
| `external-constraint` | imported theorem or observational constraint not internally derived | may be used with explicit scope and without ownership inflation |

### `GOV-01` - Canonical Source Hierarchy
Status: `governance`

The paper recognizes the following hierarchy of authority.

1. Core chapters carry the canonical scientific statements.
2. Appendices carry notation tables, governance rules, relabel aids, and full falsifiability metadata.
3. Extended proof notes may elaborate long derivations, but they do not silently upgrade claim status.
4. Planning material is not evidence.

The practical rule is that no sentence in the paper is allowed to outrun the status tag of the claim it depends on.

## 11.2 Dependency DAG and Claim Audit
The manuscript is organized as a mostly acyclic information graph:

$$
\text{Axioms}
\to
\text{Shared Definitions and Theorems}
\to
\text{Boundary and Update Structure}
\to
\text{Symmetry Layer}
\to
\text{Sector Packaging}
\to
\text{Falsifiability Rows}.
$$

This is both a writing rule and an audit rule.

1. Later chapters may depend on earlier chapters.
2. Forward references are allowed only for navigation, not for proof logic.
3. If two claims depend on each other, the common material must be lifted upward until the cycle disappears.

### `GOV-02` - Claim Audit Rule
Status: `governance`

Every nontrivial manuscript claim must admit a dependency path to one of the following:
1. an earlier paper theorem or definition,
2. an explicit postulate,
3. an explicitly scoped external theorem or empirical constraint.

If no such path exists, the claim is automatically classified as `deferred`.

## 11.3 Proof-Status Synchronization
The paper-facing status tags must agree with the canonical ledger discipline.

### `GOV-03` - Status Synchronization Rule
Status: `governance`

If a manuscript statement and its governing status registry disagree, the lower maturity wins until the conflict is resolved explicitly.

Operationally this means:
1. no theorem language for a `postulate`,
2. no established-fact language for a `deferred` item,
3. no imported theorem may be presented as internally derived.

## 11.4 Parameter Discipline and Lock Protocol
Observable-facing claims require a second control layer: parameter discipline. The paper uses four parameter classes.

| Parameter class | Meaning |
|---|---|
| `fixed` | set by convention, definition, or already-declared model choice |
| `fit` | inferred from a lock dataset and then frozen |
| `derived` | computed from fixed or fitted quantities |
| `deferred` | conceptually present, but not yet finitely parameterized or not yet lockable |

The reduced first-pass fit basis is

$$
\theta_{\mathrm{fit},v1}
=
\{
\bar{\epsilon}_{\mathrm{mix}},
\epsilon_{\mathrm{CP}},
\alpha,
\beta,
\xi_{\mathrm{leak}},
\tau_{\mathrm{relax}},
\lambda_{\mathrm{DM}},
A_{\mathrm{cong}},
\Phi_{\max}/\Phi_{\mathrm{initial}},
\chi_{\mathrm{parity}}
\}.
$$

### `GOV-04` - Disjoint Lock Protocol
Status: `governance`

1. Choose the fit basis before target testing.
2. Assign a disjoint lock dataset family to every fitted parameter.
3. Freeze the posterior or allowed interval.
4. Test the target observable on non-overlapping data only.

This is the paper's anti-circularity rule. A branch is not allowed to fit itself to the same dataset it later advertises as confirmation.

## 11.5 Main Falsifiability Contract
The paper adopts a hard-Popper standard for every main-text prediction row. A row qualifies as core only if all of the following are true.

1. the observable is operationally explicit,
2. the comparison is made against exactly one null model,
3. the sign or direction of the claim is fixed,
4. the parameter policy is either `none` or `pre-locked-from-disjoint-data`,
5. the decision rule is binary,
6. the falsifier statement is written in plain language.

### `GOV-05` - Core Prediction Admissibility
Status: `governance`

A compact falsifiability row is admissible in the main text only if it has the form

$$
(\text{observable},\ \text{null model},\ \text{signed prediction},\ \text{parameter policy},\ \text{decision rule},\ \text{falsifier}).
$$

Rows missing any component remain tracked, but they are classified as `deferred`.

## 11.6 Main Text Versus Appendix B
The main body of the paper carries only compact rows. Appendix B carries the full audit payload:

1. claim-status vocabulary,
2. sector-by-sector core and deferred counts,
3. parameter classes and reduced fit basis,
4. priority test order,
5. promotion blockers,
6. anti-circularity and blind-analysis expectations.

### `GOV-06` - Manuscript/Appendix Falsifiability Split
Status: `governance`

Compact decision rows belong in the main text. Full matrices and audit metadata belong in Appendix B. Neither may contradict the other.

## 11.7 Non-Claims Boundary and Anti-Circularity
The paper also needs an explicit anti-overclaim contract. The current non-claims are:

1. no full Standard Model derivation is claimed,
2. no full microscopic-to-observable transfer closure is claimed in every sector,
3. no complete black-hole quantitative closure is claimed,
4. no detector-level non-particle dark-sector claim is promoted without an explicit coupling map,
5. no unique microscopic transport family is claimed,
6. no full Noether closure is claimed across all sectors,
7. no full cosmological multipole transfer closure is claimed.

### `GOV-07` - Non-Claims Boundary Rule
Status: `governance`

A statement may be promoted beyond the current non-claims boundary only when its proof status, forward map, and observational decision rule have all been frozen explicitly.

## 11.8 Exploratory Numerics and Audit Procedure
The paper permits exploratory numerics, but only under quarantine.

Exploratory scans may be reported only if all three statements remain true:
1. they are not used as theorem evidence,
2. they are not used as parameter locks,
3. they are described as compatibility checks rather than confirmations.

Under that rule, the first `InferenceLight` scan may be mentioned as follows:
1. it is a compatibility-first exploratory result,
2. it indicates that the current cosmology-facing branch remains compatible with a Regge-like curved-spacetime regime,
3. it does not uniquely select GR or Einstein-field-equation closure.

A reader who wants to audit any claim in the paper should then follow this order:
1. identify the claim's status tag,
2. find its parent theorem, postulate, or external constraint,
3. inspect the relevant parameter policy,
4. inspect the falsifiability row if the claim is observable-facing,
5. check Appendix B if the main text summary is too compressed.

## Chapter 11 Summary
Established in this chapter:
1. claim status is governed by a strict four-way vocabulary,
2. manuscript logic is constrained to a mostly DAG-like dependency structure,
3. parameter fitting must obey a disjoint lock protocol,
4. main-text falsifiability statements must be compact but decision-complete,
5. exploratory numerics are explicitly quarantined from proof and calibration.

Not claimed here:
1. that governance rules themselves prove physics,
2. that every deferred item already has a finished observational interface,
3. that compatibility scans count as confirmation.

---

# Chapter 12 - Philosophical Chapter

hhis chapter is interpretive synthesis. It does not add axioms, and it does not upgrade any theorem by wording. Its purpose is to explain what sort of picture the formalism supports if the earlier chapters are taken seriously: a local, information-preserving substrate; observation through cuts and boundaries; emergent macroscopic time; and sector-dependent coarse descriptions built on top of one underlying update rule.

## 12.1 Boundary Ontology
hhe cleanest philosophical summary of UniNet is:

> Reality is what crosses a boundary; everything else is internal state.

hhat slogan is not a replacement for the mathematics. It is a compact reading of three earlier ingredients:
1. graph cuts are primitive,
2. interiors are operationally accessed only through boundary observables,
3. coarse observation is non-injective.

In formal terms, if two interior states satisfy

$$
\psi|_R \sim_{\partial R} \psi'|_R,
$$

then no exterior observer can distinguish them through the chosen boundary channel. hhe philosophical consequence is immediate: the theory does not deny interior reality, but it denies unrestricted operational access to it.

## 12.2 Determinism and Observed Randomness
At the microscopic layer the theory is deterministic in the minimal operational sense of a fixed update family:

$$
\psi_{n+1}=U_n\psi_n,
\qquad
U_n^\dagger U_n=I.
$$

So the substrate does not need a fundamental stochastic collapse term. Randomness enters when a many-to-one observation map discards microscopic detail. hhis is the meaning of the arrow theorem and of the measurement-facing packaging used in the QM chapter.

hhe resulting philosophical stance is:
1. microdynamics may remain unitary and information-preserving,
2. observed probabilities arise at the coarse interface,
3. thermodynamic irreversibility is a statement about description and access, not necessarily about microscopic loss.

hhat is why the decay slogan is reasonable in this framework:

> Decay randomness is thermodynamic in form, not ontological in origin.

Paper 1 does not claim that every measurement protocol is fully derived from this idea. It claims only that the framework has a consistent route from deterministic substrate dynamics to effective probabilistic observation.

## 12.3 hime as Order Rather hhan Primitive Flow
hhe shared theorem spine already replaces absolute observed time by order-theoretic structure plus coarse description. Philosophically, that places the framework near relational-time programs rather than naive absolute-time pictures.

hhe core object is not a primitive continuum clock. It is an update order together with causal precedence and coarse observables. A paper-facing summary is:

$$
\text{substrate order} + \text{coarse observation}
\Longrightarrow
\text{effective } t_{\mathrm{obs}}.
$$

hhis does not prove exact equivalence to Rovelli-style or Page-Wootters-style formalisms. But it does justify a strong comparative claim: observed time in UniNet is emergent from relations, accessibility, and coarse description, not assumed as a primitive background substance.

## 12.4 Wave, Particle, and Measurement Context
hhe QM chapter supports a unified reading of wave and particle language. Long-lived particle-like objects are mode structures,

$$
U\phi=\lambda\phi,
\qquad
|\lambda|=1,
$$

or narrow superpositions of such modes. Different experimental contexts then reveal different aspects of the same underlying dynamics.

hhis suggests the following philosophical summary:

> Quantum mechanics is the effective interface theory of boundary cuts whose transport is stable, local, and unsaturated.

hhe point is not to erase standard wave mechanics. It is to reinterpret it. Interference, localization, and measurement records are not three unrelated stories; they are different observable packagings of one underlying transport law plus one observation rule.

Paper 1 still stops short of a full measurement theorem. So the correct status is compatibility and explanatory coherence, not final closure.

## 12.5 Recursive Boundary Renormalization
One of the most useful conceptual consequences of the framework is the repeated appearance of the same pattern at different scales:

1. microscopic interiors are summarized by graph-cut data,
2. field-like descriptions summarize many unresolved transport histories,
3. composite matter summarizes many internal modes through a small boundary interface,
4. astrophysical systems summarize interiors through surface, horizon, and flux data,
5. cosmology summarizes inaccessible history through last-scattering and horizon-scale observables.

hhis is a recursive boundary-renormalization ladder. Complexity is controlled not by retaining every microscopic detail, but by discarding most of it while preserving the boundary information that remains operationally relevant.

hhe philosophical consequence is important: higher levels of description need not add deeper ontology. hhey may instead add better summaries.

## 12.6 Paradox Hygiene and Comparative Reading
Many famous paradoxes in quantum foundations and black-hole discussions are intensified by assumptions of unrestricted access, globally synchronized observation, or fundamental observed time. UniNet rejects those assumptions early.

hhat does not mean the paradoxes are "solved" by declaration. It means some familiar formulations become structurally ill-posed inside this framework.

hhe comparison points are then:
1. Einstein: micro-level determinism is compatible with effective observed randomness,
2. Bohr: observable content remains context-dependent at the measurement interface,
3. Wigner-style observer layering: different coarse descriptions may coexist until causal contact forces comparison,
4. Rovelli and Page-Wootters: observed time is relational and emergent rather than primitive,
5. Bell-style nonclassicality: the framework aims for contextual, observer-limited packaging without claiming a completed Bell theorem inside UniNet itself.

hhese comparisons are useful for intuition, but they are not evidence. hhe formal work still carries the proof burden.

## 12.7 Limits of Interpretation
ho keep this chapter disciplined, the paper explicitly does not claim:

1. a complete solution of the measurement problem in all protocols,
2. a full Bell-inequality derivation inside the present formalism,
3. a final resolution of Wigner-friend-type paradoxes,
4. that philosophical coherence substitutes for empirical success.

The philosophical layer is therefore subordinate to the mathematical and observational layers, not a substitute for them.

## 12.8 Speculative Numerical Hints
Exploratory numerics may motivate future work, but they do not alter theorem status. The first `InferenceLight` run is therefore relevant here only in the weakest possible sense: it suggests that the current cosmology-facing package remains compatible with a Regge-like curved-spacetime regime. It does not lock the program to GR or to Einstein-field-equation closure, and it does not substitute for the formal falsifiability rows in the sector chapters or Appendix B. The detailed quarantine rule is recorded in Chapter 11 and Appendix D.

## Chapter 12 Summary
Established in this chapter:
1. UniNet supports a boundary-centered ontology of observation,
2. microscopic determinism and effective observed randomness can coexist coherently,
3. observed time is naturally read as emergent and relational,
4. wave and particle descriptions are interpreted as context-dependent packagings of one transport law,
5. recursive boundary summarization offers a unifying view across scales.

Not claimed here:
1. a final solution to all interpretive paradoxes,
2. a complete Bell or measurement theorem,
3. philosophical closure without further proof and data.

---

# Chapter 13 - Conclusion and Paper-2 Hand-off

Paper 1 is designed to do one thing well: define a clean core, show how much follows from it already, and keep the remaining gaps explicit. The result is not a finished theory of everything. It is a structured framework with a readable axiomatic base, a shared theorem spine, a boundary-centered observational layer, a constrained update class, and sector chapters that separate theorem, postulate, and deferred work.

## 13.1 What Paper 1 Establishes
The main established outcomes are:

1. a finite graph-based substrate with relabeling covariance, locality, information preservation, graph cuts, boundary observability, and standing-mode particle language,
2. a shared theorem spine for reachability, latency, causal order, bulk-boundary balance, leaky boundaries, and the emergent arrow from non-injective observation,
3. a boundary chapter that makes cut observables, boundary capacity, and mediator language central rather than peripheral,
4. an update-function chapter that shows the admissible transport class is constrained but non-empty,
5. sector packaging chapters for GR, QM, SM, and cosmology, each with its own assumption ledger and compact falsifiability rows,
6. a governance layer that prevents proof inflation and circular calibration.

This is already enough to state a coherent research program in paper form.

## 13.2 What Remains Open
The paper also leaves several major obligations deliberately unfinished.

GR-facing obligations:
1. full action-level Regge-to-Einstein closure,
2. stronger black-hole forward models for Page-like, echo-like, and multimode observables,
3. sharper bridge from effective geometry to observationally locked waveform families.

QM-facing obligations:
1. promotion of the standing-mode proof from explicit witness-family concept to full theorem-level closure,
2. protocol-complete transport and measurement mappings,
3. stronger hardware-facing quantum-walk and fluctuation-theorem interfaces.

SM-facing obligations:
1. explicit gauge-group emergence,
2. three-family representation closure,
3. a fully locked joint flavor plus chirality plus parity forward map.

Cosmology-facing obligations:
1. explicit multipole transfer kernels,
2. scale-dependent growth residual templates,
3. inflation-exit and reheating observables,
4. detector-coupling maps for non-particle dark-sector tests.

These open items are not hidden weaknesses. They are the deferred queue that keeps the paper honest.

## 13.3 Priority Promotion Queue
The most valuable next promotions are the ones that shorten the longest logical gaps.

1. promote the GR bridge from Regge-compatible geometry to action-level Regge dynamics,
2. tighten `THEOREM-QM-02` with a cleaner standing-mode existence proof and more explicit literature-supported witness class,
3. freeze the finite parameterization needed for projection and flavor-phase sectors,
4. promote the first deferred falsifiability rows whose forward maps are closest to closure,
5. formalize the Noether promotion path where the action domain and boundary terms can actually be frozen.

This is the sequence most likely to improve both rigor and readability at the same time.

## 13.4 How Paper 2 Should Build on Paper 1
Paper 2 should not restart the axioms. It should reuse the established core and focus on one of two possible directions.

Direction A: bridge-closure paper
1. Regge dynamics,
2. Einstein-equation-facing bridge,
3. sharper horizon and waveform consequences.

Direction B: observable-interface paper
1. frozen lock protocol,
2. blind-analysis-ready prediction rows,
3. explicit sector forward maps,
4. first serious data-facing pruning.

Either route is viable, but both depend on Paper 1 remaining the canonical source of the shared core.

## 13.5 Final Position
The manuscript's final position is therefore deliberately balanced.

It proves some things.
It postulates some things.
It defers some things.

That balance is a strength, not a weakness, provided it is stated plainly. The theory is most defensible when the reader can always tell which layer they are standing on.

## Chapter 13 Summary
Established in this chapter:
1. Paper 1 has a coherent and nontrivial core contribution,
2. the open problems are organized rather than vague,
3. the next-paper handoff can proceed without re-litigating the whole manuscript architecture.

Not claimed here:
1. that all major bridges are already closed,
2. that every deferred item belongs in the next paper,
3. that the present manuscript is the final form of the program.

---

# Appendix A - Notation and Units

This appendix fixes the notation used throughout Paper 1. It is deliberately compact. The main purpose is to prevent silent renaming across chapters.

## B.1 Core Symbols

| Symbol | Meaning |
|---|---|
| $G=(V,E)$ | substrate graph |
| $n\in\mathbb{Z}$ | discrete update parameter |
| $t$ or $t_{\mathrm{obs}}$ | observed or continuous time variable |
| $\psi_n\in\mathcal{H}$ | full state at tick $n$ |
| $\psi_v(n)$ | node-local state |
| $\rho(v,n)=|\psi_v(n)|^2$ | occupancy or buffering density |
| $J_n(u\to v)$ | directed flux |
| $Q_n(R)$ | bulk quantity on region $R$ |
| $\Phi_n(\partial R)$ | boundary flux across $\partial R$ |
| $d_G(u,v)$ | graph distance |
| $\delta_{\mathrm{QM}}(u,v)$ | QM latency |
| $\delta_{\mathrm{GR,eff}}(u,v)$ | GR effective latency |
| $\Pi_v$ | projection map at node $v$ |
| $T_{00}(v,n)$ | projected energy-density-like observable |
| $\epsilon_{\mathrm{mix}}$, $\bar{\epsilon}_{\mathrm{mix}}$ | chirality-mixing quantities |
| $\epsilon_{\mathrm{CP}}=\frac12\|[\mathsf{CP},U]\|_{\mathrm{op}}$ | CP non-commutation metric |
| $\ell_e$ | physical length assigned to one graph edge in the bridge map |
| $\Delta t$ | physical duration assigned to one substrate tick |

## B.2 Canonical Equations
The most frequently reused equations are:

$$
\psi_{n+1}=U_n\psi_n,
\qquad
U_n^\dagger U_n=I,
$$

$$
\rho(v,n)=|\psi_v(n)|^2,
$$

$$
\delta_{\mathrm{QM}}(u,v)=d_G(u,v),
$$

$$
\epsilon_{\mathrm{CP}}=\frac12\|[\mathsf{CP},U]\|_{\mathrm{op}},
$$

$$
c_{\mathrm{map}}=\ell_e/\Delta t.
$$

## B.3 Units Policy

1. Dimensionless quantities are assigned unit `1`.
2. Physical quantities use standard SI symbols when a physical bridge is invoked.
3. The paper distinguishes three categories:
   1. dimensionless model variables,
   2. projected physical observables,
   3. derived bridge quantities.

The important bridge constants are:

| Quantity | Unit | Role |
|---|---|---|
| $\ell_e$ | `m` | graph-to-length map |
| $\Delta t$ | `s` | graph-to-time map |
| $c_{\mathrm{map}}$ | `m/s` | emergent speed map |
| $\Lambda_{\mathrm{proj}}$ | energy-density unit | occupancy-to-observable projection constant |

## B.4 Formatting Discipline

1. Inline mathematics uses `$...$`.
2. Display mathematics uses `$$...$$`.
3. Text subscripts use `\mathrm{...}` where appropriate.
4. Calligraphic symbols such as $\mathcal{H}$ and $\mathcal{S}$ are used consistently.
5. The operator norm is written as $\|\cdot\|_{\mathrm{op}}$.

## B.5 Status Tags

| Tag | Meaning |
|---|---|
| `proved` | established within declared scope |
| `postulate` | modeling or bridge choice |
| `deferred` | explicit unfinished item |
| `external-constraint` | imported theorem or empirical bound |

These tags are part of the paper's meaning, not cosmetic labels.

---

# Appendix B - Governance and Falsifiability Appendices

This appendix carries the full governance-facing tables that are too heavy for the main text but necessary for hostile-review transparency.

## C.1 Claim-Status Vocabulary

| Status | Meaning | Typical blocker if not higher |
|---|---|---|
| `proved` | theorem-level within stated scope | none |
| `postulate` | explicit modeling choice | independent derivation absent |
| `deferred` | not yet promotable | missing proof, map, or threshold |
| `external-constraint` | imported result or empirical bound | internal derivation intentionally absent |

## C.2 Parameter Policy
The paper uses the following parameter classes:

| Class | Meaning |
|---|---|
| `fixed` | convention or already-declared choice |
| `fit` | locked on disjoint data before target testing |
| `derived` | computed from fixed or fitted inputs |
| `deferred` | not yet finitely parameterized or not yet lockable |

Reduced first-pass fit basis:

$$
\theta_{\mathrm{fit},v1}
=
\{
\bar{\epsilon}_{\mathrm{mix}},
\epsilon_{\mathrm{CP}},
\alpha,
\beta,
\xi_{\mathrm{leak}},
\tau_{\mathrm{relax}},
\lambda_{\mathrm{DM}},
A_{\mathrm{cong}},
\Phi_{\max}/\Phi_{\mathrm{initial}},
\chi_{\mathrm{parity}}
\}.
$$

Parameters excluded from fit by construction in the present version include $\ell_e$, $\Delta t$, $c_{\mathrm{map}}$, $\Lambda_{\mathrm{proj}}$, and theorem-derived quantities such as $\delta_{\mathrm{QM}}(u,v)$.

## C.3 Hard-Popper Row Contract
A main-text or appendix prediction row is decision-complete only if it contains:

1. an operational observable,
2. exactly one null model,
3. a signed prediction,
4. a declared parameter policy,
5. a binary decision rule,
6. a plain falsifier statement.

Rows failing any one of these conditions remain `deferred`.

## C.4 Sector Snapshot

| Sector | Core rows | Deferred rows | Main near-term role |
|---|---:|---:|---|
| QM | 2 | 2 | fixed-latency and no-collapse exposure |
| GR | 4 | 4 | cone, delay, dispersion, and leaky-boundary exposure |
| SM | 2 | 2 | chirality and CP windows |
| Cosmology | 4 | 3 | background, growth, inflation, and parity exposure |

## C.5 Priority Test Order
The present program order, ranked by immediate reject power, is:

1. GR cone-speed multiband tests,
2. SM chirality-window tests from precision pion decay,
3. cosmology sign tests in the $(w_0,w_a)$ plane,
4. GR leaky-boundary tidal-heating tests,
5. cosmology parity and birefringence tests after disjoint chirality lock,
6. QM static-latency universality tests,
7. deferred rows only after explicit map and threshold closure.

## C.6 Promotion Blockers by Domain

| Domain | Main blocker |
|---|---|
| GR bridge | action-level Regge-to-Einstein closure |
| GR black holes | locked entropy, ringdown, and image-domain forward maps |
| QM observer interface | protocol-complete coarse-graining statistics |
| QM standing modes | promotion of witness-family proof to full closure |
| SM emergence | gauge-group and representation derivation |
| Cosmology precision | explicit transfer kernels to multipole and growth observables |
| Symmetry/Noether | frozen action domain, generator class, and boundary terms |

## C.7 Non-Claims Contract
The paper currently forbids the following promotions:

1. "full Standard Model derivation,"
2. "complete black-hole quantitative solution,"
3. "detector-level non-particle dark-sector proof" without coupling map,
4. "complete Noether closure,"
5. "unique microscopic transport family,"
6. "completed cosmological multipole-level closure."

These remain forbidden until the relevant proof and test interfaces are actually frozen.

---

# Appendix C - Proof-Note Index

This appendix lists the extended proof notes that support major paper claims. These notes are companions to the manuscript, not substitutes for it. The paper chapters and status tags remain canonical.

## C.1 Current Extended Proof Notes

| Proof note title | Main paper claims supported | Function in the program | Current status |
|---|---|---|---|
| *Standing/Quasi-Standing Mode Existence in the Restricted UniNet Update Class* | `THEOREM-QM-02`, `LEMMA-QM-01` to `LEMMA-QM-07` | explicit witness-family construction for standing and quasi-standing modes under the restricted update class | proof concept with explicit witnesses; promotion still pending |
| *Buffering Delay to Effective Edge Length: Rigorous Bridge to Regge Geometry* | `THEOREM-GR-05`, `THEOREM-GR-06`, `THEOREM-GR-07` | extended bridge from delay to effective geometry and Regge-compatible regime arguments | conditional bridge note; action-level closure still pending |

## C.2 Reading Rule
The recommended reading order is:

1. read the paper chapter first,
2. use the proof note only if a longer derivation is needed,
3. return to the manuscript status tag before interpreting what has actually been established.

This prevents a common failure mode in long programs: a technically interesting note is mistaken for a promoted theorem even when its formal status remains `postulate` or `deferred`.

---

# Appendix D - Speculative Numerical Notes

This appendix records exploratory numerical material that is useful for program orientation but not yet admissible as proof evidence or parameter lock material.

## D.1 Quarantine Rule
Exploratory numerics appear here only under the following restrictions:

1. they do not prove any theorem,
2. they do not determine any locked parameter value used elsewhere in the paper,
3. they are interpreted as compatibility scans rather than confirmations.

## D.2 First `InferenceLight` Exploratory Scan
The first scan is summarized only at the level needed for orientation.

| Item | Value |
|---|---|
| run identifier | `inference_light_20260401T142451Z` |
| prior mix | 3 Regge-facing priors, 2 EFE-facing priors |
| dataset families | CMB, BAO, RSD, weak lensing |
| overall traffic light | `Green` |
| compatibility verdict | `fits_known_physics_at_all = true` |

Representative posterior medians from that scan were:

| Parameter | Median |
|---|---:|
| $\tau_{\mathrm{relax}}$ | 1.14768 |
| $\lambda_{\mathrm{DM}}$ | 1.07974 |
| $A_{\mathrm{cong}}$ | 0.213038 |
| $\Phi_{\max}/\Phi_{\mathrm{initial}}$ | 63.6687 |
| $\chi_{\mathrm{parity}}$ | -0.00200499 |

## D.3 Allowed Interpretation
The strongest allowed reading is:

1. the current cosmology-facing branch remains compatible with the compressed data used in the scan,
2. the retained parameter region is compatible with a Regge-like curved-spacetime regime,
3. the result does not uniquely select GR,
4. the result does not establish Einstein-field-equation closure,
5. the result does not calibrate the paper's fit basis.

In short:

> the scan is compatible with a Regge-compatible curved-spacetime regime, but it is not a lock to GR or EFE.

## D.4 Forbidden Interpretation
This appendix does not permit the following statements:

1. "the numerics prove the bridge,"
2. "the numerics lock the model,"
3. "the numerics show GR has been derived,"
4. "the numerics replace falsifiability rows."

The numerical role here is exploratory only.
