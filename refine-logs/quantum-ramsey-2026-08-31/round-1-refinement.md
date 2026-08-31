# Round 1 Refinement

## Problem Anchor

- **Bottom-line problem:** Design a quantum algorithm for constructing classical Ramsey lower-bound witnesses that has a rigorous asymptotic advantage over a clearly specified classical algorithmic model, while returning an ordinary graph that can be checked independently.
- **Must-solve bottleneck:** Existing quantum Ramsey work already maps the problem to adiabatic evolution, Hamiltonians, QUBO, quantum annealing, or generic quadratic search. A publishable contribution must exploit the implicit, highly dependent family of forbidden monochromatic cliques and prove an end-to-end complexity theorem that is not merely “apply Grover to all colorings.”
- **Non-goals:** The first paper will not claim a practical NISQ advantage, will not claim a new numerical Ramsey bound unless an independently checked witness is actually found, will not attempt both lower- and upper-bound certification, and will not invoke topology unless a spectral-gap or hitting-time theorem is proved.
- **Constraints:** ITCS 2027 abstract is due September 2, 2026 and the paper September 4, 2026. The current idea begins without a proved theorem. Any ITCS submission must be theorem-first and must include all oracle, state-access, reversible-computation, error, and output-verification costs. Small experiments may validate circuits and scaling proxies but cannot establish quantum advantage.
- **Success condition:** A formal algorithm and proof establish a nontrivial quantum query or gate-complexity improvement for an implicit Ramsey-construction problem relative to a natural classical oracle model, survive adversarial novelty and correctness review, and are supported by reproducible small-instance simulations. A new finite Ramsey witness is optional supporting evidence, not a prerequisite for the theoretical result.

## Anchor Check

- The original bottleneck remains a theorem-level quantum advantage for constructing Ramsey witnesses.
- The initial Moser--Tardos-plus-Grover target does not solve the bottleneck: in the symmetric LLL regime it simplifies to a generic square-root neighborhood scan.
- Reframing the theorem around implicit-event search is not drift; pretending that this would improve current Ramsey bounds would be drift.
- The current exact-seven search, upper-bound certification, QAOA, annealing, and topology-only interpretations are removed from this proposal.

## Simplicity Check

- **Dominant contribution after revision:** one walk-amortized or local-computation theorem for an implicit Ramsey flaw family.
- **Components removed:** finite exact-seven Route B, QAOA/annealing, generic backtracking, topology discussion, and a separate scheduling contribution.
- **No longer claimed:** the target \(\widetilde O(\sqrt m+R\sqrt d)\) bound is not paper-worthy by itself.
- **Smallest adequate route:** first make coherent data access and exact subset-state preparation explicit; then prove a quantum search bound that is strictly stronger than restarting Grover after every repair.

## Changes Made

1. Reframed Ramsey as the concrete implicit-event family, not as evidence that a new Ramsey bound is obtained.
2. Added an explicit zero-error certification barrier.
3. Elevated coherent access to the coloring and exact preparation of a uniform \(k\)-subset state to formal lemmas.
4. Replaced the generic Grover repair loop with one hard theorem target: reuse local-update structure through a quantum walk or a quantum local-computation algorithm.
5. Made the ITCS 2027 decision an immediate no-go rather than a conditional deadline gamble.

## Revised Proposal

# Quantum Local Search for Implicit Ramsey Flaws

## Technical problem

Let \(\mathcal A\) be the \(m=\binom nk\) monochromatic-\(K_k\) flaws in a two-coloring of \(K_n\). A flaw has probability \(p=2^{1-\binom{k}{2}}\) and dependency degree

\[
d=\sum_{j=2}^{k}\binom{k}{j}\binom{n-k}{k-j}-1.
\]

Classical local-lemma algorithms repair a currently violated flaw by resampling its edges. In an implicit instance, the expensive operation is locating a flaw without materializing all \(m\) events.

A direct quantum composition finds a violated dependency-neighbor in \(\widetilde O(\sqrt d)\) checks. If \(R\) repairs occur, this yields about \(\widetilde O(R\sqrt d)\) local checks, plus setup and termination. This is a baseline, not the proposed contribution.

## Main thesis

The paper exists only if local changes to the coloring can be reused coherently so that the total quantum cost is asymptotically below independent Grover searches, or if a matching lower bound shows that \(R\sqrt d\) is optimal in a natural flaw-oracle model.

The preferred positive route is a walk-amortized algorithm:

1. maintain a quantum-searchable representation of the currently dirty portion of the flaw-dependency graph;
2. update it after resampling only \(O(k^2)\) edge colors;
3. use a quantum walk whose setup, update, checking, spectral-gap, and marked-mass costs are all explicit;
4. measure one violated flaw, resample classically, and continue with a rigorously bounded rebuild/update cost.

No concrete exponent such as \(d^{1/3}\) is claimed until the walk and its spectral analysis are proved.

## Foundational lemmas required before the main theorem

### Lemma A: Coherent access without an uncounted full QRAM

Represent the coloring by an initial pseudorandom or limited-independence seed plus a sparse log/dictionary of resampled edge values. Specify a reversible lookup circuit for the latest value of an edge and charge its memory, gate, and ancilla costs. If this cannot beat scanning a full \(\Theta(n^2)\)-bit table, stop.

### Lemma B: Uniform \(k\)-subset preparation

Prepare

\[
\binom nk^{-1/2}\sum_{S\in\binom{[n]}k}|S\rangle
\]

without paying the \(k!/k^k\) acceptance loss of sampling ordered tuples. Use a reversible combinatorial-number-system unranking circuit or a proved Dicke-state construction, with explicit cleanup and approximation error.

### Lemma C: Certification barrier

In the black-box flaw model, exact certification that no flaw remains is exact OR on \(m\) bits and therefore requires \(\Omega(m)\) queries. Consequently:

- the quantum construction theorem must be bounded-error;
- a new mathematical Ramsey bound still requires an independently checked classical graph;
- “construction complexity” and “end-to-end certified-bound complexity” are different claims.

This barrier is a companion boundary theorem, not the main positive contribution.

## Main theorem gate

Proceed only if one of the following is proved:

1. **Walk-amortized upper bound:** a rigorously defined quantum walk gives total flaw-location cost \(o(R\sqrt d)\) on the Ramsey LLL family after all setup and update costs;
2. **Tight lower bound:** \(\Omega(R\sqrt d)\) quantum queries are necessary for a natural Ramsey/flaw-oracle family, making the simple algorithm optimal;
3. **Quantum local-computation result:** individual edge colors of one consistent implicit Ramsey coloring can be answered with a proved quantum advantage without materializing or globally certifying the whole graph.

If none of these gates closes, the project is not a new quantum algorithm paper.

## Access and error model

- The mutable coloring, flaw predicate, and resampling randomness are defined as reversible oracles with charged costs.
- Unknown marked-set size uses a bounded-error search procedure designed for that setting.
- Adaptive error is controlled by a high-probability repair bound or an anytime summable schedule \(\delta_i\), not by assuming the number of calls.
- Any walk state disturbed by measurement/resampling must be rebuilt or updated at a cost included in the theorem.

## Closest prior work that must be beaten

- Gaitan--Clark (2012), Bian et al. (2013), Wang (2016), and Pion--Mniszewski (2025) on direct quantum Ramsey optimization and annealing.
- Moser--Tardos and implicit/resampling-oracle LLL algorithms, including Harvey--Vondrak.
- Montanaro quantum backtracking and Chakrabarti et al. quantum branch-and-cut.
- Ambainis variable-time search and quantum local search for SAT.
- Fixed-subgraph quantum detection and modern exact-exponential quantum graph algorithms.

The novelty statement cannot be “we apply one of these to Ramsey.” It must identify the new walk, lower bound, or local-computation theorem.

## Minimal validation

Experiments begin only after a theorem candidate exists.

1. Exhaustively verify the reversible monochromatic-clique oracle and exact \(k\)-subset state for \(n\le 7\).
2. Compare oracle calls for classical scanning, repeated Grover, and the proposed walk on identical flaw trajectories.
3. Report logical qubits, ancillas, depth, and state-preparation/update costs; simulator wall-clock is never called quantum speedup.
4. Independently enumerate every returned small coloring.

## Venue and timeline

- **ITCS 2027:** no-go. There is no central theorem four days before the deadline.
- **Research horizon:** first prove Lemmas A--C; then allow 6--10 weeks for the main theorem gate.
- **Venue choice:** theory venue only if the main gate closes; otherwise publish neither a QAOA demo nor a generic Grover application under an ITCS framing.
