# Independent referee: $R(3,18)$ exact-budget-six branch 1

Date: 2026-08-12  
Scope: the frozen branch-1 CNF and DRAT package only

## Verdict

```text
frozen 100-vertex seed identity and structure:       PASS
prior deletion-budget <=5 dependency:                PASS, imported from the pinned refereed package
branch index and exact-six edit semantics:            PASS
arbitrary original-nonedge additions:                 PASS
CNF reconstructed independently clause by clause:    PASS
cut-bank masks and implication direction:             PASS
compressed/raw CNF and DRAT identities:               PASS
fresh root-session DRAT replay:                       PASS, exit 0 and s VERIFIED
exact-budget-six branch 1 conclusion:                 PROVABLE AS STATED
exact-budget-six branch 0:                            UNKNOWN
complete fixed-seed budget <=6 ball:                  UNKNOWN
R(3,18) >= 101:                                       NOT ESTABLISHED
```

The frozen artifacts prove exactly this scoped claim:

> Let $H$ be the pinned $100$-vertex graph with SHA-256
> `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
> There is no final graph obtained by fixing the input edge $(97,99)$ absent,
> deleting exactly five further input edges of $H$, and adding an arbitrary
> subset of the original nonedges, which is both triangle-free and has no
> independent set of size $18$.

This branch-1 statement is **PROVABLE AS STATED**. Together with the earlier
proof for branch 2, it leaves branch 0 as the sole unresolved exact-six
branch. It does not prove the complete fixed-seed deletion-budget-six
exclusion, a fixed-seed repair radius of at least seven, a $100$-vertex
$(3,18)$ Ramsey graph, or $R(3,18)\ge101$.

## Frozen snapshot and hashes

I reviewed the following exact artifacts:

```text
e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e  certificates/r3_18_n100_nearmiss.txt
1a6c1323bc6d90773bd95c1c6eb72c4f0f18d4461e392b9b76439e6a4719491c  R3_18_BUDGET6_BRANCH1_PROOF.md
47da14a1b13d32379c2396b19992b9edf58ea21a2621d9f6f8d895416347b16b  check_r3_18_budget6_branch1.py
a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14  r3_18_budget6_branch_1.cnf.gz
f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c  r3_18_budget6_branch_1.cuts.json
cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec  r3_18_budget6_branch_1.drat.gz
010885ff86f45db8b7d34ebbe22a9025f3136660a516762c5296ab470486480c  r3_18_budget6_branch_1_check.json
4a3e7b4c729f696ff304c5f71621e018786b552146784a2141529a4c6f028666  r3_18_budget6_branch_1_proof.json
```

The uncompressed identities independently recovered during the semantic and
artifact audit are

```text
CNF raw SHA-256:   ced3fd39370b4c2552cb261638fb7076da173e18d6b871f6fb280668e5a1154a
CNF raw bytes:     47,089,599
CNF raw lines:     242,065 including the header
DRAT raw SHA-256:  fbf7292c3bcbf52ec6f978fca0751d319e2e2029380e7a865a17430baf282902
DRAT raw bytes:    2,137,671,968
DRAT raw lines:    5,590,150
```

Both final gzip files pass `gzip -t`. The earlier interrupted proof at
`incomplete/r3_18_budget6_branch_1.partial.drat.gz` has SHA-256
`dcdb695a11c21e473b9a715ba8048f68066f6a49c5a960809e05ad973820f38b`,
fails `gzip -t` with unexpected EOF, and was not used as evidence.

## Dependency map

The scoped conclusion depends on the following chain.

1. The pinned matrix has $100$ vertices, $827$ input edges, the unique
   triangle $(97,98,99)$, and no independent $18$-set.
2. The earlier proof-carrying package excludes every eligible repair of this
   same seed using at most five input-edge deletions, while permitting
   arbitrary original-nonedge additions.
3. Therefore a previously uncovered candidate in the deletion-budget-six
   ball would delete exactly six input edges.
4. The unique triangle gives three covering branches. Branch 1 fixes the
   second lexicographic triangle edge, $(97,99)$, absent. Its residual
   counter must therefore encode exactly five deletions among the other
   $826$ input edges.
5. Every eligible branch-1 graph extends to a model of the frozen finite CNF.
6. The hash-matched DRAT trace, freshly replayed against that CNF, proves it
   UNSAT. Hence no eligible branch-1 graph exists.

The chain does not contain a premise closing branch 0.

## Independent seed and branch reconstruction

I parsed the matrix directly. It is a symmetric $100\times100$ binary matrix
with zero diagonal and $827$ edges. Exhaustive enumeration of all
$\binom{100}{3}=161700$ triples gives the single triangle

$$
(97,98,99).
$$

The exact graph verifier rerun in this review found no independent set of
size $18$. The independent semantic reconstruction did not trust a stored
triangle list or edge count.

Lexicographic enumeration of the three triangle edges gives

$$
\bigl((97,98),(97,99),(98,99)\bigr).
$$

Thus branch index $1$ is exactly the fixed absent edge $(97,99)$, whose
primary variable is $x_{97,99}=x_{4949}$. The three branches cover every
triangle-free final graph, although they need not be disjoint. If several
triangle edges are absent, the graph belongs to several branches; this does
not affect coverage.

## Why exact five residual deletions is correct

Let $E(H)$ be the $827$ input edges and let $F$ be a final graph. The local
deletion budget is

$$
d(F)=|E(H)\setminus E(F)|.
$$

The pinned earlier package proves that no eligible repair has $d(F)\le5$.
That dependency is recorded in
`r3_18_extension_repair_check.json`, SHA-256
`cfde13c5957229168aaf12f23afc43018552a0707936a262836fbd9e573c8e9d`,
and its independent referee report has SHA-256
`961151173b4af656a83d6ff74d5de79f865d5cb0d17b0cdfc581bfae2d7a7711`.
That prior review reconstructed all three budget-five formulas and freshly
replayed all three DRAT traces to `s VERIFIED`.

Consequently any new graph with $d(F)\le6$ must have $d(F)=6$. In branch 1,
the unit $\neg x_{97,99}$ accounts for one deletion. The correct residual
equality is

$$
\sum_{e\in E(H)\setminus\{(97,99)\}}(1-x_e)=5.
\tag{1}
$$

There are exactly $826$ literals in (1). Original nonedges do not occur in
this sum. They retain primary final-edge variables and can be added or not
added freely, subject only to the final triangle and independent-set
requirements.

## Clause-by-clause CNF reconstruction

I reconstructed the formula independently rather than relying on its DIMACS
header or discovery checkpoint.

### Primary and auxiliary variables

For every unordered pair $0\le u<v<100$, the primary variable $x_{uv}$
means that $(u,v)$ is present in the final graph. Lexicographic pair order
uses variables $1,\ldots,4950$.

A fresh PySAT `CardEnc.equals` call with `EncType.seqcounter`, the exact
ordered list

$$
[-x_e:e\in E(H)\setminus\{(97,99)\}],
$$

and bound $5$ reproduces all $16420$ stored counter clauses in order. It
introduces $8210$ auxiliary variables and ends at variable $13160$.

As a separate semantic probe, I fixed all $826$ deletion literals to
assignments with deletion counts

$$
0,1,4,5,6,7,825,826.
$$

An independent SAT backend extended the counter auxiliaries if and only if
the count was exactly five.

### Triangle block

For every $a<b<c$, the first $161700$ clauses are exactly

$$
\neg x_{ab}\lor\neg x_{ac}\lor\neg x_{bc}.
\tag{2}
$$

I regenerated and compared every literal in order. These clauses impose
triangle-freeness on the final graph, including triangles created by added
original nonedges.

### Fixed branch unit

Immediately after the counter, the next clause is

$$
\neg x_{97,99}.
\tag{3}
$$

The fixed edge is excluded from the residual counter, so (1) and (3) encode
six distinct input-edge deletions in total.

### Independent-$18$ hitting clauses

The remaining $63943$ clauses are all distinct. Each consists of exactly
$153=\binom{18}{2}$ positive primary literals. For every clause, I recovered
an $18$-vertex set $S$ and checked literal-for-literal that the clause is

$$
\bigvee_{e\in\binom S2}x_e.
\tag{4}
$$

No auxiliary variable or negative literal occurs in this block. Its masks
agree in stored order with `r3_18_budget6_branch_1.cuts.json`; every mask has
popcount $18$, all masks are unique, and their deterministic ordered digest
is

```text
99b72cd5500c6140d4aca261a1028b9805b9d8209ffc3216596a0fb8fb50edcf
```

The bank need not contain every $18$-set. Every graph with no independent
$18$-set satisfies (4) for every installed $S$. Thus the finite formula is a
relaxation of the exact branch. UNSAT of the relaxation implies UNSAT of the
exact branch; the logical direction is correct.

### Formula accounting

| block | clauses |
|---|---:|
| all triangle clauses | 161,700 |
| exact-five sequential counter | 16,420 |
| fixed negative unit | 1 |
| installed $I_{18}$ hitting clauses | 63,943 |
| **total** | **242,064** |

The reconstructed maximum variable is $13160$, and the frozen header is
exactly `p cnf 13160 242064`. There are no trailing or missing clauses.

## Artifact audit and fresh DRAT replay

I reran `check_r3_18_budget6_branch1.py` without a proof checker. It
independently reconstructed the same semantic blocks and decompressed the
complete proof, returning
`BRANCH1_EXACT_BUDGET6_ARTIFACT_AUDITED_NOT_REPLAYED`. In particular, it
confirmed both compressed hashes and the raw CNF/DRAT hashes, byte counts,
and line counts quoted above.

The status of `r3_18_budget6_branch_1_check.json` is intentionally also
`ARTIFACT_AUDITED_NOT_REPLAYED`; that JSON is semantic and identity evidence,
not evidence of a DRAT replay. I do not upgrade that record's status.

Separately, during this referee pass the root agent freshly ran

```text
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --drat-trim /private/tmp/ramsey-drat-trim-2e3b2dc/drat-trim \
  --drat-seconds 300
```

against the same hash-pinned files. I independently checked the supplied
`drat-trim` executable hash:

```text
31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4
```

The fresh root-session replay, which is distinct from my semantic-only
checker run, reported

```text
13,160 variables; 242,064 input clauses
34,973 input clauses in the core
511,535 of 2,789,684 lemmas in the core
209,897,525 resolution steps
0 RAT lemmas in the core
s VERIFIED
exit code 0
elapsed 192.686 seconds including decompression
verification time 189.547 seconds
```

No solver `UNSAT` label is being promoted without a proof check. The
CaDiCaL generation binary also still matches its recorded SHA-256, but its
correctness is not needed after successful DRAT verification.

## Proof of the scoped conclusion

Assume that an eligible branch-1 graph $F$ exists. Assign every primary
variable according to $E(F)$. Triangle-freeness satisfies every clause (2).
Exact total deletion count six and the fixed absent edge make the residual
sum (1) equal five, so the standard sequential counter admits auxiliary
values satisfying its clauses. The branch assumption satisfies (3). Since
$F$ has no independent $18$-set, it satisfies every installed clause (4).

Therefore the primary assignment extends to a model of the frozen CNF. The
freshly verified DRAT trace proves that this CNF is UNSAT, a contradiction.
The scoped branch-1 exclusion follows. $\square$

## Result-to-claim gate

- `claim_supported`: **yes**, for the exact branch-1 statement above.
- `what_results_support`: branch 1, fixing $(97,99)$ absent with exactly five
  additional input-edge deletions and arbitrary original-nonedge additions,
  is UNSAT.
- `what_results_dont_support`: exclusion of branch 0, exclusion of the full
  fixed-seed budget-six ball, a fixed-seed radius-seven theorem, existence or
  nonexistence of any unrelated $100$-vertex graph, or $R(3,18)\ge101$.
- `missing_evidence`: a separated graph or a checked UNSAT proof for branch
  0 is still required for any full exact-six conclusion.
- `suggested_claim_revision`: no revision to the scoped branch-1 claim;
  retain the explicit fixed-seed, fixed-branch, and exact-budget qualifiers.
- `next_experiments_needed`: continue branch 0 only if seeking to close this
  fixed-seed budget-six ball.
- `confidence`: **high** for branch 1; the overall exact-six problem remains
  `UNKNOWN`.

## Current global boundary

The prior branch-2 CNF/DRAT pair remains independently verified. The current
three-branch state is therefore

| branch | fixed input edge absent | status |
|---:|---|---|
| 0 | $(97,98)$ | `UNKNOWN` |
| 1 | $(97,99)$ | `UNSAT`, this report |
| 2 | $(98,99)$ | `UNSAT`, previously verified |

Accordingly, **this report must not be cited as proving
$R(3,18)\ge101$**. The already-known $R(3,18)\ge100$ certificate is unchanged;
the new result is a local exact-branch exclusion around one frozen near miss.
