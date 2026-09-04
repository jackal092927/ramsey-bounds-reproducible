# Candidate check report

Date: 2026-09-03

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

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`: PASS.
- Citations and cross-references: resolved.
- Typesetting diagnostics: no overfull boxes or LaTeX warnings.
- Format: anonymous LIPIcs review copy with the local ITCS 11-point adapter.
- Main flow: pages 1--13; references: page 14; proof appendices and disclosure
  follow.
- PDF: 23 A4 pages, anonymous metadata, all fonts embedded.
- AI disclosure: included at the end of the paper.
- Representative pages 1, 12, 14, and 23 were rendered and visually inspected.
- SHA-256: `034bc4111d5f4830932e940efbb7d8012f85ace671a86ad952e41255824a8ab2`.

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
