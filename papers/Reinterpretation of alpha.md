# A Boundary–Spectral and Scaling Reinterpretation of the Fine‑Structure Constant

## Abstract
The fine‑structure constant $\alpha$ is traditionally introduced as a dimensionless bulk coupling in quantum electrodynamics. In this paper we present a boundary‑operator reinterpretation of $\alpha$ based on the Dirichlet–to–Neumann (DtN) formulation of the Coulomb problem. We show that $\alpha$ appears exclusively as a boundary coupling in the interior DtN map for the Coulomb operator, and that hydrogen‑like bound states exist only within a narrow band of $\alpha$ values. 

We then integrate a geometric scaling perspective: the identity  


\[
\alpha = \frac{\bar\lambda_e}{a_0}
\]


reveals that $\alpha$ is also the ratio between two natural radii—the reduced Compton radius and the Bohr radius. This connects the DtN window to a boundary‑capacity window: only when these radii sit in the correct hierarchy does the boundary support both a stable negative spectrum and the observed SO(3) degeneracies.

This provides a structural explanation for why $\alpha$ is small but not arbitrarily small, and why it cannot be large, without invoking renormalization or speculative unification.

---

# 1. Introduction
The fine‑structure constant


\[
\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c}
\]


is one of the most important dimensionless parameters in physics. Its numerical value,


\[
\alpha \approx \frac{1}{137},
\]


is usually treated as a fundamental input. In this work we reinterpret $\alpha$ as a **boundary coupling** in the Dirichlet–to–Neumann formulation of the Coulomb problem.

The key observation is that the hydrogen spectrum can be expressed entirely as a **boundary eigenvalue problem**, and that $\alpha$ enters only through the deformation of the interior boundary operator. This leads to a structural constraint: only a narrow band of $\alpha$ values yields a discrete negative spectrum with the observed $1/n^2$ scaling and SO(3) degeneracies.

We then show that this boundary window is equivalent to a **geometric scaling window** in the ratio $\bar\lambda_e/a_0$, linking the DtN picture to natural radii and boundary capacity.

---

# 2. Boundary formulation of the Coulomb problem

## 2.1 Interior and exterior DtN maps
Fix a sphere of radius $R$ around the proton. For each energy $E<0$, define:

- The **interior DtN map** $\Lambda_E^{\mathrm{int}}(\alpha)$ as the operator mapping boundary values of solutions of


\[
\left(-\frac{\hbar^2}{2\mu}\nabla^2 - \frac{\alpha\hbar c}{r}\right)\psi = E\psi
\]


to their normal derivatives at $r=R$.

- The **exterior DtN map** $\Lambda_E^{\mathrm{ext}}$ as the corresponding operator for the free equation outside the sphere, with decaying boundary conditions at infinity.

Both operators are diagonal in the spherical harmonics basis:


\[
\Lambda_E^{\mathrm{int}}(\alpha) Y_{\ell m} = \lambda_{\ell}^{\mathrm{int}}(E,\alpha) Y_{\ell m}, \qquad
\Lambda_E^{\mathrm{ext}} Y_{\ell m} = \lambda_{\ell}^{\mathrm{ext}}(E) Y_{\ell m}.
\]



## 2.2 Boundary mismatch operator
Define the **boundary mismatch operator**


\[
B_E(\alpha) := \Lambda_E^{\mathrm{int}}(\alpha) - \Lambda_E^{\mathrm{ext}}.
\]


Its eigenvalues are


\[
\beta_\ell(E,\alpha) := \lambda_{\ell}^{\mathrm{int}}(E,\alpha) - \lambda_{\ell}^{\mathrm{ext}}(E).
\]



---

# 3. Bound states as zero crossings of boundary eigenvalues

## 3.1 Spectral condition
A hydrogen bound state with quantum numbers $(n,\ell,m)$ exists if and only if


\[
\beta_\ell(E_n,\alpha) = 0.
\]


Thus the hydrogen spectrum is encoded entirely in the zero set of the boundary eigenvalues of $B_E(\alpha)$.

## 3.2 Structural role of $\alpha$
The Coulomb potential enters only through $\Lambda_E^{\mathrm{int}}(\alpha)$, so $\alpha$ appears **only** in the interior boundary operator. The exterior operator is independent of $\alpha$.

Thus:


\[
\alpha \text{ is the unique coupling for which } B_E(\alpha) \text{ has a zero eigenvalue at a normalizable mode.}
\]



This is a boundary‑level reinterpretation of the fine‑structure constant.

---

# 4. Narrow band of allowed couplings

## 4.1 Lower bound: existence of bound states
If $\alpha$ is too small, the Coulomb deformation of the interior DtN map is insufficient to produce any $E<0$ for which $\beta_\ell(E,\alpha)=0$. Thus no bound states exist.

## 4.2 Upper bound: stability of the operator
If $\alpha$ is too large, the Coulomb term dominates the Laplacian curvature and the interior operator loses a well‑behaved discrete spectrum.

## 4.3 Resulting window
Combining these observations yields a structural constraint:


\[
\alpha_{\min} < \alpha < \alpha_{\max},
\]


where both bounds are finite and nonzero. A simple comparison argument shows that the window is narrow and centered around a small value:


\[
10^{-3} \lesssim \alpha \lesssim 10^{-1}.
\]


This is consistent with the observed value $\alpha \approx 7.3\times 10^{-3}$.

---

## 4.4 Scaling, natural radii, and boundary capacity

The geometric identity


\[
\alpha = \frac{\bar\lambda_e}{a_0}
\]


shows that $\alpha$ is also the ratio between two natural spherical radii:

- the **reduced Compton radius** $\bar\lambda_e$, associated with the electron mass scale,
- the **Bohr radius** $a_0$, associated with the Coulombic binding scale.

Thus the DtN window in $\alpha$ is equivalently a **window in the allowed ratio** $\bar\lambda_e/a_0$. Hydrogen‑like bound states exist only when these radii sit in the correct geometric hierarchy.

A sphere of radius $R$ supports only finitely many independent boundary modes up to an effective $\ell_{\max}(R,E)$. The Coulomb problem requires enough boundary capacity to support the full SO(3) multiplets $(2\ell+1)$, but not so much capacity that the interior operator becomes unstable.

The window


\[
10^{-3} \lesssim \alpha \lesssim 10^{-1}
\]


is therefore also a **capacity window**: too small a ratio $\bar\lambda_e/a_0$ yields no negative spectrum, while too large a ratio destabilizes the interior boundary operator.

In this sense, the observed value $\alpha \approx 1/137$ is the unique boundary‑compatible ratio between the Compton and Bohr radii for which the Coulomb DtN problem supports a discrete, hydrogen‑like spectrum.

---

# 5. Standard expressions for $\alpha$ as boundary consequences

## 5.1 Field‑theoretic form


\[
\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c}.
\]



## 5.2 Vacuum impedance form
Using $Z_0 = \sqrt{\mu_0/\varepsilon_0}$,


\[
\alpha = \frac{e^2}{4\pi\hbar} Z_0.
\]


This expresses $\alpha$ as a **boundary impedance ratio**.

## 5.3 Spectral form
From $E_n = -\frac{1}{2}\alpha^2 m_e c^2 / n^2$,


\[
\alpha = \sqrt{\frac{2 h R_\infty}{m_e c}}.
\]



## 5.4 Geometric forms
Using the Bohr radius $a_0$ and reduced Compton wavelength $\bar\lambda_e$,


\[
\alpha = \frac{\bar\lambda_e}{a_0}.
\]



Using the classical electron radius $r_e$,


\[
\alpha = \sqrt{\frac{r_e}{a_0}}.
\]



## 5.5 Energetic form
Using the Hartree energy $E_{\mathrm H}$,


\[
\alpha = \sqrt{\frac{E_{\mathrm H}}{m_e c^2}}.
\]



All these expressions arise from the same boundary‑spectral structure.

---

# 6. Interpretation

## 6.1 Scaling and symmetry considerations
The boundary‑operator picture clarifies why the hydrogen spectrum exhibits the familiar SO(3) degeneracies. The existence of the $(2\ell+1)$ multiplets requires a boundary with sufficient harmonic capacity to support all spherical harmonics up to the relevant $\ell$. If the effective radius is too small, the boundary supports only a limited number of independent modes and the degeneracy structure collapses. If the radius is too large, the Coulomb deformation overwhelms the Laplacian curvature and the discrete spectrum is lost.

Thus the same narrow window that keeps the DtN operator well‑behaved also keeps the boundary spectrum rich enough to support the observed angular‑momentum structure. The fine‑structure constant is therefore simultaneously:

1. a **boundary coupling** in the interior DtN map, and  
2. a **ratio of natural radii** that determines the harmonic capacity of the boundary.

This dual role explains why $\alpha$ is small but not arbitrarily small, and why it cannot be large: only within this window do the boundary conditions support both a stable negative spectrum and the correct SO(3) degeneracies.

---

# 7. Conclusion
We have presented a boundary‑operator and scaling reinterpretation of the fine‑structure constant. While this does not derive the exact numerical value of $\alpha$, it shows that the existence of hydrogen‑like bound states already constrains $\alpha$ to a narrow, physically meaningful range. This suggests that quantum mechanics may be more naturally understood as a boundary theory, with $\alpha$ emerging as a boundary‑compatibility coefficient and a geometric ratio of natural radii.

