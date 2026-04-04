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

