# UniNet Parameter Ledger v1 (Pre-Lock)

Date: 2026-03-30
Purpose: canonical parameter inventory before lock-protocol definition.
Scope: no new derivations; bookkeeping and identifiability only.
Primary source: `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md`.

## 1. Status Codes

1. `fixed`: not fitted; set by axiom, unit choice, or definition.
2. `fit`: to be inferred from lock datasets, then frozen.
3. `derived`: computed from fixed/fit parameters; not independently fitted.
4. `deferred`: conceptually needed but transfer map or finite parameterization not yet fixed.

## 2. ParameterRecord v1 Schema

1. $parameter_id$
2. `symbol`
3. `class`
4. `status`
5. `unit`
6. `domain`
7. `meaning`
8. `source_anchor`
9. $used_by_prediction_ids$
10. $planned_lock_dataset_family$
11. $lock_priority$
12. `notes`

## 3. Ledger

| parameter_id | symbol | class | status | unit | domain | meaning | source_anchor | used_by_prediction_ids | planned_lock_dataset_family | lock_priority | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-STR-001 | $|V|$ | structural | deferred | 1 | positive integer | Total node count of substrate graph realization. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:211 | indirect (all) | none (architecture-level) | P3 | Not directly observable without a fixed projection/coarse-grain map. |
| P-STR-002 | $|E|$ | structural | deferred | 1 | positive integer | Total edge count of substrate graph realization. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:211 | indirect (all) | none (architecture-level) | P3 | User-requested graph-complexity control parameter. |
| P-STR-003 | $k_v,\bar{k}$ | structural | deferred | 1 | integer / positive real | Per-node degree and mean degree (edge density descriptors). | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:211 | QM-CORE-001, QM-DEF-004 (indirect) | none (architecture-level) | P3 | Represents edge-count structure per node. |
| P-STR-004 | $d,d_L,d_R$ | structural | deferred | 1 | positive integers | Internal Hilbert dimensions and chiral split per node. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:229; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:297 | SM-CORE-001, SM-CORE-002, COS-CORE-004 | architecture + weak/flavor consistency sets | P2 | Must be fixed before final finite transfer parameterization. |
| P-TRN-001 | $\bar{\epsilon}_{\mathrm{mix}}$ | transfer | fit | 1 | $(0,\epsilon_{\mathrm{mix}}^{\max}]$ | Graph-average chirality mixing amplitude. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | SM-CORE-001, COS-CORE-004 | flavor/weak data (non-CMB) | P1 | Primary chirality control dial. |
| P-TRN-002 | $\epsilon_{\mathrm{mix}}^{\max}$ | transfer | fit | 1 | $(0,1)$ (SM-like) | Admissible upper bound for local chiral mixing. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:789; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | SM-CORE-001 | flavor/weak global fits | P1 | Hard-cut hyperparameter in lock phase. |
| P-TRN-003 | $L_{\mathrm{mix}}$ | transfer | fit | 1 | nonnegative real | Spatial regularity bound on chirality-mixing field. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:858 | SM-CORE-001, COS-DEF-005 | flavor + structure-growth cross-checks | P2 | Controls roughness of mixing across neighboring nodes. |
| P-TRN-004 | $\epsilon_{\mathrm{CP}}$ | transfer | fit | 1 | $(0,\epsilon_{\mathrm{CP}}^{\max}]$ | CP non-commutation strength metric $\frac12\|[\mathsf{CP},U]\|$. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:798; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | SM-CORE-002, SM-DEF-003, COS-CORE-004 | kaon/B-sector CP data (non-CMB lock) | P1 | Main CP-violation dial entering cross-sector tests. |
| P-TRN-005 | $\{\delta_\alpha\}_\alpha$ (compressed) | transfer | deferred | rad | real vector/mod phases | Mode-phase structure used by CP involution. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:801 | SM-CORE-002, SM-DEF-004 | flavor-phase observables | P2 | Finite compression choice required before locking. |
| P-GR-001 | $\alpha$ | GR-latency | fit | 1 | positive real | Buffering contribution to adaptive latency kernel. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1174 | GR-CORE-001 | solar-system timing + GW propagation | P1 | Coupled with $\beta$; identifiability handled in lock protocol. |
| P-GR-002 | $\beta$ | GR-latency | fit | 1 | positive real | Curvature contribution to adaptive latency kernel. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1174 | GR-CORE-001, GR-CORE-003 | solar-system timing + GW propagation | P1 | Must be locked disjoint from final reject datasets. |
| P-GR-003 | $\xi_{\mathrm{leak}}$ | horizon/leaky-boundary | fit | 1 | nonnegative real | Effective leakage/slack amplitude for horizon-like cuts. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:440; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:446 | GR-LB-CORE-001 | GW inspiral/ringdown dissipation channels | P1 | First concrete leaky-boundary amplitude in decision tests. |
| P-GR-004 | $|\mathcal{R}|^2$ map parameter | horizon/leaky-boundary | deferred | 1 | $[0,1]$ | Reflectivity-style observable map parameterization. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:440; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:446 | GR-LB-CORE-001, GR-LB-DEF-002 | GW echo/EMRI pipelines | P2 | Deferred until a unique waveform transfer map is fixed. |
| P-PRJ-001 | $\theta_{\Pi}$ (finite basis) | projection | deferred | varies | finite real vector | Finite parameterization of projection family $\Pi_v$. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1050 | indirect (all observable-facing rows) | geometry/kinematics lock set | P1 | Mandatory for full identifiability; currently not yet finite by definition. |
| P-PRJ-002 | $\Lambda_{\mathrm{proj}}$ | projection | fixed | energy density | positive real | Buffering-to-energy projection coupling. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1086; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1089 | GR-CORE-001, GR-CORE-003, COS-CORE-001..004 | none | P0 | Fixed to Planck-density choice in core axiom text. |
| P-MAP-001 | $\ell_e$ | graph-to-physical map | fixed | m | positive real | Physical length assigned to one graph hop. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1104 | GR-CORE-001, GR-CORE-002, GR-CORE-003 | none | P0 | Model choice in Axiom 4.3 sets $\ell_e=\ell_{\mathrm{P}}$. |
| P-MAP-002 | $\Delta t$ | graph-to-physical map | fixed | s | positive real | Physical duration assigned to one tick. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:220; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1104 | GR-CORE-001, GR-CORE-002, GR-CORE-003 | none | P0 | Model choice in Axiom 4.3 sets $\Delta t=t_{\mathrm{P}}$. |
| P-MAP-003 | $c_{\mathrm{map}}=\ell_e/\Delta t$ | graph-to-physical map | derived | m/s | positive real | Emergent speed mapping from graph units to SI units. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1104 | GR-CORE-002, GR-CORE-003 | none | P0 | Equals $\ell_{\mathrm{P}}/t_{\mathrm{P}}$ under current mapping choice. |
| P-CON-001 | $\kappa$ | constant | fixed | SI gravity coupling | positive real | Einstein coupling $8\pi G/c^4$. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:198; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1003 | GR-CORE-001..003 | none | P0 | Not a fit parameter in this program. |
| P-CON-002 | $\rho_{\max}$ | constant | fixed | 1 | $=1$ | Node occupancy saturation bound. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1127 | COS-CORE-001, COS-CORE-003 | none | P0 | Normalization bound. |
| P-CON-003 | $c$ | constant | fixed | speed | positive real | Physical lightspeed constant used in projected dynamics. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:201; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1104 | GR-CORE-002, GR-CORE-003 | none | P0 | In current convention $c=c_{\mathrm{map}}$; kept explicit for units clarity. |
| P-DER-001 | $\delta_{\mathrm{QM}}(u,v)$ | regime-derived | derived | ticks/hops | nonnegative integer | QM static latency equals graph distance. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1153 | QM-CORE-001, QM-DEF-004 | none | P0 | Derived theorem, not fitted. |
| P-COS-001 | $\tau_{\mathrm{relax}}$ | cosmology | fit | time | positive real | Buffer-relaxation timescale controlling $w(z)$ drift. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1189 | COS-CORE-001 | expansion-history (BAO+SN+CMB distance priors) | P1 | Principal dark-energy timescale in UniNet branch. |
| P-COS-002 | $\lambda_{\mathrm{DM}}$ | cosmology | fit | length | positive real | Long-wavelength buffered mode scale for DM-like sector. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1201 | COS-CORE-002 | LSS + weak-lensing + Ly-alpha | P1 | Sets turnover/scale dependence of congestion effects. |
| P-COS-003 | $A_{\mathrm{cong}}$ | cosmology | fit | 1 | nonnegative real | Amplitude of congestion-feedback enhancement/suppression. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1203 | COS-CORE-002 | structure-growth residual datasets | P1 | Equation form to be frozen in lock protocol. |
| P-COS-004 | $\Phi_{\max}/\Phi_{\mathrm{initial}}$ | cosmology | fit | 1 | $>1$ | Inflation phase-accumulation ratio controlling e-fold count. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1214 | COS-CORE-003 | primordial CMB/LSS set | P2 | Can be reparameterized directly as $N_e$ in lock protocol. |
| P-COS-005 | $N_e$ | cosmology | derived | 1 | approx $50$-$70$ class | Number of inflation e-folds from phase ratio relation. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1214 | COS-CORE-003 | none | P0 | Derived from P-COS-004 when chosen parameterization is fixed. |
| P-COS-006 | $\chi_{\mathrm{parity}}$ | cosmology/parity | fit | 1 or rad (map-dependent) | small real | Effective chirality/parity amplitude for CMB parity channels. | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:798; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:1217 | COS-CORE-004, SM-DEF-004 | lock on non-CMB CP/chirality data, test on CMB | P1 | Keep disjoint-lock policy to avoid circularity in parity tests. |

## 4. Reduced Fit Basis (Candidate for Lock Protocol v1)

Recommended first identifiable fit vector:

$\theta_{\mathrm{fit},v1}=\{\bar{\epsilon}_{\mathrm{mix}},\epsilon_{\mathrm{CP}},\alpha,\beta,\xi_{\mathrm{leak}},\tau_{\mathrm{relax}},\lambda_{\mathrm{DM}},A_{\mathrm{cong}},\Phi_{\max}/\Phi_{\mathrm{initial}},\chi_{\mathrm{parity}}\}$

Excluded from fit by construction in v1:

1. $\kappa$
2. $\rho_{\max}$
3. $\ell_e$
4. $\Delta t$
5. $c_{\mathrm{map}}$
6. $c$
7. $\Lambda_{\mathrm{proj}}$
8. $\delta_{\mathrm{QM}}(u,v)$

## 5. Immediate Follow-Up for Lock Protocol Drafting

1. For each `fit` parameter, define a unique lock dataset family and a forbidden target dataset family.
2. Freeze the finite parameterization choice for $\theta_{\Pi}$ and $\{\delta_\alpha\}_\alpha$ before any global fit.
3. Decide whether $\chi_{\mathrm{parity}}$ is independent or derived from $\bar{\epsilon}_{\mathrm{mix}},\epsilon_{\mathrm{CP}}$ in v1.
4. Add covariance propagation rules from lock step to each falsifiability-row decision rule.





