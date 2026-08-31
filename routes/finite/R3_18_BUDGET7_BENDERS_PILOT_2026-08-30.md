# Exact-seven branch-1 deletion-first pilot

Date: 2026-08-30  
Status: bounded diagnostic; no finite Ramsey implication

## Claim boundary

This record concerns branch 1 of the exact-seven repair problem for the pinned
100-vertex seed: edge `(97,99)` is fixed absent and exactly six of the other
826 seed edges are deleted.  Original seed nonedges remain free additions.

Every run below ended `UNKNOWN`.  No candidate passed the independent Ramsey
verifiers, and no solver `UNSAT` endpoint has a checked DRAT/LRAT proof.
Consequently this pilot proves neither a seven-deletion repair nor branch
unsatisfiability.  In particular it does not prove `R(3,18) >= 101` or
`rho(H) >= 8`.

## Reproducible implementation

The initial degree/fallback runs used the historical ascending implementation
preserved at Git commit `622d906`.  The current runner adds explicit,
budgeted vertex-order schedules without changing the CNF:

| role | runner SHA-256 | test SHA-256 |
|---|---|---|
| historical ascending runs | `36dc3b53941605bc4ec132b70b4f61c5afbbcda13742fe9056a38ddb1683e5a0` | `ed62d2318e64d6731bca343e829f2e65c058f8f484a72b027b2a87da9f2fd76f` |
| ordered-gate implementation | `22ddb00aa93727aa51d2edd6d09b0e536a230e0cc17426004858e98620d6c4f8` | `b65ebc6f265de6552cdf6f8c09586f4c7c2ae01db0292908ae7998beea75a35c` |
| hardened release implementation | `eb911a5010581c16042c3853dd5ae98bda4bd7237fde3cae7f9e030730fd984b` | `14b173bf90be9bccb65554d86ba21b344aa2aac7cc4388ac5f99a338a2468f60` |

The pinned matrix SHA-256 is
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
The master structural fingerprint is
`e91f07db0f01b44263fa790922e46efba149b2f461d7afb77b53f847b9641839`,
and the exhaustive fixed-base independent-18-set digest is
`1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c`
for 235,504 masks.

The runner uses a deletion-first master with exact residual deletion count
six, conditional independent-set cuts, and 4,123 addition-eligibility
selectors.  A fixed-deletion exact add-only subproblem enforces all triangle
constraints and lazily separates independent 18-sets.  An incomplete master
oracle may fall back to that exact subproblem, but an incomplete subproblem
always stops without a deletion no-good.  A solver-completed fixed-deletion
`UNSAT` may add a strict six-edge no-good for search purposes; without a proof
trace it remains trusted-code telemetry rather than theorem evidence.

The dedicated test suite has 16 tests covering cardinality semantics, signed
degree clauses, conditional cuts, checkpoint/resume validation, fail-closed
`UNKNOWN` handling, no-good strictness, path-safe provenance, exact relabeling,
the two formerly hard supports, second-pass budget composition, and exhaustive
small-graph order equivalence.  At this hardened Benders snapshot the full
lightweight finite regression had 49 tests, all passing locally.  The later
generalized-core pilot adds eight separately scoped tests, so the current
repository-wide finite-light count is 57.  The 14-test ordered-gate snapshot
also passed on Sirius under Python 3.9 with
`python-sat==1.9.dev13` and `networkx==3.2.1`.

## Degree-cap lift

For every triangle-free graph `G` with `alpha(G) < 18`, the open
neighbourhood of each vertex is independent, so `deg_G(v) <= 17`.
The runner encodes this necessary condition both in the master and in every
fixed-deletion subproblem.

After fixing `(97,99)` absent, vertex 98 still has degree 18.  Hence every
valid residual six-edge deletion set must contain at least one of its 18
incident seed edges.  Of all raw six-edge subsets, the fraction excluded
immediately is

```text
C(808,6) / C(826,6) = 0.875813014052041.
```

Thus the lift removes exactly 87.5813014052041% of raw residual deletion sets,
leaving 12.4186985947959%.  This is a combinatorial pruning ratio, not a claim
of an equal wall-time speedup.

## Bounded Sirius matrix

The first matrix used a two-million-node independent-set oracle cap and a
180-second global wall.  `cN` denotes `N` initial fixed-base cuts.

| run | master / subproblem | endpoint | seconds | master iterations | new cuts | trusted fixed-D UNSAT no-goods |
|---|---|---|---:|---:|---:|---:|
| `g42_c0` | Glucose 4.2 / Glucose 4.2 | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 3.680 | 1 | 0 | 0 |
| `g42_c4096` | Glucose 4.2 / Glucose 4.2 | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 9.700 | 2 | 16 | 0 |
| `m22_c0` | Minisat 2.2 / Minisat 2.2 | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 15.256 | 12 | 2,816 | 0 |
| `m22_c4096` | Minisat 2.2 / Minisat 2.2 | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 47.856 | 6 | 1,039 | 0 |
| `m22_c16384` | Minisat 2.2 / Minisat 2.2 | `UNKNOWN_GLOBAL_WALL_LIMIT` | 180.026 | 0 | 0 | 0 |
| `maple_c4096` | MapleChrono / MapleChrono | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 62.784 | 6 | 768 | 2 |

The two solver-trusted, proof-unchecked deletion sets reached by
`maple_c4096` were:

```text
{(1,97),(10,64),(11,62),(17,98),(18,61),(18,64)}
{(1,97),(10,64),(11,62),(17,98),(18,61),(18,69)}
```

These endpoints may guide later search, but they do not support a paper
theorem and must not be described as certified cores.

The positive-signal extension resumed three checkpoints, used MapleChrono for
the fixed-deletion subproblem, raised the independent-set cap to 20,000,000
nodes and 30 seconds per call, and imposed a 300-second global wall.

| run | master / subproblem | endpoint | seconds | master iterations | new cuts this run | retained trusted no-goods |
|---|---|---|---:|---:|---:|---:|
| `g42_maple_resume` | Glucose 4.2 / MapleChrono | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 121.884 | 24 | 10,780 | 0 |
| `maple_resume` | MapleChrono / MapleChrono | `UNKNOWN_SUBPROBLEM_UNKNOWN_ORACLE_NODE_LIMIT` | 197.868 | 29 | 13,362 | 2 |
| `m22_maple_resume` | Minisat 2.2 / MapleChrono | `UNKNOWN_GLOBAL_WALL_LIMIT` | 300.095 | 25 | 12,800 | 0 |

The first two deep runs each reached a fixed-deletion subproblem model and
then stopped at exactly 20,000,001 recursive independent-set nodes.  The
Minisat master run never reached the subproblem before its global wall.
No deep run produced a candidate or a new completed fixed-D `UNSAT` endpoint.

## Exact oracle-order diagnosis and gates

The two deep fixed-D supports were reconstructed independently.  With the
historical ascending low-bit recursion, each used 2,000,001 nodes and returned
no witness before its node limit.  Relabeling the same graph in reverse order
changes no graph property, yet returned 512 independently validated
original-label independent 18-sets in 11,261 and 10,057 nodes, taking 0.0058
and 0.0052 seconds.  The apparent 20-million-node subproblem bottleneck was
therefore an ordering artifact on these two supports, not evidence of
combinatorial absence.

The current runner exposes `ascending`, `reverse`, and `bidirectional`.
`ascending` is a direct call to the historical enumerator.  `reverse`
deterministically relabels vertices `99,...,0` and maps every witness back.
`bidirectional` starts reverse with half the configured node threshold and
wall budget, then gives the aggregate remainder to ascending.  The historical
enumerator may visit threshold plus one nodes, and the aggregate accounting
preserves that convention.  Only an exhausted pass may certify absence; every
resource-limited pass remains `UNKNOWN`.

Seven ordered gates then tested whether this local repair changed the global
branch endpoint:

| run | master | cut batch | endpoint | seconds | master models | new cuts |
|---|---|---:|---|---:|---:|---:|
| `g42_bidir60` | Glucose 4.2 | 512 | global wall | 64.077 | 1 | 512 |
| `maple_bidir60` | MapleChrono | 512 | global wall | 60.165 | 0 | 0 |
| `g42_bidir10` | Glucose 4.2 | 512 | global wall | 120.218 | 5 | 2,560 |
| `m22_bidir10` | Minisat 2.2 | 512 | global wall | 120.038 | 1 | 512 |
| `maple_bidir10` | MapleChrono | 512 | global wall | 120.059 | 4 | 2,048 |
| `g42_bidir_batch4096` | Glucose 4.2 | 4,096 | global wall | 180.200 | 4 | 16,384 |
| `maple_bidir_batch4096` | MapleChrono | 4,096 | global wall | 180.089 | 3 | 12,288 |

Every returned master support yielded its full cut batch in 0.005--0.075
seconds under reverse-first search.  No ordered gate reached a fixed-D
subproblem, returned a verified candidate, emitted a proof, or added a new
fixed-D no-good.  Under these checkpoints and limits, the observed wall moved
back to the master after fast separation.  This is configuration-specific
telemetry, not a proof that the master is intrinsically hard.

The project-relative machine-readable summary is
`r3_18_budget7_benders_pilot_summary.json`.  Raw remote result files are not
release artifacts because they contain machine-local paths; their SHA-256
digests are retained in the sanitized summary solely as local provenance.

## Command template

After creating an environment containing the pinned project dependencies, a
fresh run is launched from the repository root as follows.  Change only the
solver, cut prefix, and bounded limits declared in the matrix.

```bash
PYTHONUNBUFFERED=1 .venv/bin/python \
  routes/finite/r3_18_budget7_benders_branch1.py \
  routes/finite/certificates/r3_18_n100_nearmiss.txt \
  --initial-fixed-base-cuts 4096 \
  --sub-seed-cuts 8192 \
  --solver maplechrono \
  --subsolver maplechrono \
  --master-conflicts-per-call 10000 \
  --master-max-conflicts 1000000 \
  --max-seconds 300 \
  --max-iterations 2000 \
  --cuts-per-iteration 512 \
  --oracle-nodes 20000000 \
  --oracle-seconds 30 \
  --oracle-order bidirectional \
  --sub-conflicts-per-call 10000 \
  --sub-max-conflicts 500000 \
  --sub-max-seconds 180 \
  --certificate-solver cadical195 \
  --checkpoint runs/example/checkpoint.json \
  --json runs/example/result.json \
  --candidate runs/example/candidate.txt
```

Checkpoint resumption additionally supplies `--resume` with a checkpoint whose
seed, structural formula, initial cut-bank identity, and strict-state hashes
pass validation.  The runner rejects mismatched or corrupted checkpoints.

## Stop decision and next falsifiable route

The reverse-order diagnosis repaired the two apparent fixed-D separator stalls,
but the seven ordered gates produced no verified witness, proof trace, or new
completed fixed-D `UNSAT`.  Repeating the same order/batch/master matrix with
larger walls is stopped.  Under the final gates, separation was cheap and the
master consumed the remaining wall.

The next bounded route is a single parameterized semantic formula over
deletions and additions.  If that common formula, including exact-six
semantics, together with positive assumptions for a set `K` is
proof-checked `UNSAT`, it justifies the family-level clause
`OR_{e in K} not d_e`.  A fixed-D solver core by itself is insufficient.
The engineering route stops if the first 16 replay-validated completed-UNSAT
cases all have core size six; any `UNKNOWN` learns nothing.  Before any
exact-seven cube-and-conquer run, external cuts, their witnesses, formula
hashes, and proof/coverage checks must first replay on a solved exact-six
instance.
