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

