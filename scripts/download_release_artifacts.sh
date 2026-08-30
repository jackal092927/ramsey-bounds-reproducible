#!/usr/bin/env bash
set -euo pipefail

repo="${RAMSEY_GITHUB_REPO:-jackal092927/ramsey-bounds-reproducible}"
tag="${RAMSEY_ARTIFACT_TAG:-evidence-2026-08-30}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
destination="${repo_root}/artifacts/downloads"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required to download the release assets." >&2
  exit 2
fi

if [[ -e "${destination}" ]] && [[ -n "$(find "${destination}" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "Refusing to mix release assets with an existing nonempty directory: ${destination}" >&2
  echo "Move that directory aside before downloading a fresh immutable release." >&2
  exit 2
fi

expected_list="$(mktemp)"
actual_list="$(mktemp)"
cleanup_lists() {
  rm -f "${expected_list}" "${actual_list}"
}
trap cleanup_lists EXIT

awk -F '\t' '!/^#/ && NF == 3 {print $3}' "${repo_root}/artifacts/MANIFEST.tsv" \
  | LC_ALL=C sort > "${expected_list}"
gh release view "${tag}" --repo "${repo}" --json assets \
  --jq '.assets[].name' | LC_ALL=C sort > "${actual_list}"
if ! diff -u "${expected_list}" "${actual_list}"; then
  echo "Release asset names do not exactly match artifacts/MANIFEST.tsv" >&2
  exit 1
fi

mkdir -p "${destination}"
gh release download "${tag}" --repo "${repo}" --dir "${destination}" --clobber
"${repo_root}/.venv/bin/python" "${repo_root}/scripts/verify_artifacts.py" \
  --directory "${destination}" --exact

echo RELEASE_ASSET_LIST_AND_CONTENT_VERIFIED
