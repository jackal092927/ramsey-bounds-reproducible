# Independent adversarial referee: fixed-near-miss budget-six branch 2

Date: 2026-08-12  
Scope: the frozen branch-2 exact-six certificate only

## Verdict

```text
fixed near-miss and unique triangle:              PASS
prior deletion budget <=5 dependency:             PASS, all three DRATs replayed
branch-2 exact-total-six semantics:                PASS
arbitrary original-nonedge additions:              PASS
branch-2 CNF reconstructed clause by clause:       PASS
branch-2 146 MB compressed DRAT replay:             PASS, s VERIFIED
branch-2 conclusion:                               PROVABLE AS STATED
branches 0 and 1:                                  UNKNOWN
overall fixed-seed budget <=6 edit ball:           UNKNOWN
R(3,18) >= 101 / fixed repair radius >=7:          NOT ESTABLISHED
```

The frozen artifacts prove exactly the following scoped statement:

> Let $H$ be the pinned $100$-vertex near miss with SHA-256
> `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
> There is no graph obtained by fixing the input edge $(98,99)$ absent,
> deleting exactly five further input edges of $H$, and adding an arbitrary
> subset of the original nonedges, which is both triangle-free and has no
> independent set of size $18$.

This branch-2 statement is `PROVABLE AS STATED`.  The complete three-branch
budget-six question remains `NOT CURRENTLY JUSTIFIED`: branches 0 and 1
ended only at bounded `UNKNOWN` endpoints.  Consequently this review does
not support $R(3,18)\ge101$, a $100$-vertex Ramsey graph, or the claim that
the fixed near miss has repair radius at least seven.

## Frozen snapshot and hashes

The reviewed package is pinned by

```text
f736b63735f9664234e5b785d9a223cfc69834f9ab1417475119825eb1687f49  R3_18_BUDGET6_AUDIT.md
fcb9f27bff2fe9c1cc1d563d52bf1e57aba027548473ad0bb40757908522736c  r3_18_budget6_branch.py
3b4d9c3ed620b2a4c893d06e95a42bbef157ec88b59ab54605693f1ef9e5e78b  check_r3_18_budget6.py
90696db01178e8cb8392879f181af7f7a0a1b1f1de1ae3ce49b4e3f87ffc9304  test_r3_18_budget6_branch.py
c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06  r3_18_budget6_branch_2.cnf.gz
aaa79a2f25d4c0d61c4467f1d0a721fd670a624e0391d96b2122723f97ba4598  r3_18_budget6_branch_2.cuts.json
c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9  r3_18_budget6_branch_2.drat.gz
ee0c73b80407a4dd48ca69bd1a666f391bfd5729b9a56e062deef2a6f62018de  r3_18_budget6_branch_2.json
dbcbeb4ff8f65519546119ea5ca2dc5faf37193b55a9f92a44e9b3743dda8f8a  r3_18_budget6_summary.json
e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e  certificates/r3_18_n100_nearmiss.txt
cfde13c5957229168aaf12f23afc43018552a0707936a262836fbd9e573c8e9d  r3_18_extension_repair_check.json
961151173b4af656a83d6ff74d5de79f865d5cb0d17b0cdfc581bfae2d7a7711  INDEPENDENT_R3_18_EXTENSION_REFEREE.md
```

I also recomputed the uncompressed artifact identities:

```text
CNF raw SHA-256:   65c5ff9a402bdaeb3352f90eb6fb64b86141de5b1750977cc66b8c5ae7efb4a3
CNF raw bytes:     6,919,594
CNF raw lines:     183,544 including the header
DRAT raw SHA-256:  66d0aa3d5cd2536bae7d59ed884324057561db1baa70dfcd683cda4827915a43
DRAT raw bytes:    759,008,359
DRAT raw lines:    2,837,771
```

All values agree with the frozen branch record.

## Dependency map

The scoped conclusion depends on five independently checked steps.

1. The pinned adjacency matrix has $100$ vertices, $827$ edges, no
   independent $18$-set, and the unique triangle $(97,98,99)$.
2. The earlier proof-carrying result excludes every eligible repair with at
   most five input-edge deletions, while allowing arbitrary additions.
3. Therefore a previously uncovered repair within the budget-six ball must
   use exactly six input-edge deletions.
4. In branch 2, fixing $(98,99)$ absent accounts for one deletion, so the
   correct residual condition is exactly five deletions among the other
   $826$ input edges.  The frozen CNF is a relaxation of precisely this
   branch and preserves arbitrary additions.
5. The pinned DRAT trace proves that finite CNF UNSAT.  Since every exact
   branch-2 Ramsey repair would satisfy the finite relaxation, none exists.

Steps 1--5 do not close branches 0 or 1.  The three-way triangle-edge split
is exhaustive only after all three branches are resolved; this review has
one new resolved branch and two unresolved ones.

## Matrix and branch reconstruction

I parsed the adjacency matrix independently of the package's stored JSON.
It is a symmetric $100\times100$ zero-diagonal binary matrix with $827$
edges.  Direct enumeration of all $\binom{100}{3}=161700$ vertex triples
finds exactly

$$
(97,98,99).
$$

The existing exact graph verifier again found no independent set of size
$18$.  Thus every triangle-free final graph must omit at least one of

$$
(97,98),\qquad(97,99),\qquad(98,99).
$$

This gives three covering branches, not necessarily disjoint branches.  The
present certificate concerns only the last edge.

## Why the budget is exact five after the fixed edge

Let $E(H)$ be the $827$ input edges and let $F$ be a candidate final graph.
The number counted by the edit budget is

$$
d(F)=|E(H)\setminus E(F)|.
$$

The previously checked theorem gives no candidate with $d(F)\le5$, even
when $E(F)\setminus E(H)$ is arbitrary.  Hence any new candidate satisfying
$d(F)\le6$ has $d(F)=6$.

In branch 2, the negative unit $\neg x_{98,99}$ forces one of these six
deletions and prevents that edge from being re-added.  The residual equality
is therefore

$$
\sum_{e\in E(H)\setminus\{(98,99)\}}(1-x_e)=5.
\tag{1}
$$

The counter contains $826$ literals, one for each remaining input edge.
No original nonedge appears in (1).  All $4950=\binom{100}{2}$ pairs still
have final-edge variables, so every original nonedge may independently be
set to present or absent, subject only to the triangle and $I_{18}$
conditions.  This is the advertised arbitrary-additions semantics.

The earlier budget-five dependency is not merely a stored Boolean in this
review.  I reconstructed the three prior CNFs and replayed their DRAT traces
with the same pinned checker.  The runs for fixed absent edges $(97,98)$,
$(97,99)$, and $(98,99)$ all ended in `s VERIFIED`, with checker times
approximately $5.5$, $14.0$, and $8.1$ seconds.  Thus the reduction from
``at most six'' to ``exactly six'' has a live checked dependency.

The compressed prior proof pairs replayed here have hashes

| fixed edge | CNF gzip SHA-256 | DRAT gzip SHA-256 |
|---|---|---|
| $(97,98)$ | `d64f009f840597e266ccfb3b31c88f7e87eb760d1fc551b7ee08a0854749ba66` | `60687241833df8ae957b3b4fcb02e6e9f7595c6e3dcbee8b77f02dad5443f913` |
| $(97,99)$ | `d6d321a4ac1aeec5e99c48843a8cda9395271e89555cea328e29bcda4e70ef15` | `33a9e037e19beeab8dd2af4dca5ce9010d4906b39dc3e5cc8fd62823f518497a` |
| $(98,99)$ | `8d8a543bb3cc17014941fee432673a1dc2b99c8cb4885d4d91bba9005f3b10a7` | `159865da9ad23eea298ebd4e9406f2f37ecc6015a593975e9d63e3b08a859897` |

## Clause-by-clause CNF reconstruction

### Variables

For each unordered pair $0\le u<v<100$, the primary variable

$$
x_{uv}=1
$$

means that $(u,v)$ is an edge of the final graph.  Lexicographic pair order
assigns variables $1,\ldots,4950$.  A fresh sequential counter begins at
variable $4951$.

PySAT `CardEnc.equals` with `EncType.seqcounter`, the exact ordered literal
list $[-x_e:e\in E(H)\setminus\{(98,99)\}]$, and bound $5$ is the union of
an at-least-five and at-most-five counter.  Reconstruction gives $8210$
auxiliary variables, maximum variable $13160$, and $16420$ clauses.  I
compared every one of these clauses in order with the frozen DIMACS, not
only their count.  As a semantic cross-check, complete primary assignments
with deletion counts

$$
0,1,4,5,6,7,825,826
$$

were passed to an independent SAT backend with the reconstructed counter;
exactly the count-five assignment was extensible to the auxiliaries.

### Triangle prefix

For every $a<b<c$, the first $161700$ clauses are exactly

$$
\neg x_{ab}\lor\neg x_{ac}\lor\neg x_{bc}.
\tag{2}
$$

I regenerated this lexicographically ordered prefix and compared every
literal.  Formula (2) is equivalent to triangle-freeness of the final graph,
including triangles created by added original nonedges.

### Fixed negative unit

After the exact-cardinality block, the next clause is exactly

$$
\neg x_{98,99}.
\tag{3}
$$

The fixed edge is excluded from the residual counter, so (1) together with
(3) encodes six distinct input-edge deletions in total.

### Independent-$18$ hitting clauses

The remaining $5422$ clauses are in one-to-one ordered correspondence with
the masks in the frozen cut bank.  Every mask has exactly $18$ distinct
vertices and lies within the $100$-vertex universe.  For a mask $S$, its
clause is exactly the $153$ distinct positive primary literals

$$
\bigvee_{e\in\binom{S}{2}}x_e.
\tag{4}
$$

I reconstructed the complete edge set of every mask and compared every
clause in stored order.  The masks are unique, and their deterministic
ordered digest is

```text
9d86582d574d3c788452018a9caca8e26e0ed1737a96e9f8112e315d4a0d2ac3
```

No counter variable or negative literal occurs in this tail.

The $5422$ clauses need not enumerate every possible $18$-set.  Any graph
with no independent $18$-set must satisfy (4) for every installed $S$.
Hence this finite bank is a relaxation of the exact $I_{18}$-free problem:
if the relaxation is UNSAT, the exact branch is also UNSAT.  The implication
is in the proof-required direction.

### Complete formula accounting

The clause partition is

| block | clauses |
|---|---:|
| all triangle clauses | 161,700 |
| exact-five sequential counter | 16,420 |
| fixed negative unit | 1 |
| installed $I_{18}$ hitting clauses | 5,422 |
| **total** | **183,543** |

The frozen DIMACS header is exactly `p cnf 13160 183543`, and there are no
extra or missing clauses after the reconstructed tail.

## Independent DRAT replay

The executable used in this review has

```text
source commit:          2e3b2dc0ecf938addbd779d42877b6ed69d9a985
drat-trim.c local diff: none
executable SHA-256:     31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4
```

I ran the frozen CNF/DRAT pair through this checker with a parent-enforced
$300$-second limit.  It exited $0$ after $79.8$ seconds and reported

```text
c parsing input formula with 13160 variables and 183543 clauses
c detected empty clause; start verification via backward checking
c 22811 of 183543 clauses in core
c 518481 of 1354503 lemmas in core using 182817377 resolution steps
c 0 RAT lemmas in core
s VERIFIED
```

Thus branch 2 does not rest on an imported solver status or an unreplayed
proof record.  The compressed $146$ MB trace was checked in this referee
run against the independently reconstructed frozen formula.

## Proof of the scoped conclusion

Assume that a branch-2 final graph $F$ with the stated edit semantics exists.
Assign every primary variable according to $E(F)$.  Triangle-freeness makes
all clauses (2) true.  Exact total deletion count six, together with the
fixed absent edge, makes the primary literals in (1) have sum five; the
standard sequential-counter extension supplies auxiliary values satisfying
the exact-cardinality CNF.  Clause (3) holds by the branch assumption.  Since
$F$ has no independent $18$-set, it satisfies every installed clause (4).

Therefore this assignment would extend to a model of the frozen branch-2
CNF.  The verified DRAT proof shows that the CNF is UNSAT, a contradiction.
The scoped branch-2 conclusion follows. $\square$

## Why the global endpoint remains UNKNOWN

The frozen summary records two independent $600$-second bounded discovery
runs for each of branches 0 and 1.  Their endpoints are

| branch | fixed edge | Glucose 4.2 | MapleChrono |
|---:|---|---|---|
| 0 | $(97,98)$ | `UNKNOWN_DISCOVERY_WALL_LIMIT` | `UNKNOWN_DISCOVERY_WALL_LIMIT` |
| 1 | $(97,99)$ | `UNKNOWN_DISCOVERY_WALL_LIMIT` | `UNKNOWN_DISCOVERY_WALL_LIMIT` |

Neither branch has a fully separated verified SAT graph or a checked UNSAT
proof.  Solver conflicts, accumulated cuts, partial checkpoints, and elapsed
time do not imply either satisfiability or unsatisfiability.  Consequently

```text
branch 2 exact-six slice:          UNSAT, proof verified
branches 0 and 1 exact-six slices: UNKNOWN
complete fixed budget <=6 ball:    UNKNOWN
```

The old budget-$\le5$ exclusion already implies that any repair requires at
least six deletions.  To claim repair radius at least seven one must exclude
all exact-six repairs, including branches 0 and 1; this has not been done.
Nor can a local branch exclusion prove or disprove the existence of an
unrelated $100$-vertex triangle-free, $I_{18}$-free graph.

## Claim boundary and residual trust

This report approves only the branch-2 theorem in the verdict.  It does not
approve:

- the complete fixed-seed deletion-budget-six exclusion;
- fixed-seed repair radius at least seven;
- a candidate $100$-vertex $(3,18)$ Ramsey graph;
- $R(3,18)\ge101$ or $R(3,18)=100$;
- nonexistence of any other $100$-vertex construction;
- a new global finite Ramsey-number bound.

The remaining trust boundary is the exact graph verifier for the seed's
no-$I_{18}$ fact, PySAT's sequential-counter semantics, the pinned
`drat-trim` implementation/compiler/hardware, and the operating system's
file and decompression behavior.  The matrix structure, literal mapping,
counter clauses, cut clauses, compressed and raw hashes, and DRAT trace were
all independently reconstructed or replayed in this review.
