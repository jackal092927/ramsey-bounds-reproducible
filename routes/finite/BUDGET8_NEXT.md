# Budget-eight exclusion for the non-star R(3,13) seed

Date: **2026-08-12**

## Outcome

The former budget-eight `TIME_LIMIT` for
`r3_13_n61_nonstar_k11.txt` is now closed:

```text
status = UNSAT
```

More precisely, let $G$ be that fixed 61-vertex input.  There is no graph $H$
on the same labeled vertices such that

1. $H$ is triangle-free;
2. $H$ has no independent set of size 13;
3. at most eight edges of $G$ are absent from $H$; and
4. arbitrary nonedges of $G$ may be added to $H$.

Thus every successful graph in this fixed-seed edit family would have to
delete **at least nine** input edges.  This is a new exact local exclusion
radius.  It is not a new global bound on $R(3,13)$, and it does not prove that
a budget-nine completion exists.

In the proof-writer classification, this candidate-specific computer-assisted
claim is

```text
PROVABLE AS STATED
```

The remaining trust boundary is explicit: the structural/formula encoding and
the DRAT checker implementation.  Both SAT engines agreed, and all three
Glucose proof traces passed an independently invoked DRAT checker.

## Why the old run stalled

The earlier add-only CaDiCaL CEGAR run installed one independent-set cut per
model.  It reached 406 models and the wall limit after 69.259 seconds.  That
record was correctly labeled `TIME_LIMIT`; it proved no budget-eight
exclusion.

The decisive change is to branch first on the input triangles and then preload
the complete independent-set bank forced by each branch.  Every branch becomes
UNSAT before any new lazy cut is needed.

## Exact structural decomposition

The input has the eleven triangles

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

The first ten contain hub edge $(28,60)$.  Their third vertices are all
different.  If the hub were retained, each triangle would require deletion of
one edge from its own spoke pair

$$
\{(28,v),(60,v)\},
$$

and the ten spoke pairs are pairwise disjoint.  This needs at least ten input
edge deletions, exceeding budget eight.  Therefore every budget-eight solution
must delete $(28,60)$.

After that deletion, the only surviving input triangle is $(37,46,60)$.
Adding edges cannot destroy it, so at least one of

$$
(37,46),\qquad(37,60),\qquad(46,60)
$$

must also be deleted.  These are three exhaustive, possibly overlapping
branches.  Each branch has two fixed deletions and an at-most-six residual
deletion budget.

## Why the preloaded $I_{13}$ clauses are sound

For a branch $B$, let $G_B$ be the input graph after its two fixed deletions.
All independent 13-sets of $G_B$ were enumerated exactly.  For every such set
$S$, the formula includes

$$
\bigvee_{\{u,v\}\in\binom S2} x_{uv},
$$

where $x_{uv}$ says that $(u,v)$ is an edge of the final graph.

This is a necessary condition for every valid completion: if all variables in
the clause were false, $S$ would remain an independent 13-set.  Further input
edge deletions cannot invalidate this necessity.  Arbitrary additions are
represented by the unconstrained variables for every original nonedge.

These preloaded clauses do not need to enumerate independent sets created by
later deletions.  Consequently the branch CNF is a **relaxation** of the full
Ramsey search.  UNSAT of that relaxation is sufficient to exclude the full
branch.  This direction is important: no ungenerated lazy cut is being treated
as if it were present.

An independently written reverse-order bitset enumerator produced exactly the
same set of masks in all three branches, not merely the same counts.

## Exact branch formulas

Every branch uses:

- 1,830 Boolean edge variables, one for every pair on 61 vertices;
- all 35,990 triangle clauses;
- two fixed negative edge units;
- a sequential-counter encoding of at most six deletions among the other 361
  input edges: 2,130 auxiliaries and 4,609 clauses;
- the complete branch-specific $I_{13}$ bank.

| second fixed deletion | all fixed-base $I_{13}$ | containing both 28 and 60 | total CNF clauses |
|---|---:|---:|---:|
| $(37,46)$ | 17,690 | 15,985 | 58,291 |
| $(37,60)$ | 18,117 | 15,985 | 58,718 |
| $(46,60)$ | 17,913 | 17,912 | 58,514 |

The $I_{13}$ banks were enumerated in 0.36--0.38 seconds each.  Each stored
mask was also checked to contain no undeleted input edge; within such a mask,
the only possible input edges are among the two branch-fixed deletions.

## Solver and proof results

Glucose 4.2 ran persistently in interruptible conflict slices, under a hard
30-second branch wall limit and a 200,000-conflict global branch limit.
CaDiCaL 1.9.5 was independently run on the identical frozen CNF in a child
process with a 30-second parent-enforced kill limit.

| branch | Glucose status | conflicts | lazy cuts | CaDiCaL status | DRAT check |
|---:|---|---:|---:|---|---|
| 0: delete $(37,46)$ | `UNSAT` | 18,516 | 0 | `UNSAT` | `VERIFIED` |
| 1: delete $(37,60)$ | `UNSAT` | 14,381 | 0 | `UNSAT` | `VERIFIED` |
| 2: delete $(46,60)$ | `UNSAT` | 18,181 | 0 | `UNSAT` | `VERIFIED` |

The absence of lazy cuts is stronger than a completed CEGAR loop: the
necessary fixed-base relaxation itself is inconsistent.

Glucose emitted a DRAT trace for each terminal result.  The checker was built
from the official `marijnheule/drat-trim` repository at commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; the local checker binary has
SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
All three checks returned `s VERIFIED`:

| branch | proof lines | core input clauses | core lemmas | resolution steps |
|---:|---:|---:|---:|---:|
| 0 | 37,840 | 6,687 | 10,556 | 2,835,698 |
| 1 | 29,951 | 6,266 | 10,100 | 3,030,945 |
| 2 | 35,954 | 6,586 | 10,821 | 3,413,641 |

The canonical finite-route unit suite also passes 13/13 tests, including
complete small-graph checks of the SAT encodings, clique enumerator, fixed
deletion semantics, triangle transversal, and solver-limit labeling.

## Proof conclusion

Take any putative completion with at most eight input-edge deletions.  The
ten disjoint hub spoke pairs force deletion of $(28,60)$.  Triangle
$(37,46,60)$ then places the completion in at least one of the three branch
formulas.  It satisfies all triangle clauses, the residual-six deletion
counter, the fixed units, and every preloaded necessary $I_{13}$ clause.
However, each such CNF has a checked UNSAT proof.  This contradiction excludes
the completion.  Therefore the fixed-seed edit family has deletion lower bound
nine. $\square$

## Frozen artifacts

```text
45fbab7f36127a038e9cb7e7ef2a9859aca5e7054d33fbf820d1142b2d79056a  budget8_next.py
8e4e9406d83b65ee175ba3b42ac8792812e7d416876bd1a86f0d8227bd01c04b  budget8_next.json

071f590e826105df2779c0f86e0de357b76485922ac2b34434d55862ad6d8cc5  budget8_next_branch_0.cnf.gz
bf44a9e09013a31b95ebe5b17c2b7b3af256d7c49a737216d7f311d3591ea4f4  budget8_next_branch_0.drat.gz

009547e3e491820096cfa01f8c11ee9fa1a9436c7f65572aece10fdc6879d4f3  budget8_next_branch_1.cnf.gz
7c3885b82e8b3a9ac57794a933cfff6d4513217776602a58f434952c5ce3bc6b  budget8_next_branch_1.drat.gz

88e40bfb81560d1cdd6651d429bfdf7c2969c8977ae6073cc84221c2f52e5143  budget8_next_branch_2.cnf.gz
678986f3eb30bee7595be68ce21af2a5448e708472acbfc15ae762fa9f6df4ee  budget8_next_branch_2.drat.gz
```

The gzip files are deterministic (`mtime=0`).  The JSON additionally records
the uncompressed DIMACS and DRAT hashes, exact formula sizes, solver statistics,
checker output, limits, enumeration hashes, and the full structural witness.

## Reproduction

From the repository root, with the finite-route environment installed:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/budget8_next.py \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --artifact-dir routes/finite \
  --json routes/finite/budget8_next.json \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-trim-source-commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

Without `--drat-trim`, the solver and CaDiCaL cross-replay still run, but the
JSON honestly records the proof check as `NOT_RUN`.

## Claim boundary and next step

- This excludes only the labeled edit family around the frozen non-star seed.
- It does not prove $R(3,13)\leq61$, $R(3,13)\geq62$, or any other global
  Ramsey-number improvement.
- It does not imply that a valid completion exists with nine deletions.
- The next open local question is budget nine.  Its structural master should
  again fix the hub, branch on the residual triangle, preload the corresponding
  $I_{13}$ banks, and then allow seven residual deletions.
