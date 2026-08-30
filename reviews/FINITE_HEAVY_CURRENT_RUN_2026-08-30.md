# Finite-heavy current-run record

Date: 2026-08-30  
Scope: local post-repair worktree; this is not the final clean-clone release
attestation.

Refresh note: this record was updated after the PySAT-independent
sequential-counter checker was added and the integrated driver was repaired to
keep that checker's command-line contract separate from the DRAT auditors. The
post-repair `reproduce.py` used by this run had SHA-256
`8531bd00e99e53cad7bb5a9a00ce10f9e3c8fe547159bbe2398d92cfc8934232`.

The integrated command

```text
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir routes/finite \
  --drat-trim /absolute/path/to/source-pinned/drat-trim
```

completed successfully and emitted
`FINITE_HEAVY_REPRODUCTION_PASS`.  Before replay, all twelve compressed
payloads matched `artifacts/MANIFEST.tsv`.  The checker was built from
`marijnheule/drat-trim` commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; the executable used in this run
had SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.

The same integrated invocation first ran
`routes/finite/check_r3_18_seqcounter.py` with only `--artifact-dir`. Its
SHA-256 was
`38cc478cc75f1211cfe248645cd0929be306303e6998126750bc0cdd307ef4b0`.
It imported no PySAT cardinality encoder and compared all six authenticated
DIMACS counter blocks clause-for-clause against the independent schema:

| branch family | branches | mode | clauses per counter | maximum variable | actual block compared |
|---|---:|---|---:|---:|---|
| budget five | 3 | at most four | 7,394 | 8,238 | yes, all three |
| exact six | 3 | exactly five | 16,420 | 13,160 | yes, all three |

The post-counter hitting-clause counts were `287`, `15,872`, and `8,704`
for budget five, and `251,771`, `63,943`, and `5,422` for exact six. The
independent schema module used in that comparison had SHA-256
`b66a3abc652dbadceb28f16cf635c7da23603ecfb75c45fb56df8dfcfa977baf`.

Current-run outcomes:

| layer | branch 0 | branch 1 | branch 2 |
|---|---:|---:|---:|
| budget-five formula semantics | VERIFIED | VERIFIED | VERIFIED |
| budget-five DRAT replay | VERIFIED | VERIFIED | VERIFIED |
| exact-six formula semantics | VERIFIED | VERIFIED | VERIFIED |
| exact-six DRAT replay | VERIFIED | VERIFIED | VERIFIED |

The exact-six checker outputs ended with `s VERIFIED`.  Their proof statistics
were:

| branch | clauses | raw DRAT lines | resolution steps | replay seconds |
|---:|---:|---:|---:|---:|
| 0 | 429,892 | 6,649,939 | 135,152,646 | 270.97 |
| 1 | 242,064 | 5,590,150 | 209,897,525 | 177.28 |
| 2 | 183,543 | 2,837,771 | 182,817,377 | 80.96 |

The three budget-five replays also ended with `s VERIFIED`; their current-run
wall times were 5.93, 14.03, and 8.41 seconds for branches 0, 1, and 2.

The exact-seven frozen-state audit also passed: all three bounded discovery
records remain `UNKNOWN_DISCOVERY_WALL_LIMIT`, no SAT witness was recorded,
and no UNSAT proof exists.  The theorem-level current-run summary therefore
reported:

```text
status: FINITE_THEOREM_REPRODUCED
fixed_seed_deletion_repair_radius_at_least_7: true
exact7_repair_exists: null
global_R_3_18_improvement: false
```

This record intentionally does not claim a public release, an anonymous
clean-clone replay, existence or nonexistence at exact seven, or an
improvement of the global Ramsey number.
