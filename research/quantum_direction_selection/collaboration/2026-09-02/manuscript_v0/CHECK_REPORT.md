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
- Main flow: pages 1--12; references: page 13; proof appendices and disclosure
  follow.
- PDF: 21 A4 pages, anonymous metadata, all fonts embedded.
- AI disclosure: included at the end of the paper.

## Evidence boundary

The exact local scripts and the manuscript proof were checked in this
repository.  The cited primary-source ledger was only partially refreshed.
The final SIAM King--Kohler paper was identified, but its full equation-level
proof was not available for comparison.  No unrestricted SDQC1/BQP
class-equivalence or full literature novelty certification is recorded here.
