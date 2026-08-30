# Consolidated adversarial-review disposition

Date: 2026-08-30  
Scope: the single canonical manuscript at `papers/unified/main.tex`, its
generated PDF, and the complete local reproduction package  
Status: local review complete; external second opinion and public clean-clone
verification pending

## Executive conclusion

The project now has one paper, not three. The directories `papers/upper`,
`papers/lower`, and `papers/finite` are derivation and provenance components;
`papers/unified/main.tex` and `papers/unified/main.pdf` are the sole canonical
publication outputs.

No local adversarial review found a counterexample to the three scoped
results. The correct claim statuses are nevertheless different:

| result | final local proof status | indispensable boundary |
|---|---|---|
| diagonal upper bound | **PROVABLE AS STATED** | conditional on the three version-pinned Yang--Mao v1 interfaces, the locally proved BookCor/correlation implications, and Arb ball containment |
| fixed-ratio lower bound | **PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION** as a Ramsey headline; the local ledger is **PROVABLE AS STATED** conditional on (S1)--(S5) | (S3) is an additional weighted-extension hypothesis with a frozen scalar baseline and is not attributed as a theorem stated by HMS or Lin--Niu |
| fixed-seed deletion barrier | **PROVABLE AS STATED** | local to one labelled 100-vertex seed, one one-sided edit metric, semantic CNF reconstruction, exhaustive branch cover, and six checked DRAT refutations |
| existence or nonexistence of an exact-seven repair | **NOT CURRENTLY JUSTIFIED** | all three bounded exact-seven runs ended `UNKNOWN` and produced neither a witness nor a proof |
| a new global bound (R(3,18)\ge101) | **NOT CURRENTLY JUSTIFIED** | the fixed-seed barrier is not an existence construction and implies no global Ramsey-number improvement |

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
| G2: artifact language could imply an already public release | **CLOSED FOR PRE-PUBLICATION**: the paper labels the section a planned release and says GitHub/release publication remains pending |
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

The final canonical PDF has 79 pages and SHA-256
`8ed2aec0a38278dd81bc669eda36dd15c8f86324a65c6ebf3af271d33e1c7d1a`.
Its log has no overfull box, undefined or multiply defined reference, LaTeX
warning, error, or fatal diagnostic. Representative pages spanning all three
Parts, every appendix family, long equations, tables, hashes, commands, and
the bibliography were visually inspected without finding clipping, overlap,
or unreadable content.

## Open external gates

The following are not closed by local evidence:

1. The ChatGPT Pro second-opinion review has not yet been transmitted or
   received.
2. The intended GitHub repository does not yet exist, and no immutable public
   release containing exactly the twelve manifest assets has been verified.
3. No credential-free fresh-clone replay or hosted CI result exists for the
   release commit.
4. No public reuse license has been selected. Copyright remains retained by
   Cheng Xin unless the author chooses explicit software and manuscript
   licenses.
5. No DOI, archival deposit, external human peer review, or proof-assistant
   formalization is claimed.

These gates affect public reproducibility and submission confidence; they do
not alter the scoped local proof-status labels above. Any external objection
must be logged, repaired or explicitly rejected with reasons, and reflected in
the manuscript before the package is called a public release.
