# ITCS 2027 submission checklist

## Restructured candidate of 2026-09-04 afternoon (NOT YET UPLOADED)

- Reorganized for the ITCS guidance (see `papers/ITCS_PAPER_ORGANIZATION_GUIDE.md`):
  main text is 10 pages (front matter pages 1--3, technical Sections 2--4
  pages 4--8, related work and discussion pages 9--10), references pages
  11--12, appendices pages 13--23. All full proofs are in the appendices:
  A (sampler lemma, encoding corollary), B (Section 3 upper bounds),
  C (Section 4 lower bounds and random graphs), D (multicolour, experiments,
  AI disclosure). The main text keeps statements with proof sketches.
- Result numbering is now: Theorem 1.1, Corollary 1.2, Corollary 2.1,
  Lemma 2.2, Lemma 3.1 (size-biased survival), Proposition 3.2, Lemma 3.3
  (concentration), Lemma 3.4 (survival), Lemma 3.5 (output),
  Proposition 4.1 (randomized lower bound), Proposition 4.2 (quantum greedy),
  Corollary 4.3 (separation), Remark 4.4 (classical greedy),
  Proposition 4.5 (quantum lower bound N^(1/12)), Lemma C.1, Corollary C.2,
  Corollary D.1. Earlier notes below use the previous numbering.
- The review-copy adapter now uses the standard LaTeX 11pt leading
  (11/13.6) instead of 11/14.3; the font size is unchanged at 11pt.
- No results or proofs were changed in this pass; text was moved and
  condensed. Section files: sections/01--06, appendices/A--D.
- Candidate PDF SHA-256: `281f3814cafdeb4ba750d3341be36119d3d4b42826c6a42c8dd5b3b569b13544` (446,027 bytes, 23 pages).
  No LaTeX diagnostics, no undefined references or citations, fonts
  embedded, identity scan clean.
- Human-owned actions: read the main text once for flow, verify the
  appendix proofs match the earlier version (they were moved verbatim),
  then follow the upload steps in the next entry.

## Revision candidate of 2026-09-04 morning (superseded by the entry above)

- Source revised on 2026-09-04 (early morning PDT); `main.pdf` rebuilt.
- Candidate PDF SHA-256:
  `726a9c8f63434b33f837631a1d648fc022930c28ce9e139a990bcb7bc66dd65d`
  (447,345 bytes, 26 pages; main text ends on page 16, references
  pages 17--19, appendices pages 20--26). No LaTeX errors, undefined
  references, undefined citations, or overfull boxes; fonts embedded;
  identity scan clean; `QUANTUM_RAMSEY_AUDIT_PASS` reproduced.
- Changes in this revision:
  1. Appendix B now contains a self-contained proof of the random-Painter
     weight bound (Lemma B.1, Corollary B.2) using the matching number of
     the queried graph as the potential. The earlier text cited
     "[CFGH, Theorem 1]" for the bound; the bound is the expectation
     estimate inside the proof of that theorem (Lemma 17 in arXiv v2).
  2. Proposition 5.2 is restated in distributional form (success at most
     5/8 on G(N,1/2) with T = floor(2^{(2-sqrt2)K-2}) queries, any N >= K),
     from which the worst-case statement follows.
  3. New Proposition 5.3 (quantum greedy search on G(M,1/2),
     O(K 2^{K/2} log(K/eta)) queries) and Corollary 5.4 (separation on
     G(N,1/2) at the Ramsey scale: quantum O~(N^{1/4}) versus randomized
     Omega(N^{1-1/sqrt2})). Proof in Appendix B.3.
  4. Section 6.3 adds the valid t=2 consequence of the JLRX reduction:
     an Omega(N^{1/12}) quantum lower bound (Erdos 1947 + Zhandry 2015;
     the printed JLRX parameter condition gives only 1/24, the tight
     pigeonhole in their Lemma III.1 gives 1/12), so the quantum
     complexity is bracketed between N^{1/12} and O~(sqrt N). New bibliography entries Zhandry2015 and Erdos1947;
     CFGH year corrected to 2019 with the chapter DOI.
  5. Introduction rewritten around the JLRX query question, with a
     bounds table (Table 1) and result paragraphs; Section 7 rewritten as
     explicit open questions and a scope statement; abstract updated.
  6. AI Disclosure (Appendix C.3) rewritten as a short, general statement
     naming ChatGPT and Claude, in the author's own wording; it is the only
     AI statement in the paper.
  7. External review of 2026-09-04 addressed: Corollary 5.4 now assumes
     n >= 26 (so K >= 14); the Omega(N^{1/12}) quantum lower bound is a
     formal Proposition 6.1 covering every N = 2^n (n >= 8) with the
     O(log N) collision-decoding queries (the independent adversarial
     pass found that homogeneous sets of order 2m, not 4m-2, already
     force a collision, which doubles the exponent from 1/24); Corollary B.2 is stated for at
     most T queries (no exact-T padding); Lemma B.1 sets tau(U) = infinity
     when no critical time exists and notes the fresh-bit property;
     Proposition 5.3's proof verifies pi_K < e^{-100} for K >= 14;
     Remark 5.5 proves the classical greedy O~(N^{1/2}) table entry; the
     CFGH pointer reads "proof of Theorem 1"; Table 1 cites Propositions
     5.2 and 6.1 and Remark 5.5.
- Human-owned actions before uploading:
  - [ ] Read and independently verify the new material: Lemma B.1,
        Corollary B.2, the restated Proposition 5.2, Proposition 5.3,
        Corollary 5.4, and the t=2 lower-bound paragraph in Section 6.3.
        The AI Disclosure asserts that the authors checked every argument.
  - [ ] Approve the revised AI Disclosure wording.
  - [ ] Replace the HotCRP abstract of submission #193 with the new
        abstract (plain-text version in `SUBMISSION_METADATA.md`).
  - [ ] Upload the new `main.pdf`, click `Save and resubmit`, verify the
        server hash prefix `726a9c8f`, and copy the uploaded file to
        `submitted/` with the upload timestamp.
  - Deadline: 2026-09-04 16:59:59 PDT.

## Previously submitted artifact (2026-09-02, still the live version on HotCRP)

- Title: **Quantum Query Algorithms for the Constructive Diagonal Ramsey Theorem**
- Source: `papers/quantum/main.tex`
- Anonymous PDF: `papers/quantum/main.pdf`
- PDF SHA-256: `e47b80073b1333668c2203c970548df55c1db51bdd005c268de4667077563cd7`
- Submitted revision: shortened the AI disclosure and body description, removed
  numbered-section attribution and product-tier names, and used `GPT-based
  tools` with one parenthetical identification of ChatGPT and Codex. The four
  general roles are brainstorming, constructive discussion, manuscript polishing,
  and review. The body identifies the theoretical arguments and numerical
  experiments as the subject of the discussion. Mathematical results and
  experimental outcomes are unchanged. This revision was uploaded and
  resubmitted on 2026-09-02 at 17:04:26 PDT.
- Length: 16 pages total
- Main presentation: the main quantum upper-bound proof finishes on page 8; Section 6's
  detailed comparison continues onto page 11. Merits and a concise literature
  comparison appear in the introduction. Section 7 ends on page 11;
  appendices begin on page 12.
- Format: official LIPIcs v2021.1.3, A4, single column, with its `anonymous`
  option and default line numbers. A separate review-only adapter raises body,
  abstract, keyword/classification, and bibliography text to 11pt to satisfy
  ITCS; the bundled official class is unchanged. See `TEMPLATE.md`.
- Identity scan: the author block and running heads contain only anonymous
  placeholders; no real author affiliation, personal email, ORCID link, or
  public repository URL is present. Metadata author is `Anonymous Authors`. One
  relevant prior paper by the submitting author is cited in the bibliography
  in ordinary third-person form.
- Fonts: all embedded
- LaTeX diagnostics: no warnings, undefined references, undefined citations,
  errors, or overfull/underfull boxes in the final standalone build
- The template migration preserved mathematical content and all 24 cited
  bibliography entries. The subsequent editorial pass rewrites Appendix C.2
  as self-contained small-instance numerical experiments: methods and reported
  outcomes are retained, while source-file paths and run commands are removed.
  The theoretical results do not depend on executing an artifact. These prose
  changes are mirrored in the unified manuscript. The references use
  `plainurl`; the end-of-paper AI disclosure is retained. Appendices start on
  a fresh page.

The official call at <https://itcs-conf.org/> requires at least 11pt,
single-column text and lightweight double blindness, but imposes no hard
length limit.  It recommends that the merits, innovations, literature
position, and central claims appear within the first ten pages.  The abstract
deadline is 2026-09-02 16:59 PDT and the full-paper deadline is 2026-09-04
16:59 PDT.

## Code and experimental presentation

The current official call does not require code submission, an anonymous
repository, or an open-source release. Its encouragement of public posting
concerns full papers with proofs. The PDF therefore describes the experiments
without requiring repository access or attaching an anonymous code artifact.
Methods and numerical outcomes remain in Appendix C.2; implementation and
reproduction instructions remain in the project documentation.

The existing GitHub repository is publicly viewable, including quantum
experiment code on `codex/fill-ramsey-gaps`, but `LICENSE.md` reserves all
rights rather than granting an open-source reuse license. This is not an
anonymous repository. No repository visibility or licensing change was made,
and the anonymous PDF does not link to it.

## Generative-AI policy

The ITCS 2027 call states that only humans may be listed as authors or
co-authors.  Substantive generative-AI use must be disclosed at submission in
an `AI Disclosure` statement at the end of the paper.  The statement must name
the tools and identify the parts materially affected; use that materially
affects the methodology, analysis, experiments, or implementation must also
be described in the body.  Minor copy-editing alone would not require
disclosure, but the use in this project is substantive.  The current source
therefore includes one brief body sentence identifying the tools and their
role in brainstorming/discussion of arguments and experiments, polishing, and
review, plus a concise
end-of-paper disclosure and author-responsibility statement. A numbered list
of affected sections is not explicitly required by the call.

## Verification completed

- `make paper`: PASS for both the standalone and unified manuscripts
- `make verify-quantum`: PASS (`QUANTUM_RAMSEY_AUDIT_PASS`)
- `.venv/bin/python reproduce.py quick`: PASS, including 214 finite tests
- PDF anonymity, metadata, font embedding, marker, and cross-reference scans:
  PASS

## Last verified HotCRP state (revised PDF resubmitted)

Final submission completed on 2026-09-02 after the author explicitly confirmed
no PC conflicts and authorized submission. The server returned `Updated
submission` and `The submission is ready for review`, with no further action
required. This success state was observed at approximately 16:37 PDT.
The author-approved AI-disclosure revision was subsequently uploaded and
resubmitted at 17:04:26 PDT. HotCRP returned `Updated submission (changed
Submission)` and again confirmed that the submission is ready for review.

- Submission `#193` is registered under the confirmed Fresno author record.
- The title, abstract, seven topics, AI-assisted-review preference, and
  AI-preparation survey were saved and re-opened from the submission summary.
- The previously verified Fresno HotCRP profile contains the ORCID identifier;
  the profile was not reopened in this upload pass.
- Uploaded file: `main.pdf`, 357,973 bytes (displayed as 358 kB), 16 pages.
- Server upload time: 2026-09-02 17:04:26 PDT (20:04:26 EDT).
- Uploaded PDF SHA-256:
  `e47b80073b1333668c2203c970548df55c1db51bdd005c268de4667077563cd7`.
- Local copy of the submitted PDF:
  `papers/quantum/submitted/itcs2027-paper193-2026-09-02-v2.pdf`.
- Server-displayed SHA-256 prefix: `e47b8007`, matching the submitted copy
  and current local `main.pdf`.
- The first submitted version remains preserved, without modification, at
  `papers/quantum/submitted/itcs2027-paper193-2026-09-02.pdf`.
- PC conflicts remain `None`, as explicitly confirmed by the author.
- The server explicitly allows updates until 2026-09-04 16:59:59 PDT.
- The edit page now offers `Save and resubmit` for subsequent updates.
- Lifecycle state: **SUBMITTED / READY FOR REVIEW** (not an acceptance decision).
- Submission record: <https://itcs2027.hotcrp.com/u/0/paper/193/main>.

## Scientific readiness

The completed ChatGPT Pro hostile review found no fatal mathematical defect,
and its proof-specific objections have been dispositioned in the manuscript.
A narrower final-delta review packet covering the experiment paragraph,
references, and JLRX wording was submitted on 2026-09-01. Its latest visible
state is a network error after interim analysis, not a completed verdict.
No result from that additional review is counted here.
The standalone paper's
upper bound conflicts with the printed `N^(1-o(1))` quantum lower-bound
sentence of Jain--Li--Robere--Xun at their formal default parameters.  The
paper gives the direct calculation showing that the cited route transfers at
most exponent `1/24` under the printed parameter condition and `1/12` with the
tight pigeonhole (proved as Proposition 6.1 in the September 4 revision), calls
this an apparent parameter mismatch, does not rely on the disputed consequence, and explicitly excludes their principal TFNP
separation theorems from the audit. The user reports that the clarification
email has been sent. Author clarification is desirable, but is not a
prerequisite for submission with this independently supported and explicitly
scoped comparison.

The local mathematical recheck found no fatal upper-bound defect and fixed
the classical-baseline truncation, conditional-probability notation, oracle
cost wording, and abort semantics. The author approved this candidate for
submission; final human responsibility remains with the author. Novelty and
ITCS significance remain risks, not established acceptance claims. See
`reviews/QUANTUM_SUBMISSION_READINESS_2026-09-01.md`.

## Human-owned submission actions

- [x] Incorporate the completed ChatGPT Pro mathematical review.
- [x] Accurately retain and scope the closest-source JLRX discrepancy.
- [x] Seek clarification from the JLRX authors (user reports email sent).
- [x] Confirm the final human author list and ordering.
- [x] Obtain the sole listed author's approval to submit the current manuscript,
  including its disclosed AI use and author-responsibility statement.
- [x] Register the title and abstract on the ITCS submission server.
- [x] Upload and save the anonymous PDF to submission `#193`.
- [x] Confirm and complete the PC conflict declaration (author confirms none).
- [x] Retain the AI disclosure in the uploaded manuscript.
- [x] Record the uploaded local PDF hash and matching server checksum prefix.
- [x] Mark the submission ready for review and verify the final server state.

The last verified external state is **submitted and ready for review**. The server
states that no further action is needed, while allowing revisions through
2026-09-04 16:59:59 PDT. The 17:04:26 PDT update replaced only the PDF with the
author-approved AI-disclosure revision. The title, abstract, topics, conflict
declarations, AI preferences and survey, repository visibility, and license
were not changed. The ready-for-review checkbox remains checked.
