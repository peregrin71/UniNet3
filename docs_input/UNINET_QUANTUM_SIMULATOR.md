Yes - modeling graph cuts / boundaries with qubits (or better: qudits) is a very natural fit with what you've been building. And there's already a close cousin of the idea in the quantum-gravity / holography literature: bulk-boundary mappings implemented as quantum error-correcting codes and tensor networks. [arxiv.org], [ncatlab.org], [errorcorre...ionzoo.org]
Let me connect the dots in a way that stays faithful to UniNet and to what quantum hardware is good at.

1) Why "boundaries as qubits" is conceptually aligned with UniNet
In your UniNet core, "observable facts are exported only through boundary cuts," and projection happens after micro-evolution (so boundaries are the natural interface). 
That means a boundary is essentially an information-carrying interface - and quantum computers are literally machines for representing and evolving quantum information. [onedrive.live.com], [onedrive.live.com]
So the mapping you're intuiting is:

Cut / boundary <-> quantum register
Interior <-> logical degrees of freedom (encoded, not explicitly simulated)
Boundary symmetries / constraints <-> stabilizers / code constraints / gauge redundancy
Propagation across cuts <-> local quantum channels / circuits

This is exactly the lens of holographic quantum error-correcting codes: a tensor-network encoder acts as an isometry from "bulk" logical DOFs to "boundary" physical DOFs. [arxiv.org], [ncatlab.org], [errorcorre...ionzoo.org]
That's "graph cut with qubits" in almost literal form.

2) The closest established tool: holographic QECC / tensor-network codes
The Pastawski-Yoshida-Harlow-Preskill paper ("Holographic quantum error-correcting codes") proposes toy models where a tensor network defines an encoder mapping bulk Hilbert space to boundary Hilbert space, reproducing key bulk/boundary features. 
The HaPPY code is the canonical named instance; it's widely described as capturing characteristic properties "akin to the encoding of bulk states by boundary states" expected in AdS/CFT. [arxiv.org] [ncatlab.org], [errorcorre...ionzoo.org]
This doesn't mean UniNet = AdS/CFT - but it does tell you: the boundary-as-quantum-register paradigm is technically coherent and already studied.

3) Why qudits may be even more natural than qubits
Your boundaries likely carry structured, symmetry-constrained variables. In quantum simulation of gauge theories, people increasingly use qudits because gauge fields are naturally higher-dimensional and qudits reduce register size and circuit complexity. A concrete example: a trapped-ion qudit quantum computer simulating 2D lattice gauge theories, explicitly noting qudits are "ideally suited" for gauge fields. [nature.com], [arxiv.org]
That maps cleanly onto your intuition that "symmetries on boundaries" are the key.
So: if your boundary DOFs aren't binary, don't force them to be qubits. Use qudits.

4) Two practical architectures you could aim for
A) Boundary-state emulator (QECC / tensor network on QC)
Goal: represent the state of a cut as a quantum code state, evolve boundary updates as a circuit.

Use a holographic-code style encoder (HaPPY-like or MERA-like circuit family) to represent a compressed interior logically encoded into boundary qubits/qudits. [arxiv.org], [nature.com]
Apply local boundary update rules (your "boundary update rules themselves") as shallow circuits acting only on the boundary register.
Periodically "measure" boundary observables and project into emergent spacetime variables (your movie-render step).

This fits your "we don't evolve spacetime continuously; we sample to render" idea.
B) Cut-dynamics as lattice gauge / quantum channel simulation
Goal: treat cuts as dynamical interfaces with conservation / redundancy constraints.

Encode boundary symmetries as gauge-like constraints (stabilizers, Gauss-law-like constraints).
Evolve with digital simulation methods used in lattice gauge theory quantum simulation (VQE for ground states, trotterized real-time, etc.). The literature explicitly motivates quantum computers here due to classical difficulty. [nature.com], [quantera.eu]

This is closer to "simulate the boundary physics directly," independent of any bulk reconstruction.

5) What "graph cuts with qubits" might look like in UniNet terms (concrete sketch)
Here's a minimal, implementable mental model:

Choose a region RRR in the UniNet graph and define its cut \partialR\partial R\partialR.
Define a boundary Hilbert space H\partialR\mathcal{H}_{\partial R}H\partialR represented by mmm qubits (or qudits).
Define an encoding isometry V:Hint->H\partialRV:\mathcal{H}_{\text{int}} \to \mathcal{H}_{\partial R}V:Hint->H\partialR (a circuit / tensor network) that maps interior logical DOFs into boundary physical DOFs - this is exactly what holographic QECCs formalize. [arxiv.org], [ncatlab.org]
Evolve the boundary register with a local update circuit U\partialRU_{\partial R}U\partialR representing:

boundary flux update,
congestion / saturation state changes,
symmetry-preserving constraints.


Only when needed, project boundary data into observed spacetime variables (your "play a movie" step).

No bulk PDE solving. No global state.

6) What's still genuinely hard (so we don't overpromise)
Even though the paradigm is sound, two difficult bridges remain (and they're the same ones your documents already flag as "deferred"/"postulate" style gaps):

Choosing the right boundary DOFs: what exactly are the qubits/qudits representing for UniNet (which boundary algebra)? The holographic code literature gives patterns, but UniNet's specific observable map must be fixed.
Defining the update circuit for boundaries: you've argued boundary update rules exist; the next step is pinning down a concrete family that preserves your constraints (unitarity/locality/cut-balance) and matches observed pruning.

Those aren't blockers conceptually - they're "engineering the interface" problems.

7) Why this idea is especially appealing for you
You've been pushing the view that:

interiors can be collapsed,
boundaries carry the relevant information,
projection is occasional.

Quantum hardware excels at:

representing boundary states compactly (entanglement),
applying local updates in parallel,
sampling observables.

So yes - it feels natural because it matches the computational grain of the theory.

If you want one crisp next move (no extra tools needed)
Pick one "cut" toy model:

a small boundary (say 20-100 qubits / qudits)
a simple encoding (HaPPY-like or MERA-like circuit family)
a simple boundary update rule (your congestion/bandwidth effect as a local channel)
and see if you can reproduce any coarse observable (e.g., a toy "time dilation" proxy or a toy "horizon saturation" transition).

That would turn your intuition into an executable prototype.
And yes: "graph cuts with qubits" is a very legitimate direction - it's aligned with known bulk/boundary QECC work and with practical quantum simulation of gauge-constrained systems. [arxiv.org], [nature.com], [quantera.eu]
