# R(3,18) fixed-near-miss deletion-budget-six audit

## Outcome

**Overall status: FIXED-SEED BUDGET AT MOST SIX UNSAT, PROOF VERIFIED.** No
100-vertex Ramsey certificate was found, but the full fixed-seed budget-six
edit ball is excluded under arbitrary original-nonedge additions.

The exhaustive triangle-edge split has three branches. Exact deletion budget
six is now proof-verified for all three branches:

| branch | fixed input edge absent | endpoint |
|---:|---|---|
| 0 | $(97,98)$ | UNSAT, universal-union DRAT independently VERIFIED |
| 1 | $(97,99)$ | UNSAT, fresh frozen DRAT independently VERIFIED |
| 2 | $(98,99)$ | UNSAT, frozen DRAT independently VERIFIED |

Together with the earlier checked budget-at-most-five result, this establishes
fixed-seed deletion repair radius at least seven. It proves neither existence
of a seven-deletion repair nor $R(3,18)\geq101$.

## Reduction and semantics

The frozen 100-vertex near miss has SHA-256
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`,
contains no $I_{18}$, and has the unique triangle $(97,98,99)$. Every
triangle-free final graph therefore omits at least one of its three edges.

The earlier checked proof excludes every repair with at most five input-edge
deletions, even when arbitrary original nonedges may be added. Hence a new
budget-six solution must delete exactly six input edges. Each branch fixes one
triangle edge absent and encodes exactly five further deletions among the other
826 input edges. Original nonedges are not in this cardinality counter and
remain free edge variables.

All $\binom{100}{3}=161700$ triangle clauses are installed. Independent
18-sets are exact separator witnesses; each contributes the necessary clause

$$
\bigvee_{e\in\binom{S}{2}}x_e.
$$

A finite subset is a relaxation of the full problem, so checked UNSAT of such
a finite CNF suffices for branch exclusion. A solver-level UNSAT without a
checked proof does not.

## Branch-0 universal-union proof artifact

The branch-0 follow-up transferred only universally valid $I_{18}$ hitting
clauses from the existing checked cut banks. After validation and
deduplication the union contains 251,771 distinct 18-subsets. No learned
clause or solver conclusion was transferred.

The frozen formula for fixed edge $(97,98)$ absent contains 13,160 variables
and 429,892 clauses: 161,700 triangle clauses, 16,420 exact-five counter
clauses, one fixed negative unit, and 251,771 $I_{18}$ hitting clauses.

| artifact | SHA-256 |
|---|---|
| DIMACS gzip | `47052de808b98598f2f144251a6ad73c1415dd00fef9e04b99ffe2f176229fbf` |
| cut bank JSON | `91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b` |
| DRAT gzip | `4d948ab34f1d2475af6efe943e0a4899827c78b96c2bc3835b5161f189c26bb5` |
| proof record JSON | `20729b2a818aaca35cdee6e9deeb5a0e6e4bbd6dc5ca11e5abb6dfe9409b035f` |

Fresh pinned CaDiCaL returned exit code 20 and `UNSATISFIABLE`, emitting a
3,493,847,713-byte raw proof with 6,649,939 lines. Pinned `drat-trim`,
executable SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`,
returned exit code 0 and `s VERIFIED`. The independent semantic checker
reconstructed every formula clause and all three branch/dependency boundaries.

## Bounded portfolio

All exploration processes had hard parent-enforced wall limits. TIME_LIMIT and
UNKNOWN were not promoted to UNSAT.

| branch | solver | wall seconds | resumed cuts | iterations | final cut count | conflicts | status |
|---:|---|---:|---:|---:|---:|---:|---|
| 0 | Glucose 4.2 | 600 | 2,385 | 240 | 125,265 | 91,595 | UNKNOWN |
| 0 | MapleChrono | 600 | 2,385 | 260 | 19,025 | 69,457 | UNKNOWN |
| 1 | Glucose 4.2 | 600 | 7,790 | 90 | 53,870 | 475,396 | UNKNOWN |
| 1 | MapleChrono | 600 | 7,790 | 120 | 15,470 | 541,379 | UNKNOWN |

These rows record the original bounded portfolio. Branch 0 initially produced
neither a fully separated SAT model nor a finite UNSAT cut bank; that historical
`UNKNOWN` endpoint is superseded by the universal-union proof above.
For branch 1, a later deduplicated-bank continuation added 512 separator cuts
and reached a finite UNSAT bank with 63,943 installed unique $I_{18}$ clauses,
including the fixed preload. That solver label was not trusted: the complete
CNF was reconstructed and proved independently as described below.

For branch 2, independent discovery with Glucose and Maple produced finite
UNSAT cut banks. Their deduplicated union was reconstructed from witness masks
and sent to the standalone proof-producing solver. The imported solver labels
were not used as the final proof.

## Branch-1 proof artifact

The frozen formula for fixed edge $(97,99)$ absent contains:

- 13,160 variables: 4,950 graph-edge variables and 8,210 exact-cardinality
  auxiliaries;
- 242,064 clauses: 161,700 triangle clauses, 16,420 exact-five counter
  clauses, one fixed-edge unit, and 63,943 distinct $I_{18}$ hitting clauses.

| artifact | SHA-256 |
|---|---|
| DIMACS gzip | `a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14` |
| cut bank JSON | `f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c` |
| DRAT gzip | `cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec` |
| proof record JSON | `4a3e7b4c729f696ff304c5f71621e018786b552146784a2141529a4c6f028666` |

Pinned CaDiCaL commit `c60730422e758ef1cebe7aeddf2dda31c996bf04`
returned exit code 20 and `UNSATISFIABLE`, emitting a 2,137,671,968-byte raw
proof with 5,590,150 lines. Pinned `drat-trim` commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, executable SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`,
returned exit code 0 and `s VERIFIED` after 209,897,525 reported resolution
steps.

The branch-1 checker independently reconstructs every CNF clause, checks the
complete compressed/raw CNF and proof identities, validates every installed
18-set mask, and checks the prior budget-five dependency. The earlier
interrupted output remains quarantined under `incomplete/`, fails `gzip -t`,
and was not used.

## Branch-2 proof artifact

The frozen formula for fixed edge $(98,99)$ absent contains:

- 13,160 variables: 4,950 graph-edge variables and 8,210 exact-cardinality
  auxiliaries;
- 183,543 clauses: 161,700 triangle clauses, 16,420 exact-five counter
  clauses, one fixed-edge unit, and 5,422 distinct $I_{18}$ hitting clauses.

| artifact | SHA-256 |
|---|---|
| DIMACS gzip | `c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06` |
| cut bank JSON | `aaa79a2f25d4c0d61c4467f1d0a721fd670a624e0391d96b2122723f97ba4598` |
| DRAT gzip | `c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9` |
| run JSON | `ee0c73b80407a4dd48ca69bd1a666f391bfd5729b9a56e062deef2a6f62018de` |

Pinned CaDiCaL commit `c60730422e758ef1cebe7aeddf2dda31c996bf04`
returned UNSAT and emitted a 759,008,359-byte raw proof with 2,837,771 lines.
Pinned `drat-trim` commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, executable SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`,
reported `s VERIFIED`.

The independent checker reconstructs the triangle prefix, the exact-five
sequential counter, the fixed negative unit, and every 153-literal clause as
the complete edge set of an 18-set. It also checks the prior budget-five proof
dependency.

## Reproduction

Run the unit tests and semantic reconstruction:

```bash
.venv/bin/python -m routes.finite.test_r3_18_budget6_branch -v
.venv/bin/python routes/finite/check_r3_18_budget6.py \
  --json routes/finite/r3_18_budget6_check.json
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --json routes/finite/r3_18_budget6_branch_1_check.json
.venv/bin/python routes/finite/check_r3_18_budget6_branch0_union.py \
  --json routes/finite/r3_18_budget6_branch_0_universal_union_check.json
```

To replay either compressed proof, additionally supply the pinned checker:

```bash
.venv/bin/python routes/finite/check_r3_18_budget6.py \
  --drat-trim /path/to/pinned/drat-trim --drat-seconds 300
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --drat-trim /path/to/pinned/drat-trim --drat-seconds 300
.venv/bin/python routes/finite/check_r3_18_budget6_branch0_union.py \
  --drat-trim /path/to/pinned/drat-trim --drat-seconds 360
```

## Claim boundary

- **Established:** all three exact-six branches are UNSAT with arbitrary
  original-nonedge additions; all proofs are frozen and checked. Together with
  the checked budget-at-most-five dependency, the complete fixed-seed deletion
  budget $\leq6$ edit ball is excluded and the local deletion radius is at
  least seven.
- **Not established:** existence of a seven-deletion repair.
- **Not established:** a 100-vertex $(3,18)$ Ramsey graph,
  $R(3,18)\geq101$, nonexistence of such a graph, or any new global Ramsey
  bound.
