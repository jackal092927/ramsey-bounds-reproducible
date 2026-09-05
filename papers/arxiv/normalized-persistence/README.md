# arXiv preprint edition

Status: **prepared for author upload; not submitted to arXiv**.

This standalone 11-point `article` edition is derived from `research/quantum_direction_selection/collaboration/2026-09-02/manuscript_v0/main.tex`.
It uses public author information and ordinary page numbers, with no anonymous
review or proceedings branding. The abstract, mathematical statements, proofs,
appendices, citations, and AI disclosure are preserved verbatim from the source.
The original ITCS edition is maintained separately.

- `main.pdf`: compiled preprint for inspection.
- `arxiv-source.zip`: upload this source archive to arXiv; select PDFLaTeX and `main.tex`.
- `main.tex`, `preprint.sty`, and the input/bibliography files: editable source.
- `VERIFICATION.md`: clean-package build and preservation checks.

Rebuild the PDF and source archive with `python3 package.py`.

Build only the PDF with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The source archive includes the custom style and any BibTeX source/style/output,
but excludes generated PDFs, logs, and auxiliary files. These are independent
snapshots: later mathematical edits must be synchronized deliberately between
editions. arXiv's server-generated PDF still needs inspection when uploading.

Format guidance: https://info.arxiv.org/help/submit_tex.html

The `anc/` directory contains the certificate data and nine checker scripts
referenced in Appendix C. It is included in the upload archive following
https://info.arxiv.org/help/ancillary_files.html .

The forced page break before the bibliography is removed in this edition to
avoid leaving nearly an entire page empty; the text is unchanged.
