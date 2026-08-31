# Degree--distance-two domination separator

Date: 2026-08-30  
Scope: exact-seven branch 1, fixed edge `(97,99)` absent  
Status: **IMPLEMENTED AND MODEL-AUDITED; SOLVER GATE NOT RUN**

## Mathematical lemma

Let `F` be triangle-free with `alpha(F)<18`, and define

```text
Z_v = {u != v : uv is absent and N_F(u) intersect N_F(v) is empty}.
```

The open neighbourhood `N_F(v)` is independent. Every independent set in
`F[Z_v]` is nonadjacent to every vertex of `N_F(v)`, so

```text
deg_F(v) + alpha(F[Z_v]) <= 17.
```

Consequently:

- if `deg_F(v)=17`, then `Z_v` is empty; every `u in Z_v` otherwise gives
  the explicit independent 18-set `N_F(v) union {u}`;
- if `deg_F(v)=16`, then `alpha(F[Z_v])<=1`; every nonedge `{u,t}` in
  `F[Z_v]` gives the explicit independent 18-set
  `N_F(v) union {u,t}`.

Each emitted set yields the universally valid 153-literal clause requiring
at least one edge inside that 18-set. The lemma is a structured source of
ordinary independent-set clauses; a bounded run remains a relaxation of the
complete Ramsey constraint.

## Independent common-model audit

`check_r3_18_budget7_branch1_domination_witnesses.py` imports neither PySAT,
the production formula builder, nor the existing common-model checker. It:

1. parses a complete gzip CaDiCaL model with all 154,190 variables assigned;
2. reconstructs the first 4,950 edge variables in lexicographic pair order;
3. checks square, loop-free, symmetric, triangle-free graph semantics;
4. regenerates every degree-17 witness and every degree-16 witness;
5. directly checks each emitted mask has size 18 and is independent; and
6. authenticates the universal, historical, and A+ mask files by exact file
   SHA-256 and exact mask count, rejecting symlinks, non-regular files,
   duplicate JSON keys, and duplicate masks; and
7. classifies membership in those three families and the fixed-base family.

The production mask identities are:

| family | masks | file SHA-256 |
|---|---:|---|
| universal | 251,771 | `91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b` |
| historical | 64,591 | `d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0` |
| A+ | 4,096 | `835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b` |

The accepted basename, byte count, mask count, and digest of each family are
stored in the audit JSON. Thus a same-count replacement cannot preserve a
zero-overlap verdict.

The frozen common-model audit is recorded in
`r3_18_budget7_branch1_domination_witness_audit.json`. It checked the pinned
model gzip SHA-256

```text
9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d
```

and found degree distribution `50 x 16 + 50 x 17`. The only nonempty `Z_v`
records are

```text
v=37, degree=16, Z_37={86}
v=86, degree=17, Z_86={37}.
```

There is therefore no degree-16 witness and exactly one degree-17 witness:

```text
mask = 2000000404414192982822020
set  = {5,13,17,23,25,31,32,35,37,40,43,44,50,52,58,62,70,97}.
```

Its overlap counts with the 251,771 universal masks, 64,591 historical masks,
4,096 A+ masks, and exhaustive fixed-base family are all zero. This is one
new valid clause in one model of an incomplete relaxation. It is not a repair,
a branch refutation, or evidence for a global Ramsey-number improvement.

## Bounded CEGAR engine

`r3_18_budget7_branch1_domination_cegar.py` separates the state machine from
the solver backend. The module itself launches no solver. A backend must
return a strict `SAT`, `UNSAT`, or `UNKNOWN` event. For every SAT event the
engine validates the graph, rejects stale models that violate a learned
clause, emits every degree-17 witness, and emits at most 4,096 degree-16
witnesses in deterministic lexicographic order.

The production limits are immutable:

| gate | limit |
|---|---:|
| returned SAT models | 16 |
| novel structural masks | 65,536 |
| degree-16 masks per model | 4,096 |
| aggregate wall | 900 seconds |
| productivity checkpoint | after 8 models |
| minimum novel masks at checkpoint | 2 |
| minimum novel/candidate ratio | 25% |

At the productivity checkpoint, either failed threshold stops the run as
`UNKNOWN_LOW_PRODUCTIVITY_STOP`. Every wall, cap, malformed model, stale
model, backend error, truncated-but-unresolved degree-16 scan, or old-only
witness endpoint is also `UNKNOWN`. No UNKNOWN state is resumed or converted
into evidence, and no automatic second run, solver swap, larger wall, or
larger batch is authorized by this design.

`SAT_DOMINATION_SEPARATOR_CLOSED_MODEL` means only that the returned model has
no witness in this structural family. It must not be described as an
exact-seven candidate without the complete independent-set, triangle, and edit
verifiers. `UNSAT_UNCHECKED_DOMINATION_FORMULA` is likewise not theorem
evidence. The engine never self-promotes UNSAT, even if a backend Boolean says
that a proof was checked. Promotion is admissible only in a separate external
record that authenticates and replays the exact final CNF and proof. If proved
singleton units are installed, that record must also bind and replay all four
singleton proof chains.

## Tests and reproduction

The asset-light regression is

```bash
.venv/bin/python -m unittest \
  routes.finite.test_r3_18_budget7_branch1_domination_cegar -v
```

It covers exact degree-17 and degree-16 witness semantics, malformed graphs,
strict model parsing, 153-literal clause generation, SAT/UNSAT/UNKNOWN
distinctions, rejection of backend self-promotion, wall/model/mask caps,
degree-16 truncation, and the low-productivity stop.
It also checks that same-count replacement files, symlinks, duplicate JSON
keys, and duplicate masks are rejected before overlap classification.

The production audit can stream the frozen model from Sirius without copying
it into the repository:

```bash
ssh sirius \
  'cat /common/home/cx122/iWorld/ireserch/Ramsey/runs/gap_common_formula_probe_20260830/branch1_common.model.gz' \
| .venv/bin/python \
    routes/finite/check_r3_18_budget7_branch1_domination_witnesses.py \
    --model -
```

This command only reconstructs and checks the stored model. It does not start
a solver. The CEGAR command-line surface accepts scripted events for
deterministic integration; a live solver gate remains deliberately not run in
this record.
