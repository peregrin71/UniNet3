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

