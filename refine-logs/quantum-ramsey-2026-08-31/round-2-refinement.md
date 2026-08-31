# Round 2 Refinement

## Problem Anchor

- **Bottom-line problem:** Design a quantum algorithm for constructing classical Ramsey lower-bound witnesses that has a rigorous asymptotic advantage over a clearly specified classical algorithmic model, while returning an ordinary graph that can be checked independently.
- **Must-solve bottleneck:** Existing quantum Ramsey work already maps the problem to adiabatic evolution, Hamiltonians, QUBO, quantum annealing, or generic quadratic search. A publishable contribution must exploit the implicit, highly dependent family of forbidden monochromatic cliques and prove an end-to-end complexity theorem that is not merely “apply Grover to all colorings.”
- **Non-goals:** No practical NISQ claim; no numerical Ramsey bound without a checked witness; no simultaneous lower- and upper-bound promise; no topology claim without a spectral theorem.
- **Constraints:** ITCS 2027 is days away, the direction begins with no theorem, and every oracle/state-access/gate/output-verification cost must be charged.
- **Success condition:** A Ramsey-specific quantum complexity theorem survives adversarial novelty and correctness review and returns a classically checkable graph.

## Anchor and Simplicity Check

The anchor is not rewritten as a generic quantum Lovász-local-lemma paper. The smallest honest project has one target: exploit correlations between successive locally updated Ramsey flaw searches. Stop if the result is only Grover, generic quantum backtracking, or a query bound with exponential free computation.

## Corrections from Round 2 Review

### Cross-step coherent reuse is not yet an algorithm

A repair must measure a classical flaw name and then resample classically. This collapses the proposed walk state. An append-only update log is history-dependent and cannot serve as a canonical quantum-walk data structure.

### The proposed universal lower bound is false

The claim that every execution with \(R\) repairs costs \(\Omega(R\sqrt d)\) has direct counterexamples.

- If every round has the same unique flaw, find it once and reuse it:
  \[
  O(\sqrt d+R).
  \]
- If \(R\) flaws are initially marked and removed one by one, quantum enumeration can cost
  \[
  \sum_{s=1}^{R}O\!\left(\sqrt{d/s}\right)
  =
  O(\sqrt{dR}).
  \]

The corrected independent-one-hot-block theorem is a standard direct-product result and is not Ramsey-specific.

### The within-step Johnson walk hides markedness

For a resampled \(k\)-set \(S\),

\[
D(n,k)=
\sum_{j=2}^{k}
\binom kj
\binom{n-k}{k-j}.
\]

When \(k^2=o(n)\),

\[
D(n,k)=
\binom k2
\binom{n-k}{k-2}
\left(1+O(k^2/n)\right).
\]

A Johnson walk over an \(r\)-vertex cache looks faster only if the cache's monochromatic-completion test is free. Directly searching that completion costs

\[
\widetilde O\!\left(
k\sqrt{\binom r{k-2}}
\right),
\]

which restores the direct-Grover scale. For \(k=\Theta(\log n)\), the query-only optimum reads \(\Theta(n^2)\) edges and hides an exponentially difficult clique search in free internal computation.

### The most obvious valid-state topology fails

The single-edge reconfiguration graph of triangle-avoiding colorings has 12 isolated states at \(n=5\). This kills that transition rule only; it does not rule out walks through invalid states or larger moves.

## Revised Proposal at This Round

### Dynamic correlated-flaw problem

The state is a classical edge coloring

\[
x_t\in\{0,1\}^{\binom n2}.
\]

An update changes a known set of at most \(\binom k2\) edges. The algorithm must find a newly affected monochromatic \(K_k\), while charging preprocessing, history-independent representation, coherent edge access, update, measurement, rebuild, and final verification.

### Theorem gate

Proceed only if a Ramsey-specific dynamic index or structural promise makes completion search genuinely cheaper than the best honestly costed restart algorithm in a regime including \(k=\Theta(\log n)\).

Possible sources were limited to:

1. a history-independent dynamic index of nearly monochromatic completions;
2. a proved promise on post-resampling colorings;
3. a Ramsey-specific reversible search-tree decomposition.

Generic Grover, Montanaro backtracking, and fixed-subgraph query algorithms are baselines.

### Proof-compatible output

A lower-bound discovery may be bounded-error, but it must output an ordinary graph that is verified deterministically. An upper-bound claim still requires a classical exhaustive certificate.

### Minimal validation

1. Exhaustively test the reversible oracle on \(n\le7\).
2. Compare restart, repeated Grover, and any proposed dynamic method on identical trajectories.
3. Report gates, ancillas, state preparation, update, and rebuild costs.
4. Never call simulator wall time a quantum advantage.

## Decision at This Round

- ITCS 2027: no-go.
- Johnson walk: rejected.
- Universal lower bound: rejected.
- Dynamic correlation question: retained for one more mathematical audit.
- Finite Ramsey bounds: unchanged.

