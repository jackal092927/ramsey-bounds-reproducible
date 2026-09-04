# Candidate check report

Date: 2026-09-04 (supersedes the 2026-09-03 report)

## Exact and finite checks

All commands below completed with PASS status.

- `certify_representative_bulk.py --offline`: exact representative bulk ranks,
  Betti numbers, filling ranks, zero-weight pair, and Gram determinant.
- `certify_remaining_active_atoms.py --offline`: the remaining active atoms
  and transported orbit.
- `check_active_hadamard_orbit.py`: four active atoms and fillings.
- `check_selected_cycle_guard.py`: 46,998 tensor checks in degrees 0--7,
  exact filling, and basis cone.
- `check_exact_filling_coercivity.py`: fifteen small fixtures plus guards.
- `check_weighted_history.py`: NO, YES, and zero-final-kernel history fixtures.
- `check_kernel_filtration.py`: Betti dimensions \(4,2,1\), natural map ranks
  \(2,1\), and positive gaps over four weight scales.
- `check_common_blowup.py`: chain/Laplacian intertwining and inclusion
  commutation; also detects the unequal-copy counterexample.
- `check_padded_bulk.py`: arbitrary padded coordinates retain the unit-weight
  boundary, while outside harmonic tensors cancel it.

The first attempt to run the final four checks used an incorrect relative path;
they were rerun from the correct directory and passed.  That invocation error
did not modify the mathematical artifacts.

## Manuscript checks

- All nine supplement checkers were replayed again on 2026-09-04 from
  `supplement/` with `PYTHONDONTWRITEBYTECODE=1`: all PASS.
- `latexmk -pdf -g -interaction=nonstopmode -halt-on-error main.tex`
  (forced full rebuild): PASS.
- Citations and cross-references: resolved; no `??` in the rendered text.
- Typesetting diagnostics: 0 LaTeX warnings, 0 BibTeX warnings, 0 overfull
  boxes, 0 underfull boxes (`\paragraph` headings made unnumbered via
  `secnumdepth`).
- Format: anonymous LIPIcs review copy with the local ITCS 11-point adapter.
- Main flow: introduction with Theorems 1.1--1.3 on pages 1--5; body through
  page 17; references pages 18--19; proof appendices and disclosure follow.
- PDF: 28 A4 pages, anonymous metadata (title updated), all fonts embedded.
- AI disclosure: included at the end of the paper; names ChatGPT and Claude.
- Pages 1, 3, and 9 were rendered and visually inspected after the rewrite.
- SHA-256 after the September 4 afternoon repairs: `f6eb6d96277a12f973a1c60e3bdf3f194d20dd4c4edca2ac345a17e2f6f9a1e5`.

## Anonymous supplement

- The nine checkers were copied with their required certificate data into the
  isolated `supplement/` directory and replayed there on 2026-09-03.
- All nine commands completed successfully, including 46,998 exact selected-cycle
  guard checks, palette ranks/fillings, weighted-history fixtures, filtration
  maps, common-copy intertwining, and padded-bulk behavior.
- No author name, username, private absolute path, email address, transcript, or
  version-control history is present in the supplement.
- The README records the upstream immutable commit and source-file SHA-256;
  third-party source code is not redistributed.
- Packaged archive SHA-256:
  `6f9d90f70dbdacb333f51b49306c8790a10a889bfd62aca4ab2639730f8cc194`.
- A fresh temporary extraction of that archive replayed all nine commands with
  `PYTHONDONTWRITEBYTECODE=1`: PASS.

## Evidence boundary

The exact local scripts and the manuscript proof were checked in this
repository.  The cited primary-source ledger was only partially refreshed.
The final SIAM King--Kohler paper was identified, but its full equation-level
proof was not available for comparison.  No unrestricted SDQC1/BQP
class-equivalence or full literature novelty certification is recorded here.

## September 4 afternoon repairs (external review)

Four formal repairs, none changing a theorem: the clean-input penalty
`A_in` is described as a sum of basis projectors with `ker A_in = C` and
`A_in >= P_{C^perp}` (Appendix B.2); the endpoint gap bounds are chosen as
explicit powers of two `E_i = 2^{-s_i}` (proof of Theorem 5.3); the empty
term set is handled by the register floor (Appendix A.2); Definition 2.1
requires `gamma_1, gamma_2, epsilon >= 1/poly(|V|)`.  Forced rebuild: 28
pages, 0 warnings, 0 overfull, 0 underfull, no unresolved references.
