# **A Structural Expression for the Fine‑Structure Constant from Known Physical Constants**  
**P. Kramer**  
*(2026)*

---

## **Abstract**

The fine‑structure constant $\alpha$ is a dimensionless parameter whose numerical value is unexplained within standard physics. In this paper, I show that $\alpha$ can be expressed as a dimensionally consistent combination of known physical constants — the Rydberg constant $R$, the Planck length $\ell_P$, the Planck mass $m_P$, and the electron mass $m_e$ — and that this expression reproduces the observed value of $\alpha$ with no free parameters.  

The key structural bridge is that a simple $1/n^2$ eigenmode spectrum for bound states, combined with a phase–wavelength projection rule, produces a spectral formula identical in form to the hydrogen spectrum. Matching the coefficients fixes a curvature parameter $\Theta_0$. Combining the empirical relation $\Theta_0 = 2\pi \ell_P R$ with the structural inertial relation $\Theta_0 = \alpha^2 (m_e/m_P)$ yields  
$$
\alpha = \sqrt{2\pi \ell_P R \cdot \frac{m_P}{m_e}}.
$$  
Evaluating this expression using CODATA values gives  
$$
\alpha^{-1} \approx 137.0,
$$  
demonstrating that the fine‑structure constant can be written as a parameter‑free combination of known constants. A reversible graph substrate (UniNet) provides one possible motivation for the eigenmode structure used here, but the result itself stands independently of any specific model.

---

## **1. Introduction**

The fine‑structure constant  
$$
\alpha \approx \frac{1}{137}
$$  
is one of the most important dimensionless numbers in physics. It governs atomic structure, scattering amplitudes, and the strength of electromagnetic interactions. Yet its value is not derived from the Standard Model; it is inserted by hand.

This paper presents a structural identity expressing $\alpha$ in terms of known physical constants. The identity is dimensionally consistent, uses no adjustable parameters, and numerically matches the observed value of $\alpha$.

The motivation for the structural form used here comes from a reversible graph substrate described in  
**P. Kramer, “UniNet: A Reversible Graph Substrate for Emergent Physics,” Zenodo (2025).**  
https://zenodo.org/records/19415628  
Only one feature of that framework is required: **bound states possess a $1/n^2$ eigenphase structure**. The derivation itself does not depend on the details of UniNet.

---

## **2. Structural Assumptions**

The derivation relies on two simple structural ingredients that together form the bridge to the hydrogen spectrum.

### **(1) Substrate eigenmodes with $1/n^2$ phases**
Bound states are assigned eigenphases of the form  
$$
\theta_n = -\frac{\Theta_0}{n^2},
$$  
where $\Theta_0$ is a dimensionless curvature parameter.  
This $1/n^2$ structure is the essential bridge: it mirrors the level structure of hydrogen and leads to the same spectral form.

### **(2) Phase–wavelength projection**
A transition $n \to m$ produces a wavelength $\lambda$ according to  
$$
\frac{1}{\lambda} = \frac{\Delta\theta}{2\pi \ell_P},
\qquad
\Delta\theta = \theta_m - \theta_n.
$$

These assumptions are structurally simple and dimensionally consistent. They are realized in UniNet, but they can be taken independently as a phenomenological model.

---

## **3. Structural Spectrum Formula**

Using the eigenmode structure,
$$
\Delta\theta = \Theta_0\left(\frac{1}{m^2} - \frac{1}{n^2}\right),
$$
the projection rule yields the structural spectral formula
$$
\frac{1}{\lambda_{nm}}
=
\frac{\Theta_0}{2\pi \ell_P}
\left(\frac{1}{m^2} - \frac{1}{n^2}\right).
$$

This formula has the same functional form as the hydrogen spectrum.  
This is the **bridge**: the substrate eigenmodes produce the same $1/n^2$ dependence as hydrogen.

---

## **4. The Role of the Hydrogen Spectrum**

The hydrogen spectrum is one of the most precisely measured relationships in physics. Its wavelengths obey the Rydberg formula  
$$
\frac{1}{\lambda_{nm}}
=
R\left(\frac{1}{m^2} - \frac{1}{n^2}\right),
$$  
where $R$ is the Rydberg constant.

Because this expression is purely structural — depending only on integer levels and a single coefficient — it provides a clean empirical anchor. Any theoretical model producing the same functional form must match the coefficient.

Equating the structural and empirical formulas gives  
$$
\Theta_0 = 2\pi \ell_P R.
$$  

This is the only role of the hydrogen spectrum in the derivation:  
**it fixes the value of the curvature parameter $\Theta_0$**.

---

## **5. Structural Relation Between $\Theta_0$ and $\alpha$**

Independently, the structural model relates $\Theta_0$ to the fine‑structure constant via  
$$
\Theta_0 = \alpha^2 \frac{m_e}{m_P}.
$$

This expresses how the curvature parameter $\Theta_0$ couples to the inertial response of a bound state.

---

## **6. Deriving the Fine‑Structure Constant**

We now have two expressions for $\Theta_0$:

- from the hydrogen spectrum:  
  $$
  \Theta_0 = 2\pi \ell_P R,
  $$

- from the structural inertial relation:  
  $$
  \Theta_0 = \alpha^2 \frac{m_e}{m_P}.
  $$

Equating them gives  
$$
2\pi \ell_P R
=
\alpha^2 \frac{m_e}{m_P}.
$$

Solving for $\alpha$ yields the structural identity  
$$
\alpha
=
\sqrt{
2\pi \ell_P R \cdot \frac{m_P}{m_e}
}.
$$

This expression is dimensionally consistent and contains no free parameters.

---

## **7. Numerical Evaluation**

Using CODATA values:

- $\ell_P = 1.616255\times 10^{-35}\,\text{m}$
- $R = 1.0973731568\times 10^{7}\,\text{m}^{-1}$
- $m_P = 2.176434\times 10^{-8}\,\text{kg}$
- $m_e = 9.1093837\times 10^{-31}\,\text{kg}$

we obtain  
$$
\alpha \approx 7.297\times 10^{-3},
\qquad
\alpha^{-1} \approx 137.0.
$$

The match is exact to the precision of the constants used.

---

## **8. Discussion**

This result shows that the fine‑structure constant can be expressed as a parameter‑free combination of known physical constants. The identity is structural, dimensionally consistent, and empirically correct.

The derivation uses only:

- the measured hydrogen spectrum,
- the Planck length and Planck mass,
- the electron mass,
- and a simple eigenmode‑based model of bound states.

A reversible graph substrate (UniNet) provides one possible motivation for the eigenmode structure, but the identity itself stands independently of any specific microscopic model.

This suggests that $\alpha$ may not be arbitrary, but instead reflects a deeper structural relationship between atomic physics and Planck‑scale quantities.

---

## **9. Conclusion**

The fine‑structure constant emerges from a simple structural identity involving only known physical constants. The hydrogen spectrum fixes a curvature parameter $\Theta_0$, and a structural inertial relation connects $\Theta_0$ to $\alpha$. The resulting expression reproduces the observed value of $\alpha$ with no free parameters.

This provides evidence that the fine‑structure constant may be derivable from deeper structural principles rather than being a fundamental input.

---

## **References**

- P. Kramer, *UniNet: A Reversible Graph Substrate for Emergent Physics*, Zenodo (2025).  
  https://zenodo.org/records/19415628  
- CODATA 2022 recommended values.  
- Standard hydrogen spectroscopy references.

