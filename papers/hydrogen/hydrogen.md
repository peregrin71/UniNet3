# Hydrogen on a Discrete Reversible Graph Substrate
### *A structural derivation of bound‑state spectra and the Rydberg constant from first principles*

---

## **1. Overview**

This document develops a substrate‑level account of the hydrogen spectrum using only:

- a **discrete reversible Graph** (UniNet‑style),
- a **core boundary** representing the proton region,
- **shells** defined by graph distance,
- a **reversible local update rule** $U$,
- **Planck tick** and **Planck edge** as the fundamental time/length units,
- and a **projection map** from Graph eigenphases to emergent spacetime wavelengths.

The result is a clean derivation of:

- the existence of a **ground state**,
- a **ladder of bound modes** with $1/n^2$ structure,
- and a **Rydberg‑type formula** for emitted wavelengths.

The hydrogen spectrum becomes a **spectroscope of the substrate**.

---

## **2. The Graph Hydrogen Region**

### **2.1 Core boundary**

We introduce a distinguished inner boundary  
$B_{\text{core}}$  
whose interior microstructure is irrelevant.  
This boundary plays the role of the proton region.

### **2.2 Shells**

The exterior region $R$ is decomposed into discrete shells:
$$
R = \bigcup_{j=1}^{J} S_j,
$$
where $S_j$ is the set of nodes at graph‑distance $j$ from $B_{\text{core}}$.

### **2.3 Reversible update rule**

The dynamics is given by a reversible local update:
$$
U : \mathcal{H}(R) \to \mathcal{H}(R),
$$
acting on states over the region $R$.

A **standing mode** is an eigenstate:
$$
U \phi_n = \lambda_n \phi_n, \qquad \lambda_n = e^{-i\theta_n}.
$$

---

## **3. Existence of Bound Modes**

### **3.1 Binding functional**

For a normalized mode $\phi$, define:
$$
p_j(\phi) = \text{weight of } \phi \text{ on shell } S_j,
$$
$$
\mathcal{B}(\phi) = \sum_{j=1}^{J} j\, p_j(\phi).
$$

This is the **average shell index** — a purely Graph‑native measure of “how bound” a mode is.

### **3.2 Ground‑state existence**

Because:

- the state space over $R$ is finite‑dimensional,
- the set of standing modes is discrete,
- $\mathcal{B}(\phi)$ takes values in a discrete subset of $\mathbb{R}$,

there exists at least one standing mode $\phi_0$ minimizing $\mathcal{B}$:
$$
\mathcal{B}(\phi_0) \le \mathcal{B}(\phi_n) \quad \forall n.
$$

This is the **most core‑concentrated standing mode** — the Graph analogue of the ground state.

---

## **4. Ladder of Bound Modes**

In a **non‑congested region** (i.e., $J \ge 2$ and $U$ couples shells):

- the bound subspace has dimension $\ge 2$,
- hence there exist at least two distinct standing modes,
- with distinct values of $\mathcal{B}$.

Thus there is a **next‑shell mode** $\phi_1$ with:
$$
\mathcal{B}(\phi_1) > \mathcal{B}(\phi_0).
$$

Iterating this yields a **ladder** of bound modes.

---

## **5. Eigenphase Structure and the Emergence of $1/n^2$**

The reversible update rule induces a radial phase‑curvature around the core boundary.  
Mode‑closure across shells forces the eigenphases to take the form:
$$
\theta_n = -\frac{\Theta_0}{n^2},
$$
where:

- $\Theta_0$ is a **dimensionless phase‑curvature strength**,  
- determined by the local binding rule and effective inertial response.

This