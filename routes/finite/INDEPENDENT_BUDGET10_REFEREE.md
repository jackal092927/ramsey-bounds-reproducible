# Independent referee report: complete budget-ten non-star exclusion

Date: **2026-08-12**

## Verdict

```text
PASS
PROVABLE AS STATED
UNSAT_PROOF_INDEPENDENTLY_REPLAYED
```

The following exact local claim is supported:

> Let $G$ be the labeled 61-vertex graph in
> `r3_13_n61_nonstar_k11.txt`.  No graph $H$ on the same vertex set is
> triangle-free, has no independent set of order 13, and omits at most ten
> edges of $G$, even when every nonedge of $G$ may be added.

Equivalently, a successful completion in this **one fixed labeled edit
family** requires at least eleven input-edge deletions.  This does **not**
prove $R(3,13)\ge 62$, does not improve any global Ramsey-number bound, and
does not establish that an eleven-deletion completion exists.

## Audited snapshot

```text
2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b  r3_13_n61_nonstar_k11.txt
df2b9bc1d6c24c30d3eb1cf7dc44ae2d7c92ef2b979a7ddc2e597cceeb227eed  BUDGET10_SEARCH.md
a8f31f25013f870cbcb0523a37bd5539c688adcba185577b1c13931e89cbda33  budget10_search.py
1e145b262e96ac77ae3a6402b539bc523b80bf42569b11324c87df57ac46ef9b  budget10_search.json
```

I did not modify any of the frozen seed, CNF, DRAT, source, JSON, or search
report artifacts.

## 1. Independent structural reconstruction

I parsed the seed bytes independently of `structural_decomposition`.  The
matrix is symmetric with zero diagonal and has 61 vertices, 363 edges, and
exactly these eleven triangles:

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

Write $h=(28,60)$ and $T=(37,46,60)$.  The first ten triangles contain $h$.
Their third vertices are distinct, so their ten spoke pairs

$$
\{(28,v),(v,60)\},\qquad
v\in\{19,22,24,27,29,32,34,37,48,58\},
$$

have a pairwise-disjoint 20-edge union.

### Hub absent

If $h$ is absent, $T$ is the only surviving input triangle.  At least one of

$$
(37,46),\quad (37,60),\quad (46,60)
$$

must therefore be absent.  These are three exhaustive, possibly overlapping
branches.  The two fixed deletions leave at most $10-2=8$ deletions among the
other $363-2=361$ input edges.

### Hub retained

If $h$ is retained, every hub triangle requires a deletion from its own spoke
pair.  Ten pairwise-disjoint pairs consume the entire budget, so exactly one
edge is absent from every pair and no other input edge may be deleted.  The
only spoke edge of $T$ is $(37,60)$; hence that edge is forced absent, while
the other nine spoke pairs contribute exactly $2^9=512$ choices.

I also removed the $I_{13}$ clauses from frozen branch 3, projected all SAT
models to the 363 input-edge variables, and blocked projections one by one.
There were exactly **512 distinct projections**.  Every projection retained
$h$, deleted $(37,60)$, had exactly ten input-edge deletions, and chose exactly
one edge from every spoke pair.  This independently checks that the merged
branch neither samples nor omits a transversal.

**Structural verdict: PASS.**

## 2. Frozen CNF semantics

I decoded every frozen DIMACS file instead of relying on the JSON metadata.
The pair-variable map contains all

$$
\binom{61}{2}=1830
$$

unordered vertex pairs.  In every branch I found, in the documented order:

1. exactly all $\binom{61}{3}=35{,}990$ clauses
   $\neg x_{ab}\vee\neg x_{ac}\vee\neg x_{bc}$;
2. the sequential-counter clauses over all and only the nonfixed input-edge
   deletion literals;
3. exactly the claimed negative fixed-edge units;
4. the fixed-base $I_{13}$ hitting clauses; and
5. in branch 3, the positive unit retaining $h$.

The exact decoded sizes are:

| branch | case | residual input edges / bound | auxiliary variables | counter clauses | total variables | total clauses |
|---:|---|---:|---:|---:|---:|---:|
| 0 | $h=0,(37,46)=0$ | 361 / 8 | 2,824 | 5,993 | 4,654 | 59,675 |
| 1 | $h=0,(37,60)=0$ | 361 / 8 | 2,824 | 5,993 | 4,654 | 60,102 |
| 2 | $h=0,(46,60)=0$ | 361 / 8 | 2,824 | 5,993 | 4,654 | 59,898 |
| 3 | $h=1,(37,60)=0$ | 362 / 9 | 3,177 | 6,698 | 5,007 | 44,822 |

I independently instantiated the documented PySAT sequential counter from
the decoded residual-edge lists and bounds; every counter clause and auxiliary
identifier matched the frozen DIMACS bytes.  Direct SAT probes accepted zero
deletions and several dispersed assignments at the bound, and rejected
assignments with one deletion above the bound.

All 1,467 input nonedges have ordinary edge variables, none occurs as an
input to the deletion counter, and none is fixed absent merely for being an
input nonedge.  They may therefore be added freely, subject only to the
triangle and $I_{13}$ conditions.  Thus the formulas really do cover
**arbitrary additions**, not an add-only or delete-only surrogate.

### Fixed-base $I_{13}$ clauses

I decoded every positive 78-literal clause into its unique 13-vertex set.
Each clause consists of all $\binom{13}{2}=78$ pair variables on that set,
has no duplicate literal, and its set contains no nonfixed input edge.  A
separate high-vertex-first bitset recursion re-enumerated the fixed-base
independent sets; the sets agreed exactly with the decoded banks:

| branch | fixed-base $I_{13}$ clauses | ordered-mask SHA-256 |
|---:|---:|---|
| 0 | 17,690 | `0741446d5bab4c2d3da749aa6e65da6c47249be2b208b368bf09f4632533ed2a` |
| 1 | 18,117 | `3a68a7a7812742962836e90a703d3887e348d86b5a5f51722ab8f2aeebe75e3c` |
| 2 | 17,913 | `8df0efefc8fd013a113c2c62d6da22abe1a3a4e64d3eb7372b882be77d552b82` |
| 3 | 2,132 | `846c46b160147aa185b7139168916c5551303cc2d34774636e9aec04e2f1be17` |

For any decoded set $S$, a final graph with no independent 13-set must satisfy

$$
\bigvee_{\{u,v\}\in\binom S2}x_{uv}.
$$

Further input-edge deletions can expose additional independent sets that are
not in the bank.  Omitting those clauses makes the stored CNF **weaker** than
the exact completion problem:

$$
\{\text{valid branch completions}\}
\subseteq
\{\text{models of the stored branch CNF}\}.
$$

Consequently checked UNSAT of the stored relaxation is sufficient.  No claim
requires the converse implication.  In fact, completeness of the bank is not
needed for soundness; each installed clause only has to be necessary.  The
independent re-enumeration is an additional consistency check.

**Encoding and relaxation-direction verdict: PASS.**

## 3. Artifact hashes and proof replay

I recomputed compressed and uncompressed hashes, gzip integrity and `mtime=0`,
DIMACS headers, line counts, and formula sizes.  All agree with the JSON.

| branch | compressed CNF SHA-256 | raw CNF SHA-256 | DIMACS header |
|---:|---|---|---|
| 0 | `6c5d66602bf62e60fd084efc05c59908c33d274571bbf03b93b6b0b63733d6a7` | `eee128f559d7609781d7fdfa71eb85521d8ca60a12ef2f607c8253aa9955733c` | `p cnf 4654 59675` |
| 1 | `1a6f6955a3a04001d8bfbe56e69ac19ddf6b8dd5cf7ca2bc119469379820dddf` | `0a47b503e242cb7eda077b06113eb78fd02acbb807835461ae012b94b40aabd5` | `p cnf 4654 60102` |
| 2 | `290322f089f5ec09f4cf0023c91a6745eec2e62da5385874c73520a7bea4cce5` | `e590bad31a889c8240b520ac823c5d64de906aac21b6964fbe9566a71494533a` | `p cnf 4654 59898` |
| 3 | `363e02620d93e7f12a5ac12f55b80484d31b31541d8512297126b2911ace60fc` | `4d688c2e502c2cbef52c19ba23d0626b51745b389468080343b28f1e48830a85` | `p cnf 5007 44822` |

| branch | compressed DRAT SHA-256 | raw DRAT SHA-256 | proof lines |
|---:|---|---|---:|
| 0 | `affcb39fb5c0eb272fbdc6bd26aff5dd10b61f34c5c4e84b6c34c95ef16c1447` | `a4c741b0f3e1dcc24ddf6aeb664e3060a5c23074af1443af6a459329ecdc1684` | 410,743 |
| 1 | `c0eeb889f47115339be9c6f631a4f86bf264408c33a1dc33f646bec7cd425868` | `f88761c934e8f822719dc35f36e33e4c10f441858d12ee8c7379b18f4aa932b2` | 332,352 |
| 2 | `fd5bd7cee9e1d02d50235046f45654220b07dfa3cf45dfdbc770ee13db950fcb` | `a4ba5575e85f044bc81dba80b2f055994c6a7b1cea89bea5fa641b518be3a40d` | 489,033 |
| 3 | `c7c9767328ff35bf71765d0578dd9a0e3dbd685ff49e894e7aa0d638b5d016c2` | `b1de156d0b5a423a1087d1e1679923e7b29f7090a6c0b66bfc164b7aaf49740a` | 276 |

The local checker checkout has origin
`https://github.com/marijnheule/drat-trim.git`, tracked source at commit

```text
2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

with no tracked-source diff.  The invoked binary SHA-256 is

```text
31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4
```

I independently decompressed and replayed **all four** CNF/DRAT pairs.  Every
run exited zero and printed `s VERIFIED`:

| branch | core input clauses | core lemmas | resolution steps | result |
|---:|---:|---:|---:|---|
| 0 | 9,663 | 146,804 | 53,816,381 | `VERIFIED` |
| 1 | 9,026 | 122,438 | 43,359,826 | `VERIFIED` |
| 2 | 9,997 | 176,598 | 69,074,887 | `VERIFIED` |
| 3 | 1,296 | 85 | 16,277 | `VERIFIED` |

The JSON records actual Glucose `UNSAT`, CaDiCaL 1.9.5 `UNSAT`, and checked
DRAT `VERIFIED` for every branch.  Glucose used respectively 210,556,
165,575, 260,394 and 207 conflicts; CaDiCaL used 428,863, 291,665, 483,216
and 317 conflicts.  Every branch has zero lazy cuts.  The top-level status is
`UNSAT_PROOF_VERIFIED`, while `global_ramsey_claim` is correctly `null`.

CaDiCaL is corroborating evidence, not the final proof object.  Given the
frozen DIMACS bytes, the four checked DRAT refutations establish UNSAT without
trusting either solver's bare status.

**Proof-artifact verdict: PASS.**

## 4. Limit handling and minimal tests

The runner promotes the result to `UNSAT_PROOF_VERIFIED` only when all four
branches return `UNSAT` and all four trace checks return `VERIFIED`.  A bounded
solver failure becomes `UNKNOWN_LIMIT`; unchecked solver UNSAT becomes
`UNKNOWN_PROOF_UNCHECKED`.  Therefore no timeout or incomplete branch is used
as a proof.

The repository does not install `pytest`, so I invoked the two finite-route
test modules directly through `unittest`.  All **16/16** tests passed.  They
include complete small-graph checks of clique enumeration, Ramsey SAT
encodings, bounded deletion semantics, triangle transversals, conditional
cuts, and limited-solver status handling.

## 5. Earliest dependency boundary

The implication separates into the following layers:

1. **Finite combinatorics.**  The matrix shape, edge count, eleven triangles,
   hub split, three absent-hub branches, and exact 512-way retained-hub merge
   were independently reconstructed from the seed bytes.
2. **Problem-to-CNF semantics.**  All pair variables, all triangle clauses,
   fixed units, uncounted original-nonedge additions, and every installed
   $I_{13}$ clause were decoded directly.  The earliest imported encoding
   dependency left at this layer is the correctness of PySAT 1.9.dev13's
   standard `CardEnc.atmost(..., EncType.seqcounter)` semantics.  Exact clause
   regeneration and boundary SAT probes corroborate it, but this review is
   not a formal verification of PySAT.
3. **Frozen-CNF UNSAT.**  Given the decoded DIMACS files, the remaining proof
   dependency is the pinned `drat-trim` implementation and ordinary execution
   integrity.  Glucose and CaDiCaL are outside this final proof boundary
   because the traces were checked separately.

## Final conclusion

Every putative at-most-ten-deletion completion lies in one of the three
hub-absent residual-eight branches or in the exact merged hub-retained branch.
Its edge assignment would satisfy the corresponding stored
necessary-condition relaxation.  The four independently replayed DRAT
refutations prove that none of those formulas has a model.  Therefore every
valid completion in this fixed labeled seed family requires at least eleven
input-edge deletions. $\square$

No statement beyond this fixed-seed edit family is certified.
