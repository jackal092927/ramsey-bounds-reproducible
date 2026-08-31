# Round 1 Review

- Reviewer: external Claude, high-rigor ITCS/quantum-algorithms review
- Thread ID: `df228155-1ecb-48f9-aeb5-1ecdb010f6c7`
- Overall score: 4.2/10
- Verdict: RETHINK as a Ramsey paper; REVISE as quantum constructive LLL for implicit event families

<details>
<summary>Full raw reviewer response</summary>

## Reviewer Report — ITCS 2027

*Scope note: I reviewed the proposal text as submitted. I had no file access in this session, so my comments on the repository's existing exact-seven / R(3,18) assets rely on the session context you provided, not on inspection.*

---

### Summary of position

The proposal is unusually self-aware — it correctly names its own fatal objection ("This is Moser–Tardos plus Grover"), correctly refuses to let experiments stand in for proofs, and correctly quarantines the topology material. Those are the marks of a serious author. But self-awareness is not a theorem. As of today there is no theorem, no citation, no oracle circuit, no error schedule, and no access model. What is proposed is, on its stated technical content, exactly the composition the author fears.

I first verified the combinatorics you did state, because they carry the argument. `p = 2^{1-\binom k2}` is right (two colors × `2^{-\binom k2}`). The dependency count `d = \sum_{j=2}^k \binom kj\binom{n-k}{k-j} - 1` is right, dominated by `j=2`, so `d = \Theta(k^2\binom{n-2}{k-2})`. Good. Now push it one step further, which the proposal does not do, and the picture changes materially.

**The target bound is self-defeating in the LLL regime.** The LLL condition `ep(d+1)\le 1` forces `d \approx 1/(ep)`. Moser–Tardos gives `R \le \sum_A x_A/(1-x_A) \approx emp`, so `R \approx m/d`. Substituting into your own displayed target:

- classical implicit MT with a lazy dirty-set structure: `\Theta((m + Rd)q) = \Theta(mq)`
- your quantum target: `\widetilde O((\sqrt m + R\sqrt d)q) = \widetilde O((m/\sqrt d)q)`

So the entire claimed advantage is a factor of `\sqrt d` in the inner loop, obtained by putting Grover inside the repair loop. The `\sqrt m` term is not even the binding one (`m/\sqrt d > \sqrt m` whenever `m>d`, which is always here). You have written down a target whose only content is "Grover the neighborhood search." A referee will compute this in ten minutes and reject on novelty. **Compute this substitution yourself before you write another line** — it tells you where the real theorem has to live, and it is not where you put it.

**Second, the mathematical payoff is zero and the proposal doesn't say so.** Spencer's 1975 LLL bound improves Erdős's union bound for diagonal Ramsey by a factor of 2, and the diagonal lower bound has not moved by more than a constant since. Constructivizing a fifty-year-old bound that is astronomically far from the truth is not a contribution to Ramsey theory, and the off-diagonal picture is worse now that Mattheus–Verstraëte have pinned `r(4,t) = t^{3+o(1)}` by methods that have nothing to do with LLL. Ramsey here is a costume worn by "implicit-event constructive LLL." That is a legitimate paper — but you must name it as such, or a referee will name it for you, less kindly.

**Third, the missing prior art is disqualifying at present.** The proposal contains zero citations while making novelty claims. The specific bodies you must confront, and which a referee will supply if you don't:

- *Direct quantum Ramsey.* Gaitan & Clark, PRL 108, 010501 (2012); Bian–Chudak–Macready–Clark–Gaitan, PRL 111, 130505 (2013); the Grover-based follow-ups in PRA. Also Rydberg-array MIS work (Ebadi et al., *Science* 2022) — a referee will ask why independent-set hardware isn't the natural comparison for `R(3,k)`.
- *Classical implicit/lazy LLL — your real baseline.* Chandrasekaran–Goyal–Haeupler (SODA 2010) already handle exponentially many events; Harvey–Vondrák (FOCS 2015) already frame LLL through *resampling oracles*, which is precisely your "implicit event access" framing; Achlioptas–Iliopoulos–Kolmogorov give the flaws/actions framework that legitimizes an arbitrary (including randomized, including quantum-returned) flaw-choice strategy. That last one is *good news for you* — it means your measured-flaw selection is covered — but you must cite it rather than reprove it.
- *Quantized local search, which is your true precedent.* Ambainis's quantum speedup of Schöning's random walk for 3-SAT is the canonical "amplitude-amplify a resampling process" result. Any quantum-MT paper lives or dies on distinguishing itself from it.
- *Composition tools you'll be accused of merely invoking.* BBHT for unknown solution counts; Høyer–Mosca–de Wolf for search on bounded-error inputs (this is the off-the-shelf answer to your proof obligation #2, and it is a citation, not a theorem); Ambainis's variable-time amplitude amplification.

---

### Two technical holes that decide whether the paper exists

**(a) The access model is not a detail — it is the paper.** Each flaw check reads `\binom k2` edges of a *mutating* string `x \in \{0,1\}^{\binom n2}`. Without QRAM, a coherent query costs `\widetilde\Theta(n^2)` gates and the speedup evaporates. With QRAM, ITCS referees are now openly hostile to the accounting. There is a clean way out that you should elevate to a lemma: **MT never needs `x` explicitly.** Represent `x` as (random seed, sparse update log of resampled edges). The log has size `O(Rk^2)`, not `\Theta(n^2)`, so coherent access needs only a small lookup structure plus one call to the randomness. This converts an embarrassing assumption into a stated model with a proof, and it connects naturally to the limited-independence derandomizations of LLL. This is the most valuable single suggestion in this report.

**(b) Superposition over `k`-subsets can silently eat the entire speedup.** If you prepare a uniform superposition over ordered `k`-tuples in `[n]^k`, only a `k!/k^k \approx e^{-k}` fraction are sorted and distinct, so amplitude amplification pays `e^{k/2}`. In the regime that makes Ramsey interesting, `k = \Theta(\log n)`, that is a `\mathrm{poly}(n)` factor — enough to erase the claim. You need the uniform superposition over `\binom nk` subsets exactly. Cite Bärtschi–Eidenbenz on deterministic Dicke-state preparation (`O(kn)` gates), or give a reversible combinatorial-number-system unranking circuit with explicit ancilla cleanup. Either way, state it. A referee who notices this before you do will conclude you never costed your own oracle.

**On proof obligation #3, the answer is yes, and you should just prove it.** Exact (zero-error) certification that no flaw remains requires `\Omega(m)` queries — the unstructured-OR lower bound. So end-to-end *certified* Ramsey construction is `\Theta(mq)` no matter what you do quantumly. This is a small theorem, it is honest, and it sharpens the paper by delimiting the model rather than hiding the problem. State the construction theorem in the bounded-error output model (standard sublinear-algorithms convention) and prove the `\Omega(m)` certification barrier as a companion. Do not leave this as an open worry in the text.

---

### Scores

Weights: Contribution 0.25, Specificity 0.20, Frontier 0.13, Fidelity 0.12, Feasibility 0.10, Validation 0.10, Venue 0.10.

| # | Criterion | Score |
|---|---|---|
| 1 | Problem Fidelity | 6 |
| 2 | Method Specificity | 4 |
| 3 | Contribution Quality | 3 |
| 4 | Frontier Leverage | 4 |
| 5 | Feasibility | 5 |
| 6 | Validation Focus | 7 |
| 7 | Venue Readiness | 2 |

**OVERALL (weighted): 4.2 / 10**

---

### Weaknesses, fixes, priority

**1. Problem Fidelity — 6**
*Weakness:* The anchor problem, as posed, has no mathematical consumer. LLL-Ramsey lower bounds are a factor of 2 off a 1935 union bound and have been static since 1975; making them constructive advances nothing in Ramsey theory. Meanwhile the paper's own certification section concedes that any actual published bound needs a `\Theta(m)` classical check. The proposal never resolves this tension — it names it and moves on.
*Fix:* Retitle and reframe: *"Quantum speedups for constructive LLL over implicit event families,"* with diagonal/off-diagonal Ramsey as the running instance because its event family is implicit, huge, and has exactly computable `m, d, p`. State in the introduction, in one sentence, that no new Ramsey bound is claimed and why. Paradoxically this raises fidelity, because the theorem then matches the problem it actually solves.
*Priority:* **High** — costs one hour, removes the "so what" rejection.

**2. Method Specificity — 4**
*Weakness:* The one novel component, "dependency-aware repair scheduling," is never defined. There is no scheduler, no walk, no unranking circuit, no per-call error schedule, no ancilla accounting. The single displayed bound is explicitly disclaimed as not a theorem, and (per the substitution above) is a bound whose content is one Grover call per repair.
*Fix:* Commit to one mechanism and specify it fully. My recommendation: **MNRS quantum walk with cheap updates over the dirty set.** MT is precisely a sequence of *local* modifications to a database — each resample dirties `\le d` events — which is the canonical setting where a walk with update cost `U \ll` setup cost `S` beats re-running Grover from scratch. Restarting Grover after every repair (your current design) throws away exactly the structure that would make this not-a-composition. A bound of the shape `\widetilde O(\sqrt m + R\cdot d^{1/3}\cdot q)`, beating `R\sqrt d`, would be a genuine theorem. Write the walk, the setup/update/check costs, and the ancilla cleanup explicitly.
*Priority:* **Critical** — this is the paper.

**3. Contribution Quality — 3**
*Weakness:* No theorem exists, and the theorem most likely to be proved on the current design is a composition of Moser–Tardos with Grover plus Høyer–Mosca–de Wolf error handling. Under the review standard you were given, that is a rejection.
*Fix:* Aim for **one** of three, not all: (i) the walk-amortized upper bound above; (ii) a **matching quantum lower bound** `\Omega(R\sqrt d)` in the flaw-oracle model — a tight characterization is ITCS-worthy even when the upper bound is routine; (iii) the high-upside reframe: a **quantum local computation algorithm for LLL** — answer "what is the color of edge `e` in the MT output?" in `\mathrm{poly}(d)` time without materializing the coloring. Option (iii) sidesteps the `\Theta(m)` certification barrier entirely, opens a new model question rather than optimizing an old constant, and lands in the live classical LCA-LLL / distributed-LLL literature (Rubinfeld–Tamir–Vardi–Xie; Chung–Pettie–Su; Fischer–Ghaffari) next to the active quantum-LOCAL advantage debate (Le Gall–Nishimura–Rosmanis; the recent no-advantage results for approximate coloring). That is ITCS's taste exactly. I would pursue (i) as the technical core and (iii) as the framing, with (ii) as the fallback if (i) resists.
*Priority:* **Critical.**

**4. Frontier Leverage — 4**
*Weakness:* Every primitive named — MT (2010), amplitude amplification (1997), Grover — is decades old, and the genuinely modern tools that fit this problem are absent: MNRS walks with update/setup asymmetry, variable-time AA over cost-stratified events, resampling-oracle LLL, Haeupler–Harris concentration for the resampling count (which you need for an adaptive error budget over an unknown-length run), Ambainis–Kokainis tree-size estimation on the Route B side.
*Fix:* Add a two-page related-work section built around the four clusters listed earlier, and let it drive the design rather than defend it. Specifically, replace "repeat Grover until no flaw" with a variable-time analysis: early in the run many flaws exist, so BBHT finds one in `\widetilde O(\sqrt{m/t_i})`; the new combinatorial lemma you'd need is a bound on the *flaw-count trajectory* `\{t_i\}` of MT, which classical witness-tree analysis does **not** give you (it bounds total resamplings, not simultaneous violations over time). That lemma is real, provable, and not a corollary of anything cited above.
*Priority:* **High.**

**5. Feasibility — 5**
*Weakness:* Feasible as a 3–6 month project; not feasible as stated. The proposal's own gate — "conditional go only if a formal theorem and proof skeleton exist by September 1, 2026" — is tomorrow, and no theorem exists today. Separately, the highest-risk item (access model) is one you have flagged but not resolved, and it is binary: resolve it wrong and there is no result.
*Fix:* Kill the ITCS gate now (see deadline recommendation) and re-sequence: week 1, access-model lemma + Dicke/unranking oracle + the `\Omega(m)` certification bound (all three are within reach and are the paper's foundation); weeks 2–5, the walk-amortized theorem; week 6, lower bound or LCA reframe.
*Priority:* **Medium** — the plan is executable, just not on this calendar.

**7. Venue Readiness — 2**
*Weakness:* Four days out with zero theorems, zero citations, and an unresolved access model. An ITCS submission in this state would be desk-level rejected on related work alone, and would burn the idea's first impression with a PC that will likely overlap with the venue you actually want.
*Fix:* Do not submit. See below.
*Priority:* **Critical.**

*(Validation Focus, 7 — no fix required. This is the strongest section: you name "independent global Grover calls" as a baseline, which is the correct adversarial comparison and the one most authors omit; you count reversible gates and total failure probability, not just query counts; and you require independent classical checking of any returned witness. Keep it as written.)*

---

### Simplification Opportunities

1. **Delete Route B entirely from this paper.** Montanaro finding is `\widetilde O(\sqrt T D^{3/2})` — you quoted it correctly — but with `\sim 5\times 10^{13}` surviving index sets in your current exact-seven branch, `\sqrt T` is still astronomical and the coherence requirement is fantasy. Route B is a separate classical paper about a real artifact. Merging them halves the credibility of each.
2. **Delete the topology section, including the excluded version.** A paragraph explaining what you are *not* doing with the clique complex and Johnson graph reads as an idea you couldn't part with. If the MNRS walk lands, the Johnson-graph structure returns as machinery inside a theorem, which is the only way it should appear.
3. **Drop "dependency-aware repair scheduling" as an independent contribution.** Achlioptas–Iliopoulos–Kolmogorov already licenses arbitrary flaw-choice strategies, so scheduling freedom is inherited, not invented. Cite it and spend the saved space on the walk.
4. **Collapse the six-step system overview to three:** implicit-access model, walk-based flaw finder, classical resample. Steps 5 and 6 are the certification boundary and belong in the theorem statement's model, not in the algorithm.
5. **One theorem, one instance, one baseline.** Resist stating the framework for general flaw systems *and* instantiating for Ramsey *and* running the finite benchmark. Prove it for the implicit-Ramsey instance; remark that it generalizes.

---

### Drift Warning

Three drift vectors, in order of danger:

**Gravitational pull toward the existing asset.** Your repository's genuine, hard-won work is the classical exact-seven / `R(3,18)` pipeline — CNF refutations, no-good propositions, degree conditions, DRAT checking. That work is real and the quantum proposal is not, which means every hour of difficulty on the quantum side will push you toward "let me just add a quantum section to the search paper." Route B is already the visible seam. Watch for it.

**Drift from theorem to demo.** The proposal defends against this well on paper, but the compute plan ("10–20 logical qubits, hours to a few days") is the cheapest thing in the project and the theorem is the most expensive. Under deadline pressure the cheap thing gets done. If by Sept 3 you have circuit simulations and no theorem, you have drifted, regardless of what the plan said.

**Drift from a bound to a bound-shaped expression.** The displayed target `\widetilde O((\sqrt m + R\sqrt d)q)` is labeled "not an established theorem," which is honest — but it is also, per the substitution above, not a *target worth establishing*. There is a failure mode where you spend three weeks rigorously proving the thing you already guessed, and it is a composition. Re-derive the target under `ep(d+1)\le 1` before committing.

---

### Verdict

**RETHINK** as a Ramsey paper. **REVISE** as "quantum constructive LLL for implicit event families," which is a real paper that does not yet exist in draft form.

The idea is not dead — the implicit-event angle is correct, the access-model observation is genuinely reusable, and the LCA reframe is an opening rather than an optimization. What is dead is the September timeline.

---

### Hard ITCS deadline recommendation

**Do not submit to ITCS 2027.** Do not register the September 2 abstract.

The conditional-go gate in your own proposal fires tomorrow and will fire negative. Even in the best case — you prove the `\widetilde O(q(\sqrt m + R\sqrt d))` bound cleanly in 72 hours — the headline is a composition of two textbook results, submitted with a related-work section written in a panic, to a PC that specifically prizes conceptual novelty. I would put acceptance below 10%, and the cost of a rejection is not only the rejection: ITCS and the quantum-algorithms venues share reviewers, and a "MT + Grover" first impression follows the idea.

**Recommended sequence instead:**

- **Sept 1–14:** the three foundation results — sparse-update-log access model, exact `k`-subset oracle with reversible cleanup and gate count, `\Omega(m)` exact-certification lower bound. All three are provable in two weeks and none of them is the risky part.
- **Sept 15–Nov:** the MNRS walk-amortized theorem, or the lower bound, or the quantum-LCA-for-LLL reframe. Pick by mid-October based on which is yielding.
- **Target a spring 2027 deadline** — ICALP, STACS, or a quantum-specific venue depending on how the result lands. *Verify current dates yourself; I'm not confident in specific 2027 CFP deadlines.*
- **If the walk theorem lands by December,** ITCS 2028 is the natural home, with a year of prior-art work behind it instead of four days.

Separately and in parallel: the exact-seven branch-1 material is closer to publishable than anything in this proposal. If you want something submitted this autumn, that is the manuscript to finish — the three blockers already identified there (independent CNF parse, soundness lemma, one-way implication fix) are days of work, not months.

</details>

