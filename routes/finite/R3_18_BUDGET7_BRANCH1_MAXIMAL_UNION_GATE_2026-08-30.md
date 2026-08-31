# Branch-1 maximal-union exact-seven gate

## Outcome

The production generator, independent checker, tests, and deterministic design
ledger are ready.  The design and production records themselves remain
solver-free and distinguish formula construction from scientific status.  A
subsequent single 300-second Sirius probe of the byte-audited production CNF
timed out with wrapper exit 124 and result `c UNKNOWN`.  It produced neither a
complete model nor a replayable proof.  Therefore the scientific endpoint is
**UNKNOWN / no learned cut / no branch closure**, not SAT or UNSAT.

The proposed formula starts from the authenticated branch-1 common relaxation
and installs two complementary strengthenings at once:

1. the complete deduplicated union of the universal, historical, exhaustive
   fixed-base, and A+ independent-18 families; and
2. a full maximal-triangle-free common-neighbour selector for every unordered
   pair of vertices.

It also installs the four positive edge units already justified by the checked
singleton DRAT certificates.

## Exact formula design

The common formula has 154,190 variables and 718,452 clauses.  Its 251,771
universal I18 clauses are already present, so they are not duplicated.

The four authenticated mask families have sizes

| family | masks |
|---|---:|
| universal | 251,771 |
| historical union | 64,591 |
| exhaustive branch-1 fixed-base family | 235,504 |
| A+ batch | 4,096 |

Their complete union has 530,525 masks.  Exactly 278,754 of these are absent
from the universal bank already in the common formula, and only these clauses
are appended.  The sorted 25-hex-digit digests are:

- prior three-family union: `f4220088cf6dfccc7b0e8b0aa7c2d1a2ef4a47f5ce31738506eefdd591613258`;
- four-family union: `f5c1c60877306900c1aa81bd3a7f357c3d16464ad329c676639a6f6bda9a682d`;
- appended union-minus-universal family: `2242d10f9ea3cefedef7a8c02be9a7df41db3cdb6580733e3fca9391db46d1d4`.

For each of the 4,950 pairs `uv`, the maximality encoding introduces 98
existential witnesses `y_uv_w`, one for each other vertex `w`, and emits

```text
x_uv OR y_uv_0 OR ... OR y_uv_97
not y_uv_w OR x_uw
not y_uv_w OR x_vw
```

The auxiliary allocation is deterministic: lexicographic pair-major order,
then ascending witness vertex, beginning at variable 154,191.  This contributes
485,100 variables and 975,150 clauses.  The final design therefore has exactly

```text
variables = 639,290
clauses   = 1,972,360
```

in the clause order common body, four positive units, sorted additional I18
clauses, and pair-major maximality clauses.

## Why this is a new gate

This is not another A+ prefix.  A+ appended 4,096 model-derived I18 masks to
the common formula.  The new gate installs every member of the four-family
union, including the historical and exhaustive fixed-base masks that A+ used
only as generation-time exclusions, and adds full all-pair maximality.

It is also not the Benders `--all-fixed-base-cuts` option.  That option
preloads the fixed-base I18 family into a deletion-support master.  This gate
is a direct primary-graph CNF over the common relaxation and simultaneously
contains the universal/history/fixed-base/A+ union, four retention units, and
maximality selectors.

## Branch and theorem boundary

The formula fixes deletion `(97,99)` and applies only to branch 1.  A separate
degree-initialized 1-WL diagnostic refines all 100 seed vertices to singleton
colors after two rounds, which implies that the seed automorphism group is
trivial.  Thus no triangle-edge symmetry transfers a result here to the
`(97,98)` or `(98,99)` branches.  The 1-WL observation is a scope diagnostic,
not an additional formula dependency.

The full maximality normalization relies on the already authenticated
one-sided radius-at-least-seven result: a deleted seed edge of a genuine
exact-seven target cannot be triangle-safe to add back, or it would produce an
at-most-six target.  Saturating original nonedges is free in the one-sided
metric and does not increase the independence number.  Consequently every
valid branch-1 exact-seven target has a branch-preserving maximal
triangle-free representative satisfying this formula.

A proof-checked UNSAT endpoint would therefore close only branch 1.  It would
not close the other two exact-seven branches or improve a global Ramsey bound
by itself.  A SAT endpoint containing an independent 18-set is only relaxation
telemetry.  A SAT endpoint with no independent 18-set must still pass the full
independent publication-promotion workflow before being advertised as a new
lower-bound witness.

## Fail-closed implementation

The generator:

- rejects symlinks, malformed JSON, duplicate keys and masks, wrong counts,
  and every SHA mismatch;
- independently enumerates all 235,504 fixed-base masks;
- writes raw DIMACS incrementally under a fixed byte cap;
- refuses overwrite and installs the output atomically;
- records every source SHA/count plus final raw CNF byte count and SHA;
- never invokes a solver.

The independent checker reconstructs every CNF line from the authenticated
common gzip and the four source families.  SAT promotion requires a complete
assignment of all 639,290 variables, evaluation of all 1,972,360 clauses, and
direct graph checks for triangle-freeness, exactly seven one-sided deletions,
the branch unit, four retained edges, maximum degree 17, maximality, and an
independent-18 search.

UNSAT promotion accepts neither an exit code nor a historical status bit.  It
requires a nonempty proof replayed against the exact recorded raw CNF by a
binary in the frozen SHA allowlist for drat-trim commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, with exit zero and exactly one
standalone `s VERIFIED` line.  Replay timeout, proof-byte cap, malformed data,
or any mismatch is UNKNOWN and learns nothing.

## Reproduction

The no-solver design audit is:

```bash
.venv/bin/python \
  routes/finite/r3_18_budget7_branch1_maximal_union_gate.py design \
  --output-record /tmp/maximal_union_design.json

.venv/bin/python -m unittest \
  routes.finite.test_r3_18_budget7_branch1_maximal_union_gate -v
```

With the authenticated `branch1_common.cnf.gz` release asset available, build
one production formula without solving it:

```bash
.venv/bin/python \
  routes/finite/r3_18_budget7_branch1_maximal_union_gate.py build \
  --common-cnf /path/to/branch1_common.cnf.gz \
  --output-cnf /path/to/branch1_maximal_union.cnf \
  --output-record /path/to/branch1_maximal_union_gate.json \
  --max-output-bytes 1000000000
```

Then independently reconstruct it:

```bash
.venv/bin/python \
  routes/finite/check_r3_18_budget7_branch1_maximal_union_gate.py cnf \
  --common-cnf /path/to/branch1_common.cnf.gz \
  --cnf /path/to/branch1_maximal_union.cnf \
  --record /path/to/branch1_maximal_union_gate.json
```

### Sirius bounded preflight (no solve)

After the branch containing this gate is available on Sirius, the following is
the exact remote build-and-reconstruction invocation.  It uses the frozen
common-CNF release asset already stored under the Sirius run directory.  It
creates a deterministic 408,370,088-byte CNF and its ledger, but **does not
start a SAT solver**; the only acceptable outcomes of this command are a
byte-exact reconstruction record or a fail-closed error.

```bash
ssh sirius '
  set -eu
  ramsey_repo=/path/on/sirius/to/Ramsey
  ramsey_run=/path/on/sirius/to/maximal_union_gate_20260831
  ramsey_common=/path/on/sirius/to/branch1_common.cnf.gz
  mkdir -p "$ramsey_run"
  cd "$ramsey_repo"
  python3 routes/finite/r3_18_budget7_branch1_maximal_union_gate.py build \
    --common-cnf "$ramsey_common" \
    --output-cnf "$ramsey_run/branch1_maximal_union.cnf" \
    --output-record "$ramsey_run/branch1_maximal_union_gate.json" \
    --max-output-bytes 1000000000 \
  && python3 routes/finite/check_r3_18_budget7_branch1_maximal_union_gate.py cnf \
    --common-cnf "$ramsey_common" \
    --cnf "$ramsey_run/branch1_maximal_union.cnf" \
    --record "$ramsey_run/branch1_maximal_union_gate.json" \
    --output "$ramsey_run/branch1_maximal_union_cnf_audit.json"
'
```

Expected CNF identity after this no-solver preflight is SHA-256
`09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb`,
with 639,290 variables and 1,972,360 clauses.  A later bounded solve must
preserve this raw identity, retain a complete model for the SAT path, or retain
a nonempty replayable proof for the UNSAT path; a timeout is simply UNKNOWN.

## Frozen bounded probe

The one authorized probe used CaDiCaL 3.0.1 at source commit
`c60730422e758ef1cebe7aeddf2dda31c996bf04`; the x86-64 binary SHA-256 was
`bd054bcc5864fd20c9ff117f8fff94f810f5b210014ff33971a6c1db1d0eca45`.
The external wall was 300 seconds, the proof format was non-binary DRAT, and
the proof-file cap was 10 GiB.  The wrapper returned 124 and the result file
contained exactly `c UNKNOWN`.  The solver reported 13,347 conflicts, 105,834
decisions, 1,216,037,481 propagations, and 1,897.78 MB peak RSS.  Those numbers
are resource telemetry only.

The interrupted run closed an incomplete 922,038,097-byte proof prefix with
SHA-256
`a6693fe2b3bab57f9d0e9ebe39bd7baa3883bfe2af15a5eb33b0aded972b5438`.
It was never replayed and was deleted immediately after hashing.  It is not a
partial certificate and is not evidence toward UNSAT.  No model or cut was
retained.

The sanitized endpoint ledger is
`r3_18_budget7_branch1_maximal_union_probe.json`, SHA-256
`e35f7761f92ddebdb4029553fe7a2828e31c79d68820d37b1aa2bb6ac4f80571`.
Its fail-closed checker verifies all eleven retained files, the exact timeout
result, the deleted-prefix boundary, and the absence of a retained proof:

```bash
.venv/bin/python \
  routes/finite/check_r3_18_budget7_branch1_maximal_union_probe.py
```

The audit record has SHA-256
`4e4e212f0c6bae101db00dfb118f602cc6f874e9d8833f3c43cc946432e2cc54`.
The endpoint remains branch-1 UNKNOWN; it does not transfer to the other two
triangle-edge branches and has no global Ramsey implication.

The tracked design ledger is
`r3_18_budget7_branch1_maximal_union_gate_design.json`, SHA-256
`266ca29292b61d14f033b402345cdab934d4702336cdd03fb9153b66925ed34d`.
It deliberately records `raw_cnf_sha256 = null`, because the design stage does
not build a CNF.  The separate production record has SHA-256
`cb3eaa1ed462713e13a951dbc113555ce8f1aa8325c266658d9cc32c8dd72026`
and binds the generated formula to the exact raw identity above.
