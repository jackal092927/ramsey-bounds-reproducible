# Reproducible Ramsey analysis

This repository is the working publication and reproduction package for one
canonical manuscript:

- source: [`papers/unified/main.tex`](papers/unified/main.tex)
- locally compiled PDF: [`papers/unified/main.pdf`](papers/unified/main.pdf)

The manuscript places three logically independent Ramsey results in a single
claim-to-evidence framework. The older directories
[`papers/upper`](papers/upper), [`papers/lower`](papers/lower), and
[`papers/finite`](papers/finite) are archival source components and provenance
records. They are not separate publication outputs.

## Results and exact scope

| part | scoped result | evidence boundary |
|---|---|---|
| diagonal upper bound | \(R(k,k)\le(3.780685290)^{k+o(k)}\), with certified unrounded base below `3.780685288379640114` | asymptotic and source-relative; depends on version-pinned retained-spine/book interfaces, the certified six-stage rate, and interval-arithmetic containment semantics; no effective finite-\(k\) threshold |
| fixed-ratio lower bound | for each sufficiently large fixed \(C\), a source-relative addition \(\widehat H_*(C)=(1+o_{C\to\infty}(1))/(64\log C)\) | conditional on (S1)--(S5); (S3) is an additional weighted-extension hypothesis not attributed as a theorem stated by HMS or Lin--Niu; the order of limits is fixed \(C\), then \(\ell\to\infty\), and only then \(C\to\infty\) |
| finite proof-carrying barrier | for the pinned 100-vertex near miss, the one-sided deletion repair radius under free additions is at least seven | local to one labelled seed and one edit metric; exact seven remains `UNKNOWN`; this does **not** imply \(R(3,18)\ge101\) |

No claim of a world-best bound, publication priority, global parameter
optimality, formal proof-assistant verification, or publication is made.

## Public source and release-candidate state

The source repository is public at
[`jackal092927/ramsey-bounds-reproducible`](https://github.com/jackal092927/ramsey-bounds-reproducible).
The evidence package is designated for the tagged release
[`evidence-2026-08-30`](https://github.com/jackal092927/ramsey-bounds-reproducible/releases/tag/evidence-2026-08-30)
and is valid only if it provides exactly the twelve CNF/DRAT payloads listed
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
The repository-wide publication protocol audit is
[`reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`](reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md).
The publication-facing state is [`STATUS.md`](STATUS.md). Local or AI-assisted
adversarial review does not substitute for independent external human peer
review.

## Verified local snapshot

On 2026-08-30 the following gates passed on the current worktree:

- `quick`, `full`, and networked `sources` reproduction tiers;
- all finite-heavy semantic audits and six independent DRAT replays;
- deterministic materialization of the single canonical manuscript;
- compilation of a 79-page PDF with no overfull box, unresolved or multiply
  defined reference, LaTeX warning, error, or fatal diagnostic; and
- representative-page visual inspection.

With `SOURCE_DATE_EPOCH` fixed, two clean builds under the recorded pdfTeX
1.40.24 (TeX Live 2022) and Latexmk 4.77 toolchain were byte-identical. The
canonical 79-page PDF SHA-256 is
`bad787b9a37430d39d17d789c9dddc39db212db2db0954fa668dd43c96993804`.
Byte identity across different TeX distributions, font packages, or engines is
not claimed. The external ChatGPT Pro adversarial review was transmitted on
2026-08-30 and remains in progress. No final report is treated as received
until its complete response is archived and every concrete objection is
dispositioned; it is a second opinion, not external human peer review.

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
checks, the current lower arithmetic check, all finite-route unit tests, and
the lightweight graph-certificate checks. It does not replay the long upper
rate chain or the large finite DRAT proofs.

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

The proof-carrying finite replay requires all twelve files listed in
[`artifacts/MANIFEST.tsv`](artifacts/MANIFEST.tsv) and an executable
`drat-trim` built from the source revision documented in the manuscript.  A
portable helper builds it into a new, explicit output directory:

```bash
bash scripts/build_drat_trim.sh /absolute/path/to/new-checker-directory
```

The compiled-binary hash is recorded as run provenance, not required to equal
a binary produced on another platform.  Run the theorem replay with:

```bash
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir /absolute/path/to/artifact-directory \
  --drat-trim /absolute/path/to/drat-trim
```

[`scripts/download_release_artifacts.sh`](scripts/download_release_artifacts.sh)
uses the public GitHub REST endpoint without a GitHub account, CLI login, or
token. It compares the release's complete asset-name set with the manifest,
downloads into a clean directory, and verifies every byte count and digest.

The canonical manuscript is materialized deterministically from the three
archival components and then compiled by:

```bash
make paper
```

`make papers` is retained only as an alias for the same single output.

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
| [`papers/unified`](papers/unified) | canonical manuscript and local PDF |
| [`papers/upper`](papers/upper) | archival upper-part source component |
| [`papers/lower`](papers/lower) | archival lower-part source component |
| [`papers/finite`](papers/finite) | archival finite-part source component |
| [`routes/upper`](routes/upper) | upper-bound proofs, searches, certificates, and replay logs |
| [`routes/lower`](routes/lower) | lower-bound proof ledger, arithmetic checks, and audits |
| [`routes/finite`](routes/finite) | finite graph encodings, metadata, search records, and checkers |
| [`artifacts`](artifacts) | manifest for large proof-carrying assets |
| [`reviews`](reviews) | adversarial mathematical and reproducibility reviews |
| [`scripts`](scripts) | bootstrap, materialization, verification, and release helpers |

## Release boundary

The planned release will record one unified manuscript, a tag-bound source snapshot,
an immutable twelve-asset evidence package, the pinned checker source revision,
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
