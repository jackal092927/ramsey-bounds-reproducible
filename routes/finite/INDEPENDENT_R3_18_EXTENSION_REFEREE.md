# Independent referee audit: the frozen $R(3,18)$ extension-repair package

## Verdict

**PASS — PROVABLE AS STATED.**

The frozen package proves the following three claims:

1. the $99$-vertex graph $G_0$ is triangle-free and has independence
   number $17$, hence it certifies the already-known bound
   $R(3,18)\geq 100$;
2. the frozen $100$-vertex graph $H$ has no independent set of size $18$
   and has exactly one triangle, $\{97,98,99\}$;
3. no graph obtained from this **fixed** $H$ by deleting at most five of
   its input edges and adding an arbitrary subset of its input nonedges can
   be both triangle-free and independent-$18$-free.

The claim survives unchanged.  In particular, the package does **not**
prove $R(3,18)\geq 101$, does not prove $R(3,18)=100$, and does not exclude
other $100$-vertex constructions.

## Scope and method

I treated the matrices, three DIMACS files, and three DRAT traces as frozen
artifacts.  I did not regenerate or modify any of them.  The audit comprised:

1. direct parsing and structural inspection of both adjacency matrices;
2. rerunning the exact graph verifier and checking its search invariant;
3. reconstructing all three CNF prefixes clause by clause from the frozen
   near miss;
4. checking the case split and all edit-budget quantifiers independently;
5. recomputing compressed and uncompressed hashes;
6. replaying every DRAT trace twice: once through the package checker and
   once through a freshly compiled checker from the pinned source commit.

## 1. Matrix reconstruction

The independently parsed matrices are symmetric, have zero diagonal, and
have the following frozen hashes and properties.

| graph | SHA-256 | vertices | edges | triangles | $I_{18}$ |
|---|---|---:|---:|---|---|
| $G_0$ | `3e9d16e29111f3a2f25ae3b992235804c2612de2f6ada5570901d17ceedfca45` | 99 | 809 | none | none |
| $H$ | `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e` | 100 | 827 | exactly $\{97,98,99\}$ | none |

The first $99\times99$ principal block of $H$ is entry-for-entry identical
to the adjacency matrix of $G_0$.  The new vertex has neighborhood

$$
N_H(99)=\{33,34,\ldots,48,97,98\}.
$$

Within this neighborhood the only edge of $G_0$ is $(97,98)$, which gives
the unique extension triangle.  The exact verifier also finds an
independent $17$-set in $G_0$, so the two negative searches imply
$\alpha(G_0)=17$ rather than merely $\alpha(G_0)<18$.

For a code-level adversarial check of the negative clique search, I compared
its answer with literal subset enumeration on 8,640 small random
graph/target instances; every result and every returned witness agreed.
This supplements, but does not replace, inspection of its greedy-color
upper-bound invariant.

## 2. Exhaustiveness of the three branches

Let $F$ be a triangle-free final graph in the claimed edit ball.  All three
edges

$$
(97,98),\qquad(97,99),\qquad(98,99)
$$

belong to $H$.  Since $F$ cannot retain their triangle, at least one of the
three is absent in $F$.  Therefore every eligible $F$ lies in at least one
of the three stored branches.  Branch overlap is immaterial: the argument
needs coverage, not a disjoint partition.

In a branch, one input edge is fixed absent and the counter permits at most
four further input-edge deletions.  Consequently the branch contains every
eligible final graph with at most five total input-edge deletions.  The split
does not assume that the other two triangle edges remain present.

## 3. CNF semantics

For each branch I reconstructed the variables and clauses in their stored
order.  Every formula has:

- $4,950=\binom{100}{2}$ final-edge variables $x_e$;
- $161,700=\binom{100}{3}$ clauses
  $\neg x_{ab}\lor\neg x_{ac}\lor\neg x_{bc}$, one per vertex triple;
- a sequential-counter encoding of

  $$
  \sum_{e\in E(H)\setminus\{f\}}(1-x_e)\leq4;
  $$

- the negative unit clause $\neg x_f$ for the branch edge $f$;
- a finite set of clauses $\bigvee_{e\in\binom S2}x_e$, each consisting of
  exactly the $153$ distinct pair variables of an $18$-vertex set $S$.

There are $827$ input edges in $H$.  Removing the fixed branch edge leaves
exactly $826$ literals in the deletion counter.  Original nonedges of $H$
are edge variables but never occur as counted deletion literals.  Hence
their addition is genuinely unrestricted.  The fixed edge is constrained by
the negative unit outside the counter, so it cannot be silently re-added.

The $18$-set clauses need not form the complete bank.  Every exact
independent-$18$-free graph satisfies every such clause, so a stored finite
bank yields a relaxation of the exact problem.  UNSAT of this relaxation is
therefore sufficient for UNSAT of the exact branch; the implication is in
the required direction.

The reconstructed sizes are:

| fixed absent edge | variables | triangle clauses | counter clauses | $I_{18}$ clauses | total clauses |
|---|---:|---:|---:|---:|---:|
| $(97,98)$ | 8,238 | 161,700 | 7,394 | 287 | 169,382 |
| $(97,99)$ | 8,238 | 161,700 | 7,394 | 15,872 | 184,967 |
| $(98,99)$ | 8,238 | 161,700 | 7,394 | 8,704 | 177,799 |

Thus the stored CNFs express exactly the required finite relaxations; they
do not impose a hidden restriction on additions.

## 4. Hash and DRAT audit

I recomputed every hash from the files on disk.  The values below agree with
the frozen JSON records and report.

| fixed edge | CNF gzip SHA-256 | CNF raw SHA-256 | DRAT gzip SHA-256 | DRAT raw SHA-256 |
|---|---|---|---|---|
| $(97,98)$ | `d64f009f840597e266ccfb3b31c88f7e87eb760d1fc551b7ee08a0854749ba66` | `c907dc96c1ff3378d345ead0ea22456eccef50f321cc53b6cf7dda46784d6389` | `60687241833df8ae957b3b4fcb02e6e9f7595c6e3dcbee8b77f02dad5443f913` | `517d076efd026eab6eeb89583c0226e713be968120344e6b82c3471e0efe6b5d` |
| $(97,99)$ | `d6d321a4ac1aeec5e99c48843a8cda9395271e89555cea328e29bcda4e70ef15` | `5ba541f58ea42d7fb73ff51a962e98153eece0d4a8bf13c1bea3a86ed0d50429` | `33a9e037e19beeab8dd2af4dca5ce9010d4906b39dc3e5cc8fd62823f518497a` | `84a2236b7692207f59c3d2dcb3521b2f2f2b947428470384ac643c34a7bfbf69` |
| $(98,99)$ | `8d8a543bb3cc17014941fee432673a1dc2b99c8cb4885d4d91bba9005f3b10a7` | `441b70e023f4a9fa1837f16b1502ef3b54a2f00b6143fd5e7de0131ac95beebf` | `159865da9ad23eea298ebd4e9406f2f37ecc6015a593975e9d63e3b08a859897` | `4ff3a43bda7774c09695417a9f9684e8a856fb46bf62225a08e746fbf37d1ad6` |

The package checker reconstructed the three formulas and replayed all three
proofs with the recorded checker binary; each run ended in `s VERIFIED`.

I then used the recorded `drat-trim` tree at commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, confirmed the tracked
`drat-trim.c` had no local diff, freshly compiled it, decompressed the six
artifacts, and reran all three proof pairs directly.  All three independent
runs again ended in `s VERIFIED`.  This second binary had a different build
hash from the recorded binary, so this was not merely another invocation of
the same executable.

## 5. Proof conclusion

Assume for contradiction that an eligible final graph $F$ exists.  By the
unique input triangle, $F$ lies in at least one of the three branches.  Its
edge assignment extends to the standard sequential-counter auxiliaries and
satisfies all triangle clauses, the fixed negative unit, and every installed
$18$-set hitting clause.  It would therefore satisfy that branch's frozen
CNF.  The verified DRAT proof establishes that the CNF is UNSAT, a
contradiction.  This proves the fixed-seed budget-five exclusion. $\square$

## Earliest dependency and trust boundary

There is no remaining mathematical gap inside the stated finite claim.  The
earliest non-formalized dependencies are machine components:

1. the exact bitset clique verifier for the two matrix facts;
2. the standard PySAT sequential-counter encoding for the deletion bound;
3. the pinned `drat-trim` implementation, compiler, and hardware for proof
   replay.

The matrix parser, triangle enumeration, complete CNF prefix, clause counts,
hashes, and proof replays were independently reconstructed.  The clique
search received small-instance exhaustive cross-checking, and the DRAT traces
were replayed with a fresh binary.  A fully formal proof assistant checking
the matrices, cardinality encoding, and DRAT kernel would move this boundary
further down, but its absence is not a defect relative to normal
proof-carrying SAT standards.

## Explicit exclusions

The audit establishes no statement about:

- a repair using six or more input-edge deletions;
- a different added-vertex neighborhood;
- first modifying the $99$-vertex seed and then extending it;
- any unrelated or nonisomorphic $100$-vertex graph;
- the existence or nonexistence of a $100$-vertex $(3,18)$ Ramsey graph.

Accordingly, **this package must not be cited as proving
$R(3,18)\geq101$**.  Its global Ramsey contribution remains the independently
verified, already-known certificate $R(3,18)\geq100$; the new result is a
strong local exclusion for one frozen near-miss basin.
