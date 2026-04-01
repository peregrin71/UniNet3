# UniNet Notation and Units Standard v1

Date: 2026-03-30  
Purpose: enforce notation/unit consistency across all active UniNet documents.
Scope: mandatory for core, plans, ledgers, and falsifiability matrices.

## 1. Conventions

1. Markdown math uses LaTeX delimiters `$...$` and `\[...\]`.
2. Symbols must use explicit subscripts/superscripts (no plain-text fallback when avoidable).
3. Use one canonical symbol per concept (no silent renaming).
4. Regime labels must be explicit: QM, GR, SM, Cosmology.

## 2. Core Symbol Canon

1. Graph substrate: `$G=(V,E)$`
2. Tick index: `$n \in \mathbb{Z}$`
3. State: `$\psi_n \in \mathcal{H}$`, node state `$\psi_v(n)$`
4. Buffering occupancy: `$\rho(v,n)=\|\psi_v(n)\|^2$`
5. Flux/cut variables: `$J_n(u\to v)$`, `$Q_n(R)$`, `$\Phi_n(\partial R)$`
6. Causal sets: `$J^\pm(x)$`, horismos `$E^+(x)$`
7. Observer time: `$t_{\mathrm{obs}}$`
8. Time separation: `$\tau(x,y)$`
9. Chiral mixing: `$\epsilon_{\mathrm{mix}}$`, `$\bar{\epsilon}_{\mathrm{mix}}$`, `$\epsilon_{\mathrm{mix}}^{\max}$`
10. CP metric: `$\epsilon_{\mathrm{CP}}=\frac12\|[\mathsf{CP},U]\|_{\mathrm{op}}$`
11. GR adaptive latency: `$\delta_{\mathrm{GR,eff}}$`
12. QM latency: `$\delta_{\mathrm{QM}}(u,v)=d_G(u,v)$`

## 3. Units Policy

1. Dimensionless quantities must be stated as unit `1`.
2. Use SI symbols for physical units (`m`, `s`, `kg`, `J`, `eV`) where applicable.
3. Explicitly state whether a quantity is:
   1. dimensionless model variable,
   2. projected physical observable,
   3. derived map quantity.
4. Map constants:
   1. `$c_{\mathrm{map}}=\ell_e/\Delta t$` (m/s),
   2. `$\ell_e$` (m),
   3. `$\Delta t$` (s).

## 4. Document Formatting Rules

1. Always use `\mathrm{...}` for text subscripts in math (`\rho_{\mathrm{DM}}`, `t_{\mathrm{obs}}`).
2. Use calligraphic symbols for functionals/spaces (`\mathcal{H}`, `\mathcal{S}`) consistently.
3. Use operator norm as `\|\cdot\|_{\mathrm{op}}` consistently.
4. For inequalities, keep canonical style:
   1. `0 < x \le x_{\max} \ll 1`
   2. avoid mixed textual inequalities in same equation.

## 5. Status Tagging Rules

Each major claim block must be tagged as one of:

1. `proved`
2. `postulate`
3. `deferred`
4. `external-constraint`

Status source of truth:

1. `UNINET_PROOF_STATUS_LEDGER.md`
2. `UNINET_BOUNDARY_NONCLAIMS.md`

## 6. Cross-Document Compliance

All active docs must reference this standard when adding new equations/parameters.

Minimum compliance check before accepting edits:

1. New symbols listed in or aligned with this file.
2. Units declared for every new parameter in ledgers/matrices.
3. No conflicting aliases for existing core symbols.
4. Any intentional deviation documented in a local "Notation Note" subsection.

## 7. Planned Enforcement Pass

1. New edits: enforce immediately.
2. Legacy text: normalize opportunistically during touched-file edits.
3. Full repo-wide normalization: deferred until after core theorem/section drafting stabilizes.




