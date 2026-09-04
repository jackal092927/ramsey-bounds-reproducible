# Version 2 draft check report

Date: 2026-09-04

- `latexmk -pdf -g -interaction=nonstopmode -halt-on-error main.tex`: PASS.
- 34 A4 pages in the 11-point LIPIcs review format; introduction with the
  five headline theorems on pages 1--5; body through page 23; references on
  pages 24--25; appendices from page 26.
- 0 LaTeX warnings, 0 BibTeX warnings, 0 overfull boxes, 0 underfull boxes;
  no unresolved references.
- New finite checks (run from `..`, outputs in
  `../V2_CHECK_OUTPUTS_2026-09-04.txt`):
  - `check_filling_domination.py`: for the three certified atoms and
    `lambda in {1/2,1/4,1/8,1/16}`, the operator inequality
    `Delta_up >= (||v||^2/||c(lambda)||^2) P_v` holds to machine precision,
    and the optimal constant scales as `lambda^(2 p_a)` with `p_a = 3, 5, 5`.
  - `check_harmonic_overlap.py`: on the real `|0>-|1>` atom the harmonic
    vector is within `0.65 lambda` of the register cycle space and the overlap
    singular value is `1 - O(lambda^2)`.
- The nine version-1 supplement checkers are unchanged and were replayed on
  2026-09-04 (all PASS).
