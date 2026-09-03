# Quantum hyperbolic LSH: bounded feasibility probe

Date: 2026-09-02. Status: primary-source triage plus an independently derived generic baseline; no novelty or full-proof claim.

## Verdict

**NO-GO for a paper whose contribution is “quantize hyperbolic LSH/HNSW by Grover.” NARROW only to growing-dimensional hyperbolic filtering with an explicit access model and a genuinely geometric sampler or tradeoff theorem.**

The same fixed-dimensional ANN problem already admits logarithmic classical query time and linear space. The elementary quantum hash-table tradeoff below is real under QRACM, but generic. The immediate next step is a small collision-model lemma, not an experiment or a paper draft.

## Source map

| Primary source | Verified result or relevant collision | Scope |
|---|---|---|
| Deng, Gao, Lu, Luo, Xin, [Locality Sensitive Hashing in Hyperbolic Space, SoCG 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2026.39) | States rho <= 1/c in H^2 and rho <= 1.59/c in H^d; construction normalizes geodesics intersecting a containing ball. | Data-oblivious hashing. See model caveat below before importing the high-dimensional statement. |
| Kisfaludi-Bak and van Wordragen, [A Quadtree, a Steiner Spanner, and Approximate Nearest Neighbours in Hyperbolic Space, SoCG 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2024.68) | (1+epsilon)-ANN, O_{d,epsilon}(n) space, O_{d,epsilon}(log n) query/update, O_{d,epsilon}(n log n) build. | Worst-case finite point sets, fixed dimension/accuracy; hidden dependence is d^{O(d)} log(1/epsilon)/epsilon^d. |
| Laarhoven, Mosca, van de Pol, [Finding shortest lattice vectors faster using quantum search, DCC 2015](https://link.springer.com/article/10.1007/s10623-015-0067-5) | Quantum search of LSH candidate lists and reoptimized time-space tradeoffs. | Lattice sieving; distinguish proved algorithms from heuristic spherical-distribution analyses. |
| Kirshanova, Martensson, Postlethwaite, Roy Moulik, [Quantum Algorithms for the Approximate k-List Problem and their Application to Lattice Sieving](https://crypto-kantiana.com/elena.kirshanova/Papers/quantum_sieving.pdf), Appendix B, Algorithm B.1/Theorem 9 | Explicitly enumerate relevant filters, prepare their bucket-union state, then Grover/enumerate matches. Query cost = filter enumeration + square root of candidate-count times output-count. | Iid uniform sphere points, list size exponential in dimension, quantumly addressable classical memory. Not a worst-case hyperbolic theorem. |
| Chailloux and Loyer, [Lattice sieving via quantum random walks, ASIACRYPT 2021](https://arxiv.org/abs/2105.05608) | Adds an LSF layer inside a quantum walk, improving heuristic sieve exponent 0.2653 to 0.2570. | A genuine beyond-naive-Grover structural precedent, not a hyperbolic ANN result. These are historical, not asserted current-best, exponents. |
| Cho, Hhan, Kim, Lee, Shen, [Does quantum lattice sieving require quantum RAM?, 2024 preprint](https://arxiv.org/html/2410.15565v1), Theorems 4.2–4.6 | Explicit QRAM/time interpolation; efficient coherent sampling of query-relevant product-code filters permits further acceleration. Model-specific no-QRAM lower bounds. | The lower bound cannot simply be transferred to arbitrary ANN. The sampler and memory accounting are the useful methodological precedent. |
| Xue et al., [Near-Optimal Quantum Coreset Construction Algorithms for Clustering, ICML 2023](https://proceedings.mlr.press/v202/xue23a/xue23a.pdf), Lemma 3.4 | Coherent constant-factor ANN mapping with polynomial preprocessing/QRAM and polylogarithmic query overhead. | Shows “put classical LSH into a coherent oracle” is itself established; approximation 2.5–3, Euclidean setting. |

The 2026 hyperbolic paper also explicitly notes exact H^2 nearest neighbor via Voronoi point location in O(log n) query and O(n) storage. Thus an n^{positive constant} query is not a best-ANN improvement in H^2. Fixed d has the same obstacle by SoCG 2024. Growing d is necessary, not sufficient, for a credible target.

## Honest generic quantum baseline (derived here; not claimed new)

Assume a valid (r,cr,p1,p2)-sensitive family on the entire promised data/query domain, p1>p2, independent hash tables, reversible distance comparison, and QRACM access to stored bucket entries. Let tau_h be one base-hash cost and tau_d one distance-check cost. The classical comparator may use exactly the same preprocessing and stored data.

Concatenate k base hashes, use L = ceil(a p1^{-k}) independent tables for a constant a. A fixed r-neighbor is in at least one queried bucket with probability at least 1-exp(-a). Let F be the number of bucket entries farther than cr from q, counting duplicates. Then

    E[F] <= n L p2^k.

Compute the L query hashes, bucket pointers, sizes and prefix lengths classically. This costs O(k L tau_h + L polylog(nL)), not the cost of materializing all candidates. Place the O(L) query-specific pointer/prefix metadata in QRACM. A coherent binary search through prefix lengths maps a candidate index to its table, offset and stored point in polylog(nL) overhead.

Let G be the number of acceptable entries and S=F+G. On the near-hit event, G>=1. Unknown-success quantum search costs O(sqrt(S/G)) checks, and

    S/G = 1+F/G <= 1+F.

Markov's inequality plus a suitable constant cutoff gives constant overall success with

    T_Q = O_tilde(k L tau_h + tau_d sqrt(1+n L p2^k)).
    Space = O(nL + hash-description storage + nd),
    classical build = O_tilde(n k L tau_h).

This handles arbitrary bucket imbalance without pretending that all buckets have their expected size. Empty/no-good buckets and absent neighbors cannot create false positives because distance is verified. Standard repetition raises success probability.

Writing rho=log(1/p1)/log(1/p2), choose (up to ceilings)

    k = log n / log(1/(p1 p2)),
    L = n^{rho/(1+rho)},
    n L p2^k = n^{2rho/(1+rho)}.

Ignoring only genuinely subpolynomial oracle factors gives query exponent rho/(1+rho), space exponent 1+rho/(1+rho). These clean exponents assume fixed p1,p2, or that integer-rounding factors and k remain subpolynomial; otherwise use the unabridged bound. This improves the usual n^rho-query LSH implementation, and the same-index classical candidate scan has n^{2rho/(1+rho)} expected far work. It is NOT a lower bound against the best classical ANN data structure.

For a valid rho<=A/c family this becomes A/(c+A), with A=1 in H^2 or the stated A=1.59 in higher dimension. At c=2, these are 1/3 and approximately 0.443. Neither is an unconditional result of this probe: H^2 is classically dominated, and the high-dimensional model must first pass the next gate. Also compare against generic O(sqrt n) quantum search; A/(c+A)<1/2 only when c>A.

Simply retaining the usual k=log(n)/log(1/p2) leaves L=n^rho query hashes, so replacing only the candidate scan by Grover does not halve total query exponent. Coherent filtering may avoid this bottleneck, but preparing that state is a theorem obligation.

## Immediate geometry/access gate

In the [official 2026 PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/LIPIcs.SoCG.2026.39/LIPIcs.SoCG.2026.39.pdf), Lemma 8 (p.39:7) proves collision 1-d/(pi sinh R) when BOTH points lie in B(0,R). Section 4 (p.39:10) writes a Gaussian projection integral over z from zero to infinity with integrand 1-F(sz)/w and fixed w=2 sinh R. For s>0, F(sz) grows unboundedly. The stated fixed-radius identity therefore requires an explicit conditioning/truncation or radius analysis before it is safe to reuse. This is a specific import gate, not a completed correctness verdict on the entire paper.

Separately, even in the clean H^2 bounded-domain case, set W=pi sinh R. The standard k is approximately W log(n)/(cr); the retuned quantum k above is approximately W log(n)/((c+1)r) when r/W is small. Thus radius independence of rho is not radius independence of running time. Query points need a stated domain, and bit precision and d-dependent hash costs remain charged.

Smallest lemma to prove now: fix a data-independent bounded query domain K in H^d; specify one fixed distribution over projection-plus-geodesic hashes; prove uniform near/far collision bounds on K, with explicit projection-tail error, radius/precision dependence, and per-hash evaluation cost. The tail error must be o(p1-p2) and remain controlled after k concatenations. If this cannot be done without an exponential-radius factor, stop importing the asymptotic exponent as an efficient ANN result.

Only after that gate: seek a structured hyperbolic filter family with a poly(d,log n,precision)-cost coherent sampler of query-relevant filters, and prove candidate mass/degree control for the SAME dataset class as the classical baseline. A quantum query-space frontier improving on the generic bound above would be substantive. Merely applying the existing sampler-to-Grover or sampler-to-quantum-walk template is not enough; the geometric sampler/collision lemma must be the new mechanism.

No files outside this probe directory were changed. No external messages or browser actions were taken. Literature coverage was targeted, not exhaustive.
