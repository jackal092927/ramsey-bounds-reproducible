# External proof artifacts

Several proof traces are too large for ordinary GitHub objects. The manifest
contains the three budget-five dependency pairs, the three exact-six headline
pairs, four strongest branch-1 singleton CNF/DRAT pairs, and the branch-1
common CNF/model pair.  It also freezes two audited `drat-trim` binaries, the
pinned source marker, and the upstream MIT license.  Dominated historical
pair-core proofs are intentionally not part of the normative antichain.
Several compressed DRAT files exceed GitHub's 100 MB ordinary-object limit.

The repository therefore keeps:

- all source code and small machine-readable results in Git;
- a SHA-256/size manifest in `artifacts/MANIFEST.sha256` and
  `artifacts/MANIFEST.tsv`;
- verified large CNF/DRAT pairs designated as release assets; and
- incomplete or unverified traces outside the publication artifact set.

The strict `finite-heavy` core-proof gate accepts exactly the manifest's
audited Linux x86-64 or macOS arm64 checker hash.  A local source build remains
useful for manual comparison, but is not a substitute for either normative
binary in the immutable Release replay.

After publication, download the public Release assets into a new
`artifacts/downloads/` directory and verify them by running:

```bash
bash scripts/download_release_artifacts.sh
```

The planned public artifact tag will be
[`evidence-2026-08-30`](https://github.com/jackal092927/ramsey-bounds-reproducible/releases/tag/evidence-2026-08-30).
The download helper defaults to that repository and tag, requires the release
asset-name set to equal `MANIFEST.tsv` exactly, and verifies every byte count
and SHA-256 digest. Override `RAMSEY_GITHUB_REPO` or `RAMSEY_ARTIFACT_TAG` when
replaying a mirror.

The proof status is determined by the theorem reports and verified manifests,
not merely by the presence of a file with a `.drat.gz` suffix.
