# UniNet Paper 1 - Manuscript Build Plan (Human-Readable + Formal)
Date: 2026-04-02
Status: Active draft plan

## 1) Paper Objective
Write one paper that is readable for a technical generalist and still auditable for a specialist.
The paper must do four things at once:
1. State a minimal core clearly (axioms + role of modeling postulates).
2. Prove what is actually proved, and label what is postulated/deferred.
3. Build intuition using boundary/cut mechanics and observational anchors.
4. Keep formal traceability to governance artifacts (DAG, proof ledger, non-claims).

## 2) Editorial Rules (Hard)
1. Every chapter starts with a human paragraph before formal statements.
2. Every claim block is tagged: `proved`, `postulate`, `deferred`, `external-constraint`.
3. Every theorem used in sector chapters must point back to one canonical statement location.
4. Every major section ends with:
   - what is proved,
   - what is assumed,
   - what remains open.
5. Observation links are illustrative unless the row is a locked falsifiability prediction.
6. Do not duplicate formal content across chapters: every definition/theorem/proof has one canonical home, and other chapters use short summaries plus references.
7. Prefer referencing over restating: if a result is already stated once, later chapters should cite it and only restate the minimum needed for readability.
8. Wherever UniNet touches an established domain, refer to existing literature and make clear whether the paper is reusing, reinterpreting, or extending known structures.
9. Literature references should be strongest in chapter introductions, bridge arguments, and any place where familiar mathematical machinery appears.
10. The document dependency structure should itself be mostly a DAG: later chapters may depend on earlier ones, but logical back-dependence and circular proof flow are not allowed.
11. Forward references are allowed for reader navigation, not for proof dependence.
12. When material is transferred from existing input documents, inherited references to old local labels must be rewritten to the paper's relabeled IDs unless the referenced item intentionally keeps its canonical ID.
13. Source requirement labels such as `R1..R10` are legacy/source aliases only; in the paper they must be rewritten to `REQUIRED-*` labels.
14. Falsifiability statements must appear inside the paper itself, not only in external governance files: the main text carries compact paper-facing falsifiability rows and Appendix B / the source governance files carry the full matrices and audit metadata.
15. The first `InferenceLight` run may be mentioned only as a clearly marked speculative exploratory note; it must not serve as theorem evidence, must not calibrate locked parameters, and must remain clearly separated from core falsifiability rows. If interpreted at all, it may only be described as preliminary compatibility with a Regge-compatible curved-spacetime regime, not as a lock to GR/EFE closure.
16. The manuscript itself must be self-contained: if a definition, theorem statement, or explanatory dependency is needed for readability, copy or restate it cleanly in the paper rather than leaving the reader with internal file-path references.
17. Internal build metadata does not belong in manuscript chapters: no `Source blocks`, no `Source alias` notes, no `Draft status`, and no links or file/line references to `docs_input/*`, `docs/*`, or other repo-internal source documents anywhere in paper prose.
18. Source pickup locations, old-to-new relabel traces, and file/line audit metadata belong in this build plan and related editorial tracking only, not in the manuscript chapters.
19. Core axioms, definitions, theorems, corollaries, and other formal claim blocks should use mathematical language whenever it materially improves precision; plain-language guidance should frame the statement, not replace the formal statement.

## 3) Proposed Document Structure (Final Paper)

## Chapter 0 - Abstract + Reader Guide
Chapter introduction paragraph: state what the paper tries to do and how rigor/readability are balanced.
- 0.1 Abstract: one compact paragraph with the core inevitability claim and strict scope limits.
- 0.2 How to read the paper: explain fast path (intuition) versus full proof path (audit).
- 0.3 Claim-status legend (`proved/postulate/deferred`): define tags so readers can parse certainty level immediately.
- 0.4 Notation, units, and status guide: give readers the symbol canon, unit policy, and status vocabulary needed for the rest of the paper.
- 0.5 Formula presentation rule: explain native UniNet formulas versus optional variational/Lagrangian companion forms.

## Chapter 1 - Human Introduction
Chapter introduction paragraph: motivate the problem in human terms before formalism.
- 1.1 Why this framework exists: describe current conceptual pain points and hidden-assumption overload.
- 1.2 Core intuition: explain updates, cuts, boundaries, and delayed observability with one concrete mental picture.
- 1.3 What this paper does and does not claim: separate theorem-level claims from interpretation and open work.
- 1.4 Roadmap: give chapter-by-chapter reading map and dependency order.

## Chapter 2 - Core Axioms and Modeling Layer
Chapter introduction paragraph: establish the contract of what is foundational versus representational.
- 2.1 Core axioms (`AXIOM-1` ... `AXIOM-10`) explained in plain language: one short intuition line per axiom.
- 2.2 Modeling postulates (`MODEL-P*`, `SM-FOUND-*`, `BRIDGE-P*`) and why they are separate: justify why these are not core.
- 2.3 Immediate consequences: summarize finite propagation, no-information-loss, and relabel invariance outputs.
- 2.4 "No smuggling" statement: prove that sector assumptions are not injected upstream.

## Chapter 3 - Shared Theorem Spine (Before Sectors)
Chapter introduction paragraph: explain that this is the non-negotiable theorem backbone for all sectors.
- 3.1 Reachability, latency, causal order: define causal scaffolding and minimal delay language.
- 3.2 Cut balance and continuity (bulk-boundary): show conservation bookkeeping through boundaries.
- 3.3 Graph cutting primitive and boundary observability: formalize what an external observer can operationally access.
- 3.4 Leaky vs closed boundaries: define leak criteria and physical interpretation of each regime.
- 3.5 Observer-time/coarse-graining and arrow theorem: derive macro arrow from non-injective observation.
- 3.6 Shared theorem summary table (dependencies + status): provide one-page dependency and maturity snapshot.

## Chapter 4 - Boundary/Horizon Mechanics (Core Intuition Chapter)
Chapter introduction paragraph: make boundaries/horizons the central physical interface of the framework.
- 4.1 Graph cuts -> boundaries as operational interface: connect formal cut objects to measurable interfaces.
- 4.2 Delayed boundary representation and external observability limits: explain why delay is structural, not noise.
- 4.3 Stable horizon symmetries and boundary mode selection: show how symmetry constrains admissible modes.
- 4.4 Leaky horizons and implications for black-hole surfaces: describe closure versus leak behavior and signatures.
- 4.5 Boundary mediator interpretation (boson analogue): give the mediator analogy with explicit status tags.
- 4.6 CMB/parity/chirality relevance from boundary channel constraints: connect boundary channel structure to cosmology-facing observables.

## Chapter 5 - Update Function Chapter
Chapter introduction paragraph: constrain the update operator before any sector-specific interpretation.
- 5.1 Why one update family (`AXIOM-4`) and homogeneity (`AXIOM-5`) matter: lock law-uniformity and comparability.
- 5.2 Locality + no-information-loss constraints on admissible $U$: state hard admissibility filters.
- 5.3 Schrodinger-like/discrete wave transport as admissible class: show one constructive witness class exists.
- 5.4 Queue/backpressure constraints and regime handoff conditions: define when transport behavior changes regime.
- 5.5 Non-empty admissible transport family and witness construction: show at least one explicit witness family exists and define what counts as admissible.
- 5.6 What update-function freedom remains (explicitly): list allowed degrees of freedom and non-allowed moves.

## Chapter 6 - Symmetry and Formalism Layer
Chapter introduction paragraph: place symmetry claims and formula styles in one shared location before any sector-specific use.
- 6.1 Symmetry registry and maturity taxonomy: classify items as theorem-level, noether-like, or deferred-noether.
- 6.2 Native and variational companion forms: explain when native notation is primary and when action/Lagrangian form is mandatory.
- 6.3 Noether promotion protocol: define the exact upgrade conditions for symmetry claims to become true Noether theorems.
- 6.4 Cross-sector symmetry placement and non-claims: show where symmetry results are used and where they remain incomplete.

## Chapter 7 - GR Sector
Chapter introduction paragraph: show how GR-like structure emerges from adaptive latency plus projection.
- 7.1 Sector assumption ledger: list exact imports and forbid extra hidden assumptions.
- 7.2 Adaptive latency, trapping, and boundary-dominant release: present the queue/trapping theorem chain.
- 7.3 Projection bridge and geometric interpretation: map transport bookkeeping to geometry-facing observables.
- 7.4 Regge interface proof package: present discrete-to-geometric bridge results and admissibility domain.
- 7.5 Defense of edge-length lower bound ($\ell_e >= 1$ graph units) and Planck mapping rationale: justify lower bound and calibration choice.
- 7.6 Mapping completeness and proof obligations: state what is fully mapped, what is only scaffolded, and what blocks promotion.
- 7.7 Observation anchors: connect to measurable GR tests and expected deviation windows.
- 7.8 GR falsifiability statements: include compact paper-facing prediction rows with explicit nulls and reject criteria.

## Chapter 8 - QM Sector
Chapter introduction paragraph: derive QM-like behavior as the fixed-latency branch of the same update law.
- 8.1 Sector assumption ledger: list the imported structures and regime restrictions explicitly.
- 8.2 Fixed-latency regime and unitarity consequences: establish invariant transport timing regime.
- 8.3 Standing-wave existence proof program (current `docs/20_proofs/qm_sm/...`): present theorem statement and proof flow.
- 8.4 Two-node standing mode (degenerate base case) vs first nontrivial graph-supported family: explain why cycle rank adds genuine graph-supported families.
- 8.5 Schrodinger-like interpretation without extra Hamiltonian postulate: connect discrete update to familiar wave mechanics.
- 8.6 Simulator outlook: boundary-register, qudit, and tensor-network/QECC style realizations as execution pathways rather than theorem claims.
- 8.7 Mapping completeness and proof obligations: show what is proved, what is packaged, and what remains open.
- 8.8 Observation anchors: outline what can be numerically checked now.
- 8.9 QM falsifiability statements: include compact paper-facing prediction rows with explicit nulls and reject criteria.

## Chapter 9 - SM Sector
Chapter introduction paragraph: package particle-structure claims with strict maturity tags.
- 9.1 Sector assumption ledger: show exactly which SM-facing inputs are imported and at what status.
- 9.2 Chiral decomposition and admissibility constraints (`REQUIRED-SM-01..04`): define the allowed mode window.
- 9.3 Particle identity as boundary-stabilized standing-wave class: connect `AXIOM-10` to sector language.
- 9.4 CP/spin-statistics constraints and what remains external/deferred: mark imported versus derived components.
- 9.5 Gauge-as-redundancy placement and symmetry maturity: separate established equivalence from open closure proofs.
- 9.6 CP/CMB chirality overlap box: include the bounded consistency-check link between SM chirality control and cosmology-facing parity observables.
- 9.7 Mapping completeness and proof obligations: state what is currently rigorous and what still needs a derivation route.
- 9.8 Observation anchors (flavor/CP channels): map current constraints to empirical channels.
- 9.9 SM falsifiability statements: include compact paper-facing prediction rows with explicit nulls and reject criteria.

## Chapter 10 - Cosmology Sector
Chapter introduction paragraph: present cosmology as constrained phenomenological packaging, not overclaimed derivation.
- 10.1 Sector assumption ledger: state the imported effective assumptions and their maturity tags.
- 10.2 Phenomenological packaging (DE/DM/Inflation) with explicit status tags: mark each branch as proved/postulate/deferred.
- 10.3 Early black holes and boundary-trapping interpretation: explain early structure channel in UniNet terms.
- 10.4 Last-parsec problem notes (what UniNet can/cannot currently claim): include limits and falsifying conditions.
- 10.5 Computability note: boundary cutting as model-complexity reduction strategy: describe why boundary abstractions can simplify simulation.
- 10.6 Mapping completeness and proof obligations: show what is packaged, what is still missing, and what the forward-model blockers are.
- 10.7 Observation anchors (CMB, LSS, parity channels): tie packaging claims to concrete datasets and point back to the Chapter 9.6 chirality box when relevant.
- 10.8 Cosmology falsifiability statements: include compact paper-facing prediction rows with explicit nulls and reject criteria.

## Chapter 11 - Governance, Audit, and Falsifiability Discipline
Chapter introduction paragraph: show readers how to audit the manuscript line-by-line and how the paper avoids circular self-validation.
- 11.1 Canonical artifact hierarchy and source-of-truth rule: distinguish core sources, governance artifacts, section packaging, and planning-only material.
- 11.2 Axiom-to-prediction DAG walkthrough: trace representative claims from axiom to test.
- 11.3 Proof status ledger integration: synchronize manuscript status tags with governance ledger.
- 11.4 Parameter ledger and disjoint-data lock protocol: explain which parameters are fixed, fit, derived, or deferred and how circular fitting is blocked.
- 11.5 Falsifiability standard and priority test order: summarize decision rules, matrix discipline, and test ordering.
- 11.5A Falsifiability-statement import rule: define how compact paper-facing falsifiability rows are derived from the canonical matrices.
- 11.6 Non-claims boundary and anti-circularity rules: define forbidden reasoning patterns.
- 11.6A Exploratory-results policy: define how `InferenceLight` and other non-canonical numerical outputs may be mentioned without being promoted.
- 11.7 How to audit any claim in the paper to source artifact lines: provide repeatable audit procedure.

## Chapter 12 - Philosophical Chapter
Chapter introduction paragraph: interpret implications without upgrading status of any theorem.
- 12.1 What becomes less mysterious (wave-particle, gauge redundancy, time arrow): summarize explanatory gains.
- 12.2 Ontology vs representation (boundary access limits): separate what exists from what can be observed.
- 12.3 Recursive boundary renormalization / scale ladder: explain the boundary-summary ladder as an interpretive picture, not a new theorem source.
- 12.4 Time, measurement, contextuality, and observer-relative framing: place the philosophy against the actual theorem scaffold.
- 12.5 Limits of interpretation (explicit humility section): mark unresolved metaphysical and formal gaps.
- 12.6 Speculative numerical hints and how to read them: explain how exploratory numerical results may motivate future work without altering theorem status.

## Chapter 13 - Conclusion and Paper-2 Hand-off
Chapter introduction paragraph: close Paper 1 with strict accounting and a forward proof agenda.
- 13.1 Summary of proved spine: list only theorem-backed outcomes.
- 13.2 Summary of open/deferred items: list unresolved claims and blockers.
- 13.3 Exact handoff list to Paper 2 (priority proofs): prioritize next proof packages and dependencies.

## 3A) Planned Appendices and Boxed Inserts

### Appendices
- Editorial-only relabel map: maintained in this build plan and related tracking, not in the reader-facing manuscript.
- Appendix A: full notation, units, and symbol canon for reader lookup.
- Appendix B: full falsifiability matrices and audit metadata for the paper-facing compact rows, plus parameter-lock and proof-status governance tables.
- Appendix C: proof-note index for long proofs kept outside the main narrative flow.
- Appendix D: speculative numerical/exploratory notes index (`InferenceLight`, early scans, and non-canonical fit experiments) with explicit non-evidentiary status.

### Boxed inserts
- Box 1: CP/CMB chirality overlap consistency check.
- Box 2: Quantum simulator / boundary-register outlook.
- Box 3: Recursive boundary renormalization ladder.

## 3B) Paragraph-Level Execution Queue

Global transfer rule for all paragraph tasks:
- [ ] If source text refers to legacy/local labels from `docs_input` or proof notes, rewrite those references to the paper's relabeled names during transfer.
- [ ] Old source labels and file-line pickups stay in the build plan or separate editorial audit notes, not in manuscript prose.
- [ ] Canonical IDs that remain unchanged (`AXIOM-*`, `MODEL-P*`, `SM-FOUND-*`, `BRIDGE-P*`, `NS-*`) may be kept as-is; source `R*` labels must be rewritten to `REQUIRED-*`.

### Chapter 0 Execution Queue
- [x] `P0-I` Chapter 0 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:9-165`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:6-22`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-21`; transfer the paper contract: readable core, audited proof path, status tags, and observable-facing discipline; no relabeling in this paragraph.
- [x] `P0.1` Abstract: pickup `docs_input/UNINET_CORE_AXIOMS.md:142-165`, `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:156-162`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:6-39`; transfer the core inevitability claim, the update/boundary mechanism, and strict scope limits; cite `AXIOM-1..AXIOM-10` collectively and do not restate proofs.
- [x] `P0.2` How to read the paper: pickup `docs_input/UNINET_NOTATION_UNITS_STANDARD.md:7-99`, `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG_v2.md:4-35`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:23-62`; transfer the fast path versus full audit path and how readers should traverse the DAG-shaped manuscript; no relabeling.
- [x] `P0.3` Claim-status legend: pickup `docs_input/UNINET_NOTATION_UNITS_STANDARD.md:65-78`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:6-12`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:13-19`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:40-67`; transfer the meaning of `proved`, `postulate`, `deferred`, `external-constraint`, `noether-like`, and language discipline; no relabeling.
- [x] `P0.4` Notation, units, and status guide: pickup `docs_input/UNINET_NOTATION_UNITS_STANDARD.md:7-99`, `docs_input/UNINET_CORE_AXIOMS.md:166-205`; transfer the symbol canon, unit policy, math formatting, and cross-document compliance rules; no relabeling.
- [x] `P0.5` Formula presentation rule: pickup `docs_input/UNINET_DUAL_TRACK_FORMALISM_STANDARD.md:6-50`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:32-54`, `docs_input/UNINET_CORE_AXIOMS.md:1007-1079`; transfer the native-versus-variational formula policy and when Lagrangian form is mandatory; prepare later references to `FORM-01` and `FORM-02`.

### Chapter 1 Execution Queue
- [x] `P1-I` Chapter 1 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:9-141`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION_PLAN.md:6-40`; transfer the human motivation and why this framework is trying to reduce hidden assumptions rather than add more sector models; no relabeling.
- [x] `P1.1` Why this framework exists: pickup `docs_input/UNINET_CORE_AXIOMS.md:57-141`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:13-80`; transfer the paradox/motivation setup, especially hidden assumptions about time, access, and sector splits; no relabeling.
- [x] `P1.2` Core intuition: pickup `docs_input/UNINET_CORE_AXIOMS.md:13-56`, `docs_input/UNINET_CORE_AXIOMS.md:114-141`, `docs_input/UNINET_SNIPPETS.md:20-31`; transfer the update/cut/boundary/delayed-observability picture and re-anchor any wording from `UNINET_SNIPPETS.md` to the canonical core text before use; no relabeling.
- [x] `P1.3` What this paper does and does not claim: pickup `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:6-67`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:23-62`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:81-99`; transfer the claim boundary, promotion rules, and open-work framing; no relabeling.
- [x] `P1.4` Roadmap: pickup `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:14-132`, `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG_v2.md:11-35`; transfer the chapter-by-chapter dependency order and explain that the paper mirrors a mostly forward DAG; no relabeling.

### Chapter 2 Execution Queue
- [x] `P2-I` Chapter 2 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:206-352`, `docs_input/UNINET_CORE_AXIOMS.md:211-224`; transfer the distinction between foundational axioms and representation/modeling choices; no relabeling.
- [x] `P2.1` Core axioms explained in plain language: pickup `docs_input/UNINET_CORE_AXIOMS.md:225-352`, `docs_input/UNINET_CORE_AXIOMS.md:932-945`, `docs_input/UNINET_CORE_AXIOMS.md:1441-1459`; transfer one plain-language sentence per canonical axiom; keep `AXIOM-1..AXIOM-10` unchanged and do not relabel.
- [x] `P2.2` Modeling postulates and why they are separate: pickup `docs_input/UNINET_CORE_AXIOMS.md:265-352`, `docs_input/UNINET_CORE_AXIOMS.md:1085-1150`; transfer why `MODEL-P1`, `MODEL-P2`, `SM-FOUND-A1`, and `BRIDGE-P1..BRIDGE-P3` are useful but not core; keep their canonical IDs unchanged.
- [x] `P2.3` Immediate consequences: pickup `docs_input/UNINET_CORE_AXIOMS.md:361-453`, `docs_input/UNINET_CORE_AXIOMS.md:755-770`, `docs_input/UNINET_CORE_AXIOMS.md:932-985`; transfer finite propagation, continuity, relabel invariance, and norm conservation as immediate outputs; preview later references to `LEMMA-SH-01`, `THEOREM-SH-01`, and `AXIOM-2` without duplicating proofs.
- [x] `P2.4` No-smuggling statement: pickup `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:14-132`, `docs_input/UNINET_QM_SECTION.md:14-25`, `docs_input/UNINET_GR_SECTION.md:16-28`, `docs_input/UNINET_SM_SECTION.md:14-24`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:14-24`; transfer the argument that sector assumptions are ledgered downstream rather than hidden upstream; no relabeling.

### Chapter 3 Execution Queue
- [x] `P3-I` Chapter 3 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:353-752`, `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:102-132`; transfer that this chapter is the shared theorem spine all sectors depend on; no relabeling.
- [x] `P3.1` Reachability, latency, causal order: pickup `docs_input/UNINET_CORE_AXIOMS.md:359-399`, `docs_input/UNINET_CORE_AXIOMS.md:577-645`; transfer the causal/latency scaffold; import and relabel `Lemma 1.1 -> LEMMA-SH-01`, `Definition 1.1 -> DEFINITION-SH-01`, `Lemma 1.2 -> LEMMA-SH-02`, `Definition 2.1 -> DEFINITION-SH-03`, `Lemma 2.1 -> LEMMA-SH-03`, `Definition 2.2 -> DEFINITION-SH-04`, `Lemma 2.2 -> LEMMA-SH-04`, `Proposition 2.1 -> PROPOSITION-SH-01`.
- [x] `P3.2` Cut balance and continuity: pickup `docs_input/UNINET_CORE_AXIOMS.md:400-453`; transfer continuity, boundary flux bookkeeping, and exact closure with bookkeeping; import and relabel `Definition 1.2 -> DEFINITION-SH-02`, `Theorem 1.1 -> THEOREM-SH-01`, `Corollary 1.1 -> COROLLARY-SH-01`.
- [x] `P3.3` Graph cutting primitive and boundary observability: pickup `docs_input/UNINET_CORE_AXIOMS.md:440-481`; transfer the operational boundary register, graph cut primitive, and leakiness setup; keep `AXIOM-9` and `AXIOM-8` unchanged, cite `Definition 1.5` by source alias, and import `Theorem 1.2 -> THEOREM-SH-02`.
- [x] `P3.4` Leaky vs closed boundaries: pickup `docs_input/UNINET_CORE_AXIOMS.md:475-576`, `docs_input/QUEUEING_RIGOR_PLAN.md:89-98`; transfer exact closure versus quasi-closure, leakiness, and the physical interpretation of boundary release; reference `THEOREM-SH-02` here and defer the full trapping/release proof chain to `THEOREM-GR-01`, `THEOREM-GR-02`, and `COROLLARY-GR-01` in Chapter 7.
- [x] `P3.5` Observer-time, coarse-graining, and arrow theorem: pickup `docs_input/UNINET_CORE_AXIOMS.md:648-744`, `docs_input/UNINET_SNIPPETS.md:102-110`; transfer observer time, coarse-graining, and the emergent arrow, re-anchoring any snippet paraphrase to the theorem text; import and relabel `Definition 3.1 -> DEFINITION-SH-05`, `Lemma 3.1 -> LEMMA-SH-05`, `Definition 3.2 -> DEFINITION-SH-06`, `Definition 3.3 -> DEFINITION-SH-07`, `Definition 3.4 -> DEFINITION-SH-08`, `Theorem 3.2 -> THEOREM-SH-03`, `Corollary 3.1 -> COROLLARY-SH-02`, `Corollary 3.2 -> COROLLARY-SH-03`, `Corollary 3.3 -> COROLLARY-SH-04`.
- [x] `P3.6` Shared theorem summary table: pickup `docs_input/UNINET_PROOF_STATUS_LEDGER.md:23-62`, `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:14-132`; transfer the dependency and maturity summary for the shared theorem spine; no new relabeling beyond the imported `SH` IDs.

### Chapter 4 Execution Queue
- [x] `P4-I` Chapter 4 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:440-481`, `docs_input/UNINET_CORE_AXIOMS.md:1328-1493`; transfer the claim that boundaries/horizons are the operational interface of the framework; no relabeling.
- [x] `P4.1` Graph cuts -> boundaries as operational interface: pickup `docs_input/UNINET_CORE_AXIOMS.md:465-481`, `docs_input/UNINET_CORE_AXIOMS.md:1390-1402`; transfer the move from graph cuts to operational interfaces; keep `AXIOM-8` and `AXIOM-9` unchanged and import `Definition 1B.1 -> DEFINITION-BND-05`, `Theorem 1B.1 -> THEOREM-BND-04`.
- [x] `P4.2` Delayed boundary representation and observability limits: pickup `docs_input/UNINET_CORE_AXIOMS.md:440-453`, `docs_input/UNINET_CORE_AXIOMS.md:697-729`, `docs_input/UNINET_CORE_AXIOMS.md:1390-1402`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:33-61`; transfer why delayed representation is structural and why observation is boundary-limited; reference `AXIOM-9`, `THEOREM-SH-03`, and `THEOREM-BND-04` without duplicating their proofs.
- [x] `P4.3` Stable horizon symmetries and boundary mode selection: pickup `docs_input/UNINET_CORE_AXIOMS.md:1330-1378`, `docs_input/UNINET_CORE_AXIOMS.md:1409-1438`; transfer bandwidth growth, effective dimension, symmetry capacity, and mode-selection logic; import and relabel `Definition 1A.1 -> DEFINITION-BND-01`, `Definition 1A.2 -> DEFINITION-BND-02`, `Theorem 1A.1 -> THEOREM-BND-01`, `Definition 1A.3 -> DEFINITION-BND-03`, `Definition 1A.4 -> DEFINITION-BND-04`, `Theorem 1A.2 -> THEOREM-BND-02`, `Theorem 1A.3 -> THEOREM-BND-03`.
- [x] `P4.4` Leaky horizons and black-hole surfaces: pickup `docs_input/UNINET_CORE_AXIOMS.md:475-576`, `docs_input/UNINET_GR_SECTION.md:109-130`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:10-67`; transfer closure versus leak behavior, black-hole surface implications, and explicit non-claims; reference `THEOREM-SH-02`, `THEOREM-GR-02`, and `COROLLARY-GR-01` without restating the full proofs.
- [x] `P4.5` Boundary mediator interpretation: pickup `docs_input/UNINET_CORE_AXIOMS.md:1403-1438`, `docs_input/UNINET_CORE_AXIOMS.md:1460-1493`; transfer the mediator/horizon-boson analogy with status tags and literature anchors; import and relabel `Theorem 1B.2 -> THEOREM-BND-05`, `Theorem 1B.3 -> THEOREM-BND-06`, `Theorem 1B.4 -> THEOREM-BND-07`, `Theorem 1B.5 -> THEOREM-BND-08`, `Theorem 1B.6 -> THEOREM-BND-09`, `Theorem 1B.7 -> THEOREM-BND-10`.
- [x] `P4.6` CMB/parity/chirality relevance from boundary channel constraints: pickup `docs_input/UNINET_CORE_AXIOMS.md:792-900`, `docs_input/UNINET_CORE_AXIOMS.md:1219-1255`, `docs_input/UNINET_CP_CMB_CHIRALITY_OVERLAP_NOTE.md:26-102`, `docs_input/UNINET_CORE_AXIOMS.md:1460-1493`; transfer the cross-sector relevance of chirality and parity constraints while keeping the phenomenology status-tagged; reference `REQUIRED-SM-01..04`, `BOX-SM-01`, and `PROPOSITION-COS-01..03`.

### Chapter 5 Execution Queue
- [x] `P5-I` Chapter 5 introduction paragraph: pickup `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:5-162`, `docs_input/QUEUEING_RIGOR_PLAN.md:22-129`; transfer that the update operator must be constrained before any sector packaging is allowed; no relabeling.
- [x] `P5.1` Why one update family and homogeneity matter: pickup `docs_input/UNINET_CORE_AXIOMS.md:243-264`, `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:17-22`; transfer why law-uniformity and update homogeneity are non-negotiable; keep `AXIOM-4` and `AXIOM-5` unchanged.
- [x] `P5.2` Locality + no-information-loss constraints on admissible `U`: pickup `docs_input/UNINET_CORE_AXIOMS.md:280-313`, `docs_input/UNINET_CORE_AXIOMS.md:755-791`, `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:27-56`; transfer the hard admissibility filters from locality, unitarity, and no phenomenological delays; keep `AXIOM-6` and `AXIOM-7` unchanged and import and relabel `R1 -> REQUIRED-UPD-01`, `R2 -> REQUIRED-UPD-02`, `R3 -> REQUIRED-UPD-03`, `R4 -> REQUIRED-UPD-04`.
- [x] `P5.3` Schrodinger-like/discrete wave transport as admissible class: pickup `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:85-162`, `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:16-120`, `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:326-358`; transfer wave/wavelet transport, one-dimensional update, and literature placement; reference `THEOREM-QM-02` as the constructive witness and do not restate the full standing-wave proof here.
- [x] `P5.4` Queue/backpressure constraints and regime handoff conditions: pickup `docs_input/UNINET_CORE_AXIOMS.md:495-576`, `docs_input/UNINET_CORE_AXIOMS.md:901-927`, `docs_input/QUEUEING_RIGOR_PLAN.md:42-98`; transfer queue/backpressure constraints, regime handoff, and the physical regime picture; reference `THEOREM-GR-01`, `THEOREM-GR-02`, and `COROLLARY-GR-01` without duplicating their proofs.
- [x] `P5.5` Non-empty admissible transport family and witness construction: pickup `docs_input/QUEUEING_RIGOR_PLAN.md:29-41`, `docs_input/QUEUEING_RIGOR_PLAN.md:74-111`, `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:88-320`, `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:425-680`; transfer the requirement that the admissible transport set is non-empty and that explicit witness families exist; reference `THEOREM-QM-02`, `THEOREM-GR-06`, and `THEOREM-GR-07`.
- [x] `P5.6` What update-function freedom remains: pickup `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:57-155`, `docs_input/UNINET_PARAMETER_LEDGER.md:30-79`, `docs_input/UNINET_QM_SECTION.md:90-95`, `docs_input/UNINET_GR_SECTION.md:147-174`, `docs_input/UNINET_SM_SECTION.md:116-121`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:108-113`; transfer what remains free, what is parameterized, and what is still deferred; no new relabeling.

### Chapter 6 Execution Queue
- [ ] `P6-I` Chapter 6 introduction paragraph: pickup `docs_input/UNINET_CORE_AXIOMS.md:928-1079`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:7-72`, `docs_input/UNINET_DUAL_TRACK_FORMALISM_STANDARD.md:6-50`; transfer why symmetry and formula style need one shared chapter before the sectors; no relabeling.
- [ ] `P6.1` Symmetry registry and maturity taxonomy: pickup `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:13-31`, `docs_input/UNINET_NOETHER_SYMMETRY_PROGRAM.md:13-30`, `docs_input/UNINET_CORE_AXIOMS.md:932-998`; transfer the registry and maturity taxonomy for symmetry claims; keep `NS-001..NS-007` unchanged.
- [ ] `P6.2` Native and variational companion forms: pickup `docs_input/UNINET_DUAL_TRACK_FORMALISM_STANDARD.md:6-50`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:32-44`, `docs_input/UNINET_CORE_AXIOMS.md:1007-1079`; transfer when native notation is primary and when a Lagrangian/action companion is required; import `FORM-02`.
- [ ] `P6.3` Noether promotion protocol: pickup `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:45-54`, `docs_input/UNINET_NOETHER_SYMMETRY_PROGRAM.md:31-56`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:48-62`; transfer the exact upgrade conditions for turning a noether-like statement into a full theorem; import `FORM-01`.
- [ ] `P6.4` Cross-sector symmetry placement and non-claims: pickup `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:55-72`, `docs_input/UNINET_QM_SECTION.md:73-83`, `docs_input/UNINET_GR_SECTION.md:70-108`, `docs_input/UNINET_SM_SECTION.md:70-115`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:66-98`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:10-67`; transfer where symmetry claims are used, where they stop, and how status tags prevent overclaiming; reference `NS-*`, `FORM-01`, and `FORM-02`.

### Chapter 7 Execution Queue
- [ ] `P7-I` Chapter 7 introduction paragraph: pickup `docs_input/UNINET_GR_SECTION.md:8-28`, `docs_input/UNINET_CORE_AXIOMS.md:1080-1218`; transfer the GR branch contract and why adaptive latency plus projection are the only inputs being used; no relabeling.
- [ ] `P7.1` Sector assumption ledger: pickup `docs_input/UNINET_GR_SECTION.md:16-28`, `docs_input/UNINET_GR_SECTION_RIGOR_PLAN.md:24-65`; transfer the GR assumption ledger, dependency graph, and allowed imports; no relabeling.
- [ ] `P7.2` Adaptive latency, trapping, and boundary-dominant release: pickup `docs_input/UNINET_CORE_AXIOMS.md:495-576`, `docs_input/UNINET_CORE_AXIOMS.md:1200-1218`, `docs_input/UNINET_CORE_AXIOMS.md:901-927`, `docs_input/UNINET_GR_SECTION.md:109-121`; transfer the queue/trapping theorem chain; import and relabel `Theorem 1.3 -> THEOREM-GR-01`, `Theorem 1.4 -> THEOREM-GR-02`, `Corollary 1.2 -> COROLLARY-GR-01`, `Theorem: GR Latency -> THEOREM-GR-04`.
- [ ] `P7.3` Projection bridge and geometric interpretation: pickup `docs_input/UNINET_CORE_AXIOMS.md:1085-1161`, `docs_input/UNINET_GR_SECTION.md:47-69`; transfer the projection bridge, proper-time setup, and geometry coupling; keep `BRIDGE-P1..BRIDGE-P3` unchanged and import `Theorem 4.1 -> THEOREM-GR-03`.
- [ ] `P7.4` Regge interface proof package: pickup `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:205-363`, `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:425-680`, `docs_input/UNINET_GR_SECTION.md:131-146`; transfer the delay-to-length bridge and Regge admissibility domain; import and relabel `Theorem 8.1 -> THEOREM-GR-05`, `Theorem 8.4B -> THEOREM-GR-06`, `Theorem 8.5 -> THEOREM-GR-07`.
- [ ] `P7.5` Defense of edge-length lower bound and Planck mapping rationale: pickup `docs_input/UNINET_CORE_AXIOMS.md:1139-1150`, `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:95-205`, `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:425-680`, `docs_input/UNINET_PARAMETER_LEDGER.md:30-79`; transfer why `\ell_e >= 1` graph units is the microscopic lower-bound choice and why the Planck mapping is the current calibration convention; reference `BRIDGE-P3` and `THEOREM-GR-05..07`.
- [ ] `P7.6` Mapping completeness and proof obligations: pickup `docs_input/UNINET_GR_SECTION.md:131-188`, `docs_input/UNINET_GR_SECTION_RIGOR_PLAN.md:111-209`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:6-14`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:31-40`; transfer what is fully mapped, what remains scaffolded, and what still blocks theorem promotion; no new relabeling.
- [ ] `P7.7` Observation anchors: pickup `docs_input/UNINET_GR_SECTION.md:189-210`, `docs_input/UNINET_GR_FALSIFIABILITY_MATRIX.md:1-36`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:35-54`; transfer the GR observation hooks and priority tests; no relabeling.
- [ ] `P7.8` GR falsifiability statements: pickup `docs_input/UNINET_GR_FALSIFIABILITY_MATRIX.md:1-36`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-59`; transfer the paper-facing GR falsifiability rows, including observable, null baseline, decision rule, and falsifier statement; keep only compact rows in the main text and place the full matrix plus audit metadata in Appendix B / source governance files.

### Chapter 8 Execution Queue
- [ ] `P8-I` Chapter 8 introduction paragraph: pickup `docs_input/UNINET_QM_SECTION.md:7-25`, `docs_input/UNINET_CORE_AXIOMS.md:1181-1197`, `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:57-124`; transfer the QM branch contract and why fixed latency is the relevant regime split; no relabeling.
- [ ] `P8.1` Sector assumption ledger: pickup `docs_input/UNINET_QM_SECTION.md:14-25`, `docs_input/UNINET_QM_SECTION_RIGOR_PLAN.md:24-63`; transfer the QM assumption ledger and scope lock; no relabeling.
- [ ] `P8.2` Fixed-latency regime and unitarity consequences: pickup `docs_input/UNINET_CORE_AXIOMS.md:280-313`, `docs_input/UNINET_CORE_AXIOMS.md:1181-1197`, `docs_input/UNINET_QM_SECTION.md:28-45`; transfer fixed latency, locality, and unitarity in the QM regime; import and relabel `Theorem: QM Latency -> THEOREM-QM-01`.
- [ ] `P8.3` Standing-wave existence proof program: pickup `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:86-358`, `docs_input/UNINET_CORE_AXIOMS.md:1441-1459`; transfer the theorem statement and proof flow; keep `AXIOM-10` unchanged and import and relabel `Theorem E1 -> THEOREM-QM-02`, `Lemma L1 -> LEMMA-QM-01`, `Lemma L2 -> LEMMA-QM-02`, `Lemma L3 -> LEMMA-QM-03`, `Lemma L3A -> LEMMA-QM-04`, `Lemma L4 -> LEMMA-QM-05`, `Lemma L5 -> LEMMA-QM-06`, `Lemma L6 -> LEMMA-QM-07`.
- [ ] `P8.4` Two-node standing mode vs first nontrivial graph-supported family: pickup `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:165-320`; transfer the degenerate two-node witness versus the first nontrivial cycle-supported family; reference `LEMMA-QM-03..07` without duplicating their proofs.
- [ ] `P8.5` Schrodinger-like interpretation without extra Hamiltonian postulate: pickup `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:105-162`, `docs_input/UNINET_QM_SECTION.md:96-103`, `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:326-358`, `docs_input/UNINET_CORE_AXIOMS.md:1258-1262`; transfer the literature-oriented comparison to quantum walks and discrete Schr-like evolution; no new relabeling.
- [ ] `P8.6` Simulator outlook: pickup `docs_input/UNINET_QUANTUM_SIMULATOR.md:1-93`; transfer the boundary-register, qudit, and tensor-network/QECC outlook as a box or short outlook paragraph only; no relabeling.
- [ ] `P8.7` Mapping completeness and proof obligations: pickup `docs_input/UNINET_QM_SECTION.md:90-117`, `docs_input/UNINET_QM_SECTION_RIGOR_PLAN.md:81-150`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:10-67`; transfer what is proved, what is only packaged, and what remains deferred; no new relabeling.
- [ ] `P8.8` Observation anchors and simulator pathways: pickup `docs_input/UNINET_QM_SECTION.md:118-127`, `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:1-27`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:35-44`; transfer the QM-facing tests and simulator-facing checks; no relabeling.
- [ ] `P8.9` QM falsifiability statements: pickup `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:1-27`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-59`; transfer the paper-facing QM falsifiability rows, including signed prediction direction, decision rule, and falsifier statement; keep only compact rows in the main text and place the full matrix plus audit metadata in Appendix B / source governance files.

### Chapter 9 Execution Queue
- [ ] `P9-I` Chapter 9 introduction paragraph: pickup `docs_input/UNINET_SM_SECTION.md:7-24`, `docs_input/UNINET_CORE_AXIOMS.md:333-352`, `docs_input/UNINET_CORE_AXIOMS.md:792-900`, `docs_input/UNINET_CORE_AXIOMS.md:1439-1459`; transfer the SM branch contract and its status-tagged scope; no relabeling.
- [ ] `P9.1` Sector assumption ledger: pickup `docs_input/UNINET_SM_SECTION.md:14-24`, `docs_input/UNINET_SM_SECTION_RIGOR_PLAN.md:26-59`; transfer the SM assumption ledger and scope lock; no relabeling.
- [ ] `P9.2` Chiral decomposition and admissibility constraints: pickup `docs_input/UNINET_CORE_AXIOMS.md:333-352`, `docs_input/UNINET_CORE_AXIOMS.md:792-900`, `docs_input/UNINET_SM_SECTION.md:38-64`; transfer the chiral mode taxonomy and admissible transfer window; keep `SM-FOUND-A1` unchanged and import and relabel `R5 -> REQUIRED-SM-01`, `R6 -> REQUIRED-SM-02`, `R7 -> REQUIRED-SM-03`, `R8 -> REQUIRED-SM-04`.
- [ ] `P9.3` Particle identity as boundary-stabilized standing-wave class: pickup `docs_input/UNINET_CORE_AXIOMS.md:1439-1459`, `docs_input/UNINET_SM_SECTION.md:27-55`, `docs_input/UNINET_SM_SECTION.md:94-104`, `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:88-320`; transfer the move from standing-wave existence to particle identity; keep `AXIOM-10` unchanged and reference `THEOREM-QM-02`.
- [ ] `P9.4` CP/spin-statistics constraints and what remains external/deferred: pickup `docs_input/UNINET_CORE_AXIOMS.md:833-877`, `docs_input/UNINET_SM_SECTION.md:56-80`; transfer the CP and spin-statistics constraints together with their maturity boundaries; reference `REQUIRED-SM-02` and `REQUIRED-SM-03`.
- [ ] `P9.5` Gauge-as-redundancy placement and symmetry maturity: pickup `docs_input/UNINET_CORE_AXIOMS.md:1390-1402`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:20-61`, `docs_input/UNINET_SM_SECTION.md:70-115`; transfer gauge-as-redundancy and distinguish proved equivalence from open Noether closure; reference `THEOREM-BND-04`, `NS-004`, and `NS-006`.
- [ ] `P9.6` CP/CMB chirality overlap box: pickup `docs_input/UNINET_CP_CMB_CHIRALITY_OVERLAP_NOTE.md:8-102`, `docs_input/UNINET_SM_SECTION.md:122-152`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:114-147`; transfer the bounded scale-level consistency check and all caveats; import `BOX-SM-01`.
- [ ] `P9.7` Mapping completeness and proof obligations: pickup `docs_input/UNINET_SM_SECTION.md:116-143`, `docs_input/UNINET_SM_SECTION_RIGOR_PLAN.md:77-142`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:23-30`; transfer what is rigorous, what remains deferred, and what derivation route is still missing; no new relabeling.
- [ ] `P9.8` Observation anchors: pickup `docs_input/UNINET_SM_SECTION.md:144-152`, `docs_input/UNINET_SM_FALSIFIABILITY_MATRIX.md:1-28`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:35-44`; transfer the flavor/CP observation anchors and priority tests; no relabeling.
- [ ] `P9.9` SM falsifiability statements: pickup `docs_input/UNINET_SM_FALSIFIABILITY_MATRIX.md:1-28`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-59`; transfer the paper-facing SM falsifiability rows, including observable, null baseline, decision rule, and falsifier statement; keep only compact rows in the main text and place the full matrix plus audit metadata in Appendix B / source governance files.

### Chapter 10 Execution Queue
- [ ] `P10-I` Chapter 10 introduction paragraph: pickup `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:7-24`, `docs_input/UNINET_CORE_AXIOMS.md:1219-1255`; transfer the cosmology branch contract and its status-tagged packaging discipline; no relabeling.
- [ ] `P10.1` Sector assumption ledger: pickup `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:14-24`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION_RIGOR_PLAN.md:26-65`; transfer the cosmology assumption ledger and scope lock; no relabeling.
- [ ] `P10.2` Phenomenological packaging (DE/DM/Inflation): pickup `docs_input/UNINET_CORE_AXIOMS.md:1223-1255`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:27-60`; transfer the packaged DE/DM/inflation branches with explicit status tags; import and relabel `Dark Energy -> PROPOSITION-COS-01`, `Dark Matter -> PROPOSITION-COS-02`, `Inflation -> PROPOSITION-COS-03`.
- [ ] `P10.3` Early black holes and boundary-trapping interpretation: pickup `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:82-98`, `docs_input/UNINET_GR_SECTION.md:122-130`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:6-14`; transfer the early-BH/boundary-trapping story as an explicitly deferred phenomenology layer; no new relabeling.
- [ ] `P10.4` Last-parsec problem notes: pickup `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:15-22`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:71-98`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION_RIGOR_PLAN.md:112-126`; transfer what UniNet can and cannot currently say about last-parsec and dark-sector detection interfaces; no relabeling.
- [ ] `P10.5` Computability note: pickup `docs_input/UNINET_SNIPPETS.md:39-91`, `docs_input/UNINET_CORE_AXIOMS.md:422-481`, `docs_input/UNINET_CORE_AXIOMS.md:697-729`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:82-98`; transfer the boundary-cut/compression intuition only after re-anchoring it to cut balance and coarse-graining theorems; no relabeling.
- [ ] `P10.6` Mapping completeness and proof obligations: pickup `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:108-137`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION_RIGOR_PLAN.md:84-159`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:15-22`; transfer the forward-model blockers and promotion gates; no relabeling.
- [ ] `P10.7` Observation anchors: pickup `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:138-147`, `docs_input/UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md:1-34`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:35-44`, `docs_input/UNINET_CP_CMB_CHIRALITY_OVERLAP_NOTE.md:26-102`; transfer the observation anchors and point back to `BOX-SM-01` where relevant; no relabeling.
- [ ] `P10.8` Cosmology falsifiability statements: pickup `docs_input/UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md:1-34`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-59`; transfer the paper-facing cosmology falsifiability rows, including signed branch pattern, decision rule, and falsifier statement; keep only compact rows in the main text and place the full matrix plus audit metadata in Appendix B / source governance files.

### Chapter 11 Execution Queue
- [x] `P11-I` Chapter 11 introduction paragraph: pickup `docs_input/UNINET_ARTIFACT_CLASSIFICATION.md:5-15`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:1-62`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-101`; transfer the governance/audit contract and anti-circularity stance; no relabeling.
- [x] `P11.1` Canonical artifact hierarchy and source-of-truth rule: pickup `docs_input/UNINET_ARTIFACT_CLASSIFICATION.md:5-15`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:6-27`; transfer the artifact hierarchy and what counts as canonical, governance, packaging, or planning-only material; import `GOV-01`.
- [x] `P11.2` Axiom-to-prediction DAG walkthrough: pickup `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:7-132`, `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG_v2.md:4-35`; transfer a sample end-to-end audit path from axiom to prediction; import `GOV-02`.
- [x] `P11.3` Proof status ledger integration: pickup `docs_input/UNINET_PROOF_STATUS_LEDGER.md:6-62`; transfer status vocabulary, ledger synchronization, and promotion queue discipline; import `GOV-03`.
- [x] `P11.4` Parameter ledger and disjoint-data lock protocol: pickup `docs_input/UNINET_PARAMETER_LEDGER.md:8-92`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-81`; transfer fixed/fit/derived/deferred parameter discipline, reduced fit basis, and disjoint-data lock policy; import `GOV-04`.
- [x] `P11.5` Falsifiability standard and priority test order: pickup `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-101`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:28-65`, `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:1-27`, `docs_input/UNINET_GR_FALSIFIABILITY_MATRIX.md:1-36`, `docs_input/UNINET_SM_FALSIFIABILITY_MATRIX.md:1-28`, `docs_input/UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md:1-34`; transfer the matrix discipline, decision rules, and priority order for testing; import `GOV-05` and `GOV-06`.
- [x] `P11.5A` Falsifiability-statement import rule: pickup `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:8-59`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:22-44`; transfer the explicit manuscript rule that each sector chapter must carry compact falsifiability statements in-paper, while Appendix B and the source governance files preserve the full matrices and audit metadata; reference `GOV-05` and `GOV-06`.
- [x] `P11.6` Non-claims boundary and anti-circularity rules: pickup `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:6-67`, `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md:62-72`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:81-99`; transfer the anti-circularity and language-discipline rules; import `GOV-07`.
- [x] `P11.6A` Exploratory-results policy (`InferenceLight`, early fits, scan outputs): pickup `docs_input/UNINET_SNIPPETS.md:114-140`, `docs_input/UNINET_ARTIFACT_CLASSIFICATION.md:5-15`, `docs_input/UNINET_PARAMETER_LEDGER.md:8-29`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:6-39`; transfer the rule that the first `InferenceLight` run and any similar exploratory numerical outputs may be mentioned only as speculative/non-canonical notes and may not be used as proof evidence, locked calibration, or falsifiability-row support unless formally promoted; if a one-line interpretation is included, state it only as preliminary compatibility with a Regge-compatible curved-spacetime regime and explicitly not as GR/EFE lock-in.
- [x] `P11.7` How to audit any claim in the paper: pickup `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG.md:116-132`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:43-62`, `docs_input/UNINET_FALSIFIABILITY_STANDARD.md:22-38`, `docs_input/UNINET_PARAMETER_LEDGER.md:15-29`; transfer a repeatable theorem-to-observable audit procedure; no new relabeling.

### Chapter 12 Execution Queue
- [x] `P12-I` Chapter 12 introduction paragraph: pickup `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION_PLAN.md:6-71`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:7-99`, `docs_input/UNINET_SNIPPETS.md:17-110`, `docs_input/UNINET_CORE_AXIOMS.md:706-744`; transfer the philosophy contract: interpretation must be theorem-grounded and may not upgrade theorem status; no relabeling.
- [x] `P12.1` What becomes less mysterious: pickup `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:62-80`, `docs_input/UNINET_SNIPPETS.md:17-30`, `docs_input/UNINET_SNIPPETS.md:102-110`, `docs_input/UNINET_CORE_AXIOMS.md:706-744`, `docs_input/UNINET_CORE_AXIOMS.md:1397-1459`; transfer the demystification of wave-particle, gauge redundancy, and time arrow, re-anchoring snippet language to canonical sources; no new relabeling beyond cited theorem IDs.
- [x] `P12.2` Ontology vs representation: pickup `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:33-61`, `docs_input/UNINET_SNIPPETS.md:24-31`, `docs_input/UNINET_CORE_AXIOMS.md:440-453`, `docs_input/UNINET_CORE_AXIOMS.md:697-729`, `docs_input/UNINET_CORE_AXIOMS.md:1390-1402`; transfer the distinction between what exists and what can be observed through boundaries; no relabeling.
- [x] `P12.3` Recursive boundary renormalization / scale ladder: pickup `docs_input/UNINET_SNIPPETS.md:39-91`, `docs_input/UNINET_CORE_AXIOMS.md:422-481`, `docs_input/UNINET_CORE_AXIOMS.md:1328-1438`; transfer the scale-ladder picture as boxed intuition only, re-anchored to cut-balance and boundary-capacity theorems; reference `THEOREM-SH-01`, `THEOREM-BND-01..10`.
- [x] `P12.4` Time, measurement, contextuality, and observer-relative framing: pickup `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:13-70`, `docs_input/UNINET_SNIPPETS.md:7-13`, `docs_input/UNINET_SNIPPETS.md:20-31`, `docs_input/UNINET_CORE_AXIOMS.md:697-744`, `docs_input/UNINET_QM_SECTION.md:55-77`; transfer the measurement/time/contextuality framing with explicit status discipline; no relabeling.
- [x] `P12.5` Limits of interpretation: pickup `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:81-99`, `docs_input/UNINET_BOUNDARY_NONCLAIMS.md:10-67`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:48-62`; transfer explicit philosophical non-claims, formal gaps, and upgrade conditions; no relabeling.
- [x] `P12.6` Speculative numerical hints and how to read them: pickup `docs_input/UNINET_SNIPPETS.md:114-140`, `docs_input/UNINET_PHILOSOPHICAL_RESULTS_SECTION.md:81-99`; transfer a very short note on how exploratory numerical hints can motivate future work without changing theorem status; mention only the first `InferenceLight` run, label it as speculative only, point readers to Appendix D, and if summarized in prose phrase it as “still compatible with a Regge-like curved-spacetime regime, but not locked to GR/EFE.”

### Chapter 13 Execution Queue
- [x] `P13-I` Chapter 13 introduction paragraph: pickup `docs_input/UNINET_PROOF_STATUS_LEDGER.md:23-62`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:28-65`, `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:6-40`; transfer a strict close-out and handoff discipline; no relabeling.
- [x] `P13.1` Summary of proved spine: pickup `docs_input/UNINET_PROOF_STATUS_LEDGER.md:23-42`, `docs_input/UNINET_CORE_AXIOMS.md:353-1459`; transfer only theorem-backed outcomes and summarize them using the paper relabels already assigned; no new relabeling.
- [x] `P13.2` Summary of open/deferred items: pickup `docs_input/UNINET_PROOF_STATUS_LEDGER.md:48-62`, `docs_input/UNINET_QM_SECTION.md:104-117`, `docs_input/UNINET_GR_SECTION.md:155-188`, `docs_input/UNINET_SM_SECTION.md:129-143`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md:121-137`; transfer unresolved claims, blockers, and deferred packages; no relabeling.
- [x] `P13.3` Exact handoff list to Paper 2: pickup `docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md:6-40`, `docs_input/UNINET_NOETHER_SYMMETRY_PROGRAM.md:48-56`, `docs_input/QUEUEING_RIGOR_PLAN.md:99-129`, `docs_input/UNINET_QM_SECTION_RIGOR_PLAN.md:150-161`, `docs_input/UNINET_GR_SECTION_RIGOR_PLAN.md:209-225`, `docs_input/UNINET_SM_SECTION_RIGOR_PLAN.md:142-153`, `docs_input/UNINET_COSMOLOGY_LCDM_SECTION_RIGOR_PLAN.md:159-172`; transfer the exact Paper 2 backlog and execution order; no relabeling.

### Appendix and Box Execution Queue
- [x] `APP-A` Appendix A notation and units: pickup `docs_input/UNINET_NOTATION_UNITS_STANDARD.md:7-99`, `docs_input/UNINET_CORE_AXIOMS.md:166-205`; transfer the full reader lookup appendix; no relabeling.
- [x] `APP-B` Appendix B governance and falsifiability appendices: pickup `docs_input/UNINET_QM_FALSIFIABILITY_MATRIX.md:1-27`, `docs_input/UNINET_GR_FALSIFIABILITY_MATRIX.md:1-36`, `docs_input/UNINET_SM_FALSIFIABILITY_MATRIX.md:1-28`, `docs_input/UNINET_COSMOLOGY_LCDM_FALSIFIABILITY_MATRIX.md:1-34`, `docs_input/UNINET_PARAMETER_LEDGER.md:8-92`, `docs_input/UNINET_PROOF_STATUS_LEDGER.md:6-62`, `docs_input/UNINET_FALSIFIABILITY_INDEX.md:28-65`; transfer the full falsifiability matrices or their full paper appendix equivalents, plus audit metadata, parameter-lock, proof-status, and test-priority tables; reference `GOV-03..06`.
- [x] `APP-C` Appendix C proof-note index: pickup `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:1-358`, `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:1-736`; transfer a proof-note index that points readers from main-text theorem IDs to the long-form notes; reference `THEOREM-QM-02`, `LEMMA-QM-01..07`, and `THEOREM-GR-05..07`.
- [x] `APP-D` Appendix D speculative numerical notes: pickup `docs_input/UNINET_SNIPPETS.md:114-140`; transfer the first `InferenceLight` run metadata, dataset manifest, parameter-range snapshot, and compatibility-first verdict only as a non-canonical exploratory note; add an explicit warning that it is not proof evidence, not a locked fit result, and not part of the compact main-paper falsifiability rows; if interpretation is included, state it as an inference that the explored parameter region remains compatible with a Regge-like curved-spacetime packaging, while not locking the theory to GR/EFE closure.

## 4) Theorem Placement Map (Working)

### Shared theorem chapter (Chapter 3)
- Reachability / latency basis (Lemma/Definition package)
- Cut-balance theorem + boundary bookkeeping corollary
- Cut primitive + leaky-boundary criterion
- Causal-order and observer-time constructions
- Arrow theorem from coarse-graining

### Boundary/horizon chapter (Chapter 4)
- Boundary observability principle (operational)
- Boundary redundancy/gauge equivalence results
- Horizon-like cut interpretation results
- Boundary mediator structure claims (with maturity tags)

### Symmetry/formalism chapter (Chapter 6)
- Symmetry registry and status taxonomy
- Native versus variational companion rules
- Noether-promotion protocol and boundary conditions

### GR chapter (Chapter 7)
- Queue drift + trapping + boundary-dominant release package
- Adaptive GR latency theorem
- Projection/bridge coupling theorem(s)
- Regge bridge proof set (including edge-length bound defense)

### QM chapter (Chapter 8)
- QM static latency theorem
- Standing-wave existence theorem and proof refinement
- Degenerate vs nontrivial standing-mode families

### SM chapter (Chapter 9)
- Chiral/CP/spin-statistics/admissible-window constraints
- Particle as boundary-stabilized standing-wave interpretation

### Cosmology chapter (Chapter 10)
- DE/DM/Inflation packaging statements
- Early-BH + last-parsec phenomenology (status-tagged)
- Computability implications from boundary cutting

### Governance chapter (Chapter 11)
- Artifact hierarchy, proof ledger, and source-of-truth rules
- Parameter-lock and falsifiability governance tables
- Paper-facing falsifiability statement policy and exploratory-results separation
- Audit path from theorem to observable

## 4A) Anti-Duplication and Reference Policy
1. One canonical statement location per formal item:
   - Shared items live in Chapter 3 unless they are truly sector-local.
   - Boundary-specific items live in Chapter 4.
   - Sector-local proofs live once in their own sector chapter or appendix.
2. Sector chapters should not copy shared proofs in full.
   - They may include a one-paragraph reminder.
   - They must then reference the canonical theorem ID and source location.
3. If a proof is too long for the narrative flow:
   - keep the full proof once in an appendix or proof note,
   - keep only the statement and proof idea in the main text,
   - reference the full location explicitly.
4. Definitions should be introduced once whenever possible.
   - Later uses should reference the canonical definition rather than re-define it.
5. Observational and phenomenological material should also avoid duplication.
   - One main discussion location,
   - brief cross-references elsewhere.
6. Falsifiability content also follows one canonical-home rule:
   - compact falsifiability statements appear once in the relevant sector chapter,
   - the fuller governance/audit version lives in Chapter 11 and Appendix B,
   - matrices remain source-of-truth artifacts but are not the only paper location.

## 4AA) Document Dependency DAG Policy
1. Chapter dependency should run mainly forward:
   - Chapter 1 -> Chapter 2 -> Chapter 3 -> Chapter 4 -> Chapter 5 -> Chapter 6 -> sector chapters -> governance -> philosophy -> conclusion.
2. Sector chapters should depend on shared chapters, not on each other, unless a cross-sector dependency is truly unavoidable and stated explicitly.
3. Definitions should appear before theorems that use them.
4. Shared theorems should appear before sector packaging that relies on them.
5. Appendices and proof notes may support main-text claims, but main-text logic should not require readers to chase circular references between appendices and chapters.
6. If two chapters appear to depend on each other, that is a refactoring signal:
   - move the shared material upward,
   - or split the claim into a shared theorem plus sector-specific corollaries.
7. Cross-references should distinguish:
   - `dependency reference`: needed for logic,
   - `context reference`: useful for intuition only.
8. The paper outline and the theorem relabel map should therefore be readable as a manuscript-level DAG.

## 4B) Literature-Reference Policy
1. Each chapter introduction should mention the nearest existing literature domain so readers can orient themselves.
2. Each major formal bridge should state whether UniNet is:
   - reproducing a known mathematical structure,
   - giving a new interpretation of a known structure,
   - or claiming a genuinely new theorem.
3. Priority literature touchpoints:
   - Chapter 3: causal order, cone structures, coarse-graining, boundary observability.
   - Chapter 4: horizons, boundary symmetries, holographic/boundary-style intuition where relevant.
   - Chapter 5: discrete unitary transport, lattice Schrödinger-style evolution, reversible local update systems.
   - Chapter 6: symmetry registries, Noether-style structure, discrete variational formalisms, boundary terms.
   - Chapter 7: Regge calculus, causal structure, effective geometry, black-hole surface phenomenology.
   - Chapter 8: standing waves on graphs, spectral graph intuition, discrete Schrödinger dynamics, quantum-walk literature.
   - Chapter 9: chirality, CP structure, spin-statistics, gauge redundancy and symmetry constraints.
   - Chapter 10: cosmological phenomenology, early-structure formation, CMB/parity literature, computability analogies where legitimate.
4. Literature is used to orient and compare, not to smuggle assumptions.
5. When no close literature exists, say that explicitly rather than implying a precedent.

## 4C) Informal Source and Boxed Material Policy
1. `UNINET_SNIPPETS.md` may be used as a source pool for philosophical framing and boxed intuition only.
2. `UNINET_SNIPPETS.md` is not a canonical source for theorem statements, formal definitions, or quantitative claims.
3. Any adopted idea from `UNINET_SNIPPETS.md` must be re-anchored to a canonical UniNet source or external literature before it enters the manuscript.
4. Quantitative snippet material stays out of the main paper unless it is promoted into a canonical governance or results artifact first.

## 5) Theorem Intake and Relabel Plan (docs_input-centered)

Working scope:
1. Primary pickup source is `docs_input/*`.
2. `docs/*` is read-only fallback only when there is no equivalent `docs_input` proof text yet.
3. Canonical output target is the chapter-file set under `papers/paper1/`; a stitched master manuscript is optional and is not required for Paper 1 execution.
4. `docs_input/*` remains source/governance/input material; manuscript drafting and chapter output should not be written back into `docs_input`.
5. Manuscript chapters under `papers/paper1/` are reader-facing outputs and must therefore omit internal source-pickup metadata; that metadata stays here in the plan.

Relabel convention in output doc:
1. Keep canonical IDs unchanged: `AXIOM-1..AXIOM-10`, `MODEL-P*`, `SM-FOUND-*`, `BRIDGE-P*`, `NS-*`.
2. Shared spine (Chapter 3): `DEFINITION-SH-*`, `LEMMA-SH-*`, `PROPOSITION-SH-*`, `THEOREM-SH-*`, `COROLLARY-SH-*`.
3. Boundary chapter (Chapter 4): `DEFINITION-BND-*`, `THEOREM-BND-*`, `COROLLARY-BND-*`.
4. Update-function chapter (Chapter 5): `REQUIRED-UPD-*` for admissibility/constraint rows.
5. Symmetry/formalism chapter (Chapter 6): keep `NS-*` for registry rows and use `FORM-*` for chapter-local formalism blocks.
6. GR chapter (Chapter 7): `DEFINITION-GR-*`, `LEMMA-GR-*`, `THEOREM-GR-*`, `COROLLARY-GR-*`, `PROPOSITION-GR-*`.
7. QM chapter (Chapter 8): `DEFINITION-QM-*`, `LEMMA-QM-*`, `THEOREM-QM-*`, `COROLLARY-QM-*`.
8. SM chapter (Chapter 9): `DEFINITION-SM-*`, `THEOREM-SM-*`, `COROLLARY-SM-*`, and `REQUIRED-SM-*` for requirement rows.
9. Cosmology chapter (Chapter 10): `DEFINITION-COS-*`, `THEOREM-COS-*`, `COROLLARY-COS-*`, `PROPOSITION-COS-*`, and `REQUIRED-COS-*` for requirement rows.
10. Governance chapter (Chapter 11): `GOV-*` for tables, audit rules, and lock/falsifiability blocks.
11. Every imported block must be tracked here with source alias and pickup location, but the manuscript chapter should show only the paper-facing label and self-contained statement.

Per-theorem workflow checklist (run for each row below):
- [ ] Copy statement and proof text from source into output draft with no semantic edits.
- [ ] Compare copied text to source lines and confirm no loss.
- [ ] Apply new output relabel and add dependency tags in the manuscript; keep source alias and pickup location in the plan/editorial audit only.
- [ ] Rewrite inherited in-text references so transferred prose points to the paper's new labels rather than the source document's old local labels.
- [ ] Mark the one canonical location where the item will live in the paper.
- [ ] Replace any later duplicate restatement with a short summary plus reference.
- [ ] Add literature placeholders where the result interfaces with known mathematics or physics.

### 5.1 Shared spine intake queue (Chapter 3)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Lemma 1.1 Reachability via Graph Distance | `docs_input/UNINET_CORE_AXIOMS.md:361` | `LEMMA-SH-01` |
| [ ] | Definition 1.1 Effective Latency | `docs_input/UNINET_CORE_AXIOMS.md:374` | `DEFINITION-SH-01` |
| [ ] | Lemma 1.2 Metric Properties of Latency | `docs_input/UNINET_CORE_AXIOMS.md:388` | `LEMMA-SH-02` |
| [ ] | Definition 1.2 Local Conservation / Continuity | `docs_input/UNINET_CORE_AXIOMS.md:400` | `DEFINITION-SH-02` |
| [ ] | Theorem 1.1 Discrete Gauss/Stokes: Bulk = Boundary | `docs_input/UNINET_CORE_AXIOMS.md:422` | `THEOREM-SH-01` |
| [ ] | Corollary 1.1 Exact Closure with Boundary Bookkeeping | `docs_input/UNINET_CORE_AXIOMS.md:453` | `COROLLARY-SH-01` |
| [ ] | Theorem 1.2 Leaky-Boundary Criterion | `docs_input/UNINET_CORE_AXIOMS.md:481` | `THEOREM-SH-02` |
| [ ] | Definition 2.1 Precedence Relation | `docs_input/UNINET_CORE_AXIOMS.md:579` | `DEFINITION-SH-03` |
| [ ] | Lemma 2.1 Partial Order | `docs_input/UNINET_CORE_AXIOMS.md:591` | `LEMMA-SH-03` |
| [ ] | Definition 2.2 Causal Futures/Pasts and Horismos | `docs_input/UNINET_CORE_AXIOMS.md:603` | `DEFINITION-SH-04` |
| [ ] | Lemma 2.2 Horismos Characterization | `docs_input/UNINET_CORE_AXIOMS.md:622` | `LEMMA-SH-04` |
| [ ] | Proposition 2.1 Closed Cone Structure | `docs_input/UNINET_CORE_AXIOMS.md:634` | `PROPOSITION-SH-01` |
| [ ] | Definition 3.1 Time Function | `docs_input/UNINET_CORE_AXIOMS.md:648` | `DEFINITION-SH-05` |
| [ ] | Lemma 3.1 Existence of Time Functions | `docs_input/UNINET_CORE_AXIOMS.md:658` | `LEMMA-SH-05` |
| [ ] | Definition 3.2 Volume-Based Time | `docs_input/UNINET_CORE_AXIOMS.md:667` | `DEFINITION-SH-06` |
| [ ] | Definition 3.3 Time Separation | `docs_input/UNINET_CORE_AXIOMS.md:680` | `DEFINITION-SH-07` |
| [ ] | Definition 3.4 Coarse-Graining Observation Map | `docs_input/UNINET_CORE_AXIOMS.md:697` | `DEFINITION-SH-08` |
| [ ] | Theorem 3.2 Emergent Arrow from Non-Injective Observation | `docs_input/UNINET_CORE_AXIOMS.md:706` | `THEOREM-SH-03` |
| [ ] | Corollary 3.1 QM Sector Consequence | `docs_input/UNINET_CORE_AXIOMS.md:730` | `COROLLARY-SH-02` |
| [ ] | Corollary 3.2 GR Sector Consequence | `docs_input/UNINET_CORE_AXIOMS.md:739` | `COROLLARY-SH-03` |
| [ ] | Corollary 3.3 SM Sector Consequence | `docs_input/UNINET_CORE_AXIOMS.md:744` | `COROLLARY-SH-04` |

### 5.2 Boundary and horizon intake queue (Chapter 4)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Definition 1A.1 Boundary Bandwidth Function | `docs_input/UNINET_CORE_AXIOMS.md:1330` | `DEFINITION-BND-01` |
| [ ] | Definition 1A.2 Effective Dimension from Bandwidth Growth | `docs_input/UNINET_CORE_AXIOMS.md:1338` | `DEFINITION-BND-02` |
| [ ] | Theorem 1A.1 Boundary Growth Controls Volume Growth | `docs_input/UNINET_CORE_AXIOMS.md:1346` | `THEOREM-BND-01` |
| [ ] | Definition 1A.3 Boundary Observable Algebra | `docs_input/UNINET_CORE_AXIOMS.md:1352` | `DEFINITION-BND-03` |
| [ ] | Definition 1A.4 Boundary Redundancy Group | `docs_input/UNINET_CORE_AXIOMS.md:1356` | `DEFINITION-BND-04` |
| [ ] | Theorem 1A.2 Boundary Capacity Bounds Independent Conserved Flows | `docs_input/UNINET_CORE_AXIOMS.md:1364` | `THEOREM-BND-02` |
| [ ] | Theorem 1A.3 Goldilocks Window for Boundary Symmetry Viability | `docs_input/UNINET_CORE_AXIOMS.md:1370` | `THEOREM-BND-03` |
| [ ] | Corollary 1A.1 Constraint on SM Gauge Structure | `docs_input/UNINET_CORE_AXIOMS.md:1379` | `COROLLARY-BND-01` |
| [ ] | Definition 1B.1 Cut-External Observational Equivalence | `docs_input/UNINET_CORE_AXIOMS.md:1390` | `DEFINITION-BND-05` |
| [ ] | Theorem 1B.1 Gauge Equivalence as Cut-Observable Equivalence | `docs_input/UNINET_CORE_AXIOMS.md:1397` | `THEOREM-BND-04` |
| [ ] | Theorem 1B.2 Universal Boundary Mediator Structure | `docs_input/UNINET_CORE_AXIOMS.md:1403` | `THEOREM-BND-05` |
| [ ] | Theorem 1B.3 Boundary Rank Bound on Independent Conserved Charges | `docs_input/UNINET_CORE_AXIOMS.md:1409` | `THEOREM-BND-06` |
| [ ] | Theorem 1B.4 Low-Dimensional Abelianization | `docs_input/UNINET_CORE_AXIOMS.md:1415` | `THEOREM-BND-07` |
| [ ] | Theorem 1B.5 High-Dimensional Symmetry Proliferation Instability | `docs_input/UNINET_CORE_AXIOMS.md:1421` | `THEOREM-BND-08` |
| [ ] | Theorem 1B.6 Dimensional Attractor Hypothesis | `docs_input/UNINET_CORE_AXIOMS.md:1427` | `THEOREM-BND-09` |
| [ ] | Theorem 1B.7 Field Limit as Boundary Ensemble Average | `docs_input/UNINET_CORE_AXIOMS.md:1433` | `THEOREM-BND-10` |

### 5.3 Update-function requirement intake queue (Chapter 5)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | `R1` Locality-preserving update support | `docs_input/UNINET_CORE_AXIOMS.md:755` | `REQUIRED-UPD-01` |
| [ ] | `R2` No-information-loss / norm-preserving evolution | `docs_input/UNINET_CORE_AXIOMS.md:764` | `REQUIRED-UPD-02` |
| [ ] | `R3` No phenomenological delays in the update law | `docs_input/UNINET_CORE_AXIOMS.md:771` | `REQUIRED-UPD-03` |
| [ ] | `R4` Transport-function admissibility and closure conditions | `docs_input/UNINET_UPDATE_OPERATOR_CONSTRAINTS.md:27` | `REQUIRED-UPD-04` |

### 5.4 Symmetry and formalism intake queue (Chapter 6)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Symmetry registry `NS-001..NS-007` | `docs_input/UNINET_NOETHER_SYMMETRY_SECTION.md` | Keep `NS-*` |
| [ ] | Noether/symmetry promotion protocol | `docs_input/UNINET_NOETHER_SYMMETRY_PROGRAM.md` | `FORM-01` |
| [ ] | Native vs variational companion rule | `docs_input/UNINET_DUAL_TRACK_FORMALISM_STANDARD.md` | `FORM-02` |

### 5.5 GR intake queue (Chapter 7)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Theorem 1.3 Queue Drift Identity and Low-Load Stability | `docs_input/UNINET_CORE_AXIOMS.md:526` | `THEOREM-GR-01` |
| [ ] | Theorem 1.4 Near-Saturation Trapping Bound | `docs_input/UNINET_CORE_AXIOMS.md:548` | `THEOREM-GR-02` |
| [ ] | Corollary 1.2 Boundary-Dominant Release | `docs_input/UNINET_CORE_AXIOMS.md:567` | `COROLLARY-GR-01` |
| [ ] | Theorem 4.1 Buffering Couples to Geometry | `docs_input/UNINET_CORE_AXIOMS.md:1151` | `THEOREM-GR-03` |
| [ ] | Theorem: GR Latency (Adaptive) | `docs_input/UNINET_CORE_AXIOMS.md:1206` | `THEOREM-GR-04` |
| [ ] | Theorem 8.1 Delay-to-Length Equivalence and Effective Geometry | `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:328` | `THEOREM-GR-05` |
| [ ] | Theorem 8.4B Canonical Small-Coupling Regge Regime | `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:567` | `THEOREM-GR-06` |
| [ ] | Theorem 8.5 Seed-to-Open-Overlap Principle | `docs/20_proofs/gr/01_buffering_delay_to_effective_edge_length_equivalence.md:680` | `THEOREM-GR-07` |

### 5.6 QM intake queue (Chapter 8)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Theorem: QM Latency | `docs_input/UNINET_CORE_AXIOMS.md:1188` | `THEOREM-QM-01` |
| [ ] | AXIOM-10 Particle Modes as Boundary-Stabilized Standing Waves | `docs_input/UNINET_CORE_AXIOMS.md:1441` | Keep `AXIOM-10` |
| [ ] | Theorem E1 Existence in Restricted Class | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:88` | `THEOREM-QM-02` |
| [ ] | Lemma L1 No Information Loss | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:123` | `LEMMA-QM-01` |
| [ ] | Lemma L2 Propagation Delay Structure | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:146` | `LEMMA-QM-02` |
| [ ] | Lemma L3 Cycle Prerequisite | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:165` | `LEMMA-QM-03` |
| [ ] | Lemma L3A Two-Node Degenerate Witness | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:197` | `LEMMA-QM-04` |
| [ ] | Lemma L4 Base Witness on One Cycle | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:252` | `LEMMA-QM-05` |
| [ ] | Lemma L5 Embedding in source `R5-R8` / paper `REQUIRED-SM-01..04` window | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:273` | `LEMMA-QM-06` |
| [ ] | Lemma L6 Induction on Cycle Rank | `docs/20_proofs/qm_sm/01_standing_wave_existence_restricted_update_class.md:310` | `LEMMA-QM-07` |

### 5.7 SM intake queue (Chapter 9)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | `R5` Chiral Structure Preservation | `docs_input/UNINET_CORE_AXIOMS.md:792` | `REQUIRED-SM-01` |
| [ ] | `R6` CP Symmetry or Violation | `docs_input/UNINET_CORE_AXIOMS.md:833` | `REQUIRED-SM-02` |
| [ ] | `R7` Spin-Statistics Connection | `docs_input/UNINET_CORE_AXIOMS.md:861` | `REQUIRED-SM-03` |
| [ ] | `R8` Quantitative Admissible Window | `docs_input/UNINET_CORE_AXIOMS.md:878` | `REQUIRED-SM-04` |
| [ ] | AXIOM-10 Standing-Wave Particle Principle | `docs_input/UNINET_CORE_AXIOMS.md:1441` | Keep `AXIOM-10` |
| [ ] | CP/CMB chirality overlap box | `docs_input/UNINET_CP_CMB_CHIRALITY_OVERLAP_NOTE.md` | `BOX-SM-01` |

### 5.8 Cosmology intake queue (Chapter 10)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Core packaging statement: DE branch | `docs_input/UNINET_CORE_AXIOMS.md:1223` | `PROPOSITION-COS-01` |
| [ ] | Core packaging statement: DM branch | `docs_input/UNINET_CORE_AXIOMS.md:1235` | `PROPOSITION-COS-02` |
| [ ] | Core packaging statement: inflation branch | `docs_input/UNINET_CORE_AXIOMS.md:1244` | `PROPOSITION-COS-03` |
| [ ] | `R9` Queue-response correction requirement for macro packaging | `docs_input/UNINET_CORE_AXIOMS.md:901` | `REQUIRED-COS-01` |
| [ ] | `R10` Saturation correction requirement for macro packaging | `docs_input/UNINET_CORE_AXIOMS.md:917` | `REQUIRED-COS-02` |
| [ ] | Cosmology package claims (status-tagged, no theorem promotion yet) | `docs_input/UNINET_COSMOLOGY_LCDM_SECTION.md` | `COS-PKG-01` |

### 5.9 Governance and audit intake queue (Chapter 11)
| Status | Source ID | Source location | Output relabel |
|---|---|---|---|
| [ ] | Artifact hierarchy and source-of-truth rule | `docs_input/UNINET_ARTIFACT_CLASSIFICATION.md` | `GOV-01` |
| [ ] | Axiom-to-prediction DAG | `docs_input/UNINET_AXIOM_TO_PREDICTION_DAG_v2.md` | `GOV-02` |
| [ ] | Proof-status ledger integration | `docs_input/UNINET_PROOF_STATUS_LEDGER.md` | `GOV-03` |
| [ ] | Parameter ledger and reduced fit basis | `docs_input/UNINET_PARAMETER_LEDGER.md` | `GOV-04` |
| [ ] | Falsifiability standard | `docs_input/UNINET_FALSIFIABILITY_STANDARD.md` | `GOV-05` |
| [ ] | Falsifiability priority index | `docs_input/UNINET_FALSIFIABILITY_INDEX.md` | `GOV-06` |
| [ ] | Boundaries and non-claims discipline | `docs_input/UNINET_BOUNDARY_NONCLAIMS.md` | `GOV-07` |

### 5.10 Cross-reference relabel pass (paper output)
| Status | Task | Source | Output |
|---|---|---|---|
| [x] | Keep relabel map editorial-only in the build plan; do not include it in the reader-facing manuscript | All rows in 5.1-5.9 | Build plan only |
| [ ] | Replace in-chapter references to new IDs | `papers/paper1/*.md` | All chapters |
| [ ] | Replace inherited source-document label mentions inside transferred prose | All chapter drafts built from `docs_input` / proof notes | All chapters |
| [ ] | Keep source alias and pickup-line auditability in the build plan/editorial notes, not in manuscript chapters | All imported blocks | Plan + editorial tracking |
| [ ] | Verify each theorem has dependency tag list | Shared + sector chapters | Theorem headers |

## 6) Observation-Link Policy
Per chapter, add a compact table with columns:
`claim_id | status | observable | current evidence anchor | future decisive test | rejection condition`.

Use existing falsifiability matrices as source-of-truth; do not invent new numeric thresholds in the prose chapter.
Each sector chapter must include compact paper-facing falsifiability statements distilled from the canonical matrices:
`prediction_id | null_model | signed prediction | locked-parameter policy | decision_rule | falsifier_statement`.
The full matrices and audit metadata live in Appendix B and the source governance files.
Exploratory numerical results, including the first `InferenceLight` run, are excluded from these rows unless formally promoted through the governance path.

## 7) Immediate Execution Plan (Paper Build)

### Phase A - Structure Lock
1. Freeze this chapter order and claim-tag policy.
2. Freeze theorem placement map (shared vs sector chapters).
3. Freeze appendix and box policy.

### Phase B - Core + Shared Chapters First
1. Write Chapter 1 (human intro) and Chapter 2 (axioms/modeling split).
2. Write Chapter 3 (shared theorem spine) end-to-end before sector text.
3. Write Chapter 4 (boundary/horizon intuition chapter).

### Phase C - Update + Formalism Layer
1. Write Chapter 5 (update function constraints, witness family, and admissible class).
2. Write Chapter 6 (symmetry registry, dual-track formalism, and Noether-promotion discipline).

### Phase D - Sector Chapters
1. Write Chapter 7 (GR) including Regge edge-length defense.
2. Write Chapter 8 (QM) with standing-wave proof cleanup and simulator box.
3. Write Chapter 9 (SM) including the CP/CMB chirality box.
4. Write Chapter 10 (Cosmology + computability note).

### Phase E - Governance + Philosophy + Close
1. Write Chapter 11 (governance, lock protocol, and falsifiability traceability).
2. Write Chapter 12 (philosophical interpretation with explicit limits and snippet-derived framing re-anchored to canonical sources).
3. Write Chapter 13 (conclusion + Paper-2 handoff backlog).

## 8) Done Criteria for Paper 1
1. A non-specialist can follow Chapters 1-5 without reading appendices.
2. Every sector claim is traceable to shared theorem spine + tagged assumptions.
3. Every chapter has a proved/assumed/open summary block.
4. Every major claim has an observation/falsifiability pointer.
5. Governance artifacts and manuscript claims are mutually consistent.
6. No formal item is stated in full in more than one canonical place.
7. Manuscript chapter dependencies are readable as a mostly forward DAG.
8. Each sector chapter contains compact in-paper falsifiability statements, with the full matrices and audit metadata preserved in Appendix B / source governance files.
9. The first `InferenceLight` run is mentioned only as a speculative exploratory note and cannot be mistaken for proof evidence or a locked-fit result; any interpretive gloss is limited to Regge-compatible curved-spacetime viability and must explicitly deny GR/EFE lock-in.

---
End of plan.




