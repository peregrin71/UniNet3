# UniNet: Minimal Axiomatic Foundation

**A rigorous, self-contained reference for the graph-to-spacetime framework**

*Version 1.2 (March 2026, working draft)*

---

## Conceptual Preview: What Are We Building?

**In one sentence:** We are rebuilding Quantum Mechanics, the Standard Model, and General Relativityâ€”**entirely on a deterministic substrate**.

### The Intuition

Imagine a **vast graph** (like a cosmic network) where:
- **Each node** stores quantum information (internal d.o.f., split into left/right chiral sectors)
- **Each $t_{\text{tick}}$**, this information propagates to neighbors via a fixed **unitary transfer operator** $U$
- **No randomness, no collapse, no external rules**â€”just pure, reversible, deterministic wave evolution

### Information as the Currency: Mass/Energy Emerges from Confinement

Here's the key insight: **Information is not abstractâ€”it has physical consequences.**

**In the graph (Tier 0 â€” Microscopic):**
- Information at node $v$ is quantified by buffering density $\rho(v, t_{\text{tick}}) = |\psi_v(t_{\text{tick}})|^2$
- **Unitary evolution preserves total information** (Axiom 0.2: $\sum_v \rho(v, t_{\text{tick}}) = 1$ conserved)
- Confined information (high $\rho$ at a node) **resists propagation** â€” signals slow down
- Everything is deterministic, reversible, unitaryâ€”no randomness, no collapse

### What Emerges When We Coarse-Grain This Structure

Now the key question: **What happens when we average over microscopic structure and ask macroscopic questions?**

When we coarse-grain deterministic graph dynamics (averaging over Planck-scale structure), we get:

1. **Quantum mechanics' randomness** emerges from **projection and information hiding** (buffering density obscures phase information; we only observe composite observables, not all d.o.f.)
2. **Born rule** emerges from **averaging over fine structure**â€”deterministic â†’ appears random at macro scale
3. **Spacetime geometry** emerges as a **coarse-grained effective description** (transport costs create effective geometric delays)
4. **Standard Model gauge groups** $(U(1) \times SU(2) \times SU(3))$ emerge from **chiral mode topology** (not postulated)
5. **Fermion-boson distinction** emerges from **spin-statistics** (antisymmetry vs. symmetry under chiral sector exchange)
6. **CP violation** emerges from **complex phases in chiral involutions** (left/right sectors coupled with complex amplitudes)
7. **Dark matter, dark energy, inflation** all emerge from **buffer relaxation dynamics** (single mechanism, three manifestations)

### After Coarse-Graining: Projection to Spacetime and the Energy-Information Link

Once we've coarse-grained to a macroscopic description, we introduce the **linear projection** $\Pi_v$:
- Buffering density $\rho(v,n)$ (microscopic Tier 0) maps to energy density $T_{00}$ (macroscopic spacetime)
- **High information density = high energy density = strong gravity** (via Einstein's equation)
- **Mass emerges from information confinement**, not as a separate property

**Physical consequence:**
- **Black holes:** Extreme buffering (information maximally confined at horizon) â†’ extreme spacetime curvature
- **Information paradox resolved:** Information is **never lost** at Tier 0 (unitary evolution); it's released gradually via Hawking radiation as buffer decays (effective thermodynamics at macro scale)
- **Energy conservation:** Always rooted in information conservation (unitary dynamics at Tier 0)
- **Arrow of time emerges:** Coarse-graining discards phase information; forward evolution hides information in unobservable phases; backward reversal is impossible without the lost phase data. Result: **macroscopic time becomes irreversible** (second law, entropy increase) even though Tier 0 is reversible.

### Why This Matters

**Standard physics has separate stories:**
- QM: Born rule (axiom), measurement collapse (axiom), uncertainty principle (derived)
- GR: Smooth manifolds (axiom), Einstein-Hilbert action (axiom), curvature (derived)
- SM: Gauge groups (axiom), three families (axiom), Higgs mechanism (axiom)

**UniNet has one story:** Start with graph + unitary + buffering. Everything else is a **theorem**.

### The Price and the Prize

**What we give up:**
- Smooth spacetime (temporarilyâ€”emerges in continuum limit)
- Locality in spacetime (only graph locality; spacetime locality emerges)
- Gauge principle as starting point (gauge structure emerges)

**What we gain:**
- **Fundamental determinism** (no collapse; evolution is unitary)
- **Unified framework** (one mechanism for QM, SM, GR, cosmology)
- **Emergent structure** (gauge groups, coupling constants, family structure all derived)
- **Falsifiability** (specific predictions: buffer relaxation timescale, congestion feedback, chiral asymmetry in gravitational waves)

### The Constraints That Enable This

To achieve this emergence, the transfer operator $U$ is **not arbitrary**. It must satisfy:

- **R1: Graph locality** â€” information only spreads one hop per tick (enables causal structure)
- **R2: Unitarity (Information Preservation)** â€” reversible, norm-preserving dynamics (the **core constraint**: information is never lost, only redistributed; this solves the information paradox and guarantees energy conservation)
- **R3: Buffering consistency** â€” local conservation of information density (enables stress-energy projection; mass/energy emerges from information confinement via buffering)
- **R5: Chiral structure** â€” left/right sectors with measurable mixing (enables parity violation, CP violation)
- **R6: CP structure** â€” real chiral phases with controlled non-commutation with $U$ (enables matter-antimatter asymmetry while preserving unitarity)
- **R7: Spin-statistics** â€” fermions antisymmetric, bosons symmetric (enables Pauli exclusion)
- **R8: Quantitative admissible window** â€” transfer operators must lie in a narrow, weak-sector-compatible parameter band

Without these constraints, $U$ could be almost anything. **With them, $U$ converges to something that looks like the Standard Model.**

### The Roadmap

This document develops:

1. **Tier 0:** Seven axioms (graph, unitary, buffering, chirality) that are **non-negotiable**
2. **Tier 1â€“3:** Causal structure, time functions, observer timeâ€”all derived as theorems
3. **Tier 4â€“6:** Spacetime projection and energy-momentum calibration via explicit **bridge axioms** (4.1â€“4.3), then derived consequences
4. **Regimes:** QM (static latency) and GR (dynamic latency via field equation)
5. **Application:** Cosmology (dark sectors, inflation) from single buffering mechanism
6. **Queueing rigor expansion (planned):** explicit backlog/throughput observables, transport-operator viability gates, and boundary-layer black-hole queue theorems (see [QUEUEING_RIGOR_PLAN.md](QUEUEING_RIGOR_PLAN.md))

**The thesis:** If you grant the Tier-0 core axioms plus the Tier-4 bridge axioms, the remaining structure follows as a mathematical consequence.

### Queueing Rigor (Planned, No Axiom Creep)

Queueing behavior is treated as a **derived layer** from existing locality, unitarity, and continuity, not as a new microscopic axiom.

Planned additions are formal definitions and theorems plus stricter transport-function inequalities, with an explicit non-emptiness gate to ensure the admissible operator class remains viable.

Implementation plan: [QUEUEING_RIGOR_PLAN.md](QUEUEING_RIGOR_PLAN.md).

### The Central Theme: Information Flow â†’ Spacetime Structure

As you read, keep this chain in mind:

```
Information at node (Ïˆ_v)
    â†“
Buffering density (Ï = |Ïˆ|Â²)
    â†“
Confinement = reduced propagation speed
    â†“
Effective geometric delay (latency)
    â†“
Spacetime curvature (Einstein equation)
    â†“
Gravitational effects (mass appears)
```

**Key insight:** You never postulate mass. It emerges from how information gets buffered/trapped at nodes. A node with high $\rho$ (densely packed information) acts as a gravitational sourceâ€”not because we added a "mass field," but because the information density, when projected to spacetime, IS the energy density.

This is why:
- **Black holes are resolvable:** The information is still there, just maximally buffered
- **Black hole thermodynamics works:** Hawking radiation is the gradual release of buffered information
- **Energy is conserved:** Energy conservation is rooted in information conservation (unitary evolution)
- **Dark matter and dark energy exist:** They're different manifestations of buffer dynamics at cosmological scales

---

## Executive Summary

UniNet is a **discrete-to-continuum framework** for quantum gravity that:

1. **Starts with minimal axioms:** an undirected graph $G=(V,E)$, a unitary and graph-local transfer operator $U$, node buffering density $\rho(v,n)$, and **chiral decomposition** of internal degrees of freedom into left/right sectors.

2. **Derives geometric structures automatically:** latency â†’ causal order â†’ light cones â†’ time functions â†’ spacetime metric, all as theorems.

3. **Bridges microscopic and macroscopic physics:** buffering density Ï projects to energy density Tâ‚€â‚€; flux projects to momentum; Planck scale emerges as information saturation. **Crucially: information is the fundamental conserved quantity (unitary evolution); mass/energy emerges from information confinement.**

4. **Guarantees information preservation:** Unitary dynamics means no information is ever lostâ€”even in black holes (resolves the information paradox). Energy conservation is rooted in information conservation.

5. **Unifies QM and GR:** in the QM regime, latency is topological (fixed); in the GR regime, a field equation makes delays dynamic and adaptive to buffering.

6. **Explains cosmology:** dark energy (buffer relaxation), dark matter (long-wavelength modes + congestion), inflation (phase accumulation), all from a single buffering mechanism.

7. **Incorporates CP/chirality rigorously:** Chiral sector decomposition enables parity asymmetry, CP violation, and spin-statistics connection (fermion antisymmetry, boson symmetry) without additional assumptions.

8. **Explains the arrow of time:** Microscopic evolution (Tier 0) is fully reversible and bidirectional ($n \in \mathbb{Z}$); macroscopic time (Tier 4â€“6) becomes unidirectional and irreversible due to **information hiding during coarse-graining**. Entropy increase, black hole thermodynamics, and cosmological expansion all emerge from this information-loss transition.

**Key insight:** Fewer axioms, more emergence. No independent latency postulate; no separate edge-delay mechanism; no auxiliary fields; no separate arrow-of-time axiom. Time direction, CP violation, and all apparent irreversibility emerge from coarse-graining and chiral mixing in the transfer operator.

---

## Notation Guide

| Symbol | Meaning | Domain | Tier |
|--------|---------|--------|------|
| $G=(V,E)$ | Undirected graph | Substrate | 0 |
| $\|V\|,\|E\|$ | Node and edge counts | Graph measure | 0 |
| $n\in\mathbb{Z}$ | Tick (discrete time index) | Iteration parameter | 0 |
| $\psi_n \in \mathcal{H}$ | Global quantum state at tick $n$ | $\bigoplus_{v\in V}\mathbb{C}^d$ | 0 |
| $\psi_v(n) \in \mathbb{C}^d$ | Amplitude at node $v$ at tick $n$ | Internal d.o.f. | 0 |
| $\rho(v,n) = \|\psi_v(n)\|^2$ | Node buffering occupancy (dimensionless) | $[0,1]$ | 0 |
| $U:\mathcal{H}\to\mathcal{H}$ | Unitary transfer operator (propagator) | $U^\dagger U=I$ | 0 |
| $d_G(u,v)$ | Shortest-path graph distance | $\mathbb{Z}_{\geq0}$ | 1 |
| $\delta(u,v)$ | Effective latency (derived) | $=d_G(u,v)$ | 1 |
| $J_n(u\to v)$ | Edge flux (oriented) | $\mathbb{R}$ | 1 |
| $Q_n(R)$ | Interior information in region $R$ | $\mathbb{R}_{\geq0}$ | 1 |
| $\Phi_n(\partial R)$ | Net boundary flux across cut | $\mathbb{R}$ | 1 |
| $b_n(\partial R)$ | Boundary register (flux accumulator) | $\mathbb{R}$ | 1 |
| $\widetilde{Q}_n(R)$ | Closed regional total $Q_n+b_n$ | $\mathbb{R}_{\geq0}$ | 1 |
| $X=V\times\mathbb{Z}$ | Event set | Discrete spacetime points | 1 |
| $\prec$ | Precedence/causal relation | Partial order on $X$ | 2 |
| $J^+(x)$ | Causal future of event $x$ | $\subset X$ | 2 |
| $J^-(x)$ | Causal past of event $x$ | $\subset X$ | 2 |
| $E^+(x)$ | Horismos (light-cone boundary) | $= J^+(x) \setminus I^+(x)$ | 2 |
| $t_{\mathrm{obs}}(v,n)$ | Observer time (volume-based) | $\mathbb{R}_{\geq0}$ | 3 |
| $\tau(x,y)$ | Time separation (Lorentzian metric core) | $\mathbb{R}_{\geq0}$ | 3 |
| $\Pi_v:\mathcal{H}\to\mathbb{C}^{p+q}$ | Linear projection of amplitudes to Minkowski | Embedding | 4 |
| $x_n(v)\in\mathbb{C}^{p+q}$ | Projected Minkowski coordinate | Spacetime point | 4 |
| $\eta = \mathrm{diag}(-I_p,+I_q)$ | Minkowski metric | Indefinite signature | 4 |
| $\Delta\tau_n(v)$ | Proper-time increment along worldline | $\mathbb{R}_{\geq0}$ | 4 |
| $\mathcal{E}(e;\rho,J)$ | Effort functional (transport cost) | $\mathbb{R}_{\geq0}$ | 5 |
| $\mathcal{S}[\tau,\rho,J]$ | Total action (geometric + source) | $\mathbb{R}$ | 5 |
| $\mathrm{Curv}[\tau]$ | Discrete curvature functional | Via $\tau$ variation | 5 |
| $\kappa$ | Einstein coupling constant | $8\pi G/c^4$ | 5 |
| $\ell_{\mathrm{P}}$ | Planck length | $\sqrt{\hbar G/c^3}$ | 6 |
| $t_{\mathrm{P}}$ | Planck time | $\sqrt{\hbar G/c^5}$ | 6 |
| $c$ | Lightspeed | $\ell_e/\Delta t$ | 6 |
| $\Lambda_{\mathrm{proj}}$ | Buffering-to-energy-density projection coupling | $\sim c^7/(\hbar G^2)$ | 6 |

---

## Core Axioms (Tier 0: Microscopic Foundation)

These are the only unfalsifiable assumptions of the microscopic substrate (Tier 0).  
Tier 4â€“6 introduces explicit bridge axioms for mapping to physical spacetime units/observables.

### Axiom 0.1 â€” Graph Substrate
Let $G=(V,E)$ be a finite, undirected, connected simple graph (no multi-edges, no loops).

**Intuition:** The graph encodes network/lattice topology. It is the fabric on which information propagates.

**Role:** Defines positions and adjacency. Causal order will emerge from graph distance.

---

### Axiom 0.2 â€” Tick Parameter
There exists a discrete global parameter $n \in \mathbb{Z}$ called tick time, with step size $\Delta t$ (to be identified with Planck time $t_{\mathrm{P}}$ in physical units).

**Intuition:** Iteration index, not (yet) physical time. Physical time emerges from causal order.

**Role:** Parameterizes evolution steps. Allows time-sliced descriptions.

---

### Axiom 0.3 â€” Hilbert Space and States
Define the global state space as
\[
\mathcal{H} := \bigoplus_{v \in V} \mathbb{C}^d
\]
where $d$ is the internal (spin/coin) degrees of freedom per node. A state at tick $n$ is $\psi_n \in \mathcal{H}$.

**Intuition:** Local Hilbert spaces at each node; global state is their direct sum. Standard for quantum walks.

**Role:** Supports unitary evolution and buffering. Enables interference.

**Literature:** Aharonov et al. (1993), Ambainis et al. (2001) on quantum walk Hilbert spaces.

---

### Axiom 0.4 â€” Unitary Evolution
There exists a unitary operator $U: \mathcal{H} \to \mathcal{H}$ with $U^\dagger U = I$, such that
\[
\boxed{\; \psi_{n+1} = U \psi_n. \;}
\]

**Intuition:** Reversible, norm-preserving dynamics. Standard in quantum mechanics.

**Role:** Preserves probability mass and phase information. Enables causal structure.

**Conserved quantity:** $\|\psi_n\| = \|\psi_0\|$ for all $n$.

**Literature:** Standard postulate in quantum mechanics and quantum walks.

---

### Axiom 0.5 â€” Graph Locality of Transfer
The unitary $U$ is graph-local: it decomposes as $U = S \circ C$ where

- $C = \bigoplus_{v \in V} C_v$ acts independently on each node's internal d.o.f.,
- $S$ only couples adjacent nodes (or internal d.o.f. on the same node).

Equivalently: in one evolution step, amplitude at node $u$ can reach node $v$ **only if** $\{u, v\} \in E$ or $u = v$.

**Intuition:** Information cannot "teleport"; it propagates along graph edges. Standard locality principle.

**Role:** Fundamental to deriving latency and causal order. **Removing this breaks everything above it.**

**Ablation:** Non-local $U$ â†’ instantaneous influence â†’ no meaningful causal structure.

**Literature:** Quantum walk locality (Aharonov et al., Ambainis et al.); discrete quantum mechanics.

---

### Axiom 0.6 â€” Node Buffering
Each node $v$ at tick $n$ retains a **buffering measure**:
\[
\rho(v, n) := \|\psi_v(n)\|^2.
\]

**Intuition:** Information can pile up (congest) at nodes via interference. Buffering measures confinement vs. spreading.

**Role:** 
- Microscopic: drives confinement and interference patterns
- Macroscopic: projects to energy density $T_{00}$ in spacetime
- Cosmological: long-wavelength modes â†’ dark matter; relaxation â†’ dark energy

**Conserved quantity:** $\sum_{v \in V} \rho(v,n) = 1$ (probability mass).

**Symmetry:** Preserved under graph isomorphisms and relabelings (gauge invariance).

---

### Axiom 0.7 â€” Chiral Decomposition of Internal Degrees of Freedom

At each node $v$, the internal Hilbert space decomposes into left-handed and right-handed chiral sectors:
$$\mathcal{H}_v = \mathcal{H}_v^L \oplus \mathcal{H}_v^R,$$
where each sector has dimension at least 1.

Define the **chirality operator** $\mathcal{X}_v$ acting on $\mathcal{H}_v$ via:
$$\mathcal{X}_v = \begin{pmatrix} +I_L & 0 \ 0 & -I_R \end{pmatrix},$$
where $I_L, I_R$ are identity operators on their respective sectors (eigenvalues $\pm 1$).

**Intuition:** Chiral decomposition is fundamental to the weak interactions and spin-statistics. Left and right sectors couple *differently* to geometry and projection, breaking parity at the microscopic level.

**Role:** 
- Allows CP violation to emerge naturally (paired chiral sectors can have inequivalent spectra)
- Enables spin-statistics connection (fermions antisymmetric under sector exchange)
- Restricts gauge group structure (chiral anomalies impose consistency conditions)

**Literature:** Weyl spinors (chiral fermions); weak interaction parity violation (Lee & Yang 1956); chiral anomalies (Adler-Bell-Jackiw).

---

## Derived Structures (Tiers 1â€“3: Geometric Emergence)

**Philosophy:** Every object in Tier 1â€“3 below is a theorem proved from Axioms 0.1â€“0.7. No additional axioms are introduced in this section.

---

### Tier 1: Graph Distance Latency

#### Lemma 1.1 â€” Reachability via Graph Distance
For events $(u, n), (v, m) \in V \times \mathbb{Z}$, information at $u$ at tick $n$ can influence $v$ by tick $m$ only if
\[
m \geq n + d_G(u, v),
\]
where $d_G(u,v)$ is the shortest-path distance in $G$.

**Proof:** By Axiom 0.5 (graph locality), each tick extends reachable zone by â‰¤1 hop. Reaching distance $d$ requires â‰¥ $d$ ticks. âˆŽ

**Ablation:** Remove locality â†’ conclusion fails; reachability becomes instantaneous or unbounded.

---

#### Definition 1.1 â€” Effective Latency
Define the **effective latency** as:
\[
\boxed{\; \delta(u, v) := d_G(u, v). \;}
\]

**Intuition:** The minimum time for influence to propagate between nodes is the graph distance.

**Key point:** This is **not a new axiom**. It is a direct consequence of Axiom 0.5.

**Warning:** Never postulate separate "edge delays" $\tau_e$; they are redundant and break the framework.

---

#### Lemma 1.2 â€” Metric Properties of Latency
The derived latency satisfies:
1. **Symmetry:** $\delta(u,v) = \delta(v,u)$
2. **Triangle inequality:** $\delta(u,w) \leq \delta(u,v) + \delta(v,w)$
3. **Additivity on paths:** $\delta(u,w) = d_G(u,w) = \sum_{\text{edges on path}} 1$

**Proof:** Standard graph theory (shortest paths). âˆŽ

**Interpretation:** Latency is a true metric and inherits all properties of graph distance.

---

#### Definition 1.2 â€” Local Conservation / Continuity
For an information density $\rho_n(v) : V \to \mathbb{R}_{\geq0}$, define oriented edge flux $J_n(u \to v) \in \mathbb{R}$ with $J_n(u \to v) = -J_n(v \to u)$.

Define **local conservation** by the discrete continuity equation:
\[
\rho_{n+1}(v) - \rho_n(v) + \sum_{u \sim v} J_n(v \to u) = 0. \quad \text{(LC)}
\]

**Existence statement:** Axiom 0.4 gives global conservation
$\sum_v \rho_{n+1}(v)=\sum_v \rho_n(v)$, hence
$\sum_v\left[\rho_{n+1}(v)-\rho_n(v)\right]=0$.
On a connected finite graph, this guarantees existence of an antisymmetric edge flux $J_n$ satisfying (LC)
(non-unique up to divergence-free gauge freedom).

**Intuition:** Information at a node changes only by net flux across its boundary.

**Comparison to GR:** This is the discrete analogue of $\nabla_a T^{ab} = 0$ (stress-energy conservation).

**Literature:** Discrete continuity equations; Benamouâ€“Brenier optimal transport.

---

#### Theorem 1.1 â€” Discrete Gauss/Stokes: Bulk = Boundary
For any region $R \subseteq V$, define:
- **Interior sum:** $Q_n(R) := \sum_{v \in R} \rho_n(v)$
- **Boundary flux:** $\Phi_n(\partial R) := \sum_{\substack{u \in R, v \notin R \\ \{u,v\} \in E}} J_n(u \to v)$

Then (LC) and antisymmetry imply:
\[
\boxed{\; Q_{n+1}(R) - Q_n(R) = -\Phi_n(\partial R). \quad \text{(GB)} \;}
\]

**Proof:** Sum (LC) over all $v \in R$; internal fluxes cancel by antisymmetry; only cut-edges contribute. âˆŽ

**Interpretation:** Conservation = bulk change balanced by boundary flux. This is the flux-first viewpoint of stress-energy in GR.

**Literature:** Regge calculus, discrete gravity, finite-element methods.

---

#### Definition 1.3 â€” Boundary Register (Quasi-Local Closure)
For each region $R \subseteq V$, define a boundary register $b_n(\partial R)$ by
\[
b_{n+1}(\partial R) = b_n(\partial R) + \Phi_n(\partial R).
\]

Define the closed regional quantity
\[
\widetilde{Q}_n(R) := Q_n(R) + b_n(\partial R).
\]

---

#### Corollary 1.1 â€” Exact Closure with Boundary Bookkeeping
Under Theorem 1.1,
\[
\widetilde{Q}_{n+1}(R) = \widetilde{Q}_n(R) \quad \forall n.
\]

**Proof:** From (GB), $Q_{n+1}-Q_n=-\Phi_n$ and $b_{n+1}-b_n=+\Phi_n$; summing gives zero net change. âˆŽ

**Interpretation:** For bounded regions, conservation is exact only after boundary exchange is explicitly tracked.

---

#### Definition 1.4 â€” Horizon-Like Cut (Quasi-Local, Minimal Sense)
A cut $\partial R$ is **horizon-like** on a tick interval $I \subseteq \mathbb{Z}$ if interior bookkeeping alone is not closed on $I$, i.e.
\[
\exists n \in I \text{ such that } \Phi_n(\partial R) \neq 0.
\]

Equivalently, boundary data is required to close conservation on $R$.

---

#### Definition 1.5 â€” Boundary Slack and Leakiness
- **Boundary slack at tick $n$:** constraints permit $\Phi_n(\partial R) \neq 0$.
- **Leaky (at tick $n$):** $\Phi_n(\partial R) \neq 0$.

---

#### Theorem 1.2 â€” Leaky-Boundary Criterion
Assume Definition 1.2 (LC) and Theorem 1.1 (GB). For any region $R \subseteq V$ and tick $n$:

1. \(Q_{n+1}(R)=Q_n(R)\) **iff** \(\Phi_n(\partial R)=0\).
2. If \(\Phi_n(\partial R)\neq 0\), the region exchanges information with its exterior (leaky at tick \(n\)).
3. Even in the leaky case, \(\widetilde{Q}_n(R)=Q_n(R)+b_n(\partial R)\) remains exactly conserved.

**Proof:** Immediate from (GB) and Corollary 1.1. âˆŽ

**Consequence for later tiers:** This provides a rigorous quasi-local mechanism for horizon-like boundaries with controlled leakage, without assuming teleological event horizons.

---


#### Definition 1.6 - Queue Interpretation of Buffering

Define the local queue depth at node $v$ and tick $n$ by
\[
q_v(n) := \rho(v,n) = \|\psi_v(n)\|^2,\qquad 0\le q_v(n)\le 1.
\]
For any region $R\subseteq V$, define the regional queue depth
\[
Q_n(R)=\sum_{v\in R} q_v(n),\qquad 0\le Q_n(R)\le 1.
\]

**Interpretation:** Queue depth is continuous-valued occupancy on a discrete substrate.

---

#### Definition 1.7 - Queue Throughput Decomposition

For any region $R\subseteq V$, define boundary throughput components
\[
S_n(R):=\max\{\Phi_n(\partial R),0\}\quad\text{(service/outflow)},
\]
\[
A_n(R):=\max\{-\Phi_n(\partial R),0\}\quad\text{(arrival/inflow)}.
\]
Then Theorem 1.1 is equivalently
\[
Q_{n+1}(R)=Q_n(R)+A_n(R)-S_n(R).
\]

---

#### Theorem 1.3 - Queue Drift Identity and Low-Load Stability

Under Definition 1.2 and Theorem 1.1, for any region $R$ and tick interval $I$:

1. **Exact drift identity:**
\[
Q_{n+k}(R)-Q_n(R)=\sum_{j=0}^{k-1}\big(A_{n+j}(R)-S_{n+j}(R)\big).
\]

2. **Low-load stability condition:** If there exists $\varepsilon>0$ such that
\[
S_m(R)-A_m(R)\ge \varepsilon\quad\forall m\in I,
\]
then queue depth is non-increasing with strict negative drift until saturation at zero,
\[
Q_{n+k}(R)\le \max\{0,\,Q_n(R)-k\varepsilon\}.
\]

**Proof:** Item 1 follows by telescoping Theorem 1.1 with the definitions of $A_n,S_n$. Item 2 follows from uniform drift bound and non-negativity of $Q_n(R)$. QED.

---

#### Theorem 1.4 - Near-Saturation Trapping Bound (GR Regime)

Assume GR-regime effective latency law
\[
\delta_{\mathrm{GR,eff}}(u\to v)=\min_{\text{paths}}\int_{\text{path}}\big(1+\alpha\rho+\beta\,\mathrm{Curv}[\tau]\big)\,d\ell,
\]
with $\alpha,\beta>0$ (GR regime theorem), and let $H\subseteq V$ be a shell such that
\[
\rho(w,n)\ge 1-\eta\quad(0<\eta\ll1),\qquad \mathrm{Curv}[\tau](w,n)\ge K_{\min}\ge0\quad\forall w\in H.
\]
If any outward causal path from interior region $R_{\mathrm{in}}$ to exterior crosses shell length at least $L_H$, then
\[
\delta_{\mathrm{out}}\ge L_H\big(1+\alpha(1-\eta)+\beta K_{\min}\big).
\]

**Consequence:** Near-saturation shells induce large outbound dwell times; interior dynamics can remain unitary while outward release is boundary-layer controlled.

---

#### Corollary 1.2 - Boundary-Dominant Release (Closure vs Leak)

In the trapping regime of Theorem 1.4:

1. If $\Phi_n(\partial R_{\mathrm{in}})=0$, interior regional queue is exactly closed.
2. If $\Phi_n(\partial R_{\mathrm{in}})\neq0$ but small, net release rate is governed by boundary throughput, while interior remains long-lived and scrambling-dominated.

**Interpretation:** This formalizes "blocked interior + boundary-layer emission" without violating unitarity.

---
### Tier 2: Causal Order and Cones

#### Definition 2.1 â€” Precedence Relation
For events $x = (u, n), y = (v, m) \in X := V \times \mathbb{Z}$, define:
\[
\boxed{\; x \prec y \iff m \geq n + d_G(u, v). \;}
\]

**Intuition:** Event $x$ can causally influence $y$ if $y$ is at least $\delta(u,v)$ ticks in the future.

**Role:** Foundation for causal cone structures.

---

#### Lemma 2.1 â€” Partial Order
The relation $\prec$ is a **partial order** on $X$:
1. **Reflexive:** $(v,n) \prec (v,n)$ (since $d_G(v,v)=0$)
2. **Transitive:** $x \prec y$ and $y \prec z \implies x \prec z$ (by path additivity)
3. **Antisymmetric:** $x \prec y$ and $y \prec x \implies x = y$ (by causality)

**Proof:** Immediate from lattice metric properties. âˆŽ

**Literature:** Minguzzi (2018) on causality theory; causal sets.

---

#### Definition 2.2 â€” Causal Futures/Pasts and Horismos
For event $x = (u,n)$, define:
\[
J^+(x) := \{ y \in X : x \prec y \} \quad \text{(causal future)}
\]
\[
I^+(x) := \{ (v,m) : m > n + d_G(u,v) \} \quad \text{(strict timelike reachability)}
\]
\[
\boxed{\; E^+(x) := J^+(x) \setminus I^+(x) \quad \text{(horismos = light-cone boundary)} \;}
\]

**Intuition:** 
- $J^+$ = all causally reachable future events
- $I^+$ = events reachable with strict delay (timelike traversal)
- $E^+$ = "null boundary" = events reachable with exactly minimal delay

---

#### Lemma 2.2 â€” Horismos Characterization
An event $y = (v,m)$ lies on horismos $E^+(x)$ iff:
\[
m = n + d_G(u, v) \quad \text{(exactly the latency).}
\]

**Proof:** By definition of $I^+$ and $J^+$. âˆŽ

**Literature:** Horismos in Minguzzi (2018); null surface in differential geometry.

---

#### Proposition 2.1 â€” Closed Cone Structure
The collection $\{ J^+(x) : x \in X \}$ with partial order $\prec$ forms a **closed cone structure** in Minguzzi's sense (2018).

**Consequence:** All standard causality conditions apply:
- Time functions exist
- Chronology, causal continuity are well-defined
- Maximal causal curves play the role of geodesics

**Literature:** Minguzzi, *Causality theory for closed cone structures with applications* (Living Review in Relativity, 2018).

---

### Tier 3: Observer Time and Geometry

#### Definition 3.1 â€” Time Function
A function $t: X \to \mathbb{R}$ is a **time function** (or **causal function**) if:
\[
x \prec y \implies t(x) < t(y).
\]

**Intuition:** Time assignment that respects causal order. Plays the role of "coordinate time" in GR.

---

#### Lemma 3.1 â€” Existence of Time Functions
For any finite causal set with partial order $\prec$, there exists at least one time function.

**Proof (sketch):** Finite posets admit topological sorts; assign levels accordingly. âˆŽ

**Literature:** Gerochâ€“Hawking "time functions" in GR; computability in causal sets.

---

#### Definition 3.2 â€” Volume-Based Time
Define observer time via past-set cardinality:
\[
t_{\mathrm{obs}}(v, n) := |J^-((v,n))|,
\]
where $|J^-|$ counts events in the causal past.

**Intuition:** "How much has happened before this event?" Measures accumulated history.

**Justification:** If $(u,n) \prec (v,m)$, then $J^-(u,n) \subseteq J^-(v,m)$, so $t_{\mathrm{obs}}$ is monotone increasing along causal curves. âœ“

---

#### Definition 3.3 â€” Time Separation (Lorentzian Metric Core)
Define the **time separation function** between events:
\[
\tau(x, y) := \max_{\text{causal curves } \gamma : x \to y} \int_\gamma \mathrm{d\ell},
\]
where $\mathrm{d\ell}$ is a suitably defined causal-length element.

**Intuition:** Maximum proper time along causal curves. In GR, this is the Lorentzian distance.

**Role:** The time separation $\tau$ is the **metric core** of Lorentzian length spaces (Kunzingerâ€“SÃ¤mann); curvature is encoded via convexity/concavity properties of $\tau$.

**Literature:** Kunzinger & SÃ¤mann (2018) *Lorentzian length spaces*; Beranâ€“Kunzingerâ€“Rott (2021).

---

#### Subsection 3.4 â€” Arrow of Time: Reversibility at Tier 0 â†’ Irreversibility at Tier 4â€“6

#### Definition 3.4 â€” Coarse-Graining Observation Map
Let
\[
\Phi_{\mathrm{cg}}:\mathcal{H}\to\mathcal{M}
\]
be the observational map that keeps macroscopic observables (for example $\rho(v,n)=\|\psi_v(n)\|^2$, coarse flux summaries, and projected coordinates) while discarding phase-resolved microscopic data. In general, $\Phi_{\mathrm{cg}}$ is non-injective.

---

#### Theorem 3.2 â€” Emergent Arrow from Non-Injective Observation
Assume Axiom 0.4 (unitarity), Definitions 3.1â€“3.2 (observer-time construction), and Definition 3.4 (coarse-graining map). For
\[
m_n:=\Phi_{\mathrm{cg}}(U^n\psi_0),
\]
the following hold:

1. **Microscopic reversibility (Tier 0):**
\[
\psi_{n+1}=U\psi_n,\qquad \psi_n=U^\dagger\psi_{n+1}.
\]

2. **Macroscopic irreversibility (observational):**
if $\Phi_{\mathrm{cg}}$ is non-injective, $m_n$ does not uniquely determine $\psi_n$, hence there is no unique inverse map $m_n\mapsto m_{n-1}$ in general.

3. **Arrow statement:**
along causal precedence where $t_{\mathrm{obs}}$ is monotone (Definition 3.2), observers restricted to $m_n$ recover an effective forward-only history with entropy-production interpretation at coarse scale.

Therefore, the arrow of time is not a Tier-0 axiom; it is an emergent consequence of information hiding at the observation layer.

**Proof sketch:** Item 1 is immediate from unitarity. Item 2 follows from non-injectivity of $\Phi_{\mathrm{cg}}$: many microscopic states share the same macrostate. Item 3 combines this information-loss asymmetry with monotonic observer-time construction. CP/T-asymmetry cross-reference hints relevant to sector interpretation: neutral-kaon CP violation (Christenson et al., 1964), Sakharov conditions linking CP violation plus nonequilibrium to matter asymmetry (Sakharov, 1967), and direct T-violation observation in $B$ mesons (BaBar, 2012).

---

#### Corollary 3.1 â€” QM Sector Consequence (Kinematic Arrow Only)
In the QM regime (Section "QM Regime: Static Topological Latency"), latency remains
\[
\delta_{\mathrm{QM}}(u,v)=d_G(u,v),
\]
independent of buffering. Hence no additional microscopic time-direction postulate is introduced in QM; the observed arrow is entirely from coarse-graining/measurement interface.

---

#### Corollary 3.2 â€” GR Sector Consequence (Strengthened Operational Arrow)
In the GR regime, adaptive latency and queue constraints (`R9`, `R10`) plus Theorem 1.4 imply stronger one-way operational behavior in near-saturation regions: long dwell/trapping times with boundary-dominant release. This sharpens the observable arrow without violating Tier-0 reversibility.

---

#### Corollary 3.3 â€” SM Sector Consequence (CP as Modifier, Not Origin)
Requirement `R6` (CP non-commutation metric) constrains asymmetry channels in flavor/chiral observables, but does not define the thermodynamic arrow by itself. CP violation is a sector-level asymmetry modifier on top of Theorem 3.2, not the foundational source of irreversibility.

---

**Literature:** Zurek *Decoherence and the transition from quantum to classical* (Rev. Mod. Phys. 2003); Ellis *Issues in the Philosophy of Cosmology* (2011); Sorkin on causal sets and emergence of spacetime; Christenson et al. (1964) neutral-kaon CP violation; Sakharov (1967) baryogenesis conditions; BaBar Collaboration (2012) direct T-reversal violation.

---

## Requirements on Transfer Operator U

### R1: Graph Locality (Axiom 0.5)
$U = S \circ C$ where $C$ acts node-wise and $S$ only couples adjacent nodes.

**Why:** Enables causal structure. Removes it â†’ causality collapses.

---

### R2: Unitarity (Axiom 0.4)
$U^\dagger U = I$ (reversible, norm-preserving).

**Why:** Preserves unitarity and information. Enables Tier 1â€“3 derivations.

**Conserved quantity:** $\|\psi_n\| = \text{const}$.

---

### R3: Consistency with Buffering
The induced dynamics on $\rho_n(v) = \|\psi_v(n)\|^2$ must admit an antisymmetric edge flux
$J_n$ such that Definition 1.2 holds:
\[
\rho_{n+1}(v) - \rho_n(v) + \sum_{u \sim v} J_n(v \to u) = 0.
\]

**Why:** Ensures stress-energy is locally conserved, matching GR axiom.

**Automatic:** For graph-local unitary $U$, this follows from norm conservation plus connected-graph flow decomposition
(flux representation is not unique).

---

### R4: No Phenomenological Edge Delays
Do **not** add independent "edge latencies" $\tau_e$ on top of $U$. Latency is derived from locality (Lemma 1.1).

**Why:** Redundant, over-constrains dynamics, breaks equivalence between $d_G$ and causal order.

---

### R5: Chiral Structure Preservation (Axiom 0.7)
The coin operator $C_v$ at each node must respect the chiral decomposition:
\[
C_v = \begin{pmatrix} C_v^{LL} & C_v^{LR} \ C_v^{RL} & C_v^{RR} \end{pmatrix}
\]
where $C_v^{LL}, C_v^{RR}$ are operations within each chiral sector, and $C_v^{LR}, C_v^{RL}$ are off-diagonal couplings between sectors (chiral mixing).

Since $C_v$ is unitary, block components must satisfy:
\[
\begin{aligned}
(C_v^{LL})^\dagger C_v^{LL} + (C_v^{RL})^\dagger C_v^{RL} &= I_L,\
(C_v^{LR})^\dagger C_v^{LR} + (C_v^{RR})^\dagger C_v^{RR} &= I_R,\
(C_v^{LL})^\dagger C_v^{LR} + (C_v^{RL})^\dagger C_v^{RR} &= 0.
\end{aligned}
\]
These identities are hard algebraic constraints on admissible transfer blocks.

**Key constraint:** Define the **chirality violation amplitude**:
\[
\epsilon_{\text{mix}}(v) := \frac{\|C_v^{LR}\|_{\text{op}} + \|C_v^{RL}\|_{\text{op}}}{\|C_v\|_{\text{op}}},
\]
where $\|\cdot\|_{\text{op}}$ is the operator norm. Then:
- **Chirality-conserving regime:** $\epsilon_{\text{mix}} \approx 0$ (parity-respecting)
- **Chiral-mixing regime:** $\epsilon_{\text{mix}} \sim \text{small but nonzero}$ (parity violation)
- **Anomalous regime:** $\epsilon_{\text{mix}} \sim O(1)$ (strong sector dynamics)

Because $C_v$ is unitary, $\|C_v\|_{\text{op}}=1$, so
\[
\epsilon_{\text{mix}}(v)=\|C_v^{LR}\|_{\text{op}}+\|C_v^{RL}\|_{\text{op}},\qquad 0\le \epsilon_{\text{mix}}(v)\le 2.
\]
For physically admissible weak-sector behavior, require
\[
\epsilon_{\text{mix}}(v)\le \epsilon_{\text{mix}}^{\max}\ll 1 \quad \forall v.
\]

**Why:** Enforces that chiral sectors couple differently to geometry/projection, enabling parity asymmetry, CP violation, and gauge anomaly cancellation.

**Literature:** Weak interaction parity breaking (Lee & Yang 1956); chiral anomalies (Adler-Bell-Jackiw 1969); GIM mechanism (Glashow-Iliopoulos-Maiani 1970).

---

### R6: CP Symmetry or Violation (Axiom 0.7 Consequence)
For each periodic mode class $\Psi_{\alpha}$, define the **CP involution**:
\[
\mathsf{CP}(\Psi_\alpha^L) = e^{i\delta_\alpha} \Psi_\alpha^R,
\]
with
\[
\mathsf{CP}(\Psi_\alpha^R) = e^{-i\delta_\alpha} \Psi_\alpha^L,\qquad \delta_\alpha\in\mathbb{R}.
\]
This keeps $\mathsf{CP}$ norm-preserving on mode pairs.

Define the CP-breaking strength
\[
\epsilon_{\text{CP}} := \frac{\|[\mathsf{CP},U]\|_{\text{op}}}{2\|U\|_{\text{op}}}
= \frac{1}{2}\|[\mathsf{CP},U]\|_{\text{op}},
\]
using $\|U\|_{\text{op}}=1$.

**CP Symmetry:** $\epsilon_{\text{CP}}=0$.

**CP Violation:** $\epsilon_{\text{CP}}>0$ (small in SM-like regime). Mode-dependent real phases $\delta_\alpha$ and chiral mixing feed the non-commutation.

**Phenomenological anchor:** Kaon mixing parameter $\epsilon_K \sim 2.2 \times 10^{-3}$ (PDG 2023).

**Why:** Narrows transfer operator space to experimentally viable regime (CP violation ~0.1%).

---

### R7: Spin-Statistics Connection (Axiom 0.7 Consequence)
For half-integer spin (fermionic modes), combined wavefunctions must be **antisymmetric** under particle exchange:
\[
\Psi_{\alpha\beta}^{\text{fermi}} = -\Psi_{\beta\alpha}^{\text{fermi}}.
\]

For integer spin (bosonic modes), **symmetry** is required:
\[
\Psi_{\alpha\beta}^{\text{bose}} = +\Psi_{\beta\alpha}^{\text{bose}}.
\]

**Why:** Enforces Pauli exclusion and Bose-Einstein condensation. Follows from spin-statistics theorem (Weinberg-Haag-Lopuszanski-Sohnius).

**Experimental bound:** VIP-2 experiment: Pauli exclusion violation probability < $10^{-29}$ (Di Domenico et al. 2018).

---

### R8: Quantitative Admissible Window for Transfer Operator
Define global diagnostics:
\[
\bar{\epsilon}_{\text{mix}} := \frac{1}{|V|}\sum_{v\in V}\epsilon_{\text{mix}}(v),\qquad
\epsilon_{\text{CP}} := \frac{1}{2}\|[\mathsf{CP},U]\|_{\text{op}}.
\]

For a constrained, SM-like operator class require:
\[
0 < \bar{\epsilon}_{\text{mix}} \le \epsilon_{\text{mix}}^{\max}\ll 1,\qquad
0 < \epsilon_{\text{CP}} \le \epsilon_{\text{CP}}^{\max}\ll 1.
\]

Additionally impose spatial regularity of chiral mixing:
\[
\max_{u\sim v}\left|\epsilon_{\text{mix}}(u)-\epsilon_{\text{mix}}(v)\right| \le L_{\text{mix}}.
\]

**Why:** Excludes both trivial parity-symmetric operators ($\bar{\epsilon}_{\text{mix}}=0$) and strongly mixed/non-perturbative operators ($O(1)$), sharply reducing admissible $U$.

---


### R9: Queue-Response Monotonicity in Effective Transport (GR Regime)

For admissible effective transport laws in the GR regime, require monotone slowdown with buffering and curvature:
\[
\partial_{\rho}\,\tau_{\mathrm{eff}}\ge0,\qquad
\partial_{\mathrm{Curv}}\,\tau_{\mathrm{eff}}\ge0.
\]
Additionally, enforce baseline dominance
\[
\tau_{\mathrm{eff}}(u\to v)\ge d_G(u,v).
\]

**Why:** Encodes backpressure as a constitutive inequality without introducing new microscopic axioms.

---

### R10: Saturation Throughput Suppression and Regularity

Near occupancy saturation, outward throughput across a horizon-like cut must be suppressed in a controlled manner. Require a bound class of the form
\[
|\Phi_n(\partial R)|\le F(1-\rho_{\mathrm{shell}}(n)),\qquad F(x)\to0\ \text{as}\ x\to0^+,
\]
with regularity of $F$ sufficient for stable perturbation analysis (e.g., locally Lipschitz on $(0,1]$).

**Why:** Prevents unphysical finite outflow at full saturation while keeping the leaky branch mathematically well-posed.

---
## Symmetries and Conserved Properties

### Graph-Level Symmetries

#### S1: Graph Isomorphism Invariance (Gauge Symmetry)
The dynamics are invariant under graph relabelings (renumbering nodes/edges).

**Formal:** If $\varphi: G \to G'$ is an isomorphism, then
\[
\varphi_*( U_G(\psi) ) = U_{G'}( \varphi_*(\psi) ).
\]

**Intuition:** Physics is independent of labeling; labels are pure gauge.

**Literature:** Discrete gravity, causal sets (Sorkin); loop quantum gravity.

---

#### S2: Time-Translation Invariance (In QM Regime)
If the graph is periodic in spatial directions and $U$ is time-independent, then $U^n$ commutes at different ticks.

**Conserved:** Eigenvalues of $U$ (spectral properties).

---

#### S3: Locality-Preserving Symmetries
Transformations $U \to U' = V U V^\dagger$ where $V$ is also graph-local preserve causal structure.

**Example:** Local spin rotations $C_v \to U_v C_v U_v^\dagger$ at each node.

---

### Projected Spacetime Symmetries

#### S4: Pseudo-Unitary Invariance (Design Goal)
If the projection $\Pi_v: \mathcal{H} \to \mathbb{C}^{p,q}$ is chosen such that projected increment $\Delta x_n(v)$ evolves as
\[
\Delta x_{n+1}(v) = U_{\mathrm{proj}} \Delta x_n(v)
\]
with $U_{\mathrm{proj}}^\dagger \eta U_{\mathrm{proj}} = \eta$ (pseudo-unitary), then Lorentz invariants are preserved.

**Intuition:** Generalization of Lorentz symmetry to indefinite-metric spaces.

**Literature:** Pseudo-Riemannian geometry, causal structure in GR.

---

### Conserved Quantities

#### C1: Norm (Probability)
\[
\|\psi_n\|^2 = \|\psi_0\|^2 \quad \forall n.
\]

**Source:** Unitarity (Axiom 0.4).

---

#### C2: Information Entropy
For a basis decomposition $\psi_v(n) = \sum_j c_{v,j}(n) |j\rangle$, define:
\[
S_v(n) := -\sum_j |c_{v,j}(n)|^2 \log |c_{v,j}(n)|^2.
\]

**In reversible evolution:** Total entropy is conserved (no dissipation).

**In GR regime with buffer relaxation:** Entropy increases as buffer decays (Second Law from irreversible projection).

---

#### C3: Topological Charge (Model-Dependent)
If $G$ is periodic/lattice-like and $U$ has hidden symmetry, winding numbers or topological invariants may exist.

**Example:** In 2D quantum walks, quantized chirality.

**Literature:** Topological phases in quantum walks (Tarasinski et al., 2015).

---

## Lagrangian Formulation

### Action Principle

Observed geometric structures (particularly in GR regime) can be derived from an action principle:
\[
\mathcal{S}[\tau, \rho, J] := \mathcal{S}_{\mathrm{geo}}[\tau] + \kappa \, \mathcal{S}_{\mathrm{src}}[\rho, J].
\]

---

### Geometric Action

The geometric part encodes the "cost" of spatial distances and shifts in proper time:
\[
\mathcal{S}_{\mathrm{geo}}[\tau] := \sum_{n,u,v} \left( \tau(x_n(u), x_n(v)) \right)^2 + \text{(curvature terms)}.
\]

Equivalently, using a continuum limit, this becomes an Einsteinâ€“Hilbert action:
\[
\mathcal{S}_{\mathrm{geo}} = \frac{1}{16\pi G} \int \sqrt{-g} \, R \, \mathrm{d}^4 x.
\]

**Literature:** Regge calculus (deficit angles as curvature), causal dynamical triangulation.

---

### Source (Transport Effort) Action

The transport cost penalizes flux under continuity:
\[
\mathcal{S}_{\mathrm{src}}[\rho, J] := \sum_n \sum_{e \in E} \mathcal{L}\left( \rho_n(e), J_n(e) \right),
\]
where $\mathcal{L} \geq 0$ is a Lagrangian density (effort per edge).

**Example form (Benamouâ€“Brenier):**
\[
\mathcal{L} = \frac{J^2(e)}{2 \rho_e}, \quad \text{(kinetic energy / transport cost)}
\]

**Interpretation:** Highest flux with lowest density costs the most (high acceleration).

**Stress-energy coupling:**
\[
T^{\alpha\beta} \propto \frac{\delta \mathcal{S}_{\mathrm{src}}}{\delta \tau_{\alpha\beta}}.
\]

**Literature:** Benamou & Brenier (1991), Optimal Transport; Entropic gradient flows.

---

### Field Equation (Variational Condition)

Stationarity under variations $\delta \tau$:
\[
\frac{\delta \mathcal{S}}{\delta \tau} = 0 \quad \implies \quad \mathrm{Curv}[\tau] = \kappa \, \mathrm{StressEffort}[\rho, J].
\]

**Discrete form:**
\[
\mathrm{Curv}[\tau]_{ij} = \kappa \left( T_{\mathrm{src}} \right)_{ij},
\]
where $\mathrm{Curv}[\tau]_{ij}$ is a discrete curvature (e.g., deficit angle, holonomy).

**Comparison to GR:**
\[
G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu} \quad \text{(Einstein's equation)}.
\]

**Literature:** Regge calculus (Wheeler, 1961); discrete GR (Sorkin, 1975).

---

## Projection to Physical Spacetime (Tier 4â€“6)

Tier 4â€“6 is an interface layer: assumptions here calibrate the microscopic model to physical
spacetime observables/units. They are explicit bridge axioms, not claimed as Tier-0 theorems.

### Axiom 4.1 â€” Linear Projection of Amplitudes
For each node $v$, define a fixed linear map:
\[
\Pi_v: \mathcal{H} \to \mathbb{C}^{p,q}.
\]

The **projected Minkowski coordinate** of $v$ at tick $n$ is:
\[
x_n(v) := \Pi_v(\psi_n),
\]
where $\mathbb{C}^{p,q}$ is Minkowski space with signature $\eta = \mathrm{diag}(-I_p, +I_q)$.

**Intuition:** Embed quantum amplitudes into spacetime points. This is the model interface.

---

### Definition 4.1 â€” Worldline and Proper Time
For each vertex $v$, the projected worldline is:
\[
\gamma_v(n) := x_n(v) \in \mathbb{C}^{p,q}.
\]

The displaced increment per tick:
\[
\Delta x_n(v) := \Pi_v( (U - I) \psi_n ).
\]

If $\langle \Delta x_n(v), \Delta x_n(v) \rangle_\eta < 0$ (timelike), define proper time:
\[
\Delta \tau_n(v) := \sqrt{-\langle \Delta x_n(v), \Delta x_n(v) \rangle_\eta}.
\]

**Interpretation:** Standard Lorentzian metric length (RIemannian analogue for timelike segments).

---

### Axiom 4.2 â€” Buffering to Energy Projection
Node buffering density projects linearly to energy-density stress-tensor component:
\[
T_{00}(v, n) := \Lambda_{\mathrm{proj}} \cdot \rho(v, n),
\]
where $\Lambda_{\mathrm{proj}}$ is a universal coupling constant.

**Dimensions:** $[\Lambda_{\mathrm{proj}}] = \text{energy density}$ (since $\rho$ is dimensionless occupancy).

**Natural choice (Planck calibration):**
\[
\Lambda_{\mathrm{proj}} := \rho_{\mathrm{P}} = \frac{c^7}{\hbar G^2}.
\]

**Consequence:** High buffering ($\rho \to 1$) sources high energy density â†’ strong gravity.

---

### Axiom 4.3 â€” Lightspeed from Lattice Ratio
The maximum propagation speed (one hop per tick) is identified with lightspeed:
\[
c := \frac{\ell_e}{\Delta t}.
\]

**Model choice:** Set $\ell_e = \ell_{\mathrm{P}}$, $\Delta t = t_{\mathrm{P}}$.

**Automatic:** Then $c = \ell_{\mathrm{P}} / t_{\mathrm{P}}$ identically (by definition of Planck units).

---

### Theorem 4.1 â€” Buffering Couples to Geometry
High buffering density $\rho$ implies:
1. Enhanced transport effort â†’ longer effective latency
2. Field equation couples effort to curvature
3. Curvature deforms horismos and light cones
4. Deep potential wells emerge â†’ gravity

**Result:** Buffering IS the source of spacetime curvature. No separate mass field.

---

### Definition 4.2 â€” Node Occupancy Saturation Bound
Since $\rho(v,n)=\|\psi_v(n)\|^2$ is a normalized node occupancy:
\[
0 \le \rho(v,n) \le 1,\qquad \rho_{\max}=1.
\]

Projected energy density therefore obeys:
\[
0 \le T_{00}(v,n)=\Lambda_{\mathrm{proj}}\rho(v,n)\le \Lambda_{\mathrm{proj}}.
\]

**Intuition:** Microscopic saturation is occupancy concentration, not geometric area density.

**Consequence:** Near-saturation ($\rho\to1$) drives near-maximal local source term in the projected field equation.

---

## QM vs GR Regimes

### QM Regime: Static Topological Latency

#### Axiom: QM
- Unitary transfer $U$ with locality (Axioms 0.1â€“0.6)
- Node buffering $\rho(v,n)$
- **No field equation** coupling geometry to stress-energy

#### Theorem: QM Latency
Latency is **fixed and topological:**
\[
\delta_{\mathrm{QM}}(u,v) = d_G(u,v) \quad \text{(independent of } \rho \text{)}
\]

**Consequence:** Causal cones are **universal** and **time-independent**.

---

### GR Regime: Dynamic Latency from Field Equation

#### Axiom: GR
- Axioms 0.1â€“0.6 (graph, unitary, locality, buffering)
- Local conservation (Definition 1.2)
- Effort functional $\mathcal{E}(e; \rho, J) \geq 0$
- **Field equation:** $\mathrm{Curv}[\tau] = \kappa \, \mathrm{StressEffort}[\rho, J]$

#### Theorem: GR Latency (Adaptive)
Effective latency becomes dynamically coupled:
\[
\delta_{\mathrm{GR, eff}}(u \to v) = \min_{\text{paths}} \int_{\text{path}} \left( 1 + \alpha \rho + \beta \, \mathrm{Curv}[\tau] \right) \, \mathrm{d}\ell,
\]
where $\alpha, \beta > 0$ are coupling constants (determined by action principle).

**Intuition:** Signals slow down in high-$\rho$, high-curvature regions (Shapiro delay analogue).

**Consequence:** Causal cones **deform** in response to buffering.

---

## Dark Matter, Dark Energy, Inflation (Application to Cosmology)

*(Sketched; see UNINET_MERGED.md Section F for full details)*

### Dark Energy
**Mechanism:** Primordial buffering $\rho_{\max}$ relaxes via coupling decay $\rho(t) = \rho_{\max} \exp(-t/\tau_{\mathrm{relax}})$.

**Effective equation of state:**
\[
w \approx -1 + \frac{1}{3 H_0 \tau_{\mathrm{relax}}}.
\]

**Observable:** Evolving $w(z)$ in BAO, SNe, weak lensing.

---

### Dark Matter
**Mechanism:** Long-wavelength buffering modes ($\lambda \sim$ Mpc) with $w \approx 0$ (pressureless).

**Congestion feedback:** High $\rho_{\mathrm{DM}}$ creates additional buffering â†’ reduced propagation â†’ amplified clustering.

**Observable:** Matter power spectrum enhancement, $\sigma_8$; Lyman-$\alpha$ forest; galaxy cluster abundance.

---

### Inflation
**Mechanism:** Maximal phase accumulation $\Phi \to \Phi_{\max}$ drives exponential expansion $a \propto \exp(H_{\mathrm{inf}} t)$.

**Number of e-folds:**
\[
N_e \sim \log(\Phi_{\max} / \Phi_{\mathrm{initial}}) \approx 50â€“70.
\]

**Observable:** Scalar spectral index $n_s \approx 0.96$ (red-tilted); tensor-to-scalar ratio $r$; chiral asymmetry in CMB.

---

## Literature Cross-References

### Foundational: Quantum Walks
- Aharonov, Davidovich, Zagury (1993). "Quantum random walks." *PRL* 48:1494â€“1497.
- Ambainis, Bach, Nayak, Vishwanathan, Watrous (2001). "One-dimensional quantum walks with absorbing boundaries." *J. Comput. System Sci.* 69:562â€“592.
- Venegas-Andraca (2012). "Quantum walks for computer scientists." *Synth. Lect. Quantum Comput.* 1:1â€“149.

### Causality Theory
- Minguzzi, E. (2018). "Causality theory for closed cone structures with applications." *Living Reviews in Relativity* 21:3.
- Penrose, R. (1972). "Techniques of differential topology in relativity." SIAM.

### Synthetic Lorentzian Geometry
- Kunzinger, M., SÃ¤mann, C. (2018). "Lorentzian length spaces." *Annales Globales Analysi Geometriae* 54:399â€“447.
- Beran, T., Kunzinger, M., Rott, A. (2021). "Generalized Lorentzian length spaces." *Preprint arXiv:2107.02010*.
- Burtscher, A., GarcÃ­a-Heveling, L. (2021â€“2025). Time functions in Lorentzian length spaces without manifold assumptions. *Preprints*.

### Discrete Gravity & Regge Calculus
- Wheeler, J.A. (1962). Geometrodynamics. Academic Press.
- Regge, T. (1961). "General relativity without coordinates." *Nuovo Cimento* 19:558â€“571.
- Sorkin, R.D. (1975). "A combinatorial approach to the Dirac equation." *Preprint arXiv:1003.1091*.
- Corichi, A., Zapata, J.A. (2010). "From discrete to continuous general relativity." *Preprint arXiv:0905.1826*.

### Optimal Transport & Source Terms
- Benamou, J.-D., Brenier, Y. (1989). "A computational fluid mechanics solution to the Mongeâ€“Kantorovich mass transfer problem." *Numer. Math.* 84:375â€“393.
- Villani, C. (2003). "Topics in Optimal Transport." AMS.

### Black Hole Information
- Page, D.N. (1993). "Information in black hole radiation." *PRL* 71:3743â€“3746.
- Harlow, D. (2016). "The Ryuâ€“Takayanagi formula from quantum error correction." *Comm. Math. Phys.* 354:865â€“912.

### Cosmology & Dark Sectors
- Planck Collaboration (2018). "Planck 2018 results. VI. Cosmological parameters." *A&A* 641:A6.
- Hui, L., Joyce, A., Khoury, J., Steinhardt, P.J. (2021). "Fuzzy dark matter." *Phys. Rev. D* 95:043541.
- Maggiore, M., Mancarella, M. (2021). "Nonlocal infrared modifications of gravity: a review." *Preprint arXiv:2105.00461*.

---

## Quick-Reference Checklist

Before using this framework, ensure:

- [ ] Graph $G=(V,E)$ is finite and undirected
- [ ] Unitary $U$ is truly graph-local (not fully-connected)
- [ ] No separate edge delays; latency emerges from graph distance
- [ ] Buffering $\rho(v,n)$ represents local information concentration
- [ ] Local conservation (Def. 1.2) holds for any flux assignment
- [ ] Bounded-region conservation uses boundary bookkeeping $\widetilde{Q}_n(R)=Q_n(R)+b_n(\partial R)$ (Cor. 1.1)
- [ ] Leaky-boundary criterion is applied via $\Phi_n(\partial R)\neq 0$ (Thm. 1.2)
- [ ] Causal order $\prec$ is derived from latency (Def. 2.1)
- [ ] Time functions exist (Lemma 3.1) and time progression is causal
- [ ] Projection $\Pi$ maps amplitudes linearly to spacetime
- [ ] Energy density couples to buffering (Axiom 4.2)
- [ ] Field equation is variational (from action principle)
- [ ] **Chirality:** Internal d.o.f. decompose into $L/R$ sectors (Axiom 0.7)
- [ ] **Coin operator:** Respects chiral structure with measurable mixing parameter $\epsilon_{\text{mix}}(v)$ (R5)
- [ ] **CP symmetry/violation:** Quantified by $\epsilon_{\text{CP}}=\tfrac12\|[\mathsf{CP},U]\|_{\text{op}}$ with real chiral phases (R6)
- [ ] **Spin-statistics:** Fermionic modes antisymmetric, bosonic modes symmetric (R7)
- [ ] **Admissible $U$-window:** $\bar{\epsilon}_{\text{mix}},\epsilon_{\text{CP}}$ in weak-sector-compatible bounds and spatially regular (R8)

---

**End of Core Axioms Document**

*For detailed applications, proofs, and cosmological predictions, see UNINET_MERGED.md.*







---
## Tier 1A: Boundary Bandwidth, Effective Dimension, and Symmetry Capacity

### Definition 1A.1 — Boundary Bandwidth Function
For a nested family of regions $\{R_r\}$ in $G$ (e.g. graph balls of radius $r$), define the **boundary bandwidth**
$$
B(r) := |\partial R_r|,
$$
or, more generally, a capacity-weighted boundary throughput bound when edge weights or flux constraints are present.

---
### Definition 1A.2 — Effective Dimension from Bandwidth Growth
Define the **effective dimension** associated with boundary growth as
$$
d_{\mathrm{eff}} := 1 + \limsup_{r\to\infty} \frac{\log B(r)}{\log r}.
$$
**Interpretation:** dimension is the exponent governing how many independent information channels become available as a cut grows.

---
### Theorem 1A.1 — Boundary Growth Controls Volume Growth
Under mild regularity assumptions on $\{R_r\}$ (nestedness, bounded eccentricity), boundary-growth exponent and volume-growth exponent are linked: polynomial boundary growth with exponent $d_{\mathrm{eff}}-1$ implies polynomial volume growth with exponent $d_{\mathrm{eff}}$.

**Status:** proved (graph-theoretic; independent of SM assumptions).

---
### Definition 1A.3 — Boundary Observable Algebra
For a region $R$, define $\mathcal{O}(\partial R)$ as the algebra of observables accessible outside the cut (net fluxes, coarse-grained boundary registers, projected boundary variables).

---
### Definition 1A.4 — Boundary Redundancy Group
Define the **boundary redundancy group**
$$
\mathcal{G}(\partial R) := \{\text{internal transformations on } R \text{ leaving } \mathcal{O}(\partial R) \text{ invariant}\}.
$$
**Interpretation:** internal relabelings that do not affect boundary-observable information flow are physically redundant (gauge freedom).

---
### Theorem 1A.2 — Boundary Capacity Bounds Independent Conserved Flows
The number of independent conserved exchange modes detectable outside $R$ is bounded above by a function of the boundary bandwidth $B(r)$. In particular, no more than $O(B(r))$ linearly independent boundary-resolved flows can be simultaneously conserved.

**Status:** noether-like (requires full action–symmetry pipeline for promotion).

---
### Theorem 1A.3 — Goldilocks Window for Boundary Symmetry Viability
There exists a window of effective dimensions $d_{\mathrm{eff}}$ such that:
1. For $d_{\mathrm{eff}}$ too small, admissible boundary redundancy groups collapse to effectively abelian or trivial classes.
2. For $d_{\mathrm{eff}}$ too large, redundancy structures proliferate and destabilize under coarse-graining.
3. Within an intermediate window (empirically near $d_{\mathrm{eff}} \approx 3$), a small class of compact, low-rank boundary symmetries remains stable under locality, conservation, and coarse-graining constraints.

**Status:** deferred (explicit constructive witness families and full Noether promotion required).

---
### Corollary 1A.1 — Constraint (Not Derivation) on SM Gauge Structure
Boundary bandwidth scaling sharply constrains admissible internal boundary symmetries. Identification of the Standard Model gauge group $U(1) \times SU(2) \times SU(3)$ as a realized member of this constrained class remains a deferred result pending constructive derivation.

**Status:** deferred (see Proof Status Ledger PS-010).


---
## Tier 1B: Cut Interfaces, Gauge-as-Redundancy, and Emergent Field Limits

**Purpose (non-axiomatic):** This block extracts additional *derived* statements suggested by the boundary/cut viewpoint. No new Tier‑0 axioms are introduced. Each item is tagged by proof maturity following the project’s Noether governance.

### Definition 1B.1 — Cut-External Observational Equivalence
Fix a region $R\subseteq V$ and its boundary $\partial R$. Let $\mathcal{O}(\partial R)$ denote the algebra of observables accessible outside $R$ (e.g., boundary throughput summaries $\Phi_n(\partial R)$, boundary register $b_n(\partial R)$, and any declared coarse-grained boundary projections). Two interior microstates at tick $n$, denoted $\psi_n|_R$ and $\psi'_n|_R$, are **externally equivalent across the cut** if they induce identical boundary observables:
\[
\psi_n|_R \sim_{\partial R} \psi'_n|_R \iff \mathcal{O}(\partial R;\psi_n)=\mathcal{O}(\partial R;\psi'_n).
\]

---
### Theorem 1B.1 — Gauge Equivalence as Cut-Observable Equivalence
**Claim.** The relation $\sim_{\partial R}$ is an equivalence relation on interior microstates (reflexive, symmetric, transitive). The automorphisms of each equivalence class are precisely the **boundary redundancy transformations** ("gauge" in the cut sense): transformations acting on $R$ that preserve $\mathcal{O}(\partial R)$.

**Status:** proved (equivalence-relation construction; depends only on Definition 1B.1 and the definition of $\mathcal{O}(\partial R)$).

---
### Theorem 1B.2 — Universal Boundary Mediator Structure (Horizon/Boson Analogue)
**Claim.** For any horizon-like cut $\partial R$ (Definition 1.4), the exterior-facing effect of the interior dynamics is fully characterized by the boundary data $(\Phi_n(\partial R),\, b_n(\partial R))$ together with the chosen observation map $\Phi_{\mathrm{cg}}$ (Definition 3.4). In particular, the exterior cannot distinguish interior microstates within the same $\sim_{\partial R}$ class; it observes only a delayed, bandwidth-limited projection mediated by the boundary.

**Status:** proved (depends on Theorem 1.1 (GB), Corollary 1.1, Theorem 1.2, and Definition 3.4).

---
### Theorem 1B.3 — Boundary Rank Bound on Independent Conserved Charges
**Claim.** The number of independent conserved exchange modes/charges that can be resolved outside $R$ is bounded by a function of the boundary bandwidth $B(r)$ and (when defined) by the rank/size of the boundary redundancy group $\mathcal{G}(\partial R)$. Intuitively: independent conserved flows cannot exceed the number of independent boundary channels.

**Status:** noether-like (a full Noether promotion requires a frozen action, a continuous symmetry action, and explicit current/charge construction).

---
### Theorem 1B.4 — Low-Dimensional Abelianization (Boundary Symmetry Collapse)
**Claim.** If boundary bandwidth growth is too small (e.g., $d_{\mathrm{eff}}\le 2$ under Definition 1A.2 for a canonical exhaustion), then admissible boundary redundancy structures that act faithfully on boundary-resolved degrees of freedom collapse under coarse-graining to effectively abelian (commutative) classes.

**Status:** noether-like (requires formal stability/coarse-graining class and the action-to-charge pipeline for full promotion).

---
### Theorem 1B.5 — High-Dimensional Symmetry Proliferation Instability
**Claim.** If boundary bandwidth grows too rapidly (e.g., super-polynomial growth or $d_{\mathrm{eff}}\gg 3$), then boundary redundancy structures proliferate faster than coarse-graining can stabilize them, so no small, robust low-rank effective symmetry description persists at macroscopic scale.

**Status:** deferred (requires an explicit stability definition under coarse-graining and witness-family construction).

---
### Theorem 1B.6 — Dimensional Attractor (Bandwidth-Driven Fixed-Window Hypothesis)
**Claim.** Under repeated coarse-graining with stability constraints on boundary throughput, the effective dimension defined by boundary bandwidth (Definition 1A.2) flows toward a fixed window compatible with stable, low-rank non-abelian boundary redundancies.

**Status:** deferred (requires a formal renormalization/coarse-graining flow definition and stability criteria).

---
### Theorem 1B.7 — Field Limit as a Boundary Ensemble Average (Boltzmann Analogue)
**Claim.** In regimes where cuts are dense and individual boundary mediations cannot be resolved, effective classical/quantum fields arise as ensemble-averaged descriptions of boundary-mediated information transfer histories, analogous to Boltzmann/kinetic descriptions of molecular microdynamics.

**Status:** noether-like (requires an explicit ensemble measure on transfer histories and an observational equivalence specification).

---
## Tier 1C: Particle Modes as Boundary-Stabilized Standing Waves

### Theorem 1C.1 — Particle Modes as Horizon-Supported Standing Waves
**Claim.** In UniNet, any long-lived, particle-like excitation corresponds to a **standing or quasi-standing wave pattern** of the update dynamics, stabilized by a **horizon-like boundary (cut)** whose surface admits a symmetry group. The observable properties of the excitation are determined by the symmetry structure of this boundary and the allowed standing-wave modes it supports.

**Explanation (structural, non-axiomatic):**
1. Fundamental update dynamics are unitary, local, and wave-like.
2. Stability under iteration requires phase-coherent interference across multiple nodes.
3. Cut/boundary theorems imply that persistent modes must be supported by boundary-mediated balance.
4. Boundary symmetries discretize and stabilize admissible standing-wave patterns.

**Consequences:**
- Particle identity is not node-local.
- Localization is emergent and projection-dependent.
- Gauge and internal quantum numbers correspond to boundary symmetry labels.

**Status:** derived theorem.
---
``


---
## Literature Anchors for Boundary, Bandwidth, and Gauge-Redundancy Results
The following references provide established context and partial formal precedents for the Tier 1A–1B results. These are **conceptual anchors**, not claims of derivation equivalence.

### Gauge Symmetry as Redundancy / Boundary Structure
- C. Rovelli, *Gauge Is More Than Mathematical Redundancy*, PhilSci-Archive (2020). Emphasizes gauge as relational/boundary structure rather than surplus ontology. citeturn46search64
- H. Gomes, *Why Gauge? Conceptual Aspects of Gauge Theories*, PhD Thesis, Cambridge (2021). Detailed analysis of gauge as descriptive redundancy and boundary relevance. citeturn46search63
- J. Schwichtenberg, *Demystifying Gauge Symmetry*, arXiv:1901.10420. Gauge symmetry as redundancy clarified operationally. citeturn46search50

### Boundary Information and Holography
- G. ’t Hooft (1993); L. Susskind (1995). Original holographic principle: bulk information encoded on boundaries. citeturn46search56
- C. Fields, J.F. Glazebrook, A. Marciano, *The Physical Meaning of the Holographic Principle*, arXiv:2210.16021. Information-theoretic boundary encoding perspective. citeturn46search57

### Isoperimetric / Boundary Growth and Dimension
- F. Chung, *Discrete Isoperimetric Inequalities*, UCSD. Boundary size vs. volume growth in graphs. citeturn46search46
- Pittet & Saloff-Coste, *Isoperimetry, Volume Growth and Random Walks*, Cornell survey. Relates boundary growth to effective dimension. citeturn46search45

### Bulk–Boundary Mediation and Gauge Constraints
- I. Heemskerk, *Construction of Bulk Fields with Gauge Redundancy*, arXiv:1201.3666. Boundary constraints and non-locality from Gauss law. citeturn46search66

