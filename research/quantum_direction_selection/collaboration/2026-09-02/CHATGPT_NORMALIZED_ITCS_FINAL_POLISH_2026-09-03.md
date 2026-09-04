# Final ITCS re-audit and polish record

**Date:** September 3–4, 2026  
**Repository:** `jackal092927/ramsey-bounds-reproducible`  
**Source branch re-audited:** `codex/fill-ramsey-gaps`  
**Latest source head reviewed:** `acc447bec2988ec68702f0ea59a12166a4266c72`  
**Polish branch:** `chatgpt/normalized-itcs-final-polish-2026-09-03`  
**Manuscript/build commit:** `fe8efdf7c459d895f0542e828dffea63cb0c6d6a`  
**Scope:** `research/quantum_direction_selection`, principally `collaboration/2026-09-02/manuscript_v0`. The unrelated `papers/quantum` subtree was neither reviewed nor modified.

## Final disposition

**SUBMISSION-CANDIDATE.**

The commits added after the earlier review at source commit
`586811c8e7e3b610f79eec570b7914a62ce1b817` close the previously identified
submission blockers. The current paper now contains a formal weighted and
unweighted target problem, a complete fixed-palette certification appendix, an
anonymous computational supplement, an exact gate-dependent source statement,
encoded polynomial parameter choices, source-version and bibliography repairs,
and an ITCS/LIPIcs review build. An independent reread found no remaining gap in
the complete claimed chain:

1. finite-certificate transfer for arbitrary full geometric chains;
2. exact geometric kernel multiplicity and an inverse-polynomial floor above
   the complete positive spectrum;
3. canonical quotient naturality and exact persistent rank;
4. the fixed-eight `BQP_1^{G_2}` source with values `3/4` and `1/8`;
5. common-copy weighted-to-unweighted transfer.

This is not a claim that the result has no novelty or acceptance risk. The
closest prior-work collision remains King--Kohler's many-gadget architecture,
and the denominator is deliberately padding-generated. The manuscript states
those limitations and does not promote the theorem to ordinary BQP,
unrestricted `SDQC_1`, gate-independent `BQP_1`, or arbitrary complex gates.

## Residual issues found and repaired in this pass

### 1. Empty term sets

The transfer theorem previously permitted an empty term set while its global
leakage proof sums over at least one attached gadget. The theorem now states the
many-gadget estimate for nonempty term sets. A bare-register level is handled
separately using the constant bowtie-register gap. This removes a real theorem
edge-case mismatch without weakening the circuit application.

### 2. Dyadic parameter selection

The phrase “largest dyadic below” was undefined because dyadic rationals are
dense. The reduction now chooses:

- the least integer `b` for which `lambda=2^{-b}` satisfies the transfer bound;
- for each endpoint, the least integer `s_i` with `2^{-s_i}` below a displayed
  positive rational target.

This gives deterministic, exact, polynomial-bit encodings of `lambda`,
`E_in`, and `E_out`.

### 3. Input-penalty strength

The history appendix now states exactly what the dirty-sector estimate uses:
`A_in` is the sum of clean-input penalty projectors, vanishes on the valid
input space, and satisfies `A_in|_{C^perp} >= I`.

### 4. Operator and field conventions

The preliminaries now define the up, down, and full Laplacians, define
`gamma_+`, state the empty-positive-spectrum convention, and explain scalar
extension from rational certificates to complex chain spaces. The text calls
`g_A` a certified coercivity constant rather than assuming it is always a
literal smallest positive eigenvalue.

### 5. Unweighting map

The unweighted corollary now displays the load-bearing harmonic intertwining
identity

```
P_hat_j J_hat_ij U_i = U_j P_j J_ij,
```

so preservation of the inclusion-induced homology rank is explicit rather than
only asserted. Polynomial vertex and edge bounds after blow-up are also stated.

### 6. ITCS presentation

The fixed-eight hardness theorem was moved to page 9 so the formal headline
claim appears within the first ten pages. The conclusion now flows directly
into the references rather than leaving an orphan line on a separate page. The
AI disclosure names the tools, their uses, and the materially affected sections
and appendices.

## Build and PDF verification

A temporary branch-only GitHub Actions workflow compiled the exact manuscript
commit `fe8efdf7c459d895f0542e828dffea63cb0c6d6a` in a clean Ubuntu 24.04
runner.

- Workflow run: `33845094693`
- Job: `100935135216`
- Result: **success**
- PDF pages: `24`
- Page size: A4
- Unresolved citations/references: none
- Overfull boxes: none
- Fonts: embedded and subset
- PDF author metadata: `Anonymous Authors`
- PDF SHA-256:
  `a376017228bedad427688da7ce8a4448d14bc537361bb6165729c8f8d239a617`
- Log SHA-256:
  `9851811117111f3e26f32ad2a4bf64c015c82e3c14976f77622d058ecb0a17fe`
- Workflow artifact digest:
  `sha256:4da5c5da5310f6dbf0e41dc2c8272e4ed90ca98f9c04c9be3a00096a73147295`

All 24 rendered pages were visually inspected. No clipping, overlapping text,
broken glyphs, blank pages, or identifying PDF metadata was found. The
temporary CI workflow was removed after this verification and is not part of
the merge-ready branch contents.

## Clean-room supplement replay

A second temporary verification branch, based exactly on the merge-ready polish
head, installed its dependencies from scratch, replayed the isolated anonymous
supplement, and rebuilt the paper. This verifies the submitted supplement rather
than merely trusting earlier `PASS` receipts.

- Verification branch: `chatgpt/normalized-itcs-verification-2026-09-04`
- Verification commit: `0ae3b05727afe865529953db1b1d9022f758f436`
- Workflow run: `33846037977`
- Job: `100938026879`
- Result: **success**
- Commands replayed successfully:
  - `certify_representative_bulk.py --offline`
  - `certify_remaining_active_atoms.py --offline`
  - `check_active_hadamard_orbit.py`
  - `check_selected_cycle_guard.py`
  - `check_exact_filling_coercivity.py`
  - `check_weighted_history.py`
  - `check_kernel_filtration.py`
  - `check_common_blowup.py`
  - `check_padded_bulk.py`
- Representative finite certificate: **PASS**
- Remaining active atoms: **PASS**
- Four Hadamard relabeling/orbit certificates: **PASS**
- Selected-cycle guard, including 46,998 exact all-degree identities: **PASS**
- Weighted-history and zero-final-kernel fixtures: **PASS**
- Quotient-filtration fixture: **PASS**
- Common-copy and padded-bulk checks: **PASS**
- Fresh PDF SHA-256:
  `39c5867b9a29bc9a46ff2a27b81ed3e2f76b7e2e0e61ef9f799e0c3b683335b9`
- Fresh log SHA-256:
  `3104b44efb65a2d731d960ff9bbf5de71f66ef80f213e8dcb914b70d89085e33`
- Verification artifact ID: `9926598467`
- Verification artifact digest:
  `sha256:a4fd21d596cae861e6fdba19495233d839507b7dffef1989bd2905037245bacb`

The two PDF hashes differ because PDF creation timestamps are embedded; both
builds compiled the same manuscript source. The verification workflow itself is
kept off the merge-ready polish branch.

The repository-wide `canonical-paper` job also ran, but it targets the separate
canonical quantum manuscript and failed its own unresolved-reference check. Per
the task boundary, that unrelated subtree and workflow were not modified. The
isolated normalized-persistence build and clean-room replay above are the
relevant verification results.

## Remaining human submission actions

No mathematical or LaTeX blocker remains in this branch. The remaining steps
are administrative and author-controlled:

1. review the final author list, affiliations, acknowledgments, and funding
   text outside the anonymous PDF;
2. enter author/institution metadata and conflicts of interest in HotCRP;
3. upload the anonymous PDF and, if desired, the isolated `supplement/`
   directory as supplementary material;
4. confirm that there is no conflicting archival submission;
5. perform final author signoff on the title, claims, and AI disclosure.

The paper should be merged or cherry-picked from the polish branch only after
that signoff. The source branch was not edited directly in this pass.
