# The Cut Theorem — the whole idea, in one guided walk

If there’s one idea I’d quietly ask you to keep in the back of your mind while reading UniNet, it’s this: **cuts matter more than they look like they should.**

Pick any region $R$ of the graph. The moment you do, you’ve also created a boundary $\partial R$: the set of connections where “inside” meets “outside.” That boundary isn’t decoration. It’s where the accounting lives.

The theorem spine is almost disarmingly simple. Define the region’s total occupancy

$$
Q_n(R)=\sum_{v\in R}ho_n(v),
$$

and define the net boundary flux $\Phi_n(\partial R)$ as the sum of edge fluxes crossing the cut. Then:

$$
Q_{n+1}(R)-Q_n(R)=-\Phi_n(\partial R).
$$

So whatever changes inside is exactly what crossed the boundary. Nothing is “lost” in the bookkeeping — but also, nothing is magically self‑contained unless the boundary says it is.

And here’s the practical punchline: if you actually want a region to behave like a closed system, you don’t get to declare it — you have to **include the boundary register**. Add a bookkeeping variable that accumulates the boundary flux, and the combined quantity

$$
\widetilde Q_n(R)=Q_n(R)+b_n(\partial R)
$$

becomes exactly conserved. That’s UniNet’s version of closure: **inside + boundary ledger**.

This is also where the horizon language becomes precise. A cut is *closed* when $\Phi_n(\partial R)=0$. A cut is *leaky* when $\Phi_n(\partial R)
eq 0$. The difference isn’t poetic; it’s whether the boundary flux vanishes.

Now add locality. Because updates only propagate locally on the graph, influence has a derived latency tied to graph distance — nothing jumps instantly. So boundaries don’t just filter information; they **delay** it. Whatever the outside learns about the inside has to travel, step by step, until it becomes boundary‑visible.

That sets up the observer story. From the outside, many different interior microstates can be operationally indistinguishable if they induce the same boundary observables. Different interiors, same boundary story — the same physics for the observer. This is where gauge‑style redundancy naturally lives in the framework.

Once you’re comfortable with that, it becomes natural to say that observers — detectors, experiments, even whole laboratories — are cuts in practice. They are interfaces. They carve the world into “what I can access” and “what I can’t,” and what they receive is boundary‑mediated, delayed, and coarse‑grained.

That coarse‑graining does real work. Even though the microscopic dynamics are reversible, the act of observing through a boundary isn’t. Information gets hidden, merged, and discarded in ways that can’t be undone from the outside. **This is where the arrow of time in observed spacetime comes from.** Not because the underlying dynamics point one way, but because once information is lost behind a cut, the observer has no path back to it. From the inside, nothing prefers a direction. From the outside, history starts to look one‑way.

The nice thing about this picture is that it scales. Horizon‑like cuts become a careful way to talk about black‑hole‑style trapping and release. Cosmology becomes boundary‑limited by construction, which is why the same language applies to things like the CMB. And “particles” become stable standing or quasi‑standing mode structure — patterns that persist because the boundary conditions let them.

So when I say “everything is graph cuts,” I don’t mean it as a slogan. I mean it as a guidepost. **Cuts tell you what can be known, what must be tracked to keep conservation exact, and what kinds of structure are even allowed to persist.**

If you follow that thread patiently, a surprising amount of physics stops looking mysterious — and starts looking inevitable.
