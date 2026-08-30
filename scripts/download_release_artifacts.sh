#!/usr/bin/env bash
set -euo pipefail

repo="${RAMSEY_GITHUB_REPO:-jackal092927/ramsey-bounds-reproducible}"
tag="${RAMSEY_ARTIFACT_TAG:-evidence-2026-08-30}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
destination="${repo_root}/artifacts/downloads"

if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required to download the public release assets." >&2
  exit 2
fi

if [[ -e "${destination}" ]] && [[ -n "$(find "${destination}" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "Refusing to mix release assets with an existing nonempty directory: ${destination}" >&2
  echo "Move that directory aside before downloading a fresh immutable release." >&2
  exit 2
fi

expected_list="$(mktemp)"
actual_list="$(mktemp)"
asset_table="$(mktemp)"
release_json="$(mktemp)"
cleanup_lists() {
  rm -f "${expected_list}" "${actual_list}" "${asset_table}" "${release_json}"
}
trap cleanup_lists EXIT

awk -F '\t' '!/^#/ && NF == 3 {print $3}' "${repo_root}/artifacts/MANIFEST.tsv" \
  | LC_ALL=C sort > "${expected_list}"

# The public REST endpoint keeps this path credential-free.  In particular,
# callers do not need a GitHub account, gh configuration, or a token.
curl --fail --location --silent --show-error --retry 5 --retry-all-errors \
  --header 'Accept: application/vnd.github+json' \
  --header 'X-GitHub-Api-Version: 2026-03-10' \
  "https://api.github.com/repos/${repo}/releases/tags/${tag}" \
  --output "${release_json}"

"${repo_root}/.venv/bin/python" - \
  "${release_json}" \
  "${asset_table}" \
  "${repo_root}/artifacts/MANIFEST.tsv" \
  "${tag}" <<'PY'
import json
import sys
from pathlib import Path

release_path = Path(sys.argv[1])
table_path = Path(sys.argv[2])
manifest_path = Path(sys.argv[3])
expected_tag = sys.argv[4]
release = json.loads(release_path.read_text(encoding="utf-8"))

if release.get("tag_name") != expected_tag:
    raise SystemExit("release tag does not match the requested tag")
if release.get("draft") is not False:
    raise SystemExit("release is still a draft")
if release.get("prerelease") is not False:
    raise SystemExit("release is marked as a prerelease")
if release.get("immutable") is not True:
    raise SystemExit("release is not immutable")

expected = {}
for number, raw in enumerate(
    manifest_path.read_text(encoding="utf-8").splitlines(), 1
):
    if not raw or raw.startswith("#"):
        continue
    fields = raw.split("\t")
    if len(fields) != 3:
        raise SystemExit(f"manifest line {number} does not have three fields")
    digest, raw_size, name = fields
    if name in expected:
        raise SystemExit(f"duplicate manifest asset name: {name!r}")
    if (
        "/" in name
        or "\\" in name
        or name in {".", ".."}
        or any(character in name for character in "\t\r\n")
    ):
        raise SystemExit(f"unsafe manifest asset name: {name!r}")
    expected[name] = (int(raw_size), digest)

rows = []
seen = set()
for asset in release.get("assets", []):
    name = asset.get("name")
    url = asset.get("browser_download_url")
    if not isinstance(name, str) or not isinstance(url, str):
        raise SystemExit("release contains an asset without a name or download URL")
    if (
        "/" in name
        or "\\" in name
        or name in {".", ".."}
        or any(character in name for character in "\t\r\n")
    ):
        raise SystemExit(f"unsafe release asset name: {name!r}")
    if name in seen:
        raise SystemExit(f"duplicate release asset name: {name!r}")
    seen.add(name)
    if name not in expected:
        raise SystemExit(f"unexpected release asset: {name!r}")
    expected_size, expected_digest = expected[name]
    if asset.get("state") != "uploaded":
        raise SystemExit(f"release asset is not fully uploaded: {name!r}")
    if asset.get("size") != expected_size:
        raise SystemExit(f"release asset size mismatch: {name!r}")
    if asset.get("digest") != f"sha256:{expected_digest}":
        raise SystemExit(f"release asset API digest mismatch: {name!r}")
    rows.append((name, url))
if seen != set(expected):
    missing = sorted(set(expected) - seen)
    raise SystemExit(f"release is missing manifest assets: {missing!r}")
table_path.write_text(
    "".join(f"{name}\t{url}\n" for name, url in sorted(rows)),
    encoding="utf-8",
)
PY

cut -f 1 "${asset_table}" > "${actual_list}"
if ! diff -u "${expected_list}" "${actual_list}"; then
  echo "Release asset names do not exactly match artifacts/MANIFEST.tsv" >&2
  exit 1
fi

mkdir -p "${destination}"
while IFS=$'\t' read -r name url; do
  curl --fail --location --silent --show-error --retry 5 --retry-all-errors \
    --continue-at - --output "${destination}/${name}" "${url}"
done < "${asset_table}"
"${repo_root}/.venv/bin/python" "${repo_root}/scripts/verify_artifacts.py" \
  --directory "${destination}" --exact

echo RELEASE_ASSET_LIST_AND_CONTENT_VERIFIED
