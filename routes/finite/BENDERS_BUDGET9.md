# R(3,13) budget-9 shared-deficit / Benders search

Date: 2026-08-12  
Scope: the 61-vertex basin around `r3_13_n61_frozen_nearmiss_k11.txt`  
Verdict: **UNKNOWN at an explicit master conflict limit; no candidate and no new Ramsey bound**

## New decomposition

The earlier exact deductions remain in force: edge `(56,60)` is forced deleted,
and the exact budget-8 result is UNSAT.  Therefore a budget-9 solution must
delete the hub and exactly eight of the 360 remaining original edges.

`benders_budget9.py` separates this residual problem rather than repeating the
1,830-final-edge monolithic SAT formulation.

1. A master selects exactly eight deletion variables `d_e`.
2. For each original nonedge `f={u,v}`, selector `y_f` can be true only if the
   same deletion set hits every common-neighbor spoke pair

   ```text
   {{u,w},{v,w}}  for w in N_H(u) intersect N_H(v).
   ```

   Thus `y_f` says that adding `f` is locally triangle-safe.
3. In the support graph consisting of retained base edges and selected `y_f`
   edges, an independent 13-set `X` yields the conditional master cut

   ```text
   OR_{e in E_H(X)} not d_e  OR  OR_{f in nonedges_H(X), f != hub} y_f.   (1)
   ```

   This separator finds independent sets created by the eight deletions too;
   it is not restricted to the 25,685 sets present immediately after hub
   deletion.
4. If all such local cuts pass, an add-only fixed-deletion SAT subproblem checks
   collective triangle constraints exactly.  Deleted original edges remain
   fixed absent and are never add-variables.  Any SAT output is reconstructed
   as a matrix and passed to the independent `verify_ramsey.py` checker.

### Why cut (1) is valid

Suppose a feasible final graph uses deletion set `D`.  If some base edge of
`X` is retained, the first disjunction is true.  Otherwise, because `X` cannot
remain independent, the final graph adds some original nonedge `f` inside
`X`.  Triangle-freeness implies that for every base common neighbor `w`, at
least one of `{u,w}` and `{v,w}` lies in `D`; hence `f` is locally eligible and
the corresponding `y_f` may be true.  Therefore every feasible final graph
satisfies (1).

The master also contains a stronger shared-deficit family.  The local
requirements of one addition form a matching on deletion-edge variables.  The
union for two additions has maximum degree two, so its minimum vertex cover is
computed exactly component-by-component.  If that cover exceeds eight, the
binary cut `not y_f OR not y_g` is valid.  There are **81,345** such strict
pairwise incompatibility cuts in this instance.

## Bounded experiments

The initial strict-cut generation run used MiniSat22, conflict slices of 5,000,
one million global master conflicts, 256 cuts per separated master model, and a
240-second wall cap.  It reached:

| measure | result |
|---|---:|
| Status | `UNKNOWN_MASTER_CONFLICT_LIMIT` |
| Master models | 49 |
| Strict conditional cuts generated | 12,544 |
| Master conflicts | 1,000,001 |
| Decisions | 3,267,708 |
| Propagations | 912,002,889 |
| Timer interruptions | 0 |
| Elapsed | 83.528 s |

A second strict continuation imported those 12,544 masks, installed the 81,345
pairwise cuts, and used batches of 4,096 witnesses.  At 750,001 more conflicts
it examined three new exact deletion sets and added 12,288 new cuts, leaving a
reusable union of **24,832 distinct conditional cuts**.  Every one of the three
support graphs exposed at least 4,096 independent 13-sets.  No fixed-deletion
subproblem was reached.

The pinned final machine record is a fresh proof-safe replay starting with all
24,832 imported cuts and all 81,345 pairwise cuts:

| measure | result |
|---|---:|
| Status | `UNKNOWN_MASTER_CONFLICT_LIMIT` |
| `proof_complete` bookkeeping flag | `true` |
| Imported strict conditional cuts | 24,832 |
| Strict pairwise cuts | 81,345 |
| Heuristic UNKNOWN no-goods | **0** |
| Master models reached | 0 |
| Limited calls | 200 |
| Master conflicts | 1,000,001 |
| Decisions | 2,677,157 |
| Propagations | 863,288,341 |
| Timer interruptions | 0 |
| Elapsed | 138.732 s |

Here `proof_complete=true` means only that every installed exclusion is
logically valid: there were no heuristic no-goods and no incomplete oracle
decision was used as a proof step.  It does **not** turn a conflict-limit return
into UNSAT.  The overall status remains `UNKNOWN`, no candidate was emitted,
and `R(3,13) >= 62` remains unproved.

The 24,832 masks are embedded in `benders_budget9.json` under
`reusable_strict_cuts.conditional_I13_masks_hex`; `--resume-json` reconstructs
their clauses after checking the schema and input hash.  The pairwise family is
regenerated deterministically from its stated rule.  Strict fixed-deletion
UNSAT no-goods and heuristic UNKNOWN exclusions have separate fields; both are
zero in the pinned record.

## Small-graph oracles and regression tests

Three new exact tests guard the decomposition:

- all triangle-free base/final graph pairs on four vertices satisfy the
  conditional-cut implication whenever the final graph has no independent
  3-set;
- the two-addition lower-bound routine matches brute-force minimum vertex cover
  on all pairs of matchings over six labels;
- after deleting the only edge of `K2`, the fixed-deletion subproblem for
  `s=2` is UNSAT and that deleted edge is not an add-variable.  The old generic
  post-delete repair routine deliberately returns SAT by re-adding it, so the
  test directly detects this modeling regression.

Canonical full test command:

```bash
.venv/bin/python -m unittest routes/finite/test_verify_ramsey.py -v
```

## Reproducibility

Pinned files and SHA-256 values:

```text
input matrix              a144986d21117eff66eda4c37a30acfe25ab274a5587a2542740cf4a82b2f484
budget-8 result           c0fd54ee12cc144087e31e6bc6767209db75beb93a66cabfef5c4da73d759ab0
Benders script            575fc90e34727c5360d32af4e8bd2373ef4912b599504bcd99ac346705a16da0
pinned machine result     f5a60930b468795cfd1c0490e502ba6506cb60e1b0750f71db2eee4f3357b3c2
finite test suite         b38c01c6ee003939db9c7bd113a99de874ce07e1d6c1f08c59b19b63c4ff28c4
```

Run metadata, all resource limits, the complete strict mask list, cut-stream
hash, solver statistics, provenance, and the zero heuristic-no-good count are
stored in `benders_budget9.json`.  The script hash inside that record matches
the final script hash above.

## Exact claim boundary

- A candidate independently accepted by `verify_ramsey.py` would prove
  `R(3,13) >= 62`.
- Master UNSAT with zero heuristic exclusions would prove this budget-9 basin
  empty, not the global nonexistence of all 61-vertex Ramsey graphs.
- Conditional cuts, pairwise incompatibilities, and fixed-deletion UNSAT
  no-goods are strict and reusable.
- A fixed-deletion subproblem returning UNKNOWN may be skipped only as a
  heuristic exploration choice.  Such exclusions are counted separately and
  permanently prevent an UNSAT claim for that run.
- The pinned record is `UNKNOWN`; it changes no published Ramsey-number bound.
