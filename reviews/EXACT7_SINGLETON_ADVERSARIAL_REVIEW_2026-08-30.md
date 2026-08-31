# Adversarial review of the S3 closure and exact-seven singleton package

Date: 2026-08-30  
Scope: current unified-manuscript source, the lower-bound S3 closure, the
branch-1 common relaxation, four singleton CNF/DRAT pairs, the checked common
SAT model, the exact support count, and the bounded A+ no-repeat gate  
Review posture: fail closed; distinguish mathematical implication, formula
semantics, proof replay, trusted-code evidence, bounded telemetry, and global
Ramsey claims

## Executive disposition

1. **Lower S3 gap: closed locally.** The weighted reverse-propagation rule is
   proved from the indicator-kernel identity, integrability, conditional tower
   property, exact projection/conjugation identity, null-event handling, and
   both terminal levels. It is no longer an imported or free-standing
   assumption. This does **not** remove source items S1, S2, S4, or S5, make
   the source constant effective, or change the fixed-
   \(C\) order of limits.
2. **Four branch-1 singleton consequences: proof checked.** For
   \(a=(11,62)\), \(b=(18,61)\), \(c=(18,64)\), and \(d=(18,69)\), four
   independently reconstructed CNFs and four freshly replayed DRAT traces
   establish
   \[
     \Psi_1\models x_a\wedge x_b\wedge x_c\wedge x_d.
   \]
   Since every exact-seven branch-1 repair extends to a model of \(\Psi_1\),
   every such repair must preserve all four edges.
3. **Non-vacuity: checked.** A complete assignment satisfies all 718,452
   clauses of \(\Psi_1\), and all four named variables are true. The same
   assignment contains a checked independent 18-set, so it is not a target
   repair. This establishes only that the common relaxation is nonempty.
4. **Exact combinatorial effect: checked.** The degree cap plus four singleton
   restrictions exclude 380,670,699,850,897 of the
   \(\binom{826}{6}=433,155,188,594,590\) raw branch-1 residual supports,
   leaving 52,484,488,743,693. The four singleton restrictions account for
   1,307,748,575,589 exclusions beyond the degree cap, or 2.4311102136% of
   the degree-cap survivors. The combined raw-support exclusion fraction is
   87.8832136551%.
5. **Exact seven remains UNKNOWN.** None of the preceding facts constructs a
   seven-deletion repair, refutes the complete branch-1 target formula, closes
   branches 0 and 2, establishes \(\rho(H)=7\) or \(\rho(H)\ge8\), or proves
   \(R(3,18)\ge101\).
6. **A+ endpoint: authenticated SAT relaxation model, not a Ramsey witness.**
   The single bounded call returned after 2,532.3617309331894 seconds.  A
   fail-closed independent audit reparsed all 154,190 assignment literals,
   evaluated all 722,552 augmented clauses, rebuilt the graph, checked that it
   is triangle-free, and found the independent set
   \(\{81,82,\ldots,97,99\}\).  The endpoint is therefore
   `F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND`: it learns no cut, does not
   close branch 1, and does not prove \(R(3,18)\ge101\).

## 1. Lower S3 proof replay

### 1.1 Claimed implication

The revised lower manuscript states S3 as a lemma. For deterministic
nonnegative triangular \(T\), deterministic real \(\lambda_i\), and the
printed one-step inequalities for \(\mathcal K_i^T\), it propagates the
weighted potential backward through the filtration.

### 1.2 Load-bearing checks

- The indicator form
  \(\mathbb E[\mathbf1_{A_i^R}e^{-\mathcal P_i^T}\mid
  \mathcal F_{i-1}]\) is primary. The quotient by \(q_i\) is not used to
  define a conditional expectation on a zero-probability event.
- For the Gaussian truncated coordinates actually used in the paper, the
  displayed domination by linear exponentials of negative parts supplies
  finite conditional exponential moments. The proof does not silently apply
  tower or monotonicity to a nonintegrable random variable.
- The exact projection identities separate the inherited term \(U_i\), the
  new-coordinate term \(V_i\), and the boundary term \(W_i\). This yields the
  required conjugation identity without exchangeability.
- The levels \(s=r\) and \(s=r-1\) are both checked. The latter is essential
  because the one-step premise stops at \(i<r\).
- Reverse induction uses
  \(\Lambda_{i-1}=\lambda_i+\Lambda_i\) with the correct index range.

### 1.3 Remaining boundary

The fixed-ratio result remains a source-relative theorem under S1, S2, S4,
and S5. A standalone, source-independent Ramsey lower bound is not established.
The admissible-history, fixed-large-\(C\), non-effective \(C_0(K)\), and order-
of-limits qualifications remain mathematically active.

**Disposition:** PROVABLE AS CURRENTLY STATED, subject to the four remaining
version-pinned source items.

## 2. Exact-seven logical chain

### 2.1 Target-to-relaxation direction

The common formula \(\Psi_1\) contains:

- every triangle clause;
- an exact-six counter on residual seed-edge deletions;
- the fixed negative unit for \((97,99)\);
- degree-at-most-17 counters for every vertex; and
- the ordered 251,771-clause bank of valid independent-18 hitting clauses.

Every exact-seven branch-1 target graph satisfies these conditions and has an
extension to the auxiliary counter variables. The universal bank is
incomplete, so the only sound implication is

\[
  \text{target repair}\Longrightarrow\Psi_1.
\]

The reverse implication is neither used nor true in general.

### 2.2 Singleton proof direction

For each \(e\in\{a,b,c,d\}\), the authenticated formula is exactly
\(\Psi_1\wedge\neg x_e\). A checked refutation therefore proves
\(\Psi_1\models x_e\). Composing this with the target-to-relaxation
implication proves that a target repair cannot delete \(e\).

The proof does not establish that these are the only forced edges, that the
set of four is minimal, or that adding the four units makes the target formula
complete.

### 2.3 Formula authentication

The common formula fingerprint is
`a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2`.
Each singleton instance has 154,190 variables and 718,453 clauses. The
independent semantic checker:

- imports neither PySAT nor the production formula builder;
- reconstructs triangle, equality-counter, fixed-unit, degree-counter, and
  ordered bank blocks;
- verifies the candidate negative unit and its polarity; and
- compares the complete DIMACS byte stream.

The final proof-summary digest is
`8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a`.
The old pair proofs are valid but strictly dominated and are excluded from the
normative antichain.

### 2.4 Proof authentication

All four CaDiCaL runs exited with complete DRAT traces. Pinned `drat-trim`
replayed every trace to one exact `s VERIFIED` status. A separately compiled
arm64 checker replayed the same four traces. This cross-architecture check
reduces binary/build risk but is not a logically independent implementation
of DRAT semantics; the standard checker remains inside the trusted computing
base.

The release replay additionally authenticates the summary before parsing,
stages private immutable input snapshots, removes dynamic-loader injection
variables, binds the checker to its adjacent source-commit marker, rejects
undeclared or aliased assets, and prevents output paths from colliding with
authenticated inputs.

**Disposition:** PROOF-CHECKED CONSEQUENCES OF THE FROZEN RELAXATION.

## 3. Non-vacuity and witness boundary

The checked common model has compressed CNF and model identities
`39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365`
and
`9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d`.
Direct evaluation accepts every common clause. The model sets all four named
edge variables true and contains the independently checked 18-set

\[
\{99,96,97,95,92,90,87,91,85,93,84,73,70,88,82,81,78,83\}.
\]

Thus \(\Psi_1\) is satisfiable, while this model violates the actual
independence constraint. It cannot be reported as a near-certificate, repair,
or positive Ramsey witness.

## 4. Exact support count

Let \(\Delta_{98}\) be the 18 residual seed edges incident with vertex 98.
The degree cap requires every six-edge support \(D\) to meet
\(\Delta_{98}\). The four singleton edges are outside \(\Delta_{98}\).
Therefore the supports surviving both filters are exactly

\[
  \binom{822}{6}-\binom{804}{6}=52,484,488,743,693.
\]

The raw universe is \(\binom{826}{6}=433,155,188,594,590\), and the
degree-only survivors number
\(\binom{826}{6}-\binom{808}{6}=53,792,237,319,282\). Subtraction gives the
reported additional and combined exclusion counts.

This calculation counts deletion-support indices. It is not a count of final
graphs, satisfying assignments, isomorphism classes, or solver branches, and
it does not imply a proportional runtime reduction.

## 5. A+ no-repeat gate

The A+ batch is deterministically regenerated from the checked common model by
reverse-first independent-set enumeration. It excludes three authenticated
families:

| family | masks | ordered SHA-256 |
|---|---:|---|
| universal bank | 251,771 | `f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa` |
| historical learned union | 64,591 | `74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8` |
| exhaustive fixed-base family | 235,504 | `1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c` |

The accepted 4,096-mask batch has ordered digest
`a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0`
and zero overlap with each family. It was obtained after 192,166 recursive
nodes, 6,512 completed witnesses, and 2,416 exclusions. No solver is invoked
by the generator.

Adding the four proved positive units and 4,096 hitting clauses to the common
formula produces 154,190 variables, 722,552 clauses, 183,161,315 bytes, and
SHA-256
`6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f`.
Separate local and Sirius exports from the same implementation were
byte-identical.  This is a cross-host determinism check, not an independent
implementation of the exporter.

The one parent-enforced 3,600-second CaDiCaL call returned a complete SAT
assignment after 2,532.3617309331894 seconds.  The historical gate JSON,
compressed model, and independent audit have respective SHA-256 identities
`d46115036cb6aba0411a50659f7bfca9efcd2dad739ba75d51f3b3286d3d36b3`,
`19db55d05fe0b907ab77dc9645cf9356fd383bdbb83d91aa7690c6473965ffd3`,
and
`b1f1732dfcdd1274c84c83aa7237d8385156c260b1f5e78f90b39a3e4f24ab82`.
The independent audit re-evaluated every exact clause and recovered the
triangle-free 823-edge graph together with the independent 18-set
\[
 \{81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99\}.
\]
That set belongs to both the historical learned-cut union and the exhaustive
fixed-base family, but to neither the installed universal bank nor the A+
batch.  Thus the SAT assignment explains a finite-bank omission; it is not a
target repair.  A fresh local reconstruction of the augmented CNF reproduced
its exact SHA-256, and combining it with the committed endpoint files yielded
a byte-identical second audit JSON.

Acceptance rules are asymmetric:

- SAT requires a complete unique assignment, direct evaluation of every
  augmented clause, and an exact graph check. A returned independent 18-set is
  classified against the universal, historical, new-batch, and fixed-base
  families and is not learned automatically.
- timeout, malformed output, kill, or other UNKNOWN learns no mask and proves
  nothing.
- exit 20 plus a nonempty trace remains `UNSAT_UNCHECKED`.  Promotion requires
  all of the following in one authenticated record: a fresh `drat-trim` replay
  of the trace against the exact augmented CNF with SHA-256
  `6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f`;
  authentication of the frozen singleton summary; and fresh replay of all
  four singleton CNF/DRAT proofs that justify adding the four positive units
  to \(\Psi_1\).  Replaying only the augmented trace would prove an artificially
  strengthened formula unsatisfiable, not close branch 1.

## 6. Literature and attribution audit

The current interval \(100\le R(3,18)\le120\) is attributed to revision 18
of Radziszowski's dynamic survey. The public 99-vertex lower-bound
construction is now explicitly attributed to Nagda, Raghavan, and Thakurta,
*Reinforced Generation of Combinatorial Structures: Ramsey Numbers*,
arXiv:2603.09172v5. This attribution was missing from the finite introduction
and has been added to the canonical source and bibliography.

The AlphaEvolve work uses evolved stochastic search, with the \(R(3,18)\)
route described through cyclic and block constructions, adaptive growth,
heuristic filtration, and exact independence-number validation.  A separate
solver-trusted exact CEGAR run for a direct triangle-free,
independent-18-free one-point extension of the frozen 99-vertex base returned
`UNSAT`, but it emitted no DRAT/LRAT certificate and is not described here as
a proof-carrying refutation.  This is distinct from the one-triangle near miss
\(H\). Merely rerunning the same fixed-base extension or relabeling the current
CEGAR loop is not a new technique.

Smart cubing and co-certificate learning remain methodological references,
not evidence that cubing or another lazy clause prefix will solve this
instance. The existing pipeline already implements the basic witness-to-
clause co-certificate pattern; a future proposal must provide lifting,
coverage, or a quantitatively falsifiable decomposition advantage.

## 7. Submission blockers and stop rules

Hard blockers before a release-candidate claim:

1. replace both A+ placeholders with the frozen endpoint and its exact claim
   disposition, and freeze an endpoint-specific authenticated record.  A SAT
   endpoint additionally requires its complete model and an independent
   clause/graph audit; an UNSAT endpoint additionally requires the augmented
   CNF, proof, augmented-proof replay, and bound four-singleton replay chain.
   These endpoint artifacts are not part of the pre-endpoint 26-asset set;
2. finish the 26-asset heavy replay, including all four singleton DRAT traces;
3. run the complete repository test suite after all files are stable;
4. materialize the unified paper from canonical sources and build it twice;
5. inspect changed PDF pages and require a clean LaTeX log;
6. verify the release manifest, privacy scan, and clean-clone command surface;
7. commit and push the exact source snapshot before claiming GitHub sync; and
8. obtain fresh action-time confirmation before sending the ChatGPT Pro
   collaboration packet.

Stop rules:

- no automatic second A+ round;
- no claim from UNKNOWN or an unchecked proof;
- no promotion from branch 1 to all three branches;
- no promotion from local pruning or a branch closure to a global Ramsey
  number; a complete independently checked 100-vertex target witness would,
  by contrast, legitimately prove \(R(3,18)\ge101\);
- no claim that local S3 closure removes S1, S2, S4, or S5;
- no standalone or source-independent reading of the lower theorem, no
  effective \(C_0(K)\), and no exchange of the fixed-\(C\),
  \(\ell\to\infty\), then \(C\to\infty\) limit order; and
- no unproved common-normalization comparison or priority claim relative to
  Lin--Niu.

## Final review verdict

Subject to replacing the A+ placeholders and completing the listed
reproduction/build gates, the S3 closure and four singleton consequences are
logically clean and correctly bounded. The largest remaining scientific gap
is unchanged: exact seven is unresolved. The correct publication value is a
proof-carrying local obstruction with a new family-level singleton pruning
result, not a new global value or bound for \(R(3,18)\).
