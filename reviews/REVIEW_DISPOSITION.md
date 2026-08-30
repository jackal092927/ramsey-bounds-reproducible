# Consolidated adversarial-review disposition

Date: 2026-08-30  
Scope: the single canonical manuscript at `papers/unified/main.tex`, its
generated PDF, and the complete local reproduction package  
Status: local and ChatGPT Pro author-side reviews complete and dispositioned;
final-tag and public-Release verification pending

## Executive conclusion

The project now has one paper, not three. The directories `papers/upper`,
`papers/lower`, and `papers/finite` are derivation and provenance components;
`papers/unified/main.tex` and `papers/unified/main.pdf` are the sole canonical
publication outputs.

No local adversarial review found a counterexample to the three scoped
results. The correct claim statuses are nevertheless different:

| result | final local proof status | indispensable boundary |
|---|---|---|
| diagonal upper bound | **PROVABLE AS STATED ONLY UNDER THE EXPLICIT SOURCE-INTERFACE AND INTERVAL-ARITHMETIC TRUST BOUNDARY** | conditional on the three version-pinned Yang--Mao v1 interfaces, the locally proved BookCor/correlation implications, and Arb ball containment |
| fixed-ratio lower bound | **PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION** as a Ramsey headline; the local ledger is **PROVABLE AS STATED** conditional on (S1)--(S5) | the frozen scalar baseline belongs to (S2); (S3) consists only of the additional weighted-extension implication and is not attributed as a theorem stated by HMS or Lin--Niu |
| fixed-seed deletion barrier | **PROVABLE AS STATED** | local to one labelled 100-vertex seed, one one-sided edit metric, semantic CNF reconstruction, exhaustive branch cover, and six checked DRAT refutations |
| existence or nonexistence of an exact-seven repair | **NOT CURRENTLY JUSTIFIED** | all three bounded exact-seven runs ended `UNKNOWN` and produced neither a witness nor a proof |
| a new global bound (R(3,18)\ge101) | **NOT CURRENTLY JUSTIFIED** | the fixed-seed barrier is not an existence construction and implies no global Ramsey-number improvement |

The fresh independent audit in
`reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md` reached the same scoped
verdicts without using the earlier review conclusions as premises. It found
zero fatal and zero major issues and one terminological minor: two references
to a “history in” the terminal event \(B_r^R\). Both occurrences now quantify
over a red-admissible \(\mathcal F_{i-1}\)-history for target \(r\); this
changed no estimate, theorem, or constant.

The final theorem-specific hostile reconstructions are consolidated in
`reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md`. They found zero
fatal and zero major issues, plus nine minor findings. The upper proof now
spells out two omitted elementary cases and separates local from external
dependencies; the lower proof keeps S3 unambiguously hypothetical and narrows
its replay sentinel; the finite package uses an exact DRAT status line,
represents unknown data as null, and corrects the artifact-ledger scope.
The repository-wide publication audit and safe immutable-release sequence are
recorded in `reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`; its
implementation verdict is zero remaining blocker, major, or minor finding
after repair, while live publication remains an open external gate.

The ChatGPT Pro second opinion is archived and dispositioned in
`reviews/CHATGPT_PRO_REVIEW.md`. Its valid presentation and trust-boundary
objections led to an explicit first-prior lemma, a complete half-line base
gate, clearer 256/512-bit separation, stricter certificate parsing, a cleaner
S2/S3 split and limit ledger, and a constructive sequential-counter semantics
lemma with an independent implementation. It reported no numerical
counterexample to a scoped theorem. This remains AI-assisted author-side
review, not external human peer review.

A final hostile integration pass then found three non-theorem defects that a
successful LaTeX build or unit test alone would not expose. The unified-source
materializer's context-free equation-tag replacement had silently changed the
correct function evaluation `D(2.9)` into an equation reference; it now uses a
context-sensitive replacement rule with regression tests and explicit
cross-scope mappings. The finite-heavy driver passed DRAT-only flags to the
new independent sequential-counter checker; the checker and DRAT auditors now
run as separate commands. Four missing backslashes before `\qquad` and an
interrupting finite table placement were also repaired. Repository checks now
fail on a recurrence of that malformed token or release-facing control bytes.

## Mathematical findings and repairs

### Upper component

The first review identified four blocking classes: an incomplete imported
interface, a missing outer wedge, unsupported decimal precision, and no
theorem connecting the rate certificates to the displayed rate. The repaired
paper now:

1. states the exact regularization, parameterized-book, and compatibility
   interfaces and proves the positive-moment/tail handoff locally;
2. covers the direct region, exceptional wedge, both colour orientations,
   reservoir endpoint, and the (x=y=1) endpoint;
3. prints a 512-bit outward enclosure with unrounded base strictly below
   `3.780685288379640114`; and
4. proves the finite-net, density-split, small-ratio, induction, and exact
   six-certificate identity implications.

The generated-copy audit reproduced all ten upper files byte for byte and
found 106 labels, 116 references, and 85 handwritten tags with no duplicate,
unresolved, unnamespaced, or malformed item. U1--U4 and the endpoint/notation
gate are closed.

### Lower component

The first review correctly rejected prose references to an undefined weighted
reverse-induction bridge. The repaired paper defines the Gaussian/Bartlett
space, filtration, admissible histories, conditional events and probabilities,
the weighted potential, the one-step invariant, total-probability transition,
projection identities, and scalar baseline. It also repairs the source-line
map, exact-merge normalization, and the scope of the (1/64) method cap.

The resulting boundary is deliberately conditional. Items (S1), (S2), (S4),
and (S5) are explicit version-pinned source hypotheses. Item (S3) is a formal
extra weighted-extension assumption; no sentence in the paper represents it
as a verbatim theorem of HMS or Lin--Niu. Under (S1)--(S5), the residual
recursion, full-box Hessian bound, square completion, Hölder ledger,
same-history accounting, extraction, and red--blue crossing close. The
normalized exact-merge claim closes, and the (1/64) cap closes only inside
the class defined in Definition 16.1, not for all conceivable methods.

### Finite component

The proof-carrying theorem is restricted to the same labelled vertex set and
the metric (d_H(F)=|E(H)\setminus E(F)|), with additions outside (E(H))
free. The local replay independently reconstructed the seed properties,
three-way triangle branch cover, all six CNF semantics, and all six DRAT
refutations with a checker built from pinned source commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`. The exact-seven computations
remain outside the theorem and are recorded only as `UNKNOWN`.

## Global-claim audit

Five global-prose findings were repaired:

| finding | disposition |
|---|---|
| G1: lower summary obscured the extra status of (S3) | **CLOSED**: the abstract, introduction, evidence table, and conclusion now identify (S3) explicitly |
| G2: artifact language could imply an already public release | **CLOSED FOR THE TAG CANDIDATE**: the paper designates the intended tag and asset contract but does not claim that publication, immutability, credential-free download, or final-tag replay has already passed; those require a post-publication verification record |
| G3: finite short statement omitted the same-labelled-set quantifier | **CLOSED** |
| G4: upper source interfaces were hidden under an umbrella phrase | **CLOSED**: all three imported interfaces are enumerated and the local moment/tail proof is separated |
| G5: “new results” risked an unsupported priority reading | **CLOSED**: the wording is now “results developed here” with no priority claim |

## Reproducibility disposition

The post-repair reproducibility review closed all four major implementation
findings: the release-asset overlay, current-run versus stored-provenance
separation, portable checker policy, and accurate quick/full evidence labels.
The following commands or equivalent integrated checks passed on the current
tree:

```text
.venv/bin/python reproduce.py quick        QUICK_REPRODUCTION_PASS
.venv/bin/python reproduce.py full         FULL_REPRODUCTION_PASS
.venv/bin/python reproduce.py sources      EXTERNAL_SOURCE_IDENTITIES_VERIFIED
.venv/bin/python reproduce.py finite-heavy FINITE_HEAVY_REPRODUCTION_PASS
make paper                                  UNIFIED_PAPER_COMPILED
```

The finite-heavy run verified the exact names, byte counts, and SHA-256 values
of all twelve compressed assets before reconstructing semantics and replaying
the proofs. The source tier independently matched three pinned arXiv TeX
members and five upstream graph matrices. The materializer was rerun twice
with identical output.

The current release-candidate PDF has 83 pages and local post-review SHA-256
`6ff124cc1ae5f1504510c7a557cff1fe964c4ec24889e9e050294b56c9553885`.
Two clean builds under the pinned toolchain produced byte-identical PDFs. This
is not yet a published-Release digest; publication and credential-free replay
remain separate external gates.
Its log has no overfull box, undefined or multiply defined reference, LaTeX
warning, error, or fatal diagnostic. Representative pages spanning all three
Parts, every appendix family, long equations, tables, hashes, commands, and
the bibliography were visually inspected without finding clipping, overlap,
or unreadable content.

## Open external gates

The following are not closed by local evidence:

1. The public source repository exists, but the final evidence tag and
   immutable twelve-asset Release do not.
2. Anonymous and hosted verification passed for the initial public commit;
   final-tag Release-asset verification remains pending.
3. No public reuse license is granted; copyright is retained by Cheng Xin.
4. No DOI, archival deposit, external human peer review, or proof-assistant
   formalization is claimed.

These gates affect public reproducibility and submission confidence; they do
not alter the scoped local proof-status labels above. Any external objection
must be logged, repaired or explicitly rejected with reasons, and reflected in
the manuscript before the package is called a public release.
