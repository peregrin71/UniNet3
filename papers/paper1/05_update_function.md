# Chapter 5 - Update Function

This chapter constrains the update operator before any sector-specific interpretation is allowed. The point is not to guess a preferred form of $U$ and then retrofit the rest of the theory around it. The point is to show that once the core and boundary theorems are fixed, only a narrow operator class survives, and at least one explicit witness family exists inside that class.

## 5.1 Why One Update Family and Homogeneity Matter
The core update commitments are:
1. `AXIOM-4`: one declared update-rule family,
2. `AXIOM-5`: update homogeneity across the graph.

These two constraints do more than simplify notation. They block three forms of hidden model drift:
1. undeclared patchwork laws assigned to different nodes,
2. ad hoc per-edge clocks or per-region rule changes,
3. post hoc tuning in which later sector behavior is smuggled into the microscopic law through hidden heterogeneity.

The paper therefore treats one update family and homogeneity as law-discipline constraints. They are what make later operator pruning meaningful rather than cosmetic.

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

This is the precise sense in which the admissible class is Schrodinger-like without introducing an independent continuum-time Hamiltonian postulate. The claim is not that this is the unique admissible microscopic law. The claim is that at least one physically familiar wave-like class survives all hard constraints and therefore serves as a constructive witness.

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
