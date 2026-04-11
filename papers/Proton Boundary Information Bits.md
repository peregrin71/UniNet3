# Observable Information Content of a Proton Boundary in UniNet

The goal is to quantify the **observable** degrees of freedom of a proton-like SU(3) object under UniNet’s boundary‑first ontology. By AXIOM‑8, AXIOM‑9, and AXIOM‑10, only boundary signatures matter:

- AXIOM‑8: “Graph cuts are primitive… one must track boundary flux through $\partial R$.”
- AXIOM‑9: “Interior microstates are operationally accessible only through boundary observables.”
- AXIOM‑10: “Long‑lived particle-like excitations are boundary-stabilized standing or quasi-standing modes…”

Everything inside the cut is redundancy; only the **boundary field** $c_e^\*$ on $\partial R$ contributes to observable information.

---

## 1. Boundary field and spherical coarse‑graining

For a proton-like SU(3) object:

- the boundary $\partial R$ coarse‑grains to a combinatorial $S^2$,
- the effective boundary field is $c_e^\*$ (edge‑length / buffering),
- isotropy forces $c_e^\*$ to be well-approximated by a **low‑$l$ spherical harmonic expansion**.

Write:

$$
c_e^\*(\theta,\phi) \approx \sum_{l=0}^{l_{\max}} \sum_{m=-l}^l a_{lm} Y_{lm}(\theta,\phi).
$$

Boundary isotropy and color‑singletness collapse almost all coefficients.

---

## 2. What survives isotropy and color singletness

### 2.1 Monopole term ($l=0$)
The only rotationally invariant component is:

$$
a_{00} Y_{00}(\theta,\phi),
$$

representing the **overall boundary intensity** (mass/charge‑like scalar).  
This is **1 continuous degree of freedom**.

### 2.2 Spin orientation (dipole axis)
The proton’s spin appears as a preferred axis in the coupling of the standing mode to the boundary. This corresponds to a **unit vector** on $S^2$:

$$
\hat{s} = (\theta_s, \phi_s),
$$

giving **2 continuous degrees of freedom**.

### 2.3 Discrete labels
A few discrete invariants survive boundary projection:

- spin up/down along a chosen axis (1 bit),
- parity or similar discrete signatures (1–2 bits).

Color does **not** survive: the proton is a color singlet, and the SU(3) triplet is fully hidden from $\partial R$.

---

## 3. Total continuous degrees of freedom

Collecting the surviving continuous parameters:

- monopole strength: $1$ DOF,
- spin orientation: $2$ DOF.

So the proton boundary has:

$$
N_{\text{cont}} = 3 \quad \text{continuous degrees of freedom}.
$$

Everything else is washed out by isotropy or hidden by color singletness.

---

## 4. Converting to information (bits)

Let the observer resolve each continuous parameter to precision $\Delta$.

If each parameter is resolved to $\sim 10^{-3}$–$10^{-4}$ relative precision, then each continuous DOF carries:

$$
\log_2\!\left(\frac{1}{\Delta}\right) \approx 10\text{–}12 \text{ bits}.
$$

Thus:

- monopole: $\sim 10$–$12$ bits,
- spin orientation (two angles): $\sim 20$–$24$ bits,
- discrete labels: $\sim 2$–$4$ bits.

Total observable information:

$$
S_{\text{cut}}^{(p)} \approx 32\text{–}40 \text{ bits}.
$$

This is the **cut‑entropy** of a proton boundary: the number of distinguishable boundary signatures consistent with “this is a proton.”

---

## 5. Interpretation

Even if the substrate realization of the proton spans $\sim 5\times 10^{19}$ edges across, the **boundary‑visible** information content is only:

- **three continuous parameters**, plus
- **a few discrete bits**, totaling
- **$\sim 30$–$40$ bits** at realistic resolution.

The proton is structurally simple because its **boundary invariants** are simple. The enormous substrate size is merely the resolution needed to stabilize those invariants under local, reversible UniNet dynamics.



## Information capacity of a proton-sized boundary (Bekenstein bound)

Using the energy–radius form of the Bekenstein bound gives a far tighter limit than the holographic black‑hole area bound.

The bound is

$$
S \le \frac{2\pi E R}{\hbar c},
\qquad
N_{\text{bits}} = \frac{S}{k_B \ln 2}.
$$

For a proton:

- Energy  
  $$E \approx m_p c^2 \approx 938\,\text{MeV} \approx 1.50\times 10^{-10}\,\text{J}$$

- Radius  
  $$R \approx 0.84\times 10^{-15}\,\text{m}$$

- Constants  
  $$\hbar c \approx 3.17\times 10^{-26}\,\text{J\,m}, \qquad \ln 2 \approx 0.693$$

Compute the dimensionless factor:

$$
\frac{E R}{\hbar c}
\approx
\frac{1.50\times 10^{-10}\cdot 0.84\times 10^{-15}}{3.17\times 10^{-26}}
\approx 4.0.
$$

Then the bit bound becomes

$$
N_{\text{bits}}^{\max}
\approx
\frac{2\pi}{\ln 2}\,\frac{E R}{\hbar c}
\approx
\frac{2\pi}{0.693}\times 4.0
\approx 36.
$$

### Result

A proton-sized boundary can store at most **on the order of a few dozen bits** according to the Bekenstein bound—dramatically lower than the \(10^{40}\) bits implied by the black‑hole area limit.

This fits beautifully with the Gaussian/boundary interpretation: the boundary of a proton carries only a tiny amount of accessible information, while the interior microstructure can be vastly richer, with many interior configurations mapping to the same small boundary signature.


# Logical Comparison of Proton Boundary Information Content  
### UniNet Boundary Reduction vs. Bekenstein Energy–Radius Bound

Both derivations constrain the **maximum observable information** on a proton-sized boundary. They arise from different principles but converge on the same scale: a few dozen bits.

---

## 1. UniNet: Boundary‑Observable Reduction

UniNet’s axioms imply that only boundary-accessible quantities matter:

- AXIOM‑8: cuts are primitive; all exchange is through $\partial R$.
- AXIOM‑9: interior microstates are equivalent if they produce the same boundary observables.
- AXIOM‑10: particles are boundary-stabilized standing modes.

The boundary field $c_e^*(\theta,\phi)$ on a coarse-grained $S^2$ admits a spherical harmonic expansion:

$$
c_e^*(\theta,\phi)
=
\sum_{l=0}^{l_{\max}}
\sum_{m=-l}^{l}
a_{lm} Y_{lm}(\theta,\phi).
$$

For a proton-like SU(3) object:

- isotropy suppresses all but the lowest multipoles,
- color singletness hides all SU(3) internal structure,
- only a tiny set of invariants survive.

### Surviving continuous degrees of freedom
- monopole amplitude $a_{00}$ → 1 DOF  
- spin orientation $(\theta_s,\phi_s)$ → 2 DOF  

Total:
$$
N_{\text{cont}} = 3.
$$

### Surviving discrete degrees of freedom
- spin up/down (1 bit)  
- parity-like labels (1–2 bits)

### Information count
If each continuous parameter is resolved to $\sim 10^{-3}$–$10^{-4}$ precision:

- monopole: $\sim 10$–$12$ bits  
- spin orientation: $\sim 20$–$24$ bits  
- discrete labels: $\sim 2$–$4$ bits  

Total UniNet boundary information:

$$
S_{\text{cut}}^{(p)} \approx 32\text{–}40 \text{ bits}.
$$

---

## 2. Bekenstein: Energy–Radius Information Bound

The Bekenstein bound limits the entropy of any system of energy $E$ confined to radius $R$:

$$
S \le \frac{2\pi E R}{\hbar c},
\qquad
N_{\text{bits}} = \frac{S}{k_B \ln 2}.
$$

For a proton:

- $E \approx 1.50\times 10^{-10}\,\text{J}$  
- $R \approx 0.84\times 10^{-15}\,\text{m}$  
- $\hbar c \approx 3.17\times 10^{-26}\,\text{J\,m}$  

Compute:

$$
\frac{E R}{\hbar c} \approx 4.0.
$$

Thus:

$$
N_{\text{bits}}^{\max}
\approx
\frac{2\pi}{\ln 2}\times 4
\approx 36.
$$

The Bekenstein bound independently caps the information capacity of a proton-sized region at **≈36 bits**.

---

## 3. Logical Comparison

| Aspect | UniNet Boundary Reduction | Bekenstein Bound |
|-------|---------------------------|------------------|
| Origin of limit | Structural collapse of boundary observables | Thermodynamic energy–radius constraint |
| What is counted | Only DOFs that survive projection onto $\partial R$ | Maximum entropy allowed by physics |
| Mechanism | Mode degeneracy + isotropy + color singletness | $S \le 2\pi E R / \hbar c$ |
| Result | $\sim 32$–$40$ bits | $\sim 36$ bits |
| Interpretation | Boundary cannot encode more than a few parameters | No proton-sized system can store more than a few dozen bits |

---

## 4. Unified conclusion

Both derivations — one structural, one thermodynamic — independently conclude:

> **A proton boundary can carry only a few dozen bits of observable information.**

The UniNet argument explains *why* the boundary collapses to so few invariants.  
The Bekenstein argument shows *that it cannot be otherwise* for any physical system of that size and energy.

The proton’s interior may involve $\sim 10^{19}$ substrate edges, but almost all of that is redundant under boundary-limited observation. The boundary is the bottleneck; the interior is a high-resolution realization of a very small observable signature.
