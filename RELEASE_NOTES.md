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
  source-relative fixed-large-`C` statement conditional on source items (S1),
  (S2), (S4), and (S5), with weighted reverse propagation (S3) proved locally.
  The order is:
  fixed `C` and fixed `w > omega_0`, then `ell -> infinity`, then
  `w -> omega_0` from above, and only afterward `C -> infinity`.
- **Finite barrier:** a proof-carrying one-sided deletion repair radius at
  least seven for one labelled 100-vertex seed. Exact seven remains `UNKNOWN`,
  and no implication `R(3,18) >= 101` is made. A follow-up branch-1 degree-cap
  lemma removes 87.5813014052041% of raw residual six-deletion sets. An
  order-aware reconstruction removed two apparent separator stalls, but all
  sixteen bounded deletion-first endpoints remain `UNKNOWN` and are not
  theorem evidence. Four proof-checked singleton consequences then force the
  preservation of four named seed edges in the frozen branch-1 common
  relaxation. A checked satisfying model proves that the relaxation is
  nonempty but is not a target repair. Combined with the degree cap, the
  singleton filter excludes 87.88321365513743% of raw branch-1 supports; exact
  seven remains `UNKNOWN`. The latest structural audit proves a
  maximal-triangle-free normal form and freezes its combination with the full
  530,525-mask union as a 639,290-variable CNF. Its single 300-second Sirius
  probe returned `UNKNOWN`; no model, proof, cut, branch closure, or global
  implication resulted.

The exact proof-status and trust boundaries are recorded in `STATUS.md`, the
paper, and `reviews/REVIEW_DISPOSITION.md`.

## Release assets

The published Release must contain exactly the 26 assets listed in
`artifacts/MANIFEST.tsv`: the six historical theorem CNF/DRAT pairs, four
strongest singleton CNF/DRAT pairs, the common CNF/model pair, two audited
checker binaries, the source marker, and the upstream checker license. The
manifest fixes every name, byte count, and SHA-256 digest. Ordinary source
clones remain small because the large proof traces are Release assets rather
than Git objects.

GitHub Release immutability locks the tag and assets after publication and
provides a signed release attestation. The release-triggered workflow verifies
that attestation, binds every downloaded file to it, reconstructs six theorem
formulas and four singleton formulas, replays all ten DRAT refutations, and
checks the complete common-relaxation model.

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
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir artifacts/downloads \
  --drat-trim artifacts/downloads/drat-trim-2e3-linux-x86_64
```

The planned download path uses only public GitHub endpoints and requires no GitHub
account or token. It verifies all bytes before setting checker executable
mode. The strict branch-1 gate accepts exactly either audited checker binary
hash in the manifest; source builds remain available for manual comparison
but are not a substitute for the normative replay.

## Rights and publication boundary

Copyright © 2026 Cheng Xin. All rights reserved. No public reuse license is
granted; see `LICENSE.md` and `THIRD_PARTY_NOTICES.md`.

No DOI, DOI-bearing archival deposit, external human peer review, formal
proof-assistant verification, publication, priority, or world-best claim is
made. Public reproducibility and peer-reviewed publication are distinct.
