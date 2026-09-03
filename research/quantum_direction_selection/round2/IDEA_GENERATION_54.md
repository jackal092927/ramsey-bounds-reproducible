# Round 2 idea generation 54: quantum TDA / generalized persistence

Date: 2026-09-02 (America/Los_Angeles).

Scope: bounded 15–20 minute theorem-first brainstorm. This is not an exhaustive novelty search. I used the local decision package plus a narrow primary-source refresh of the main collision papers:

- Dey–Xin, [Generalized Persistence Algorithm](https://arxiv.org/abs/1904.03766v7)
- Dey–Jendrysiak–Kerber, [Decomposing Multiparameter Persistence Modules](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.41/LIPIcs.SoCG.2025.41.html)
- Dey–Xin, [Generalized Ranks via Unfolding](https://arxiv.org/html/2403.08110v4)
- Gyurik–Schmidhuber–King–Dunjko–Hayakawa, [Provable quantum speedups for computing persistence in topological data analysis](https://arxiv.org/html/2410.21258v2)
- Lowe–Kim–Bondesan–Hayakawa, [Normalized Persistence](https://arxiv.org/html/2607.03278v1)
- Hayakawa, [Unweighted Gapped Clique Homology is QMA1-complete](https://arxiv.org/html/2608.02726v1)

Update after follow-up correction on 2026-09-02:

- The previous “variable-weight nested-copy unweighting” recommendation was too optimistic. The already-existing common-blowup executable’s one-vertex \(1\to 2\) multiplicity mismatch is exactly the first toy obstruction one should test, and it already shows normalized one-copy symmetric vectors are not inclusion-compatible. So that idea is eliminated in its naive form.
- The previous “normalization-preserving unweighting” candidate misidentified the July normalized-persistence obstacle. Under common blow-up, the relevant Betti ranks are preserved, so the \(\beta_{1,2}/\beta_1\) ratio itself is not the problem there. The real missing step remains exact-kernel / filtration-compatible realization, not simplex-count renormalization.

## Verified constraints from round 1

These are the gates I treated as fixed while generating ideas.

1. The raw limit/colimit projector route is a real no-go in the current formulation: there is a native constant-size simplicial zigzag family with generalized rank 1, both module constraint gaps bounded below, and exponentially small relevant overlap. So “local gaps imply polynomial projector conditioning” is not a viable theorem target.
2. The naive AIDA quantum-update story is false: a one-direction candidate exchange can produce rank-\(t\) change after the actual \(\alpha\)-local quotient. The right parameter is an evaluated update rank, not \(\operatorname{rank}(T'-T)\).
3. Common-multiplicity filtered unweighting of the June 2026 harmonic-persistence hard family now looks like a likely corollary of June+August 2026, not a substantial new mechanism.
4. True normalized-persistence hardness is still open in the July 2026 paper; quasi-harmonic hardness is not the same statement.
5. “Generic Grover over candidates” is not enough. Any viable theorem needs either a new exact encoding theorem, a structural low-rank update lemma, or a genuinely new restricted class.
6. Easy special cases from unfolding are bad targets: graph \(H_1\) and top-dimensional cases already have strong classical algorithms in the Dey–Xin line.

## Ranking at a glance

| Rank | Candidate | Why it survives triage |
|---|---|---|
| 1 | Quantum \(\epsilon\)-net for additive barcode approximation | Real theorem candidate, but the TDA part is close to a corollary of Kolbe–Mayr once the quantum net theorem is proved. |
| 2 | Quantum split search on bounded evaluated-Hom width | Best direct continuation of Dey–Jendrysiak–Kerber if a natural \(r_{\mathrm{eval}}\)-bounded class exists. |
| 3 | \(\alpha\)-thin indecomposable class | Best way to make Rank 2 concrete rather than purely promise-based. |
| 4 | Restricted exact-kernel realization for normalized persistence | Biggest upside, but highest proof burden and weaker continuity with Dey–Xin. |
| 5 | Canonical-basis positive-guide lift | Real caveat, but likely auxiliary rather than headline. |
| 6 | Evaluation-faithful \(\alpha\)-endomorphism lifting | Elegant if true, but very exposed to classical algebraic collapse. |
| 7 | Quantum fold-back counting under bounded duplication rank | Direct Dey–Xin continuity, but classical streaming may erase the gain. |
| 8 | Bounded-overlap interval-decomposability | Plausible parameterized problem, but probably more classical than quantum. |
| 9 | Sparse convertibility-matrix quantum verifier | Reads too much like a generic QLSA wrapper unless a new sparse exact model appears. |

## Detailed candidates

### 1. Quantum \(\epsilon\)-net for additive barcode approximation

- Objective: obtain a clean quantum algorithm for additive approximation of stable VR/Čech barcodes by accelerating the net-construction step.
- Exact input / output / field:
  - Input: \(X\subseteq \mathbb R^d\) with bounded diameter, target scale \(\epsilon\), and coherent access strong enough to test whether \(d(x,S)>\epsilon\) for a current center set \(S\).
  - Output: an \(\epsilon\)-net \(S\) of size \(K_{\mathrm{act}}\), then an additive \(\epsilon\)-approximation of the barcode by computing it exactly on \(S\).
- Core mechanism:
  - Iteratively BBHT-search for a point outside the current \(\epsilon\)-cover.
  - Because a maximal \(\epsilon\)-separated set has size \(K_{\mathrm{act}}\), the number of marked points at step \(i\) is at least \(K_{\mathrm{act}}-i+1\), giving expected search cost \(\sum_i O(\sqrt{n/(K_{\mathrm{act}}-i+1)})=O(\sqrt{nK_{\mathrm{act}}})\) predicate calls.
  - Then invoke Kolbe–Mayr’s stability logic: an \(\epsilon\)-cover is enough for additive approximation of any stable barcode.
- Closest collision:
  - Kolbe–Mayr ICALP 2026 already prove deterministic linear-time additive \(\epsilon\)-approximation of any stable barcode under bounded doubling dimension/diameter, via greedy permutations; they explicitly say the \(\epsilon\)-cover is the key object and the linear-in-\(n\) cost comes from reading the input and finding the greedy permutation.
  - Xue–Chen–Li–Jiang ICML 2023 give \(\tilde O(\sqrt{nk})\) quantum coreset construction for \(k\)-clustering and list \(k\)-center / general metric variants as open directions, but they do not state this barcode theorem.
- Cheap falsification / minimum lemma:
  - Pin down the oracle model first. If “coherent coordinate access” means standard coordinate-by-index access, then implementing the predicate \(d(x,S)>\epsilon\) may already cost \(\Theta(d|S|)\) low-level queries, which can erase the advertised improvement.
  - If the intended model instead supplies unit-cost coherent distance or vector-load access, then the theorem becomes plausible.
- Risk: medium.
- Effort: 1–2 weeks for a clean theorem statement plus model audit.
- Verdict:
  - Not dead.
  - Not a big new TDA mechanism.
  - Best framed as a quantum \(\epsilon\)-net theorem whose barcode consequence is a corollary.
  - A companion 1D outlier lower bound via OR should be pursued immediately, since it likely gives \(\Omega(\sqrt n)\) quantum and \(\Omega(n)\) classical query lower bounds in the no-preprocessing model.

### 2. Quantum split search on bounded evaluated-Hom width

- Objective: rescue the Dey–Jendrysiak–Kerber line by replacing the false rank-1 update hope with the right structural parameter.
- Exact input / output / field:
  - Input: a minimal presentation over \(\mathbb F_q\), a fixed repeated grade \(\alpha\), an AIDA/ExtensionDecomp candidate graph on subspaces \(T \in \mathrm{Gr}_q(\kappa,\ell)\), and a promise that every adjacent move satisfies \(\operatorname{rank}\Delta \overline C_b \le r\) after the actual \(\alpha\)-local quotient.
  - Output: decide whether a splitting candidate exists and recover one if it does.
- Core mechanism:
  - Maintain the reduced consistency matrix \(\overline C_b(T)\) reversibly under Grassmann-neighbor moves.
  - Use an MNRS/Szegedy-type quantum walk or amplitude amplification over candidate subspaces.
- Closest collision:
  - Dey–Jendrysiak–Kerber already supply the exact split equations and major classical reductions.
  - Chistov–Ivanyos–Karpinski already give polynomial-time module decomposition over finite fields.
- Cheap falsification / minimum lemma:
  - Find one natural geometric class where \(r_{\mathrm{eval}}=O(1)\) or \(O(\log n)\) beyond the trivial interval case.
  - If every intended class still permits \(r_{\mathrm{eval}}=\Theta(\dim X_{b,\alpha})\), stop the quantum search route.
- Risk: medium-high.
- Effort: 2–4 weeks.
- Verdict: best Dey–Jendrysiak–Kerber-aligned theorem candidate.

### 3. \(\alpha\)-thin indecomposable class

- Objective: turn Candidate 2 from a promise problem into a natural theorem family.
- Exact input / output / field:
  - Input: finitely presented persistence modules over \(\mathbb F_q\) with the promise that every indecomposable target block relevant to the split test has \(\dim X_{b,\alpha}\le r\), for fixed small \(r\).
  - Output: exact decomposition or exact split detection.
- Core mechanism:
  - Prove a structural bound \(r_{\mathrm{eval}}\le g(r,\Delta_\alpha)\), where \(\Delta_\alpha\) measures how many source blocks can actually hit the \(\alpha\)-fiber.
  - Then Candidate 2 becomes a real algorithm theorem rather than a wish.
- Closest collision:
  - Dey–Jendrysiak–Kerber Theorem 23 is the \(r=1\) interval-style endpoint.
- Cheap falsification / minimum lemma:
  - Construct or search for a minimal geometric indecomposable with \(\dim X_{b,\alpha}=2\) but \(r_{\mathrm{eval}}=\Theta(t)\).
  - If such examples are generic, the class is too weak to matter.
- Risk: medium.
- Effort: 1–2 weeks for the structural lemma, then another 1–2 weeks for the algorithm.
- Verdict: best concrete companion to Candidate 2.

### 4. Restricted exact-kernel realization for normalized persistence

- Objective: attack the real missing theorem behind July 2026 normalized persistence, but only on a restricted verifier family.
- Exact input / output / field:
  - Input: a restricted history-Hamiltonian / verifier family with integer or inverse-polynomial coefficients and product-clock structure.
  - Output: a filtration-compatible clique pair \(G_1 \hookrightarrow G_2\) whose exact kernel multiplicities realize the intended valid-history subspace, over \(\mathbb C\).
- Core mechanism:
  - Convert coefficients into clique multiplicities or exact gadget counts.
  - Preserve the valid-history kernel under literal inclusion, not only up to low-energy approximation.
- Closest collision:
  - Lowe et al. July 2026 isolate this exact-kernel realization gap as the missing step.
  - June 2026 harmonic persistence and August 2026 unweighting supply ingredients but not this theorem.
- Cheap falsification / minimum lemma:
  - Build a toy two-level verifier gadget and test whether exact kernels survive inclusion without extra zero modes.
  - If even the toy model leaks kernel or changes the promise gap, stop.
- Risk: very high.
- Effort: 1–2 months minimum.
- Verdict: highest upside, but not the best first attempt unless normalized persistence is the main target.

### 5. Canonical-basis positive-guide lift

- Objective: remove the orientation-basis caveat from the current unweighting corollary.
- Exact input / output / field:
  - Input: a weighted harmonic-persistence instance over \(\mathbb C\) with an efficiently preparable guide in the source orientation basis.
  - Output: an unweighted filtered clique instance with a strictly positive uniform guide in a fixed canonical sorted basis.
- Core mechanism:
  - Add a sign-absorbing lift or orientation-doubling gadget so the signed cycle becomes a positive subset state in a larger complex.
- Closest collision:
  - June 2026 allows arbitrary fixed simplex orientations, so positivity in one canonical basis is not covered there.
  - The local corollary preserves source conventions only.
- Cheap falsification / minimum lemma:
  - Try to lift a single oriented 1-cycle to positive amplitudes without creating spurious harmonic states.
  - If that already fails, the theorem is probably dead.
- Risk: high.
- Effort: 2–3 weeks for a real go/no-go.
- Verdict: useful side theorem if it works, but probably not the main paper.

### 6. Evaluation-faithful \(\alpha\)-endomorphism lifting

- Objective: bypass candidate-subspace enumeration entirely by solving decomposition inside an \(\alpha\)-local endomorphism algebra.
- Exact input / output / field:
  - Input: a persistence module over \(\mathbb F_q\) with the promise that evaluation \(\operatorname{End}(X)\to \operatorname{End}(X_\alpha)\) has controlled kernel and primitive idempotents lift faithfully.
  - Output: a nontrivial direct-summand decomposition.
- Core mechanism:
  - Work in a compressed algebra visible at \(\alpha\), search for primitive idempotents there, and lift them back.
- Closest collision:
  - Classical finite-dimensional algebra decomposition over finite fields is already strong.
  - AIDA’s automorphism-invariant reductions are already exploiting local endomorphism structure.
- Cheap falsification / minimum lemma:
  - Produce a natural geometric class where evaluation hides no summands.
  - If hidden summands are generic, the whole approach collapses.
- Risk: high.
- Effort: 3–5 weeks.
- Verdict: elegant, but very exposed to “this becomes classical algebra.”

### 7. Quantum fold-back counting under bounded duplication rank

- Objective: stay closer to Dey–Xin unfolding rather than AIDA.
- Exact input / output / field:
  - Input: a finite-poset simplicial filtration over a field \(F\), together with the unfolded zigzag full intervals and a promise that each candidate interval hits at most \(\rho\) duplicated originals and induces a fold-back system of rank at most \(r\).
  - Output: count the foldable full intervals, i.e. compute generalized rank.
- Core mechanism:
  - Make the fold-back test an exact small-rank verifier and use quantum counting over candidate intervals.
- Closest collision:
  - Dey–Xin unfolding already gives strong classical algorithms, especially in graph and top-dimensional special cases.
- Cheap falsification / minimum lemma:
  - Write the per-interval fold certificate explicitly.
  - If a classical streaming check is already \(O(\rho r)\) with small constants, the quantum gain is too thin.
- Risk: high.
- Effort: 1–2 weeks.
- Verdict: direct continuity with Dey–Xin, but low confidence.

### 8. Bounded-overlap interval-decomposability

- Objective: look for a genuinely structured interval-decomposability theorem rather than a blind speedup of the known cubic algorithm.
- Exact input / output / field:
  - Input: a persistence module over \(\mathbb F_q\) whose \(\alpha\)-Hom overlap graph has bounded treewidth or degeneracy.
  - Output: decide interval-decomposability and recover the decomposition.
- Core mechanism:
  - Reduce AIDA’s local choice structure to a bounded-width dynamic program and speed up only the ambiguous branch exploration quantumly.
- Closest collision:
  - Dey–Jendrysiak–Kerber already have an \(O(N^3)\) interval-decomposable algorithm.
- Cheap falsification / minimum lemma:
  - Prove the reduced state really is local graph structure rather than disguised dense elimination.
  - If not, stop.
- Risk: medium-high.
- Effort: 2–3 weeks.
- Verdict: plausible parameterized problem, but quantum content may be secondary.

### 9. Sparse convertibility-matrix quantum verifier

- Objective: formulate a truly sparse exact linear-algebra core for fold-back rather than generic projector overlap.
- Exact input / output / field:
  - Input: an unfolded candidate interval and a sparse convertibility / fold-back matrix over \(F\).
  - Output: decide whether the interval survives fold-back.
- Core mechanism:
  - Block-encode the sparse matrix and use singular-value thresholding or exact linear-system verification.
- Closest collision:
  - Dey–Xin’s fold-back and convertibility machinery already exists classically.
  - Generic QLSA/QSVT would be an obvious reviewer objection.
- Cheap falsification / minimum lemma:
  - Show the sparse formulation is exact, natural, and not destroyed by conditioning.
  - If dense conversion or bad conditioning dominates, stop.
- Risk: high.
- Effort: about 2 weeks for a first honest check.
- Verdict: lowest-ranked surviving candidate.

## What I would actually try

### If clean quantum-TDA approximation is enough: try Candidate 1 first

Reason: after the correction, this is the clearest surviving theorem candidate. But I would frame it honestly as a quantum \(\epsilon\)-net theorem plus a barcode corollary, not as a brand-new persistence mechanism.

### If continuity with Dey–Xin / Dey–Jendrysiak–Kerber is mandatory: try Candidate 2 immediately paired with Candidate 3

Reason: this is still the cleanest direct continuation. But I would not attempt a quantum walk theorem abstractly; I would first search for a natural \(r_{\mathrm{eval}}\)-bounded class, because otherwise the whole route is just a renamed dead end.

### Try Candidate 4 only if the objective shifts toward harder quantum complexity

Reason: highest upside, but much larger proof commitment.

## Ideas I would not spend time on now

1. Common-multiplicity filtered unweighting as a standalone paper claim: too likely a direct corollary.
2. Variable-weight nested-copy unweighting in the naive form: already killed by the one-vertex \(1\to 2\) multiplicity incompatibility.
3. Any raw-projector generalized-rank algorithm under local gap promises: killed by the Möbius zigzag family.
4. Any proposal whose core sentence is just “apply Grover to candidate intervals / neighbors / subspaces”: not enough structural novelty.
5. Graph \(H_1\) or top-dimensional unfolding speedups: the classical baselines are already too strong.
