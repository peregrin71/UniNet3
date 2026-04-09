# A Boundary‑First Interpretation of Quantum Measurement  
### Sampling, Spacetime Integration, and the Origin of Apparent Randomness  
**Pepijn Kramer — 2026**

## Abstract
Quantum mechanics is traditionally formulated in terms of Hilbert spaces, operators, and probabilistic measurement postulates.  
This note presents a boundary‑first perspective in which the quantum state is understood as a *boundary signature* of an inaccessible interior evolution.  
Measurement is modeled as a finite‑duration, finite‑area *spacetime integral* over the evolving boundary.  
Apparent quantum randomness arises not from indeterminism in the interior, but from the observer’s coarse, unsynchronized sampling of a continuously evolving boundary pattern.  
The Born rule emerges naturally as the stable residue of this integration.

---

## 1. Introduction
Standard quantum mechanics treats the wavefunction as a complete description of a system and introduces randomness through the Born rule.  
In contrast, boundary‑centric physics (familiar from Gauss, Green, Stokes, and Helmholtz) emphasizes that many interior configurations can share the same boundary behavior.  
This note explores the consequences of applying this boundary‑first logic to quantum systems.

The key idea is simple:

> **The boundary evolves continuously in space and time.  
> The observer samples it only during a finite spacetime event.  
> Apparent randomness is introduced by the sampling, not the interior.**

---

## 2. Boundary Signatures and Equivalence Classes
Consider an interior configuration $\psi(x,t)$ defined on a region $R$.  
Define a boundary map
$$
B\psi = \text{(boundary values and derivatives on } \partial R).
$$

Two interior configurations are *boundary‑equivalent* if they share the same boundary signature:
$$
\psi \sim \phi \quad \Longleftrightarrow \quad B\psi = B\phi.
$$

The physical state is then the equivalence class
$$
[\psi] = \{\phi : B\phi = B\psi\},
$$
not the interior function itself.  
This captures the idea that the boundary is all the observer can access.

---

## 3. Continuous Boundary Evolution
Even the simplest quantum system exhibits nontrivial boundary dynamics.  
For a two‑level system,
$$
|\psi(t)\rangle = a e^{-i\omega_1 t}|1\rangle + b e^{-i\omega_2 t}|2\rangle,
$$
the boundary signature oscillates continuously due to the evolving relative phase
$$
\Delta\phi(t) = (\omega_2 - \omega_1)t.
$$

Thus the boundary is a *moving target*.

---

## 4. Measurement as a Spacetime Integral
A real measurement is not instantaneous.  
It is a finite‑duration, finite‑area interaction between the observer’s apparatus and a patch of the boundary world‑sheet.

Let the detector couple to a boundary patch $P \subset \partial R \times \mathbb{R}$ with area element $dA$ and time element $dt$.  
The measurement functional takes the form
$$
\mathcal{M}(\psi) \sim \iint_{P} F(B\psi(x,t))\, dA\, dt,
$$
where $F$ encodes the detector response.

Thus:

> **A measurement is a spacetime integral over the evolving boundary.**

---

## 5. Origin of Apparent Randomness
The observer does not track the boundary continuously.  
They choose a measurement window $P$ whose micro‑alignment with the interior evolution is uncontrolled.

Because $B\psi(x,t)$ oscillates rapidly in both space and time, the integral over $P$ depends sensitively on the exact micro‑timing and micro‑geometry of the interaction.

From the interior’s perspective, the observer’s sampling window is effectively random.  
Thus:

> **Quantum randomness = randomness in the observer’s sampling of a continuously evolving boundary.**

No indeterminism is required in the interior dynamics.

---

## 6. Emergence of the Born Rule
For a superposition
$$
|\psi(t)\rangle = \sum_n c_n e^{-iE_n t/\hbar}|n\rangle,
$$
the detector integrates expressions of the form
$$
\iint_P \langle \phi | \psi(x,t) \rangle \langle \psi(x,t) | \phi \rangle \, dA\, dt.
$$

Cross‑terms involving $e^{-i(E_m - E_n)t/\hbar}$ average to zero over any patch $P$ larger than the interior coherence timescale.

What remains is
$$
|c_\phi|^2,
$$
the Born probability.

Thus the Born rule is the *stable residue* of spacetime‑averaged boundary compatibility.

---

## 7. Collapse as Boundary Commitment
During the measurement window, the detector integrates the boundary signal until a threshold is crossed.  
This produces a definite outcome and enforces a new boundary condition.  
No metaphysical collapse is required — only boundary commitment.

---

## 8. Discussion
This boundary‑first perspective explains:

- **Interference:** spatial variation of the boundary signature.  
- **Decoherence:** large boundary patches smear out phase information.  
- **Observer dependence:** different observers sample different patches.  
- **Classicality:** macroscopic detectors integrate over enormous spacetime regions.  
- **Randomness:** sampling artifact, not interior indeterminism.

The entire quantum formalism emerges naturally from the geometry and dynamics of boundary sampling.

---

## 9. Conclusion
Quantum mechanics can be understood as a theory of **boundary inference**.  
The wavefunction encodes boundary‑compatible interior possibilities.  
Measurement is a spacetime integral over a dynamic boundary patch.  
Randomness arises from the observer’s coarse, unsynchronized sampling of that boundary.

This perspective unifies interference, decoherence, Born probabilities, and measurement without invoking intrinsic randomness or collapse.

