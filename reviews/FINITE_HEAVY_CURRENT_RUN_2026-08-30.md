# Finite-heavy current-run record

Date: 2026-08-30  
Scope: local post-repair worktree and local release-asset overlay. This is a
successful integrated current run, not yet a clean-clone, CI, or published
release attestation.

## 1. Exact invocation and frozen identities

The successful invocation was:

```text
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir /private/tmp/ramsey-release-overlay-20260830.vd3pAk \
  --drat-trim /private/tmp/ramsey-release-toolchain-assets-20260830/drat-trim-2e3-macos-arm64
```

It ended with `FINITE_HEAVY_REPRODUCTION_PASS`. The files that define this
current-run protocol were:

| item | SHA-256 |
|---|---|
| `reproduce.py` | `84c07591b15fa03408e3ea8079ab6d671290bcd797776b9246cf90af448ec87e` |
| `artifacts/MANIFEST.tsv` | `57bde637c6c795f7655695079ce06a670c9f5490a0794198f99befa81235727c` |
| independent sequential-counter auditor | `38cc478cc75f1211cfe248645cd0929be306303e6998126750bc0cdd307ef4b0` |
| independent sequential-counter schema | `b66a3abc652dbadceb28f16cf635c7da23603ecfb75c45fb56df8dfcfa977baf` |
| singleton core-proof replay auditor | `5756000dfc8b5292b89ad617962927daf5d25471e12b530d9a7d29287ef5f73a` |
| PySAT-free singleton CNF auditor | `2dcc16137a0bd555a2553e9987968fda429e9098ec8c21affb05bfd5a5e03f3b` |
| common-model auditor | `ca83c3a3084cc37322592e3cdb283212ac8cf0ba35869f8ebc1262599a4fd39d` |

The runtime proof checker was the audited macOS arm64 `drat-trim` binary with
SHA-256
`31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
Its adjacent `SOURCE_COMMIT` contained
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985` plus one LF and had SHA-256
`f07dc9c72b2cd95961e4c41b5aaf707cadfb030b28040a55a0665615c618f50e`.

## 2. Authenticated asset inventory

Before any semantic or proof replay, the driver verified the exact name, byte
count, and SHA-256 of all **26** manifest entries. The inventory was:

| class | files | role |
|---|---:|---|
| six theorem CNFs and their six DRAT traces | 12 | three budget-five and three exact-six branch formulas |
| four singleton CNFs and their four DRAT traces | 8 | branch-1 consequences `K_a`, `K_b`, `K_c`, `K_d` |
| common CNF and complete SAT model | 2 | non-vacuity and exact-seven boundary audit |
| two audited `drat-trim` binaries, license, and source marker | 4 | replay toolchain and legal/source identity |
| **total** | **26** | exact manifest coverage |

The run performed **10 fresh DRAT replays**: six for the theorem formulas and
four for the singleton formulas. Every accepted replay exited zero and
contained the required standalone `s VERIFIED` line. No recorded historical
`proof_verified` bit was substituted for a fresh replay. This record does not
invent or carry forward per-proof timings that were not frozen as part of the
current-run output.

## 3. Formula and proof outcomes

| layer | formulas | independent semantic result | fresh DRAT result |
|---|---:|---|---|
| budget five, branches 0--2 | 3 | `VERIFIED` for all three | `VERIFIED` for all three |
| exact six, branches 0--2 | 3 | `VERIFIED` for all three | `VERIFIED` for all three |
| branch-1 singleton cores `K_a`--`K_d` | 4 | `VERIFIED` for all four | `VERIFIED` for all four |

The independent counter audit also reconstructed all six theorem-level
counter blocks without importing PySAT:

| branch family | branches | counter condition | clauses per counter | maximum variable |
|---|---:|---|---:|---:|
| budget five | 3 | at most four | 7,394 | 8,238 |
| exact six | 3 | exactly five | 16,420 | 13,160 |

The singleton replay was driven by the frozen summary with SHA-256
`8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a`
and status
`FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN`. It authenticated
and replayed exactly:

| label | edge assumed absent | DIMACS unit |
|---|---|---:|
| `K_a` | `(11,62)` | `-1085` |
| `K_b` | `(18,61)` | `-1672` |
| `K_c` | `(18,64)` | `-1675` |
| `K_d` | `(18,69)` | `-1680` |

These four UNSAT certificates establish four consequences of the frozen
branch-1 common relaxation. They do not establish minimality, close the whole
exact-seven search, or imply a global Ramsey bound.

## 4. Common-model non-vacuity audit

The integrated common-model auditor returned
`VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL`. Its authenticated identities
and direct checks were:

| quantity | current-run value |
|---|---|
| compressed common CNF SHA-256 | `39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365` |
| raw common CNF SHA-256 | `9602ef233f5fa95748ce4e7f997457d1bef47cd46453340bf5a44c2e163d3ec7` |
| compressed model SHA-256 | `9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d` |
| raw model SHA-256 | `51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e` |
| variables / clauses evaluated | `154,190 / 718,452` |
| all reconstructed clauses satisfied | `true` |
| four singleton probe variables true | `1085, 1672, 1675, 1680` |

The same complete model contains the independently checked 18-set

```text
{70,73,78,81,82,83,84,85,87,88,90,91,92,93,95,96,97,99}.
```

Therefore the common relaxation is nonempty, but this particular model is
**not** a valid 100-vertex `(3,18)` Ramsey graph. The SAT model is not an
exact-seven repair certificate and cannot support `R(3,18) >= 101`.

## 5. Exact-seven and theorem boundary

The final frozen-state auditor still found all three first-round exact-seven
branch records at `UNKNOWN_DISCOVERY_WALL_LIMIT`. No branch supplied an
accepted exact-seven SAT witness, and no branch supplied an UNSAT proof.
Consequently the integrated summary was:

```text
status: FINITE_THEOREM_REPRODUCED
budget5 formula semantics / DRAT: 3 / 3 VERIFIED
exact6 formula semantics / DRAT: 3 / 3 VERIFIED
branch1 singleton semantics / DRAT: 4 / 4 VERIFIED
branch1 common relaxation: VERIFIED_WITH_I18_WITNESS
exact7 record state: ALL_THREE_UNKNOWN_VERIFIED
fixed_seed_deletion_repair_radius_at_least_7: true
exact7_repair_exists: null
global_R_3_18_improvement: false
```

What this current run reproduces is the proof-carrying, fixed-seed local
barrier: under the paper's labelled seed and one-sided deletion metric, no
repair using at most six input-edge deletions exists. It also freshly checks
the four singleton consequences used to prune the branch-1 exact-seven
search.

It does **not** prove existence or nonexistence of an exact-seven repair, does
not prove that the local radius equals seven, does not construct a new
100-vertex Ramsey graph, and does not improve the global bound on
`R(3,18)`. The current run also does not by itself attest a public release,
anonymous clean-clone reproduction, CI execution, or cross-platform replay.
