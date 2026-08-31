# Round 3 Refinement

## Problem Anchor

- **Bottom-line problem:** Design a quantum algorithm for constructing classical Ramsey lower-bound witnesses that has a rigorous asymptotic advantage over a clearly specified classical algorithmic model, while returning an ordinary graph that can be checked independently.
- **Must-solve bottleneck:** Existing quantum Ramsey work already maps the problem to adiabatic evolution, Hamiltonians, QUBO, quantum annealing, or generic quadratic search. A publishable contribution must exploit the implicit, highly dependent family of forbidden monochromatic cliques and prove an end-to-end complexity theorem that is not merely “apply Grover to all colorings.”
- **Non-goals:** The first paper will not claim a practical NISQ advantage, will not claim a new numerical Ramsey bound unless an independently checked witness is actually found, will not attempt both lower- and upper-bound certification, and will not invoke topology unless a spectral-gap or hitting-time theorem is proved.
- **Constraints:** ITCS 2027 abstract is due September 2, 2026 and the paper September 4, 2026. The current idea begins without a proved theorem. Any ITCS submission must be theorem-first and must include all oracle, state-access, reversible-computation, error, and output-verification costs. Small experiments may validate circuits and scaling proxies but cannot establish quantum advantage.
- **Success condition:** A formal algorithm and proof establish a nontrivial quantum query or gate-complexity improvement for an implicit Ramsey-construction problem relative to a natural classical oracle model, survive adversarial novelty and correctness review, and are supported by reproducible small-instance simulations. A new finite Ramsey witness is optional supporting evidence, not a prerequisite for the theoretical result.

## Anchor and Simplicity Check

The anchor remains a quantum algorithm for Ramsey witness construction. It is not rewritten as a generic quantum Lovász-local-lemma paper merely to rescue a route that no longer solves the user's problem.

Two proposed main results are rejected:

1. the Johnson walk, because its markedness cost cancels the apparent gain;
2. a universal \(\Omega(R\sqrt d)\) lower bound, because correlated or repeated flaws give direct counterexamples and the corrected independent-block statement is an existing direct-product theorem.

The remaining work is one diagnostic week, not a six-to-ten-week project and not an ITCS submission.

## Exact Conditional Resampling Identity

Let \(x\) be the current coloring, let \(S\) be the violated \(k\)-set being resampled, and resample every edge of \(K_S\) independently and uniformly.

For \(T\ne S\), let \(j=|T\cap S|\ge2\). Exactly \(\binom j2\) edges of \(T\) are resampled. Call \(T\) compatible with \((x,S)\) when all unchanged edges of \(T\) have one common color. Then

\[
\Pr[T\text{ is monochromatic after resampling}\mid x,S]
=
\begin{cases}
2^{-\binom j2}, & T\text{ compatible},\\
0, & T\text{ incompatible}.
\end{cases}
\]

For \(T=S\), the probability is

\[
p=2^{1-\binom k2}.
\]

If \(C_j(x,S)\) counts compatible \(T\ne S\) with \(|T\cap S|=j\), the exact conditional expected number \(Z\) of dirty violations is

\[
\mathbb E[Z\mid x,S]
=
p+\sum_{j=2}^{k-1}
C_j(x,S)2^{-\binom j2}.
\]

This uses only linearity of expectation; the dirty events need not be independent.

The LLL condition \(e(d+1)p\le1\) concerns the original product measure. It does not bound this expectation after conditioning on an arbitrary adaptive history.

### Explicit counterexample

For the all-red coloring with \(n=10\) and \(k=6\),

\[
p=2^{-14},\qquad d=209,\qquad e(d+1)p<1,
\]

but resampling any red \(K_6\) gives

\[
\begin{aligned}
\mathbb E[Z\mid x,S]
&=2^{-14}
+15\cdot2^{-1}
+80\cdot2^{-3}\\
&\quad+90\cdot2^{-6}
+24\cdot2^{-10}\\
&=\frac{310145}{16384}
\approx18.92975.
\end{aligned}
\]

Thus replacing the adaptive conditional distribution by \(dp\) creates a genuine gap in a quantum runtime proof.

## Honest Queue Baseline

A lazy algorithm must account for violations that remain outside the newest dirty neighborhood. A clean baseline maintains an exact queue.

Let

\[
m=\binom nk,\qquad
D=d+1=
\sum_{j=2}^{k}\binom{k}{j}\binom{n-k}{k-j}.
\]

If \(Z_0\) flaws are initially violated, quantum enumeration costs

\[
\widetilde O\!\left(
\sqrt{m\max(1,Z_0)}
\right).
\]

After resampling \(S_i\), re-evaluate \(\Gamma^+(S_i)\) and enumerate all \(Z_i\) violated members at cost

\[
\widetilde O\!\left(
\sqrt{D\max(1,Z_i)}
\right).
\]

The expression \(\sqrt{D/Z_i}\) finds only one mark and cannot maintain an exact queue. Queue updates, reversible access, error control, and final empty certification must also be charged.

This is a rigorous baseline model, not a lower bound.

## Live Overlap Hypothesis

For a valid resampling batch \(B\), define

\[
U(B)=\bigcup_{S\in B}\Gamma^+(S)
\]

and

\[
g(B)=\frac{|B|D}{|U(B)|}.
\]

If the neighborhoods are essentially disjoint, batch size cancels and multi-search remains at the direct square-root scale. If a valid schedule has an unbounded overlap factor \(g(B)\), its candidate volume may shrink enough to yield a \(\sqrt g\) saving.

This is the only live LLL-specific mechanism. It has two immediate risks:

- standard parallel Moser--Tardos batches mutually nondependent flaws, which may suppress useful overlap;
- batching adjacent, highly overlapping flaws requires a new resampling-correctness argument.

No asymptotic growth of \(g\) is currently proved.

## One-Week Kill Test

1. Measure \(C_j(x_i,S_i)\), \(Z_i\), and \(g(B_i)\) on genuine Ramsey resampling trajectories.
2. Separate product-measure behavior from history-conditioned behavior.
3. Prove combinatorial overlap bounds for schedules that are actually valid.
4. Compare against the exact-queue baseline with all marked-item enumeration and update costs.
5. Stop unless an unbounded overlap or another Ramsey-specific structural discount survives.

A theorem giving an end-to-end \(o(R\sqrt d)\) bound in a Ramsey-relevant regime keeps this LLL route alive. Constant overlap and product-scale compatibility kill it.

Neither outcome settles non-LLL quantum Ramsey algorithms.

## Topology Boundary

The valid-coloring, single-edge reconfiguration graph for the triangle problem has 12 isolated states at \(n=5\). Every valid coloring is a red \(C_5\) with a blue complementary \(C_5\), and recoloring any edge creates a monochromatic triangle.

This kills only a walk confined to valid states with single-edge moves. It says nothing about flaw-space walks, larger moves, or walks through invalid states.

## Minimal Validation

1. Reproduce the exact conditional expectation and the \(n=10,k=6\) counterexample with rational arithmetic.
2. Reproduce the \(n\le6\) reconfiguration counts by exhaustive enumeration.
3. Use small trajectory simulations only to formulate an overlap conjecture.
4. Require a proof for any asymptotic quantum claim.
5. Classically verify every graph emitted by any future discovery algorithm.

No Qiskit circuit is built before the overlap theorem gate. A small Grover/QAOA reproduction would not test the missing mechanism.

## Decision

- **ITCS 2027:** no-go.
- **Direct QUBO/QAOA/annealing:** abandon as a novelty route.
- **Current Johnson walk and universal lower bound:** rejected.
- **Overlap/conditional-trajectory diagnostic:** proceed for one week.
- **Longer project:** proceed only if the diagnostic exposes a precise, Ramsey-specific theorem.
- **Finite Ramsey bounds:** unchanged.

