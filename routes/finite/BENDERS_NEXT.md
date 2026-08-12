# Higher-order shared-deficit cuts for the R(3,13) budget-9 basin

Date: 2026-08-12  
Frozen predecessor: `benders_budget9.json`  
Experiment verdict: **UNKNOWN at the explicit master conflict limit; no candidate and no new Ramsey bound**

## Claim

Let $H$ be the 61-vertex near-miss after deleting the already-forced hub edge
$(56,60)$.  Let $D\subseteq E(H)$ be the eight residual base edges deleted by
a hypothetical triangle-free repair.  For an original nonedge $f=\{u,v\}$,
define its local requirement set

$$
\mathcal R_f=
\bigl\{\{\{u,w\},\{v,w\}\}:w\in N_H(u)\cap N_H(v)\bigr\}.
$$

View each member of $\mathcal R_f$ as an edge of a graph whose vertices are
deletable edges of $H$.  For three candidate additions $f,g,h$, let

$$
Q(f,g,h)=\mathcal R_f\cup\mathcal R_g\cup\mathcal R_h.
$$

If the minimum vertex-cover number satisfies

$$
\tau\bigl(Q(f,g,h)\bigr)>8,
$$

then no feasible budget-9 repair can add all three edges.  Consequently the
master clause

$$
\neg y_f\lor\neg y_g\lor\neg y_h
$$

is valid.

## Status

**PROVABLE AS STATED.**

This status applies to the higher-order cut lemma.  It does not apply to the
existence or nonexistence of a 61-vertex $(3,13)$-graph.  The bounded experiment
below remains `UNKNOWN_MASTER_CONFLICT_LIMIT`.

## Assumptions

- The base graph $H$ is the named frozen near-miss with the forced hub removed.
- A repair may delete exactly eight further edges of $H$ and may add original
  nonedges other than the forced hub.
- The final graph is triangle-free.
- $y_f=1$ means candidate edge $f$ is selected in the master support.
- The predecessor's 24,832 conditional $I_{13}$ masks are imported only after
  checking its schema, input SHA-256, uniqueness, mask cardinality, and zero
  heuristic-UNKNOWN-no-good count.

## Notation

- $E(H)$: base edges after hub deletion.
- $D$: the residual set of exactly eight deleted base edges.
- $\mathcal R_f$: common-neighbor spoke-pair requirements for addition $f$.
- $Q(f,g,h)$: union of the three requirement graphs.
- $\tau(Q)$: minimum number of vertices meeting every edge of graph $Q$.
- $y_f$: master selector for addition $f$.

## Proof Strategy

First show that triangle-freeness makes $D$ a vertex cover of every selected
addition's requirement graph.  Taking a union then makes $D$ a vertex cover of
$Q(f,g,h)$.  If $\tau(Q)>8$, this contradicts $|D|=8$.  The implementation
decides $\tau(Q)\le8$ exactly by branching on the endpoints of an uncovered
edge; a greedy matching is used only for a valid lower-bound prune.

## Dependency Map

1. The ternary-cut lemma depends on the common-neighbor triangle condition.
2. The common-neighbor condition depends only on final triangle-freeness and
   on $f$ being added to $H-D$.
3. Exact cut classification depends on the vertex-cover branching recurrence.
4. The branching recurrence depends on the fact that every vertex cover of an
   edge contains at least one endpoint of that edge.
5. The matching prune depends on the standard inequality
   $\nu(Q)\le\tau(Q)$; the implementation uses the size of one explicitly
   constructed matching, which is at most $\nu(Q)$.

## Proof

**Step 1: one selected addition.**  Suppose $f=\{u,v\}$ is added.  Fix any
$w\in N_H(u)\cap N_H(v)$.  Both $\{u,w\}$ and $\{v,w\}$ are base edges.  If
neither belongs to $D$, then all three edges
$\{u,v\},\{u,w\},\{v,w\}$ occur in the final graph, forming a triangle.  Since
the final graph is triangle-free, at least one of $\{u,w\}$ and $\{v,w\}$ lies
in $D$.  Thus $D$ meets every member of $\mathcal R_f$.

**Step 2: three selected additions.**  If $f,g,h$ are all added, Step 1 applies
to each of them.  Hence $D$ meets every edge in
$\mathcal R_f\cup\mathcal R_g\cup\mathcal R_h=Q(f,g,h)$.  Therefore $D$ is a
vertex cover of $Q(f,g,h)$ and

$$
\tau\bigl(Q(f,g,h)\bigr)\le |D|=8.
$$

Taking the contrapositive, if $\tau(Q(f,g,h))>8$, the three additions cannot
all be selected.  This is exactly the clause
$\neg y_f\lor\neg y_g\lor\neg y_h$.  This proves the stated cut lemma. $\square$

**Step 3: exactness of the computational cover decision.**  Given a nonempty
requirement graph $Q$, select an edge $\{a,b\}$.  Every vertex cover contains
$a$ or $b$.  Therefore $Q$ has a cover of size at most $k$ if and only if at
least one of the following residual graphs has a cover of size at most $k-1$:

$$
Q-a,\qquad Q-b.
$$

The recursion stops with `true` when no requirement edge remains and `false`
when an edge remains at budget zero.  These cases and the recurrence prove the
decision by induction on $k+|E(Q)|$.  Before branching, the code constructs a
matching $M$.  Every cover contains at least one distinct endpoint contribution
for each edge of $M$, so $|M|>k$ safely returns `false`.  Memoization changes
only evaluation order, not the recurrence.

## Corrections or Missing Assumptions

None for the cut lemma.  The materialized cut family is deliberately not all
possible triples among 1,469 additions.  The coverage-based choice of 128
additions is a strength/compute heuristic; it does not affect the validity of
any generated clause and is not claimed complete.

## Open Risks

- Static ternary clauses are logically redundant with the full local
  eligibility constraints plus the exact deletion cardinality; their purpose
  is stronger propagation.  The present run does not prove that they improve
  wall-clock performance.
- No master model was reached, so this phase provides no information about the
  exact add-only fixed-deletion subproblems beyond preserving their encoding.
- An UNSAT result would exclude only this forced-hub budget-9 basin, not every
  possible 61-vertex construction.  The present result is not UNSAT.

## Small-instance oracle verification

The separate `test_benders_next.py` suite performs three checks before the
61-vertex experiment:

1. For every graph on six deletion variables and every budget from zero through
   six, the recursive vertex-cover result equals brute-force subset search.
2. A genuine ternary instance uses nine disjoint requirement edges split three
   per addition: every pair needs only six deletions, while all three need nine.
   The generator emits the ternary cut and no pair subsumes it.
3. All triples of matchings on four deletion variables are enumerated for
   budgets zero, one, and two.  Every emitted ternary no-good is checked by
   brute force to have no covering deletion set within the budget.

All three tests pass.  Together with the proof above, these tests guard both the
general recurrence and the cut-generation plumbing.

## Materialized higher-order cuts

Candidate additions are ranked by descending occurrence in the 25,685 seed
$I_{13}$ sets, then by individual requirement count and edge label.  The first
128 are selected.  The preprocessing limits are 400,000 examined triples and
30 seconds; the selected family contains only
$\binom{128}{3}=341{,}376$ triples, so it exhausts before either limit.

| classification | count |
|---|---:|
| Triples examined | 341,376 |
| Already subsumed by a pairwise incompatibility | 83,090 |
| Exactly coverable with at most eight deletions | 200,407 |
| Genuine ternary incompatibilities | **57,879** |
| Exact recursive/memoized states evaluated | 1,505,511 |
| Preprocessing time | 13.431 s |

The deterministic ternary-cut stream SHA-256 is
`09c7da87bb8fe89fddf509b5a58322433ae252a59686efe00b642f8148d64071`.
All 57,879 clauses are serialized in `benders_next.json`.

## Strictly bounded experiment

Canonical command from the repository root:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/benders_next.py \
  routes/finite/r3_13_n61_frozen_nearmiss_k11.txt \
  --d8-json routes/finite/r3_13_bounded_delete_8.json \
  --strict-cut-json routes/finite/benders_budget9.json \
  --higher-order-top-k 128 \
  --higher-order-max-triples 400000 \
  --higher-order-preprocess-seconds 30 \
  --max-conflicts 750000 --conflicts-per-call 5000 \
  --per-call-seconds 8 --max-seconds 180 \
  --max-iterations 1000 --cuts-per-iteration 4096 \
  --oracle-nodes 16000000 --oracle-seconds 8 \
  --sub-max-conflicts 100000 --sub-max-seconds 30 \
  --output routes/finite/r3_13_n61_benders_next_candidate.txt \
  --json routes/finite/benders_next.json
```

The master contains the exact residual-eight cardinality encoding, 3,893 local
eligibility clauses, 81,345 strict pairwise cuts, 24,832 imported strict
conditional $I_{13}$ cuts, and 57,879 new ternary cuts.

| progress measure | result |
|---|---:|
| Status | `UNKNOWN_MASTER_CONFLICT_LIMIT` |
| Candidate | none |
| All installed exclusions strict | `true` |
| Heuristic UNKNOWN no-goods | **0** |
| Master SAT models reached | 0 |
| Limited solver calls | 150 |
| Timer interruptions | 0 |
| Conflicts | 750,004 |
| Decisions | 2,008,596 |
| Propagations | 661,096,062 |
| Restarts | 4,049 |
| Formula/cut construction | 20.428 s |
| Total elapsed | 136.038 s |

MiniSat may finish a conflict-limited call a few conflicts beyond the requested
cumulative threshold; the next outer check stopped at 750,004.  Every call was
individually limited, and the global wall cap was not reached.

The solver produced no master model, so no independent-set separator or
fixed-deletion subproblem ran and no candidate file was written.  This absence
of a model before the conflict limit is **not** an UNSAT proof.

## Reproducibility

Pinned SHA-256 values after the formal run:

```text
frozen predecessor JSON   f5a60930b468795cfd1c0490e502ba6506cb60e1b0750f71db2eee4f3357b3c2
higher-order script       d360f3a3c2fc4216a9a415fca090c246fc4839e087042f22b1bf7b1427cbdf07
higher-order result       f069f5714bbceb4cbb69e0e1c4c2ca93c5bceb48486a6e95c49c937a2f7895e3
higher-order tests        376bfdfcc2756bd663269ce432bbae3ba4211aaf27155f4b2fec9454ebb6e9ae
```

The old `benders_budget9.json` was read as a frozen input and was not
overwritten.  `benders_next.json` records all limits, provenance hashes,
selected additions, exact classification counts, serialized ternary clauses,
solver statistics, and the zero heuristic-no-good count.

## Exact claim boundary

- The 57,879 serialized ternary clauses and the general ternary-cut lemma are
  strict mathematical results for this master encoding.
- `all_installed_exclusions_strict=true` means no approximate or UNKNOWN-derived
  exclusion entered the formula.  It does not change the terminal status.
- The experiment is `UNKNOWN_MASTER_CONFLICT_LIMIT`, not UNSAT.
- No graph was emitted, so the independent bitset checker had no candidate to
  accept or reject.
- Therefore this phase does not prove $R(3,13)\ge62$ and changes no global
  Ramsey-number bound.

