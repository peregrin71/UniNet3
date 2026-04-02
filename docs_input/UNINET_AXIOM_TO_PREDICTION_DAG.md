# UniNet Axiom-to-Prediction Dependency DAG

Date: 2026-03-30  
Purpose: single traceable map from axioms to derived theorems to section-level falsifiability rows.
Scope: transparency artifact only; no new derivations.

## 1. Node Classes

1. `A*`: axioms/requirements in `../docs_input/UNINET_CORE_AXIOMS.md`.
2. `T*`: derived definitions/lemmas/theorems/corollaries in `../docs_input/UNINET_CORE_AXIOMS.md`.
3. `S*`: sector packaging claims used in section matrices.
4. `P*`: prediction rows in falsifiability matrices.

## 2. Global Skeleton

```text
AXIOM-1/AXIOM-3/AXIOM-4/AXIOM-5/AXIOM-6/AXIOM-7/MODEL-P2
  -> T1.1/T1.2/T1.1(Discrete Gauss) -> T1.2(leaky boundary)
  -> T2.1(closed cones) -> T3.2(observer time) -> T3.4/T3.2(arrow theorem family)
  -> Regime split (QM theorem / GR theorem)
  -> sector packaging (QM/GR/SM/Cosmology)
  -> prediction rows (QM-*, GR-*, SM-*, COS-*)
```

## 3. GR Branch (Buffers -> Emergent Spacetime/Gravity)

```text
AXIOM-3 + AXIOM-4 + AXIOM-5 + AXIOM-6 + AXIOM-7 + MODEL-P2
  -> T1.1 (cut balance)
  -> T1.3/T1.4 + R9/R10 (queue/backpressure constraints)
  -> BRIDGE-P1/P2/P3 (projection bridge)
  -> T(GR latency adaptive)
  -> S-GR packaging
  -> P: GR-CORE-001/002/003, GR-LB-CORE-001, GR deferred clusters
```

Core anchors:

1. `AXIOM-3`: `../docs_input/UNINET_CORE_AXIOMS.md:234`
2. `AXIOM-4`: `../docs_input/UNINET_CORE_AXIOMS.md:243`
3. `AXIOM-5`: `../docs_input/UNINET_CORE_AXIOMS.md:256`
4. `AXIOM-6`: `../docs_input/UNINET_CORE_AXIOMS.md:280`
5. `AXIOM-7`: `../docs_input/UNINET_CORE_AXIOMS.md:298`
6. `MODEL-P2`: `../docs_input/UNINET_CORE_AXIOMS.md:314`
7. `T1.4`: `../docs_input/UNINET_CORE_AXIOMS.md:548`
8. `R9/R10`: `../docs_input/UNINET_CORE_AXIOMS.md:901`, `../docs_input/UNINET_CORE_AXIOMS.md:917`
9. `BRIDGE-P1/P2/P3`: `../docs_input/UNINET_CORE_AXIOMS.md:1085`, `../docs_input/UNINET_CORE_AXIOMS.md:1121`, `../docs_input/UNINET_CORE_AXIOMS.md:1139`
10. `GR theorem`: `../docs_input/UNINET_CORE_AXIOMS.md:1206`

Prediction targets:

1. `GR-CORE-001/002/003`
2. `GR-LB-CORE-001`
3. `GR-LB-DEF-002/003`
4. `GR-BH-DEF-004/005`

## 4. QM Branch (Wave/Particle Interface)

```text
AXIOM-3 + AXIOM-4 + AXIOM-5 + AXIOM-6 + AXIOM-7
  -> QM regime axiom/theorem (static latency)
  -> T3.2 + T3.2(arrow theorem) via coarse-graining map
  -> S-QM packaging
  -> P: QM-CORE-001/002, QM-DEF-003/004
```

Core anchors:

1. `QM axiom/theorem`: `../docs_input/UNINET_CORE_AXIOMS.md:1183`, `1223`
2. `observer-time/arrow`: `../docs_input/UNINET_CORE_AXIOMS.md:667`, `706`

## 5. SM Branch (Transfer Constraints -> Flavor/CP Tests)

```text
SM-FOUND-A1
  -> R5/R6/R8 (chirality + CP metric + admissible window)
  -> S-SM packaging (still partial for gauge derivation)
  -> P: SM-CORE-001/002, SM-DEF-003/004
```

Core anchors:

1. `SM-FOUND-A1`: `../docs_input/UNINET_CORE_AXIOMS.md:333`
2. `R5/R6/R8`: `../docs_input/UNINET_CORE_AXIOMS.md:792`, `833`, `878`

## 6. Cosmology Branch (Buffer Dynamics Packaging)

```text
GR/source bridge + cosmology application block
  -> Dark Energy / Dark Matter / Inflation packaging
  -> S-COS packaging
  -> P: COS-CORE-001..004, COS-DEF-005..007
```

Core anchors:

1. `Dark Energy`: `../docs_input/UNINET_CORE_AXIOMS.md:1223`
2. `Dark Matter`: `../docs_input/UNINET_CORE_AXIOMS.md:1235`
3. `Inflation`: `../docs_input/UNINET_CORE_AXIOMS.md:1244`
4. `queue constraints used by congestion branch`: `866`, `882`

## 7. Explicit Boundary Nodes

These are intentionally non-core until promoted:

1. Gauge-group derivation node ($U(1) x SU(2) x SU(3)$ emergence).
2. Full Page/firewall/ringdown forward models.
3. CMB multipole transfer kernel lock.
4. Collider/direct-detection effective coupling map for non-particle DM branch.

Authoritative deferred list:

1. `../docs_input/UNINET_MERGED_REMAINDER_BACKLOG.md`
2. Deferred rows in section matrices.

## 8. Usage Rule

Every new prediction row must add:

1. one `A*`/`T*` parent path in this DAG,
2. one explicit source anchor in core,
3. one binary reject criterion in matrix row.










