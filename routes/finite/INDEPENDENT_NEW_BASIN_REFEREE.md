# Independent referee report: new finite basin

Date: **2026-08-12**

## Verdict

**PASS WITH IMPORTED SOLVER DEPENDENCY.**

The scoped local claim survives review unchanged:

> For the fixed 61-vertex seed with SHA-256
> `2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b`,
> there is no triangle-free graph with independence number at most twelve
> obtainable by deleting at most seven seed edges and adding an arbitrary
> subset of the seed nonedges.

Equivalently, every successful repair in this exact fixed-seed edit family
must delete at least eight of the seed's 363 edges.  This is only a local
exclusion radius.  It is not a new bound on $R(3,13)$.

No fatal encoding gap was found.  The earliest non-self-contained dependency
is the unverified trust boundary at the SAT solver: the retained runs record
CaDiCaL 1.9.5 returning `UNSAT`, but do not retain a DRAT/LRAT proof trace that
can be checked by a small independent proof checker.  Thus the result is a
computer-assisted solver-dependent theorem, not a proof-carrying SAT result.

## Claims and quantifiers audited

The review treats the final graph $G$ as an arbitrary simple graph on the same
61 labeled vertices as the seed $H$.  The edit family is

$$
\left\{G:\ |E(H)\setminus E(G)|\le d\right\}.
$$

There is deliberately no constraint on $E(G)\setminus E(H)$.  The claimed
`UNSAT` range is $d=2,3,4,5,6,7$.  Since any triangle-free repair must delete
at least two seed edges, this covers every possible repair with at most seven
deletions.  Budget eight is `TIME_LIMIT` and remains open.

The separate frozen-base $k=10$ seed run and the R(4,15) run are both
`UNKNOWN`; neither is used as a nonexistence result.

## 1. Independent seed reconstruction

I parsed the matrix independently of `read_matrix`, checked that it is a
symmetric zero-diagonal $61\times61$ binary matrix, and enumerated its edges
and all vertex triples directly.  The reconstruction gives:

- 61 vertices and 363 edges;
- exactly 11 triangles;
- no independent 13-set, by a separate exact branch search that visited
  1,377,127 states;
- maximum triangle multiplicity on one edge equal to 10, attained uniquely by
  edge $(28,60)$;
- the first 60-by-60 principal submatrix is exactly the public frozen base;
- the new vertex has degree 14.

The eleven triangles are exactly those printed in `NEW_BASIN_SEARCH.md`.
Consequently this seed is not a valid Ramsey certificate, because it contains
triangles, but it has no $I_{13}$ and is genuinely outside the all-triangles-
share-one-edge subfamily.

The exact edge-transversal number of the eleven triangles is two.  Independent
enumeration finds no one-edge transversal and exactly three two-edge
transversals:

$$
\begin{aligned}
&\{(28,60),(37,46)\},\\
&\{(28,60),(37,60)\},\\
&\{(28,60),(46,60)\}.
\end{aligned}
$$

The separately encoded retained SAT verification also agrees that $K_3$ is
present and $I_{13}$ is absent.

## 2. Encoding audit for budgets two through seven

The definitive runs use `bounded_deletion_sat_cegar.py`, not the bounded
MiniSat wrapper in `new_basin_search.py`.  Its semantics are correct for the
claim above.

1. `build_variables(61)` assigns one Boolean variable to every unordered
   vertex pair, hence all $\binom{61}{2}=1830$ possible final edges are free
   variables.  In particular, every seed nonedge can be added.
2. For every vertex triple $\{a,b,c\}$, the clause
   $\neg x_{ab}\vee\neg x_{ac}\vee\neg x_{bc}$ is installed.  The reported
   count 35,990 equals $\binom{61}{3}$, so these clauses are exactly the full
   triangle-free condition.
3. Only the 363 variables corresponding to seed edges occur in the cardinality
   constraint, as negative literals.  Therefore it counts precisely the seed
   edges absent from the final graph and does not charge additions.
4. Given a SAT model, reconstruction reads all 1,830 edge variables.  If an
   exact complement-clique search finds an $I_{13}$ on vertex set $S$, the
   clause $\bigvee_{\{u,v\}\in\binom S2}x_{uv}$ is added.  This clause is
   logically equivalent to requiring that $S$ not remain independent.
5. If the persistent solver eventually returns `UNSAT`, all previously added
   cuts are valid necessary conditions.  Hence `UNSAT` for the strengthened
   partial formula implies that no graph in the full edit family satisfies
   triangle-freeness and $\alpha(G)\le12$.

I replayed CaDiCaL independently from the retained matrix.  Budgets 2 through
7 again returned `UNSAT`, with the same iteration/cut pairs

```text
d=2:   2 /   1     d=5:  46 /  45
d=3:   7 /   6     d=6: 137 / 136
d=4:  16 /  15     d=7: 239 / 238
```

The fact that lower budgets start at two is harmless: direct triangle
transversal enumeration proves that budgets zero and one cannot remove all
eleven input triangles, regardless of additions.

## 3. Small-graph truth-table audit

The repository test suite passed all 13 tests.  Its repair-encoding regression
test exhausts all input and final graphs through four vertices, for budgets
zero and one.

I strengthened this check outside the production implementation: for every
input graph on two, three, and four vertices, for every
$s\in\{2,\ldots,n+1\}$, and for every deletion budget from zero through
$\binom n2$, I enumerated every possible final graph and compared existence
with `bounded_deletion_sat_cegar.solve`.  All 1,896 cases agreed.  This covers
the key issues at once: unrestricted addition of initial nonedges, charging
only deleted initial edges, all triangle clauses, and lazy independent-set
cuts.

The triangle-transversal routine also passes the retained 320-random-graph
comparison against exhaustive edge-subset search.  The independent direct
enumeration on the actual seed gives the same transversal number and all three
minimum covers.  The three covers now also have separately frozen add-only
CaDiCaL records; each returns `UNSAT` after one lazy $I_{13}$ cut.  Those
subproblems expose 1,469 addable edges because the two removed seed edges are
also allowed to be re-added.  This is a superset of the fixed-deletion branch,
so `UNSAT` remains a valid, slightly stronger cross-check.

## 4. UNKNOWN branches

The statuses are stated honestly.

- The preloaded non-hub $k=10$ frozen-extension experiment is
  `UNKNOWN_GLOBAL_WALL_LIMIT` after 180.01 seconds and 732,692 conflicts.  It
  proves neither existence nor nonexistence.
- The new-seed budget-eight CaDiCaL result is `TIME_LIMIT` after 406 models/cuts
  and 69.259 seconds.  No conclusion is drawn at $d=8$.
- The restricted $R(4,15)$ experiment is `UNKNOWN_GLOBAL_WALL_LIMIT`, with
  four models and 256 new-vertex-side cuts.  No 160-vertex certificate and no
  exclusion theorem is claimed.

One engineering caveat is worth recording: the legacy budget-eight runner
checks its wall limit between blocking SAT calls, and the R(4,15) wrapper does
not interrupt time spent inside the exact separator.  Therefore their stated
wall limits are soft rather than hard.  This cannot turn either `UNKNOWN` into
`UNSAT` and does not affect the completed $d\le7$ runs.

## 5. Reproducibility and frozen evidence

The reported headline hashes match the current files:

| artifact | independently recomputed SHA-256 |
|---|---|
| `new_basin_search.py` | `944746b24989a12b73f45b111dcffcfd425f8b6d8132d7aa73b7c7a28f7da054` |
| fixed seed matrix | `2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b` |
| seed JSON | `b5d4f2d22274c8a26fed895a10c3fd8218b7b5ee2d46fe0686947f5899aaf6d6` |
| independent SAT verification | `248726f7ae91be94c4e1fe99256c690594fa90a494dd7811cd89071c6db32e7b` |
| non-hub $k=10$ UNKNOWN JSON | `416920ed7593995a8b12f9f71090088e2ab153c835f7232c19fe4a348d2143a6` |
| R(4,15) UNKNOWN JSON | `dd2061cff2db1590a62851c25d3591ee1bdef5aad74057b8942d35a109494560` |
| CaDiCaL $d=7$ JSON | `af0074acb487ada82298ea4b354461e1c0a17d335a592391cc6a70bdfd449a38` |
| CaDiCaL $d=8$ JSON | `b47359f8a4161cc879440e4f6467de9c1bd2f45637e5d4232418a0f253f9c387` |
| $d=2$ split JSON 0 | `3371086dbb79f2c03447b40fd59d02428640f466be89ea9bac5b76a51ef2df3a` |
| $d=2$ split JSON 1 | `bd6516080efb8c6ecafbb5d4b67cd8916fdabe0c1dd522465d9d3f94cb37bbf4` |
| $d=2$ split JSON 2 | `12b5d84081ee6844ee282508042ec23991732755202a2e4fb3176777fad8ae4e` |

The audited environment was Python 3.11.15, PySAT 1.9.dev13, with solver name
`cadical195`.  The definitive encoding script has SHA-256
`d930b133d3e45b03fa92e90172f78c09267082448667aa8ae9c2a0f65d0cbba2`.

## Corrections and open risks

1. **No fatal gap in the scoped $d\le7$ theorem.**  The solver trust boundary
   is the earliest imported dependency.  A publication-grade upgrade would
   emit one proof certificate for each final UNSAT formula and verify it with
   an independent DRAT/LRAT checker.
2. **Resolved during review:** the initially missing ancillary records for the
   three $d=2$ transversal branches are now frozen as
   `new_basin_r3_nonstar_k11_split_0.json` through
   `new_basin_r3_nonstar_k11_split_2.json`.  Their deleted-edge pairs, seed
   hash, counts, statuses, and file hashes agree with the direct enumeration.
3. Hashes establish artifact identity, not semantic correctness.  The semantic
   support comes from the encoding audit, the independent seed reconstruction,
   the 1,896-case truth table, and the fresh $d=2,\ldots,7$ replay above.
