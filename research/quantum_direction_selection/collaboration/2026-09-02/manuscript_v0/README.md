# Manuscript v0

This is the first integrated paper draft produced after the September 3 theorem-delta and source-collision audit. It is deliberately venue-neutral and uses the standard `article` class. The mathematical center is the finite-certificate all-chain transfer theorem; the kernel/min--max step and common-copy unweighting are presented as corollaries.

Current build: 19 pages. `latexmk` resolves every citation and cross-reference and reports no LaTeX warnings. This is a typesetting/integration check, not a fresh certification of every proof dependency.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Evidence boundary: the draft incorporates the locally checked fixed-palette certificates and proof synthesis. The final SIAM version of King--Kohler was not available during the bounded Pro comparison, so the exact published-version priority comparison remains open. The draft does not claim ordinary BQP, unrestricted SDQC1, gate-independent BQP1, complex-phase coverage, intrinsic denominator growth, or practical gap size.

The source tree is modular:

- `sections/3_transfer.tex` and `sections/A_transfer_proof.tex` contain the load-bearing all-chain theorem.
- `sections/4_quotient.tex` derives exact persistence maps.
- `sections/5_circuit.tex` gives the fixed-eight gate-dependent source.
- `sections/6_unweighting.tex` states the Hayakawa-based unweighted corollary.
- `sections/7_related_work.tex` records collisions and the exact priority boundary.
