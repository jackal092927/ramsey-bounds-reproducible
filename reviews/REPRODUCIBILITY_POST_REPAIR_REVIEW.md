# Reproducibility post-repair adversarial review

**Review date:** 2026-08-30  
**Snapshot:** local worktree based on commit `5e96a39`, including the
uncommitted post-review repairs visible at the time of this audit  
**Review mode:** read-only inspection plus lightweight/negative tests; the six
large DRAT replays were deliberately not repeated in this round

## Verdict

**THE FOUR MAJOR IMPLEMENTATION DEFECTS ARE SUBSTANTIALLY REPAIRED, BUT THE
PACKAGE IS STILL NOT A PUBLICATION-READY REPRODUCIBLE RELEASE.**

The finite replay now has a coherent tracked-metadata/release-asset overlay,
all four semantic auditors are wired into one proof-carrying command, and a
missing checker is a hard failure.  Stored provenance and work performed in
the current invocation are now separated.  The cross-platform binary-hash
contradiction is removed, and the lightweight upper command is no longer
called a complete theorem replay.

The decisive publication blocker is now external: there is still no accessible
GitHub repository or immutable release containing the twelve manifest assets.
The canonical generated sources have been rematerialized from the repaired
components and compiled into a 79-page PDF.  An independent temporary-tree
materialization produced the same 32 generated files byte for byte, the final
LaTeX log passed the unresolved-reference gate, and the compiled PDF contains
the pending-publication disclaimer and integrated `finite-heavy` protocol.

## Disposition summary

| finding | disposition | short reason |
|---|---|---|
| CRITICAL-1 | **OPEN** | no Git remote, intended GitHub URL is inaccessible, and no immutable twelve-asset release exists |
| MAJOR-1 | **CLOSED** | finite overlay and integrated replay are repaired, and the canonical generated manuscript now matches the source components |
| MAJOR-2 | **CLOSED** | `recorded_provenance` and `current_run` are separated, and no-checker `finite-heavy` exits nonzero |
| MAJOR-3 | **CLOSED** | checker binary hash is recorded rather than enforced; a pinned-source build helper succeeds |
| MAJOR-4 | **CLOSED** | lightweight upper replay is labelled as such, while `full` wires the complete rate chain and audits |
| MINOR-1 | **PARTIAL** | PR CI now checks quick reproduction and the paper, but no release-asset/finite-heavy job or release attestation exists |
| MINOR-2 | **CLOSED** | exact Python and `uv` are enforced consistently, and the unhashed pip fallback has been removed |
| MINOR-3 | **PARTIAL** | CI now compiles and scans the unified paper, but the TeX distribution is not exactly pinned and no release build hash/log is archived |
| MINOR-4 | **CLOSED** | an explicit networked `sources` tier exists, is documented separately from offline replay, and passed this audit |
| MINOR-5 | **PARTIAL** | CFF placeholder authorship is repaired, but licenses and third-party redistribution review remain pending |

## Finding-by-finding verification

### CRITICAL-1 — **OPEN**: public repository and release evidence are absent

`git remote -v` returned no remote.  An anonymous
`git ls-remote https://github.com/jackal092927/ramsey-bounds-reproducible.git
HEAD` failed with `Repository not found`.  The root README and `STATUS.md` now
state this honestly and no longer claim that the local package is already
publicly reproducible.  `CITATION.cff` names Cheng Xin rather than retaining
placeholder authorship.  These are important documentation repairs, but they
do not create the missing evidence source.

The local release gate is now strict: `scripts/verify_artifacts.py --exact`
rejects unmanifested names, and `scripts/download_release_artifacts.sh` refuses
to mix files into a nonempty download directory, compares the GitHub release
asset-name list exactly with `MANIFEST.tsv`, and then performs the strict
content check.  Positive and extra-file negative tests of `--exact` passed in
this audit.  These controls cannot verify a release that does not yet exist;
after publication, the real remote asset list and an anonymous clean clone
must still be checked.

**Required to close:** create and push the immutable repository snapshot;
publish a non-draft release containing exactly the twelve files and the
manifest; record the commit/tag/release identities; then reproduce from a
credential-free clean clone.  An archival DOI mirror remains strongly
recommended.

### MAJOR-1 — **CLOSED**: the overlay and canonical manuscript are synchronized

`reproduce.py` now implements the allowed overlay alternative from the first
review:

1. all twelve release payloads are verified by size and SHA-256;
2. tracked certificates, JSON metadata, cut banks, and the complete-referee
   record are linked into a fresh temporary tree;
3. the budget-five checker and all three exact-budget-six branch checkers run
   against that tree with the requested checker; and
4. the exact-seven state audit runs before the theorem-level success record is
   emitted.

A temporary-overlay audit checked 25 proof/metadata paths and found no missing
entry.  Thus the former incompatible-directory model is repaired without
copying large files into tracked locations.

The canonical outputs have now been regenerated after the source-component
repairs.  A fresh temporary materialization produced 32 files whose SHA-256
mapping exactly equalled the current generated files, with no mismatch.  The
materializer also preserves explicit source equation labels while namespacing
them: spot checks such as `eq:correlation-definition`, `eq:rate-bound`,
`eq:descent-X`, and `eq:mu-w` became the corresponding `up:`/`low:` labels
beside their qualified visible tags.  The
generated finite section states that public GitHub and archival release
publication remain pending, documents `verify_artifacts.py --exact`, and uses
the integrated `finite-heavy` command.  The generated bibliography describes a
local pre-publication package and contains no premature repository URL.

The resulting PDF is 79 pages and was created after the synchronized generated
sources.  Text extraction confirmed that the PDF contains the same
pending-publication disclaimer and integrated finite replay instructions.
`scripts/check_latex_log.py` passed on this final build.  Direct log inspection
also found no overfull boxes, undefined or multiply defined references, LaTeX
warnings, LaTeX errors, or fatal errors.  Its SHA-256 in the reviewed worktree
is `8ed2aec0a38278dd81bc669eda36dd15c8f86324a65c6ebf3af271d33e1c7d1a`.
This digest incorporates the final wording update recording completion of the
post-repair upper adversarial replay; no mathematical formula or certificate
changed in that update.

### MAJOR-2 — **CLOSED**: historical provenance is no longer reported as current replay

All four finite auditors now use distinct `recorded_provenance` and
`current_run` namespaces.  The theorem-bearing booleans in the budget-five and
branch-0 outputs are derived from current proof replay rather than copied from
stored records.  Branches 1 and 2 likewise report `NOT_REQUESTED` when no
checker is supplied.

Two executed negative/semantic tests confirmed the behavior:

- `reproduce.py finite-heavy --artifact-dir routes/finite` without
  `--drat-trim` verified the twelve compressed identities and then exited 1
  with an explicit checker requirement; it did not emit a theorem-reproduced
  status.
- the budget-five auditor without a checker emitted
  `ALL_THREE_BRANCHES_SEMANTICS_VERIFIED_PROOFS_NOT_REQUESTED`, with historical
  UNSAT under `recorded_provenance` but
  `current_run.fixed_seed_budget5_repair_ball_unsat = false`;
- the branch-2 auditor without a checker emitted
  `BRANCH2_EXACT_BUDGET6_SEMANTICS_VERIFIED_PROOF_NOT_REQUESTED`, with
  `current_run.proof_status = NOT_REQUESTED`.

Static inspection confirmed the same non-replay treatment in branch 0 and
branch 1.  A theorem-level `FINITE_THEOREM_REPRODUCED` record is reached only
after all four checker processes, each supplied with `--drat-trim`, return
success, followed by the exact-seven state audit.

### MAJOR-3 — **CLOSED**: portable checker policy is internally consistent

The branch-0 and branch-1 auditors no longer reject a checker whose executable
SHA-256 differs from the historical binary.  They require an executable,
require exit code zero plus `s VERIFIED`, record the current executable hash,
and separately report whether it matches the historical hash.  The integrated
entry point follows the same policy.

`scripts/build_drat_trim.sh` cloned the official source into a new temporary
directory, checked out source commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, verified `HEAD` and a clean tree,
built the executable, wrote `SOURCE_COMMIT`, and recorded the executable hash.
The locally rebuilt checker was executable and displayed the expected usage
message.  This round did not repeat proof replay on multiple operating systems;
that remains a release/CI validation task, not a remaining exact-binary
acceptance bug.

### MAJOR-4 — **CLOSED**: lightweight and complete upper commands are distinct

`scripts/reproduce_upper.sh` still runs the four final exact-diagonal/transfer
checkers, but now ends with `UPPER_TRANSFER_CERTIFICATE_REPRODUCED`.  The upper
paper explicitly calls this a lightweight replay and says that it omits the
six-stage rate chain.

`reproduce.py full` runs the quick checks, `verify_chain_arb.py` over all six
linked certificates, both direct Ramsey-region orientations for every stage,
the combinatorial audit, and the complete lower replay.  Because the runner
uses `check=True`, any required subcheck prevents the final
`FULL_REPRODUCTION_PASS`.  The expensive full interval chain was not repeated
in this second-round audit; the correction being accepted here is the command
wiring and removal of the earlier overclaim.

### MINOR-1 — **PARTIAL**: CI coverage improved but does not enforce the release artifact

The push/PR workflow now uses exact Python 3.11.15 with pinned `uv`, runs
`reproduce.py quick`, compiles Python sources, builds the single canonical
paper on Ubuntu 24.04, and rejects unresolved citations/references.  A manual
workflow runs the full upper/lower tier and the networked source tier.

Still absent are: a job that enumerates and verifies the release assets, a
semantic smoke test using the release directory, a separately triggered
finite-heavy DRAT job, a release-tag trigger, and an archived attestation that
binds logs to the Git commit, asset hashes, checker source commit, and PDF.

### MINOR-2 — **CLOSED**: one exact interpreter and lockfile contract is enforced

Python 3.11.15 is now enforced consistently by `.python-version`,
`pyproject.toml`, `scripts/verify_repository.py`, both workflows, and the
bootstrap guard.  CI pins `uv==0.10.2`, and `scripts/bootstrap.sh` now requires
that exact `uv` version and fails closed when it is unavailable; there is no
pip or `requirements-repro.txt` installation path.  Installation is uniformly
`uv sync --frozen --no-dev`, and `uv lock --check` passed.

### MINOR-3 — **PARTIAL**: clean paper CI exists, but the TeX toolchain is not archival

The new paper job provisions LaTeX packages, runs `make paper`, and invokes
`scripts/check_latex_log.py`; workflow YAML parsed successfully.  The final
79-page local build log passed the unresolved-reference scanner and contains
no overfull-box, undefined-reference, multiply-defined-reference, LaTeX
warning, error, or fatal-error diagnostic.

The workflow obtains TeX packages from the current Ubuntu apt repositories
rather than pinning a TeX Live image/year and package snapshot.  It also does
not archive the build log, generated PDF, toolchain inventory, or PDF SHA-256.

### MINOR-4 — **CLOSED**: external-source identity is an explicit networked tier

`reproduce.py sources` is separate from the offline `full` tier and verifies
the three pinned arXiv TeX members plus five graph matrices in temporary
storage.  The README and unified reproducibility section state the networked
scope explicitly, and the manual full-verification workflow invokes the tier.
The command passed in this audit with all eight hashes matching.

### MINOR-5 — **PARTIAL**: citation placeholder fixed; release rights remain unresolved

`CITATION.cff` now has a specific title, scoped abstract, keywords, and Cheng
Xin authorship, without inventing a DOI or public release version.  `LICENSE.md`
honestly states that the current pre-publication package grants no public reuse
license.

That honesty is appropriate for the local workspace but is not a finished
public release state.  Software and manuscript licenses still require author
approval, and redistribution rights for all third-party matrices/source
members must be documented before release.

## Unified-manuscript and README check

The repository-level architecture now clearly has one publication output:
`papers/unified/main.tex` contains all three result parts and one unified
reproducibility section; `papers/upper`, `papers/lower`, and `papers/finite`
are described as source/provenance components.  The root README, paper README,
Makefile, and compilation script agree that `make paper` is canonical and that
`make papers` is only an alias.

The final generated manuscript is synchronized with all 32 materialized files,
and the compiled PDF contains the corrected finite reproducibility section.

## Checks performed in this round

| check | observed outcome |
|---|---|
| `.venv/bin/python reproduce.py quick` | **PASS**, including 13 frozen-file integrity checks, four upper transfer checks, current lower arithmetic check, 28 finite unit tests, exact-seven state audit, and five graph certificates |
| `reproduce.py finite-heavy` without checker | **expected FAIL**, exit 1 after twelve artifact hashes; no theorem-reproduced status |
| budget-five semantic auditor without checker | **PASS**, semantics verified and current proof status `NOT_REQUESTED` |
| branch-2 semantic auditor without checker | **PASS**, semantics verified and current proof status `NOT_REQUESTED` |
| temporary finite overlay audit | **PASS**, 25 required tracked/payload paths present |
| `scripts/build_drat_trim.sh` into a fresh temporary directory | **PASS**, pinned source commit and executable recorded |
| `.venv/bin/python reproduce.py sources` | **PASS**, three arXiv members and five graph matrices matched |
| `uv lock --check` | **PASS** |
| shell syntax, Python byte compilation, and workflow YAML parse | **PASS** |
| `scripts/verify_artifacts.py --exact` on exactly the twelve manifest files | **PASS**, `EXACT_ARTIFACT_MANIFEST_VERIFIED` |
| strict asset check against a directory containing extra names | **expected FAIL**, exit 1 with `UNEXPECTED` entries |
| final 79-page LaTeX log and `scripts/check_latex_log.py` | **PASS**, no overfull, undefined, multiply-defined, warning, error, or fatal diagnostic |
| fresh temporary materialization compared with the canonical tree | **PASS**, all 32 generated files matched byte for byte |
| explicit equation-label spot checks after materialization | **PASS**, qualified tags retained the intended namespaced source labels |
| text extraction from `papers/unified/main.pdf` | **PASS**, pending-publication and integrated `finite-heavy` language present |

Not rerun here: the complete upper interval chain, the branch-0/branch-1
multi-gigabyte proof scans, the six DRAT replays, GitHub Actions on hosted
Ubuntu, or an anonymous clean clone.  The first-round review's fresh large
proof results were not relabelled as current work in this review.

## Remaining release gate

The package should not move from `LOCAL PRE-PUBLICATION` to a public
reproducible release until all of the following hold:

1. create the GitHub repository and freeze the reviewed commit;
2. publish exactly the twelve manifest assets in an immutable release;
3. add release/finite-heavy CI and archive commit-bound logs, including the
   current PDF hash;
4. choose licenses and document third-party redistribution rights; and
5. repeat bootstrap, sources, full, finite-heavy, and paper compilation from
   an anonymous clean clone.
