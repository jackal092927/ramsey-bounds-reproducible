# Independent adversarial referee: complete fixed-seed budget-six closure

Date: 2026-08-12  
Scope: the pinned $100$-vertex $R(3,18)$ near miss and the deletion budget
$d_H(F)\leq 6$, with arbitrary additions among input nonedges

## Claim

Let $H$ be the graph in
`certificates/r3_18_n100_nearmiss.txt`, with SHA-256
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
For a graph $F$ on the same vertex set, define

$$
d_H(F)=|E(H)\setminus E(F)|.
$$

There is no graph $F$ that is triangle-free, has no independent set of size
$18$, and satisfies $d_H(F)\leq 6$.  Edges outside $E(H)$ are not charged and
may be added arbitrarily.

Equivalently, the deletion repair radius of this **fixed seed**, under these
free-addition edit semantics, is at least seven (or infinite if the seed has
no repair at any deletion count).

## Status

**PROVABLE AS STATED.**

```text
seed identity, 827 edges, and unique K3 (97,98,99):       PASS
seed has no independent 18-set:                           PASS
prior fixed-seed deletion budget <=5 dependency:          PASS
three-edge branch cover:                                  PASS
branch 0 exact-six CNF reconstructed clause by clause:    PASS
branch 0 cross-branch cut transfer:                        PASS
branch 0 compressed/raw artifact identities:              PASS
branch 0 fresh pinned drat-trim replay:                    PASS, s VERIFIED
branch 1 prior proof package and current hashes:           PASS
branch 2 prior proof package and current hashes:           PASS
complete fixed-seed deletion budget <=6 exclusion:         PASS
existence of an exact-seven repair:                        NOT ESTABLISHED
R(3,18) >= 101 or a 100-vertex Ramsey graph:               NOT ESTABLISHED
```

The conclusion is local to this frozen seed and deletion metric.  It is not a
new global lower bound for $R(3,18)$.

## Assumptions and notation

- A primary variable $x_{uv}$ denotes whether the unordered pair $(u,v)$ is
  an edge of the final graph $F$.
- All $\binom{100}{2}=4950$ pair variables exist.  In particular, original
  nonedges remain free variables and are absent from the deletion counter.
- The desired Ramsey conditions are triangle-freeness and
  $\alpha(F)<18$.
- The three branch edges are
  $f_0=(97,98)$, $f_1=(97,99)$, and $f_2=(98,99)$.
- The prior budget-five theorem is the proof-carrying fixed-seed result in
  `r3_18_extension_repair_check.json`, independently refereed in
  `INDEPENDENT_R3_18_EXTENSION_REFEREE.md`.

## Dependency map

1. Direct matrix reconstruction gives the unique seed triangle
   $(97,98,99)$.
2. Every triangle-free final graph omits at least one of $f_0,f_1,f_2$.
3. The verified prior package excludes $d_H(F)\leq5$.
4. Therefore a remaining candidate with $d_H(F)\leq6$ must have
   $d_H(F)=6$.  In a branch with $f_i$ fixed absent, exactly five of the
   other $826$ input edges are absent.
5. Each branch CNF is a relaxation of the corresponding exact Ramsey branch:
   it contains all triangle clauses, the exact-five residual counter, the
   fixed negative unit, and a subset of universally valid independent-set
   hitting clauses.
6. Complete checked DRAT proofs establish all three branch CNFs UNSAT.
7. The three covering branches and the prior budget-five result imply the
   stated budget-at-most-six exclusion.

## Seed and exhaustive branch split

I parsed the matrix independently.  It is a symmetric $100\times100$
zero-diagonal binary matrix with $827$ edges.  Exhaustive enumeration of all
$\binom{100}{3}=161700$ triples finds exactly one triangle,

$$
\{97,98,99\}.
$$

The exact graph verifier again returned no independent $18$-set.  Every
triangle-free $F$ must therefore omit at least one edge of that triangle.
The branches cover all candidates but need not be disjoint; a graph omitting
two or three triangle edges simply belongs to more than one branch.

For any candidate not already excluded by the budget-five theorem,
$d_H(F)=6$.  If $f_i$ is selected as a missing triangle edge, then

$$
\sum_{e\in E(H)\setminus\{f_i\}}(1-x_e)=5,
$$

because the unit $\neg x_{f_i}$ accounts for the sixth deletion.  This
identity remains correct when another triangle edge is also missing: that
other edge is one of the five counted residual deletions.

## Branch 0: independent formula reconstruction

Branch 0 fixes $f_0=(97,98)$ absent.  I reconstructed the frozen DIMACS from
the matrix without importing the discovery solver's result.

### Variables and exact counter

Lexicographic pair order assigns primary variables $1,\ldots,4950$.  A fresh
PySAT `CardEnc.equals` sequential counter over the $826$ literals
$[-x_e:e\in E(H)\setminus\{f_0\}]$, with bound five, reproduced all $16420$
stored counter clauses in order.  It introduces $8210$ auxiliary variables
and ends at variable $13160$.

As an additional semantic test, complete primary assignments with residual
deletion counts

$$
0,1,4,5,6,7,825,826
$$

were offered to an independent SAT backend.  The counter auxiliaries were
extendible if and only if the count was five.

### Complete clause partition

Every stored clause was compared in order against an independent
reconstruction:

| block | clauses | checked semantics |
|---|---:|---|
| triangle clauses | 161,700 | $\neg x_{ab}\lor\neg x_{ac}\lor\neg x_{bc}$ for every $a<b<c$ |
| exact-five sequential counter | 16,420 | five residual input-edge deletions |
| fixed negative unit | 1 | $\neg x_{97,98}$ |
| independent-$18$ hitting clauses | 251,771 | all 153 positive pair variables of one 18-set |
| **total** | **429,892** | exact DIMACS header and no trailing clause |

Every hitting clause contains $153=\binom{18}{2}$ distinct positive primary
variables, reconstructs exactly the complete pair family of an $18$-vertex
set, and contains no auxiliary variable.  The ordered mask digest recovered
from the CNF is

```text
f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa
```

and agrees exactly with the frozen cut bank.

### Why the transferred cut union is valid

For every $18$-vertex set $S$, every graph with $\alpha(F)<18$ satisfies

$$
C_S=\bigvee_{e\in\binom S2}x_e.
$$

This is an axiom of the target graph property and contains no branch
assumption.  It is therefore sound to reuse such clauses discovered while
solving branches 1, 2, or the budget-five branches.  Only vertex-set masks
were transferred; no solver-learned clause or solver status was imported.

I separately reparsed all seven sources.  Every mask had population count
$18$, all CNF-tail sources reconstructed complete 18-set pair families, and
their deduplicated union agreed exactly with the final $251771$-mask bank:

| source | source masks | new masks | cumulative union |
|---|---:|---:|---:|
| branch-0 discovery checkpoint | 183,133 | 183,133 | 183,133 |
| branch-0 earlier cut bank | 141,149 | 4,096 | 187,229 |
| branch-1 cut bank | 63,943 | 52,515 | 239,744 |
| branch-2 cut bank | 5,422 | 3,931 | 243,675 |
| budget-five branch-0 cut bank | 287 | 286 | 243,961 |
| budget-five branch-1 CNF tail | 15,872 | 4,262 | 248,223 |
| budget-five branch-2 CNF tail | 8,704 | 3,548 | 251,771 |

The exact $I_{18}$-free problem would contain $C_S$ for every 18-set.  The
frozen formula contains only the audited subset above, so it is a
**relaxation** of the exact branch.  UNSAT of this relaxation implies UNSAT
of the exact branch; the implication direction is correct.

Original nonedges occur among the $4950$ primary variables but not in the
counter.  They may be added or omitted, subject only to the final triangle
and installed hitting clauses.  Thus the proof does not hide a restriction
on additions.

## Branch 0: artifact and proof audit

The relevant identities recomputed in this review are:

| artifact | bytes | SHA-256 |
|---|---:|---|
| seed matrix | -- | `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e` |
| CNF gzip | 17,600,735 | `47052de808b98598f2f144251a6ad73c1415dd00fef9e04b99ffe2f176229fbf` |
| CNF raw | 174,796,028 | `0dec49bdbee74644db5fc181e25f7df02a72dfd1b23a3ab4f859501de8a0d3cd` |
| cut bank | 8,308,702 | `91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b` |
| DRAT gzip | 656,144,450 | `4d948ab34f1d2475af6efe943e0a4899827c78b96c2bc3835b5161f189c26bb5` |
| DRAT raw | 3,493,847,713 | `43dde468b13a1f45667b0a8dc54c2c7d14b0b33f6dc01d85383b0a37f5ffca91` |
| semantic checker | -- | `1e70628276c8279876af8089dea0b12164014a06a5733588570347399802fe45` |

The raw proof has $6,649,939$ lines.  All branch-0, branch-1, and branch-2
CNF/DRAT gzip streams passed integrity checking.

The proof checker was the official `drat-trim` tree at source commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; the tracked source had no local
diff.  The executable SHA-256 was
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.

I freshly decompressed the hash-matched branch-0 CNF and DRAT into a new
temporary directory and replayed them with a $360$-second checker limit.  The
checker exited $0$ after $278.513$ seconds including decompression and
reported:

```text
c parsing input formula with 13160 variables and 429892 clauses
c detected empty clause; start verification via backward checking
c 34954 of 429892 clauses in core
c 295963 of 3299012 lemmas in core using 135152646 resolution steps
c 0 RAT lemmas in core
s VERIFIED
c verification time: 273.448 seconds
```

This current replay, rather than the exploratory finite-bank UNSAT label, is
the proof that branch 0 is UNSAT.

## Branches 1 and 2 and the budget-five dependency

I recomputed the current compressed identities and reran the independent
semantic checkers for both already-refereed exact-six branches:

| branch | fixed edge | CNF gzip SHA-256 | DRAT gzip SHA-256 | current semantic audit | prior fresh replay |
|---:|---|---|---|---|---|
| 1 | $(97,99)$ | `a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14` | `cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec` | PASS | `s VERIFIED` |
| 2 | $(98,99)$ | `c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06` | `c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9` | PASS | `s VERIFIED` |

The branch-1 proof package and its prior independent referee have SHA-256
`4a3e7b4c729f696ff304c5f71621e018786b552146784a2141529a4c6f028666`
and
`f70155f98a3b9c327e7031286e9fb92c0b4dea59377dfd62812d4664e84515b8`,
respectively.  The branch-2 record has SHA-256
`ee0c73b80407a4dd48ca69bd1a666f391bfd5729b9a56e062deef2a6f62018de`.
Those prior referees reconstructed the formulas and freshly replayed the
corresponding DRAT traces.  The current hashes match those reviewed proof
pairs, which is sufficient to reuse their checked conclusions here; this
review did not spend another replay cycle on branches 1 and 2.

The prior budget-five audit record has SHA-256
`cfde13c5957229168aaf12f23afc43018552a0707936a262836fbd9e573c8e9d`.
Its independent referee report has SHA-256
`961151173b4af656a83d6ff74d5de79f865d5cb0d17b0cdfc581bfae2d7a7711`
and documents fresh successful replays of all three budget-five DRAT
traces.  Hence the reduction from budget at most six to exact budget six has
a proof-checked dependency, not merely a stored Boolean label.

## Proof of the complete fixed-seed claim

Assume for contradiction that an eligible $F$ with $d_H(F)\leq6$ exists.
The budget-five proof gives $d_H(F)=6$.  Since $F$ is triangle-free, choose
an absent edge $f_i$ of the unique seed triangle.  Assign every primary
variable of branch $i$ according to $E(F)$.

All triangle clauses hold because $F$ is triangle-free.  The unit
$\neg x_{f_i}$ holds by the branch choice.  Exactly five other input edges
are absent, so the primary assignment extends to the exact-five sequential
counter.  Finally, $\alpha(F)<18$ implies that every installed 18-set has at
least one present pair, so every hitting clause holds.  Therefore the
assignment extends to a model of branch CNF $i$.

All three branch CNFs have complete checked UNSAT proofs.  This contradiction
excludes $F$.  Therefore no eligible repair has $d_H(F)\leq6$. $\square$

## Corrections and open risks

- **Non-blocking documentation warning.**  The author checker's returned
  machine field `seven_deletion_repair_exists: false` is a hard-coded
  false/default metadata value, not the output of an exact-seven search and
  not evidence of nonexistence.  It must not be interpreted as a proof that
  no exact-seven repair exists.  Its companion field
  `seven_deletion_repair_exists_is_established: false`, the author report,
  and the proof record state the warranted conclusion.  Canonical prose
  should use only the latter formulation.
- The remaining trust boundary is the standard proof-carrying SAT toolchain:
  PySAT's sequential-counter generator, the `drat-trim` kernel, the compiler,
  and hardware.  The matrix structure, formula clauses, mask transfer,
  hashes, gzip integrity, counter behavior, and proof replay were all checked
  independently at the customary level for a computer-assisted result.

## Explicit exclusions

This result does **not** establish any of the following:

- that a repair with exactly seven input-edge deletions exists;
- that no exact-seven repair exists;
- the exact deletion repair radius of the seed;
- a $100$-vertex triangle-free graph with independence number at most $17$;
- $R(3,18)\geq101$;
- a statement about other $100$-vertex seeds or arbitrary edit metrics.

The verified conclusion is precisely the local fixed-seed lower bound
$d_H(F)\geq7$ for any successful repair, with arbitrary original-nonedge
additions allowed.
