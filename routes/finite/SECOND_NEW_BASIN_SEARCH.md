# Second new basin for $R(3,13)$: a dispersed 17-triangle near miss

Date: **2026-08-12**  
Verdict: **new structurally dispersed near-miss basin; no new Ramsey bound**

## Goal and search scope

The earlier 61-vertex seed
`r3_13_n61_nonstar_k11.txt` has eleven triangles, but ten of them share one
edge.  This experiment does not edit or continue that seed.  It starts again
from the independently verified public 60-vertex $(3,13)$ graph

```text
routes/finite/certificates/alphaevolve_R3_13_ge_61.txt
SHA-256 d619f0bfed32af5e2fbc8c724d9c65dbf388a19d5647d20e7835b501bc03227a
```

and adds a fresh vertex $60$.  Its neighborhood $S\subseteq\{0,\ldots,59\}$
is the only search variable.  Since the 60-vertex base is triangle-free:

- every base edge induced by $S$ gives exactly one triangle containing
  vertex $60$;
- the number of triangles containing the new edge $(v,60)$ is exactly the
  degree of $v$ in the induced base graph $G[S]$;
- the number of triangles containing an old edge is at most one.

Thus requiring

$$
e(G[S])\leq T,
\qquad \Delta(G[S])\leq M
\tag{1}
$$

is exactly the desired triangle-count and maximum edge-triangle-multiplicity
condition for the 61-vertex extension.

All $106{,}246$ independent 12-sets of the base are precomputed and loaded
as clauses requiring $S$ to meet each one.  This condition is necessary and
sufficient for the extension to contain no independent 13-set: an $I_{13}$
not containing the new vertex would already occur in the valid base, while
one containing it consists of the new vertex plus an independent 12-set
disjoint from $S$.

## New candidate

The bounded SAT search found

```text
routes/finite/r3_13_n61_second_basin_m4_t17.txt
SHA-256 bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f
```

with neighborhood

```text
0, 2, 3, 8, 16, 19, 21, 24, 26, 29,
31, 34, 42, 45, 47, 50, 52, 53, 55, 58
```

and exact diagnostics

| quantity | value |
|---|---:|
| vertices | 61 |
| edges | 369 |
| triangles | 17 |
| independent 13-sets | 0 |
| maximum triangles sharing one edge | 4 |
| minimum edge hitting set of all triangles | 8 |

The triangles are

```text
(0,34,60), (0,53,60), (0,58,60),
(2,8,60), (2,50,60), (3,26,60),
(8,31,60), (16,50,60), (19,42,60),
(21,55,60), (24,47,60), (29,52,60),
(42,53,60), (42,58,60), (47,53,60),
(52,53,60), (55,58,60).
```

Only edge $(53,60)$ lies in four triangles.  Three edges incident to vertex
60 lie in three triangles, six lie in two, and the remaining triangle edges
have multiplicity one.  In particular, no edge lies in more than $4/17$ of
the triangles.  The exact triangle-edge hitting number is eight, compared
with two for the earlier 11-triangle near miss.  This makes the new matrix a
genuinely different, dispersed repair basin rather than a relabeling or a
small perturbation of the old hub geometry.

The graph is still only a near miss: it contains the listed triangles, so it
does not prove $R(3,13)\geq62$.

## Independent verification

The candidate is accepted only after two checks independent of the SAT
generator's model interpretation.

1. The exact bitset verifier reconstructs 61 vertices, 369 edges, a triangle,
   and no independent 13-set after 91,174 recursive nodes.
2. The separately encoded CaDiCaL verifier returns SAT for $K_3$ and UNSAT
   for $I_{13}$.

Both verifiers pin the same matrix hash
`bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f`.
The second record is
`second_new_basin_m4_t17_sat_verification.json`.

## Bounded search ledger

Every run below uses the complete 106,246-clause independent-set bank.  No
lazy separator or heuristic exclusion is involved.

| triangle condition | multiplicity cap | status | conflicts | wall budget / observed elapsed |
|---|---:|---|---:|---:|
| exactly 10 | 4 | `TIME_LIMIT` | 473,991 | 120 s / 120.06 s |
| exactly 11 | 4 | `TIME_LIMIT` | 390,680 | 90 s / 90.06 s |
| exactly 12 | 4 | `TIME_LIMIT` | 457,782 | 75 s / 76.36 s |
| at most 16 | 4 | `UNKNOWN_CONFLICT_LIMIT` | 500,000 | 90 s / 88.88 s |
| at most 17 | 4 | `SAT` | 125,471 | 90 s / 22.08 s |
| at most 20 | 3 | `TIME_LIMIT` | 246,640 | 60 s / 60.06 s |

No row in this table is `UNSAT`.  Therefore:

- combining this run with the frozen exact fixed-base result that every
  zero-$I_{13}$ extension has at least ten triangles gives
  $10\le m_{\mathrm{cap},4}\le17$; the exact value remains **unknown**;
- the at-most-16 instance is **not** excluded;
- the existence of a cap-three seed is **unknown**;
- the exact-10, exact-11, and exact-12 runs prove no nonexistence statement.

The exact-cardinality instances are retained because they were the initial
pre-registered ladder; after the candidate was found, the monotone
at-most-$T$ formulation became the relevant optimization test.

## Formula semantics

For each base vertex $v$, variable $x_v$ means $v\in S$.  For each of the
349 base edges $uv$, an auxiliary variable is reified in both directions:

$$
y_{uv}\longleftrightarrow(x_u\wedge x_v).
\tag{2}
$$

The cardinality constraint on the $y_{uv}$ is therefore exactly (not merely
an upper relaxation of) $e(G[S])$.  For each $v$, the constraint

$$
\sum_{u:uv\in E(G)}y_{uv}\leq M
\tag{3}
$$

is exactly the induced degree bound in (1).  Finally, each base $I_{12}$,
say $X$, contributes

$$
\bigvee_{v\in X}x_v,
\tag{4}
$$

which is exactly the no-$I_{13}$ condition discussed above.

The minimal unit test independently checks on a toy triangle-free graph that
the induced edge count equals the number of new triangles and induced degrees
equal new-edge triangle multiplicities.

## Reproduction

Reproduce the frozen candidate:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python \
  routes/finite/second_new_basin_search.py \
  routes/finite/certificates/alphaevolve_R3_13_ge_61.txt \
  --triangles 17 --at-most --max-multiplicity 4 \
  --solver minisat22 --conflict-chunk 10000 \
  --max-conflicts 500000 --per-call-seconds 10 --max-seconds 90 \
  --output routes/finite/r3_13_n61_second_basin_m4_t17.txt \
  --json routes/finite/second_new_basin_m4_t17_run.json
```

Run the two local structural tests:

```bash
.venv/bin/python -m unittest routes.finite.test_second_new_basin -v
```

Run the independent verifiers:

```bash
.venv/bin/python routes/finite/verify_ramsey.py \
  routes/finite/r3_13_n61_second_basin_m4_t17.txt 3 13

.venv/bin/python routes/finite/verify_ramsey_sat.py \
  routes/finite/r3_13_n61_second_basin_m4_t17.txt 3 13 \
  --solver cadical195
```

## Frozen evidence

| artifact | SHA-256 |
|---|---|
| candidate matrix | `bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f` |
| candidate SAT run | `d31ec22de001d3508957fbb54c09f52542c2d74e48e950fbe95518f508d033e9` |
| exact-10 cap-four `TIME_LIMIT` | `935e7ad07233c824709cf2811330fbfbba5c1fc8425c27d95af7f35682c58bc7` |
| exact-11 cap-four `TIME_LIMIT` | `ea85d36926a91d8dad3134054732552dd2ed7f1d879e1dd5646b2b0c99e005fc` |
| exact-12 cap-four `TIME_LIMIT` | `3fbd19850747ac4a043fea40bd9e6eee1e5abdad2882ae060e70b2e3c9f8f861` |
| at-most-16 cap-four `UNKNOWN` | `ca8dfd31d40ed7bd933423aed25e43ab8cd2eb63444d95253cc38045c4010778` |
| at-most-20 cap-three `TIME_LIMIT` | `e79b757ee0bbd61c7816ec692ad9628d438349cfbae9c560690ae511872c3f00` |

The generator, summary, and SAT-verification hashes should be recomputed when
this report is independently reviewed; unlike the candidate matrix, they can
change under documentation-only metadata updates.

## Claim boundary and next useful step

This route has produced a qualitatively different basin, not a new Ramsey
bound.  The candidate's triangle transversal number eight makes a subsequent
small deletion search structurally less hub-dominated.  A useful next
experiment would branch on minimal triangle transversals of this seed and
allow arbitrary additions, with a deletion budget beginning at eight.  It
should not be conflated with the old seed's completed budget-$10$ radius.

The cap-three question is also open, but blindly extending the same SAT run
is lower priority than the newly identified $R(3,18)$ one-conflict basin.
