# Chapter 5 - Update Function

This chapter constrains the update operator before any sector-specific interpretation is allowed. The point is not to guess a preferred form of $U$ and then retrofit the rest of the theory around it. The point is to show that once the core and boundary theorems are fixed, only a narrow operator class survives, and at least one explicit witness family exists inside that class.

Constraining change without choosing it
Up to this point, UniNet has been careful not to guess how the system evolves. The framework committed to locality, reversibility, and boundary‑aware bookkeeping, but it deliberately avoided writing down a specific update rule. Chapter 5 addresses that restraint directly.
This chapter is not about proposing a particular dynamics. It is about narrowing the space of possibilities. Once the axioms and shared theorem spine are in place, not every update rule remains admissible. Some violate locality. Others break reversibility. Others quietly smuggle in preferred directions, hidden clocks, or boundary‑blind behavior. Chapter 5 makes those exclusions explicit.
The goal here is discipline, not completeness. Rather than deriving a unique update operator, the chapter identifies constraints that any acceptable update family must satisfy. These constraints come entirely from structure already established: finite propagation, exact bookkeeping, and compatibility with cuts and boundaries. Nothing new is assumed. The update rule is placed under obligation rather than privilege.
A key theme of this chapter is separation. The framework distinguishes between what must be true of any update and what is chosen for a particular modeling regime. Schrödinger‑like updates, queue‑based dynamics, and other witnesses appear later as examples, not as defaults. Chapter 5 ensures that when such choices are made, they are made honestly and visibly.
By the end of this chapter, the reader should not know exactly how UniNet evolves — and that is intentional. What they should know is what evolution is not allowed to do. Change is constrained before it is specified. The framework does not yet pick a dynamics, but it makes clear that dynamics must earn their place.

## 5.1 Why One Update Family and Homogeneity Matter
The core update commitments are:
1. `AXIOM-4`: one declared update-rule family,
2. `AXIOM-5`: update homogeneity across the graph.

These two constraints do more than simplify notation. They block three forms of hidden model drift:
1. undeclared patchwork laws assigned to different nodes,
2. ad hoc per-edge clocks or per-region rule changes,
3. post hoc tuning in which later sector behavior is smuggled into the microscopic law through hidden heterogeneity.

The paper therefore treats one update family and homogeneity as law-discipline constraints. They are what make later operator pruning meaningful rather than cosmetic.

One update family
The first constraint on admissible dynamics is that there is a single update rule family governing the entire graph.
This is not a choice made for elegance or simplicity. It is a consequence of everything fixed earlier. Once locality, reversibility, and boundary‑aware bookkeeping are in place, allowing multiple update rules would quietly reintroduce exactly the kinds of shortcuts the framework set out to avoid. Different laws in different regions would act like undeclared boundaries, privileged locations, or hidden degrees of freedom. They would allow structure to be explained by exception rather than by interaction.
A single update family does not imply uniform behavior. It implies uniform treatment. The same rule must act everywhere, but it may act on very different inputs. All diversity is pushed into state, connectivity, and history — never into the law itself. Apparent changes of behavior must therefore be explainable as changes in configuration, not as changes in the rule being applied.
At this stage, the update rule is no longer a free ingredient. It is under obligation. It must respect locality, preserve information, and interact honestly with cuts and boundaries. Any proposed dynamics that fails to meet these requirements is not merely inconvenient; it is incompatible with the structure already established.
Section 5.1 therefore does not propose a specific evolution. It removes an entire class of inadmissible ones. By insisting on a single update family, the framework ensures that whatever structure emerges later does so without hidden law‑switching, undeclared privilege, or boundary‑blind behavior. Change is allowed — but only if it plays by the same rules everywhere.


## 5.2 Locality and No-Information-Loss Constraints on Admissible $U$
The paper-facing update requirements are:

| Paper ID | Content |
|---|---|
| `REQUIRED-UPD-01` | locality-preserving support: one hop per tick |
| `REQUIRED-UPD-02` | unitary, norm-preserving, information-preserving evolution |
| `REQUIRED-UPD-03` | buffering-consistent continuity and flux representation |
| `REQUIRED-UPD-04` | no phenomenological edge delays and admissibility closure discipline |

Together with the core axioms, these imply the following operator filters.

1. Locality:

$$
(U\psi)_v
\text{ depends only on }
(\psi_u)_{u\in N[v]}.
$$

2. Information preservation:

$$
U^\dagger U=I.
$$

3. Continuity compatibility: the induced occupancies

$$
\rho(v,n)=\|\psi_v(n)\|^2
$$

must admit a divergence-form boundary bookkeeping representation.

4. No hidden edge-delay dressing: the operator may not introduce extra microscopic delay parameters on top of locality-derived latency.

This is already a strong filter. It excludes stochastic Tier-0 laws, collapse-style microscopic updates, arbitrary long-range couplings, and delay mechanisms that duplicate the work already done by graph distance.

The second constraint sharpens the first: the single update rule family must be applied homogeneously across the graph.
This requirement is not about suppressing complexity. It is about preventing privilege. Once locality and boundary‑aware bookkeeping are taken seriously, allowing the update to behave differently at different nodes would amount to embedding structure directly into the law. Certain locations would become special, not because of their state or history, but because the rule itself treated them differently. That move would quietly reintroduce background structure the framework has worked hard to avoid.
Homogeneity means that the update rule responds only to its declared inputs, not to where it is applied. The same local configuration must be handled in the same way everywhere. If two regions behave differently, that difference must be traceable to differences in state, connectivity, or accumulated history — never to an undeclared variation in the law itself.
What matters here is the distinction between uniform rules and uniform outcomes. UniNet commits to the former, not the latter. Rich behavior, asymmetry, and hierarchy are all still possible. They simply have to arise honestly, through interaction and constraint, rather than being baked into the update mechanism.
By enforcing homogeneous application, Chapter 5 closes another escape hatch. Any admissible update family must now be able to generate all observed structure without relying on special cases, node‑specific behavior, or hidden switches. Homogeneity turns the update rule from a source of explanation into something that must itself be explained — a neutral process acting everywhere the same way.
Together, Sections 5.1 and 5.2 ensure that dynamics remain lawful without being prescriptive. The framework does not yet choose how the system evolves, but it makes clear that evolution must be fair, local, and boundary‑respecting everywhere at once.

## 5.3 Schrodinger-Like Discrete Wave Transport as an Admissible Class
A one-dimensional, local, unitary update law on a graph naturally has the form of discrete wave transport.

In native form,

$$
\psi_{n+1}=U\psi_n,
\qquad
U^\dagger U=I.
$$

For a standing-mode witness one uses

$$
U\phi=\lambda\phi,
\qquad
|\lambda|=1,
\qquad
\psi_n=\lambda^n\phi.
$$

On a chosen quasienergy branch one may also write

$$
U=e^{-iH_{\mathrm{eff}}},
$$

with Hermitian $H_{\mathrm{eff}}$ on that branch.

With a single, homogeneously applied update family in place, the remaining freedom lies in the form of the update itself. Section 5.3 makes explicit that even this freedom is sharply constrained.
Locality and information preservation are not abstract principles that an update rule may approximately satisfy. They are operator‑level requirements. The update must be able to act using only local input, and it must rearrange information without loss. Any candidate update that requires global knowledge, hidden synchronization, or implicit averaging over distant regions is ruled out immediately. Likewise, any update that erases distinctions at the microscopic level, rather than merely hiding them behind boundaries or coarse‑graining, is incompatible with the framework.
This section exists to collapse the space of admissible dynamics. Many update rules that look reasonable at first glance fail under these constraints. Some violate locality in subtle ways, allowing influence to leak across cuts. Others preserve information only statistically, rather than exactly. Still others respect locality but fail to interact honestly with boundary bookkeeping, producing apparent conservation that cannot be closed.
What matters is that locality and reversibility work together here. Locality prevents shortcuts. Reversibility prevents fundamental loss. Together, they force the update to behave like a careful transporter of structure rather than a blender or a sink. Change is allowed, but it must be traceable, undoable in principle, and accountable at boundaries.
By enforcing these constraints at the operator level, Chapter 5 draws a firm line. The framework does not ask which dynamics are elegant or familiar. It asks which ones can coexist with the causal, boundary‑aware structure already established. The answer is: very few. What remains is a narrow class of updates capable of supporting propagation, standing patterns, gliders, and long‑lived structure without cheating.
Section 5.3 therefore marks the transition from openness to obligation. The update rule is no longer a creative choice. It is something that must fit through the same constraints as everything else in the framework. Only then can it be trusted to generate physics rather than obscure it.

This is the precise sense in which the admissible class is Schrodinger-like without introducing an independent continuum-time Hamiltonian postulate. The claim is not that this is the unique admissible microscopic law. The claim is that at least one physically familiar wave-like class survives all hard constraints and therefore serves as a constructive witness.


## 5.3.1 Buffered evolution as a modeling hinge
One remaining degree of freedom concerns what happens when propagation stalls.
Locality and finite update speed imply that information cannot always move immediately. When congestion, limited connectivity, or boundary constraints prevent onward propagation, information must be temporarily held. Chapter 5 deliberately does not fix how this buffering behaves. Two admissible possibilities remain: buffered information may remain inert until it can move again, or it may continue to evolve internally while it waits.
This distinction is not forced by the axioms. Both behaviors are compatible with locality, reversibility, and boundary‑aware bookkeeping. In either case, causal structure and propagation delays remain unchanged. What differs is internal phenomenology. Static buffering treats delay as pure latency. Buffered evolution allows internal rearrangement, mixing, or pattern formation to occur while information is trapped.
This section exists to mark that choice explicitly. It is not a theorem and not a requirement. It is a modeling hinge. Choosing one behavior or the other does not alter the framework’s structural claims, but it does influence how entropy‑like behavior, irreversibility strength, scrambling, and later symmetry breaking may emerge. The framework therefore flags this distinction without resolving it.
By isolating buffered behavior here, Chapter 5 preserves a clean separation between constraints and interpretations. The update rule remains a transporter, not a creator. Whether transport pauses are dynamically active or inert is left open on purpose, to be decided only when a specific modeling regime demands it. Later chapters may explore the consequences of either choice, but the framework itself does not commit.


## 5.4 Queue and Backpressure Constraints and Regime Handoff Conditions
Queueing is not introduced as a new microscopic axiom. It is a derived layer from locality, unitarity, and continuity.

The basic queue quantities are:

$$
q_v(n):=\rho(v,n),
\qquad
Q_n(R):=\sum_{v\in R}q_v(n),
$$

with boundary throughput decomposed as

$$
Q_{n+1}(R)=Q_n(R)+A_n(R)-S_n(R).
$$

The regime handoff is then governed by two paper-facing macro-packaging requirements:

### `REQUIRED-COS-01` - Monotone Slowdown Law
Status: `postulate`

The effective transport time must satisfy

$$
\partial_\rho \tau_{\mathrm{eff}}\ge 0,
\qquad
\partial_{\mathrm{Curv}}\tau_{\mathrm{eff}}\ge 0,
$$

with baseline lower bound

$$
\tau_{\mathrm{eff}}(u\to v)\ge d_G(u,v).
$$

### `REQUIRED-COS-02` - Controlled Saturation Throughput Law
Status: `postulate`

Near saturation, boundary throughput must obey

$$
|\Phi_n(\partial R)|\le F(1-\rho_{\mathrm{shell}}(n)),
\qquad
F(x)\to 0 \text{ as } x\to 0^+.
$$

These conditions define the handoff logic:
1. in the QM regime, latency remains topological and queue bookkeeping does not renormalize transport,
2. in the GR-facing regime, adaptive delay appears only after projection or coarse-graining and is constrained by monotone slowdown and controlled saturation behavior.

Witness families as declared choices
After the admissible space of update rules has been sharply constrained, a natural question remains: how does one actually work with the framework?
Section 5.4 introduces witness families as explicit, declared examples of admissible updates. These are not promoted to axioms, nor are they treated as uniquely correct. Their role is pragmatic. A witness family demonstrates that the constraints identified so far are not empty — that there exist concrete update rules capable of satisfying locality, reversibility, homogeneity, and boundary‑aware bookkeeping all at once.
This section exists to preserve a crucial separation. The framework does not derive a single inevitable dynamics. Nor does it allow arbitrary ones. Instead, it distinguishes between constraints, which are structural and non‑negotiable, and choices, which are modeling decisions made for specific purposes. Schrödinger‑like updates, queue‑based rules, or other constructions appear here only as witnesses: proofs of existence, not declarations of truth.
What matters is that witness families are labeled as such. They are not smuggled in as defaults. When a particular update form is used, the reader can see exactly which additional assumptions are being made and why. This keeps the theory auditable. If later results depend on properties specific to a chosen witness, that dependence is visible rather than hidden.
By introducing witness families at this stage, Chapter 5 completes its task without overreach. The framework has constrained what change is allowed, shown that those constraints are satisfiable, and resisted the temptation to collapse choice into necessity. Dynamics are now possible — but only within a space that has been earned.

## 5.5 Non-Empty Admissible Transport Family and Witness Construction
The admissible transport set must not merely be defined. It must be shown to be non-empty.

At the programmatic level one writes

$$
\mathcal{A}_U
:=
\left\{
U
\;\middle|\;
\text{all paper-facing locality, unitarity, continuity, and admissibility requirements hold}
\right\}.
$$

Before theorem promotion, the program requires at least one explicit witness family with non-empty parameter domain.

Two witness directions already exist within the paper program:

1. the standing-wave route:
   a local unitary class supports exact or quasi-standing modes on graphs with nontrivial cycle structure;

2. the Regge bridge route:
   explicit admissible parameter families produce a non-empty geometric seed and an open small-coupling regime around that seed.

The combined lesson is enough for Paper 1:
1. the admissible set is not empty in the current programmatic sense,
2. explicit witness families already exist on both the standing-wave side and the geometric-bridge side,
3. uniqueness is not claimed.

What the update rule is not
The final section of Chapter 5 is deliberately negative in character. It clarifies what the update rule is not allowed to do.
After all constraints have been applied, it becomes tempting to smuggle back familiar structures under new names. Continuous time, global clocks, implicit averaging, background geometry, or hidden optimization principles can easily reappear disguised as features of the update. Section 5.5 exists to block those moves explicitly.
The update rule is not a Hamiltonian in disguise. It is not an action principle waiting to be extremized. It does not know about space, momentum, or energy unless those notions are constructed later as interpretations of persistent patterns. It does not synchronize distant regions, inspect global state, or enforce conservation except through the local, boundary‑aware bookkeeping already established.
This section exists to protect the framework from premature closure. UniNet does not deny that familiar formalisms may emerge. It insists only that they must emerge honestly. If a concept is not grounded in locality, reversibility, and boundary mediation, it does not belong in the update itself. Anything that looks global must be reconstructible from local interaction and accumulated structure.
By stating these exclusions explicitly, Chapter 5 completes its task. The framework has not chosen a dynamics, but it has fenced off an entire landscape of inadmissible ones. What remains is a narrow, disciplined space of updates capable of supporting propagation, stability, and emergence without hidden assumptions.
At this point, the reader should not yet know how UniNet evolves. But they should know exactly what evolution is no longer allowed to be. That clarity is what makes the next chapters possible.

## 5.6 What Update-Function Freedom Remains
The remaining freedom is real, but tightly fenced.

Still free:
1. the precise member of the admissible local unitary family,
2. branch choices within explicit witness families,
3. some coupling ranges before full observational pruning,
4. some coarse-grained constitutive closure choices in the bridge program.

Not free:
1. graph locality,
2. unitarity and no information loss,
3. continuity-compatible flux bookkeeping,
4. the ban on hidden phenomenological edge delays,
5. the demand that any promoted family survive parameter-lock and falsifiability discipline.

So the right conclusion is neither "the update is fully solved" nor "anything goes." The right conclusion is that the admissible class is narrow, wave-like, and already populated by explicit witnesses, while the remaining internal freedom is what later sector chapters and falsifiability rows are supposed to prune.

Updates as transport, not generation
The final constraint on admissible dynamics is interpretive rather than technical: the update rule is a mechanism of transport, not a source of structure.
After all restrictions have been applied, what remains of the update is deliberately modest. It does not create information, invent degrees of freedom, or impose global organization. Its role is to move, rearrange, and redistribute existing structure in a way that respects locality, reversibility, and boundary bookkeeping. Anything that looks like creation, dissipation, or ordering must arise from accumulation, constraint, and access — not from the update itself.
This section exists to prevent a final kind of shortcut. It is tempting to treat the update as the place where complexity enters, where symmetry is enforced, or where macroscopic behavior is decided. UniNet refuses that move. The update rule is blind. It does not know about observers, particles, geometry, or conservation laws beyond what is already encoded locally. It applies its rule and nothing more.
What matters is the inversion this implies. Structure is not explained by dynamics; dynamics are constrained by structure. Boundaries decide what survives. Capacity decides what stabilizes. Observation decides what becomes irreversible. The update merely carries information forward one step at a time, without preference or foresight.
By framing the update this way, Chapter 5 completes its task. Dynamics are no longer mysterious or privileged. They are reduced to their proper role: a disciplined transporter of state through a constrained substrate. Everything interesting — causality, symmetry, particles, time — has already been earned elsewhere.
At this point, the framework is ready to be read rather than extended. Subsequent chapters do not add new kinds of motion. They reinterpret the same motion under different projections. The update has done its job by getting out of the way.

## Chapter 5 Summary
Established in this chapter:
1. the update law is sharply constrained by one-family, homogeneity, locality, and no-information-loss requirements,
2. a Schrodinger-like discrete wave class is admissible as a constructive witness,
3. queue and backpressure conditions define a disciplined regime split rather than a second microscopic law,
4. the admissible set is programmatically non-empty because explicit witness-family routes already exist.

Open:
1. full classification of admissible standing spectra,
2. full observational closure of the Regge-dynamical bridge,
3. final pruning of the remaining free operator family by locked sector data.

What change is no longer allowed to be
This chapter has constrained dynamics without choosing them.
After the structural commitments of earlier chapters, evolution itself could no longer be treated as a free ingredient. Chapter 05 made that explicit. It identified what any admissible update rule must respect: locality, reversibility, homogeneity, and honest interaction with cuts and boundaries. These are not preferences. They are obligations imposed by the framework’s own consistency.
Rather than proposing a specific dynamics, the chapter narrowed the space of possibilities. Entire classes of update rules were ruled out — those that rely on hidden global knowledge, privileged locations, implicit dissipation, or undeclared structure. What remains is a small, disciplined family of updates capable of transporting information without erasing it, propagating influence without shortcuts, and interacting cleanly with boundary bookkeeping.
The introduction of witness families clarified the role of choice without blurring the line between constraint and model. Concrete examples were allowed, but never promoted. Dynamics were demonstrated to be possible, not declared to be unique. This preserved the framework’s auditability and kept later interpretations honest.
Finally, the chapter reframed the role of dynamics itself. The update rule is not a source of structure, symmetry, or direction. It is a transporter. All higher‑level phenomena — causality, particles, time’s arrow, and symmetry breaking — arise from how structure accumulates under constraint, not from what the update decides to create.
By the end of Chapter 05, evolution has been stripped of mystique. Change is no longer something that explains the world; it is something that must fit within it. With this constraint in place, the framework is ready to be read outward — toward geometry, quantum behavior, and eventually chirality — as interpretations of the same disciplined motion under different projections.