# Final release preflight

**Date:** 2026-08-30  
**Scope:** repository-wide claim consistency, deterministic paper build,
machine-readable status, GitHub Actions supply chain, and the proposed
immutable evidence Release

## Executive status

The mathematical claim surfaces are mutually consistent: Part I remains
conditional/source-relative, Part II remains conditional on S1--S5 with S3 an
extra hypothesis, and Part III proves only a fixed-seed one-sided deletion
radius lower bound of seven. Exact seven remains UNKNOWN and no
(R(3,18)ge101) claim is made.

The final release implementation audit reached **0 blocker / 0 major /
0 minor** after the repairs below. This is a verdict on the implementation and
publication protocol, not a statement that the tag or Release already exists.
The final PDF hash, ChatGPT Pro disposition, hosted final-commit checks,
publication, attestation, and credential-free replay remain separate gates
until their completion is recorded.

## Findings and disposition

### P1. Machine-readable exact-seven overstatement — repaired

The historical aggregate file used the key
`minimum_deletions_for_any_completion_in_fixed_seed_ball: 7`. Read
literally, that field asserted the unknown equality rather than the proved
lower bound. It now reads
`one_sided_deletion_radius_lower_bound_in_fixed_seed_ball: 7`, while the
separate exact-seven field continues to say that existence has not been
established.

### P2. Hosted-action pin did not denote a commit — repaired

The original `astral-sh/setup-uv` identity denoted the immutable annotated
tag object for v7. Although content-addressed, it did not justify the literal
statement that every action was commit-pinned. All three workflows now use
the peeled commit
`37802adc94f370d6bfd71619e3f0bf239e1f3b78`. Checkout, Python setup,
and artifact upload were already fixed by full commit identities.

### P3. Annotated-tag property was procedural only — repaired

The release workflow already bound both the raw tag-object SHA and the peeled
commit, but it did not reject a lightweight tag. It now additionally requires
`git cat-file -t refs/tags/$TAG` to return `tag`.

### P4. Prospective release metadata could be read as current state — repaired

The authoritative README and STATUS already said that the Release was
pending. The citation message and Release-note source now explicitly state
that their tagged-release fields become current-state assertions only after
the advertised URL resolves to a published, non-prerelease, immutable Release
with the exact manifest set. The final publication report must be based on
live GitHub state, not the presence of these prospective files.

### P5. Stale candidate PDF hash — repaired for the current freeze point

Four status documents retained the previous candidate hash. After two clean
builds produced identical bytes, those current-status occurrences were
updated atomically to
`bad787b9a37430d39d17d789c9dddc39db212db2db0954fa668dd43c96993804`.
They must be checked again if a later review changes any manuscript source.
Historical review snapshots whose text explicitly identifies an earlier
worktree are not rewritten.

### P6. Review/status index drift — repaired

The final theorem-specific adversarial review is now indexed from the README,
STATUS, PAPER_PLAN, NARRATIVE_REPORT, and consolidated disposition. The plan
also recognizes that the public GitHub repository already exists, and the
artifact README calls the absent Release tag planned rather than current.

## Supply-chain invariants checked

The audited release workflow:

1. checks out the exact annotated tag and requires HEAD to equal its peeled
   commit;
2. requires the GitHub Release to be published, non-prerelease, and immutable;
3. verifies GitHub's signed release attestation against the repository, tag,
   raw annotated-tag object, and the complete manifest digest map;
4. downloads with no Authorization header and rejects any missing, extra,
   renamed, incomplete, size-mismatched, or digest-mismatched asset;
5. builds `drat-trim` from the fixed source commit;
6. binds every downloaded file to the release attestation; and
7. reconstructs all six formulas and replays all six DRAT proofs through the
   finite-heavy entry point.

The manifest contains exactly 12 rows totalling 1,342,246,254 bytes. Every
local file's name, byte count, and SHA-256 matched at preflight.

## Local preflight results

The current post-repair tree passed:

- repository integrity and `git diff --check`;
- Python compilation, JSON parsing, shell syntax, and all workflow YAML
  parsing;
- official CFF 1.2.0 schema validation;
- deterministic unified-source materialization;
- the quick tier, including four independent 512-bit upper transfers,
  lower arithmetic checks, 28 finite-route unit tests, and lightweight graph
  certificates; and
- the full tier, including the six-stage interval chain, six independent
  two-sided region replays, upper regression audits, and the complete lower
  arithmetic-certificate suite.

The full command ended with `FULL_REPRODUCTION_PASS`. The finite-heavy
current-run replay had already passed against the same twelve local artifact
bytes; the decisive public replay remains the credential-free post-release
run.

## Safe publication order

1. Close the independent ChatGPT Pro review and disposition every concrete
   objection.
2. Materialize the unified source, clean-build twice, require byte identity,
   and update every current-status hash.
3. Push the final commit and require fast and full hosted verification on that
   exact commit.
4. Create and push the annotated evidence tag, then verify its raw object and
   peeled commit.
5. Create a draft Release with `--verify-tag`; upload the twelve explicit
   manifest paths without globbing, replacement, or clobbering.
6. Validate the draft's exact names, states, sizes, and digests; publish once.
7. Verify immutability, signed release attestation, and each asset binding.
8. Clone without author credentials, download through public endpoints, build
   the pinned checker, and require finite-heavy to pass.
9. Only then write the post-release verification report on the default branch.

No tag or asset may be moved or replaced after immutable publication.
