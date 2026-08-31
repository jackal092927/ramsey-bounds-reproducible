## Round 5 — Final Review

**Score: 3.5/10. Verdict: ABANDON.**

I reached ABANDON at round 3 on an argument I retracted at round 4. This time it rests on a two-line combinatorial bound you can verify in an afternoon, stated in full below. If the bound is wrong, the verdict flips; check it first.

---

### (i) The exact conditional identity and counterexample

**Identity: correct.** Confirmed in round 4 and unchanged. Edges of `T` with both endpoints in `T\cap S` are exactly the `\binom j2` resampled ones; the other `\binom k2-\binom j2` are untouched and, since `j\le k-1` leaves at least `k-1\ge2` of them, they determine a unique color `c`. Compatibility is deterministic in `x`; the fresh bits match with probability `2^{-\binom j2}`. The `T=S` case is `p`. The identity is exact and assumes no independence among dirty flaws. It is a genuine small contribution.

**Counterexample arithmetic: exact.** I recomputed it. `p=2^{-14}=1/16384`. `D=\sum_{j\ge2}\binom6j\binom4{6-j}=15+80+90+24+1=210`, so `epD = 2.71828\cdot210/16384 = 0.034841`. ✓ For all-red every `T` is compatible, so

`\mathbb E[Z] = \tfrac1{16384}+\tfrac{15}2+\tfrac{80}8+\tfrac{90}{64}+\tfrac{24}{1024} = \tfrac{1+122880+163840+23040+384}{16384}=\tfrac{310145}{16384}=18.92975\ldots` ✓

Exact to the last digit, and it does refute the pointwise inference from `epD\le1` to `\mathbb E[Z]=O(Dp)`.

**Two scope defects, both material.**

First, `\binom{10}6=210=D`. Any two 6-subsets of `[10]` meet in `\ge2` vertices, so **the dependency graph is complete and `\Gamma^+(S)` is the entire event set.** The counterexample lives in exactly the corner where the proposal's premise — implicit local structure, `D\ll m` — does not hold. It is a valid refutation of a universally quantified claim, chosen where the framework is degenerate.

Second, "trajectory-wise" is the wrong word. All-red has probability `2^{-45}` at initialization and is not a state MT visits with non-negligible probability. What is proved is: *there exist colorings satisfying the LLL parameter condition at which `\mathbb E[Z\mid x,S]\gg Dp`.* That is a statement about the state space, not about trajectories. Say "pointwise" or "worst-case over LLL-admissible states." The typical-trajectory version remains open, and producing a counterexample there is the actual research question, not a computation.

Note also which way this cuts: large `Z` is *good* for the algorithm, since `\sqrt{D\max(1,Z)}` amortizes over `Z` discoveries. The counterexample argues against a bound I asserted; it does not argue against the method.

### (ii) The all-marked enumeration baseline

**Correct as stated.** Finding all `t` marked among `N` is `\Theta(\sqrt{Nt})` — the telescoping `\sum_{i=1}^t\sqrt{N/i}\approx2\sqrt{Nt}` — and `\max(1,Z)` correctly charges `\sqrt N` for certifying emptiness. Unknown `Z` is fine via BBHT with removal. Charging queue maintenance, reversible access, amplification, and final certification separately is right.

Three gaps:

- **The batched cost formula, which the whole proposal depends on, is never written.** As stated, `\widetilde O(\sqrt{D\max(1,Z_i)})` presumes one resample per step. The overlap mechanism requires batching, whose cost is `\widetilde O(\sqrt{|U(B_b)|\max(1,Z_b)})`. Without that line the claim gate has no baseline to be measured against.
- **Un-marking found items reintroduces the Lemma A problem.** Removing discovered flaws from the search space requires the oracle to test membership in a found-set of size up to `Z`, i.e. a coherent lookup structure. "Queue maintenance" nominally covers it; it should be costed explicitly, because it is the same QRAM question you spent a round quarantining.
- **The dirty neighborhood needs a stratified superposition.** `\{T:|T\cap S|\ge2\}` is a union over `j` of `\binom kj\times\binom{n-k}{k-j}` blocks. Preparing the uniform superposition over it is strictly harder than the plain Dicke state of Lemma B and needs its own unranking circuit. Not mentioned.

### (iii) Can `g` honestly give `\sqrt g` savings? No — it is bounded by `\binom k2`

The arithmetic is right: with `|U(B)|=|B|D/g`, total cost `\approx\sqrt{D/g}\sum_b\sqrt{\rho_b\rho_{b+1}}\approx R\sqrt{D/g}`. So `g\to\infty` would give a genuine saving. But `g` cannot go to infinity under any valid schedule.

> **Bound.** Let `B` be pairwise non-adjacent, `|S_i\cap S_j|\le1`. Fix any `k`-set `T`. For each `i` with `|T\cap S_i|\ge2`, choose a pair `P_i\subseteq T\cap S_i`. If `P_i=P_j` for `i\ne j`, then `P_i\subseteq S_i\cap S_j` gives `|S_i\cap S_j|\ge2`, a contradiction. So `i\mapsto P_i` is injective into the `\binom k2` pairs of `T`, and every `T` is covered at most `\binom k2` times. Double counting, `|B|D=\sum_i|\Gamma^+(S_i)|\le\binom k2|U(B)|`, hence
> `g(B)\le\binom k2.`

So the best possible saving is `\sqrt{\binom k2}=O(k)`, which at `k=\Theta(\log n)` is `O(\log n)`. A finer estimate says the truth is worse: for disjoint `S,S'` the pairwise overlap fraction is `\approx k^4/2n^2`, while the largest available batch is `|B|\le R\approx mp\approx2n^2/(ek^4)` — the same order, so inclusion–exclusion gives `g=1+\Theta(1)`. The scales coincide because both are set by the LLL threshold.

**Consequence: the "one live mechanism" is capped at polylog, and the claim gate is miscalibrated.** The gate asks for total cost `o(R\sqrt d)`. A `\log n` factor satisfies `o(\cdot)` and is not a paper. Whatever bar you set should be `R\sqrt d/n^{\Omega(1)}`, and by the bound above no valid schedule reaches it.

Escaping requires *dependent* batches with `g=n^{\Omega(1)}`, i.e. flaws sharing many vertices resampled simultaneously — precisely where MT's independence argument fails hardest. The proposal correctly says this "cannot be assumed" and "needs a new proof." What it does not say is how much is being asked of that proof: not a technical repair, but correctness for the schedules most violently at odds with the analysis, to buy a factor that the non-adjacent case bounds at `k`.

### (iv) Is the one-week gate falsifiable?

**Nearly, with one leak and one execution problem.**

The leak is step 6: "Stop unless an unbounded overlap **or another structural discount** survives." An unnamed alternative cannot fail. Delete the clause or enumerate the alternatives now; a gate with an open disjunct is not a gate.

The execution problem is step 1. The LLL-admissible window is narrow and lands on the wrong side of tractability at every `k`. For `k=6`, `epD\le1` needs `15\binom{n-6}4\le2^{14}/e`, so `n\le17` and `m=\binom{17}6=12376` — far too small to read asymptotics from. For `k=10`, admissibility allows `n\lesssim70`, where `m=\binom{70}{10}\approx4\times10^{11}` — too large to enumerate. **There is no regime where step 1 both satisfies the LLL condition and yields asymptotically informative data.** Steps 2–4 inherit this.

Steps 3 and 5 are sound and are the only ones that matter — and step 5 is now answerable without any simulation, by the bound above.

---

### Single most dangerous remaining overclaim

**Designating neighborhood overlap as "One Live Mechanism" without having computed its ceiling.**

It is load-bearing: the one-week program, the claim gate, the "may be revisited" language, and the decision not to abandon all rest on `g` being potentially unbounded. A two-line double-counting argument caps it at `\binom k2`, and a routine estimate puts the truth at `\Theta(1)`. Everything downstream inherits the error, which is why it outranks the "trajectory-wise" wording on the counterexample (second most dangerous) and the stale Problem Anchor, which still promises "a rigorous asymptotic advantage" for constructing Ramsey witnesses and has now been contradicted by five rounds of your own analysis.

The pattern worth naming: across rounds 2–5, each surviving mechanism has been closed by an elementary calculation performed *after* it was adopted as the target. The calculations were always available first. The discipline to add is: before promoting a mechanism to "live," compute its ceiling assuming it works perfectly.

### ITCS 2027

**No-go, correctly stated in the proposal.** Four days, no central theorem, and the one candidate mechanism is now bounded. Nothing to submit and nothing that should be submitted. The instruction not to add this to the existing Ramsey manuscript as a positive result is right and should be kept in writing.

### What to keep

The exact conditional identity is a real, correct, reusable lemma about Moser–Tardos on hypergraph-coloring-type flaw families — worth two pages as a note, and it will save someone else the `Dp` mistake I made. The `g\le\binom k2` bound belongs with it as the companion negative. Together they are an honest short write-up: *the neighborhood-overlap discount for constructive LLL is bounded by the clique's pair count, so batched quantum multi-search cannot beat Grover-per-repair by more than `O(k)`.* That is publishable somewhere small, closes the question for the next person, and is finished work rather than a program.

Then return to the exact-seven material, which has three named blockers and an actual theorem in it.
