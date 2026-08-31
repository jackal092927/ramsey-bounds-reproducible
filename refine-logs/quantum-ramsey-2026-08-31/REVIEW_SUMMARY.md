# Review Summary

## Final verdict

**Current LLL-based quantum Ramsey program: ABANDON.**

This verdict is scoped. It rejects QUBO/QAOA/annealing, Grover-in-Moser--Tardos, the proposed Johnson walks, the proposed universal lower bound, and standard-batch overlap as an ITCS-level quantum-advantage route. It does not prove that every possible quantum Ramsey algorithm is impossible.

**ITCS 2027: NO-GO.** The project has no central positive quantum theorem and the deadline is days away.

## Results that survived review

1. Exact conditional resampling identity:
   \[
   \mathbb E[Z\mid x,S]
   =
   p+\sum_{j=2}^{k-1}
   C_j(x,S)2^{-\binom j2}.
   \]
2. Pointwise counterexample at \(n=10,k=6\):
   \[
   e(d+1)p<1
   \quad\text{but}\quad
   \mathbb E[Z\mid x,S]\approx18.92975.
   \]
3. Standard valid-batch overlap cap:
   \[
   g(B)\le\binom k2.
   \]
4. Pairwise dirty-neighborhood overlap formula and diagonal-regime asymptotics.
5. Exact \(n=5\) topology boundary: 12 valid triangle-avoiding colorings, all isolated under single-edge valid moves.
6. Correct bounded-error queue invariant and predicate-query baseline, with explicit warnings about uncounted queue/data-access costs.

## Claims rejected during review

- The direct \(\widetilde O(R\sqrt d)\) Grover composition is not a novel main contribution.
- Cross-step coherent walk reuse is unsupported after measurement and classical resampling.
- The within-step Johnson walk loses its gain when markedness is charged.
- A universal \(\Omega(R\sqrt d)\) lower bound is false.
- The LLL condition does not give a history-by-history \(dp\) bound.
- Neighborhood overlap in standard valid batches cannot yield a polynomial-in-\(n\) advantage.
- Small Qiskit simulations cannot establish quantum advantage or change a Ramsey bound.

## Important reviewer corrections

The external reviewer twice made claims that were later retracted:

1. It first recommended a universal \(\Omega(R\sqrt d)\) barrier; explicit repeated-flaw and multi-marked counterexamples refuted it.
2. It later inferred \(\Theta(1)\) dirty violations from \(dp\le1/e\) along adaptive trajectories; the exact conditional formula and the all-red counterexample refuted that inference.

The final conclusions incorporate the corrections, not the retracted claims.

