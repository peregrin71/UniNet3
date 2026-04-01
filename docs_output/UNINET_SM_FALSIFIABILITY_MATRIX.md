# UniNet SM Falsifiability Matrix

Date: 2026-03-30
Standard: `UNINET_FALSIFIABILITY_STANDARD.md` (`PredictionRecord v1`)
Section scope: chirality-mixing windows and CP non-commutation tests against flavor-sector observables.

| prediction_id | claim_status | source_anchor | model_equation_or_rule | observable | sign_or_direction | null_model | current_constraint | forecast_constraint | free_parameter_policy | decision_rule | falsifier_statement |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SM-CORE-001 | postulate | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:757; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | Chiral transfer blocks with bounded mixing: $\epsilon_{\mathrm{mix}}$ must remain in weak-compatible admissible window (R5/R8). | Pion leptonic ratio residual $\Delta R_\pi = R_{e/mu}^{exp} - R_{e/mu}^{SM}$. | Must remain small and sign-consistent with locked $\epsilon_{\mathrm{mix}}$ branch. | SM V-A charged-current baseline. | Current world class: $R_{e/mu}^{exp} = (1.2344 +/- 0.0030) x 10^-4$ vs $R_{e/mu}^{SM} = (1.2352 +/- 0.0001) x 10^-4$ (PIONEER summary, 2023). | PIONEER program targets about 15x precision improvement for $R_{e/mu}$ and $|V_ud|$ precision near $0.02\%$ (phased run plan, late 2020s to early 2030s). | pre-locked-from-disjoint-data | Reject if pre-locked $\epsilon_{\mathrm{mix}}$ predicts a residual window that is excluded at >=5 sigma by PIONEER-era $R_{e/mu}$ data. | If precision pion-decay data rule out the locked chirality-mixing window, the SM-side chiral transfer packaging fails. |
| SM-CORE-002 | postulate | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:798; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | CP non-commutation metric $\epsilon_{\mathrm{CP}} = 0.5 ||[CP,U]||_op$ maps to flavor CP asymmetry amplitudes under a locked transfer map. | $\sin(2 \phi_1)$ from $B \to J/\psi K_S$ time-dependent CP asymmetry. | Must be nonzero and inside locked CP window. | CKM baseline fit in SM flavor sector. | Belle II early sample: $\sin(2 \phi_1)=+0.720 \pm 0.062(\mathrm{stat}) \pm 0.016(\mathrm{syst})$ at $190\,\mathrm{fb}^{-1}$; Belle: $+0.670 \pm 0.029 \pm 0.013$ at $771\,\mathrm{fb}^{-1}$ (PTEP 2025 review). | Belle II full $50\,\mathrm{ab}^{-1}$ target: Unitarity Triangle angles at about $1^\circ$ precision class, tightening CP-window tests (2030s). | pre-locked-from-disjoint-data | Lock $\epsilon_{\mathrm{CP}}$ on kaon-sector data, then test on $B$-sector CP asymmetry; reject if measured $\sin(2 \phi_1)$ falls outside 95% predictive interval with >5 sigma tension. | If locked CP non-commutation fails cross-sector prediction in $B$ decays, the CP map is falsified. |
| SM-DEF-003 | deferred | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:798 | Same CP non-commutation metric tested directly in kaon sector. | $|\epsilon_K|$. | Must be nonzero but small. | SM CKM kaon baseline. | PDG 2025: $|\epsilon| = (2.228 +/- 0.011) x 10^-3$. | No pre-registered, instrument-level future threshold tied to UniNet transfer-map parameters is locked yet in this matrix version. | pre-locked-from-disjoint-data | Promote to core after a specific future kaon-program sensitivity target and lock/test split are fixed in writing. | Current kaon value is a strong anchor, but without locked forecast threshold this row remains deferred. |
| SM-DEF-004 | deferred | C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:798; C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:843 | Joint CP-CMB chirality linkage ($\epsilon_{\mathrm{CP}}$, $\epsilon_{\mathrm{mix}}$ -> parity channels) exists only as buildup-level scaling, not a fully locked forward model. | Joint statistic $\chi_{\mathrm{joint}}$ from flavor CP + CMB parity datasets. | Must stay in overlap window if linkage is correct. | Decoupled SM flavor + LCDM parity baseline. | Ballpark overlap note exists (`../docs_input/UNINET_CP_CMB_CHIRALITY_OVERLAP_NOTE.md`), but no fixed global likelihood yet. | LiteBIRD/CMB-S4 plus Belle II/LHCb upgrades can support a joint fit in 2030s after model lock. | pre-locked-from-disjoint-data | Promote to core only when the joint likelihood, lock policy, and blind-analysis protocol are written and frozen before fit. | Without a locked forward model, overlap is compatibility evidence, not yet a Popper prediction. |

## External Sources (Current and Forecast Anchors)

1. PIONEER experiment overview (current $R_{e/mu}$ context and forecast precision goals): https://www.stonybrook.edu/commcms/physics/pioneer/
2. APS DNP/PSJ abstract, "The PIONEER Rare Pion Decay Experiment" (2023). https://archive.aps.org/haw/2023/2wbb/3/
3. Belle II prospects review (PTEP 2025): https://doi.org/10.1093/ptep/ptae010
4. PDG 2025 strange-meson table ($|\epsilon|$): https://pdg.lbl.gov/2025/tables/rpp2025-tab-mesons-strange.pdf
5. Belle + Belle II CKM updates (example combined result stream): https://doi.org/10.1007/JHEP10(2024)143







