# Independent referee report: second $R(3,13)$ near-miss basin

Date: **2026-08-12**

## Verdict

**PASS — MINOR DOCUMENTATION CORRECTIONS RESOLVED.**

The main scoped claim survives independent review unchanged.  For the fixed
60-vertex graph with SHA-256
`d619f0bfed32af5e2fbc8c724d9c65dbf388a19d5647d20e7835b501bc03227a`,
the neighborhood

$$
S=\{0,2,3,8,16,19,21,24,26,29,31,34,42,45,47,50,52,53,55,58\}
$$

produces a 61-vertex graph with 369 edges, exactly 17 triangles, no
independent 13-set, maximum triangle multiplicity four on one edge, and
triangle-edge transversal number eight.  The candidate matrix has SHA-256
`bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f`.

This is a verified near miss, not a triangle-free Ramsey graph.  It does not
prove $R(3,13)\geq62$ and does not improve any global Ramsey-number bound.
None of the six bounded-search rows is `UNSAT`; the time- and conflict-limited
rows prove no nonexistence statement.

## Claim normalization and assumptions

Let $G$ be the frozen 60-vertex base and let $G_S^+$ be obtained by adding a
new vertex $60$ adjacent exactly to the vertices in $S$.  The reviewed claims
use the following established properties of the particular input matrix:

1. $G$ is triangle-free and has independence number 12.
2. The first 60-by-60 principal submatrix of the candidate is exactly $G$.
3. The only search variables are the membership indicators of $S$; no old
   edge of $G$ is edited in this experiment.
4. Solver outcomes `TIME_LIMIT` and `UNKNOWN_CONFLICT_LIMIT` are observations
   about bounded runs, not proofs of unsatisfiability.

The proof strategy is direct finite reconstruction, followed by independent
bitset and SAT checks.  The dependencies are:

1. Candidate counts depend only on the two pinned matrices.
2. The no-$I_{13}$ condition depends on the complete family of base
   independent 12-sets, or equivalently on an exact independent-set search in
   the candidate.
3. The transversal number depends only on the 17 reconstructed triangles.
4. Search-limit statements depend on the retained JSON statuses and do not
   support any additional mathematical exclusion.

## 1. Base provenance and artifact identity

The base is recorded in `certificate_manifest.json` as the file
`ramsey_number_bounds/improved_bounds/R(3, 13) >= 61.txt` in the official
Google Research repository at commit
`015539128d9a7dbe14b5f5308a198a15da808949`.  A fresh download from that exact
commit independently hashed to the same value as the local file:

```text
d619f0bfed32af5e2fbc8c724d9c65dbf388a19d5647d20e7835b501bc03227a
```

The currently audited files have the following independently recomputed
SHA-256 hashes.

| artifact | SHA-256 |
|---|---|
| `SECOND_NEW_BASIN_SEARCH.md` | `46932a337148bfe3aa622ee55347cc0587091f44478a1817dd51922612196d1e` |
| `second_new_basin_search.py` | `d06afd3c43191da91da45a714a6c13ba0c5f249ebbcd143aca97bc9a8d98d00b` |
| base matrix | `d619f0bfed32af5e2fbc8c724d9c65dbf388a19d5647d20e7835b501bc03227a` |
| candidate matrix | `bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f` |
| candidate SAT run | `d31ec22de001d3508957fbb54c09f52542c2d74e48e950fbe95518f508d033e9` |
| candidate SAT verification | `eea8695047e0cb5be866c22528a3328cd1845b52b1e40cdb99a1d940ccb51046` |
| summary | `3bd08c956fa9ebecf1b97905d0e4504dc0081a6b88df24c3a6aeae13678e5c7f` |
| structural tests | `b66ce8d0dd1971cf38398b83e4ca5f4ab8b51d7c83c1573ef5fedc0c61eb4bd8` |
| exact-10 cap-four record | `935e7ad07233c824709cf2811330fbfbba5c1fc8425c27d95af7f35682c58bc7` |
| exact-11 cap-four record | `ea85d36926a91d8dad3134054732552dd2ed7f1d879e1dd5646b2b0c99e005fc` |
| exact-12 cap-four record | `3fbd19850747ac4a043fea40bd9e6eee1e5abdad2882ae060e70b2e3c9f8f861` |
| at-most-16 cap-four record | `ca8dfd31d40ed7bd933423aed25e43ab8cd2eb63444d95253cc38045c4010778` |
| at-most-20 cap-three record | `e79b757ee0bbd61c7816ec692ad9628d438349cfbae9c560690ae511872c3f00` |

## 2. Independent matrix reconstruction

I parsed the two matrices without importing the production graph utilities,
then checked squareness, binary entries, zero diagonal, and symmetry.  The
base has 60 vertices and 349 edges.  Its first 60 rows and columns agree
entry-for-entry with the corresponding principal submatrix of the candidate.
The candidate adds the 20 edges from vertex 60 to the displayed set $S$, so
it has $349+20=369$ edges.

Direct enumeration of all vertex triples gives exactly the 17 triangles
printed in the main report.  Every one contains vertex 60.  The induced base
graph $G[S]$ has 17 edges and degree sequence, indexed by $S$,

```text
0:3, 2:2, 3:1, 8:2, 16:1, 19:1, 21:1, 24:1, 26:1, 29:1,
31:1, 34:1, 42:3, 45:0, 47:2, 50:2, 52:2, 53:4, 55:2, 58:3.
```

Consequently edge $(53,60)$ is the unique edge in four triangles.  Vertices
$0,42,58$ give the three new edges of multiplicity three, and vertices
$2,8,47,50,52,55$ give the six new edges of multiplicity two.  Every old edge
in a triangle has multiplicity one.  This independently verifies the reported
maximum multiplicity and its distribution.

## 3. Why the fixed-extension encoding is exact

Because $G$ is triangle-free, any triangle of $G_S^+$ must contain vertex 60.
For $u,v\in S$, the triple $\{u,v,60\}$ is a triangle exactly when
$uv\in E(G)$.  Therefore

$$
\#K_3(G_S^+)=e(G[S]).
$$

For a new edge $(v,60)$, its triangle multiplicity is
$\deg_{G[S]}(v)$.  An old edge lies in at most the one triangle completed by
vertex 60.  Thus the current instances, all of which have nonnegative
triangle bounds and multiplicity caps at least one, encode the triangle count
and maximum edge multiplicity exactly.

The production clauses for every old edge $uv$ are

$$
(\neg x_u\vee\neg x_v\vee y_{uv})\wedge
(\neg y_{uv}\vee x_u)\wedge(\neg y_{uv}\vee x_v),
$$

which are equivalent to $y_{uv}\leftrightarrow(x_u\wedge x_v)$.  Hence the
cardinality constraint on the $y_{uv}$ counts exactly the edges of $G[S]$,
and each incident cardinality constraint is exactly an induced-degree bound.
The auxiliary-variable pool begins after all 60 membership variables and 349
edge indicators and is reused monotonically, so the reviewed encoding has no
variable collision.

For the blue condition, an independent 13-set containing vertex 60 is
$\{60\}\cup X$, where $X$ is a base independent 12-set disjoint from $S$.
Since the base itself has no $I_{13}$, the extension has no $I_{13}$ exactly
when $S$ meets every base $I_{12}$.  Independent enumeration found all
106,246 such sets and reproduced their ordered-mask hash

```text
8338f2e07306f56909033907986e71cbfd3f4281e1ad22fe225832fb52121604.
```

As a separate regression check, I exhaustively enumerated every graph and
every possible new-vertex neighborhood through five base vertices.  Across
33,866 graph-neighborhood pairs, the independent-set hitting equivalence held
for every possible target size.  Across the 13,138 pairs with triangle-free
bases, the triangle-count and edge-multiplicity identities above also held.
The repository's two retained structural unit tests pass.

## 4. Independent no-$I_{13}$ verification

A standalone increasing-order bitset search, distinct from the production
branch ordering, gave:

| graph | query | result | recursive calls |
|---|---|---:|---:|
| 60-vertex base | $I_{13}$ | absent | 1,242,420 |
| 61-vertex candidate | $I_{13}$ | absent | 1,333,915 |

The production Tomita-style checker independently returned no candidate
$I_{13}$ after 91,174 recursive nodes, matching the retained report.  A fresh
Glucose 4.2 run with an ordered-position encoding, rather than the retained
CaDiCaL selector encoding, returned `UNSAT` for $I_{13}$ from 53,814 clauses.
It also returned `SAT` for $K_3$ and exhibited triangle $(42,58,60)$.

These checks verify that the graph is a near miss with no $I_{13}$, while its
17 triangles prevent it from being a Ramsey certificate.

## 5. Exact triangle-edge transversal number

All triangles correspond to the 17 edges of $G[S]$.  If a triangle hitting
set contains the new edges $(v,60)$ for $v$ in a set $X\subseteq S$, then
every remaining triangle corresponds to an edge of $G[S\setminus X]$ and can
only be hit by selecting that old edge.  Therefore the minimum possible size
is exactly

$$
\min_{X\subseteq S}\bigl(|X|+e(G[S\setminus X])\bigr).
$$

Exhausting all $2^{20}=1,048,576$ sets $X$ gives minimum eight, with no set of
cost at most seven and exactly three optimal covers.  They are

```text
{(0,60),(8,60),(42,60),(47,60),(50,60),(52,60),(55,60),(3,26)}
{(0,60),(3,60),(8,60),(42,60),(47,60),(50,60),(52,60),(55,60)}
{(0,60),(8,60),(26,60),(42,60),(47,60),(50,60),(52,60),(55,60)}
```

Thus the reported transversal number eight is exact.  Together with maximum
triangle-edge multiplicity four, it also proves that this graph is not
isomorphic to the earlier 11-triangle seed, whose corresponding invariants
are two and ten.

## 6. Reproduction and bounded-status audit

I reran the frozen candidate command with the current generator in a fresh
temporary directory.  MiniSat 2.2 again returned `SAT`, recovered the same
20-vertex neighborhood, and wrote a byte-identical candidate with hash
`bb43e22b66e0d93cf02fdbfc81a0cdfc03587a794dea7605e87dbc171c40792f`.
The reconstructed result again had 17 triangles, maximum multiplicity four,
106,246 preloaded $I_{12}$ clauses, and the same bank hash.

The retained bounded-search records state:

| condition | cap | retained status | raw status | recorded conflicts |
|---|---:|---|---|---:|
| exactly 10 | 4 | `TIME_LIMIT` | `UNKNOWN_GLOBAL_WALL_LIMIT` | 473,991 |
| exactly 11 | 4 | `TIME_LIMIT` | `UNKNOWN_GLOBAL_WALL_LIMIT` | 390,680 |
| exactly 12 | 4 | `TIME_LIMIT` | `UNKNOWN_GLOBAL_WALL_LIMIT` | 457,782 |
| at most 16 | 4 | `UNKNOWN_CONFLICT_LIMIT` | `UNKNOWN_GLOBAL_CONFLICT_LIMIT` | 500,000 |
| at most 17 | 4 | `SAT` | `SAT` | 125,471 |
| at most 20 | 3 | `TIME_LIMIT` | `UNKNOWN_GLOBAL_WALL_LIMIT` | 246,640 |

No record says `UNSAT`, and the main report correctly refuses to infer
nonexistence from any limited run.  In particular, at-most-16 with cap four,
the cap-three search, and the exact-10 through exact-12 instances all remain
open under these records.

The archived exact-10 through exact-12 JSON files use the older metadata key
`exact_triangle_count`, whereas the current generator writes the pair
`triangle_count_relation` and `triangle_count_bound`.  This does not affect a
theorem because all three archived outcomes are only `TIME_LIMIT`; the current
candidate command itself reproduced exactly.

## Resolution audit for the main report

The two requested documentation corrections have been applied and rechecked
against the retained JSON records.

1. The report now imports the already frozen unrestricted fixed-base result
   that triangle counts zero through nine are impossible and states the
   sharper honest interval

   $$
   10\leq \min\{e(G[S]):S\text{ hits every base }I_{12},\
   \Delta(G[S])\leq4\}\leq17.
   $$

   The report continues to mark the exact value unknown.
2. The table now distinguishes “wall budget / observed elapsed.”  Its six
   displayed pairs agree, after rounding to two decimals, with the requested
   budgets and retained total elapsed times: 120/120.06, 90/90.06,
   75/76.36, 90/88.88, 90/22.08, and 60/60.06 seconds.  Every limited row
   retains its original `TIME_LIMIT` or `UNKNOWN_CONFLICT_LIMIT` status.

The corrected main report has SHA-256
`46932a337148bfe3aa622ee55347cc0587091f44478a1817dd51922612196d1e`.

One interpretive caveat remains rather than a requested correction:

- “Not a small perturbation” should be read as a qualitative structural
   description.  The nonisomorphism and the dispersed triangle geometry are
   verified by the invariant changes above, but no formal edit-distance
   threshold was stated or proved.

## Open risks and claim boundary

- The no-$I_{13}$ computation has independent bitset and SAT implementations,
  but no proof-assistant formalization or retained DRAT/LRAT trace.  The
  earliest remaining trust boundary is the correctness of these small exact
  programs and their runtime libraries.
- Hashes establish artifact identity, not semantic correctness.  The semantic
  support comes from direct matrix reconstruction, full $I_{12}$ enumeration,
  two differently ordered $I_{13}$ searches, the independent positional SAT
  run, exhaustive small-graph truth tables, and the $2^{20}$ transversal
  computation.
- The search explores only one-vertex extensions of one fixed 60-vertex base.
  It neither excludes other 61-vertex constructions nor establishes that a
  repair exists at deletion budget eight.
- The candidate is useful as a distinct local repair basin, but all claims
  beyond the displayed finite diagnostics remain experimental and open.
