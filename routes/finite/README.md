# Finite Ramsey-number route

This directory is a self-contained, CPU-oriented baseline for checking and
locally extending explicit classical Ramsey graph certificates.  The live
snapshot date is **2026-08-12**.

The principal target selected after the record audit is

\[
R(3,13)\ge 62,
\]

starting from the public 60-vertex AlphaEvolve certificate for
\(R(3,13)\ge61\).  No improved Ramsey bound was obtained, but the run produced
exact local exclusion results in two distinct fixed-seed basins and a concrete
near frontier.  The non-star-seed exclusion reaches `d<=10`; its exhaustive
branch formulas have frozen DRAT traces independently accepted by
`drat-trim`.  It is still only a fixed-seed statement, not a proof of
`R(3,13)>=62`.

A second live target is `R(3,18)>=101`.  The public 99-point certificate for
`R(3,18)>=100` has a frozen 100-point extension with exactly one triangle and
no `I18`.  A proof-carrying three-branch computation excludes every repair of
that named near miss using arbitrary additions and at most five input-edge
deletions. At exact budget six, all three branches fixing `(97,98)`, `(97,99)`,
and `(98,99)` absent now have frozen, replayed DRAT UNSAT proofs. Thus the
complete fixed-seed deletion-budget-six ball is excluded even with arbitrary
original-nonedge additions, and this named seed has deletion repair radius at
least seven. This does not show that a seven-deletion repair exists, does not
construct a 100-point Ramsey graph, and does not establish `R(3,18)>=101`.

## Canonical reproduction

Run every command from the repository root. For a non-destructive complete
lightweight replay, prefer `python reproduce.py quick`; the commands below are
the route-level equivalents.

```bash
.venv/bin/pip install -r routes/finite/requirements.txt
.venv/bin/python routes/finite/fetch_certificates.py
.venv/bin/python -m unittest discover -s routes/finite -t . -p 'test_*.py' -v
```

Independent certificate checks:

```bash
.venv/bin/python routes/finite/verify_ramsey.py routes/finite/certificates/scale_R3_17_ge_93.txt 3 17
.venv/bin/python routes/finite/verify_ramsey.py routes/finite/certificates/scale_R4_15_ge_160.txt 4 15
.venv/bin/python routes/finite/verify_ramsey.py routes/finite/certificates/alphaevolve_R3_13_ge_61.txt 3 13
.venv/bin/python routes/finite/verify_ramsey.py routes/finite/certificates/alphaevolve_R3_18_ge_100.txt 3 18
```

Independent SAT vertex-selection cross-checks for the two post-survey
certificates:

```bash
.venv/bin/python routes/finite/verify_ramsey_sat.py routes/finite/certificates/scale_R4_15_ge_160.txt 4 15
```

The direct selector-SAT cross-check of the larger \(I_{17}\) exclusion was not
completed within this run's time budget; its bitset certificate check did
complete.  Do not interpret the absent SAT JSON as a failed certificate.

Fixed-base extension diagnosis with two SAT solvers:

```bash
.venv/bin/python routes/finite/extension_sat_cegar.py routes/finite/certificates/alphaevolve_R3_13_ge_61.txt 3 13
.venv/bin/python routes/finite/extension_sat_cegar.py routes/finite/certificates/alphaevolve_R3_13_ge_61.txt 3 13 --solver glucose42
```

The structured repair test behind the old all-hub basin's local exclusion is:

```bash
.venv/bin/python routes/finite/bounded_deletion_sat_cegar.py routes/finite/r3_13_n61_frozen_nearmiss_k11.txt 13 --budget 8 --json /tmp/r3_13_budget8.json
```

The bounded, interruptible budget-9 diagnostic is:

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

It terminated as `UNKNOWN_GLOBAL_CONFLICT_LIMIT`; this is diagnostic evidence,
not UNSAT.  The exact forced-hub reduction and all counters are recorded in
[BUDGET9_CORE_GUIDED.md](BUDGET9_CORE_GUIDED.md).

The follow-up shared-deficit/Benders decomposition is:

```bash
.venv/bin/python routes/finite/benders_budget9.py \
  routes/finite/r3_13_n61_frozen_nearmiss_k11.txt \
  --d8-json routes/finite/r3_13_bounded_delete_8.json \
  --max-seconds 240 --master-max-conflicts 1000000 \
  --cuts-per-iteration 4096 \
  --output routes/finite/r3_13_n61_benders_candidate.txt \
  --json /tmp/benders_budget9_next.json
```

It produced 24,832 reusable strict conditional cuts and 81,345 strict pairwise
incompatibilities, but the pinned replay remains
`UNKNOWN_MASTER_CONFLICT_LIMIT`; it used zero heuristic UNKNOWN no-goods and
emitted no candidate.  See [BENDERS_BUDGET9.md](BENDERS_BUDGET9.md).

The higher-order follow-up is:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/benders_next.py \
  routes/finite/r3_13_n61_frozen_nearmiss_k11.txt \
  --d8-json routes/finite/r3_13_bounded_delete_8.json \
  --strict-cut-json routes/finite/benders_budget9.json \
  --higher-order-top-k 128 --higher-order-max-triples 400000 \
  --higher-order-preprocess-seconds 30 \
  --max-conflicts 750000 --conflicts-per-call 5000 \
  --per-call-seconds 8 --max-seconds 180 \
  --output routes/finite/r3_13_n61_benders_next_candidate.txt \
  --json routes/finite/benders_next.json
```

It exhaustively classifies all 341,376 triples among the 128 selected
high-coverage additions and serializes 57,879 genuine ternary shared-deficit
cuts. Every serialized cut was independently replayed, but the bounded master
run still returned `UNKNOWN_MASTER_CONFLICT_LIMIT` and emitted no candidate.
See [BENDERS_NEXT.md](BENDERS_NEXT.md).

The scripts use independent bitset clique search, exact SAT constraints, and
full verifier checks.  They do not call the certificate producers' notebooks.

See [REPORT.md](REPORT.md) for provenance and current bounds, and
[BUDGET9_CORE_GUIDED.md](BUDGET9_CORE_GUIDED.md) and
[BENDERS_BUDGET9.md](BENDERS_BUDGET9.md) and
[BENDERS_NEXT.md](BENDERS_NEXT.md) for the budget-nine decompositions.

The first deliberately different basin is documented in
[NEW_BASIN_SEARCH.md](NEW_BASIN_SEARCH.md). Exact diagnostics show that the old
k=10 near miss is itself a ten-triangle hub. A newly generated k=11 seed has no
independent 13-set but no edge common to all eleven triangles. With arbitrary
additions allowed, the original CaDiCaL run excluded at most seven seed-edge
deletions.  Budgets eight and nine are now also excluded: the hub edge
is forced, the remaining triangle gives three exhaustive branches, and all
three branch relaxations are UNSAT in Glucose and CaDiCaL with independently
checked DRAT traces.  At budget nine the residual counter permits seven rather
than six additional deletions, and the three stronger branch formulas again
have checked UNSAT traces.  Budget ten is also excluded: three hub-deleted
residual-eight formulas and a fourth formula merging exactly all 512
hub-retained transversals have checked UNSAT traces.  Thus this fixed seed
requires at least eleven deletions. The
competing 159-to-160 (R(4,15)) edit diagnostic remains `UNKNOWN`, and no new
global Ramsey bound is claimed.  See [BUDGET10_SEARCH.md](BUDGET10_SEARCH.md)
for the newest proof-carrying endpoint, [BUDGET9_NONSTAR.md](BUDGET9_NONSTAR.md)
and [BUDGET8_NEXT.md](BUDGET8_NEXT.md) for
its predecessor, and
[INDEPENDENT_NEW_BASIN_REFEREE.md](INDEPENDENT_NEW_BASIN_REFEREE.md) for the
earlier encoding audit.  The budget-nine replay is in
[INDEPENDENT_BUDGET9_REFEREE.md](INDEPENDENT_BUDGET9_REFEREE.md); the newest
endpoint's independent structure/CNF/DRAT reconstruction is
[INDEPENDENT_BUDGET10_REFEREE.md](INDEPENDENT_BUDGET10_REFEREE.md).

A second, independently reviewed one-vertex basin is documented in
[SECOND_NEW_BASIN_SEARCH.md](SECOND_NEW_BASIN_SEARCH.md) and
[INDEPENDENT_SECOND_NEW_BASIN_REFEREE.md](INDEPENDENT_SECOND_NEW_BASIN_REFEREE.md).
Its frozen 61-vertex graph has 369 edges, 17 triangles, no independent
13-set, maximum triangle-edge multiplicity four, and triangle transversal
number eight.  Combining the exact fixed-base lower diagnosis with the
candidate gives `10 <= m_cap4 <= 17`; the exact optimum remains unknown.  It
is a dispersed near miss, not a certificate for `R(3,13)>=62`.

Replay the endpoint of that new local radius with:

```bash
.venv/bin/python routes/finite/bounded_deletion_sat_cegar.py \
  routes/finite/r3_13_n61_nonstar_k11.txt 13 \
  --budget 7 --solver cadical195 \
  --json /tmp/new_basin_d7.json
```

`UNSAT` here quantifies only over edits of the named fixed seed.  It permits
arbitrary additions, but it does not quantify over all 61-vertex graphs.

The proof-carrying budget-eight endpoint is reproduced by:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/budget8_next.py \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --artifact-dir routes/finite \
  --json routes/finite/budget8_next.json \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-trim-source-commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

The proof-carrying budget-nine endpoint uses the same pinned checker:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/budget9_nonstar.py \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --artifact-dir routes/finite \
  --json routes/finite/budget9_nonstar.json \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-trim-source-commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

The proof-carrying budget-ten endpoint uses the same pinned checker with
`routes/finite/budget10_search.py`; it contains four exhaustive branch CNFs.

## R(3,18) one-point extension

The complete fixed-seed statement, formula semantics, artifact hashes, and
claim boundary are in [R3_18_EXTENSION_REPAIR.md](R3_18_EXTENSION_REPAIR.md).
An independent reviewer rebuilt the graph facts and every CNF, then replayed
all three proofs both with the packaged checker and with a freshly compiled
binary; see
[INDEPENDENT_R3_18_EXTENSION_REFEREE.md](INDEPENDENT_R3_18_EXTENSION_REFEREE.md).
The small primitive tests are:

```bash
.venv/bin/python -m routes.finite.test_r3_18_budget5_branch
```

The frozen checker reconstructs the three CNFs and can replay all three DRAT
proofs when given the pinned `drat-trim` executable:

```bash
.venv/bin/python routes/finite/check_r3_18_extension_repair.py \
  --artifact-dir routes/finite \
  --drat-trim /absolute/path/to/drat-trim \
  --drat-seconds 120 \
  --json routes/finite/r3_18_extension_repair_check.json
```

The conclusion is restricted to the named edit ball.  It neither excludes
other 100-vertex graphs nor proves `R(3,18)>=101`.

The exact budget-six shell is documented in
[R3_18_BUDGET6_AUDIT.md](R3_18_BUDGET6_AUDIT.md).  Its branch-2 finite CNF
allows arbitrary original-nonedge additions and enforces exactly six total
input-edge deletions.  The 146 MB compressed DRAT proof was independently
replayed; see
[INDEPENDENT_R3_18_BUDGET6_REFEREE.md](INDEPENDENT_R3_18_BUDGET6_REFEREE.md).
The branch-2 proof was followed by a deduplicated cut-bank continuation that
closed branch 1 with a fresh 433 MB compressed DRAT proof, replayed against
the full 242,064-clause CNF.  Its earlier partial DRAT remains quarantined and
unused.  See
[R3_18_BUDGET6_BRANCH1_PROOF.md](R3_18_BUDGET6_BRANCH1_PROOF.md) and its
independent clause-level review in
[INDEPENDENT_R3_18_BUDGET6_BRANCH1_REFEREE.md](INDEPENDENT_R3_18_BUDGET6_BRANCH1_REFEREE.md).
Finally, a validated union of 251,771 universal $I_{18}$ cuts closed branch 0
with a 429,892-clause CNF and 656 MB compressed DRAT replayed to `s VERIFIED`.
All three exact-six branches are therefore excluded, giving fixed-seed
deletion radius at least seven but no seven-deletion witness and no new global
Ramsey bound. See
[R3_18_BUDGET6_BRANCH0_UNION_PROOF.md](R3_18_BUDGET6_BRANCH0_UNION_PROOF.md).

Budget-six semantic reconstruction and small regression tests:

```bash
.venv/bin/python -m routes.finite.test_r3_18_budget6_branch -v
.venv/bin/python routes/finite/check_r3_18_budget6.py \
  --json routes/finite/r3_18_budget6_check.json
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --json routes/finite/r3_18_budget6_branch_1_check.json
.venv/bin/python routes/finite/check_r3_18_budget6_branch0_union.py \
  --json routes/finite/r3_18_budget6_branch_0_universal_union_check.json
```
