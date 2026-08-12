# R(3,18) fixed-near-miss budget-six closure

Date: 2026-08-12

## Verdict

**Exact-budget-six branch 0 is UNSAT with a complete `drat-trim`-verified
proof.** Together with the previously verified branches 1 and 2 and the
earlier proof of the deletion-budget-at-most-five ball, this excludes every
repair of the frozen 100-vertex near miss that deletes at most six input edges,
while allowing arbitrary additions among original nonedges.

Thus the fixed seed's deletion repair radius is at least seven under these
edit semantics. This does **not** prove that a seven-deletion repair exists,
does not construct a 100-vertex $(3,18)$ Ramsey graph, and does not establish
$R(3,18)\ge101$.

## Exhaustive cover

The seed has SHA-256
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`,
827 edges, no independent 18-set, and exactly one triangle, $(97,98,99)$.
Every triangle-free repair must therefore omit at least one of

$$
(97,98),\qquad(97,99),\qquad(98,99).
$$

The earlier proof-carrying result excludes all repairs using at most five
input-edge deletions. Any still-possible repair within budget six must hence
use exactly six. Each branch fixes one triangle edge absent and counts exactly
five residual deletions among the other 826 input edges. The three exact-six
branches now have complete checked DRAT proofs:

| branch | fixed absent edge | status |
|---:|---|---|
| 0 | $(97,98)$ | `UNSAT_PROOF_VERIFIED` |
| 1 | $(97,99)$ | `UNSAT_PROOF_VERIFIED` |
| 2 | $(98,99)$ | `UNSAT_PROOF_VERIFIED` |

## Universal-cut transfer and semantic audit

For every 18-subset $S$, every graph with no independent 18-set satisfies

$$
\bigvee_{e\in\binom S2}x_e.
$$

This clause is independent of the triangle-edge branch. We therefore audited
and deduplicated all available branch-0 cuts plus valid $I_{18}$ hitting
clauses from the checked branch-1, branch-2, and budget-five banks. The union
contains 251,771 distinct 18-subsets. No solver conclusion or learned clause
was transferred.

The final branch-0 finite relaxation was independently reconstructed clause by
clause:

| block | clauses |
|---|---:|
| all triangle clauses | 161,700 |
| exact-five sequential counter | 16,420 |
| fixed unit $\neg x_{97,98}$ | 1 |
| universal $I_{18}$ hitting clauses | 251,771 |
| **total** | **429,892** |

It has 13,160 variables. Every trailing clause was checked to be the 153
distinct positive primary variables for the complete pair set of one
18-subset. The finite formula is a relaxation of the exact branch; its checked
UNSAT status therefore excludes the full branch.

## Fresh proof

The exploratory PySAT solve independently reached finite-bank UNSAT after
201.811 seconds, but that label was not used as proof. Pinned CaDiCaL 3.0.1
was started from the frozen DIMACS and returned exit code 20 and
`UNSATISFIABLE`. It produced a 3,493,847,713-byte raw DRAT with 6,649,939
lines.

Pinned official `drat-trim`, source commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, executable SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`,
returned exit code 0 and `s VERIFIED`. It reported 295,963 of 3,299,012 lemmas
in the core, 135,152,646 resolution steps, and zero RAT lemmas in the core.

## Frozen artifacts

| artifact | bytes | SHA-256 |
|---|---:|---|
| `r3_18_budget6_branch_0_universal_union.cnf.gz` | 17,600,735 | `47052de808b98598f2f144251a6ad73c1415dd00fef9e04b99ffe2f176229fbf` |
| `r3_18_budget6_branch_0_universal_union.cuts.json` | 8,308,702 | `91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b` |
| `r3_18_budget6_branch_0_universal_union.drat.gz` | 656,144,450 | `4d948ab34f1d2475af6efe943e0a4899827c78b96c2bc3835b5161f189c26bb5` |
| raw CNF | 174,796,028 | `0dec49bdbee74644db5fc181e25f7df02a72dfd1b23a3ab4f859501de8a0d3cd` |
| raw DRAT | 3,493,847,713 | `43dde468b13a1f45667b0a8dc54c2c7d14b0b33f6dc01d85383b0a37f5ffca91` |
| `check_r3_18_budget6_branch0_union.py` | — | `1e70628276c8279876af8089dea0b12164014a06a5733588570347399802fe45` |
| semantic audit JSON | — | `d27b829f5fdc56af7553143f27a2da074ff10fe731ce45c365bd00041694b435` |

Both compressed formula and proof pass `gzip -t`; no proof or solver process
remained after freezing.

## Reproduction

Rebuild the transferred cut union and formula:

```bash
.venv/bin/python routes/finite/build_r3_18_budget6_branch0_union.py
```

Audit artifact identities and reconstruct all formula clauses:

```bash
.venv/bin/python routes/finite/check_r3_18_budget6_branch0_union.py \
  --json routes/finite/r3_18_budget6_branch_0_universal_union_check.json
```

For a full proof replay, add the pinned checker:

```bash
.venv/bin/python routes/finite/check_r3_18_budget6_branch0_union.py \
  --drat-trim /absolute/path/to/pinned/drat-trim \
  --drat-seconds 360
```
