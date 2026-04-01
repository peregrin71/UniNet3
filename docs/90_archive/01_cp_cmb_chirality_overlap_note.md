# UniNet Note: CP and CMB Constraints on Chirality (Ballpark Overlap)

**Date:** 2026-03-30  
**Purpose:** Provide a buildup-stage, non-derivation estimate of whether current CP-violation and CMB parity/birefringence constraints can allow an overlapping chirality window.

---

## Scope

This note is a **consistency check**, not a parameter derivation or fit.  
Assume a small effective chirality-control parameter $\chi$ that influences both:

- particle-sector CP observables, and
- CMB parity/birefringence observables.

Use linearized scaling near the weakly-broken regime:

```math
O_{CP} \sim c_{CP}\,\chi,\qquad O_{CMB} \sim c_{CMB}\,\chi,
```

with model-dependent coefficients $c_{\mathrm{CP}}$, $c_{\mathrm{CMB}}$.

---

## Data Anchors (Current Literature)

1. **Kaon CP violation scale (PDG 2025):**

```math
|\epsilon| = (2.228 \pm 0.011)\times 10^{-3}.
```

2. **CMB parity/birefringence sensitivity scales:**

- BICEP/Keck BK18 multipole-dependent birefringence step-size uncertainty: `< 0.15 deg` (68% CL), i.e. about `2.6e-3 rad`.
- Planck 2018 anisotropic birefringence:

```math
A^{\alpha\alpha} < 0.104\ {\rm deg}^2 \quad (95\%~CL),
```

with sliced case $A^{\alpha\alpha} < 0.085 deg^2$.
- SPT (2025) anisotropic birefringence:

```math
A_{CB} < 1.2\times 10^{-4}\quad (95\%~CL),
```

and `0.53e-4` with additional lensing prior.

---

## Ballpark Overlap Statement

If $c_{\mathrm{CP}}$ and $c_{\mathrm{CMB}}$ are not highly hierarchical (order-unity to within 1-2 orders of magnitude), then:

- CP suggests a characteristic symmetry-breaking scale near `1e-3`.
- CMB constraints admit effects at roughly the `few x 1e-3`-equivalent angle scale (dataset/model dependent).

So an overlap window is plausible around:

```text
chi ~ 1e-3  (ballpark)
```

with possible broadening/narrowing depending on the exact map from $\chi$ to observables.

---

## Interpretation for UniNet Build-Up Chapter

- The overlap result supports a **non-empty admissible region** for constrained `U`.
- This is compatible with the current design choice of small chiral mixing / small CP non-commutation.
- It does **not** validate uniqueness or prove the model; it only removes immediate scale-level tension.

---

## Caveats

- This note compares scales, not full likelihoods.
- Different observables probe different transfer-function combinations.
- A rigorous step requires a joint forward model and global likelihood over CP + CMB datasets.

---

## Sources

- PDG 2025 strange meson summary tables:  
  https://pdg.lbl.gov/2025/tables/rpp2025-tab-mesons-strange.pdf
- BICEP/Keck XXI (2026):  
  https://arxiv.org/abs/2603.06812
- Planck 2018 anisotropic birefringence constraints:  
  https://arxiv.org/abs/2008.10334
- SPT anisotropic birefringence constraints (2025):  
  https://arxiv.org/abs/2510.07928






