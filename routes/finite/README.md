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

### Exact-seven branch-1 deletion-first pilot

`r3_18_budget7_benders_branch1.py` is a bounded diagnostic for only the
`(97,99)` branch.  Its master chooses exactly six residual input-edge
deletions, derives locally eligible additions from common-neighbour wedges,
enforces the necessary degree bound \(\deg(v)\le 17\), and separates
conditional independent-18 cuts.  The degree bound is exact as a necessary
condition: in a triangle-free graph every open neighbourhood is independent,
so `alpha < 18` forces its size to be at most 17.  A fixed-deletion add-only
subproblem checks collective triangle constraints and the same degree bound
exactly.  An `UNKNOWN` subproblem always stops without adding a deletion
no-good.

A small local smoke run, with all output kept outside the frozen artifact
tree, is:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python \
  routes/finite/r3_18_budget7_benders_branch1.py \
  routes/finite/certificates/r3_18_n100_nearmiss.txt \
  --initial-fixed-base-cuts 256 \
  --master-conflicts-per-call 100 \
  --master-max-conflicts 1000 \
  --master-per-call-seconds 1 \
  --max-seconds 10 \
  --oracle-order bidirectional \
  --sub-max-conflicts 1000 \
  --sub-max-seconds 2 \
  --checkpoint /tmp/r3_18_b7_b1.checkpoint.json \
  --json /tmp/r3_18_b7_b1.json \
  --candidate /tmp/r3_18_b7_b1_candidate.txt
```

For a stronger bounded pilot, add the checked universal bank with
`--universal-bank routes/finite/r3_18_budget6_branch_0_universal_union.cuts.json`
and use `--all-fixed-base-cuts`.  The checkpoint contains only deterministic
conditional cuts and fixed-deletion no-goods obtained from completed UNSAT
solver endpoints; those no-goods are solver-trusted but are not proof-checked.
Use `--resume` to import that state.  Every checkpoint's `formula` object is a
current snapshot (including installed masks, no-goods, and total clauses), and
the twelve-entry `last_master_models` ring records the sorted selected-`y`
edge support needed to replay either oracle.  Repository inputs are recorded
repository-relatively; external output paths are reduced to basenames.
Minisat22 is the default because this runner requires a backend that supports
resumable conflict-limited SAT slices.

Both master and fixed-deletion separators use the explicit `--oracle-order`
schedule.  `ascending` is the historical low-bit recursion, preserved as a
direct call to the original enumerator for replay of runs made with script
SHA-256
`36dc3b53941605bc4ec132b70b4f61c5afbbcda13742fe9056a38ddb1683e5a0`.
`reverse` applies the same exact recursion after the deterministic relabeling
`99,98,...,0`.  The default `bidirectional` mode starts `reverse` with half
the configured node threshold and wall budget, then gives the remaining
aggregate budget to `ascending`.  The historical enumerator may visit
threshold plus one nodes, and the aggregate accounting preserves that
convention. Relabeling changes only search order: every returned mask is
mapped back to the original labels before a cut is formed.
Resource-limited passes remain `UNKNOWN`; only a pass that exhausts its search
space can certify absence.  Checkpoints record the chosen schedule and each
pass's limits, nodes, time, witnesses, and completion status.  The CNF and its
strict-state fingerprint are independent of oracle order, so a resumed run may
change schedules without importing any heuristic exclusion.

If the master support oracle reaches its node or wall limit without finding a
new independent-18 witness, the runner records
`MASTER_ORACLE_INCOMPLETE_FALLBACK_TO_EXACT_SUBPROBLEM` and sends the same
six-edge deletion set to the exact add-only subproblem; the selected `y` edges
are only a phase hint.  If the exact subproblem is SAT, the candidate still
passes both the bitset checker and a separate vertex-selection SAT checker,
plus an observed-versus-declared exact-seven edit check.  If it is UNSAT, only
a solver-trusted deletion no-good is learned.  If it is UNKNOWN, the run stops
and learns nothing from that endpoint.

This pilot emits no DRAT.  A reported UNSAT endpoint is therefore unchecked
and is not a theorem; in particular, neither a fixed-deletion no-good nor a
master UNSAT endpoint establishes the branch theorem without proof-producing
reconstruction.  A verified SAT witness would establish `R(3,18) >= 101`, but
no such witness is presently claimed here.

### Exact-seven branch-1 singleton certificates

The strongest current branch-1 proof antichain consists of four singleton
consequences in the frozen common relaxation:

```text
x_11,62 = x_18,61 = x_18,64 = x_18,69 = 1.
```

Each negated singleton has a standalone checked DRAT refutation. The
PySAT-free semantic checker reconstructs all 718,453 clauses byte for byte,
and the strict proof replay accepts only the four declared singleton asset
pairs and one of two audited `drat-trim` binary hashes. A separate complete
model audit proves the 718,452-clause common relaxation satisfiable and
recovers an explicit independent 18-set, so the model is not a target repair.
The full claim boundary, hashes, cross-architecture replay, and exact support
counts are in
[R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md](R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md).

Targeted source checks are:

```bash
.venv/bin/python -m unittest \
  routes.finite.test_check_r3_18_budget7_branch1_core_cnf \
  routes.finite.test_check_r3_18_budget7_branch1_core_proofs \
  routes.finite.test_check_r3_18_budget7_branch1_common_sat -v
```

These certificates prune branch 1 but do not close it. Exact seven remains
`UNKNOWN`, and no `R(3,18)>=101` claim follows.

### Exact-seven degree--distance-two domination separator

The bounded structural separator in
[R3_18_BUDGET7_BRANCH1_DOMINATION_SEPARATOR_2026-08-30.md](R3_18_BUDGET7_BRANCH1_DOMINATION_SEPARATOR_2026-08-30.md)
implements the necessary condition
`deg(v) + alpha(F[Z_v]) <= 17`, where `Z_v` contains nonneighbors of `v`
having no common neighbor with `v`.  Its independent audit of the frozen
common model finds one new degree-17 independent-18 mask and no degree-16
mask.  This is an ordinary valid independent-set clause, not a stronger
relaxation, branch refutation, or Ramsey-number improvement.

Production overlap classification is fail-closed: the universal, historical,
and A+ mask files must match their exact SHA-256 and mask count; symlinks,
non-regular files, duplicate JSON keys, and duplicate masks are rejected.
The accepted basename, byte count, mask count, and digest of all three inputs
are recorded in the audit JSON.  The scripted bounded CEGAR state machine has
fixed limits of 16 SAT models, 65,536 novel masks, 4,096 degree-16 masks per
model, and 900 aggregate seconds.  It has not been connected to or used to
start a live solver.

The reproducible files are pinned as follows:

| file | SHA-256 |
|---|---|
| `check_r3_18_budget7_branch1_domination_witnesses.py` | `a612d431df71fdc7c8eb7cf96afd73aa9371d0af2de1a821068de23806f976b6` |
| `r3_18_budget7_branch1_domination_cegar.py` | `ef1051c948ef2f615d3313de8a6151805c42fa07ad70fe002f2938bdf340c202` |
| `test_r3_18_budget7_branch1_domination_cegar.py` | `8fd35c5316e550ac541fffacf9edf793605626d7e95ae4dc9c0cdd21fc6b0351` |
| `r3_18_budget7_branch1_domination_witness_audit.json` | `e9ccc8a14c6375e47809f4231e15a0926e76500e5bb8950761a66df3a7c41cd2` |
| `r3_18_budget7_branch1_domination_separator_design.json` | `479f9cb616e5ec26257f3db2a4abf8cdbb2743567cf6a6405c7eddbf2a4d68a5` |
| `R3_18_BUDGET7_BRANCH1_DOMINATION_SEPARATOR_2026-08-30.md` | `f0fda1e629ef28ad4b19b17a81e8eb7f666e0ddb1ea9c2e9f41f5c452e9383b9` |

The 15 asset-light regression tests are:

```bash
.venv/bin/python -m unittest \
  routes.finite.test_r3_18_budget7_branch1_domination_cegar -v
```

They include a same-count mask-file substitution regression, so retaining a
count while changing file content cannot forge a zero-overlap result.  Every
cap, timeout, incomplete scan, stale or malformed model, backend error, and
unchecked UNSAT endpoint remains explicitly non-theorem `UNKNOWN` or
`UNSAT_UNCHECKED` evidence.

### Exact-seven branch-1 full mask union

The solver-free builder and checker in
[build_r3_18_budget7_branch1_full_mask_union.py](build_r3_18_budget7_branch1_full_mask_union.py)
authenticates and deduplicates the universal, historical, exhaustive
fixed-base, and A+ independent-18 mask families. The three older families
have 526,429 distinct masks after 25,437 duplicate memberships are removed;
the 4,096 A+ masks are disjoint, giving 530,525 masks in total. Since the
common CNF already contains the 251,771 universal masks, the deterministic
augmentation adds four proof-checked positive units and 278,754 new I18
clauses.

The resulting 154,190-variable, 997,210-clause plain DIMACS file has
390,604,816 bytes and SHA-256
`4f7e8f5b724a657888c7814d2c25cac41c283c3db356fb8f1a15f4c7322c375d`.
It was constructed without a solver and audited line by line; the large CNF
is reproducible and is not stored in Git. This is materially stronger than
the earlier A+ gate: that gate used history and fixed base only as exclusion
families and its checked SAT model violates a mask in both. It is also not a
duplicate of Benders `--all-fixed-base-cuts`, which uses projected master
clauses and omits 43,614 history-only plus 4,096 A+ masks.

Full overlap counts, input and output hashes, the 11-test regression, and the
one-run/300-second optional-probe stop rule are in
[R3_18_BUDGET7_BRANCH1_FULL_MASK_UNION_2026-08-30.md](R3_18_BUDGET7_BRANCH1_FULL_MASK_UNION_2026-08-30.md).
That solver-free formula alone has no endpoint claim.

### Exact-seven branch-1 maximal-union gate

The maximal-union gate combines the complete mask union above with the full
all-pair maximal-triangle-free selector normal form.  The deterministic CNF has
639,290 variables, 1,972,360 clauses, 408,370,088 bytes, and SHA-256
`09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb`.
Independent reconstruction matched byte for byte.  The generator and checker
reject symlinked authenticated inputs at their command-line boundary; two
regression tests cover the formerly vulnerable pre-validation path handling.
A separate deterministic 1-WL audit reaches 100 singleton colors after two
refinement rounds and therefore certifies that the seed automorphism group is
trivial; branch-1 results cannot be transferred to branches 0 or 2 by
relabeling.

Exactly one externally bounded Sirius call ran for 300 seconds.  The wrapper
returned 124 and the result was `c UNKNOWN`; no complete model, replayed proof,
or learned cut resulted.  The incomplete 922,038,097-byte DRAT prefix was
hashed and deleted, so it is not a certificate.  The sanitized endpoint and
fail-closed audit are
`r3_18_budget7_branch1_maximal_union_probe.json` and
`r3_18_budget7_branch1_maximal_union_probe_audit.json`.  Recheck them with:

```bash
.venv/bin/python \
  routes/finite/check_r3_18_budget7_branch1_maximal_union_probe.py
```

Full design, reconstruction, endpoint, and stop-rule details are in
[R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md](R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md).
Branch 1 and exact seven remain `UNKNOWN`; there is no global Ramsey-number
implication.
