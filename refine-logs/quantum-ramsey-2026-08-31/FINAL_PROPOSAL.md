# Final Disposition: Quantum Ramsey Search After Adversarial Audit

## Bottom Line

The broad idea remains scientifically legitimate, but every concrete quantum-advantage mechanism examined in this cycle fails or is sharply capped. There is no ITCS 2027 paper and no new numerical Ramsey bound.

The present LLL+Grover/Johnson/batching program should stop. Non-LLL quantum Ramsey algorithms remain logically open, but they should not become an active paper project until a genuinely new Ramsey-specific structural theorem is identified before the quantum wrapper is designed.

## Problem Anchor

The desired result was a quantum algorithm that constructs a classical Ramsey lower-bound witness with a rigorous asymptotic advantage over a clear classical model, followed by independent classical verification.

The result obtained in this audit is different: two exact diagnostic lemmas and several no-go conclusions for proposed mechanisms. They must not be presented as the requested positive quantum speedup.

## Rejected Routes

1. Direct Hamiltonian, QUBO, QAOA, and quantum annealing collide with existing quantum Ramsey work.
2. Global Grover is an existing generic quadratic search and remains exponentially large.
3. Generic quantum backtracking is not novel without a Ramsey-specific tree or kernel theorem.
4. Cross-step coherent walks lose their proposed reusable state at measurement/resampling boundaries.
5. The within-step Johnson walk hides the monochromatic-completion problem in its markedness cost.
6. A universal \(\Omega(R\sqrt d)\) lower bound is false for correlated, repeated, or multi-marked flaws.
7. Valid-coloring, single-edge reconfiguration is already disconnected at the \(n=5\) triangle threshold.
8. Standard parallel-batch neighborhood overlap is capped too strongly to yield a polynomial advantage in \(n\).

## Exact Result 1: Conditional Dirty-Flaw Identity

Let \(x\) be the current coloring and \(S\) a violated \(k\)-set. Resample all edges inside \(S\) independently and uniformly. For \(T\ne S\), let \(j=|T\cap S|\ge2\). Call \(T\) compatible with \((x,S)\) if all unchanged edges of \(T\) have one common color.

Then

\[
\Pr[T\text{ monochromatic after resampling}\mid x,S]
=
\mathbf 1[T\text{ compatible}]
2^{-\binom j2}.
\]

For \(T=S\), the probability is \(p=2^{1-\binom k2}\). If \(C_j(x,S)\) counts compatible \(T\ne S\) with intersection size \(j\), then

\[
\boxed{
\mathbb E[Z\mid x,S]
=
p+\sum_{j=2}^{k-1}
C_j(x,S)2^{-\binom j2}.
}
\]

This is exact and uses no independence assumption among dirty flaws.

For the all-red state with \(n=10,k=6\),

\[
e(d+1)p\approx0.03484<1,
\]

yet

\[
\mathbb E[Z\mid x,S]
=
\frac{310145}{16384}
\approx18.92975.
\]

Thus the LLL condition does not give a pointwise \(O(dp)\) bound over all admissible coloring states. This is a worst-case/state-space counterexample, not a claim about typical trajectories.

## Exact Result 2: Standard-Batch Overlap Cap

Let

\[
\Gamma^+(S)=
\left\{T\in\binom{[n]}k:|T\cap S|\ge2\right\},
\qquad
D=|\Gamma^+(S)|.
\]

For a standard parallel Moser--Tardos batch \(B\), every two flaws are nondependent:

\[
|S_i\cap S_j|\le1.
\]

Define

\[
U(B)=\bigcup_{S\in B}\Gamma^+(S),
\qquad
g(B)=\frac{|B|D}{|U(B)|}.
\]

For a fixed \(T\in U(B)\), associate to every covering \(S_i\) a pair contained in \(T\cap S_i\). No pair of \(T\) can be used twice, because that would force two batch flaws to share at least two vertices. Hence every \(T\) is covered at most \(\binom k2\) times, and

\[
\boxed{
g(B)\le\binom k2.
}
\]

The ideal candidate-volume saving is therefore at most \(O(k^2)\), and a square-root search can save at most \(O(k)\). At \(k=\Theta(\log n)\), this is at most logarithmic in \(n\), not a polynomial quantum advantage.

The pairwise overlap has the exact form

\[
A_r=
\sum_{\substack{a,b,c\ge0\\
a+b\ge2,\ a+c\ge2}}
\binom ra
\binom{k-r}b
\binom{k-r}c
\binom{n-2k+r}{k-a-b-c},
\]

where \(A_r=|\Gamma^+(S_1)\cap\Gamma^+(S_2)|\) and \(r=|S_1\cap S_2|\), with out-of-range binomial coefficients interpreted as zero.

When \(n\gg k^3\),

\[
\frac{A_0}{D}\sim\frac{k^4}{2n^2},
\qquad
\frac{A_1}{D}\sim\frac{2k}{n},
\qquad
\frac{A_2}{D}\sim\frac{2}{k^2}.
\]

Thus moderate valid batches have \(g(B)=1+o(1)\) in the diagonal Ramsey--LLL regime. Extremely large Steiner-type designs can approach the \(O(k^2)\) ceiling, so a uniform constant bound would be false; even that ceiling yields only an \(O(k)\) ideal saving.

## Correct Bounded-Error Queue Baseline

Let \(M(x_i)\) be all flaws violated by coloring \(x_i\). With total failure probability at most \(\delta\), maintain

\[
Q_i=M(x_i).
\]

After resampling \(S_i\),

\[
Q_{i+1}
=
\bigl(Q_i\setminus\Gamma^+(S_i)\bigr)
\cup
\bigl(M(x_{i+1})\cap\Gamma^+(S_i)\bigr).
\]

If \(Z_0=|M(x_0)|\), \(Z_i=|M(x_{i+1})\cap\Gamma^+(S_i)|\), and a coherent flaw test costs \(q\), bounded-error enumeration uses

\[
\widetilde O\!\left(
q\left[
\sqrt{m(Z_0+1)}
+\sum_i\sqrt{D(Z_i+1)}
\right]\right)
\]

predicate queries.

This expression is not an end-to-end theorem. Put

\[
A_i=|Q_i\cap\Gamma^+(S_i)|,
\qquad
b=\binom k2.
\]

With an edge-to-queued-flaw incidence index, purging affected entries and inserting new ones adds work of order

\[
O\!\left(
b\left[
Z_0+\sum_i(A_i+Z_i)+R
\right]\right)
\]

and corresponding memory. Quantum enumeration also needs a charged coherent membership structure for already discovered flaws, plus reversible state access and an error schedule summing to \(\delta\).

Queue emptiness logically certifies termination only conditional on every bounded-error update succeeding. Exact zero-error absence requires linear flaw-oracle work; a new Ramsey bound is finalized by deterministic classical verification of the output graph.

## Reproducible Finite Diagnostics

The exact conditional counterexample is reproduced by:

~~~bash
python3 experiments/quantum_ramsey/mt_dirty_expectation.py \
  --self-check --n 10 --k 6
~~~

The valid-state topology boundary is reproduced by:

~~~bash
python3 experiments/quantum_ramsey/reconfiguration_scan.py \
  --self-check --min-n 3 --max-n 6
~~~

These are exact classical diagnostics, not quantum-speedup experiments.

## Claim Boundaries

What can be claimed now:

- the conditional resampling identity;
- the explicit \(n=10,k=6\) pointwise counterexample;
- the valid-batch overlap cap;
- the pairwise overlap formulas/asymptotics;
- the \(n=5\) valid-state reconfiguration obstruction;
- no ITCS 2027 submission is justified.

What cannot be claimed:

- a new quantum algorithm;
- a quantum advantage;
- a new finite Ramsey bound;
- a lower bound against all quantum Ramsey algorithms;
- typical-trajectory behavior from the all-red counterexample;
- a practical speedup from simulator wall time.

## Future Restart Rule

Reopen a quantum Ramsey project only after identifying one of the following independently of generic Grover:

1. a Ramsey-specific structural kernel or search-tree theorem;
2. a valid dependent-cluster resampling theorem with more than polylogarithmic benefit after all costs;
3. a non-LLL configuration-space walk with a proved spectral/effective-resistance bound;
4. a natural Ramsey instance family with a rigorous separation from a specified classical model.

Until then, effort should return to the existing exact-seven/classical Ramsey program, where the mathematical claim boundaries are already concrete.
