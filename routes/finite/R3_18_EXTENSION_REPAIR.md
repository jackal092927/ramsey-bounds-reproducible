# R(3,18) single-point extension and budget-five repair audit

## Claim

Let $G_0$ be the frozen $99$-vertex graph in
`certificates/alphaevolve_R3_18_ge_100.txt`, and let $H$ be the frozen
$100$-vertex near miss in `certificates/r3_18_n100_nearmiss.txt`.

1. $G_0$ is triangle-free and has no independent set of size $18$, so it
   certifies the already-known lower bound $R(3,18)\geq 100$.
2. $H$ has no independent set of size $18$ and has exactly one triangle,
   $\{97,98,99\}$.
3. There is no triangle-free, independent-$18$-free graph obtained from $H$
   by deleting at most five edges of $H$, even if arbitrarily many nonedges
   of $H$ may simultaneously be added.

The third claim is a statement about one fixed edit ball. It does **not**
exclude other $100$-vertex graphs and does **not** improve a global Ramsey
bound.

## Status

**PROVABLE AS STATED (proof-carrying finite computation).**

The stronger claims “$R(3,18)=100$” and “$R(3,18)\geq101$” are **NOT
CURRENTLY JUSTIFIED** by this route.

## Frozen inputs

| object | vertices | edges | SHA-256 |
|---|---:|---:|---|
| $G_0$ | 99 | 809 | `3e9d16e29111f3a2f25ae3b992235804c2612de2f6ada5570901d17ceedfca45` |
| $H$ | 100 | 827 | `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e` |

The first $99$ vertices of $H$, after discarding their bit for vertex $99$,
are exactly $G_0$. Vertex $99$ has neighborhood

$$
\{33,34,\ldots,48,97,98\}.
$$

The only base edge induced by this neighborhood is $(97,98)$, hence the
displayed single-point extension has one triangle conflict.

## Assumptions and encoding

- Vertices are $0,\ldots,99$.
- For every unordered pair $e$, $x_e=1$ means that $e$ is present in the
  final graph.
- Every triple has the clause $\neg x_{ab}\lor\neg x_{ac}\lor\neg x_{bc}$.
- In the branch fixing input edge $f$ deleted, the unit clause $\neg x_f$ is
  present. Thus a deleted branch edge cannot be silently re-added.
- A sequential counter applies only to the other $826$ input edges and
  permits at most four of their literals to be false.
- Variables for original nonedges are absent from that counter, so additions
  are unrestricted.
- For every selected $18$-set $S$, the formula contains

$$
\bigvee_{e\in \binom{S}{2}}x_e.
$$

  This is a necessary clause for every graph with no independent set of size
  $18$. A finite subset of these clauses is therefore a relaxation of the
  exact problem; UNSAT of that relaxation is sufficient for branch UNSAT.

## Proof strategy and dependency map

1. Independent bitset search verifies the frozen matrices.
2. The unique input triangle gives an exhaustive three-case split according
   to which one of its edges is absent in the final triangle-free graph.
3. Each branch CNF expresses triangle-freeness, its fixed deletion, at most
   four additional input-edge deletions, arbitrary input-nonedge additions,
   and a finite bank of necessary $I_{18}$-hitting clauses.
4. The minimal checker reconstructs every structural CNF prefix and verifies
   that every remaining clause is exactly all $153$ edge variables of an
   $18$-set.
5. A DRAT proof verified by the pinned official checker proves each finite CNF
   UNSAT.
6. Exhaustiveness of the three cases proves the fixed-seed budget-five claim.

## Proof

### Step 1: matrix facts

`verify_ramsey.py` reports for $G_0$:

- no $K_3$ (66 recursive search nodes);
- no $I_{18}$ (1,521,239 recursive search nodes);
- a $K_2$ and an $I_{17}$, hence $\omega(G_0)=2$ and
  $\alpha(G_0)=17$.

Thus $G_0$ is a valid $99$-vertex $(3,18)$ Ramsey graph and proves
$R(3,18)\geq100$.

For $H$, the same bitset verifier finds no $I_{18}$ (1,990,791 recursive
nodes). Direct triangle enumeration returns only $\{97,98,99\}$. Therefore
$H$ is a near miss rather than a Ramsey certificate.

The exact one-vertex extension CEGAR calculation on the unmodified base
returns UNSAT after 2,748 iterations and 2,747 discovered $I_{17}$ clauses.
This proves that $G_0$ has no direct triangle-free/$I_{18}$-free one-vertex
extension. The statement remains restricted to this labeled base.

### Step 2: exhaustive branch reduction

Suppose that a final graph $F$ in the stated edit ball is triangle-free.
Since all three edges $(97,98)$, $(97,99)$, and $(98,99)$ are present in $H$,
at least one is absent in $F$. Consequently $F$ belongs to one or more of the
following exhaustive branches:

1. $x_{97,98}=0$;
2. $x_{97,99}=0$;
3. $x_{98,99}=0$.

One deletion is fixed in each branch, leaving at most four additional input
edge deletions. Overlap between branches is harmless because only coverage is
needed.

### Step 3: branch formula semantics

The independent checker reconstructs all three stored DIMACS files. Each has
8,238 variables, consisting of 4,950 edge variables and 3,288 sequential-
counter auxiliaries. In every branch it verifies, in order:

- exactly 161,700 triangle clauses, one for each triple;
- exactly 7,394 sequential-counter clauses encoding at most four deletions
  among the 826 non-fixed input edges;
- the negative unit for the fixed triangle edge;
- every remaining clause is 153 distinct positive edge literals and those
  literals are exactly $\binom{S}{2}$ for an $18$-vertex set $S$.

The branch sizes are:

| fixed absent edge | $I_{18}$ clauses | total clauses | DIMACS gzip SHA-256 |
|---|---:|---:|---|
| $(97,98)$ | 287 | 169,382 | `d64f009f840597e266ccfb3b31c88f7e87eb760d1fc551b7ee08a0854749ba66` |
| $(97,99)$ | 15,872 | 184,967 | `d6d321a4ac1aeec5e99c48843a8cda9395271e89555cea328e29bcda4e70ef15` |
| $(98,99)$ | 8,704 | 177,799 | `8d8a543bb3cc17014941fee432673a1dc2b99c8cb4885d4d91bba9005f3b10a7` |

Every exact solution in a branch satisfies every displayed clause, so it
satisfies the corresponding stored finite CNF.

### Step 4: checked UNSAT proofs

The official `drat-trim` executable built from pinned commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985` has SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
It was rerun independently on every frozen DIMACS/DRAT pair and printed
`s VERIFIED` in all cases:

| fixed absent edge | DRAT gzip SHA-256 | independent check |
|---|---|---|
| $(97,98)$ | `60687241833df8ae957b3b4fcb02e6e9f7595c6e3dcbee8b77f02dad5443f913` | VERIFIED |
| $(97,99)$ | `33a9e037e19beeab8dd2af4dca5ce9010d4906b39dc3e5cc8fd62823f518497a` | VERIFIED |
| $(98,99)$ | `159865da9ad23eea298ebd4e9406f2f37ecc6015a593975e9d63e3b08a859897` | VERIFIED |

Thus every branch CNF is UNSAT. Step 3 shows that a graph satisfying the
branch edit semantics would satisfy that CNF, and Step 2 shows that every
triangle-free graph in the full budget-five edit ball lies in a branch.
Therefore no such triangle-free/$I_{18}$-free graph exists. $\square$

## Search-state ledger

The following non-proof-carrying runs are retained only as search provenance:

- full arbitrary-addition CEGAR budgets $1,2,3,4,5$: solver status UNSAT;
  budget $5$ took 1,735 iterations and 575.24 seconds in CaDiCaL;
- the analogous Glucose budget-$5$ search: TIME_LIMIT after 600.62 seconds;
- full budget $6$: TIME_LIMIT after 902.05 seconds and 3,103 cuts.

The checked three-branch proof above, rather than these exploratory statuses,
supports the final fixed-seed conclusion. Budget $6$ remains UNKNOWN.

## Reproduction

Run the small primitive tests:

```bash
.venv/bin/python -m routes.finite.test_r3_18_budget5_branch
```

Reconstruct all formula semantics and rerun all three proofs:

```bash
.venv/bin/python routes/finite/check_r3_18_extension_repair.py \
  --artifact-dir routes/finite \
  --drat-trim /path/to/pinned/drat-trim \
  --drat-seconds 120 \
  --json routes/finite/r3_18_extension_repair_check.json
```

The frozen machine-readable result is
`r3_18_extension_repair_check.json`, SHA-256
`cfde13c5957229168aaf12f23afc43018552a0707936a262836fbd9e573c8e9d`.

## Claim boundary and open risks

- **Established:** the 99-point certificate; the exact properties of the
  frozen near miss; and fixed-seed repair-ball UNSAT for deletion budget five
  with arbitrary additions.
- **Not established:** nonexistence of a 100-point Ramsey graph; a new upper
  bound; a 100-point Ramsey certificate; or $R(3,18)\geq101$.
- **OPEN:** repair budget six and higher, other one-point neighborhoods after
  modifying the base, and graph families not isomorphic to this seed.
- Proof replay needs the pinned `drat-trim`; absolute `/tmp` tool paths in run
  JSON are provenance, not permanent dependencies. Matrices, CNFs, DRATs,
  scripts, and hashes are frozen in this directory.
