# Complete budget-ten exclusion for the non-star $R(3,13)$ seed

Date: **2026-08-12**

## Claim

Let $G$ be the labeled 61-vertex graph in
`r3_13_n61_nonstar_k11.txt`.  There is no graph $H$ on the same vertex
set such that

1. $H$ is triangle-free;
2. $H$ has no independent set of size 13;
3. at most ten edges of $G$ are absent from $H$; and
4. arbitrary nonedges of $G$ may be present in $H$.

Equivalently, every successful completion in this fixed-seed edit family
would require at least **eleven** input-edge deletions.

## Status

```text
PROVABLE AS STATED
UNSAT_PROOF_VERIFIED
```

All four exhaustive branch relaxations were UNSAT in Glucose 4.2 and
CaDiCaL 1.9.5.  The four frozen Glucose traces were accepted by the pinned
official `drat-trim` checker.  No bounded or timed-out result was promoted to
UNSAT.

This is a local exclusion around one labeled seed.  It is not a global
improvement of $R(3,13)$ and it does not establish that an eleven-deletion
completion exists.

## Assumptions and notation

- $G$ is exactly the frozen 61-by-61 adjacency matrix whose SHA-256 is
  `2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b`.
- An input-edge deletion means an edge of $G$ that is absent from the final
  graph $H$.  Additions are not counted and are unrestricted.
- The hub edge is $h=(28,60)$.
- The only input triangle not containing $h$ is
  $T=(37,46,60)$.
- A branch CNF is allowed to omit independent 13-sets exposed only after
  additional deletions.  It is therefore a necessary-condition relaxation;
  checked UNSAT of that relaxation is sufficient for exclusion.

## Proof strategy and dependency map

1. Validate the eleven input triangles and split all completions according to
   whether $h$ is absent or present.
2. If $h$ is absent, split on which edge of $T$ is absent.  This gives three
   exhaustive, possibly overlapping branches.
3. If $h$ is present, use the ten pairwise edge-disjoint spoke pairs and the
   exact deletion budget to reduce all $2^9=512$ transversals to one merged
   CNF.
4. In every branch, encode all triangles, the residual deletion budget, fixed
   edge units, and every independent 13-set of the fixed-deletion base.
5. Check a DRAT refutation for every frozen CNF.  Exhaustiveness plus the four
   refutations proves the claim.

The only non-symbolic trust boundary is the formula/structural encoding, the
sequential-counter implementation, and the independently invoked DRAT checker.
CaDiCaL replay is corroborating evidence rather than a replacement for the
checked traces.

## Structural decomposition

The eleven input triangles are

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

### Case 1: the hub is absent

After deleting $h$, the sole surviving input triangle is $T$.  Every
triangle-free completion must therefore omit at least one of

$$
(37,46),\qquad (37,60),\qquad (46,60).
$$

Fixing $h$ and one displayed edge consumes two deletions and leaves a residual
budget of eight among the other 361 input edges.  These are branches 0, 1,
and 2 below.  A completion that omits multiple edges of $T$ may occur in more
than one branch, which does not affect exhaustiveness.

### Case 2: the hub is present

For each

$$
v\in\{19,22,24,27,29,32,34,37,48,58\},
$$

the input triangle $(28,v,60)$ forces at least one deletion from

$$
\{(28,v),(v,60)\}.
$$

These ten spoke pairs are pairwise edge-disjoint.  Retaining $h$ thus costs at
least ten input-edge deletions, so budget ten forces exactly one deletion in
every pair and permits no deletion elsewhere.  Of the three edges of $T$, the
only spoke edge is $(37,60)$.  Consequently $(37,60)$ is forced absent,
$(28,37)$ is retained, and the other nine spoke pairs make $2^9=512$
binary choices.

Branch 3 represents all 512 choices in one CNF: it fixes $(37,60)$ absent and
$h$ present, permits at most nine residual deletions, and includes every
triangle clause.  The nine other hub triangles force at least nine residual
spoke deletions, so the counter makes each of their pairs an exact one-of-two
choice and forbids any other deletion.  Thus the merged representation is
exact for the hub-present case; no transversal is sampled or omitted.

## Exact branch relaxation

There is one Boolean edge variable $x_{uv}$ for each of the
$\binom{61}{2}=1830$ vertex pairs.  Each branch contains:

- all $\binom{61}{3}=35{,}990$ clauses
  $\lnot x_{ab}\lor\lnot x_{ac}\lor\lnot x_{bc}$ excluding triangles;
- negative units for fixed deletions and, in branch 3, a positive unit for the
  retained hub;
- a sequential-counter encoding of the residual input-edge deletion budget;
  and
- one edge-hitting clause for every independent 13-set $S$ of the graph after
  exactly the fixed deletions,

$$
\bigvee_{\{u,v\}\in\binom S2}x_{uv}.
$$

The last clause is necessary for every valid completion because $H$ must add
or retain at least one edge inside $S$.  Further deletions can expose other
independent sets, but omitting their clauses only relaxes the formula.  All
four relaxed formulas were already UNSAT, so zero lazy cuts were needed.

| branch | case / fixed units | residual budget | variables | clauses | preloaded $I_{13}$ |
|---:|---|---:|---:|---:|---:|
| 0 | $h=0$, $(37,46)=0$ | 8 | 4,654 | 59,675 | 17,690 |
| 1 | $h=0$, $(37,60)=0$ | 8 | 4,654 | 60,102 | 18,117 |
| 2 | $h=0$, $(46,60)=0$ | 8 | 4,654 | 59,898 | 17,913 |
| 3 | $h=1$, $(37,60)=0$; all 512 transversals | 9 | 5,007 | 44,822 | 2,132 |

The three hub-absent independent-set banks have the same hashes as their
fixed bases in the earlier budget-nine proof.  The branch-3 bank has SHA-256
`846c46b160147aa185b7139168916c5551303cc2d34774636e9aec04e2f1be17`.

## Solver and checked-proof results

Glucose ran persistently in interruptible 20,000-conflict slices under a
3,000,000-conflict and 900-second limit per branch.  CaDiCaL ran in a separate
process with a parent-enforced 300-second wall limit.  Every solver completed
before its limit.

| branch | Glucose | conflicts | solve seconds | lazy cuts | CaDiCaL | DRAT |
|---:|---|---:|---:|---:|---|---|
| 0 | `UNSAT` | 210,556 | 34.900 | 0 | `UNSAT` | `VERIFIED` |
| 1 | `UNSAT` | 165,575 | 26.299 | 0 | `UNSAT` | `VERIFIED` |
| 2 | `UNSAT` | 260,394 | 44.912 | 0 | `UNSAT` | `VERIFIED` |
| 3 | `UNSAT` | 207 | 0.013 | 0 | `UNSAT` | `VERIFIED` |

The checker was built from `marijnheule/drat-trim` commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`.  Its binary SHA-256 was
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
All four checks terminated with `s VERIFIED`.

| branch | DRAT lines | core input clauses | core lemmas | resolution steps |
|---:|---:|---:|---:|---:|
| 0 | 410,743 | 9,663 | 146,804 | 53,816,381 |
| 1 | 332,352 | 9,026 | 122,438 | 43,359,826 |
| 2 | 489,033 | 9,997 | 176,598 | 69,074,887 |
| 3 | 276 | 1,296 | 85 | 16,277 |

The complete formal run took 353.842 seconds, including both solvers, proof
compression, and proof checking.

## Proof

Assume that a graph $H$ satisfying the claim's four conditions exists.

If $h\notin E(H)$, triangle $T$ forces at least one of its three edges to be
absent.  Choose such an edge.  The edge assignment of $H$ then satisfies the
corresponding branch's fixed units and residual-eight counter.  Since $H$ is
triangle-free it satisfies all triangle clauses.  Since $H$ has no independent
13-set, it satisfies every fixed-base $I_{13}$ hitting clause.  Hence it
satisfies branch 0, 1, or 2, contradicting that branch's checked refutation.

If $h\in E(H)$, the ten disjoint spoke pairs consume all ten allowed deletions.
The preceding structural argument forces $(37,60)$ to be the deletion in its
spoke pair, with exactly one deletion in every other spoke pair.  Therefore
the edge assignment of $H$ satisfies branch 3's units, counter, triangle
clauses, and fixed-base $I_{13}$ clauses.  This contradicts branch 3's checked
refutation.

The two hub cases are exhaustive, so no such $H$ exists.  Therefore every
valid completion in this fixed-seed family needs at least eleven input-edge
deletions. $\square$

## Frozen artifacts

```text
a8f31f25013f870cbcb0523a37bd5539c688adcba185577b1c13931e89cbda33  budget10_search.py
1e145b262e96ac77ae3a6402b539bc523b80bf42569b11324c87df57ac46ef9b  budget10_search.json

6c5d66602bf62e60fd084efc05c59908c33d274571bbf03b93b6b0b63733d6a7  budget10_search_branch_0.cnf.gz
affcb39fb5c0eb272fbdc6bd26aff5dd10b61f34c5c4e84b6c34c95ef16c1447  budget10_search_branch_0.drat.gz

1a6f6955a3a04001d8bfbe56e69ac19ddf6b8dd5cf7ca2bc119469379820dddf  budget10_search_branch_1.cnf.gz
c0eeb889f47115339be9c6f631a4f86bf264408c33a1dc33f646bec7cd425868  budget10_search_branch_1.drat.gz

290322f089f5ec09f4cf0023c91a6745eec2e62da5385874c73520a7bea4cce5  budget10_search_branch_2.cnf.gz
fd5bd7cee9e1d02d50235046f45654220b07dfa3cf45dfdbc770ee13db950fcb  budget10_search_branch_2.drat.gz

363e02620d93e7f12a5ac12f55b80484d31b31541d8512297126b2911ace60fc  budget10_search_branch_3.cnf.gz
c7c9767328ff35bf71765d0578dd9a0e3dbd685ff49e894e7aa0d638b5d016c2  budget10_search_branch_3.drat.gz
```

The compressed artifacts are deterministic (`mtime=0`).  The JSON also pins
the uncompressed DIMACS/DRAT hashes, exact formula sizes, solver limits and
statistics, checker output, and the structural witness.  All eight gzip files
passed integrity checking after the run.

## Reproduction

Build the checker from the pinned official source commit, then run from the
repository root:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/budget10_search.py \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --artifact-dir routes/finite \
  --json routes/finite/budget10_search.json \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-trim-source-commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

If the checker is omitted or rejects any trace, the script emits
`UNKNOWN_PROOF_UNCHECKED`, not a proof-carrying UNSAT conclusion.  Any branch
that reaches a conflict or wall limit makes the global outcome
`UNKNOWN_LIMIT`.

## Claim boundary and open risks

- This excludes only the labeled edit family around the named seed.
- It does not prove $R(3,13)\ge 62$ or improve any global Ramsey-number bound.
- It does not establish existence with eleven deletions.
- The formula generator and sequential-counter semantics remain part of the
  trusted encoding boundary; the checked DRAT traces certify the frozen CNFs,
  not the mathematical exhaustiveness argument by themselves.
- Budget eleven was not searched in this run.
