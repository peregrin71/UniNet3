# Standing/Quasi-Standing Mode Existence in the Restricted UniNet Update Class

Date: 2026-04-02  
Status: `postulate` (proof concept with explicit witness-family; formal full-proof promotion pending)

Notation standard reference: `docs/40_governance/03_notation_units_standard.md`.

## 0. Reader Roadmap

This note is easiest to read in three passes:

1. Section 0A + L1-L2: read the minimal operator equations and verify no information loss with explicit delay structure.
2. L3: understand why loop topology ($\beta\ge1$) is the first nontrivial threshold for graph-supported standing families.
3. L3A + L4-L6: see explicit witnesses (two-node and one-cycle) and then extension by induction on cycle rank.

## 0A. Core Operator Equations Used in This Proof

From `docs_input/UNINET_CORE_AXIOMS.md` (AXIOM-7 and Theorem 3.2):

$$
\psi_{n+1}=U\psi_n,\quad U^\dagger U=I.
$$

Standing-mode form used in this note:

$$
U\phi=\lambda\phi,\quad |\lambda|=1,\quad \psi_n=\lambda^n\phi.
$$

Interpretation:

1. The first equation is the microscopic update rule.
2. The second equation is the simplest exact standing/eigenmode statement for a discrete unitary map.
3. "Quasi-standing" means a narrow superposition of nearby unit-modulus eigenmodes whose envelope stays approximately fixed over the claimed timescale.

## 1. Goal

Show that at least one admissible update function exists in the already-restricted UniNet class such that:

1. Information is not lost (unitary evolution).
2. Propagation remains local with explicit delay structure.
3. Dynamics supports at least one standing or quasi-standing wave mode on a graph with nontrivial cycle structure.

This is an existence result, not a uniqueness claim.

## 2. Restricted Operator Class (Input Constraints)

Define the admissible microscopic class:

$$
\mathcal{U}_{\mathrm{adm}}
=
\left\{
U=S\circ C
\;\middle|\;
\mathrm{R1,R2,R3,R5,R6,R8}
\right\}.
$$

Operational constraints:

1. `R1` (graph locality): one-hop transfer per tick.
2. `R2` (unitarity): $U^\dagger U=I$, so information norm is preserved.
3. `R3` (buffer-consistent continuity): induced $\rho(v,n)=|\psi_v(n)|^2$ admits discrete flux form.
4. `R5-R8` (SM-facing restrictions): chiral block structure plus bounded/nonzero $\bar{\epsilon}_{\mathrm{mix}}$ and $\epsilon_{\mathrm{CP}}$.

Delay discipline:

1. QM regime: $\delta_{\mathrm{QM}}(u,v)=d_G(u,v)$.
2. GR effective regime (coarse-grained): $\delta_{\mathrm{GR,eff}}(u,v)\ge d_G(u,v)$ with monotone slowdown (`R9`) and saturation regularity (`R10`).

Schrodinger-like interpretation (discrete-time reader note):

$$
\psi_{n+1}=U\psi_n,\quad U^\dagger U=I
$$

is the discrete analogue of unitary wave evolution. On a chosen quasienergy branch one may write

$$
U=e^{-iH_{\mathrm{eff}}},
$$

with Hermitian $H_{\mathrm{eff}}$ (branch-dependent logarithm). This is the precise sense in which the witness family is Schrodinger-like without introducing a separate continuum-time postulate.

## 3. Claim and Status

### Theorem E1 (Existence in Restricted Class)
Status: `postulate`

Let $G=(V,E)$ be finite and connected. If $G$ has at least one independent cycle,

$$
\beta := |E|-|V|+1 \ge 1,
$$

then there exists $U\in\mathcal{U}_{\mathrm{adm}}$ and nonzero mode data satisfying one of:

1. Exact standing eigenmode:

$$
U\phi=\lambda\phi,\quad |\lambda|=1,\quad \psi_n=\lambda^n\phi.
$$

2. Quasi-standing mode packet:

$$
\psi_n=\sum_{r\in\mathcal{R}} c_r\,\lambda_r^n\,\phi_r,\quad |\lambda_r|=1,
$$

with coefficients concentrated on a narrow spectral cluster so the spatial envelope is stable up to bounded beat modulation.

Additionally,

$$
\|U^n\phi\|=\|\phi\| \quad \forall n\in\mathbb{Z},
$$

so information norm is conserved exactly.

## 4. Proof Concept

### Lemma L1 (No Information Loss)
Status: `proved`

From `R2`, $U^\dagger U=I$. Hence:

$$
\|\psi_{n+1}\|^2
=
\langle U\psi_n,U\psi_n\rangle
=
\langle\psi_n,\psi_n\rangle.
$$

Therefore total information norm is conserved for all ticks $n$.

Why this matters: the standing/quasi-standing claim is about persistent mode structure. Without exact norm preservation, persistence could be mistaken for transient storage/decay.

Literature anchor:

1. Standard unitary postulate in quantum mechanics and the Schrodinger picture.
2. Stone theorem link between unitary evolution and self-adjoint generators (continuous-time analogue).
3. Discrete-time quantum walk formalism (Aharonov-Davidovich-Zagury; Ambainis et al.).

### Lemma L2 (Propagation Delay Structure)
Status: `proved` (QM scope), `postulate` (GR effective mapping scope)

From `R1`, amplitude moves at most one hop per tick. Therefore earliest-arrival delay obeys:

$$
n'-n \ge d_G(u,v).
$$

In QM regime this gives $\delta_{\mathrm{QM}}(u,v)=d_G(u,v)$.  
In GR effective regime, delays can increase but remain constrained by `R9-R10` through $\delta_{\mathrm{GR,eff}}(u,v)\ge d_G(u,v)$.

Why this matters: we are proving mode existence inside the accepted delay discipline, not by adding ad hoc edge-delay rules.

Literature anchor:

1. Finite-speed propagation and locality in discrete quantum-walk dynamics.
2. Causal-graph/shortest-path latency interpretation used in discrete spacetime and walk models.

### Lemma L3 (Cycle Prerequisite for Nontrivial Multi-Node Standing Patterns)
Status: `postulate`

Counter-propagating interference that closes on itself requires at least one cycle.  
Equivalent connected-graph condition:

$$
\beta\ge1 \iff |E|\ge|V|.
$$

Human-readable explanation:

1. If $\beta=0$, the graph is a tree. Between any two nodes there is only one simple path. Waves can still reflect from endpoints/cuts, but there is no independent closed loop to support circulation-phase closure.
2. If $\beta\ge1$, at least one simple cycle exists. Then there are two directed routes around the loop, and phase closure can be imposed around that loop:

$$
e^{ikL_{\mathrm{cyc}}}=1
\iff
k=\frac{2\pi m}{L_{\mathrm{cyc}}},
\quad
m\in\mathbb{Z}.
$$

This closure condition is exactly what produces robust standing/quasi-standing loop modes.

Clarification on the two-node case: a two-node standing pattern is possible as a boundary-reflection/Rabi-type oscillation on a single link, but it does not probe nontrivial cycle topology ($\beta=0$). That is why it is called degenerate here.

Literature anchor:

1. Spectral graph viewpoint: cycles create periodic phase constraints and nontrivial loop eigenmodes.
2. Quantum-graph wave mechanics: closed loops support quantized phase closure and standing patterns.

### Lemma L3A (Explicit Two-Node Degenerate Witness)
Status: `postulate`

Let $G_2$ have two nodes $a,b$ with one edge $\{a,b\}$, so $\beta=0$.  
Use basis states $|a,\chi\rangle,|b,\chi\rangle$ for $\chi\in\{L,R\}$.

Define graph-local shift:

$$
S|a,\chi\rangle=|b,\chi\rangle,\quad
S|b,\chi\rangle=|a,\chi\rangle.
$$

Take baseline local coins $C_a=C_b=I$, so $U_2=S\circ C=S$.

For each chirality $\chi$, define symmetric/antisymmetric node modes:

$$
\phi_{\chi,\pm}:=\frac{|a,\chi\rangle\pm|b,\chi\rangle}{\sqrt{2}}.
$$

Then

$$
U_2\phi_{\chi,\pm}=\pm\phi_{\chi,\pm},
$$

hence

$$
\psi_n=(\pm 1)^n\phi_{\chi,\pm}.
$$

Therefore the spatial envelope is fixed and node occupancies are constant:

$$
\rho(a,n)=\rho(b,n)=\frac12.
$$

So an exact standing pattern on two nodes exists.

Operator-summary line for this witness:

$$
U_2\phi_{\chi,\pm}=\lambda_{\pm}\phi_{\chi,\pm},\quad \lambda_{\pm}=\pm1,\quad \psi_n=\lambda_{\pm}^n\phi_{\chi,\pm}.
$$

Embedding note (restricted `R5-R8` window):

1. Add small block-unitary chiral-mixing/CP phases in $C_v$ so $0<\bar{\epsilon}_{\mathrm{mix}}\le\epsilon_{\mathrm{mix}}^{\max}\ll1$ and $0<\epsilon_{\mathrm{CP}}\le\epsilon_{\mathrm{CP}}^{\max}\ll1$.
2. $U_2$ remains local and unitary.
3. By spectral continuity under small unitary perturbations, the exact two-node standing modes deform to quasi-standing modes with small bounded envelope modulation.

This proves the two-node case is not merely assumed.

### Lemma L4 (Base Witness on One Cycle)
Status: `postulate`

Take $G=C_L$ (cycle length $L$) with local chiral space $\mathbb{C}^2$ and

$$
U_0=S\circ C_0,
$$

where $S$ is nearest-neighbor shift and $C_0$ is node-local unitary.  
For translationally uniform $C_0$, Fourier modes $e^{ikj}$ diagonalize $U_0$ with $k=2\pi m/L$. Opposite-$k$ superpositions produce standing envelopes (exact in the symmetric limit).

Hence a standing-mode-supporting local unitary exists at $\beta=1$.

Why this matters: this is the explicit witness that the admissible class is not empty at the first nontrivial topology.

Literature anchor:

1. Quantum walk on periodic lattices/cycles: Fourier mode diagonalization and counter-propagating superpositions.
2. Floquet/quasienergy language for discrete-time unitary maps.

### Lemma L5 (Embedding in the `R5-R8` Window)
Status: `postulate`

Choose block-unitary coins:

$$
C_v=
\begin{pmatrix}
C_v^{LL} & C_v^{LR}\\
C_v^{RL} & C_v^{RR}
\end{pmatrix},
\quad
\|C_v^{LR}\|_{\mathrm{op}}+\|C_v^{RL}\|_{\mathrm{op}}=\epsilon_{\mathrm{mix}}(v),
$$

with canonical admissible inequality:

$$
0<\bar{\epsilon}_{\mathrm{mix}}\le\epsilon_{\mathrm{mix}}^{\max}\ll1.
$$

Impose small CP asymmetry:

$$
0<\epsilon_{\mathrm{CP}}\le\epsilon_{\mathrm{CP}}^{\max}\ll1.
$$

By continuity of spectra/eigenmodes under small unitary perturbations, standing modes of the symmetric witness deform into quasi-standing modes while remaining in the admissible window.

Hence the constrained class is non-empty and mode-supporting.

Why this matters: the proof target is existential ("at least one admissible transport function"), so this perturbative embedding is the key step.

Literature anchor:

1. Perturbation stability of spectral data for bounded normal/unitary operators (Kato framework).

### Lemma L6 (Induction on Cycle Rank)
Status: `postulate`

Induction variable:

$$
\beta=|E|-|V|+1.
$$

1. Base: $\beta=1$ by L4-L5.
2. Step: assume existence for $\beta=r$. Add one edge that creates one new independent cycle ($\beta=r+1$). Keep prior local coins and add a small local unitary coupling on the new edge. By unitary perturbation continuity, at least one prior standing/quasi-standing mode persists (possibly spectrally shifted), and the new cycle adds closed interference channels.

Therefore existence extends to all connected finite graphs with $\beta\ge1$.

Why this matters: this converts the single-cycle witness into a general topology statement indexed by cycle rank.

## 5. What Is Already Known from Literature

Status: `external-constraint`

1. Linear unitary wave dynamics generically decomposes into normal modes; standing waves are superpositions of counter-propagating/phase-conjugate traveling modes (QM and wave-physics standard result; see Refs. 1-2).
2. Discrete-time quantum walks are the canonical graph-local, unitary, Schrodinger-like update systems; their spectra and mode structure are well studied on lines, cycles, and lattices (Refs. 3-5).
3. Cycles impose phase-closure quantization conditions and therefore support robust loop resonances/standing envelopes; trees lack this independent loop-closure channel (Refs. 6-7).
4. Small admissible perturbations of a unitary witness typically preserve nearby spectral/mode structure, motivating the standing-to-quasi-standing step used here (Ref. 8).

These facts do not prove UniNet by themselves; they justify that the proof strategy is mathematically standard once the UniNet admissibility constraints are fixed.

## 6. Scope Boundaries

### Established in This Note
Status: `postulate`

1. At least one transport/update function in the restricted class supports mode data in the explicit forms $U\phi=\lambda\phi$ (exact) or narrow unit-modulus mode packets (quasi-standing).
2. Information conservation is exact at the microscopic level through unitarity.
3. Delay behavior is locality-derived and regime-consistent.

### Not Established in This Note
Status: `deferred`

1. Full classification of standing spectra for arbitrary $G$.
2. Uniqueness of admissible witness family.
3. Full SM gauge-group constructive derivation.

## 7. Dependency Anchors

1. `docs_input/UNINET_CORE_AXIOMS.md`: AXIOM-7, AXIOM-6, MODEL-P2 (Node Buffering), `R1-R3`, `R5-R10`, AXIOM-10.
2. `docs/00_foundation/02_update_operator_constraints.md`: consolidated restricted-class constraints and wave-transport interpretation.

## 8. Literature Hooks Used in This Proof

1. Schrodinger, E. (1926). Wave-mechanics formulation of quantum dynamics (unitary wave evolution context).
2. Stone, M. H. (1932). One-parameter unitary groups in Hilbert space (self-adjoint generator theorem).
3. Aharonov, Y., Davidovich, L., Zagury, N. (1993). Quantum random walks.
4. Ambainis, A. et al. (2001). Discrete-time quantum walks with boundaries.
5. Venegas-Andraca, S. E. (2012). Quantum walks review.
6. Chung, F. (1997). Spectral graph theory (cycle/spectrum structure).
7. Kottos, T., Smilansky, U. (1999). Quantum graphs and wave/standing-mode structure on graph networks.
8. Kato, T. (1966/1995 edition). Perturbation theory for linear operators (spectral continuity under small perturbations).




