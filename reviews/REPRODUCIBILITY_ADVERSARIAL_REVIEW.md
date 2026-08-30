# Adversarial reproducibility review

**Repository snapshot reviewed:** local commit `5e96a39` (`main`)  
**Review date:** 2026-08-30  
**Role:** independent clean-reproduction auditor  
**Scope:** `README.md`, `STATUS.md`, `CITATION.cff`, `Makefile`,
`reproduce.py`, `pyproject.toml`, lock/requirements files, `scripts/`,
`artifacts/MANIFEST.tsv`, the two GitHub Actions workflows, the three
manuscripts, and the proof/test/certificate entry points used by them.

## Verdict

**REJECT AS A PUBLICATION-READY REPRODUCIBILITY ARTIFACT, PENDING THE
CRITICAL AND MAJOR REPAIRS BELOW.**

This is not a rejection of the three mathematical claims.  On the author's
existing machine, the quick upper/lower/finite checks, the complete lower
arithmetic suite, all 28 finite unit tests, the five graph certificates, the
three pinned external TeX members, the five upstream graph downloads, and all
12 locally present compressed SAT artifacts passed the checks run in this
review.  The problem is narrower and still decisive: a clean independent
clone cannot currently follow one coherent, public, portable path from the
advertised release assets to all four finite-proof outcomes required by the
finite manuscript.  Several status fields also say that a proof was verified
when the proof was explicitly **not rerun**.  Finally, the command called the
complete upper replay omits the six-stage rate certificate on which the upper
theorem depends.

The artifact is suitable for another internal review round after the fixes.
It should not yet be described as a publicly reproducible archival release.

## Severity convention

- **CRITICAL:** blocks independent access to proof-carrying evidence or permits
  a false publication-level reproducibility claim.
- **MAJOR:** an advertised command does not establish its stated evidence
  level, or a clean-clone path is broken.
- **MINOR:** does not invalidate the current local computations, but weakens
  portability, CI enforcement, or long-term reconstruction.

## Findings

### CRITICAL-1 — The cited repository/release is not an independently accessible evidence source

The local clone has no configured Git remote.  At review time, anonymous HTTPS
access to both
`https://github.com/jackal092927/ramsey-bounds-reproducible` and the advertised
`evidence-2026-08-12` release URL returned HTTP 404.  A private repository may
exist, but that does not satisfy the finite manuscript's statement that the
repository is public or allow an independent reader to download the 12
proof-carrying assets.  There is also an internal contradiction:

- `papers/finite/sections/07_reproducibility.tex` calls it a **public
  repository**;
- `scripts/download_release_artifacts.sh` calls the default target a **private
  publication repository**;
- `papers/finite/references.bib` cites the currently inaccessible URL; and
- `CITATION.cff` still contains placeholder authorship.

The six DRAT files are not tracked by Git and are essential to the radius-at-
least-seven proof.  Consequently, the advertised public evidence chain stops
before proof replay.

**Minimum repair.** Create and push an immutable repository snapshot; choose
and document its visibility; create a non-draft release at the pinned tag;
upload exactly the 12 manifest entries; publish `MANIFEST.tsv` with the
release; and record the repository commit and release URL in the unified
paper.  For durable scholarly access, mirror the release to an archival DOI
service.  Replace the CFF placeholder before release.  If the repository must
remain private during review, the paper and README must say so and must not
claim public reproducibility.

**Verification after repair.** From a machine with no pre-existing clone and,
for a public release, no repository-specific credentials:

```bash
git clone https://github.com/jackal092927/ramsey-bounds-reproducible.git
cd ramsey-bounds-reproducible
git remote -v
git rev-parse HEAD
bash scripts/bootstrap.sh
bash scripts/download_release_artifacts.sh
.venv/bin/python scripts/verify_artifacts.py \
  --directory artifacts/downloads
```

The release asset list must equal the 12 manifest names, not merely contain a
subset with matching names.

### MAJOR-1 — Downloaded assets and semantic checkers use incompatible directory models

`scripts/download_release_artifacts.sh` downloads only the 12 CNF/DRAT files
to `artifacts/downloads/`.  The exact-six semantic checkers accept one
`--artifact-dir`, but then expect **both** the downloaded payloads and tracked
supporting files in that same directory.  For example,
`routes/finite/check_r3_18_budget6.py:134-139` expects the seed under
`certificates/`, the branch result JSON, and the budget-five audit JSON beside
the CNF/DRAT files.  The branch-0 and branch-1 checkers similarly require cut
banks and proof records that are tracked under `routes/finite/`, not shipped
as release assets.

This was reproduced with a directory containing precisely the 12 manifest
assets: branch 2 exited with `FileNotFoundError` for
`r3_18_budget6_branch_2.json`.  Meanwhile,
`reproduce.py:106-141` verifies compressed hashes and invokes `drat-trim`, but
never calls the formula-semantic reconstruction routines.  Therefore the
documented clean path cannot jointly establish the finite manuscript's four
required outcomes: identity, semantics, proof replay, and exact-seven status.

**Minimum repair.** Separate the path arguments:

- keep tracked metadata, seeds, cut banks, and result records under a
  `--metadata-dir` defaulting to `routes/finite`; and
- read only CNF/DRAT payloads from an `--artifact-dir` defaulting to
  `artifacts/downloads`.

Then make one top-level finite command execute, in order: manifest verification,
budget-five semantic reconstruction, exact-six semantic reconstruction for all
three branches, all six DRAT replays, and the exact-seven state audit.  An
alternative is a verified materialization step that symlinks/copies only the
12 hash-checked assets into the ignored `routes/finite/` locations, but the
two-directory interface is less error-prone.

**Verification after repair.** Run the following from a clean clone where
`routes/finite/*.cnf.gz` and `routes/finite/*.drat.gz` do not exist:

```bash
test -z "$(find routes/finite -maxdepth 1 \
  \( -name '*.cnf.gz' -o -name '*.drat.gz' \) -print -quit)"
bash scripts/download_release_artifacts.sh
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir artifacts/downloads \
  --drat-trim /absolute/path/to/drat-trim
```

The final machine-readable report should contain separate `VERIFIED` fields
for all six formula semantics and all six DRAT replays.

### MAJOR-2 — Machine-readable statuses conflate stored provenance with a replay performed now

The finite paper correctly requires four distinct outcomes and says that hash
checks or unit tests alone do not reproduce the theorem.  The checkers violate
that rule:

- `routes/finite/check_r3_18_extension_repair.py:199-209` sets every proof to
  `NOT_RERUN` when no checker is supplied, yet lines 218-220 emit
  `status: ALL_THREE_BRANCHES_VERIFIED` and the UNSAT conclusion.
- `routes/finite/check_r3_18_budget6.py:153-162` sets
  `proof.status: NOT_RERUN`, yet unconditionally emits
  `BRANCH2_EXACT_BUDGET6_PROOF_VERIFIED`.
- `routes/finite/check_r3_18_budget6_branch0_union.py:208-212` distinguishes
  `ARTIFACT_VERIFIED_NOT_REPLAYED`, but lines 257-263 still emit
  `all_three_exact_budget6_branches_proof_verified: true` and the radius
  conclusion even when no proof was replayed in this invocation.
- `reproduce.py finite-heavy` called without `--drat-trim` prints that replay
  was skipped but exits with status 0.

The branch-2 behavior was observed directly: semantic reconstruction passed,
`proof.status` was `NOT_RERUN`, and the top-level status still said
`PROOF_VERIFIED`.  The no-checker heavy tier likewise returned exit code 0.
These are evidence-state errors even if the historical stored records are
honest.

**Minimum repair.** Use two explicit namespaces in every JSON result:

```text
recorded_provenance.proof_status = VERIFIED_IN_PINNED_RECORD
current_run.proof_status = NOT_REQUESTED | VERIFIED | FAILED | TIMEOUT
```

Derive the top-level `current_run.status` only from work performed in the
current invocation.  A theorem-level `REPRODUCED` status must require all
semantic and DRAT statuses to be `VERIFIED`.  Make `finite-heavy` require
`--drat-trim`; otherwise exit nonzero, or rename the no-checker mode to an
explicit `finite-assets-only` tier.

**Verification after repair.** These two tests must differ:

```bash
set +e
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir artifacts/downloads
test "$?" -ne 0
set -e

.venv/bin/python routes/finite/check_r3_18_budget6.py \
  --metadata-dir routes/finite \
  --artifact-dir artifacts/downloads \
  | tee /tmp/branch2-without-replay.json
python - <<'PY'
import json
p = json.load(open('/tmp/branch2-without-replay.json'))
assert p['current_run']['proof_status'] == 'NOT_REQUESTED'
assert 'PROOF_VERIFIED' not in p['current_run']['status']
PY
```

### MAJOR-3 — The portable-checker policy contradicts the integrated checkers

`README.md:49-51` says that compiled `drat-trim` hashes are provenance, not a
portability requirement.  The finite verification protocol tells a reviewer
to compile the pinned source commit.  Nevertheless,
`check_r3_18_budget6_branch1.py:265-268` and
`check_r3_18_budget6_branch0_union.py:211-212` reject any checker binary whose
SHA-256 is not the exact historical executable hash.  A fresh Linux or macOS
build from the correct commit is not expected to reproduce another machine's
binary hash, so the manuscript's integrated commands are non-portable by
construction.  Branch 2 and `reproduce.py finite-heavy` follow a different,
portable policy, producing inconsistent trust rules across branches.

**Minimum repair.** Require an executable checker and record its binary hash,
but do not require equality with the historical binary.  Instead provide a
small build script that clones the official repository, checks out
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, verifies `HEAD` and a clean source
tree, and builds the checker.  Keep the historical binary hash in provenance
only.  If exact-binary replay is desired as an additional mode, publish the
binary per platform and label that mode separately.

**Verification after repair.** On at least Ubuntu and macOS, build independently
from the pinned source commit and run the same exact-six branch with both
binaries.  Both runs must accept; their checker hashes may differ; both must
end with exit code zero and `s VERIFIED`.

### MAJOR-4 — The command called the complete upper replay omits the rate-certificate proof

`papers/upper/sections/06_computation.tex:41-50` calls
`bash scripts/reproduce_upper.sh` the complete local theorem replay.
`scripts/reproduce_upper.sh:8-11`, however, runs only the four current
exact-diagonal/outer-transfer checkers.  The outer checker reads the stage-six
target polynomial, but this command does not run `verify_chain_arb.py`, the six
direct two-sided region replays, or `audit_tests.py`.  Those checks are deferred
to `reproduce.py full`.

Thus the paper's advertised complete command proves the final transfer
conditional on an unverified rate input in that invocation.  The script then
prints `UPPER_THEOREM_REPRODUCED`, which overstates the completed evidence.

**Minimum repair.** Either change the manuscript's complete command to
`.venv/bin/python reproduce.py full`, or add a dedicated `upper-full` tier that
runs the six-stage chain, direct region checks, combinatorial audit, and all
four final checkers.  Rename the present lightweight output to
`UPPER_TRANSFER_CERTIFICATE_REPRODUCED` if it is retained.

**Verification after repair.** A complete upper log must contain all of:

```text
PASS: verified 6-stage Ramsey-rate certificate chain
PASS: independent direct two-sided Ramsey-region replay
PASS: 512-bit exact-diagonal inner certificate
PASS: independent adaptive 512-bit exact-diagonal referee replay
```

and must exit nonzero if any required certificate JSON is removed or changed.

### MINOR-1 — CI enforces only a subset of the publication artifact

The push/PR workflow runs `reproduce.py quick` and byte-compiles Python.  The
full upper/lower replay is manual only; no workflow downloads or even
availability-checks the release artifacts; no workflow performs finite
semantic reconstruction from the release directory; and no workflow compiles
the manuscripts.  Consequently, a PR can break the paper, the release path,
or the full certificate chain while fast CI remains green.  There is also no
checked-in CI run attestation tied to the release commit.

**Minimum repair.** Add jobs for (i) clean LaTeX compilation, (ii) exact
interpreter/dependency setup from `uv.lock`, (iii) full upper/lower verification
on manual dispatch and release, and (iv) release-asset manifest plus semantic
smoke checks.  The multi-gigabyte DRAT replay can remain a separately triggered
job, but its immutable log and commit/release identities should be archived.

**Verification after repair.** Require all non-heavy jobs on pull requests;
run the heavy job on the release tag; download the resulting logs and verify
that they name the same Git commit, asset hashes, and checker source commit as
the paper.

### MINOR-2 — Interpreter and dependency promises are not enforced consistently

The README, `.python-version`, `pyproject.toml`, and `uv.lock` identify Python
3.11.15, but `scripts/verify_repository.py` accepts any Python 3.11 patch
release, the CI asks for floating `3.11`, and the no-`uv` bootstrap fallback
uses whatever `python3` is first on `PATH`.  The pip fallback pins versions but
not distribution hashes.  Conversely, `pyproject.toml` requires exactly
3.11.15, so the `uv` and pip paths do not implement the same contract.

**Minimum repair.** Decide whether 3.11.15 is exact or merely the reference.
If exact, enforce `(3, 11, 15)` everywhere and request `3.11.15` in CI.  If
patch portability is intended, loosen `requires-python` and say which patch
versions were tested.  Prefer the lockfile path in CI and document the pinned
`uv` version; if pip remains supported, use a hash-locked export.

### MINOR-3 — The LaTeX toolchain is neither pinned nor tested cleanly in CI

`make papers` assumes a system `latexmk`, TeX distribution, and bibliography
tooling.  Neither the bootstrap script nor CI provisions or versions them.
The local command passed in this review only because pre-existing TeX Live
2022 outputs were already up to date; that is not a clean-clone test.

**Minimum repair.** Pin a TeX Live year/container, compile from a clean build
directory in CI, fail on undefined references/citations, and state whether PDF
bit-for-bit identity is promised.  At minimum, archive the successful clean
build log and generated PDF hash for the release commit.

### MINOR-4 — `full` does not check the pinned external-source or graph-source manifests

The two fetchers are functional and passed in this review, but neither is part
of `reproduce.py full`.  A reader can reproduce the local computations while
never checking that the imported Yang--Mao/HMS/Lin--Niu source members or the
five graph matrices still match their pinned upstream commits.

**Minimum repair.** Add an explicit networked `sources` tier and invoke it in
release CI, or clearly separate `full-offline` from `full-with-sources`.  Do not
make ordinary offline proof replay silently depend on network availability.

### MINOR-5 — Release engineering metadata is still provisional

`CITATION.cff` asks the releaser to replace placeholder authorship, and
`LICENSE.md` says no public reuse license has been selected.  Those are honest
pre-submission markers, but they are incompatible with presenting the current
snapshot as a finished public research software release.  Third-party matrix
redistribution terms should also be checked before publication.

**Minimum repair.** Replace placeholder citation metadata, choose explicit
software/manuscript licenses with author approval, retain third-party
provenance, and validate `CITATION.cff` before the GitHub release.

## Checks performed and observed outcomes

The following were run without modifying proof code or certificate data:

| check | observed outcome |
|---|---|
| `.venv/bin/python reproduce.py quick` | PASS; 49.84 s; four current upper checks, final lower checker, 28 tests, five graph certificates |
| `bash scripts/reproduce_lower.sh` | PASS; 25.29 s; all four lower arithmetic checkers |
| `scripts/fetch_external_sources.py` | PASS; three selected TeX-member hashes matched |
| `routes/finite/fetch_certificates.py --output-dir <temp>` | PASS; five files matched pinned commits/hashes |
| `scripts/verify_artifacts.py --directory routes/finite` | PASS; all 12 **locally present ignored** assets matched `MANIFEST.tsv` |
| branch-2 semantic checker without `drat-trim` | semantic PASS; proof `NOT_RERUN`; misleading top-level `PROOF_VERIFIED` observed |
| `reproduce.py finite-heavy --artifact-dir routes/finite` without checker | artifact hashes PASS; replay skipped; exit code 0 |
| semantic checker against a directory containing only the 12 release assets | FAIL; required tracked JSON/seed metadata absent |
| `uv lock --check` and repository integrity checker | PASS |
| Python byte compilation and `git diff --check` | PASS |
| `make papers` | PASS only as an up-to-date local build; not a clean toolchain reconstruction |

The six-stage interval chain was not rerun in this audit because the quick
review deliberately avoided duplicating the repository's heaviest interval
work.  The six multi-gigabyte DRAT proofs were not replayed because no locally
installed pinned-source checker was available.  Their compressed identities
were checked, not their proof semantics.  These non-actions are intentionally
reported as `NOT_RERUN`, not as successful reproduction.

## Resolution gate

Before changing the verdict, an independent reviewer should receive a **fresh
clone** at a stated commit and be able to do all of the following without any
untracked author-machine files:

1. build the exact Python environment and the pinned-source DRAT checker;
2. fetch and hash-check the public immutable release assets;
3. run the complete upper chain and final transfer;
4. run the complete lower arithmetic suite;
5. reconstruct all six finite CNFs against the tracked mathematical metadata;
6. replay all six DRAT refutations and obtain `s VERIFIED`;
7. observe exact-seven as `UNKNOWN`, not as a theorem; and
8. compile the single unified manuscript from a clean TeX environment.

Only then should the package emit a top-level status equivalent to
`FULL_REPRODUCTION_PASS`.
