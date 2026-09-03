# Reproducible Ramsey analysis

This repository is the working publication and reproduction package for two
paper artifacts built from shared theorem sources:

- archival unified manuscript: [`papers/unified/main.tex`](papers/unified/main.tex)
  and [`papers/unified/main.pdf`](papers/unified/main.pdf);
- standalone anonymous ITCS quantum submission: [`papers/quantum/main.tex`](papers/quantum/main.tex)
  and [`papers/quantum/main.pdf`](papers/quantum/main.pdf).

The unified manuscript places four logically independent Ramsey results in a single
claim-to-evidence framework. The older directories
[`papers/upper`](papers/upper), [`papers/lower`](papers/lower), and
[`papers/finite`](papers/finite) remain provenance components.  The quantum
directory is both the shared source component and a separate submission
target; it intentionally excludes the other three results.

The current research consolidation is the
[project results and collaboration dossier](research/pro_collaboration_2026-09-02/README.md).
The [canonical TDA collaboration record](research/quantum_direction_selection/collaboration/2026-09-02/README.md)
contains the latest proof packet, Pro dispatch and continuation state. It
prioritizes true normalized persistence with explicit source and gate-set
dependencies, while preserving the useful negative results and alternative
directions. These are research candidates, separate from the submitted
quantum Ramsey theorem.

## Results and exact scope

| part | scoped result | evidence boundary |
|---|---|---|
| diagonal upper bound | \(R(k,k)\le(3.780685290)^{k+o(k)}\), with certified unrounded base below `3.780685288379640114` | asymptotic and source-relative; depends on version-pinned retained-spine/book interfaces, the certified six-stage rate, and interval-arithmetic containment semantics; no effective finite-\(k\) threshold |
| fixed-ratio lower bound | after fixing the source constant \(K\), for each sufficiently large fixed \(C\), a source-relative addition \(\widehat H_*(C)=(1+o_{C\to\infty}(1))/(64\log C)\) | conditional on the version-pinned source items (S1), (S2), (S4), and (S5); weighted reverse propagation (S3) is proved locally from the indicator kernel and tower property; for fixed \(C\) and \(w>\omega_0\), first take \(\ell\to\infty\), then \(w\downarrow\omega_0\), and only afterward \(C\to\infty\); \(C_0(K)\) is non-effective |
| finite proof-carrying barrier | for the pinned 100-vertex near miss, the one-sided deletion repair radius under free additions is at least seven | local to one labelled seed and one edit metric; exact seven remains `UNKNOWN`; this does **not** imply \(R(3,18)\ge101\) |
| quantum constructive search | on any coherently queried graph with at least \(4^{K-1}\) vertices, a verified homogeneous \(K\)-set can be found in \(O(2^K K\log(K/\eta))\) edge queries; a cleaner size-biased proof gives \(O(2^K K^2\log K\log(1/\eta))\) and extends to multiple colours | proved worst-case query upper bounds; no numerical Ramsey improvement, physical-speedup claim, or separation from all randomized classical algorithms; a published lower-bound parameter conflict awaits clarification |

No claim of a world-best bound, publication priority, global parameter
optimality, formal proof-assistant verification, or publication is made.

## Public source and release-candidate state

The source repository is public at
[`jackal092927/ramsey-bounds-reproducible`](https://github.com/jackal092927/ramsey-bounds-reproducible).
The evidence package is designated for the tagged release
[`evidence-2026-08-30`](https://github.com/jackal092927/ramsey-bounds-reproducible/releases/tag/evidence-2026-08-30)
and is valid only if it provides exactly the 26 content-addressed assets listed
in [`artifacts/MANIFEST.tsv`](artifacts/MANIFEST.tsv). At this pre-release
snapshot the final tag, immutable Release, credential-free asset download,
and final-tag replay remain pending. Their completion must be recorded in a
post-publication verification report rather than inferred from this README.

This is a public source repository containing a reproducibility release
candidate, not yet a completed artifact Release or a peer-reviewed
publication. No DOI has been assigned. No public reuse license is granted;
copyright remains with Cheng Xin.

The first-round audits and all post-repair reviews are retained under
[`reviews`](reviews). The consolidated current verdict is
[`reviews/REVIEW_DISPOSITION.md`](reviews/REVIEW_DISPOSITION.md), and the
fresh independent mathematical audit is
[`reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md`](reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md).
The three theorem-specific hostile reconstructions and their nine resolved
minor findings are consolidated in
[`reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md`](reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md).
The subsequent local proof and adversarial closure of lower item S3 is
[`reviews/LOWER_S3_CLOSURE_2026-08-30.md`](reviews/LOWER_S3_CLOSURE_2026-08-30.md).
The theorem-by-theorem mathematical audit of the new quantum part is
[`reviews/QUANTUM_RAMSEY_MATHEMATICAL_AUDIT_2026-08-31.md`](reviews/QUANTUM_RAMSEY_MATHEMATICAL_AUDIT_2026-08-31.md).
The repository-wide publication protocol audit is
[`reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`](reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md).
The ChatGPT Pro second-opinion report and claim-by-claim disposition are
[`reviews/CHATGPT_PRO_REVIEW.md`](reviews/CHATGPT_PRO_REVIEW.md).
The historical exact-seven collaboration packet is retained at
[`reviews/CHATGPT_PRO_EXACT7_COLLABORATION_PACKET.md`](reviews/CHATGPT_PRO_EXACT7_COLLABORATION_PACKET.md).
A completed text-only Pro reply has now been recovered and preserved with
[its disposition](research/pro_collaboration_2026-09-02/REVIEW_DISPOSITION.md).
That reply predates the checked singleton progress and does not supersede it.
The separate quantum Ramsey review was completed and dispositioned; a later
narrow differential review ended in a network error without a final verdict.
The publication-facing state is [`STATUS.md`](STATUS.md). Local or AI-assisted
adversarial review does not substitute for independent external human peer
review.

The exact-seven branch-1 follow-up, including the degree-cap proof, exact
87.5813014052041% raw deletion-set pruning, bounded Sirius matrices,
order-aware oracle reconstruction, fail-closed endpoints, and stop rule, is
recorded in
[`routes/finite/R3_18_BUDGET7_BENDERS_PILOT_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BENDERS_PILOT_2026-08-30.md).
All sixteen deletion-first endpoints remain `UNKNOWN`. Reverse vertex order
removed two apparent independent-set-separator stalls, while all seven repaired
gates reached their global walls while still in the master under the tested
configurations. These are diagnostic facts, not a strengthening of the global
Ramsey interval.

A proof-carrying follow-up strengthens the branch-1 filter from four pair
clauses to four singleton consequences: every model of the frozen common
relaxation preserves `(11,62)`, `(18,61)`, `(18,64)`, and `(18,69)`.  All four
singleton refutations passed byte-independent CNF reconstruction and DRAT
replay on x86-64 and arm64.  A checked SAT model proves that the common
relaxation is nonempty, but that model contains an explicit independent
18-set and is not a repair.  Combined with the degree cap, the singleton
consequences exclude 87.88321365513743% of the raw branch-1 residual supports
and leave exact seven `UNKNOWN`.  The full ledger is
[`routes/finite/R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md).

The latest no-repeat gate proves a maximal-triangle-free normal form for any
branch-1 target and combines it with the complete 530,525-mask union.  Its
byte-audited CNF has 639,290 variables and 1,972,360 clauses (SHA-256
`09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb`).
One fixed 300-second Sirius call returned wrapper exit 124 and `c UNKNOWN`.
The incomplete proof prefix was hashed and deleted without replay; no model,
certificate, cut, or branch closure resulted.  The exact endpoint and
fail-closed checker are documented in
[`routes/finite/R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md).

## Verified local snapshot

On 2026-08-31 the following gates passed after the quantum integration:

- the current `quick` tier, including the new exact quantum audit; the legacy
  upper/lower components had also passed `full` and networked `sources`
  earlier that day and were not changed mathematically by this integration;
- the exact 26-asset finite-heavy gate, including six theorem-formula and four
  singleton-formula reconstructions, all ten checked DRAT replays, and the
  complete common-relaxation model audit;
- deterministic materialization of the unified manuscript;
- compilation and anonymity/font/reference checks for the standalone
  16-page ITCS quantum draft, whose central claims and concise literature
  comparison appear within the first ten pages;
- compilation of a 115-page PDF with no overfull box, unresolved or multiply
  defined reference, LaTeX warning, error, or fatal diagnostic; and
- representative-page visual inspection.

The current 115-page unified PDF SHA-256 is
`8fcb9c04133bf558391f452894a94c1bb7cfb917aa1b7d1036ebbc755dfcb3b6`.
The current 16-page anonymous quantum PDF SHA-256 is
`e47b80073b1333668c2203c970548df55c1db51bdd005c268de4667077563cd7`.
This version shortens the AI disclosure. The
[submission receipt](papers/quantum/SUBMISSION_CHECKLIST.md) records its
resubmission to ITCS #193 on September 2 at 17:04:26 PDT and the server's
ready-for-review confirmation. The September 3 consolidation rechecked the
local PDF hash; it did not operate or refresh HotCRP.
The current submitted PDF is preserved at
`papers/quantum/submitted/itcs2027-paper193-2026-09-02-v2.pdf`.
The first September 2 submitted PDF is preserved separately at
`papers/quantum/submitted/itcs2027-paper193-2026-09-02.pdf`; its SHA-256 is
`bd11783756a99ac1ab865548ab08078dbb969d3034b44ef8df2e134640696a2f`.
The September 1 submission candidate now uses the official LIPIcs class in
anonymous mode with a separate ITCS 11pt review adapter. The main quantum
upper-bound proof finishes on page 8, the detailed comparison and conclusion
finish on page 11, and the appendices begin on page 12. The final standalone
build has no LaTeX/BibTeX warnings. The layout-only migration preserves all
mathematical content and references; see
[`papers/quantum/TEMPLATE.md`](papers/quantum/TEMPLATE.md).
The subsequent editorial pass makes Appendix C.2 a self-contained account of
the numerical experiments, retaining methods and outcomes but removing source
paths and run commands. Reproduction instructions remain in the repository;
the anonymous paper does not depend on access to a code artifact.
For the earlier candidate, with `SOURCE_DATE_EPOCH` fixed, two clean builds under the
recorded pdfTeX 1.40.24 (TeX Live 2022) and Latexmk 4.77 toolchain were
byte-identical.
Byte identity across different TeX distributions, font packages, or engines is
not claimed. A separate ChatGPT Pro AI second opinion completed on
2026-08-30 for the first three parts. Every recoverable concrete objection was
checked against those canonical sources and repaired or explicitly
dispositioned in the archived report. The quantum-specific Pro review
completed and was dispositioned on 2026-08-31. A narrower final-delta packet
covering the experiment paragraph, references, and JLRX wording was prepared
and submitted to the same personal-account Pro conversation on 2026-09-01;
its latest visible state is a network error after interim analysis, not a
completed verdict. Neither completed review is external human peer review.
The latest local mathematical pass and JLRX source comparison are recorded in
[`reviews/QUANTUM_SUBMISSION_READINESS_2026-09-01.md`](reviews/QUANTUM_SUBMISSION_READINESS_2026-09-01.md).
The user reports sending the author inquiry; receiving a reply is desirable
but not required before submission with the current scoped comparison.

## Reproduction

The reference Python environment is 3.11.15 with dependencies locked in
[`uv.lock`](uv.lock), materialized by exactly `uv 0.10.2`. The bootstrap
fails closed if that `uv` version is unavailable; there is no unhashed pip
fallback in the reproduction contract. From a clean local checkout:

```bash
bash scripts/bootstrap.sh
.venv/bin/python reproduce.py quick
make paper
```

`quick` performs repository-integrity checks, the current upper transfer
checks, the current lower arithmetic check, all finite-route unit tests, the
lightweight graph-certificate checks, and the exact quantum-recurrence audit.
It does not replay the long upper rate chain or the large finite DRAT proofs.

The quantum diagnostics can also be run alone:

```bash
make verify-quantum
```

The heavier offline asymptotic replay is:

```bash
.venv/bin/python reproduce.py full
```

The separate networked source-identity tier downloads the three pinned arXiv
members and five upstream graph matrices into temporary storage and verifies
their hashes:

```bash
.venv/bin/python reproduce.py sources
```

The proof-carrying finite replay requires every file listed in
[`artifacts/MANIFEST.tsv`](artifacts/MANIFEST.tsv) and one of the two audited
`drat-trim` binaries in that manifest.  The credential-free download helper
verifies the bytes before setting executable mode.  A portable source-build
helper remains available for non-normative manual comparison:

```bash
bash scripts/build_drat_trim.sh /absolute/path/to/new-checker-directory
```

The strict core-proof gate accepts exactly the audited Linux x86-64 or macOS
arm64 binary hash; an arbitrary local build is not a substitute for this
normative gate.  Run the theorem replay with:

```bash
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir /absolute/path/to/artifact-directory \
  --drat-trim /absolute/path/to/audited-manifest-binary
```

[`scripts/download_release_artifacts.sh`](scripts/download_release_artifacts.sh)
uses the public GitHub REST endpoint without a GitHub account, CLI login, or
token. It compares the release's complete asset-name set with the manifest,
downloads into a clean directory, and verifies every byte count and digest.

The unified manuscript is materialized deterministically from the four source
components, and both paper artifacts are compiled by:

```bash
make paper
```

`make papers` is retained as an alias for the same two-output build.

## Evidence levels

The repository keeps the following states distinct:

- a written analytic implication;
- a version-pinned source interface;
- an interval certificate;
- a semantically reconstructed SAT instance;
- a replayed DRAT proof;
- a bounded solver outcome such as `UNKNOWN`; and
- an unrerun historical provenance record.

A hash authenticates bytes, not a mathematical implication. A solver log is
not a proof unless its encoding, case coverage, and proof trace are all
checked. In particular, an `UNKNOWN` exact-seven run is evidence of neither
existence nor nonexistence.

## Repository map

| path | role |
|---|---|
| [`papers/unified`](papers/unified) | archival unified manuscript and local PDF |
| [`papers/upper`](papers/upper) | archival upper-part source component |
| [`papers/lower`](papers/lower) | archival lower-part source component |
| [`papers/finite`](papers/finite) | archival finite-part source component |
| [`papers/quantum`](papers/quantum) | standalone anonymous ITCS submission and shared quantum source |
| [`routes/upper`](routes/upper) | upper-bound proofs, searches, certificates, and replay logs |
| [`routes/lower`](routes/lower) | lower-bound proof ledger, arithmetic checks, and audits |
| [`routes/finite`](routes/finite) | finite graph encodings, metadata, search records, and checkers |
| [`experiments/quantum_ramsey`](experiments/quantum_ramsey) | exact recurrence, split-tree, and ideal-sampler diagnostics |
| [`artifacts`](artifacts) | manifest for large proof-carrying assets |
| [`reviews`](reviews) | adversarial mathematical and reproducibility reviews |
| [`scripts`](scripts) | bootstrap, materialization, verification, and release helpers |

## Release boundary

The planned release will record one unified manuscript, a tag-bound source snapshot,
an immutable 26-asset evidence package, the pinned checker source revision,
adversarial-review dispositions, and separate light/full/finite-heavy build
logs. Historical searches and old review snapshots remain labelled by what was
actually rerun at the time.

Public availability does not grant reuse rights. [`LICENSE.md`](LICENSE.md)
retains copyright and grants no license; [`CITATION.cff`](CITATION.cff) supplies
citation metadata without inventing a DOI. No external human peer review,
archival deposit, proof-assistant formalization, priority claim, or formal
publication is implied.

See [`PAPER_PLAN.md`](PAPER_PLAN.md) for the unified editorial plan and
[`NARRATIVE_REPORT.md`](NARRATIVE_REPORT.md) for the claim narrative.
