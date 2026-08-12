# R(3,18), exact budget 6: proof-carrying closure of branch 1

Date: 2026-08-12

## Verdict

**Branch 1 is UNSAT with a complete independently verified DRAT proof.**  For
the frozen 100-vertex near miss, there is no eligible final graph that fixes
input edge $(97,99)$ absent, deletes exactly five further input edges, permits
arbitrary additions among original nonedges, is triangle-free, and has no
independent set of size 18.

This closes branch 1 only.  Branch 2 was already proof-verified UNSAT, while
branch 0 was still `UNKNOWN` at the time of this branch-1 report. A subsequent
universal-cut proof closed branch 0; see
`R3_18_BUDGET6_BRANCH0_UNION_PROOF.md`. The complete fixed-seed budget-six ball
is now excluded, but this still does **not** establish $R(3,18)\geq101$.

## Evidence boundary

The frozen seed has SHA-256
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`,
100 vertices, 827 edges, no independent 18-set, and the unique triangle
$(97,98,99)$.  The earlier proof-carrying budget-five exclusion is retained as
an explicit dependency.  Hence a new repair in the budget-six ball would have
to delete exactly six input edges.  In branch 1 the negative unit
$\neg x_{97,99}$ accounts for one deletion, and the sequential counter enforces
exactly five deletions among the other 826 input edges.  Original nonedges are
not in that counter and remain free final-edge variables.

An independent checker reconstructed the entire CNF in order:

| block | clauses |
|---|---:|
| all triangle clauses | 161,700 |
| exact-five sequential counter | 16,420 |
| fixed negative unit | 1 |
| valid $I_{18}$ hitting clauses | 63,943 |
| **total** | **242,064** |

The formula has 13,160 variables.  Every trailing hitting clause consists of
the 153 distinct positive primary variables for all pairs of one 18-set; its
ordered mask digest is
`99b72cd5500c6140d4aca261a1028b9805b9d8209ffc3216596a0fb8fb50edcf`.
Thus the finite CNF is a sound relaxation of the full branch: its checked
UNSAT status excludes the exact branch.

## Fresh proof and independent replay

The prior interrupted output was not reused.  Pinned CaDiCaL 3.0.1, source
commit `c60730422e758ef1cebe7aeddf2dda31c996bf04` and executable SHA-256
`62d48c0890fae760c859e65676dc0598d59c36ac8170cbc5f115208d0a549429`,
was started from the complete frozen CNF.  It returned exit code 20 and
`UNSATISFIABLE`, writing a 2,137,671,968-byte, 5,590,150-line raw DRAT.  The
solver plus deterministic compression took 275.792 seconds.

Pinned official `drat-trim`, source commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985` and executable SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`,
then replayed the complete CNF/proof pair.  It returned exit code 0 and
`s VERIFIED`; the checker reported 511,535 of 2,789,684 lemmas in the core,
209,897,525 resolution steps, and zero RAT lemmas in the core.  Replay plus
decompression took 202.046 seconds, of which 198.812 seconds were checker
verification time.

## Frozen artifacts

| artifact | bytes | SHA-256 |
|---|---:|---|
| `r3_18_budget6_branch_1.cnf.gz` | 5,052,085 | `a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14` |
| `r3_18_budget6_branch_1.cuts.json` | 2,110,304 | `f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c` |
| `r3_18_budget6_branch_1.drat.gz` | 433,552,903 | `cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec` |
| raw CNF | 47,089,599 | `ced3fd39370b4c2552cb261638fb7076da173e18d6b871f6fb280668e5a1154a` |
| raw DRAT | 2,137,671,968 | `fbf7292c3bcbf52ec6f978fca0751d319e2e2029380e7a865a17430baf282902` |
| `check_r3_18_budget6_branch1.py` | — | `47da14a1b13d32379c2396b19992b9edf58ea21a2621d9f6f8d895416347b16b` |
| `r3_18_budget6_branch_1_check.json` | — | `010885ff86f45db8b7d34ebbe22a9025f3136660a516762c5296ab470486480c` |

The fresh proof gzip passes `gzip -t`.  It was written to a `.new` path and
renamed to its final name only after complete compression.  No CaDiCaL or
`drat-trim` process remained afterward.

The older interrupted file remains quarantined at
`incomplete/r3_18_budget6_branch_1.partial.drat.gz`; it has SHA-256
`dcdb695a11c21e473b9a715ba8048f68066f6a49c5a960809e05ad973820f38b`,
fails `gzip -t`, and was not used at any stage of the conclusion.

## Reproduction

Artifact identities and clause semantics can be checked without a long proof
replay:

```bash
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --json routes/finite/r3_18_budget6_branch_1_check.json
```

To replay the complete proof, add the pinned checker:

```bash
.venv/bin/python routes/finite/check_r3_18_budget6_branch1.py \
  --drat-trim /absolute/path/to/pinned/drat-trim \
  --drat-seconds 300
```

No branch-0 search was started in this follow-up.
