# UniNet GR Section (Rigorous Scaffold v2)

Date: 2026-03-30  
Primary source of truth: `../docs_input/UNINET_CORE_AXIOMS.md`  
Plan baseline: `../docs_input/UNINET_GR_SECTION_RIGOR_PLAN.md`  
Governance: `UNINET_NOTATION_UNITS_STANDARD.md`, `UNINET_PROOF_STATUS_LEDGER.md`, `UNINET_BOUNDARY_NONCLAIMS.md`, `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`

## 1. Contract and Scope Lock

1. No new microscopic axioms are introduced.
2. Allowed input claims are limited to Tier-0 axioms, Tier-1 to Tier-3 derived structures, bridge axioms 4.1-4.3, and transfer constraints `R9`, `R10`.
3. Claim taxonomy used in this section: `Definition`, `Lemma`, `Theorem`, `Corollary`, `Postulate`, `Proposition`, `Boundary Note`.
4. Status vocabulary is constrained to: `proved`, `postulate`, `deferred`, `external-constraint`.
5. No observational fitting is done in this section.

## 2. Assumption Ledger and Dependency Graph

| id | statement | status | source anchor | depends_on |
|---|---|---|---|---|
| GR-A1 | Graph-local unitary buffering substrate | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:211,244,260,278` | none |
| GR-A2 | Causal precedence, cones, horismos | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:544,568,599` | GR-A1 |
| GR-A3 | Observer-time and time-separation structures | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:613,632,645` | GR-A2 |
| GR-A4 | Projection bridge (`4.1`, `4.2`, `4.3`) | postulate | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1050,1086,1104` | GR-A1, GR-A3 |
| GR-A5 | Adaptive latency in GR regime | postulate | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1171` | GR-A4 |
| GR-A6 | Queue drift and trapping package | proved | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:491,513,532` | GR-A1, GR-A5 |
| GR-A7 | Effective transport constraints `R9`, `R10` | postulate | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:866,882` | GR-A5 |
| GR-A8 | Pseudo-unitary projected invariance target | deferred | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:927` | GR-A4 |

## 3. Formal Mapping Blocks (M1-M9)

### M1. Substrate -> Causal Order

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M1.1 | Lemma | proved | GR-A1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:326` | Graph locality implies finite-speed reachability bound. |
| M1.2 | Theorem | proved | M1.1, GR-A2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:556` | Precedence relation is a partial order. |
| M1.3 | Corollary | proved | M1.2, GR-A2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:587,599` | Horismos is the cone-boundary notion in the discrete causal setting. |

### M2. Causal Order -> Observed Time

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M2.1 | Definition | proved | GR-A2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:632` | Define observer-time functional via past-set volume. |
| M2.2 | Theorem | proved | M2.1, GR-A3 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:623,632` | Under nondegeneracy, `x \prec y => t_{\mathrm{obs}}(x) < t_{\mathrm{obs}}(y)`. |
| M2.R | Remark | proved | M2.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:220,632` | Distinguish microscopic tick `n` from emergent observed time `t_{\mathrm{obs}}`. |

### M3. Microscopic State -> Observed Spacetime

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M3.1 | Definition | postulate | GR-A4 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1050` | Projection interface map from microscopic amplitudes to observed fields/events. |
| M3.2 | Theorem target | deferred | M3.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:897,1050` | Label-gauge covariance of projection under graph isomorphisms. |
| M3.3 | Theorem target | deferred | M3.1, M1.2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:544,599,1050` | Causal compatibility of projection (no superluminal inversion). |

### M4. Observed Spacetime -> Proper Time and Time Dilation

Domain assumptions: projected increments are timelike where proper-time is evaluated.

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M4.1 | Definition | proved | GR-A4 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1066` | Proper-time increment from projected Lorentzian norm. |
| M4.2 | Theorem target | postulate | M4.1, GR-A5, GR-A6 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:513,1066,1171` | Congestion/adaptive-delay regimes reduce accumulated proper time relative to low-load branch. |
| M4.3 | Corollary target | deferred | M4.2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1066,1171` | Operational time-dilation comparison statement between observers. |

Native expression:
\[
\Delta \tau_n(v)=\frac{\sqrt{-\langle \Delta x_n(v),\Delta x_n(v)\rangle_\eta}}{c_{\mathrm{map}}}.
\]

### M5. Dynamics -> Lorentz Invariance Envelope

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M5.1 | Definition target | deferred | GR-A8 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:927` | Admissible projected pseudo-unitary transformation class. |
| M5.2 | Theorem target | deferred | M5.1, M4.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:927,1066` | Invariance of projected interval under admissible class. |
| M5.3 | Proposition target | deferred | M5.2, GR-A5 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1171` | Controlled deviation envelope from discrete corrections. |

Low-load local envelope (postulated target metric):
\[
ds^2 \approx -c_{\mathrm{map}}^2\,dt_{\mathrm{obs}}^2 + dx^2+dy^2+dz^2.
\]

### M6. Geometry -> Geodesics in Observed Spacetime

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M6.1 | Definition | proved | GR-A3 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:645` | Time-separation core `\tau(x,y)` as geodesic scaffold. |
| M6.2 | Theorem target | external-constraint | M6.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:645` | Existence of maximizing causal curves under adopted regularity class. |
| M6.3 | Theorem target | deferred | M6.1, M3.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:326,645,1050` | Correspondence between graph-optimal paths and projected geodesics. |

### M7. Sources -> Curvature Dynamics

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M7.1 | Definition target | postulate | GR-A4, GR-A5 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:999,1023,1171` | Stress-effort map from buffering/flux variables. |
| M7.2 | Theorem target | postulate | M7.1 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1023,1171` | Discrete Euler-Lagrange field equation for GR-regime packaging. |
| M7.3 | Lemma target | deferred | M7.2 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1023` | Conservation compatibility (Bianchi-type consistency identity). |

Native target equation:
\[
\mathrm{Curv}[\tau]=\kappa\,\mathrm{StressEffort}[\rho,J].
\]

Variational companion (mandatory class):
\[
\frac{\delta\!\left(\mathcal{S}_{\mathrm{geo}}[\tau]+\kappa\,\mathcal{S}_{\mathrm{src}}[\rho,J]\right)}{\delta \tau}=0.
\]

### M8. Queueing/Backpressure -> Horizon-Scale Transport

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M8.1 | Definition target | postulate | GR-A6, GR-A7 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:460,475,866,882` | Normal vs near-saturation queueing regimes in projected GR observables. |
| M8.2 | Theorem | proved | GR-A6 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:491` | Queue-drift identity and low-load stability imply finite-release behavior. |
| M8.3 | Theorem | proved | GR-A5, GR-A6, GR-A7 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:513,866,882` | Near-saturation trapping bound under adaptive-latency + throughput constraints. |
| M8.4 | Corollary | proved | M8.3 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:532` | Boundary-dominant release with closure-vs-leak branch split. |

Branch declaration requirement:
1. Exact-closure branch: `\Phi_n(\partial R_{\mathrm{in}})=0`.
2. Leaky branch: `\Phi_n(\partial R_{\mathrm{in}})\neq 0` with bounded throughput class.

### M9. Black-Hole Application Layer (Deferred-to-Core Path)

| statement_id | type | status | depends_on | source anchor | statement |
|---|---|---|---|---|---|
| M9.1 | Proposition target | deferred | M8.2, M8.3, GR-A3 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:513,671,704` | Operational Page-turnover proxy for coarse-grained radiation entropy trajectory. |
| M9.2 | Proposition target | deferred | M8.3, M8.4 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:513,532,882` | Near-horizon smoothness/no-firewall statement as bounded transport law condition. |
| M9.3 | Proposition target | deferred | M8.4 | `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:446,532` | Multimode ringdown coefficient map from leakage/microstate parameters. |
| M9.B | Boundary Note | proved | M9.1-M9.3 | `../docs_output/UNINET_GR_FALSIFIABILITY_MATRIX.md` | M9 claims are not promotable without explicit forward map and binary reject threshold. |

## 4. Continuum Correspondence Block

Scaling assumptions (all explicit postulates unless already proved):

1. `\ell_e` and `\Delta t` define `c_{\mathrm{map}}=\ell_e/\Delta t`.
2. Coarse-graining scale is large relative to graph spacing.
3. Effective fields are smooth enough on the projection scale for continuum observables.

Limit statement (deferred target):

\[
\text{Discrete projected dynamics} \xrightarrow[\ell_e,\Delta t\to 0]{\ell_e/\Delta t=c_{\mathrm{map}}} \text{Lorentzian continuum envelope on admissible domains}.
\]

Status: `deferred` pending explicit regularity and convergence theorem.

## 5. Failure Modes (Explicit)

1. Projection non-covariance under relabeling invalidates M3.2.
2. Any required superluminal inversion in projection invalidates M3.3.
3. Absence of an admissible pseudo-unitary class invalidates M5 envelope claims.
4. Inconsistent queue branch declaration invalidates M8/M9 horizon statements.
5. Failure to construct a forward observable map blocks promotion of M9 propositions.

## 6. Open Proof Obligations and Promotion Gates

| obligation_id | target | current status | promotion blocker | promotion artifact |
|---|---|---|---|---|
| GR-PO-01 | M3.2 | deferred | explicit projection covariance theorem missing | theorem proof note + dependency closure |
| GR-PO-02 | M3.3 | deferred | causal-compatibility proof missing | no-inversion theorem with assumptions |
| GR-PO-03 | M4.3 | deferred | explicit observer-comparison bound missing | time-dilation inequality theorem |
| GR-PO-04 | M5.1-M5.3 | deferred | admissible transform class + invariance proof missing | symmetry block theorem package |
| GR-PO-05 | M6.3 | deferred | graph-to-geodesic correspondence theorem missing | correspondence theorem + regularity class |
| GR-PO-06 | M7.3 | deferred | conservation-compatibility proof missing | Bianchi-type compatibility lemma |
| GR-PO-07 | M9.1-M9.3 | deferred | forward observable maps and thresholds missing | matrix-promotion package |

## 7. Claim Discipline (Hard Review Mode)

1. Every theorem/proposition must list dependencies explicitly.
2. Every equation used as a claim must state domain/regularity assumptions.
3. Every horizon statement must declare branch (`\Phi=0` or `\Phi\neq0`) and throughput class.
4. No phenomenological claims appear in proof-status sections without status tags.
5. Dynamics claims include native and variational forms where mandatory.

## 8. Mapping-Complete Audit Table

| mapping target | required by plan | current section status | audit result |
|---|---|---|---|
| M1 | formal statements | present with IDs/dependencies | pass |
| M2 | formal statements | present with IDs/dependencies | pass |
| M3 | formal statements | present (postulate/deferred) | pass (deferred-aware) |
| M4 | proper-time + dilation theorem | present (dilation partially deferred) | partial |
| M5 | Lorentz envelope + failure regime | present (deferred theorem targets) | partial |
| M6 | geodesic existence + correspondence | present (one external, one deferred) | partial |
| M7 | native + variational dynamics | present | pass (postulate-scoped) |
| M8 | queue/backpressure-horizon block | present | pass |
| M9 | deferred-aware BH application block | present with promotion gate | pass |

## 9. Literature Hooks (Imported Steps)

1. Minguzzi (2019), Lorentzian causality theory.
2. Minguzzi (2019), closed cone structures and smooth time functions.
3. Kunzinger-Samann (2018), Lorentzian length spaces.
4. Beran-Rott (2024), gluing in Lorentzian length spaces.
5. Gourgoulhon (2013), proper time and Lorentz frames.
6. Regge (1961), discrete gravity action precedent.

## 10. Falsifiability Cross-Links

1. Core GR rows: `GR-CORE-001`, `GR-CORE-002`, `GR-CORE-003` in `UNINET_GR_FALSIFIABILITY_MATRIX.md`.
2. Leaky-boundary rows: `GR-LB-CORE-001`, `GR-LB-DEF-002`, `GR-LB-DEF-003`.
3. Black-hole deferred rows: `GR-BH-DEF-004`, `GR-BH-DEF-005`.
4. Axiom-to-prediction dependency map: `UNINET_AXIOM_TO_PREDICTION_DAG.md`.



