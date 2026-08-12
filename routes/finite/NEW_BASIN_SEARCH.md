# New-basin finite Ramsey search

Date: **2026-08-12**  
Global verdict: **no new Ramsey bound; one new exact local exclusion radius**

## Purpose and claim boundary

This experiment deliberately leaves the previously studied 11-triangle
single-hub basin for R(3,13), and compares it with a small-edit extension of
the public 159-vertex R(4,15) graph. All terminating labels below retain
their literal SAT meaning:

- `UNSAT` excludes only the stated fixed input and edit family;
- `UNKNOWN_*` and `TIME_LIMIT` prove no nonexistence statement;
- no valid 61-vertex (3,13)-graph or 160-vertex (4,15)-graph was found.

In particular, the experiment does **not** improve a global Ramsey-number
bound.

## Correction to the proposed k=10 entrance

The existing file `r3_13_n61_frozen_nearmiss_k10.txt` is not a non-hub seed.
Exact reconstruction gives the ten triangles

```text
(0,34,60), (25,34,60), (28,34,60), (30,34,60), (33,34,60),
(34,35,60), (34,38,60), (34,40,60), (34,43,60), (34,54,60).
```

They all contain edge (34,60). The earlier `k10` label means only “ten
triangles”; it must not be read as “non-hub.”

A stricter SAT model was therefore constructed over the new vertex’s 60
neighborhood variables. It requires:

1. exactly ten base edges induced by the neighborhood, hence ten triangles;
2. all 106,246 independent 12-sets of the frozen base to be hit;
3. every old vertex to occur in at most nine of those ten induced edges.

Condition 3 excludes a new–old edge common to all ten triangles. Exact
reification uses one indicator per base edge, both implication directions, an
exact-ten cardinality constraint, and the 60 incident-degree constraints.

The fully preloaded MiniSat22 run reached the 180-second limit after 732,692
conflicts without reaching a model:

```text
status                         UNKNOWN_GLOBAL_WALL_LIMIT
preloaded I12 clauses          106,246 (the complete base family)
initial clauses                123,288
SAT/CEGAR models reached       0
conflicts                      732,692
wall time                      180.01 s
```

Thus existence of a non-hub frozen-optimal k=10 extension remains **open**.
The run is not UNSAT.

## New non-hub k=11 seed

Relaxing exact triangle count from ten to eleven while retaining a maximum
incident count of ten immediately produced
`r3_13_n61_nonstar_k11.txt`:

```text
input SHA-256       d619f0bfed32af5e2fbc8c724d9c65dbf388a19d5647d20e7835b501bc03227a
output SHA-256      2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b
vertices / edges    61 / 363
triangles           11
independent I13     0
max triangles on one edge  10
```

Its triangles are

```text
(19,28,60), (22,28,60), (24,28,60), (27,28,60),
(28,29,60), (28,32,60), (28,34,60), (28,37,60),
(28,48,60), (28,58,60), (37,46,60).
```

The first ten share (28,60), while the last does not. This is a minimal
departure from single-hub geometry, not a claim of a completely dispersed
triangle family. The independent bitset verifier finds no I13, and
independently recounts a forbidden K3; hence it is a near miss rather than
a Ramsey certificate. A separately encoded CaDiCaL vertex-selection verifier
agrees: K3 is SAT and I13 is UNSAT.

The exact minimum number of seed edges meeting all eleven input triangles is
two. One witness is

```text
(28,60), (37,46).
```

The transversal routine was checked against exhaustive subset search on 320
random graphs of orders three through six.

## Exact edit radius around the new seed

For each deletion budget d, every one of the 1,830 possible final edges is a
SAT variable. All 35,990 triangle
clauses are installed initially. At most d edges present in the seed may be
deleted, while **every original nonedge may be added without charge**.
Independent 13-set clauses are added lazily by the exact bitset oracle.

The CaDiCaL 1.9.5 replay gives:

| deletion budget | status | CEGAR iterations | I13 cuts | seconds |
|---:|---|---:|---:|---:|
| 2 | `UNSAT` | 2 | 1 | 0.022 |
| 3 | `UNSAT` | 7 | 6 | 0.035 |
| 4 | `UNSAT` | 16 | 15 | 0.117 |
| 5 | `UNSAT` | 46 | 45 | 0.767 |
| 6 | `UNSAT` | 137 | 136 | 2.890 |
| 7 | `UNSAT` | 239 | 238 | 16.887 |
| 8 | `TIME_LIMIT` | 406 | 406 | 69.259 |

The d=2 minimum-transversal entrance was also split into its three possible
two-edge triangle covers and checked separately with add-only CaDiCaL
subproblems; every subproblem returned UNSAT after one I13 cut. Their machine
records are frozen as `new_basin_r3_nonstar_k11_split_0.json` through
`new_basin_r3_nonstar_k11_split_2.json`. The
bounded MiniSat22 master independently agrees for d=2,...,6. Its
d=7 run stopped at one million conflicts and remains
`UNKNOWN_GLOBAL_CONFLICT_LIMIT`; that does not weaken the completed CaDiCaL
UNSAT result.

Therefore any successful graph in this **new fixed-seed edit family** must
delete at least eight of the seed’s 363 edges. This is an exact local result,
not an upper bound on R(3,13). Budget eight remains open.

## Competing R(4,15) entrance

The alternative entrance starts from the independently checked public
159-vertex graph (SHA-256
`05bf670069207edad54951a960c194eee9f67cb033dae1e8be3bf0306f7dde1f`).
The restricted small-edit family allows:

- an arbitrary neighborhood for vertex 159;
- deletion of at most one of the 3,761 old edges;
- no addition between two old vertices.

The 14,084 old triangles generate exact new-vertex K4 clauses. Both old
I15 witnesses created by deletions and new-vertex I15 witnesses
are separated exactly. Its 60-second diagnostic ended
`UNKNOWN_GLOBAL_WALL_LIMIT` after four models and 256 new-vertex-side cuts.
No candidate was emitted.

This route is currently less attractive per CPU-second: exact I14
separation dominated the run, whereas the new R(3,13) seed admitted an
exact edit-radius proof through seven deletions. A future R(4,15) attempt
should precompute/maximalize I14 structure or use a portfolio/local
structural seed; simply repeating the present CEGAR loop is unlikely to be
efficient.

## Reproduction

Generate the non-hub seed with the complete blue family preloaded:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/new_basin_search.py seed-r3 \
  routes/finite/certificates/alphaevolve_R3_13_ge_61.txt \
  --triangles 11 --preload-blue --solver minisat22 \
  --conflict-chunk 5000 --max-conflicts 500000 \
  --per-call-seconds 8 --max-seconds 90 --batch-size 1024 \
  --output routes/finite/r3_13_n61_nonstar_k11.txt \
  --json /tmp/new_basin_seed.json
```

Replay the exact d=7 edit budget with the independent legacy CEGAR
implementation:

```bash
.venv/bin/python routes/finite/bounded_deletion_sat_cegar.py \
  routes/finite/r3_13_n61_nonstar_k11.txt 13 \
  --budget 7 --solver cadical195 \
  --json /tmp/new_basin_d7.json
```

Run the bounded budget-eight diagnostic instead of an unbounded call:

```bash
PYTHONUNBUFFERED=1 .venv/bin/python routes/finite/new_basin_search.py repair-r3 \
  routes/finite/r3_13_n61_nonstar_k11.txt \
  --budget 8 --solver minisat22 \
  --conflict-chunk 5000 --max-conflicts 1000000 \
  --per-call-seconds 8 --max-seconds 180 --batch-size 256 \
  --output /tmp/new_basin_d8_candidate.txt \
  --json /tmp/new_basin_d8.json
```

The canonical unit suite, including the exhaustive triangle-transversal oracle,
passes 13/13 tests:

```bash
.venv/bin/python -m unittest routes.finite.test_verify_ramsey -v
```

## Frozen evidence

| artifact | SHA-256 |
|---|---|
| `new_basin_search.py` | `944746b24989a12b73f45b111dcffcfd425f8b6d8132d7aa73b7c7a28f7da054` |
| non-hub k=11 matrix | `2e97d94560a4c3f30a70729ec5985e9a22f431a9d2e78b338994291b6d4c441b` |
| k=11 seed JSON | `b5d4f2d22274c8a26fed895a10c3fd8218b7b5ee2d46fe0686947f5899aaf6d6` |
| k=11 independent SAT verification | `248726f7ae91be94c4e1fe99256c690594fa90a494dd7811cd89071c6db32e7b` |
| non-hub k=10 UNKNOWN JSON | `416920ed7593995a8b12f9f71090088e2ab153c835f7232c19fe4a348d2143a6` |
| R(4,15), d=1 UNKNOWN JSON | `dd2061cff2db1590a62851c25d3591ee1bdef5aad74057b8942d35a109494560` |
| CaDiCaL d=7 JSON | `af0074acb487ada82298ea4b354461e1c0a17d335a592391cc6a70bdfd449a38` |
| CaDiCaL d=8 TIME_LIMIT JSON | `b47359f8a4161cc879440e4f6467de9c1bd2f45637e5d4232418a0f253f9c387` |
| d=2 split JSON 0 | `3371086dbb79f2c03447b40fd59d02428640f466be89ea9bac5b76a51ef2df3a` |
| d=2 split JSON 1 | `bd6516080efb8c6ecafbb5d4b67cd8916fdabe0c1dd522465d9d3f94cb37bbf4` |
| d=2 split JSON 2 | `12b5d84081ee6844ee282508042ec23991732755202a2e4fb3176777fad8ae4e` |

The per-budget CaDiCaL JSON files for d=2,...,8 are retained separately;
older hub-basin results and files were not overwritten.
