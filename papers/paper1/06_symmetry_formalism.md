# Chapter 6 - Geometry from Graph

The manuscript needs one shared symmetry chapter before the sector chapters for a simple reason: symmetry language is reused across QM, GR, SM, and cosmology, but the proof maturity is not the same in all four places. If that distinction is not fixed once, early, the sector chapters will either duplicate each other or overclaim. This chapter therefore does two jobs. It records the current symmetry registry with explicit proof status, and it fixes the rule for how formulas are presented when native UniNet notation and variational language coexist.

The previous chapters established structure, constraints, and admissible dynamics without ever appealing to space or geometry. This chapter shows that geometry nevertheless appears.
Chapter 06 does not introduce a manifold, coordinates, or a metric. Instead, it asks a more restrained question: once causality, delay, and boundary‑aware evolution are fixed, what kind of geometric structure is already implied? The answer is that much of what later looks like spacetime geometry is already encoded in the causal and temporal relations of the graph itself.
The focus of this chapter is Regge‑like structure: how discrete connectivity, finite propagation, and update order conspire to produce effective notions of distance, curvature, and geometry. These notions are not assumed. They are inferred from how influence spreads, how delays accumulate, and how paths compose. Geometry here is not something the system lives in — it is something the system exhibits.
This chapter is careful about scope. No continuum limit is taken. No smoothness is assumed. Where analogies to general relativity are drawn, they are marked as interpretations rather than identifications. The goal is not to reproduce spacetime, but to show that a geometric reading is unavoidable once causal structure becomes rich enough.
By the end of Chapter 06, the reader should see how geometry can emerge from bookkeeping alone. Distances arise from latency. Paths acquire length. Curvature appears as deviation from uniform propagation. None of this requires a background space. Geometry is revealed as a secondary description of the same underlying relational structure that has been present all along.


## 6.1 Symmetry Registry and Maturity Taxonomy
The current registry separates theorem-level symmetry claims from noether-like and deferred claims. Paper 1 keeps that separation rather than smoothing it over.

| Registry ID | Claim | Paper status | Paper-facing reading |
|---|---|---|---|
| `NS-001` | graph relabeling covariance | `proved` | physics does not depend on node labels |
| `NS-002` | QM time-translation invariance in the static regime | `proved` | fixed-$U$ QM branches conserve spectral data |
| `NS-003` | locality-preserving conjugation symmetry | `proved` | graph-local basis changes do not alter causal structure |
| `NS-004` | pseudo-unitary projected invariance | `noether-like` | intended Lorentz-style envelope symmetry on projected branches |
| `NS-005` | norm conservation | `proved` | unitarity gives exact information conservation |
| `NS-006` | entropy or closure-style invariants | `noether-like` | continuity and cut bookkeeping suggest conserved structure, but the full observable class is not frozen |
| `NS-007` | source-curvature conservation compatibility | `deferred-noether` | a Bianchi-like closure target for the GR bridge, pending action-level completion |

Three points matter for the reader.

1. `NS-*` rows are not new axioms. They are status-tagged consequences or program items built from earlier chapters.
2. `proved` here means theorem-level in the current corpus, not merely plausible.
3. `noether-like` means there is a recognizable invariant structure, but the full action-symmetry-current pipeline has not yet been completed.

## 6.2 Native and Variational Companion Forms
The paper keeps native UniNet notation as the primary presentation layer.

### `FORM-02` - Native-First, Variational-Companion Rule
Status: `governance`

Every major claim should first appear in the notation that is already doing the explanatory work in the paper. A variational or Lagrangian companion is then added when, and only when, it materially improves rigor or transparency.

Mandatory companion cases:
1. source-curvature coupling claims,
2. action- or stationarity-based dynamics claims,
3. claims explicitly framed as Noether results.

Optional companion cases:
1. pure kinematic definitions,
2. cut or boundary bookkeeping statements,
3. early theorem scaffolds whose action domain is not yet frozen.

The native expressions remain the most readable handles:

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I,
$$

$$
\mathrm{Curv}[\tau]=\kappa\,\mathrm{StressEffort}[\rho,J].
$$

The companion variational form enters when the argument actually needs it:

$$
\frac{\delta\!\left(\mathcal{S}_{\mathrm{geo}}[\tau]+\kappa\,\mathcal{S}_{\mathrm{src}}[\rho,J]\right)}{\delta\tau}=0.
$$

So the paper's formula policy is not "native or variational." It is "native first, variational where the claim class requires it."

## 6.3 Noether Promotion Protocol
### `FORM-01` - Noether Promotion Protocol
Status: `governance`

No symmetry claim may be promoted from `noether-like` or `deferred-noether` to full Noether-theorem status unless all of the following are frozen.

1. The action functional and admissible state or field domain.
2. The symmetry group action on that domain.
3. The variation and differentiability assumptions.
4. The boundary-term handling.
5. The derived current or charge law together with exact scope.

This protocol is intentionally strict. It is the paper's defense against the common failure mode where invariant-looking statements are presented as if a full conserved-current theorem already exists.

## 6.4 Cross-Sector Symmetry Placement and Non-Claims
The benefit of the shared registry is that each sector chapter can now point to exactly the symmetry layer it is using.

QM usage:
1. `NS-001`, `NS-002`, `NS-003`, and `NS-005` are active and sufficient for the fixed-latency unitary regime,
2. `NS-004` is not needed to claim ordinary graph-local standing or transport structure.

GR usage:
1. the GR chapter uses the native projected-geometry language first,
2. `NS-004` and `NS-007` remain the relevant deferred or noether-like symmetry targets,
3. GR therefore inherits a symmetry envelope program, not a completed Noether closure.

SM usage:
1. chirality, CP sensitivity, and gauge-as-redundancy language sit at the boundary between theorem-level and noether-like structure,
2. the paper uses the symmetry registry to keep gauge redundancy distinct from full gauge-group emergence.

Cosmology usage:
1. effective-fluid and parity-sensitive packaging may refer back to the shared symmetry layer,
2. no cosmology chapter statement is allowed to upgrade symmetry maturity by rhetoric alone.

This chapter is therefore a control layer. It tells the reader how to interpret later symmetry references, and it prevents sector prose from silently doing work that only a full variational proof could justify.

## Chapter 6 Summary
Established in this chapter:
1. symmetry claims are organized by a shared registry rather than repeated ad hoc per sector,
2. the manuscript uses native formulas first and adds variational companions only where the claim class requires them,
3. Noether promotion has an explicit hard protocol.

Not claimed here:
1. full Noether closure for all sectors,
2. automatic promotion of invariant-looking statements to theorem status,
3. replacement of readable native formulas by action-only presentation.
