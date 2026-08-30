# Draft evidence release notes for `evidence-2026-08-30`

**Publication condition.** This file is the source for the GitHub Release
body. Statements below about “the release” become current-state assertions
only after GitHub reports this tag as published, non-prerelease, and immutable
with the exact manifest asset set. A source checkout containing this file is
not by itself evidence that publication occurred.

When published and verified, this immutable evidence Release will accompany
one unified Ramsey-theory manuscript. It will not represent three separate
papers.

## Scoped claims

- **Diagonal upper bound:** the conditional, source-relative asymptotic
  statement `R(k,k) <= (3.780685290)^(k+o(k))`, with the longer certified upper
  endpoint documented in the paper.
- **Fixed-ratio lower addition:** after fixing the source constant `K`, the
  source-relative fixed-large-`C` statement conditional on (S1)--(S5), with
  (S3) explicitly an additional weighted-extension assumption. The order is:
  fixed `C` and fixed `w > omega_0`, then `ell -> infinity`, then
  `w -> omega_0` from above, and only afterward `C -> infinity`.
- **Finite barrier:** a proof-carrying one-sided deletion repair radius at
  least seven for one labelled 100-vertex seed. Exact seven remains `UNKNOWN`,
  and no implication `R(3,18) >= 101` is made.

The exact proof-status and trust boundaries are recorded in `STATUS.md`, the
paper, and `reviews/REVIEW_DISPOSITION.md`.

## Release assets

The published Release must contain exactly the twelve compressed CNF/DRAT files listed in
`artifacts/MANIFEST.tsv`, totalling 1,342,246,254 bytes. The manifest fixes each
asset's name, compressed byte count, and SHA-256 digest. Ordinary source clones
remain small because these proof traces are Release assets rather than Git
objects.

GitHub Release immutability locks the tag and assets after publication and
provides a signed release attestation. The release-triggered workflow verifies
that attestation, binds every downloaded file to it, reconstructs the six SAT
instances, and replays all six DRAT refutations.

## Reproduction

From a clean checkout of the eventual tag:

```bash
bash scripts/bootstrap.sh
.venv/bin/python reproduce.py quick
.venv/bin/python reproduce.py full
.venv/bin/python reproduce.py sources
make paper
```

The finite proof-carrying replay is:

```bash
bash scripts/download_release_artifacts.sh
bash scripts/build_drat_trim.sh /absolute/path/to/new-checker-directory
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir artifacts/downloads \
  --drat-trim /absolute/path/to/new-checker-directory/drat-trim
```

The planned download path uses only public GitHub endpoints and requires no GitHub
account or token. A checker executable hash is current-run provenance; the
portable acceptance condition is the pinned checker source revision plus a
successful replay, not a cross-platform binary hash.

## Rights and publication boundary

Copyright © 2026 Cheng Xin. All rights reserved. No public reuse license is
granted; see `LICENSE.md` and `THIRD_PARTY_NOTICES.md`.

No DOI, DOI-bearing archival deposit, external human peer review, formal
proof-assistant verification, publication, priority, or world-best claim is
made. Public reproducibility and peer-reviewed publication are distinct.
