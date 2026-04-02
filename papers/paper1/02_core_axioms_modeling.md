# Chapter 2 - Core Axioms and Modeling Layer

This chapter fixes the contract of the paper. The core axioms are the minimal substrate commitments. Modeling postulates and bridge postulates are useful, often necessary, and fully legitimate, but they are not allowed to masquerade as microscopic inevitabilities. The distinction is what keeps the manuscript auditable.

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

Taken together, the core says:
1. there is a graph,
2. labels do not matter,
3. updates are ordered,
4. one law family governs the substrate,
5. that law family is homogeneous,
6. transport is local,
7. information is not destroyed,
8. cuts are physically meaningful,
9. observation is boundary-limited,
10. persistent particle-like structure is standing-wave structure.

## 2.2 Modeling Postulates and Why They Are Separate
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
