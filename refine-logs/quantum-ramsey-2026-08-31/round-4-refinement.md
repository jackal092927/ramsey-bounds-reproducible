# Round 4 Refinement

## Problem Anchor

- **Bottom-line problem:** Design a quantum algorithm for constructing classical Ramsey lower-bound witnesses that has a rigorous asymptotic advantage over a clearly specified classical algorithmic model, while returning an ordinary graph that can be checked independently.
- **Must-solve bottleneck:** Existing quantum Ramsey work already covers Hamiltonians, QUBO, annealing, and generic quadratic search. A publishable result must exploit Ramsey structure and prove an end-to-end theorem.
- **Non-goals:** No NISQ advantage claim; no numerical bound without a checked witness; no upper-bound claim without a classical certificate; no topology without a spectral theorem.
- **Success condition:** A Ramsey-specific asymptotic advantage survives adversarial correctness/novelty review and all access, gate, update, and verification costs.

## Corrections Carried Forward

1. The Johnson-walk gain disappears when its monochromatic-completion markedness test is charged.
2. The universal \(\Omega(R\sqrt d)\) lower bound is false.
3. The exact conditional expectation after resampling is
   \[
   \mathbb E[Z\mid x,S]
   =
   p+\sum_{j=2}^{k-1}
   C_j(x,S)2^{-\binom j2}.
   \]
4. At \(n=10,k=6\), the all-red state satisfies the symmetric LLL parameter inequality but has conditional expected dirty-violation count about \(18.93\).
5. The all-red result is pointwise/worst-case; typical trajectory behavior remains open.

## Honest Baseline

With probability at least \(1-\delta\), maintain a duplicate-free queue \(Q_i=M(x_i)\) of all current flaws. After resampling \(S_i\),

\[
Q_{i+1}
=
\bigl(Q_i\setminus\Gamma^+(S_i)\bigr)
\cup
\bigl(M(x_{i+1})\cap\Gamma^+(S_i)\bigr).
\]

If a coherent flaw test costs \(q\), the predicate-query term is

\[
\widetilde O\!\left(
q\left[
\sqrt{m(Z_0+1)}
+\sum_i\sqrt{D(Z_i+1)}
\right]\right).
\]

This is not an end-to-end theorem. Purging old queue items, coherent found-set membership, state preparation, reversible access, memory, error allocation, and deterministic verification remain charged.

## Proposed Live Mechanism Before Round 5

For a valid batch \(B\), define

\[
U(B)=\bigcup_{S\in B}\Gamma^+(S),
\qquad
g(B)=\frac{|B|D}{|U(B)|}.
\]

The hypothesis was that a growing \(g(B)\) might reduce candidate volume and give a \(\sqrt g\) quantum enumeration saving without cross-step coherent-state reuse.

The proposed one-week gate was:

1. measure conditional compatibility and overlap on genuine Ramsey resampling trajectories;
2. derive combinatorial bounds on \(g(B)\) for valid schedules;
3. charge all queue and enumeration costs;
4. stop unless overlap gives an end-to-end \(o(R\sqrt d)\) bound in the diagonal Ramsey regime.

## Round 5 Targeted Question

Before adopting overlap as a live mechanism, compute its best possible ceiling for pairwise nondependent Moser--Tardos batches. If the ceiling is only polylogarithmic in \(n\), close the route rather than replacing it with another framing.

## Venue Decision

ITCS 2027 remains no-go because no central quantum theorem exists.

