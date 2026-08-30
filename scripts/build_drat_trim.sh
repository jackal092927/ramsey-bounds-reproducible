#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 /absolute/output/directory" >&2
  exit 2
fi

output_dir="$1"
case "${output_dir}" in
  /*) ;;
  *)
    echo "output directory must be absolute" >&2
    exit 2
    ;;
esac

if [[ -e "${output_dir}" ]]; then
  echo "refusing to overwrite existing path: ${output_dir}" >&2
  exit 2
fi

source_commit="2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
temporary_root="$(mktemp -d)"
cleanup() {
  rm -rf "${temporary_root}"
}
trap cleanup EXIT

git clone --quiet https://github.com/marijnheule/drat-trim.git "${temporary_root}/source"
git -C "${temporary_root}/source" checkout --quiet "${source_commit}"
test "$(git -C "${temporary_root}/source" rev-parse HEAD)" = "${source_commit}"
test -z "$(git -C "${temporary_root}/source" status --porcelain)"
make -C "${temporary_root}/source" drat-trim

mkdir -p "${output_dir}"
install -m 0755 "${temporary_root}/source/drat-trim" "${output_dir}/drat-trim"
printf '%s\n' "${source_commit}" > "${output_dir}/SOURCE_COMMIT"
shasum -a 256 "${output_dir}/drat-trim" > "${output_dir}/drat-trim.sha256"
echo "DRAT_TRIM_BUILT ${output_dir}/drat-trim"
