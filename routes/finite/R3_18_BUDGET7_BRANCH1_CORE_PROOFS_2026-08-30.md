# Proof-carrying branch-1 singleton consequences

Date: 2026-08-30  
Scope: exact-seven branch fixing `(97,99)` absent  
Status: **FOUR SINGLETON NO-GOODS PROOF-VERIFIED; COMMON RELAXATION SAT; EXACT SEVEN UNKNOWN**

## Checked result and exact boundary

Let `Psi_1` be the frozen branch-1 common CNF relaxation below, and let
`x_uv=1` mean that edge `(u,v)` is present in the final graph. Four standalone
CaDiCaL runs, each followed by pinned `drat-trim`, prove

```text
Psi_1 entails x_11,62 and x_18,61 and x_18,64 and x_18,69.
```

Equivalently, each of the following formulas has a checked DRAT refutation:

```text
Psi_1 and not x_11,62
Psi_1 and not x_18,61
Psi_1 and not x_18,64
Psi_1 and not x_18,69
```

Every feasible branch-1 exact-seven repair satisfies `Psi_1`; therefore a
feasible residual six-deletion support must preserve all four named seed
edges. The implication is deliberately one-way because the stored
independent-18 bank is universally valid but incomplete.

A separately checked complete model proves that `Psi_1` is satisfiable, so
the entailments are not vacuous. That model contains an explicit independent
18-set and is not a Ramsey repair. Consequently this record:

- does not close branch 1;
- does not decide whether an exact-seven repair exists;
- does not determine the exact repair radius;
- does not construct a 100-vertex `(3,18)`-Ramsey graph; and
- does not imply `R(3,18)>=101`.

No minimality claim is made. The earlier four pair no-goods remain valid but
are strictly dominated by these singleton consequences; they are omitted from
the final release antichain and its exact asset namespace.

## Frozen common relaxation

The common formula fingerprint is

```text
a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2
```

Its 718,452 clauses, before a candidate unit, are ordered as follows:

1. 161,700 triangle clauses on all 100 labelled vertices;
2. 19,680 sequential-counter clauses imposing exactly six deletions among the
   826 residual seed edges;
3. the unit fixing `(97,99)` absent;
4. 285,300 sequential degree-at-most-17 clauses;
5. 251,771 ordered universal independent-18 hitting clauses.

There are 154,190 variables. Original seed nonedges are free primary
variables and none enters the deletion counter. No learned core clause is
installed. Each singleton formula has 718,453 clauses and 180,104,608 raw
DIMACS bytes.

## Strongest proof antichain

The exporter snapshot is Git commit `408e3bb`, with script SHA-256

```text
5e05f75affc5c6c5323fb2f1bddd3097c7a851c00330fd558f1f731e978936cf
```

The final machine summary is
`routes/finite/r3_18_budget7_branch1_core_proof_summary.json`, SHA-256

```text
8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a
```

| label | assumed deleted edge | unit | candidate SHA-256 | CNF gzip bytes | CNF gzip SHA-256 | DRAT gzip bytes | DRAT gzip SHA-256 |
|---|---|---:|---|---:|---|---:|---|
| `K_a` | `(11,62)` | `-1085` | `31640894cc90a10322b2024b3f4b99e3bad2a77478597d8953be84333bdec219` | 18,914,252 | `1ec7a15b9afd7c7c0944bbc663db2522b47d6f4f12fe98f23501d1006fabe411` | 707,650,273 | `c71be4804965a66e2783c61ae4711e1dc5faeb13a42ecab50672dd0efdd8818c` |
| `K_b` | `(18,61)` | `-1672` | `ac239cde61113e19d8f6014b88b3815f4ce9028631c7e0280d589812e5f3b709` | 18,914,251 | `1df74150cf9678e977364d4df782e179d62dff811b940d9fc0ea35c30cda845b` | 855,530,402 | `c34b97f66e3513c8261e1424f66b9e2299a49b9f38a6d953ade17e6c4e266bfa` |
| `K_c` | `(18,64)` | `-1675` | `92e505fe9c85fc12e464ff3e83a895e54e816b4696af618c11827b51456dccc1` | 18,914,252 | `95efbf95802cf05e7ce5d676c35470989b126b6145eb00f7e67a546948bde07e` | 1,117,799,611 | `375abf0884e415c2f4fea15d1971b818b2535996f017269fee742e90376f7fc3` |
| `K_d` | `(18,69)` | `-1680` | `1f2a0c28b60f40a429930292135451c9e96f02d1073930d508fa881c22651165` | 18,914,248 | `b852ca92b33ac461d425f62309486e30645f36f7736bd18b2b5e15b90fb27483` | 811,556,002 | `34853e20f7055e9a1e33b2668437046414e37a06821a82526eb4c822e61ab886` |

The raw CNF SHA-256 values in table order are

```text
5410ad606e1e707b35bfe3f42257a6a3dd924925e5ddf63d7013423193b74103
c7e0d8364ad664e4038b1bbb21c3c1131d5eceda77e748a18681e2f7ebef2c23
0ca9d154be8495d287ab177cd756f622e2033d0224707aa6d588058132094c11
40833477da2a42d63c89ecab8926570feabc55896a7ceb4290e2e5f52c4b9406
```

CaDiCaL solve times were 793.307, 1011.594, 1325.393, and 1008.488 seconds;
the pinned Sirius `drat-trim` checks took 419.201, 574.373, 690.524, and
527.999 seconds. Every solver run exited 20 after producing a complete proof,
and every checker run exited zero with an exact standalone `s VERIFIED` line.

Pinned proof toolchains:

| tool | source commit | binary SHA-256 |
|---|---|---|
| CaDiCaL | `c60730422e758ef1cebe7aeddf2dda31c996bf04` | `f5e2cf978a3b9ebf17601b9a7a25f298c684c18841846b66bdd6a6e20951fb2a` |
| Sirius `drat-trim` x86-64 | `2e3b2dc0ecf938addbd779d42877b6ed69d9a985` | `b535cc5334e97fba5b5db6013625c5a0b16ce348a98d59ff91b45a83fa56b39e` |
| macOS `drat-trim` arm64 | `2e3b2dc0ecf938addbd779d42877b6ed69d9a985` | `31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4` |

The arm64 binary performed a separate cross-architecture replay of the same
four authenticated CNF/proof pairs. It is not described as an independent
implementation of DRAT semantics. Its replay times were 320.114, 428.888,
539.029, and 408.999 seconds; all four verdicts were `VERIFIED`.

## Independent semantic reconstruction

`check_r3_18_budget7_branch1_core_cnf.py` independently parses the matrix and
ordered universal bank, allocates lexicographic edge variables, reconstructs
both sequential-counter families without importing the production formula
builder or PySAT, and byte-compares the full DIMACS stream. Its SHA-256 is

```text
2dcc16137a0bd555a2553e9987968fda429e9098ec8c21affb05bfd5a5e03f3b
```

The four independent audit JSON SHA-256 values are

```text
K_a  4637a558f46abefcfafc5940781eb4c9c76556793491e48b1eb5e919d9d6d581
K_b  c5d1f6823fb08388517c4eb9e0cddc040e27d080168ff4bd513928e095a908a9
K_c  3a95e9e412d78c2fb7af1e1ff68828846958a5f969a70996051d2c5dcbbef9bf
K_d  f38e987e9fecd7c4ed646cd9c0f50a3838f8ee6cadd436cd4b563d5db431b26c
```

The release replay is fail-closed: it authenticates the summary from one byte
snapshot, requires the strongest record family to be an antichain, rejects
unexpected `branch1_core_*` assets, stages authenticated private snapshots of
the checker/CNF/proof, verifies gzip completion and hashes, strips loader
injection variables, reconstructs every CNF, and freshly runs `drat-trim`.

## Checked common-relaxation model

The deterministic common-CNF and complete-model assets are:

| asset | gzip bytes | gzip SHA-256 | raw SHA-256 |
|---|---:|---|---|
| `branch1_common.cnf.gz` | 18,919,093 | `39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365` | `9602ef233f5fa95748ce4e7f997457d1bef47cd46453340bf5a44c2e163d3ec7` |
| `branch1_common.model.gz` | 391,052 | `9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d` | `51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e` |

The PySAT-free common-model checker has SHA-256
`ca83c3a3084cc37322592e3cdb283212ac8cf0ba35869f8ebc1262599a4fd39d`.
Its audit JSON SHA-256 is
`7b2af8d92d35721fd6197b3ac3c5d52066bd04faa545e219cc57b94dce035921`.
It evaluated all 718,452 clauses, recovered exactly seven seed deletions, and
confirmed all four probe edges true. It also recovered the independent set

```text
[99,96,97,95,92,90,87,91,85,93,84,73,70,88,82,81,78,83].
```

This proves only that `Psi_1` is nonempty and that this model is not a target
repair. The existence of an exact-seven repair remains `null`/unknown.

## Exact combinatorial effect

Let `E` be the 826 residual seed edges and `H98` the 18 edges incident with
vertex 98. The four singleton edges lie outside `H98`. The degree cap forces a
residual six-deletion support to meet `H98`, excluding

```text
C(808,6) = 379,362,951,275,308
```

of the raw `C(826,6)=433,155,188,594,590` supports. Avoiding the four singleton
edges removes 12,471,578,096,257 raw supports, of which 11,163,829,520,668
were already removed by the degree cap. Thus the certified singleton
consequences add exactly

```text
1,307,748,575,589 exclusions
= 2.4311102135925352% of the degree-cap survivors.
```

The number surviving both filters is

```text
C(822,6) - C(804,6) = 52,484,488,743,693.
```

Together the filters exclude 380,670,699,850,897 supports, or
87.88321365513743% of the raw support universe. These are support-index
counts, not graph counts or measured runtime speedups.

## Reproduction and publication boundary

Source-level regression:

```bash
.venv/bin/python -m unittest \
  routes.finite.test_independent_seqcounter \
  routes.finite.test_check_r3_18_budget7_branch1_core_cnf \
  routes.finite.test_check_r3_18_budget7_branch1_core_proofs \
  routes.finite.test_check_r3_18_budget7_branch1_common_sat -v
```

Normative artifact replay:

```bash
.venv/bin/python reproduce.py finite-heavy \
  --artifact-dir /absolute/path/to/the/exact-release-overlay \
  --drat-trim /absolute/path/to/an-audited-manifest-binary
```

The strict Release package contains the four singleton CNF/DRAT pairs, the
common CNF/model pair, and the two audited checker binaries plus source marker
and license. The old pair assets are excluded. A local or Sirius pass does not
by itself mean that a GitHub Release has been published or independently
replayed.

## Next bounded route

The historical order/batch/master matrix is stopped. The checked common model
exposes new independent 18-sets; a one-shot direct-CNF CEGAR gate can add a
frozen, independently validated batch together with the four proved positive
units. `SAT` may supply only a next counterexample, and `UNKNOWN` learns
nothing.  Raw `UNSAT` is not promoted unless one authenticated record replays
the proof against the exact augmented CNF and also binds and freshly replays
the singleton summary and all four singleton proofs that justify those units.
No automatic solver/order/batch sweep is authorized by this record.
