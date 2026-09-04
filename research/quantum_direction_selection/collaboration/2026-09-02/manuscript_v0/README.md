# Normalized Persistence manuscript

This directory contains the anonymous LIPIcs/ITCS submission candidate produced
after the September 3 theorem-delta and source-collision audit.  The mathematical
center is the finite-certificate all-chain concentration theorem.  Exact
kernel multiplicity, the whole positive gap, quotient naturality, and
common-copy unweighting are downstream consequences with their assumptions
spelled out.

Current title: *Exact Kernel Transfer to Clique Complexes and the Hardness of
Normalized Persistence*.  Current build: 28 pages in the 11-point LIPIcs review
format; the introduction with the three main theorem statements ends on page 5,
the main narrative ends on page 17, references occupy pages 18--19, and the
remaining pages are proof appendices and the AI disclosure.  The build resolves
every citation and cross-reference with no LaTeX, BibTeX, overfull, or underfull
diagnostics.  See `PROOF_AUDIT.md` for the dependency audit (including the
September 4 independent review) and `CHECK_REPORT.md` for executable and
rendering checks.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Evidence boundary: the draft incorporates locally checked fixed-palette
certificates and proof synthesis.  Equation-level comparison against the final
SIAM version of King--Kohler has not been performed, so the exact
published-version priority comparison remains open.  The draft does not claim
ordinary BQP, unrestricted SDQC1, gate-independent BQP1, complex-phase coverage,
intrinsic denominator growth, or practical gap size.

The anonymous `supplement/` directory contains the submission-safe certificate
data, nine checker scripts, offline receipts, requirements, exact commands, and
upstream provenance. It excludes collaboration transcripts and Git history.
The upload-ready archive is `normalized-persistence-anonymous-supplement.zip`.

The source tree is modular:

- `sections/3_transfer.tex` and `sections/A_transfer_proof.tex` contain the load-bearing all-chain theorem.
- `sections/4_quotient.tex` derives exact persistence maps.
- `sections/5_circuit.tex` gives the fixed-eight gate-dependent source.
- `sections/6_unweighting.tex` states the Hayakawa-based unweighted corollary.
- `sections/7_related_work.tex` records the precise relation to Lowe et al.'s Problem 9 and Conjectures 1--2, and the exact priority boundary.
- `sections/8_limitations_conclusion.tex` lists limitations and five open problems.
- `sections/C_palette_certificates.tex` records the finite palette and certificate interface.
- `PROOF_AUDIT.md` separates mathematical closure from remaining source-priority risk.
