# ITCS 2027 submission checklist

Snapshot date: 2026-09-01

## Current artifact

- Title: **Quantum Query Algorithms for the Constructive Diagonal Ramsey Theorem**
- Source: `papers/quantum/main.tex`
- Anonymous PDF: `papers/quantum/main.pdf`
- PDF SHA-256: `8ac5f6f08123f339b1ae80e51357ba4b251b71c5a71123c96dae9846c2874bf9`
- Length: 16 pages total
- Main presentation: central claims, proofs, and literature comparison are
  within the first ten pages; the scope conclusion and Appendix A share page 11
- Format: 11pt, single column, US letter
- Identity scan: no author block, affiliation, personal email, or public
  repository URL in the PDF; metadata author is `Anonymous Authors`.  One
  relevant prior paper by the submitting author is cited in the bibliography
  in ordinary third-person form.
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

## HotCRP state

- Submission `#193` is registered under the confirmed Fresno author record.
- The title, abstract, seven topics, AI-assisted-review preference, and
  AI-preparation survey were saved and re-opened from the submission summary.
- The Fresno HotCRP profile contains the verified ORCID identifier; its value
  is intentionally omitted from this anonymous repository record.
- Lifecycle state: **REGISTERED DRAFT / NO PDF UPLOADED / NOT READY FOR REVIEW**.

## Scientific submission gate

The completed ChatGPT Pro hostile review found no fatal mathematical defect,
and its proof-specific objections have been dispositioned in the manuscript.
A narrower final-delta review packet covering the experiment paragraph,
references, and JLRX wording is prepared but has not been transmitted; no
result from that additional review is counted here.
The main remaining blocker is not formatting or code.  The standalone paper's
upper bound conflicts with the printed `N^(1-o(1))` quantum lower-bound
sentence of Jain--Li--Robere--Xun at their formal default parameters.  The
paper gives the direct calculation showing that the cited route transfers at
most exponent `1/24`, calls this an apparent parameter mismatch, does not rely
on the disputed consequence, and explicitly excludes their principal TFNP
separation theorems from the audit.  Author clarification remains desirable
before upload.

This gate does not retract the locally checked theorem.  It prevents an
overconfident novelty/model comparison while the closest-source discrepancy
is unresolved.

## Human-owned submission actions

- [x] Incorporate the completed ChatGPT Pro mathematical review.
- [x] Accurately retain and scope the closest-source JLRX discrepancy.
- [ ] Seek clarification from the JLRX authors before final upload if time
  permits.
- [x] Confirm the final human author list and ordering.
- [ ] Confirm that every listed human author accepts responsibility for the
  final claims, references, code, and AI disclosure.
- [x] Register the title and abstract on the ITCS submission server.
- [ ] Upload the anonymous PDF and complete the COI declaration.
- [ ] Retain the AI disclosure in the submitted manuscript.
- [ ] Record the actual uploaded PDF hash; submission ID `#193` is recorded.

The abstract is registered externally.  No PDF has been uploaded, and the
draft is not ready for review.
