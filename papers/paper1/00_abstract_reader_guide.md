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
