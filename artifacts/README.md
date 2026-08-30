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
- verified large CNF/DRAT pairs as release assets; and
- incomplete or unverified traces outside the publication artifact set.

After downloading release assets into `artifacts/downloads/`, run:

```bash
bash scripts/download_release_artifacts.sh
```

The planned default release tag is `evidence-2026-08-30` in the intended
public repository. Until that release is actually published, the command is a
release contract rather than evidence of public availability. Override
`RAMSEY_GITHUB_REPO` or `RAMSEY_ARTIFACT_TAG` when replaying a mirror.

The proof status is determined by the theorem reports and verified manifests,
not merely by the presence of a file with a `.drat.gz` suffix.
