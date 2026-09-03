# Archived ChatGPT Pro response — exact-seven finite repair

Captured on 2026-09-02 PDT from the pre-existing registered exact-seven conversation after matching the visible personal account. The response is advisory and does not itself constitute a graph witness or an UNSAT certificate. Original prompt/status labels elsewhere may predate the actual submission.

Conversation: [Generate adversarial report](https://chatgpt.com/c/6a94f943-6db4-83e8-9620-be57ee17c8b4)

---

# Adversarial proof-aware report on the Ramsey exact-seven packet

## 1. Executive assessment

I reviewed the full text-only packet and treated the **CURRENT DELTA** as authoritative. I did **not** receive the seed matrix, DIMACS instances, DRAT/LRAT files, reconstruction code, binaries, or checker logs, so I have not independently replayed any proof. Throughout this report, “packet-reported verified” means exactly that: the text reports a checked computation; it is not a claim that I reran it.

The delta materially changes the evidence state. The four pairs

$\begin{aligned}
K_{ab}&=\{(11,62),(18,61)\},\\
K_{ac}&=\{(11,62),(18,64)\},\\
K_{ad}&=\{(11,62),(18,69)\},\\
K_{bd}&=\{(18,61),(18,69)\}
\end{aligned}$

are no longer heuristic one-$D$ no-goods. The packet reports four standalone UNSAT instances, each proof-produced by CaDiCaL, accepted by pinned `drat-trim`, independently reconstructed, and replayed using a separately compiled arm64 build of the same checker. It explicitly limits them to **local branch-1, exact-six family exclusions**, disclaims minimality, and leaves all four singleton assumptions pending. 

My bottom-line judgments are:

- **The logical form of each pair exclusion is sound**, provided the independently reconstructed CNF really has the advertised branch-1 semantics and every exact branch-1 witness maps to a model of the common formula.

- **The four exclusions are useful certified structure but weak bulk pruning.** Their union excludes only about $0.0175\%$ of raw six-deletion sets.

- **They do not establish a four-edge structural theorem, singleton exclusions, branch UNSAT, $\rho(H)\ge 8$, or any new Ramsey bound.**

- **Do not spend the next cycle repeating pair extraction.** The highest-value work is:
  - proof-checked lifted deletion inequalities or projected deletion relations;
  - a seed-relative “near-independent 18-set” formulation;
  - proof-aware cubing only after the external-cut ledger is frozen.

- The two arm64/x86 replays improve operational confidence, but **they are not independent proof checkers**. Both use the `drat-trim` implementation. The four relatively small pair packages should be converted to LRAT and checked by a formally verified checker before they are used as foundational lemmas in a final proof package.

The exact-seven endpoint remains unchanged: either a verified graph with exactly seven deleted seed edges, or checked UNSAT for all three exhaustive triangle-edge branches. A witness proves $R(3,18)\ge101$; three-branch UNSAT proves only the labelled, one-sided statement $\rho(H)\ge8$. 

---

## 2. What is now established, and what is not

| Claim | Assessment | Reason |
| --- | --- | --- |
| The four files $F_1\land K_i$ are UNSAT | **Packet-reported proof-carrying result** | The delta reports deterministic DIMACS, CaDiCaL DRAT, two `drat-trim` replays, and independent CNF reconstruction. I did not receive the artifacts. |
| $F_1\models\bigvee_{e\in K_i}\neg d_e$ | **Logically follows** | This is the propositional consequence of $\operatorname{UNSAT}(F_1\land\bigwedge_{e\in K_i}d_e)$. |
| No exact branch-1 Ramsey repair can contain $K_i$ | **Follows conditionally on the encoding interface** | It requires every valid branch-1 repair to induce a model of the checked common formula $F_1$. |
| The four pairs are minimal cores | **Not established** | No singleton SAT result or checked minimality certificate is supplied. The delta expressly disclaims minimality. |
| Any of the four singleton deletions is impossible | **PENDING/UNKNOWN** | The delta explicitly assigns this status. |
| The same clauses apply to branches 0 or 2 | **Not established** | The seed has no accepted symmetry transferring branch-1 consequences to another branch. |
| There is a reusable graph-theoretic obstruction involving vertices 11, 18, 61, 62, 64, 69 | **Not established** | The clauses may arise from global exact-six, addition, and $I_{18}$ interactions rather than a local lemma. |
| Branch 1 is UNSAT | **Not established** | Four excluded pair families are far from exhaustive. |
| $\rho(H)=7$, $\rho(H)\ge8$, or $R(3,18)\ge101$ | **Not established** | None of the required endpoint certificates exists. |

The historical deletion-first implementation and its bounded runs remain diagnostics only. In particular, the reverse-order diagnosis showed that the two old deep fixed-$D$ stalls were ordering artefacts; the repaired gates then spent their walls in the master and produced neither candidates nor proofs.  

---

## 3. Exact logical audit of the four pair exclusions

Let $F_1(d,x,z)$ denote the frozen branch-1 common CNF:

- branch edge $(97,99)$ is absent;

- $d_e=1$ means residual seed edge $e$ is deleted;

- exactly six of the 826 residual seed edges are deleted;

- $x$ denotes free addition or final-edge variables;

- $z$ denotes encoding auxiliaries;

- all installed triangle, degree, and independently valid $I_{18}$ constraints are included.

For any $K\subseteq E(H)\setminus\{(97,99)\}$,

$\operatorname{UNSAT}
\left(
F_1\land\bigwedge_{e\in K}d_e
\right)$

implies

$F_1\models C_K,
\qquad
C_K:=\bigvee_{e\in K}\neg d_e.$

The proof is elementary. If an assignment satisfied both $F_1$ and every $d_e$, $e\in K$, it would satisfy the supposedly UNSAT conjunction.

To turn this CNF fact into a combinatorial family exclusion, one further implication is required:

$T_1\Longrightarrow F_1,$

where $T_1$ is the exact combinatorial branch-1 specification. It is enough that $F_1$ be a **sound relaxation**: it may omit some $I_{18}$ constraints, but it must never exclude a valid target graph for an unjustified reason. If $T_1\Rightarrow F_1$, then

$T_1\land\bigwedge_{e\in K}d_e
\Longrightarrow
F_1\land\bigwedge_{e\in K}d_e,$

contradicting the checked UNSAT result.

### 3.1 The actual four deletion clauses

Write

$a=d_{11,62},\quad
b=d_{18,61},\quad
c=d_{18,64},\quad
d=d_{18,69}.$

The accepted consequences are

$\neg a\lor\neg b,\qquad
\neg a\lor\neg c,\qquad
\neg a\lor\neg d,\qquad
\neg b\lor\neg d.$

Equivalently:

- selecting $a$ excludes $b,c,d$;

- selecting $d$ excludes $a,b$;

- selecting $b$ excludes $a,d$;

- selecting $c$ excludes only $a$, among these four variables.

This is **not** an at-most-one constraint on $\{a,b,c,d\}$. The known clauses do not exclude $b=c=1$, nor do they exclude $c=d=1$. They also do not establish that any one of $a,b,c,d$ is itself impossible.

### 3.2 Exact coverage

There are

$\binom{826}{6}=433{,}155{,}188{,}594{,}590$

raw six-deletion sets in branch 1.

A checked core of size $k\le 6$ excludes precisely

$N_k=\binom{826-k}{6-k}$

raw deletion sets containing that core.

| Core size $k$ | Raw sets excluded | Fraction of all six-sets |
| --- | --- | --- |
| 1 | 3,146,405,728,290 | $0.726392251816\%$ |
| 2 | 19,069,125,626 | $0.004402377284\%$ |
| 3 | 92,568,571 | $2.137076351\times10^{-5}\%$ |
| 4 | 337,431 | $7.790071755\times10^{-8}\%$ |
| 5 | 821 | $1.895394587\times10^{-10}\%$ |

Thus a verified singleton would be roughly 165 times more valuable in raw coverage than one pair clause.

Because the four pair families overlap, their coverage must not be added naively. Among the four distinguished variables, four two-element patterns are forbidden, all four three-element patterns contain a forbidden pair, and the four-element pattern is forbidden. Therefore their exact union is

$4\binom{822}{4}
+
4\binom{822}{3}
+
\binom{822}{2}
=
75{,}906{,}565{,}651.$

This is

$0.017524103982\%$

of the raw six-deletion space.

The existing degree argument at vertex 98 leaves

$\binom{826}{6}-\binom{808}{6}
=
53{,}792{,}237{,}319{,}282$

sets after requiring a deletion among the relevant 18 incident edges. Since none of $a,b,c,d$ is incident to 98, the four pair clauses exclude

$\begin{aligned}
&4\!\left[\binom{822}{4}-\binom{804}{4}\right]
+4\!\left[\binom{822}{3}-\binom{804}{3}\right]\\
&\qquad+\left[\binom{822}{2}-\binom{804}{2}\right]
=6{,}437{,}315{,}625
\end{aligned}$

of that simple degree-filtered space, or approximately $0.0119670\%$. The packet correctly warns that exact combinatorial coverage is not a wall-time prediction. 

The right interpretation is therefore:

The pair clauses are valuable because they are the first certified nontrivial projection of the exact branch onto deletion variables, not because four clauses materially collapse the search space.

---

## 4. Adversarial audit of the certificate chain

The reported chain is respectable, but it should be described with the following exact trust boundaries.

### 4.1 What the DRAT checks establish

A successful DRAT check establishes that the precise DIMACS formula supplied to the checker is unsatisfiable. The official `drat-trim` specification requires every addition to satisfy its redundancy rule and the proof to derive the empty clause. [GitHub](https://github.com/marijnheule/drat-trim)

It does **not** itself establish:

- that variable $v$ means deletion of the advertised seed edge;

- that the 826-variable counter excludes the branch edge and all original nonedges;

- that free additions were encoded correctly;

- that all clauses came from sound graph constraints;

- that the supplied seed equals the stated frozen matrix;

- that the proof was actually checked against the independently reconstructed CNF rather than only against the production CNF.

Those are encoding and artifact-interface obligations.

### 4.2 Same checker, different build

Replaying on x86 and arm64 independently compiled binaries catches some compiler, architecture, file-corruption, and build-environment failures. It does not diversify the checking algorithm: both verdicts ultimately rely on the same `drat-trim` implementation.

For these four pair packages, the next trust upgrade should be:

- convert or elaborate each DRAT to LRAT;

- check the LRAT with a formally verified checker;

- archive the resulting formula-specific theorem or checker transcript.

LRAT-Catcher now exposes a formally verified Lean-core LRAT checker and can also compose cube-and-conquer leaves with a checked cover certificate. [arXiv](https://arxiv.org/html/2607.00815v1)

This is not required for using the pair clauses in exploratory search. It is strongly recommended before they become axioms of the final proof chain.

### 4.3 The common hash is insufficient by itself

The common formula fingerprint

```
a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2
```

pins the common CNF $F_1$, but not automatically the four formulas $F_1\land K_i$. A complete package needs, for each $K_i$:

- the common formula hash;

- variable-map hash;

- canonical edge-to-variable mapping;

- ordered assumption/unit list;

- complete per-core DIMACS hash;

- DRAT hash;

- LRAT hash, when available;

- solver binary/source hash and command line;

- checker binary/source hash and command line;

- complete stdout/stderr and exit status.

The independent generator should either:

- reproduce the exact per-core DIMACS bytes and therefore the exact SHA-256; or

- reproduce an explicitly normalized clause multiset under an independently checked variable map, followed by proof replay against the independently emitted DIMACS.

“Independently reconstructed” without specifying which comparison and replay occurred leaves an avoidable ambiguity.

### 4.4 Additions must remain existentially available

For a family exclusion, addition variables must remain free variables subject to the full common constraints. Fixing them to one historical addition pattern would prove only that one completion fails.

Thus the correct object is

$\exists d_{\bar K},x,z\;
F_1(d,x,z)\land\bigwedge_{e\in K}d_e,$

not a particular fixed-$x$ subproblem.

### 4.5 Lazy $I_{18}$ clauses

The $I_{18}$ bank need not be complete for an UNSAT family proof. It must, however, be:

- frozen for the proof-producing rerun;

- content-addressed;

- composed only of universally valid clauses;

- independently reconstructible from their 18-vertex witnesses.

An incomplete bank gives a weaker formula. UNSAT of that weaker formula is still sufficient. A bank contaminated by a heuristic no-good is not.

The packet’s current acceptance policy already has the correct direction: a finite installed formula is a relaxation, so its UNSAT is conclusive while its SAT requires further separation and independent candidate checking. 

---

## 5. Exact integration of the four pair clauses

The common formula hash must remain immutable. Do not regenerate the common formula with four new clauses and call the result the same formula.

Use this three-layer identity:

$\texttt{base\_formula\_hash}
\quad+\quad
\texttt{ledger\_root}
\quad\longrightarrow\quad
\texttt{augmented\_formula\_hash}.$

### 5.1 Scope

Each pair entry must carry:

```
seed_scope: e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e
branch_scope: fixed_absent=(97,99)
budget_scope: exactly_six_residual_deletions
common_formula: a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2
```

The clauses must not be installed unconditionally into:

- branch 0;

- branch 2;

- an at-most-six formulation;

- an exact-$k$ formulation with another $k$;

- a re-encoded formula whose semantic relationship to the checked formula has not been proved.

### 5.2 Append-only integration

The recommended discovery formula is

$M_1\land C_{ab}\land C_{ac}\land C_{ad}\land C_{bd},$

where $M_1$ is the current branch-1 master. It is acceptable that $M_1$ is not byte-identical to the checked $F_1$, provided the external ledger establishes that the four clauses are valid for the same target specification.

For a final CNF proof, there are two valid composition choices:

- **External lemma composition.**
  Check each core proof, accept its conclusion into the ledger, then check the final augmented formula. A small meta-checker verifies:
  $T_1\Rightarrow M_1,\qquad T_1\Rightarrow C_i,\qquad
\operatorname{UNSAT}(M_1\land\bigwedge_i C_i).$

- **Single proof derivation.**
  Transform or stitch the assumption refutations into derivations of the four clauses from the final common formula and include them in one LRAT/DRAT chain.

The first route is simpler and naturally matches the requested MathCheck-style ledger.

### 5.3 Formula evolution

If a later formula is literally

$F'_1=F_1\land G$

with only appended, independently valid constraints, every old pair clause remains valid because $F'_1\land K_i$ is also UNSAT.

If the formula is re-encoded, drops clauses, changes the counter, renumbers variables, or alters cut semantics, hash ancestry alone is insufficient. Reprove the pair lemmas or produce a checked equivalence/interface proof.

### 5.4 Coverage accounting

Maintain three separate quantities:

- **raw exact-six coverage**, exactly countable from the $d$-only clauses;

- **coverage after a named static $d$-only relaxation**, such as the vertex-98 hit;

- **empirical solver impact**, measured on a fixed formula and fixed run protocol.

Do not describe empirical speedup as “coverage,” and do not estimate union coverage by summing individual core counts.

---

## 6. Conditional singleton plan

### Outcome A: at least one singleton is VERIFIED

A verified singleton $\{e\}$ gives the unit

$\neg d_e$

and excludes

$\binom{825}{5}=3{,}146{,}405{,}728{,}290$

raw six-deletion sets, or $0.726392\%$.

For $s$ distinct verified singleton units among the four candidates, the exact raw union is

$\binom{826}{6}-\binom{826-s}{6}.$

For $s=1,2,3,4$, the excluded fractions are approximately:

| Verified singleton count | Raw fraction excluded |
| --- | --- |
| 1 | $0.726392\%$ |
| 2 | $1.448382\%$ |
| 3 | $2.165991\%$ |
| 4 | $2.879240\%$ |

Actions:

- Append each unit as a separately proven ledger lemma.

- Mark pair clauses containing that literal as **subsumed for solving**, but retain their proof records.

- Keep the existing exact-six counter and add the unit. Do not silently rebuild a five-of-825 counter while preserving the old formula identity.

- Use the singleton to seek a genuinely lifted statement, not merely more pairs. For example, if $a$ is verified impossible, search elsewhere. If $a$ remains possible but the pair results survive, test an implication of the form
  $d_a=1\Longrightarrow\sum_{e\in B}d_e=0$
  for a larger, structurally chosen set $B$ of edges incident to vertex 18.

- Do not transfer the unit to another branch or another seed edge through an alleged symmetry.

### Outcome B: all singleton attempts are UNKNOWN or non-verified

Actions:

- Preserve the four pair clauses and stop the identical singleton route at the declared 1800-second wall.

- Distinguish:
  - timeout or no proof: `UNKNOWN`;
  - emitted proof rejected by a checker: invalid artifact requiring debugging;
  - hash or reconstruction mismatch: quarantine the whole result.

- Do not infer singleton satisfiability or pair minimality.

- Move to group or projected constraints. The most direct candidate suggested by the current pattern is not another pair, but:
  $F_1\land d_a\land
\left(\sum_{e\in B}d_e\ge1\right),$
  where $B$ is a predeclared set of edges incident to vertex 18. If this is proof-checked UNSAT, it certifies all pair conflicts between $a$ and $B$ at once.

- Another candidate is
  $\sum_{e\in B}d_e\le1$
  for a carefully chosen incident-edge set $B$, checked by refuting
  $F_1\land\left(\sum_{e\in B}d_e\ge2\right).$

- Use the pair clauses as propagation inside the cuber, but do not assume $a$ is a good split variable: its raw positive branch is only about $6/826$ of the exact-six space and is highly unbalanced.

---

## 7. Ranked nonredundant exact-seven techniques

| Rank | Technique | Formulation and expected benefit | Certificate path | Cost | Falsifiable failure signal |
| --- | --- | --- | --- | --- | --- |
| **1** | **Proof-checked deletion projection and lifted inequalities** | Derive $d$-only clauses or PB inequalities $L(d)$ by checking $F_b\land\neg L$ UNSAT. Generalizes pair cores to implications, at-most-$t$ constraints, and small projected relations. Directly attacks the master bottleneck. | Standalone deterministic CNF/OPB for $F_b\land\neg L$; DRAT→LRAT or VeriPB; independent checker and ledger entry. | Medium | After a fixed candidate budget, no verified non-subsumed cut achieves at least ten times the unique coverage of the current four-pair union or materially balances cubes. |
| **2** | **Near-independent-18 hypergraph/transversal formulation** | Enumerate 18-sets inducing at most six residual seed edges. Add their exact conditional edge-hitting rows statically or via a ZDD/BDD. This changes the representation rather than merely the separator order. | Every row reconstructed from a sorted 18-set; deterministic CNF/OPB; UNSAT proof. Completeness is unnecessary for an UNSAT relaxation, but required to claim an exact static encoding. | High, but sharply testable | Layer counts or decision-diagram size exceed the declared cap, or a fixed replay shows no propagation/master improvement over the existing cut bank. |
| **3** | **Proof-aware deletion-only cubing** | Freeze the cut ledger, partition only the 826 $d$-variables, and conquer cubes independently. Pair/lifted clauses contribute propagation. | Deterministic cover certificate plus one checked proof per UNSAT cube; SAT cubes return to all candidate verifiers. | Medium–high | Exact-six calibration fails coverage checking, exceeds the monolithic CPU/proof-size ratios, or produces a heavy-tailed set of unresolved cubes. |
| **4** | **Native pseudo-Boolean exact-branch formulation** | Replace sequential-counter CNF by native equalities and inequalities for exact deletion count, triangle constraints, degrees, and conditional $I_{18}$ rows. Cutting-plane reasoning may expose budget interactions hidden by the CNF counter. This is speculation until calibrated. | OPB formula, proof-producing PB solver, VeriPB; optionally PBLean/CakePB for formally verified checking. | Medium–high | Exact-six proof-producing calibration is slower by more than $2\times$, or certificate/checking size exceeds the declared disk budget. |
| **5** | **Global one-sided PB/MaxSAT repair optimization** | Minimize $\sum_{e\in E(H)}(1-x_e)$, avoiding three overlapping triangle branches. A checked lower bound of 8 proves $\rho(H)\ge8$; a cost-$\le7$ model is independently verified. This requires a new audited reduction and must not be presented as a silent change from exact seven to at most seven. | VeriPB optimization/lower-bound certificate plus exact candidate checker. | High | Proof logging cannot certify the chosen optimization algorithm, or exact-six predecessor calibration offers no benefit over the branch formulation. |
| **6** | **Small-scope structural kernel around the pair support** | Compute the complete feasible relation on $\{a,b,c,d\}$, or a larger bounded-radius deletion interface around vertices 11 and 18, rather than checking isolated pairs. Seek a human-readable neighborhood lemma or a compact BDD constraint. | One checked proof for each excluded local pattern or one proof of the compiled projected relation; independent relation checker. | Low–medium | The complete projection yields only the four already known clauses and no stronger relation or explanatory invariant. |

### Novelty warning

None of “use unsat cores,” “use CCL,” “use cubing,” or “use PB” is methodologically new. Co-certificate learning already formalizes witness-to-clause learning for graph search, and the packet’s lazy $I_{18}$ loop is already an instance of that basic pattern. [arXiv](https://arxiv.org/abs/2306.10427?utm_source=chatgpt.com)

Likewise, prerun collection followed by graph-search cubing is established methodology rather than a novelty claim. [arXiv](https://arxiv.org/html/2501.17201v1)

The plausible novelty is instead:

- the **Ramsey-repair-specific projection** onto exact deletion patterns;

- the **near-independent-set layer decomposition** induced by the six-deletion budget;

- a new certified repair or obstruction for this fixed 100-vertex seed;

- possibly a reusable proof architecture connecting lifted deletion lemmas, cubing, and exact Ramsey candidate verification.

---

# 8. Fully specified formulation I: proof-checked generalized deletion projection

## 8.1 Common formula

For each branch $b$, freeze

$F_b(d,x,z),$

where:

- $d_e\in\{0,1\}$, one for each of the 826 residual seed edges;

- $\sum_e d_e=6$;

- the branch triangle edge is fixed absent and excluded from the counter;

- all seed nonedges remain free addition variables;

- triangle and exact degree constraints are included;

- every installed $I_{18}$ clause is reconstructible and universally valid.

The common formula must have a content hash independent of any candidate core.

## 8.2 Simple generalized core

For $K\subseteq E(H)\setminus\{b\}$, generate the proof instance

$Q_{b,K}
=
F_b\land\bigwedge_{e\in K}d_e.$

A checked refutation yields

$F_b\models\bigvee_{e\in K}\neg d_e.$

Assumption-based solving may be used to propose $K$, but the final proof run must export a standalone formula with explicit units. A solver’s failed-assumption array is discovery telemetry, not a certificate.

## 8.3 Lifted cardinality cut

For $S\subseteq E(H)\setminus\{b\}$ and $t<|S|$, propose

$L(S,t):\qquad \sum_{e\in S}d_e\le t.$

Check

$Q_{b,S,t}
=
F_b\land
\operatorname{Enc}\!\left(\sum_{e\in S}d_e\ge t+1\right).$

If $Q_{b,S,t}$ is proof-checked UNSAT, then $L(S,t)$ is valid.

A native OPB/VeriPB check is preferable for large $S$, because it avoids adding another opaque cardinality encoder. VeriPB is designed to check pseudo-Boolean refutations and optimization claims; PBLean can import elaborated VeriPB proofs into Lean. [GitHub](https://github.com/StephanGocht/VeriPB) [arXiv](https://arxiv.org/abs/2602.08692?utm_source=chatgpt.com)

## 8.4 Exact raw coverage

A lifted inequality over $m=|S|$ variables blocks

$B(m,t)
=
\sum_{j=t+1}^{\min(m,6)}
\binom{m}{j}\binom{826-m}{6-j}$

raw exact-six sets.

For a conventional size-$k$ core, take $m=k$ and $t=k-1$, recovering

$B(k,k-1)=\binom{826-k}{6-k}.$

Candidate cuts should be ranked by **unique incremental coverage after all existing $d$-only constraints**, computed by a small exact BDD/DP, not by individual counts.

## 8.5 Recommended first lifted hypotheses

The following are hypotheses, not consequences of the current proofs:

- For a selected set $B\subseteq\delta_H(18)$,
  $d_{11,62}=1
\Longrightarrow
\sum_{e\in B}d_e=0.$
  Certify through
  $F_1\land d_{11,62}\land\left(\sum_{e\in B}d_e\ge1\right).$

- For a selected $B\subseteq\delta_H(18)$,
  $\sum_{e\in B}d_e\le1.$

- A complete projected relation on $\{a,b,c,d\}$. There are only 16 local truth patterns. Known pair proofs already refute every pattern containing $ab,ac,ad,$ or $bd$; the remaining patterns can be tested as one bounded projection experiment rather than a new pair sweep.

## 8.6 Acceptance rule

A lifted cut enters the ledger only if:

- its scope matches the frozen seed, branch, and exact-six budget;

- the negated cut is encoded deterministically;

- the complete proof checks;

- the cut conclusion is independently reconstructed;

- all formula, proof, checker, and map hashes match;

- no heuristic or unverified no-good appears in the antecedent formula.

---

# 9. Fully specified formulation II: near-independent-18 hypergraph formulation

This is the strongest genuinely different formulation I see in the packet.

Fix a branch edge $b$, and let $D$ contain exactly six residual seed edges.

For any $18$-vertex set $S$, define

$R_b(S)
=
\left(E(H)\setminus\{b\}\right)\cap\binom{S}{2},$

the residual seed edges induced by $S$, and

$A(S)=\binom{S}{2}\setminus E(H),$

the seed nonedges inside $S$.

Let $a_f=1$ mean seed nonedge $f$ is added.

## 9.1 Key exact reduction

If

$|R_b(S)|\ge7,$

then $S$ cannot become independent, because only six residual seed edges are deleted. At least one residual seed edge inside $S$ must remain.

Therefore only

$\mathcal N_b
=
\{S\subseteq V: |S|=18,\ |R_b(S)|\le6\}$

can become independent.

For every $S\in\mathcal N_b$, add

$\boxed{
\sum_{e\in R_b(S)}(1-d_e)
+
\sum_{f\in A(S)}a_f
\ge1
}
\tag{NI18}$

or its equivalent clause

$\bigvee_{e\in R_b(S)}\neg d_e
\;\lor\;
\bigvee_{f\in A(S)}a_f.$

## 9.2 Proof of exactness

Suppose the row for $S$ is violated. Then:

- $d_e=1$ for every residual seed edge $e\in R_b(S)$;

- $a_f=0$ for every seed nonedge $f\in A(S)$;

- the branch edge $b$, if contained in $S$, is already absent.

Hence every pair in $S$ is absent in the final graph, so $S$ is independent.

Conversely, if $S$ is independent in the final graph, every residual seed edge in $S$ has been deleted. Since there are exactly six residual deletions,

$|R_b(S)|\le6,$

so $S\in\mathcal N_b$, and its row is violated.

Thus the complete family of `(NI18)` rows is exactly equivalent to $\alpha(F)<18$ under the branch and exact-six semantics.

## 9.3 Full formulation

Variables:

- $d_e$, 826 residual seed-edge deletion variables;

- $a_f$, 4,123 seed-nonedge addition variables.

Constraints:

- Exact deletion budget:
  $\sum_e d_e=6.$

- Triangle constraints. For each triple $T$,
  $\sum_{e\in R_b(T)}(1-d_e)
+
\sum_{f\in A(T)}a_f
\le2.$

- Degree constraints. For every vertex $v$,
  $\sum_{\substack{e\in E(H)\setminus\{b\}\\v\in e}}(1-d_e)
+
\sum_{\substack{f\notin E(H)\\v\in f}}a_f
\le17.$

- All `(NI18)` rows for $S\in\mathcal N_b$.

- Branch-1 only: the four independently proved pair clauses, introduced through the external ledger.

This can be emitted as OPB or compiled to deterministic CNF.

## 9.4 Why it may avoid the observed master wall

This is speculation, but it has a concrete mechanism:

- the current master learns conditional $I_{18}$ rows only after reaching particular models;

- the near-independent formulation organizes all potentially dangerous 18-sets by their induced seed-edge count;

- preloading selected low-$|R_b(S)|$ layers couples deletion and addition variables before complete master models are produced;

- a ZDD or BDD may share the large common substructure among these rows.

However, the existing full-bank-first run was poor. Therefore “preload more rows” is not itself a recommendation. The pilot must add layers incrementally:

$|R_b(S)|=0,\ 1,\ 2,\ldots$

and measure end-to-end master progress on a fixed replay.

## 9.5 Certificate semantics

There are two safe modes:

**Incomplete static bank.**

Every emitted row is independently checked as valid. The resulting formula is a relaxation. If it is UNSAT, the branch is UNSAT. Completeness of enumeration is unnecessary.

**Complete exact bank.**

To claim exactness without a final separator, enumeration completeness must be independently supported, for example by two independent enumerators with a common canonical output root, or by a separately checked enumeration certificate.

A SAT assignment from an incomplete bank remains only a candidate and must pass the exact independent-set verifiers.

---

## 10. Independent-set separator decision

Further separator work is **not the highest-value standalone route**.

The order-aware bitset separator now returns full batches of 512 or 4,096 witnesses in milliseconds, while the bounded runs spend their walls in the master. Generic vertex-selection SAT was already slower on the known fixed seed. 

The only justified continuation is separator work that changes what reaches the master:

- a compressed ZDD/BDD family;

- a proof-checked lifted deletion inequality;

- the near-independent layer formulation;

- a family certificate that dominates many ordinary 18-set clauses.

### Falsifying microbenchmark

Freeze:

- one common formula hash;

- one ledger root;

- one solver build/configuration;

- one deterministic set of starting models or random seeds;

- a fixed 30-minute replay per condition.

Compare:

- current ordinary batch separator;

- near-independent layer $0$;

- layers $0$–$1$;

- layers $0$–$2$;

- compressed representation, if available.

Positive signal must be at least one of:

- $2\times$ reduction in time to the next fully separated master model;

- $2\times$ reduction in master models required for the same number of exact fixed-$D$ completions;

- a verified lifted cut with at least ten times the current pair-union coverage;

- a complete solved relaxation with a proof.

Stop if:

- enumeration exceeds $10^9$ explicit rows;

- a decision diagram exceeds 50 million nodes or 128 GB;

- the added representation slows the fixed replay by more than $2\times$;

- it produces only more ordinary clauses and no end-to-end gain.

---

# 11. External-cut ledger

The ledger is the semantic firewall between untrusted discovery and proof production.

## 11.1 Required record fields

Every record should include:

```
schema_version
record_id
record_type
seed_sha256
branch_scope
budget_scope
base_formula_sha256
variable_map_sha256
parent_ledger_root
canonical_conclusion
conclusion_sha256
witness_or_negated_cut
proof_formula_sha256
proof_sha256
checker_name
checker_source_hash
checker_binary_hash
checker_command
checker_status
created_by
status = ACCEPTED | UNKNOWN | REJECTED | DUPLICATE
```

Accepted records contribute to the next ledger root. `UNKNOWN`, `REJECTED`, crash, and timeout records never alter solver semantics.

## 11.2 Record types

| Type | Reconstructible payload | Independent checker rule |
| --- | --- | --- |
| `I18_CUT` | Sorted 18-vertex set $S$ | Verify 18 distinct labels; reconstruct the exact final-edge hitting clause; check clause equality. |
| `DEGREE_CUT` | Vertex $v$, bound 17 | Reconstruct every incident final-edge term; verify the mathematical scope includes triangle-free and $\alpha<18$. |
| `PAIR_CORE` | $K$, explicit negated clause, per-core CNF and proof | Check formula/hash ancestry; replay proof of $F_b\land K$; reconstruct conclusion. |
| `LIFTED_PB_CUT` | $S,t$, inequality, negated-cut encoding | Check a proof of $F_b\land(\sum_{e\in S}d_e\ge t+1)$. |
| `NEAR_I18_ROW` | $S$, $R_b(S)$, $A(S)$ | Recompute induced seed edges and exact row. |
| `CRASH_OR_TIMEOUT` | Run manifest and last valid checkpoint | Diagnostic only; no cut or no-good. |
| `DUPLICATE` | Canonical conclusion hash and original record ID | No new semantic contribution or coverage credit. |
| `CHECKPOINT` | Base hash, ledger root, solver configuration, cut order | Replay only if every identity matches. It is not theorem evidence. |

## 11.3 Checkpoint semantics

A checkpoint must bind:

- seed hash;

- branch;

- variable map;

- exact counter identity;

- common formula;

- canonical ledger root;

- cut ordering;

- separator schedule;

- solver build/configuration.

Internal learned clauses may remain untrusted discovery state. If they are exported and shared across runs, they must either:

- be incorporated in a proof trace from the common formula; or

- enter the external ledger through an accepted derivation.

## 11.4 Composition with a final proof

For each branch $b$, let $T_b$ be the combinatorial target, $M_b$ the frozen master/relaxation, and $L_b$ the conjunction of accepted ledger conclusions.

The semantic checker establishes

$T_b\Longrightarrow M_b\land L_b.$

Then either:

- a monolithic checked proof establishes
  $\operatorname{UNSAT}(M_b\land L_b);$

- or cubing establishes a checked cover and
  $\operatorname{UNSAT}(M_b\land L_b\land Q_i)$
  for every cube $Q_i$.

Cube-and-conquer proof methodology requires a checked proof that the cube disjunction covers the intended search space, not merely a list produced by the cuber. [arXiv](https://arxiv.org/abs/1605.00723?utm_source=chatgpt.com)

---

# 12. Proof-aware cubing plan

Cubing begins only after the common formula and ledger are frozen.

## 12.1 Variables

Cube only deletion variables $d_e$.

Do not cube addition variables unless a separate experiment demonstrates that doing so improves exact-six calibration. Additions constitute the existential completion layer; splitting them risks reproducing the fixed-completion mistake and substantially enlarges the cover.

## 12.2 Coverage

Preferred format: a deterministic binary decision tree.

Each internal node branches on

$d_e=0
\quad\text{versus}\quad
d_e=1.$

Every leaf is either:

- an emitted cube;

- closed by a checked ledger lemma;

- closed by direct propagation from the common formula.

A tree-based structural checker can establish coverage. For arbitrary cube lists, check

$E_6(d)\land L_b(d)\land
\bigwedge_i\neg Q_i$

UNSAT and retain the corresponding proof. Coverage may be relative to the frozen exact-six and accepted $d$-only constraints; this scope must be explicit.

## 12.3 Per-cube obligations

For every cube:

- common formula hash;

- ledger root;

- cube literal list and hash;

- complete cube DIMACS hash;

- solver/proof/checker manifests;

- terminal status.

An UNSAT cube requires a checked proof.

A SAT cube must pass through:

- exact bitset Ramsey verification;

- independent vertex-selection SAT verification;

- exact edit-semantics verification.

No cube may terminate as `UNKNOWN` in a claimed full branch refutation.

## 12.4 Exact-six gate

Before exact seven, reproduce the solved exact-six branches.

Proceed only if all of the following hold:

- deterministic coverage checks;

- every cube closes with a checked proof;

- total conquer CPU is at most $1.5\times$ the monolithic exact-six CPU;

- total proof bytes are at most $3\times$ the monolithic proof bytes;

- total checker CPU is at most $3\times$ the monolithic checker CPU;

- the slowest cube is at most ten times the median cube;

- no hash, replay, or proof-check mismatch occurs.

These thresholds are deliberately stricter than “some cubes got easier.”

---

# 13. Discovery and proof production should be separate tracks

| Track | Permitted mechanisms | Positive evidence | Falsifying outcome |
| --- | --- | --- | --- |
| **Discovery** | Fast solvers, assumptions, heuristic core extraction, restarts, model sampling, unproved candidate cuts | A fully verified graph; a candidate cut later independently proved; a reproducible end-to-end improvement on a fixed replay; a balanced cube distribution validated on held-out cubes | More conflicts, more learned cuts, longer runs, or another timeout without a proof/candidate |
| **Proof** | Frozen formula, frozen ledger, deterministic DIMACS/OPB, proof-producing solver, independent checker | Checked core lemma; checked cube; checked branch refutation; formally checked LRAT/VeriPB certificate | Proof-generation failure, checker rejection, reconstruction mismatch, or projected proof storage beyond the declared cap |

The solver may be completely untrusted in the proof track. CaDiCaL’s normal command-line interface supports a DIMACS input and proof output, but the proof must be checked independently. [GitHub](https://github.com/arminbiere/cadical)

---

# 14. Bounded two-week experiment matrix

The following is a cap, not a prediction of completion.

| Phase | Work | CPU cap | Memory cap | Disk cap | Hard gate |
| --- | --- | --- | --- | --- | --- |
| **1. Pair-package hardening** | Per-core hashes, independent reconstruction replay, DRAT→LRAT, formally verified checking | 32 CPU-hours | 32 GB | 100 GB | All four formulas and proofs agree. Any mismatch halts use of the affected lemma. |
| **2. Singleton closeout** | Consume the already running 1800-second attempts; check any emitted proofs | No new identical solver runs | 32 GB | 100 GB | VERIFIED units enter ledger; all other outcomes stay UNKNOWN or REJECTED. |
| **3. Lifted deletion pilot** | At most 64 predeclared implication/cardinality candidates; at most 30 minutes discovery and 60 minutes proof production per selected candidate | 256 CPU-hours | 64 GB/job | 300 GB | Continue only if one verified cut blocks at least $0.1\%$ of the vertex-98-filtered raw space, or the union of new cuts exceeds ten times current pair-union coverage. |
| **4. Near-independent layers** | Enumerate/count ( | R_b(S) | =0,1,2,\ldots); test explicit versus compressed rows on fixed replays | 256 CPU-hours | 128 GB |
| **5. Exact-six cubing calibration** | All three solved branches, or at minimum branch 1 plus the historically largest-proof branch | 512 CPU-hours | 64 GB/job | 600 GB | Must satisfy all coverage, CPU, proof-size, checker, and balance thresholds in §12.4. |
| **6. Native PB calibration** | Exact-six branch 1 and hardest branch, OPB plus checked proof | 256 CPU-hours | 128 GB/job | 400 GB | Continue only if solve-plus-check is within $2\times$ of CNF and proof storage within $3\times$. |
| **7. Exact-seven gated pilot** | Run only the single route that passed calibration; per cube at most 2 CPU-hours and 20 GB proof output | 1,024 CPU-hours | 128 GB/job | 1.5 TB | Stop when projected total exceeds 2,500 CPU-hours or 2 TB, or when more than 20% of a stratified pilot remain UNKNOWN without a verified progress object. |

Positive signals in Phase 7 are restricted to:

- a fully verified Ramsey graph;

- a checked UNSAT cube;

- a checked lifted lemma with quantified new coverage;

- a fully checked branch refutation.

Conflict counts, solver-reported UNSAT without proof, raw cut count, or elapsed time are not positive signals.

---

# 15. Automorphism audit

The packet reports that NetworkX `GraphMatcher` enumerated one automorphism of $H$, but correctly treats this as a result requiring independent replication before it becomes evidence. 

The smallest independent route is:

- Parse the frozen seed and verify the matrix hash, vertex count, and edge count.

- Run deterministic color refinement and record the refinement transcript.

- If the final coloring is discrete, that transcript is a small certificate: every automorphism preserves each color class, hence fixes every vertex.

- If refinement is not discrete:
  - cross-check with nauty/Traces or bliss;
  - construct a nonidentity-automorphism SAT formula restricted to the unresolved color cells;
  - require a DRAT/LRAT refutation.

Nauty and Traces are specifically designed to compute graph automorphism groups and canonical labels and provide a suitable independent implementation-level cross-check. [ANU User Portal](https://users.cecs.anu.edu.au/~bdm/nauty/?utm_source=chatgpt.com)

The SAT formulation uses permutation variables $p_{v,w}$, exact-one constraints for each row and column, adjacency-preservation constraints, and

$\bigvee_v \neg p_{v,v}$

to require a nonidentity permutation. Checked UNSAT proves that the automorphism group is trivial.

Even then, the conclusion is only:

- no nontrivial seed-vertex automorphism;

- hence no inherited vertex symmetry in any fixed-edge branch.

It does not exclude auxiliary-variable symmetries created by a particular counter or encoding. SMS/Satsuma should remain non-primary unless such an encoding-level symmetry is explicitly identified and soundly exploited.

---

# 16. Minimal implementation and test plan

## 16.1 State artifacts

| Artifact | Purpose |
| --- | --- |
| `seed-H.bin` / `seed-H.edges` | Frozen labelled seed, canonical serialization |
| `variable-map.json` | Bidirectional map among edges, deletion variables, addition variables, and auxiliaries |
| `branch-b-common.cnf` | Immutable branch common formula |
| `branch-b-common.manifest.json` | Seed, branch, dimensions, clause categories, encoder identities |
| `cut-ledger.jsonl` | Canonical accepted/rejected cut records |
| `cut-ledger.root` | Content root of accepted records |
| `core-<id>.cnf/.drat/.lrat` | Standalone proof packages |
| `branch-b-augmented.cnf` | Deterministic common formula plus ledger conclusions |
| `cubes.jsonl` / `cover.lrat` | Cubes and checked coverage |
| `cube-<id>.cnf/.proof` | Per-cube instances and proofs |
| `candidate-<id>.graph` | Complete final adjacency matrix and edit lists |
| `run-manifest.json` | Exact binaries, commands, environment, resource endpoints |

## 16.2 Mandatory tests

- Exhaustive small-$n$ truth-table tests for the exact deletion counter.

- Negative tests showing the branch edge and seed nonedges never enter the deletion counter.

- Exhaustive small-instance comparison between the graph specification and both independent formula generators.

- One-bit mutation tests:
  - change a core unit;
  - change one seed edge;
  - change one DIMACS clause;
  - change the variable map;
  - verify that replay fails closed.

- $I_{18}$-cut reconstruction tests from arbitrary sorted 18-sets.

- Near-independent row tests against brute-force final graphs on small toy seeds.

- Duplicate-ledger and crash-ledger tests proving that neither changes the augmented formula.

- Checkpoint tests rejecting a stale ledger root, cut order, separator schedule, or variable map.

- Cube-cover tests with deliberately omitted and duplicated leaves.

- Candidate tests containing:
  - a hidden triangle;
  - an independent 18-set;
  - six or eight deletions;
  - a re-added fixed branch edge;
  - an incorrectly charged original nonedge.

## 16.3 Trust boundaries

**Untrusted:**

- SAT/PB/MaxSAT solver;

- failed-assumption list;

- heuristic core minimizer;

- separator schedule;

- runtime statistics;

- checkpoint internals;

- model before verification.

**Checked but not formally verified unless upgraded:**

- graph-to-CNF encoder;

- seed parser;

- independent reconstruction code;

- bitset maximum-independent-set verifier;

- coverage checker;

- ledger checker.

**Proof kernel:**

- LRAT or VeriPB checker;

- optionally Lean/CakePB/CakeLPR for a formally verified implementation;

- a small formalized or independently audited graph-encoding interface.

---

# 17. Exact acceptance requirements

## 17.1 SAT witness

Accept a witness only if the package contains:

- A complete symmetric $100\times100$ adjacency matrix on labels $0,\dots,99$, with zero diagonal.

- The frozen seed hash and an independently reconstructed seed.

- Explicit lists
  $E(H)\setminus E(F)
\quad\text{and}\quad
E(F)\setminus E(H).$

- Exactly seven elements in $E(H)\setminus E(F)$; additions are uncharged.

- Exhaustive triangle verification.

- Exact verification that no independent 18-set exists:
  - exact bitset or maximum-clique search;
  - independently encoded vertex-selection SAT check;
  - preferably a checked UNSAT proof for the latter.

- Exact edit-semantic checks, including treatment of the fixed branch edge.

- Agreement of all independent verifiers on the same graph hash.

Only this establishes a 100-vertex $(3,18)$-Ramsey graph and $R(3,18)\ge101$.

A master model, fixed-$D$ add-only model, or model satisfying an incomplete cut bank is not enough. The packet explicitly requires both independent Ramsey verifiers and exact edit checks. 

## 17.2 Three-branch UNSAT

For each of the three fixed absent edges:

$(97,98),\quad(97,99),\quad(98,99),$

require:

- Seed and variable-map hashes.

- Correct exclusion of the fixed edge from the residual counter.

- Exactly six residual deletions among the other 826 seed edges.

- A sound-relaxation argument from the exact branch specification to the checked formula.

- Frozen and independently checked cut ledger.

- Checked monolithic proof, or:
  - checked cube cover;
  - checked proof for every cube;
  - no `UNKNOWN` leaves.

- For branch 1, checked composition of the four pair lemmas and any later singleton/lifted lemmas.

- Independent formula reconstruction.

- Preferably LRAT or another formally checked proof path in addition to ordinary DRAT replay.

- A final branch-coverage argument: every triangle-free exact-seven repair omits at least one of the three seed-triangle edges and therefore appears in at least one branch.

Only after all three branches close may the conclusion be

$\rho(H)\ge8.$

It does not yield a global Ramsey upper or lower bound. 

A separately audited global PB/MaxSAT certificate for “at most seven deletions” could replace the branch decomposition logically, but it would be a different reduction and must not be silently reported as the requested three-branch package.

---

# 18. Conclusions the present data cannot support

The current packet does **not** justify any of the following:

- that any singleton among $a,b,c,d$ is impossible;

- that the four pair cores are minimal;

- that $\{a,b,c,d\}$ satisfies an at-most-one constraint;

- that there is a local graph-theoretic obstruction rather than a global exact-six encoding interaction;

- that the clauses transfer to branch 0 or branch 2;

- that branch 1, or any branch, is UNSAT;

- that a seven-deletion witness is rare or nonexistent;

- that the master is intrinsically hard;

- that the universal preload is globally helpful or harmful;

- that further separator research is mathematically useless, as opposed to currently low-value;

- that cubing will help this instance merely because it helped other graph-search systems;

- that the reported trivial automorphism group is proof evidence before independent certification;

- that two builds of `drat-trim` constitute independent checker implementations;

- that $\rho(H)=7$, $\rho(H)\ge8$, or $R(3,18)\ge101$.

These restrictions agree with the packet’s explicit do-not-repeat and non-implication rules. 

---

## Final recommendation

The immediate sequence should be:

- **Harden the four existing pair packages** with complete per-core manifests, replay against the independent reconstruction, and LRAT/formally verified checking.

- **Consume the current singleton attempts once.** Integrate verified units; otherwise freeze their status as UNKNOWN and stop that identical route.

- **Run one bounded lifted-projection campaign**, prioritizing group implications involving $d_{11,62}$ and a larger subset of edges incident to vertex 18.

- **In parallel, enumerate the near-independent layers** $|R_b(S)|=0,1,2,\ldots$ and determine whether an explicit or compressed formulation is viable.

- **Freeze the resulting ledger, validate deletion-only cubing on exact six, and only then spend proof-producing resources on exact seven.**

That sequence uses the new pair proofs as foundations without exaggerating their coverage or novelty, and it creates a route in which every positive outcome is either a verified witness, a reusable checked lemma, or a composable UNSAT certificate.

