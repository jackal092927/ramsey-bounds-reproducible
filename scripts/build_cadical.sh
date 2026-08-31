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

source_commit="c60730422e758ef1cebe7aeddf2dda31c996bf04"
temporary_root="$(mktemp -d)"
cleanup() {
  rm -rf "${temporary_root}"
}
trap cleanup EXIT

git clone --quiet https://github.com/arminbiere/cadical.git \
  "${temporary_root}/source"
git -C "${temporary_root}/source" checkout --quiet "${source_commit}"
test "$(git -C "${temporary_root}/source" rev-parse HEAD)" = "${source_commit}"
test -z "$(git -C "${temporary_root}/source" status --porcelain)"

(
  cd "${temporary_root}/source"
  ./configure
  make
)

mkdir -p "${output_dir}"
install -m 0755 "${temporary_root}/source/build/cadical" \
  "${output_dir}/cadical"
printf '%s\n' "${source_commit}" > "${output_dir}/SOURCE_COMMIT"
shasum -a 256 "${output_dir}/cadical" > "${output_dir}/cadical.sha256"
echo "CADICAL_BUILT ${output_dir}/cadical"
