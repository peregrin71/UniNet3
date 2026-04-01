# UniNet Falsifiability Standard v1

Date: 2026-03-30
Scope: mandatory standard for all UniNet falsifiability matrices.
Applies to: QM, GR, SM, and Cosmology (LCDM-comparison).
Governance dependencies: `UNINET_PROOF_STATUS_LEDGER.md`, `UNINET_BOUNDARY_NONCLAIMS.md`, `UNINET_AXIOM_TO_PREDICTION_DAG.md`, `UNINET_NOTATION_UNITS_STANDARD.md`, `UNINET_DUAL_TRACK_FORMALISM_STANDARD.md`.

## 1. Hard-Popper Contract

A matrix row is a core falsifiable only if all conditions below are true.

1. Observable is explicit and operationally measurable.
2. Prediction has a signed direction (up/down/nonzero/zero) against exactly one null baseline.
3. Parameters used by the prediction are either fixed as `none` or pre-locked on disjoint data.
4. Current constraint includes: value, confidence level, source, and date.
5. Forecast constraint includes: instrument/survey, expected sensitivity, and date window.
6. Decision rule is binary (`reject` or `not reject`), with no narrative fallback.
7. Source anchor maps to a concrete statement in `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md`.

Rows failing any condition remain in the matrix as `deferred`.

## 2. Mandatory Row Schema (PredictionRecord v1)

Every row in every section matrix must contain all fields below.

1. `prediction_id`
2. `claim_status` (`theorem` | `postulate` | `deferred`)
3. `source_anchor` (absolute path + line in core docs)
4. `model_equation_or_rule`
5. `observable`
6. `sign_or_direction`
7. `null_model`
8. `current_constraint`
9. `forecast_constraint`
10. `free_parameter_policy` (`none` | `pre-locked-from-disjoint-data`)
11. `decision_rule`
12. `falsifier_statement`

## 3. Field Interpretation Rules

1. `claim_status`
- `theorem`: explicitly claimed as derived in source anchor.
- `postulate`: explicit modeling choice used for testing.
- `deferred`: missing map-to-observable or missing hard thresholds.

2. `source_anchor`
- Format: `C:/SB/UniNet3/docs_input/UNINET_CORE_AXIOMS.md:<line>`.
- Multiple anchors allowed if one line is insufficient.

3. `current_constraint`
- Must include numeric statement and CL when available.
- Must include source and publication date.

4. `forecast_constraint`
- Must include instrument/survey name.
- Must include expected sensitivity and date window.
- If sensitivity is scaling-based, mark it explicitly as inference.

5. `free_parameter_policy`
- `none`: no fitted nuisance/transfer parameter used in this test.
- `pre-locked-from-disjoint-data`: all fitted parameters locked on a non-overlapping dataset before target test.

6. `decision_rule`
- Must be executable as a binary criterion.
- Must define threshold and confidence standard.

## 4. Core Gate and Deferred Gate

Core gate pass requires all of:

1. No vague observable language.
2. No circular fit to the same target dataset.
3. Current and forecast thresholds both present.
4. Concrete source anchor in UniNet core docs.

Deferred gate applies when any core criterion fails:

1. Keep row in section matrix.
2. Set $claim_status = deferred$.
3. Put the missing requirement in `decision_rule` or `falsifier_statement`.

## 5. Quality Gates (Mandatory Review Pass)

1. Completeness check: every core row has all 12 fields filled.
2. Traceability check: each row points to a valid core anchor.
3. Non-circularity check: lock set and target dataset are disjoint for locked rows.
4. Decision check: each row has an explicit reject criterion.
5. Baseline check: each row names exactly one null baseline and one observable family.
6. Red-team check: remove any row without a realistic analysis path.

## 6. Language Discipline

1. Rows are model-risk exposure statements, not advocacy.
2. Do not label consistency-only statements as predictions.
3. No new physical derivations in this phase.
4. Matrix outputs must be decision-complete for the later statistics phase.




