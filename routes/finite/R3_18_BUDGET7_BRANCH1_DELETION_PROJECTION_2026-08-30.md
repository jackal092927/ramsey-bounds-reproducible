# Proof Package: Branch-1 deletion-covering projection

## Claim

Let (H) be the frozen 100-vertex near-miss, whose unique triangle is
({97,98,99}), and let

$$
B=H-(97,99).
$$

Fix (k=6). Suppose a graph (F) is obtained from (B) by deleting exactly
(k) edges of (B), never re-adding ((97,99)), and adding an arbitrary set
of original nonedges of (H). If (F) is triangle-free and
(alpha(F)<18), then its residual deletion support extends to a satisfying
assignment of the exact-seven deletion-covering projection defined below.

The uniform statement with (k=5), omitting the four exact-seven singleton
exclusions, is also valid and is called the exact-six analogue.

## Status

PROVABLE AS STATED

This status applies to the necessity theorem above. The bounded exact-six SAT
call ended `UNKNOWN_HARD_WALL_LIMIT`; it proves neither satisfiability nor
unsatisfiability of the projection.

## Assumptions

- The seed file is the 100-vertex graph with SHA-256
  `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
- The separately checked seed fact (alpha(H)<18) is available. This premise
  is used only to prove that the reconstructed fixed-base family is complete.
- The fixed branch edge ((97,99)) cannot be re-added.
- A target graph is formed only by deleting edges of (B) and adding original
  nonedges of (H); no other graph operation is allowed.
- For the exact-seven profile, the four proof-checked singleton consequences
  apply: ((11,62)), ((18,61)), ((18,64)), and ((18,69)) are retained.
  These units are not assumed in the exact-six analogue.

## Notation

- (E(B)) is the 826-edge family of the fixed base.
- (D\subseteq E(B)) is the residual deletion support.
- (mathcal A) is the set of 4,123 original nonedges of (H). It excludes
  ((97,99)) because that edge is fixed absent and cannot be re-added.
- (d_e) is true exactly when (e\in D).
- For (uv\inmathcal A), (g_{uv}) is a local-eligibility selector.
- For a fixed-base independent 18-set (S),
  (inom{S}{2}\capmathcal A) is its family of addable internal pairs.
- (N_B(u)\cap N_B(v)) is the common-neighbour set of (u,v) in (B).

## Proof Strategy

Map any genuine repair (F) to a projection assignment. Set the deletion
variables from its actual residual deletion support. Set (g_{uv}) true for
every pair actually added in (F). Triangle-freeness supplies all local wedge
clauses, while (alpha(F)<18) supplies every fixed-base covering clause. The
degree cap and the four checked singleton consequences supply the remaining
support restrictions.

## Dependency Map

1. Completeness of the fixed-base family depends on (alpha(H)<18) and on the
   fact that (B) differs from (H) in only the pair ((97,99)).
2. The vertex-98 hit depends on (d_B(98)=18) and on the elementary fact that
   every neighbourhood in a triangle-free graph is independent.
3. Each local-eligibility clause depends only on triangle-freeness of (F).
4. Each fixed-base cover depends only on (alpha(F)<18).
5. The exact-seven singleton units depend on the four checked CNF/DRAT pairs;
   they are deliberately absent from the exact-six analogue.
6. The auxiliary sequential-counter variables depend on the independently
   tested constructive semantics of the canonical counter encoding.

## Proof

### Step 1: reconstruct the complete fixed-base family

The only edge removed when passing from (H) to (B) is ((97,99)). Let
(S) be an independent 18-set of (B). If (S) did not contain both 97 and
99, then no pair of (S) would change between (H) and (B), so (S) would
also be independent in (H). This contradicts the checked premise
(alpha(H)<18). Therefore every such (S) has the form

$$
S=\{97,99\}\cup T,
$$

where (T) is an independent 16-set in the common non-neighbourhood of 97
and 99 in (H). That common non-neighbourhood contains exactly 65 vertices.
An increasing-label generator and an independent decreasing-label checker
both enumerate exactly 235,504 such sets. Their lifted-mask digest is

```text
1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c
```

and the residual 16-set digest is

```text
071fe425f750b0e3021b89573a929a15b98ef6449aac2c60c3c1d014eb7df8cd
```

Thus this is the complete fixed-base (I_{18}) family, subject exactly to the
stated seed premise.

### Step 2: exact deletion cardinality

By hypothesis, (F) deletes exactly (k) residual edges of (B). Assign
(d_e=1) if and only if (e\in D). Then

$$
\sum_{e\in E(B)} d_e=k.
$$

The canonical equality counter therefore has a satisfying auxiliary extension.

### Step 3: the vertex-98 degree hit

The fixed base has (d_B(98)=18). Since (F) is triangle-free, (N_F(98))
is independent. The assumption (alpha(F)<18) gives (d_F(98)\le17). If
(a_{98}) is the number of added pairs incident to 98, then

$$
d_F(98)=18-|D\cap\delta_B(98)|+a_{98}\le17.
$$

Hence

$$
|D\cap\delta_B(98)|\ge a_{98}+1\ge1.
$$

This proves the projection clause

$$
\bigvee_{e\in\delta_B(98)}d_e.
$$

### Step 4: local eligibility of every actual addition

Let (uv) be an original nonedge that is added in (F), and let
(w\in N_B(u)\cap N_B(v)). If neither (uw) nor (vw) were in (D), then
all three pairs (uv,uw,vw) would be edges of (F), contradicting
triangle-freeness. Therefore

$$
g_{uv}\Longrightarrow d_{uw}\lor d_{vw}
$$

for every such common neighbour (w), when (g_{uv}) is set true for actual
additions. Across all 4,123 original nonedges this produces 12,832 wedge
clauses. The common-neighbour-count histogram is

| common neighbours | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pairs | 737 | 1498 | 209 | 1132 | 150 | 9 | 352 | 36 |

### Step 5: cover every fixed-base independent 18-set

Let (S) be any fixed-base independent 18-set. Deleting further base edges
cannot destroy the independence of (S). Because (F) has no independent
18-set, at least one pair internal to (S) must be added. The pair
((97,99)) cannot be re-added, so one of the 152 pairs in
(inom{S}{2}\capmathcal A) is an actual addition. Step 4 makes its
selector true. Hence

$$
\bigvee_{uv\in \binom{S}{2}\cap\mathcal A} g_{uv}
$$

holds for each of the 235,504 reconstructed sets.

### Step 6: exact-seven singleton exclusions

The four checked singleton consequences say that every model of the common
exact-seven relaxation retains the four edges listed in the assumptions. A
genuine exact-seven repair maps into that relaxation. Therefore its deletion
support satisfies

$$
d_{11,62}=d_{18,61}=d_{18,64}=d_{18,69}=0.
$$

No corresponding import is made for exact-six, because these proofs were
constructed for the exact-seven common formula.

Steps 2--6 provide a satisfying projection assignment for every genuine
repair in the stated scope. This proves necessity. (square)

## Exact formula identities

| profile | residual deletions | variables | clauses | complete DIMACS SHA-256 |
|---|---:|---:|---:|---|
| exact-six analogue | 5 | 13,159 | 264,757 | `8611eaab2f01062948ae00e6ea91d265a439a0dcec3e2750f3df8deda5826c0e` |
| exact-seven, not emitted or solved | 6 | 14,789 | 268,021 | `fcff09425a50a8985266308948fc7f8545922b12fb0e0ff8c818abace503b0e6` |

The exact-seven digest is an independent streamed reconstruction of the CNF
that would be emitted; no exact-seven CNF or solver endpoint was produced.

## Strength-gate endpoint

The exact-six analogue is the correct strength gate because the full
exact-six branch is already excluded by a checked proof. Its projection was
generated on Sirius and independently reconstructed byte for byte:

- CNF: 179,912,421 bytes and 264,758 lines including the header;
- solver: CaDiCaL 3.0.1, commit
  `c60730422e758ef1cebe7aeddf2dda31c996bf04`;
- executable SHA-256:
  `f5e2cf978a3b9ebf17601b9a7a25f298c684c18841846b66bdd6a6e20951fb2a`;
- hard solver wall: 300 seconds;
- endpoint: exit 124, no SAT/UNSAT status line;
- classification: `UNKNOWN_HARD_WALL_LIMIT`.

The interrupted process left a 1,887,813,632-byte DRAT prefix with SHA-256
`3b1a7e09c00602c3a3c9b39ca7f8c96f5cd4bc1bff932c3fd493d71e0f662dad`.
It was incomplete, was never passed to a proof checker, and was deleted from
Sirius after its identity was recorded. It is not evidence.

## Corrections or Missing Assumptions

- The projection does not encode triangles using two or three added edges.
- It does not encode degree caps away from the necessary vertex-98 hit.
- It does not encode independent 18-sets created by the residual deletions.
- It does not require all locally eligible selectors to form one globally
  consistent final addition set.
- Consequently, projection SAT would not imply that a repair exists.
- Solver UNSAT would not be accepted without a complete, independently
  replayed proof.

## Open Risks

- The exact-six strength gate is unresolved, not failed by a mathematical
  counterexample. The timeout does not show that the projection is SAT or
  intrinsically hard.
- The predefined gate did not pass, so a one-shot proof-producing exact-seven
  call is not justified. Recommendation: `DO_NOT_RUN` until the projection is
  strengthened or the exact-six analogue is certified.
- This route produces no new (R(3,18)) bound and no repair certificate.

The complete machine ledger is
`routes/finite/r3_18_budget7_branch1_deletion_projection.json`; the independent
checker is
`routes/finite/check_r3_18_budget7_branch1_deletion_projection.py`.
