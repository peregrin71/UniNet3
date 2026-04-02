# Chapter 11 - Governance, Audit, and Falsifiability Discipline

Paper 1 is intentionally split into two layers: a mathematical layer that states axioms, definitions, theorems, and postulates, and a governance layer that controls how claims are allowed to appear. This chapter defines that second layer. Its purpose is simple. It prevents theorem inflation, parameter circularity, and retrospective storytelling after data are known.

## 11.1 Claim Classes and Artifact Hierarchy
The paper uses four claim-status tags.

| Status | Meaning | Allowed manuscript use |
|---|---|---|
| `proved` | derived from earlier paper material or imported external theorem with declared scope | may be stated as established within that scope |
| `postulate` | explicit modeling or bridge choice | may be used operationally, but not advertised as derived |
| `deferred` | missing proof, forward map, threshold, or closure step | may be tracked, but not promoted rhetorically |
| `external-constraint` | imported theorem or observational constraint not internally derived | may be used with explicit scope and without ownership inflation |

### `GOV-01` - Canonical Source Hierarchy
Status: `governance`

The paper recognizes the following hierarchy of authority.

1. Core chapters carry the canonical scientific statements.
2. Appendices carry notation tables, governance rules, relabel aids, and full falsifiability metadata.
3. Extended proof notes may elaborate long derivations, but they do not silently upgrade claim status.
4. Planning material is not evidence.

The practical rule is that no sentence in the paper is allowed to outrun the status tag of the claim it depends on.

## 11.2 Dependency DAG and Claim Audit
The manuscript is organized as a mostly acyclic information graph:

$$
\text{Axioms}
\to
\text{Shared Definitions and Theorems}
\to
\text{Boundary and Update Structure}
\to
\text{Symmetry Layer}
\to
\text{Sector Packaging}
\to
\text{Falsifiability Rows}.
$$

This is both a writing rule and an audit rule.

1. Later chapters may depend on earlier chapters.
2. Forward references are allowed only for navigation, not for proof logic.
3. If two claims depend on each other, the common material must be lifted upward until the cycle disappears.

### `GOV-02` - Claim Audit Rule
Status: `governance`

Every nontrivial manuscript claim must admit a dependency path to one of the following:
1. an earlier paper theorem or definition,
2. an explicit postulate,
3. an explicitly scoped external theorem or empirical constraint.

If no such path exists, the claim is automatically classified as `deferred`.

## 11.3 Proof-Status Synchronization
The paper-facing status tags must agree with the canonical ledger discipline.

### `GOV-03` - Status Synchronization Rule
Status: `governance`

If a manuscript statement and its governing status registry disagree, the lower maturity wins until the conflict is resolved explicitly.

Operationally this means:
1. no theorem language for a `postulate`,
2. no established-fact language for a `deferred` item,
3. no imported theorem may be presented as internally derived.

## 11.4 Parameter Discipline and Lock Protocol
Observable-facing claims require a second control layer: parameter discipline. The paper uses four parameter classes.

| Parameter class | Meaning |
|---|---|
| `fixed` | set by convention, definition, or already-declared model choice |
| `fit` | inferred from a lock dataset and then frozen |
| `derived` | computed from fixed or fitted quantities |
| `deferred` | conceptually present, but not yet finitely parameterized or not yet lockable |

The reduced first-pass fit basis is

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

### `GOV-04` - Disjoint Lock Protocol
Status: `governance`

1. Choose the fit basis before target testing.
2. Assign a disjoint lock dataset family to every fitted parameter.
3. Freeze the posterior or allowed interval.
4. Test the target observable on non-overlapping data only.

This is the paper's anti-circularity rule. A branch is not allowed to fit itself to the same dataset it later advertises as confirmation.

## 11.5 Main Falsifiability Contract
The paper adopts a hard-Popper standard for every main-text prediction row. A row qualifies as core only if all of the following are true.

1. the observable is operationally explicit,
2. the comparison is made against exactly one null model,
3. the sign or direction of the claim is fixed,
4. the parameter policy is either `none` or `pre-locked-from-disjoint-data`,
5. the decision rule is binary,
6. the falsifier statement is written in plain language.

### `GOV-05` - Core Prediction Admissibility
Status: `governance`

A compact falsifiability row is admissible in the main text only if it has the form

$$
(\text{observable},\ \text{null model},\ \text{signed prediction},\ \text{parameter policy},\ \text{decision rule},\ \text{falsifier}).
$$

Rows missing any component remain tracked, but they are classified as `deferred`.

## 11.6 Main Text Versus Appendix B
The main body of the paper carries only compact rows. Appendix B carries the full audit payload:

1. claim-status vocabulary,
2. sector-by-sector core and deferred counts,
3. parameter classes and reduced fit basis,
4. priority test order,
5. promotion blockers,
6. anti-circularity and blind-analysis expectations.

### `GOV-06` - Manuscript/Appendix Falsifiability Split
Status: `governance`

Compact decision rows belong in the main text. Full matrices and audit metadata belong in Appendix B. Neither may contradict the other.

## 11.7 Non-Claims Boundary and Anti-Circularity
The paper also needs an explicit anti-overclaim contract. The current non-claims are:

1. no full Standard Model derivation is claimed,
2. no full microscopic-to-observable transfer closure is claimed in every sector,
3. no complete black-hole quantitative closure is claimed,
4. no detector-level non-particle dark-sector claim is promoted without an explicit coupling map,
5. no unique microscopic transport family is claimed,
6. no full Noether closure is claimed across all sectors,
7. no full cosmological multipole transfer closure is claimed.

### `GOV-07` - Non-Claims Boundary Rule
Status: `governance`

A statement may be promoted beyond the current non-claims boundary only when its proof status, forward map, and observational decision rule have all been frozen explicitly.

## 11.8 Exploratory Numerics and Audit Procedure
The paper permits exploratory numerics, but only under quarantine.

Exploratory scans may be reported only if all three statements remain true:
1. they are not used as theorem evidence,
2. they are not used as parameter locks,
3. they are described as compatibility checks rather than confirmations.

Under that rule, the first `InferenceLight` scan may be mentioned as follows:
1. it is a compatibility-first exploratory result,
2. it indicates that the current cosmology-facing branch remains compatible with a Regge-like curved-spacetime regime,
3. it does not uniquely select GR or Einstein-field-equation closure.

A reader who wants to audit any claim in the paper should then follow this order:
1. identify the claim's status tag,
2. find its parent theorem, postulate, or external constraint,
3. inspect the relevant parameter policy,
4. inspect the falsifiability row if the claim is observable-facing,
5. check Appendix B if the main text summary is too compressed.

## Chapter 11 Summary
Established in this chapter:
1. claim status is governed by a strict four-way vocabulary,
2. manuscript logic is constrained to a mostly DAG-like dependency structure,
3. parameter fitting must obey a disjoint lock protocol,
4. main-text falsifiability statements must be compact but decision-complete,
5. exploratory numerics are explicitly quarantined from proof and calibration.

Not claimed here:
1. that governance rules themselves prove physics,
2. that every deferred item already has a finished observational interface,
3. that compatibility scans count as confirmation.

