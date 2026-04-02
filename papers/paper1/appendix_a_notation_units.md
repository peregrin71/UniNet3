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

