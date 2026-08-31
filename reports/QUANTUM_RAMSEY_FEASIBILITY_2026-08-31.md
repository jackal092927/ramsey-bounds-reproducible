# Quantum Algorithms for Ramsey Search: Feasibility and Adversarial Audit

Date: 2026-08-31

## Later addendum: a non-LLL route survived review

The executive decision below records the state of the earlier
LLL/Grover/Johnson/topology exploration.  Later on the same date, a different
route produced a proved oracle-query theorem: capped quantum sampling of the
implicit candidate sets in the elementary Erdős--Szekeres recursion finds a
$K$-clique or $K$-vertex independent set in a promised valid graph on at
least $4^{K-1}$ vertices using

$$
O\!\left(2^K K\log(K/\eta)\right)
$$

edge queries.  A separate estimation-free, size-biased implementation gives
the cleaner bound
$O(2^K K^2\log K\log(1/\eta))$ and extends to any number of edge colours.
The theorem, proof, literature conflict, and nonclaims are in
[`QUANTUM_IMPLICIT_MAJORITY_CANDIDATE_2026-08-31.md`](QUANTUM_IMPLICIT_MAJORITY_CANDIDATE_2026-08-31.md).
It supersedes the historical statements below that there was no central
quantum theorem or possible ITCS contribution; it does not revive the LLL or
topology routes audited here and does not improve a numerical Ramsey bound.

## Executive decision

Quantum computation is a legitimate tool for Ramsey search, but the obvious paper is already occupied and the obvious speedups are not new. A useful project must prove a Ramsey-specific, end-to-end complexity theorem. A QUBO, QAOA, annealing, or generic Grover implementation with small-graph simulations is not enough.

Current status:

- **Longer-term direction:** conditional go for one tightly scoped diagnostic week.
- **ITCS 2027 at this earlier stage:** no-go before the later theorem above.
- **Numerical Ramsey bound:** unchanged. No new \(R(3,18)\) witness or exhaustive certificate has been produced.
- **Best quantum role:** discover a lower-bound witness and then verify it classically.
- **Upper-bound role:** heuristic guidance only unless the computation emits a classical exhaustive proof certificate.

## 1. Three different tasks

Let an edge coloring \(x\) be valid for \(R(s,t)\) at order \(n\) if it contains neither a red \(K_s\) nor a blue \(K_t\).

### 1.1 Verify a proposed coloring

The input graph is already known. A quantum routine may search for a violating clique, but a finite Ramsey theorem should still use a deterministic classical checker. Faster quantum counterexample search does not certify that no counterexample exists.

### 1.2 Construct a lower-bound witness

This is the natural quantum target. If a quantum algorithm outputs a classical coloring of \(K_n\), an ordinary checker can establish that it has no forbidden monochromatic clique. The discovery may be probabilistic; the mathematical certificate is the graph itself.

For the present project, a triangle-free 100-vertex graph with independence number below 18 would imply

\[
R(3,18)\ge 101.
\]

### 1.3 Prove an upper bound or nonexistence result

A bounded-error quantum run that does not find a graph is not a proof of nonexistence. An upper-bound improvement still requires an independently checkable exhaustive object, such as a proof-producing SAT certificate or a new mathematical argument.

## 2. Prior art that rules out the naive paper

The phrase “quantum algorithm for Ramsey numbers” is not new.

- [Gaitan and Clark (2012)](https://arxiv.org/abs/1103.1345) map Ramsey-number computation to adiabatic quantum optimization and simulate \(R(3,3)\) and \(R(2,s)\).
- [Bian et al. (2013)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.111.130505) experimentally determine small Ramsey instances on early D-Wave hardware.
- [Wang (2016)](https://arxiv.org/abs/1510.01884) gives a quantum Ramsey search and claims a quadratic search improvement.
- [Pion and Mniszewski (2025)](https://arxiv.org/abs/2311.04405) explicitly target Ramsey bounds with QUBO order reduction and quantum annealing. Their experiments document severe variable inflation and performance below classical simulated annealing.
- [Montanaro's quantum backtracking](https://arxiv.org/abs/1509.02374) and later quantum branch-and-cut methods already give generic near-quadratic improvements for static classical search trees.
- [Lee, Magniez, and Santha](https://arxiv.org/abs/1109.5135) and subsequent work already give quantum query algorithms for fixed-subgraph detection.

Consequently, none of the following is a defensible novelty claim:

1. encode the Ramsey objective as a Hamiltonian or QUBO;
2. apply QAOA or quantum annealing to \(R(3,3)\) or another small instance;
3. Grover-search all graphs or all deletion supports;
4. substitute a Ramsey backtracking tree into a generic quantum-backtracking theorem;
5. call a solution-space graph “topological” without proving its spectral properties.

## 3. Resource reality for the present \(R(3,18)\) gap

A global 100-vertex graph has

\[
\binom{100}{2}=4950
\]

edge variables. Black-box amplitude amplification over all graphs has worst-case scale \(2^{2475}\) oracle calls, before implementing the expensive validity oracle.

The current exact-seven branch is smaller but still not a direct quantum experiment. After the proved classical filters, it has

\[
52{,}484{,}488{,}743{,}693
\]

remaining deletion supports. Its square root is about \(7.24\times10^6\), but each amplitude-amplification step would require a coherent reversible completion/SAT oracle. Treating one classical solver call as a unit-cost quantum oracle would hide the dominant cost.

Small state-vector simulations can validate circuit logic; they cannot simulate the \(R(3,18)\) search or establish a practical speedup.

## 4. Candidate route: quantum flaw repair

Consider a random red/blue coloring of \(K_n\). The bad events are monochromatic \(K_k\)'s. There are

\[
m=\binom nk
\]

events, each with probability

\[
p=2^{1-\binom k2}.
\]

Two events are dependent when their vertex sets share at least two vertices. If \(S\) is a resampled \(k\)-set, define the dirty set, including \(S\), by

\[
\Gamma^+(S)=
\left\{T\in\binom{[n]}k:|T\cap S|\ge2\right\}.
\]

Its size is

\[
D(n,k)=
\sum_{j=2}^{k}\binom{k}{j}\binom{n-k}{k-j},
\]

and the usual dependency degree is \(d=D-1\).

Searching an unstructured dirty set for one violation costs \(\widetilde O(\sqrt D)\). This is only Grover inside Moser--Tardos, not a new algorithm. Moreover, a rigorous implementation must deal with old violations that persist outside the newest dirty set.

A clean bounded-error baseline maintains, with total success probability at least \(1-\delta\), a duplicate-free queue

\[
Q_i=M(x_i),
\]

where \(M(x_i)\) is the complete set of flaws violated by the current coloring. If \(S_i\in Q_i\) is resampled, the correct eager update is

\[
Q_{i+1}
=
\bigl(Q_i\setminus\Gamma^+(S_i)\bigr)
\cup
\bigl(M(x_{i+1})\cap\Gamma^+(S_i)\bigr).
\]

If \(Z_0=|M(x_0)|\), \(Z_i=|M(x_{i+1})\cap\Gamma^+(S_i)|\), and one coherent flaw test costs \(q\), its bounded-error predicate-query cost is

\[
\widetilde O\!\left(
q\left[
\sqrt{m(Z_0+1)}
+\sum_i\sqrt{D(Z_i+1)}
\right]\right).
\]

The second term enumerates all marked items. The smaller expression \(\sqrt{D/Z_i}\) finds only one mark and is not enough to preserve the queue invariant.

This is not yet an end-to-end gate bound. If

\[
A_i=|Q_i\cap\Gamma^+(S_i)|,\qquad b=\binom k2,
\]

then an explicit edge-to-queued-flaw incidence index adds work on the order of

\[
O\!\left(
b\left[Z_0+\sum_i(A_i+Z_i)+R\right]
\right)
\]

and corresponding memory. Quantum enumeration also needs a charged coherent membership structure for already found flaws. Exact zero-error absence in the flaw-oracle model costs \(m\) global queries; for a new Ramsey bound, the final graph is instead checked deterministically by the independent classical verifier.

This queue model is a baseline, not a proved best algorithm.

## 5. Why cross-step coherent walk reuse currently fails

A repair step must:

1. find a violated \(k\)-set;
2. measure and output its classical name;
3. resample its edges with classical randomness;
4. continue on a changed coloring.

Measuring the walk-position register collapses the coherent state that would support amortization. Rebuilding the state every round can erase the gain. Running all repairs coherently instead makes the coloring and repair history entangled and requires a new quantum-process analysis.

An append-only “latest update wins” log is also history-dependent: two update sequences reaching the same coloring have distinct physical encodings and cannot interfere as one walk state. A valid quantum walk needs a canonical history-independent representation, whose update and lookup costs must be charged.

These facts obstruct the proposed walk; they are not a lower bound against every possible quantum algorithm.

## 6. Why the within-step Johnson-walk gain disappears

For \(k^2=o(n)\), the dominant dirty events share exactly two vertices with the repaired set:

\[
D(n,k)=
\left(1+O(k^2/n)\right)
\binom{k}{2}\binom{n-k}{k-2}.
\]

Let \(N=n-k\), \(\ell=k-2\), and \(h=\binom{k}{2}\). A tempting walk state chooses a pair \(e\in\binom S2\) and an \(r\)-subset \(W\subseteq V\setminus S\). It is marked when \(W\) contains an \(\ell\)-set completing \(e\) to a monochromatic \(K_k\).

If markedness were free, optimizing \(r\) would produce an impressive query exponent. Markedness is not free: it is itself a search for a monochromatic completion among \(\binom r\ell\) subsets. Direct quantum search costs

\[
\widetilde O\!\left(
\ell\sqrt{\binom r\ell}
\right).
\]

Substituting this into the walk bound restores \(\widetilde O(\ell\sqrt D)\), the direct-Grover scale.

In the diagonal Ramsey regime \(k=\Theta(\log n)\), the query-only optimum has \(r=\Theta(n)\). It reads a constant fraction of all edges and then treats finding a \(K_{\Theta(\log n)}\) inside the cache as free internal computation. The apparent advantage is a query-model artifact, not an honest time/gate speedup.

## 7. Why the tempting universal lower bound is false

The converse claim, “every \(R\)-repair algorithm requires \(\Omega(R\sqrt d)\) queries,” is false without strong independence promises.

- If the same unique flaw \(J\) remains violated in every round, find it once and reuse it. The cost is \(O(\sqrt d+R)\).
- If many flaws are valid outputs and are removed one by one, quantum enumeration can cost
  \[
  \sum_{s=1}^{R}O\!\left(\sqrt{d/s}\right)
  =O(\sqrt{dR}).
  \]

An \(\Omega(R\sqrt d)\) theorem can be proved for \(R\) independent one-hot search blocks by existing strong direct-product results. That artificial model assumes away the shared-edge correlations that make Ramsey repair interesting, so it is neither a Ramsey theorem nor a new contribution.

## 8. Exact conditional resampling identity

Fix the current coloring \(x\) and a violated \(k\)-set \(S\). Resample every edge inside \(S\) independently and uniformly.

For \(T\ne S\), let \(j=|T\cap S|\ge2\). Exactly \(\binom j2\) edges of \(T\) are resampled. Call \(T\) compatible with \((x,S)\) when all unchanged edges of \(T\) have one common color. Then

\[
\Pr[T\text{ is monochromatic after resampling}\mid x,S]
=
\begin{cases}
2^{-\binom j2}, & T\text{ is compatible},\\
0, & T\text{ is incompatible}.
\end{cases}
\]

For \(T=S\), the probability is \(p\). If \(C_j(x,S)\) counts compatible \(T\ne S\) with \(|T\cap S|=j\), then the exact conditional expectation of the number \(Z\) of dirty violations is

\[
\boxed{
\mathbb E[Z\mid x,S]
=
p+\sum_{j=2}^{k-1}
C_j(x,S)2^{-\binom j2}.
}
\]

No independence between different \(T\)'s is needed; this follows from linearity of expectation.

This identity shows why the symmetric LLL condition cannot be substituted for trajectory analysis. The inequality \(e(d+1)p\le1\) controls the original product measure, not every adaptive history.

### Explicit counterexample

Take \(n=10\), \(k=6\), and the all-red coloring. Then

\[
p=2^{-14},\qquad d=209,\qquad e(d+1)p\approx0.03484<1.
\]

Nevertheless, after resampling any red \(K_6\),

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

Thus \(dp\approx0.01276\) does not give a pointwise bound over all LLL-admissible coloring states. The example is an exponentially rare initial state and does not establish typical Moser--Tardos trajectory behavior. It does show that any uniform complexity proof assuming “about \(dp\) dirty violations after every resampling” has a real gap.

## 9. Exact topology kill test

Define \(\mathcal R_n\) as the reconfiguration graph whose states are red/blue colorings of \(K_n\) with no monochromatic triangle, with single-edge recoloring moves that remain valid.

Exact enumeration gives:

| \(n\) | valid colorings | components | reconfiguration edges |
|---:|---:|---:|---:|
| 3 | 6 | 1 | 6 |
| 4 | 18 | 1 | 24 |
| 5 | 12 | 12 | 0 |
| 6 | 0 | 0 | 0 |

For \(n=5\), every valid coloring is a red \(C_5\) with a blue complementary \(C_5\). Recoloring any edge adds a chord to the opposite-color 5-cycle and creates a monochromatic triangle. Thus every state is isolated; distinct valid states differ on at least four edges.

This kills a quantum walk confined to valid colorings with single-edge moves. It does not kill walks through invalid states, larger moves, or flaw-space algorithms.

## 10. Standard batch overlap is also capped

For a valid resampling batch \(B\), let

\[
U(B)=\bigcup_{S\in B}\Gamma^+(S)
\]

and define its neighborhood-overlap factor

\[
g(B)=\frac{|B|D}{|U(B)|}.
\]

In the standard parallel Moser--Tardos schedule, distinct members of \(B\) are nondependent, so

\[
|S_i\cap S_j|\le1.
\]

Fix \(T\in U(B)\). For every \(S_i\) whose dirty neighborhood contains \(T\), choose a pair

\[
P_i\subseteq T\cap S_i.
\]

The pairs \(P_i\) are distinct: equality would put the same two vertices in \(S_i\cap S_j\). Since \(T\) has only \(\binom k2\) pairs, its coverage multiplicity is at most \(\binom k2\). Double counting gives

\[
|B|D
\le
\binom k2\,|U(B)|,
\qquad
\boxed{g(B)\le\binom k2}.
\]

Therefore standard valid batching can reduce candidate volume by at most \(O(k^2)\), and the ideal square-root search cost by at most \(O(k)\). For diagonal Ramsey parameters \(k=\Theta(\log n)\), this is at most a logarithmic factor, not a new polynomial quantum advantage. This ceiling does not prove that the factor is attainable; pairwise-overlap estimates suggest the typical factor is smaller.

The pairwise overlap can be counted exactly. Let

\[
A_r=
|\Gamma^+(S_1)\cap\Gamma^+(S_2)|,
\qquad
r=|S_1\cap S_2|,
\]

and put \(u=n-2k+r\). Partition \(S_1\cup S_2\) into its intersection and the two exclusive parts. Then

\[
\begin{aligned}
A_r
={}&
\sum_{a=0}^{r}
\sum_{b=0}^{k-r}
\sum_{c=0}^{k-r}
\mathbf 1[
a+b\ge2,\,
a+c\ge2,\,
a+b+c\le k
]\\
&\qquad\cdot
\binom ra
\binom{k-r}b
\binom{k-r}c
\binom u{k-a-b-c}.
\end{aligned}
\]

When \(n\gg k^3\),

\[
D=
\binom k2\binom{n-k}{k-2}
\left(1+O(k^2/n)\right),
\]

where the multiplicative error applies to the whole leading term, and the overlap fractions satisfy

\[
\frac{A_0}{D}
\sim\frac{k^4}{2n^2},
\qquad
\frac{A_1}{D}
\sim\frac{2k}{n},
\qquad
\frac{A_2}{D}
\sim\frac{2}{k^2}.
\]

For the diagonal LLL scale \(n\asymp k2^{k/2}\), all three fractions tend to zero. In particular, any batch of size polynomial in \(k\) has \(g(B)=1+o(1)\) under the valid pairwise-nondependent condition. Very large, highly structured designs can approach the \(O(k^2)\) ceiling, so a uniform constant bound would be false; even the sharp ceiling yields only an \(O(k)\) square-root saving.

Obtaining substantially larger \(g\) would require batching dependent flaws that share at least two vertices. Standard Moser--Tardos correctness does not permit that for free; it would require a new cluster-resampling algorithm and proof. That is a new classical/probabilistic mechanism, not a remaining implementation detail of the current quantum proposal.

The correct disposition is to stop the present LLL+Grover/Johnson/batching program. The conditional identity and the overlap cap are rigorous scoped negative results. They do not settle non-LLL quantum Ramsey algorithms.

## 11. Reproducible finite checks

The topology scan is reproduced by:

~~~bash
python3 experiments/quantum_ramsey/reconfiguration_scan.py \
  --self-check --min-n 3 --max-n 6
~~~

The exact conditional-expectation counterexample is reproduced by:

~~~bash
python3 experiments/quantum_ramsey/mt_dirty_expectation.py \
  --self-check --n 10 --k 6
~~~

Both scripts use exhaustive finite computation and Python's exact rational arithmetic where relevant. They are diagnostics, not quantum simulations.

No Qiskit circuit is included. Reproducing an already known \(R(3,3)\) Grover/QAOA oracle would not test the missing mathematical mechanism.

## 12. Submission decision

[ITCS 2027](https://itcs-conf.org/) requires the abstract by September 2, 2026 at 4:59pm PDT and the full paper by September 4 at 4:59pm PDT. The call asks for clear proofs of central claims and a clear account of significance and innovation in the first ten pages.

No current candidate meets that standard. Submitting a QAOA/Grover demo would collide with prior work; submitting the overlap hypothesis would submit a conjecture. The correct decision is not to submit this direction to ITCS 2027.

## Final assessment

The user's intuition is directionally right: Ramsey construction is a structured combinatorial search problem for which quantum algorithms may eventually yield rigorous benefits. The useful conclusion is narrower:

- quantum discovery plus classical certification is a clean lower-bound workflow;
- generic quantum search gives only an already-known quadratic improvement;
- topology matters only through a proved transition structure and spectral bound;
- the present walk and universal-lower-bound proposals fail adversarial scrutiny;
- the exact conditional identity and the \(n=10,k=6\) counterexample close a real correctness gap;
- standard valid-batch overlap is capped by \(g(B)\le\binom k2\), so it cannot provide a polynomial improvement;
- at the end of this LLL/topology route alone, no numerical Ramsey bound or
  publishable quantum theorem had been obtained; the later implicit-set
  theorem in the addendum changes the second conclusion but not the first.

The present LLL-based quantum-advantage program should be stopped. Broader, non-LLL quantum Ramsey research remains logically open, but it needs a genuinely new Ramsey-specific structural theorem before it becomes an active paper project.
