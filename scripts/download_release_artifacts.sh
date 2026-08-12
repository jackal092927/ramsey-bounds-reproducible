#!/usr/bin/env bash
set -euo pipefail

repo="${RAMSEY_GITHUB_REPO:-jackal092927/ramsey-bounds-reproducible}"
tag="${RAMSEY_ARTIFACT_TAG:-evidence-2026-08-12}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
destination="${repo_root}/artifacts/downloads"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required to download private release assets." >&2
  exit 2
fi

mkdir -p "${destination}"
gh release download "${tag}" --repo "${repo}" --dir "${destination}" --clobber
"${repo_root}/.venv/bin/python" "${repo_root}/scripts/verify_artifacts.py" \
  --directory "${destination}"

echo RELEASE_ARTIFACTS_DOWNLOADED_AND_VERIFIED
