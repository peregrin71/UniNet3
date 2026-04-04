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

