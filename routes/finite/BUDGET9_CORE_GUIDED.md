# R(3,13) budget-9 core-guided diagnostic

Date: 2026-08-12  
Scope: the 61-vertex basin around `r3_13_n61_frozen_nearmiss_k11.txt`  
Verdict: **UNKNOWN at the explicit conflict limit; no candidate and no new Ramsey bound**

## What was audited

`bounded_deletion_sat_cegar.py` has the intended exact basin encoding:

- one Boolean variable for every possible final edge;
- all triangle-free clauses present initially;
- a cardinality bound on original edges deleted;
- unrestricted additions of initial nonedges; and
- lazy, independently found `I_s` edge-hitting clauses.

Its previous `--max-seconds` guard was checked only between calls to
`solver.solve()`.  A single hard call could therefore run past the guard.  The
old budget-9 record correctly says `UNKNOWN_TIME_LIMIT`; its external
termination is neither SAT nor UNSAT evidence.

`budget9_core_guided.py` retains the exact formulation but uses MiniSat22
`solve_limited()` calls.  Every call has both a conflict budget and a wall-clock
interrupt, and the run also has global conflict and wall limits.  Learned
clauses persist between slices.

## Strict structural deductions

These are logical deductions, not search heuristics.

1. The input has exactly 11 triangles:

   ```text
   (5,56,60)  (8,56,60)  (19,56,60) (22,56,60)
   (33,56,60) (36,56,60) (47,56,60) (48,56,60)
   (50,56,60) (52,56,60) (56,58,60)
   ```

2. Every triangle contains hub edge `(56,60)`.  If that edge is retained, each
   triangle requires deletion of at least one of its two spoke edges.  The 11
   two-edge spoke groups are pairwise edge-disjoint, so retaining the hub costs
   at least 11 deletions.  A budget-9 solution must therefore delete `(56,60)`.

3. The earlier exact full-graph CEGAR result at budget 8 is UNSAT (749 CEGAR
   iterations and 748 lazy `I_13` clauses).  Consequently, any budget-9 solution
   must use exactly nine deletions: the forced hub plus exactly eight other
   original edges.

4. Deleting the hub from the near-miss creates exactly 25,685 independent
   13-sets.  Every one contains both hub endpoints.  Their deterministic witness
   stream has SHA256
   `3a7a95b88b5541af42e65931f51fcf2ac17e8a134748f31e6ce8a466b4078c3a`.
   With the hub fixed absent, every witness gives a 77-literal hitting clause
   requiring another edge inside that set.  All 25,685 clauses were installed
   before solving; any independent sets caused by the other eight deletions
   would still be separated lazily.

This is the finite-route analogue of a shared deficit: the 11 local triangle
violations cannot be budgeted independently.  Their shared hub first yields a
group-level forced choice; only then is the residual budget of eight exposed.

## Bounded experiment

Canonical command, from the repository root:

```bash
.venv/bin/python routes/finite/budget9_core_guided.py \
  routes/finite/r3_13_n61_frozen_nearmiss_k11.txt \
  --d8-json routes/finite/r3_13_bounded_delete_8.json \
  --s 13 --budget 9 --hub 56 60 --solver minisat22 \
  --conflicts-per-call 5000 --max-conflicts 1000000 \
  --per-call-seconds 8 --max-seconds 240 \
  --output routes/finite/r3_13_n61_budget9_candidate.txt \
  --json routes/finite/budget9_core_guided.json
```

The initial formula had 1,830 edge variables, 5,632 cardinality auxiliary
variables, and 72,940 clauses: 35,990 triangle clauses, 11,264 exact-residual-
budget clauses, one forced-hub unit clause, and 25,685 preseeded `I_13` clauses.

| progress measure | result |
|---|---:|
| Status | `UNKNOWN_GLOBAL_CONFLICT_LIMIT` |
| Limited calls | 200 |
| Conflict-budget returns | 200 |
| Timer interruptions | 0 |
| Conflicts | 1,000,000 |
| Decisions | 2,818,200 |
| Propagations | 829,173,832 |
| Restarts | 5,398 |
| Elapsed | 219.699 s |
| SAT models reached | 0 |
| Additional lazy `I_13` clauses | 0 |

No call was unbounded: all 200 calls returned at their conflict budget, and the
global conflict limit ended the run.  The solver never reached a model of even
the preseeded relaxation, so there are no empirical deletion-frequency claims
to make.  This is useful progress information but **not** an UNSAT proof.

No candidate file was produced.  Therefore the independent
`verify_ramsey.py` certificate check was not triggered.  In particular, this
experiment does not prove `R(3,13) >= 62`; the global bound is unchanged.

## Reproducibility and tests

Pinned inputs and outputs:

- near-miss matrix SHA256:
  `a144986d21117eff66eda4c37a30acfe25ab274a5587a2542740cf4a82b2f484`
- budget-8 result SHA256:
  `c0fd54ee12cc144087e31e6bc6767209db75beb93a66cabfef5c4da73d759ab0`
- diagnostic script SHA256:
  `6b9b4f83a144ee007672b148c5266ff81647a9944c0c66fd3aad29d37adcd5ee`
- machine result SHA256:
  `e06d52de6b9e50912e63a95ea1293cd606247210dc74b29e0544f3f0be86193f`

Canonical test command:

```bash
.venv/bin/python -m unittest routes/finite/test_verify_ramsey.py -v
```

The test suite includes a small forced-hub hitting proof and a pigeonhole
instance that must return `UNKNOWN` at a one-conflict solver slice, guarding
against regression to an unbounded blocking call.  Existing exhaustive small-
graph oracles continue to test the clique search and repair encodings.

## Best next search direction (not run here)

Repeating the same monolithic solve for more conflicts is not the most
informative next step.  A stronger decomposition would treat each potential
added edge as a residual deletion charge: adding nonedge `(u,v)` requires, for
every current common neighbor `w`, deletion of at least one of `(u,w)` and
`(v,w)`.  The 25,685 `I_13` clauses demand added edges, while only eight
non-hub deletions are available.  A Benders/MaxSAT-style master can therefore:

1. select eight residual deletions;
2. hit multiple `I_13` witnesses with shared additions; and
3. add weighted group cuts for the spoke deletions those additions force.

The important accounting rule is to aggregate overlapping witnesses before
charging the deletion budget.  Summing per-witness local costs would double
count shared repairs, just as treating the original 11 triangles separately
would miss the forced hub decision.  Persisting the master cuts and CEGAR
witness stream would also make the next bounded run resumable and more
diagnostic than another opaque SAT call.

