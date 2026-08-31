# Exact-seven branch-1 full I18-mask union

Date: 2026-08-30  
Status: **CNF CONSTRUCTED AND BYTE-AUDITED; SOLVER NOT RUN**

## Claim boundary

This record strengthens only the finite branch-1 relaxation for the pinned
100-vertex near miss. It does not prove that the strengthened formula is SAT
or UNSAT, does not close branch 1, does not produce an exact-seven repair, and
does not imply `R(3,18) >= 101`.

The tracked audit reconstructs all mask families and checks a deterministic
390,604,816-byte DIMACS file. The large DIMACS file is reproducible and is not
stored in Git.

## Why every transferred mask is sound

Let `x_uv` mean that `{u,v}` is an edge of the final graph. For every fixed
18-subset `S` of the 100 vertices, a graph with independence number below 18
must satisfy

```text
OR_{ {u,v} in binom(S,2) } x_uv.
```

This is a 153-literal positive clause. Its validity depends only on `S` being
an 18-subset; it does not depend on which branch, solver model, or search run
first exposed `S`. Thus every canonical mask in the universal, historical,
fixed-base, and A+ sources is a valid obstruction clause for every exact-seven
target. Discovery provenance affects expected usefulness, not soundness.

The checker rejects any mask outside `[100]`, any mask of cardinality other
than 18, noncanonical hexadecimal encodings, duplicate masks within a source,
and all source-identity drift before it forms a clause.

## Independently authenticated families

| family | masks | ordered-mask SHA-256 | role |
|---|---:|---|---|
| universal | 251,771 | `f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa` | already installed in the common CNF |
| historical | 64,591 | `74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8` | union of 113,448 raw masks from 18 frozen checkpoints |
| fixed base | 235,504 | `1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c` | independently re-enumerated after deleting `(97,99)` |
| A+ | 4,096 | `a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0` | reverse-first batch, disjoint from all three earlier families |

The fixed-base reconstruction does not import the Benders enumerator. Starting
from the pinned seed, it enumerates every independent 16-set in the common
nonneighbourhood of vertices 97 and 99, adjoins both endpoints, and directly
checks each resulting 18-set in the graph with `(97,99)` removed. It visits
16,213,880 deterministic recursion nodes and reproduces the exact 235,504-mask
digest. Exhaustiveness uses the separately pinned seed-verification premise
that the original graph has no independent 18-set.

All JSON inputs are bound by exact whole-file SHA-256 and semantic counts.
Final-component symlinks, non-regular files, duplicate JSON keys, unsafe or
duplicate history source paths, and same-count replacement files are rejected.

## Exact overlap and deduplication

The pairwise intersections among the three older families are:

| intersection | masks |
|---|---:|
| universal and history | 11,429 |
| universal and fixed base | 4,460 |
| history and fixed base | 10,194 |
| all three | 646 |

Their raw membership total is 551,866. Inclusion-exclusion removes 25,437
duplicate memberships and leaves 526,429 distinct masks, with ordered-union
SHA-256
`f4220088cf6dfccc7b0e8b0aa7c2d1a2ef4a47f5ce31738506eefdd591613258`.

The 4,096 A+ masks have zero overlap with each of the three older families.
The complete union therefore contains 530,525 masks, with ordered-union
SHA-256
`f5c1c60877306900c1aa81bd3a7f357c3d16464ad329c676639a6f6bda9a682d`.

The exclusive membership ledger is:

| membership | masks |
|---|---:|
| universal only | 236,528 |
| history only | 43,614 |
| fixed base only | 221,496 |
| universal and history only | 10,783 |
| universal and fixed base only | 3,814 |
| history and fixed base only | 9,548 |
| all three older families | 646 |
| A+ only | 4,096 |

## Deterministic CNF

The authenticated common CNF already contains all 251,771 universal clauses.
The new builder writes, in this exact order:

1. the 718,452 common clauses;
2. the four independently proof-checked positive units `1085`, `1672`,
   `1675`, and `1680`; and
3. the sorted 278,754 masks in the complete union that are not already in the
   universal bank.

The extra-mask stream has SHA-256
`2242d10f9ea3cefedef7a8c02be9a7df41db3cdb6580733e3fca9391db46d1d4`.
The resulting plain DIMACS identity is:

| field | value |
|---|---:|
| variables | 154,190 |
| clauses | 997,210 |
| bytes | 390,604,816 |
| SHA-256 | `4f7e8f5b724a657888c7814d2c25cac41c283c3db356fb8f1a15f4c7322c375d` |

The post-construction audit reads the file without following a symlink,
reconstructs the original common-CNF hash from the first 718,452 body lines,
checks the four units byte for byte, reconstructs every one of the 278,754
appended 153-literal clauses, rejects trailing clauses, and rechecks the final
byte count and SHA-256.

## Relation to earlier experiments

This route is not a byte-level or formula-level duplicate of either earlier
route.

The historical A+ gate contained the universal bank, four positive units, and
the 4,096 A+ clauses: 722,552 clauses in total. It used history and fixed base
only to ensure that A+ was new; it did not install either family. Its verified
SAT endpoint contained the independent-set mask

```text
bfffe00000000000000000000
```

which belongs to both the historical and fixed-base families. The full union
therefore blocks that exact model and adds 274,658 clauses absent from the A+
gate. This removes a concrete omission, but it does not predict the next SAT
or UNSAT endpoint.

The Benders configuration using both `--universal-bank` and
`--all-fixed-base-cuts` has 482,815 distinct initial masks. The full union adds
43,614 history-only masks and 4,096 A+ masks beyond that set, for 47,710
additional masks. Benders also projects masks into deletion/addition master
variables, whereas this construction emits full positive edge-variable
clauses. The fixed-base content is shared, but the complete formula and search
state are not.

## Bounded go/no-go decision

The current decision is:

```text
GO:     build and independently audit the full-union CNF
NO-GO:  start an unbounded or repeated solver campaign at this stage
```

If a single exploratory probe is later authorized, the frozen design permits
one pinned proof-capable backend, at most 300 wall seconds, with no resume,
solver swap, second seed, or cap increase:

- `SAT`: require a complete model satisfying all 997,210 clauses, then check
  triangle-freeness, exact edit semantics, and independent 18-sets; record the
  endpoint and stop;
- `UNKNOWN`: stop and learn nothing;
- `UNSAT`: retain only `UNSAT_UNCHECKED` unless the exact final CNF has a
  nonempty proof that is independently replayed.

This recommendation reflects prior telemetry: the earlier A+ solve required
about 2,532 wall seconds, while the Benders master also consumed its bounded
walls. A larger static bank is promising enough to construct, but not enough
to justify an open-ended solve.

## Reproduction

Source-only audit and regression tests:

```bash
.venv/bin/python \
  routes/finite/build_r3_18_budget7_branch1_full_mask_union.py \
  > /tmp/branch1_full_mask_union_plan.json

.venv/bin/python -m unittest \
  routes.finite.test_build_r3_18_budget7_branch1_full_mask_union -v
```

Given the frozen `branch1_common.cnf.gz` asset, construct and immediately
re-audit the full CNF:

```bash
.venv/bin/python \
  routes/finite/build_r3_18_budget7_branch1_full_mask_union.py \
  --common-cnf /path/to/branch1_common.cnf.gz \
  --emit-cnf /tmp/branch1_full_mask_union.cnf \
  > /tmp/branch1_full_mask_union_audit.json

.venv/bin/python \
  routes/finite/build_r3_18_budget7_branch1_full_mask_union.py \
  --check-cnf /tmp/branch1_full_mask_union.cnf
```

The common gzip input must have SHA-256
`39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365`.
When the output basename is `branch1_full_mask_union.cnf`, the second command's
JSON must be byte-identical to
`r3_18_budget7_branch1_full_mask_union_audit.json`.

No command in this record launches a SAT solver.

## Tracked small-artifact identities

| file | SHA-256 |
|---|---|
| `build_r3_18_budget7_branch1_full_mask_union.py` | `22ae0006b8d5dd852b054c46e8438cc03946848cf3f9172bfc000fa0fc352eb0` |
| `test_build_r3_18_budget7_branch1_full_mask_union.py` | `1c95719e5dace1df0a7098062c261cb2fe537393532863e5c4650de29a2667c0` |
| `r3_18_budget7_branch1_full_mask_union_audit.json` | `8cbe7000f3b85984e6c0aff9a3fb50a727a92d0dd50f528487569be9229926db` |
| `r3_18_budget7_branch1_full_mask_union_design.json` | `8e5972674e717a3b68c79b0808f1e4e2b4af494e675a92be08a632b4ab83fd90` |
