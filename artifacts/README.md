# External proof artifacts

Several proof traces are too large for ordinary GitHub objects. The manifest
contains both the three budget-five dependency pairs and the three exact-six
headline pairs. In
particular, compressed DRAT files in `routes/finite/` range from roughly
146 MB to more than 600 MB, above GitHub's 100 MB per-file limit.

The repository therefore keeps:

- all source code and small machine-readable results in Git;
- a SHA-256/size manifest in `artifacts/MANIFEST.sha256` and
  `artifacts/MANIFEST.tsv`;
- verified large CNF/DRAT pairs designated as release assets; and
- incomplete or unverified traces outside the publication artifact set.

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
