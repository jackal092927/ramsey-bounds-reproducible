# R(3,18), fixed n=100 near miss: exact-seven first-round search

Date: 2026-08-12  
Status: **all three branches `UNKNOWN`**

## Result

The first exact-seven portfolio did not find a $100$-vertex Ramsey graph and
did not prove any branch UNSAT.  All three solvers reached the registered
300-second discovery wall while still inside their first SAT call.  Thus the
only valid endpoint is

```text
branch 0, fixed absent (97,98), CaDiCaL:    UNKNOWN
branch 1, fixed absent (97,99), Glucose42:  UNKNOWN
branch 2, fixed absent (98,99), MapleChrono: UNKNOWN
```

There is no new global Ramsey bound.  In particular, this round does **not**
establish $R(3,18)\geq101$, does not establish that an exact-seven repair
exists, and does not exclude an exact-seven repair.

The machine-readable frozen state is
`r3_18_budget7_first_round_summary.json`.

## Why exact seven has these three branches

The frozen input is the 100-vertex near miss with SHA-256

```text
e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e
```

It has 827 edges, no independent 18-set, and the unique triangle
$(97,98,99)$.  The proof-checked budget-six package excludes every repair
with at most six input-edge deletions while allowing arbitrary additions of
input nonedges.  Its current authoritative summary and complete referee are
pinned by

```text
0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a  r3_18_budget6_summary.json
1bb634ed1a6181064ac2ae0277ea6582cd2627a76a92208907cc1532d49bfede  INDEPENDENT_R3_18_BUDGET6_COMPLETE_REFEREE.md
```

The older `dbcb...` summary identity is deliberately not used: it belonged
to a partial snapshot in which branches 0 and 1 were still unresolved.

Any repair inside the next deletion layer therefore deletes exactly seven
input edges.  Triangle-freeness forces at least one of the three input
triangle edges absent.  Fixing that edge absent leaves an equality requiring
exactly six deletions among the other 826 input edges.  The three branches
cover every exact-seven repair; they need not be disjoint.  All 4,123 input
nonedges retain free final-edge variables and are absent from the deletion
counter, although triangle clauses still constrain which additions can
coexist.

## Formula and universal cut preload

Every branch used the same formula dimensions:

| block | size |
|---|---:|
| primary pair variables | 4,950 |
| sequential-counter auxiliaries | 9,840 |
| all triangle clauses | 161,700 |
| exact-six counter clauses | 19,680 |
| fixed negative unit | 1 |
| universal independent-18 hitting clauses | 251,771 |
| total initial clauses | 433,152 |

The universal bank is
`r3_18_budget6_branch_0_universal_union.cuts.json`, SHA-256
`91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b`.
An independent state checker parsed all 251,771 entries, confirmed that each
is a distinct 18-subset of the 100 vertices, and reproduced the ordered
digest
`f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa`.
Each corresponding positive 153-edge clause is necessary for every graph
with independence number below 18, so cross-branch reuse is sound.

No heuristic no-good was installed or treated as evidence.

## Bounded endpoints

| branch | solver | load checkpoint | discovery wall | iterations | new cuts | endpoint |
|---:|---|---:|---:|---:|---:|---|
| 0 | `cadical195` | 5.494 s | 300.030 s | 0 | 0 | `UNKNOWN_DISCOVERY_WALL_LIMIT` |
| 1 | `glucose42` | 5.786 s | 300.013 s | 0 | 0 | `UNKNOWN_DISCOVERY_WALL_LIMIT` |
| 2 | `maplechrono` | 5.708 s | 300.015 s | 0 | 0 | `UNKNOWN_DISCOVERY_WALL_LIMIT` |

The `READY` checkpoints were written only after the complete structural
formula and universal bank had been installed.  In every branch the first
call to `solve()` remained active until the parent process enforced the hard
wall.  Consequently the reported zero iterations means that no SAT model
reached the exact independent-set separator; it does not mean UNSAT.

The recoverable state is the pinned universal bank plus an empty list of
additional cuts.  Internal CDCL search state was not serialized, so a later
run can safely reconstruct the exact formula and cuts but cannot resume at
the interrupted instruction.

## Frozen branch artifacts

| branch | result JSON SHA-256 | checkpoint SHA-256 |
|---:|---|---|
| 0 | `97e777da32b82a83b8e999c9af1f927c87b67689b8fb72f8b31ded07b39a2f7f` | `918dc1cc80860d97b3209f6d969a156b9df5fb8b4df7f0fa910e72fdc5778098` |
| 1 | `81734a23298ea9c3364a047c3b7b10910bcd44faf9ff55c3a251fd709f6ac64f` | `8491cbd5e073170b6f7a503efb3d6af6c077b6d72defbf9cd6feb6f06e85fc7f` |
| 2 | `92e2c948892d6f298e0ca3a5055cf31cf3eea361b6eee8197ba536922e437554` | `9e8ea23904378ec1bfc6e4c486fd32f10ccc99c1646855c7589c21cc3c9b9f5c` |

The independent frozen-state checker and tests are pinned by

```text
8c1f2629193de8b16e018f036ce462b8e18110b9f4f1c13b3162b25fe415d6f4  check_r3_18_budget7.py
46b0324d67baaf66bae49027bf4ddbfe3aa08684d3cbe364326bc4400914c987  test_r3_18_budget7_branch.py
13a7cfeb564297fcad2ea2c6ca831a6bf4b4755e0223abcf9d1bd1178103d0de  r3_18_budget7_branch.py
```

The checker returned `FIRST_ROUND_STATE_VERIFIED`, and all six unit tests
passed.  The tests include the exact counter truth table (five residual
deletions UNSAT, six SAT, seven UNSAT under complete input-edge assumptions),
prove that original nonedge variables are absent from the counter, and check
that a conflicting nonedge addition remains correctly forbidden by triangle
clauses.

## Claim boundary

The still-valid positive statement is only the prior local result: the
fixed seed admits no repair with at most six input-edge deletions under free
input-nonedge additions.  This first exact-seven round adds a reproducible
search state, not a theorem about the exact-seven layer and not a global
Ramsey-number improvement.
