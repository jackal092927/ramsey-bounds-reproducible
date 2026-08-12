# Independent referee report: budget-nine non-star exclusion

Date: **2026-08-12**

## Verdict

**PASS**, for the following exact local claim:

> Let $G$ be the labeled 61-vertex graph in
> `r3_13_n61_nonstar_k11.txt`.  There is no graph $H$ on the same vertex set
> which is triangle-free, has no independent set of order 13, and omits at
> most nine edges of $G$, even when every nonedge of $G$ may be added.

Equivalently, a valid completion in this one fixed-seed edit family requires
at least ten input-edge deletions.  The audit does **not** establish that a
ten-deletion completion exists and does **not** prove any global bound on
$R(3,13)$.

The first non-combinatorial dependency boundary is the interpretation of the
frozen DIMACS files, in particular the standard PySAT sequential-counter
encoding of "at most seven".  Once the DIMACS files are fixed, their UNSAT
status no longer depends on Glucose or CaDiCaL: all three supplied traces were
rechecked directly by the pinned official `drat-trim` binary.

## Audited snapshot

```text
2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b  r3_13_n61_nonstar_k11.txt
992f75504d185de5ef901eb1e42a7c64897a2172a8f9b43508082786bd60b13d  BUDGET9_NONSTAR.md
c8914fc26a2a74cf69da4393193b7112bbff9a0b7fb5341dd64655615bcb91f4  budget9_nonstar.py
6ebb81dfa2545c0015f1337943e3109dc6965f29741bb6ea70c4af201d036f4e  budget9_nonstar.json
```

This review did not run or inspect a budget-ten search.

## 1. Structural reduction

I parsed the seed independently of `structural_decomposition`.  It has 61
vertices, 363 edges, and exactly the following eleven triangles:

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

The first ten contain $(28,60)$ and have distinct third vertices

$$
19,22,24,27,29,32,34,37,48,58.
$$

If $(28,60)$ is retained, triangle-freeness requires at least one deletion
from each pair

$$
\{(28,v),(60,v)\}.
$$

The ten pairs have a 20-edge disjoint union.  Thus they require ten distinct
input-edge deletions, and a budget-nine completion must delete $(28,60)$.
Additions cannot destroy any of these triangles.

After deleting the hub, the only input triangle left is $(37,46,60)$.
Consequently at least one of

$$
(37,46),\quad(37,60),\quad(46,60)
$$

must be absent.  The three branches are exhaustive; their overlap is harmless.
Each branch fixes the hub and one displayed edge.  An assignment with at most
nine total input-edge deletions therefore has at most

$$
9-2=7
$$

deletions among the other $363-2=361$ input edges.  If a solution deletes two
or all three edges of the residual triangle, those additional deletions are
charged by this residual-seven counter in every branch it realizes.

**Structural verdict: PASS.**

## 2. Frozen CNF semantics

I decoded every frozen CNF rather than relying only on the JSON metadata.
The variable map uses all

$$
\binom{61}{2}=1830
$$

unordered vertex pairs.  For each branch I found:

1. exactly all $\binom{61}{3}=35{,}990$ clauses
   $\neg x_{ab}\vee\neg x_{ac}\vee\neg x_{bc}$, in the expected pair-variable
   map;
2. a 5,303-clause sequential counter with 2,478 auxiliary variables and
   bound seven;
3. exactly the two claimed negative fixed-edge units; and
4. the branch-specific positive $I_{13}$ clauses.

The counter refers to all and only the 361 nonfixed input-edge variables.
None of the 1,467 original-nonedge variables occurs as a counted deletion.
Those variables are free to become edges subject only to triangle-freeness
and the $I_{13}$ hitting conditions.  Hence arbitrary additions are genuinely
allowed; this is not an add-only or delete-only encoding.

The DIMACS sizes are:

| branch | second fixed deletion | variables | clauses | residual budget |
|---:|---|---:|---:|---:|
| 0 | $(37,46)$ | 4,308 | 58,985 | 7 |
| 1 | $(37,60)$ | 4,308 | 59,412 | 7 |
| 2 | $(46,60)$ | 4,308 | 59,208 | 7 |

### Direction of the fixed-base $I_{13}$ relaxation

For each branch, I re-enumerated the independent 13-sets of the graph after
exactly its two fixed deletions using a reverse-order bitset recursion.  The
resulting sets, not merely their counts, agree exactly with the clauses in the
frozen CNF:

| branch | fixed-base $I_{13}$ sets | ordered-mask SHA-256 |
|---:|---:|---|
| 0 | 17,690 | `0741446d5bab4c2d3da749aa6e65da6c47249be2b208b368bf09f4632533ed2a` |
| 1 | 18,117 | `3a68a7a7812742962836e90a703d3887e348d86b5a5f51722ab8f2aeebe75e3c` |
| 2 | 17,913 | `8df0efefc8fd013a113c2c62d6da22abe1a3a4e64d3eb7372b882be77d552b82` |

Every such CNF clause has 78 positive edge literals.  Decoding those literals
always gives all pairs of one 13-vertex set, and that set contains no input
edge except possibly one of the two branch-fixed edges.  Thus the clause

$$
\bigvee_{\{u,v\}\in\binom S2}x_{uv}
$$

is necessary for every valid completion: without a true literal, $S$ is an
independent 13-set in the final graph.

Deleting further input edges can expose additional independent sets which
are absent from this bank.  Omitting their clauses makes the stored formula
**weaker** than the exact Ramsey problem.  The logical inclusion is

$$
\{\text{valid branch completions}\}
\subseteq
\{\text{models of the stored branch CNF}\}.
$$

Therefore UNSAT of the stored relaxation implies UNSAT of the exact branch.
The converse would not be valid, but it is not used.  All three proofs stop
with zero lazy clauses, so each checked trace is for precisely this weaker
fixed-base formula.

**Encoding-direction verdict: PASS.**

## 3. Artifact and proof verification

I recomputed both compressed and uncompressed hashes and checked the DIMACS
headers and line counts.  They agree with the JSON record.

| branch | compressed CNF SHA-256 | raw CNF SHA-256 | header |
|---:|---|---|---|
| 0 | `1ff3f8e90860a10ee7e3bfab072ec5af74ac268e0e6e8efe9b21cb1e3aedf081` | `af1f8fede0d41d8d99335054f747bc885a9519ae46b06c9745a8d99661442d70` | `p cnf 4308 58985` |
| 1 | `d67d588ff2abfbfc0c8c69e7a297c09e1871e09f94e2409813cd6f687166cf59` | `fcace1bce789b6bca23215c8e333dca8dbcd754f7998f9183525a530e7bfb0f3` | `p cnf 4308 59412` |
| 2 | `ce3bbeb80395d370efcc7c20cf3f70e8e0f49b9f3f863cc9e959e5ce62664193` | `401cc9a922f81362f3ae4a72797f7f6b95b4e9e4824ddca63d9410b09c946efc` | `p cnf 4308 59208` |

| branch | compressed DRAT SHA-256 | raw DRAT SHA-256 | proof lines |
|---:|---|---|---:|
| 0 | `2c47caa4cd9e508482711a7bb4f51873cd5dc2ec7c842795af87173b0f03a052` | `bd9e2c67319e92f96cd55e4077c731b3a2e619b352f3d46d54c8d8c69f79f666` | 115,583 |
| 1 | `5c884ee6087c207e53dc1f1f25f40f735ad90d7536378d9f45127855b1485f9c` | `a2e5f4fc7ff7420ff8a5e60d05a3d1bc9d2082d377dd3d9d28a69dd5d4ace4fa` | 71,609 |
| 2 | `ff48fccd97bdfbb8ae2a73492984e2ae8561d08b8746232ed12f3f92916a1760` | `b1918836525a0e5772fbaa95eb1f643812ca5d2776173d30d73a2a006c6986f8` | 107,569 |

The checker repository currently resolves to

```text
2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

and the invoked binary has SHA-256

```text
31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4
```

I independently decompressed and checked every pair.  All three runs exited
zero and printed `s VERIFIED`:

| branch | core input clauses | core lemmas | resolution steps | result |
|---:|---:|---:|---:|---|
| 0 | 8,321 | 36,052 | 12,701,516 | `VERIFIED` |
| 1 | 7,513 | 23,162 | 7,479,919 | `VERIFIED` |
| 2 | 7,863 | 31,532 | 10,415,683 | `VERIFIED` |

The gzip headers also have `mtime=0` as claimed.

### Bounded solver status is not the proof

The Glucose search reached an actual `UNSAT` response in every branch before
its global bound, and CaDiCaL independently returned `UNSAT` before its
parent-enforced wall limit.  CaDiCaL's bounded replay is useful corroboration
but supplies no proof object and is not needed for the conclusion.

More importantly, `budget9_nonstar.py` assigns global status
`UNSAT_PROOF_VERIFIED` only when all three branch statuses are `UNSAT` **and**
all three checker statuses are `VERIFIED`.  A solver limit becomes
`UNKNOWN_LIMIT`, and unchecked solver UNSAT becomes
`UNKNOWN_PROOF_UNCHECKED`.  Thus neither a timeout nor a merely bounded solver
response is promoted to proof.

**Proof-artifact verdict: PASS.**

## 4. Earliest dependency boundary

The audited implication can be separated into three layers.

1. **Direct finite combinatorics.**  The seed triangle list, forced hub
   deletion, three exhaustive branches, and residual budget seven were
   recomputed directly from the seed bytes.
2. **Problem-to-CNF semantics.**  Triangle clauses, fixed units, pair-variable
   coverage, free original-nonedge additions, and every $I_{13}$ clause were
   decoded independently.  The remaining imported semantic component is the
   correctness of PySAT's standard `CardEnc.atmost(..., EncType.seqcounter)`
   implementation as an at-most-seven counter.  Small-instance counter/SAT
   encodings are covered by the repository's exhaustive unit tests, but this
   review is not a formal verification of PySAT.
3. **CNF UNSAT.**  Given the exact frozen DIMACS bytes, the trust boundary is
   the pinned `drat-trim` implementation and ordinary execution integrity.
   Glucose and CaDiCaL are outside this final proof boundary because the DRAT
   traces are checked independently.

The finite-route test suite passed **13/13**, including complete small-graph
checks of the SAT encodings, fixed-deletion semantics, clique enumeration,
triangle transversals, and correct labeling of limited solver calls.

## Final conclusion

Every putative at-most-nine-deletion completion must delete the hub, lies in
at least one of the three residual-seven branches, and would induce a model of
that branch's stored necessary-condition relaxation.  The pinned DRAT checks
prove that none of those three formulas has a model.  The fixed-seed local
deletion lower bound of ten therefore follows. $\square$

No statement beyond this fixed labeled edit family is certified.
