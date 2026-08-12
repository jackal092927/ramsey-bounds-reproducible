# R(3,18), exact budget 6: branch 0/1 cut-bank merge closeout

Date: 2026-08-12

> **Subsequent update:** branch 1 was later closed by a fresh complete DRAT
> replayed to `s VERIFIED`; see `R3_18_BUDGET6_BRANCH1_PROOF.md`. The report
> below remains the historical closeout of the earlier bounded merge run.
> Branch 0 is still `UNKNOWN`, so the global claim boundary is unchanged.

## Verdict

Both branches remain **UNKNOWN**.  No separated Ramsey graph was found, and no
DRAT proof was completed and verified.  Consequently this closeout does **not**
prove the full fixed-seed budget-6 exclusion, a fixed repair radius of at least
7, or `R(3,18) >= 101`.

The run processed branches 0 and 1 only.  It did not start budget 7 and did not
extend either branch beyond the requested per-branch cumulative wall limit.

## Inputs and tools

The seed was
`certificates/r3_18_n100_nearmiss.txt` (SHA-256
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`).
The unchanged encoding script had SHA-256
`fcb9f27bff2fe9c1cc1d563d52bf1e57aba027548473ad0bb40757908522736c`.
The proof-producing CaDiCaL binary had SHA-256
`62d48c0890fae760c859e65676dc0598d59c36ac8170cbc5f115208d0a549429`
(source commit `c60730422e758ef1cebe7aeddf2dda31c996bf04`).  The pinned
`drat-trim` binary had SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`
(source commit `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`).

Preflight found 183 GiB free and no live branch solver.  Postflight found no
live `r3_18_budget6_branch`, CaDiCaL, or `drat-trim` process.

## Deduplicated merge

| branch | source-bank entries | distinct resumed I18 cuts | ordered-mask SHA-256 |
|---|---:|---:|---|
| 0 | 146,780 | 137,053 | `33500868514265841be0dfa47892f448722bcab1cabf6cbe014e96781d6dbbdf` |
| 1 | 79,800 | 59,335 | `d5fbcfc81c7d7d458808c024dd8f1a733acac789183d52588c8750bb40f14d7a` |

Branch 0 merged the pilot, grid `pre4096`, grid `batch16`, port `g0`, and port
`m0` banks.  Their respective entry counts were 160, 250, 2,080, 125,265, and
19,025.  Branch 1 merged the pilot, grid `pre4096`, grid `batch16`, Glucose,
port `g1`, and port `m1` banks, with 80, 80, 2,560, 7,740, 53,870, and 15,470
entries.  Every retained mask had popcount 18.

The first proof-producing replay reconstructed each deduplicated finite CNF,
including 4,096 fixed preload clauses.  CaDiCaL returned SAT for both finite
relaxations (branch 0: 141,149 unique I18 clauses, 319,270 total clauses;
branch 1: 63,431 unique I18 clauses, 241,552 total clauses).  These SAT models
were not fully separated, so they are not graph witnesses and carry no Ramsey
implication.

## Bounded complete-separation attempts

### Branch 0

The 700-second CEGAR stage ended at the discovery wall.  Its last atomic
checkpoint was `RUNNING`, iteration 90, with 46,080 new cuts and 183,133 total
resumed-plus-new cuts.  Its ordered-mask SHA-256 was
`9882ed1ed23291bfbff58a3812d104ad63166f9d991a6b8b64297795d2326f03`.
Because neither `SAT_SEPARATED` nor a finite-bank UNSAT state was reached, no
proof solver was started for this expanded bank.  Status: **UNKNOWN**.

### Branch 1

The worker atomically checkpointed `UNSAT_FINITE_CUT_BANK` at iteration 2 after
212.118 seconds, with 512 new cuts and 59,847 resumed-plus-new cuts (ordered-mask
SHA-256
`76be716c0a01ab5fcfc951fb813023607255ac3fc8df0d9935490421cfe3b440`).
The large result payload did not return through the multiprocessing queue before
the 700-second parent wall, so the outer closeout correctly remained UNKNOWN.

The checkpoint bank was then independently reconstructed with the fixed preload:
63,943 unique I18 clauses and 242,064 total CNF clauses.  Its cut-bank SHA-256 is
`f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c`;
the deterministic gzip CNF SHA-256 is
`a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14`
(uncompressed SHA-256
`ced3fd39370b4c2552cb261638fb7076da173e18d6b871f6fb280668e5a1154a`).
Proof-producing CaDiCaL did not finish before the cumulative branch cutoff and
was terminated.  `drat-trim` was not run.

The interrupted output is quarantined as
`incomplete/r3_18_budget6_branch_1.partial.drat.gz`.  It fails `gzip -t` with
unexpected EOF and is explicitly **incomplete, unverified, and not a proof
artifact**.  It is excluded from the hash-pinned evidence set.  Status:
**UNKNOWN**.

## Hash-pinned closeout evidence

| file | SHA-256 |
|---|---|
| `r3_18_budget6_branch_0.checkpoint.json` | `f65b9cedfe9781a9b6cd15bf83e24ffe474e3ac9c1462ba3755e609617dd267a` |
| `r3_18_budget6_branch_1.checkpoint.json` | `b0f3d9463b2003e642c57533a8f375c5ec85a08067b930c5794b2f8c185a9e1a` |
| `r3_18_budget6_branch_0_closeout.json` | `f0fe990741bea65a9e890d7c63c4fd0bcc8bc060ecba01ef2d235f6300bfbe6d` |
| `r3_18_budget6_branch_1_closeout.json` | `e7a0b95cfd0b0bc41c21e4c0b43ed48a01ca8c5e367bb63973faabee063f6662` |
| `r3_18_budget6_branch_0_initial_merge.cnf.gz` | `85c9932866f4e719a1b8d2d526d675e8089d4db84b4c7ca5a863b43c4613c686` |
| `r3_18_budget6_branch_0_initial_merge.cuts.json` | `1018283cf44a79625a70bb1c1441d7a22e8b98b0c08125af4df57bdf90120617` |
| `r3_18_budget6_branch_0_initial_merge.json` | `370fc7f624c2dd7ba8645f0312de3d0f2304fa75afc5cb5ebdde20787fb3ad8a` |
| `r3_18_budget6_branch_1_initial_merge.cnf.gz` | `96dd6f22991d30757f3082fb835d5513ce8aed55f9efe6369e29fb3b6db7a7a1` |
| `r3_18_budget6_branch_1_initial_merge.cuts.json` | `f9b6e9c6742672a5519e2217df7bdb771297a42a0e9efbf5e33c26fdb8234556` |
| `r3_18_budget6_branch_1_initial_merge.json` | `4c828ead0962d1da0d3934c0708791bcc202d02c039f4ec0ef52d4677a2314ca` |
| `r3_18_budget6_branch_1.cnf.gz` | `a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14` |
| `r3_18_budget6_branch_1.cuts.json` | `f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c` |

The two initial-merge JSON files use the generic reason text “proof emission did
not finish,” but their structured `external_proof_run.status` fields are `SAT`.
They therefore document only satisfiable finite relaxations, not UNSAT attempts.
