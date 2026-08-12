# Budget-nine exclusion for the non-star R(3,13) seed

Date: **2026-08-12**

## Outcome

For the fixed input
`r3_13_n61_nonstar_k11.txt`, the complete edit search with arbitrary
edge additions and at most nine input-edge deletions is

```text
UNSAT_PROOF_VERIFIED
```

Equivalently, if $G$ denotes this labeled 61-vertex seed, there is no graph
$H$ on the same vertex set such that

1. $H$ is triangle-free;
2. $H$ has no independent set of size 13;
3. at most nine edges of $G$ are absent from $H$; and
4. arbitrary nonedges of $G$ may be present in $H$.

Thus any successful completion in this fixed-seed edit family would need at
least **ten** input-edge deletions.  This advances the proof-carrying local
radius from eight to nine.  It is not a global improvement of $R(3,13)$ and
does not establish that a ten-deletion completion exists.

All three exhaustive branch relaxations were UNSAT in Glucose 4.2 and
CaDiCaL 1.9.5.  Each frozen Glucose trace was independently accepted by the
official `drat-trim` checker.  No bounded or timed-out result was promoted to
UNSAT.

## Structural reduction

The eleven input triangles are

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

The first ten contain hub edge $(28,60)$, and their ten remaining vertices
are distinct.  If the hub were retained, each triangle would require a
deletion from its own spoke pair

$$
\{(28,v),(60,v)\}.
$$

Those ten pairs are edge-disjoint, so retaining the hub costs at least ten
input-edge deletions.  Budget nine therefore still forces deletion of
$(28,60)$.

After deleting the hub, the only surviving input triangle is
$(37,46,60)$.  Every completion must consequently delete at least one of

$$
(37,46),\qquad(37,60),\qquad(46,60).
$$

These yield three exhaustive, possibly overlapping branches.  Each fixes two
input-edge deletions and permits at most seven more among the other 361 input
edges.

## Exact branch relaxation

Each branch has one Boolean variable $x_{uv}$ for every pair of the 61
vertices.  It contains:

- all 35,990 clauses excluding triangles;
- two negative unit clauses for the fixed deletions;
- an exact sequential-counter encoding of at most seven further input-edge
  deletions, using 2,478 auxiliary variables and 5,303 clauses; and
- one edge-hitting clause for every independent 13-set of the graph obtained
  after exactly the two fixed deletions.

For a fixed-base independent set $S$, its clause is

$$
\bigvee_{\{u,v\}\in\binom S2}x_{uv}.
$$

This clause is necessary for every valid completion: at least one edge must
be added inside $S$.  Later deletions can expose additional independent sets,
but omitting their clauses only relaxes the search.  Therefore UNSAT of the
preloaded formula already excludes the full branch.  In fact, all three
branch relaxations were UNSAT before any lazy CEGAR cut was needed.

The independent-set banks and their hashes are identical to the corresponding
fixed bases in the already audited budget-eight run; only the residual
cardinality counter changes.

| second fixed deletion | preloaded $I_{13}$ | total clauses | variables |
|---|---:|---:|---:|
| $(37,46)$ | 17,690 | 58,985 | 4,308 |
| $(37,60)$ | 18,117 | 59,412 | 4,308 |
| $(46,60)$ | 17,913 | 59,208 | 4,308 |

## Solver and checked-proof results

Glucose ran persistently in interruptible 20,000-conflict slices, subject to
a 500,000-conflict and 180-second limit per branch.  CaDiCaL ran on each
identical frozen CNF in a separate process with a parent-enforced 180-second
wall limit.

| branch | Glucose | conflicts | lazy cuts | CaDiCaL | DRAT |
|---:|---|---:|---:|---|---|
| 0: $(37,46)$ | `UNSAT` | 54,568 | 0 | `UNSAT` | `VERIFIED` |
| 1: $(37,60)$ | `UNSAT` | 37,679 | 0 | `UNSAT` | `VERIFIED` |
| 2: $(46,60)$ | `UNSAT` | 54,095 | 0 | `UNSAT` | `VERIFIED` |

The checker was built from `marijnheule/drat-trim` commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`.  Its binary SHA-256 was
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
All three runs terminated with `s VERIFIED`.

| branch | DRAT lines | core input clauses | core lemmas | resolution steps |
|---:|---:|---:|---:|---:|
| 0 | 115,583 | 8,321 | 36,052 | 12,701,516 |
| 1 | 71,609 | 7,513 | 23,162 | 7,479,919 |
| 2 | 107,569 | 7,863 | 31,532 | 10,415,683 |

The complete run took 81.39 seconds on the recorded machine, including both
solvers and all proof checks.

## Formal conclusion

Let $H$ be a putative completion with at most nine input-edge deletions.
The ten edge-disjoint hub spoke pairs force $(28,60)$ to be absent.  The
remaining input triangle then forces $H$ into at least one of the three
branches above.  Its edge assignment satisfies that branch's triangle
clauses, fixed units, residual-seven counter, and every fixed-base
$I_{13}$ hitting clause.  But the corresponding CNF has a checked UNSAT
proof, a contradiction.  Hence no such $H$ exists. $\square$

## Frozen artifacts

```text
c8914fc26a2a74cf69da4393193b7112bbff9a0b7fb5341dd64655615bcb91f4  budget9_nonstar.py
6ebb81dfa2545c0015f1337943e3109dc6965f29741bb6ea70c4af201d036f4e  budget9_nonstar.json

1ff3f8e90860a10ee7e3bfab072ec5af74ac268e0e6e8efe9b21cb1e3aedf081  budget9_nonstar_branch_0.cnf.gz
2c47caa4cd9e508482711a7bb4f51873cd5dc2ec7c842795af87173b0f03a052  budget9_nonstar_branch_0.drat.gz

d67d588ff2abfbfc0c8c69e7a297c09e1871e09f94e2409813cd6f687166cf59  budget9_nonstar_branch_1.cnf.gz
5c884ee6087c207e53dc1f1f25f40f735ad90d7536378d9f45127855b1485f9c  budget9_nonstar_branch_1.drat.gz

ce3bbeb80395d370efcc7c20cf3f70e8e0f49b9f3f863cc9e959e5ce62664193  budget9_nonstar_branch_2.cnf.gz
ff48fccd97bdfbb8ae2a73492984e2ae8561d08b8746232ed12f3f92916a1760  budget9_nonstar_branch_2.drat.gz
```

The compressed artifacts are deterministic (`mtime=0`).  The JSON also pins
the uncompressed DIMACS and DRAT hashes, formula sizes, exact limits, solver
statistics, checker output, and structural witness.

## Reproduction

Build the checker from the pinned official source commit, then run from the
repository root:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/budget9_nonstar.py \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --artifact-dir routes/finite \
  --json routes/finite/budget9_nonstar.json \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-trim-source-commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

If the checker is omitted or rejects any trace, the script deliberately emits
`UNKNOWN_PROOF_UNCHECKED`, not a proof-carrying UNSAT conclusion.  Any branch
that reaches a wall/conflict limit produces `UNKNOWN_LIMIT` globally.

## Claim boundary and next structural frontier

- This excludes only the labeled edit family around the named seed.
- It does not prove $R(3,13)\ge62$ or any other global Ramsey-number bound.
- It does not imply existence with ten deletions.
- At budget ten the hub is no longer automatically forced.  The next exact
  search must cover both (i) hub-deleted branches with eight residual
  deletions and (ii) the hub-retained case.  In the latter, all ten spoke
  triangles consume the entire budget, and triangle $(37,46,60)$ forces the
  overlapping choice $(37,60)$; the other nine spoke pairs then give 512
  binary transversal branches before symmetry or shared-clause reduction.
