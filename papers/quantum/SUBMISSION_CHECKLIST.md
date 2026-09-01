# ITCS 2027 submission checklist

Snapshot date: 2026-08-31

## Current artifact

- Title: **Quantum Query Algorithms for Constructive Ramsey Search**
- Source: `papers/quantum/main.tex`
- Anonymous PDF: `papers/quantum/main.pdf`
- PDF SHA-256: `13fda421f34f783da622cb65cb43aea393859216389d0a3e6c9eb7b873d3532a`
- Length: 14 pages total
- Main presentation: concludes on page 10; Appendix A begins on page 11
- Format: 11pt, single column, US letter
- Identity scan: no personal name, affiliation, personal email, or public
  repository URL in the PDF; metadata author is `Anonymous Authors`
- Fonts: all embedded
- LaTeX diagnostics: no undefined references, undefined citations, warnings,
  errors, or overfull boxes

The official call at <https://itcs-conf.org/> requires at least 11pt,
single-column text and lightweight double blindness, but imposes no hard
length limit.  It recommends that the merits, innovations, literature
position, and central claims appear within the first ten pages.  The abstract
deadline is 2026-09-02 16:59 PDT and the full-paper deadline is 2026-09-04
16:59 PDT.

## Generative-AI policy

The ITCS 2027 call states that only humans may be listed as authors or
co-authors.  Substantive generative-AI use must be disclosed at submission in
an `AI Disclosure` statement at the end of the paper.  The statement must name
the tools and identify the parts materially affected; use that materially
affects the methodology, analysis, experiments, or implementation must also
be described in the body.  Minor copy-editing alone would not require
disclosure, but the use in this project is substantive.  The current source
therefore includes both a research-process paragraph in Section 7 and a
specific end-of-paper disclosure.

## Verification completed

- `make paper`: PASS for both the standalone and unified manuscripts
- `make verify-quantum`: PASS (`QUANTUM_RAMSEY_AUDIT_PASS`)
- `.venv/bin/python reproduce.py quick`: PASS, including 214 finite tests
- PDF anonymity, metadata, font embedding, marker, and cross-reference scans:
  PASS

## Scientific submission gate

The main remaining blocker is not formatting or code.  The standalone paper's
upper bound conflicts with the printed `N^(1-o(1))` quantum lower-bound
sentence of Jain--Li--Robere--Xun at their formal default parameters.  The
paper gives the direct calculation showing that the cited route transfers at
most exponent `1/24`, but author clarification and the pending ChatGPT Pro
hostile review should be dispositioned before upload.

This gate does not retract the locally checked theorem.  It prevents an
overconfident novelty/model comparison while the closest-source discrepancy
is unresolved.

## Human-owned submission actions

- [ ] Resolve and incorporate the closest-source clarification/review.
- [ ] Confirm the final human author list and ordering.
- [ ] Confirm that every listed human author accepts responsibility for the
  final claims, references, code, and AI disclosure.
- [ ] Register the title and abstract on the ITCS submission server.
- [ ] Upload the anonymous PDF and complete the COI declaration.
- [ ] Retain the AI disclosure in the submitted manuscript.
- [ ] Record the actual uploaded PDF hash and submission ID.

No external submission has been made by this repository update.
