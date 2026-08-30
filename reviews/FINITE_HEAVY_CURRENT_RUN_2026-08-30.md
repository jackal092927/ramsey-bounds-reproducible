# Finite-heavy current-run record

Date: 2026-08-30  
Scope: local post-repair worktree; this is not the final clean-clone release
attestation.

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
| 0 | 429,892 | 6,649,939 | 135,152,646 | 294.95 |
| 1 | 242,064 | 5,590,150 | 209,897,525 | 191.44 |
| 2 | 183,543 | 2,837,771 | 182,817,377 | 84.09 |

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
