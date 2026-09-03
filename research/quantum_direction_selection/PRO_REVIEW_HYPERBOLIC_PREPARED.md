# Prepared Pro discussion: quantum hyperbolic navigation

Status: SENT after explicit user confirmation, September 2 PDT. The metadata line was not included in the transmitted payload. See PRO_DISPATCH_2026-09-02.md for the verified working-state receipt; no completed response has been collected.

## Request

Try to find a mathematically substantive quantum algorithm for nearest-neighbor retrieval or navigation in hyperbolic space. Our existing work is on classical navigable graphs and hyperbolic locality-sensitive hashing. We need a whole-query or whole-route advantage against the best same-access classical algorithm, not a generic application of Grover to a neighbor list. Begin by trying to defeat the candidate mechanisms below.

## Current classical starting point

The currently repaired graph statements are weaker than a blanket logarithmic-time greedy ANN claim:

- For fixed dimension and accuracy, one corrected ANN construction has constant out-degree, an approximate-Voronoi entry structure, and at most n-1 strictly improving local moves.
- A separate exact local routing theorem uses one shared random permutation and a specified record/minimum-priority policy. It has logarithmic degree and an expected O(log^2 n) hop bound under its stated local restrictions.
- Replacing that policy with any arbitrary closer neighbor is not known to inherit the bound.
- The original fast greedy ANN statement is not an available proved premise.

An earlier external review suggested broader phase arguments; subsequent local checking found a cutoff-dependent counterexample. Do not treat that earlier review as certification of the stronger premise.

## Literature collisions

- Existing quantum HNSW, IJCAI 2025: https://www.ijcai.org/proceedings/2025/739 . A claim to first quantum HNSW is unavailable.
- Fixed-dimensional hyperbolic ANN, SoCG 2024: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2024.68 . Linear space and logarithmic query time for fixed dimension and approximation. Any polynomial-in-n quantum query time loses to this baseline for ordinary ANN.
- Hyperbolic distance Gramians, KDD 2020: https://arxiv.org/abs/2005.08672 . The linear-algebraic observation below is not claimed as new distance geometry.
- Deng, Gao, Lu, Luo, Xin, Locality Sensitive Hashing in Hyperbolic Space, SoCG 2026: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2026.39 . Possible continuity in growing dimension and query-space tradeoffs, not an automatic speedup.
- Quantum filtering already includes computing relevant filters followed by search over bucket unions: https://crypto-kantiana.com/elena.kirshanova/Papers/quantum_sieving.pdf . Coherent structured filter sampling is also studied: https://arxiv.org/html/2410.15565v1 . Reoptimizing a generic quantum LSH exponent is not a new hyperbolic mechanism.

## New local model obstruction: check independently

Let Y be a finite set in H^d, represented on the unit hyperboloid with Lorentz form B(x,y)=x_0 y_0-sum_{j>=1}x_j y_j, so B(x,y)=cosh dist(x,y). Let s=dim span(Y)<=d+1. Choose anchors a_1,...,a_s from Y spanning that space. Because the span contains a timelike vector, the restricted Lorentz form is nondegenerate and the anchor Gram matrix is invertible.

Query-independent coefficients y=sum_i alpha_yi a_i therefore satisfy

    cosh dist(q,y)=sum_i alpha_yi cosh dist(q,a_i)

for every q, even outside span(Y). Thus a classical algorithm needs only s query-to-point exact distance calls to reconstruct all scores; additional arithmetic and storage are O(s|Y|). Pairwise-distance-only preprocessing can recover the representation with O(d|Y|) distance calls. This is not constant total time.

A maximum-volume anchor basis gives |alpha_yi|<=1 by determinant replacement. Consequently additive score error xi propagates to at most s xi, assuming exact preprocessing. Raw distance error tau instead incurs tau sinh(r_i+tau); finite precision and near ties remain real issues. No efficient high-dimensional maximum-volume preprocessing claim is made.

This applies to each neighbor set plus the current point. It invalidates a Delta-query classical baseline for generic geometric neighbor search in a model allowing exact geometry preprocessing. Fixed-seed H2, H3 and lower-dimensional embedded tests agree to approximately 1.8e-15. These are not quantum simulations or full graph experiments.

## One positive geometric calculation, but not yet a routing theorem

Let dist(p,q)=R and draw u uniformly in direction on the radius-R sphere about p. For 0<=delta<R, progress dist(u,q)<=R-delta occurs in the angular cap

    theta=2 asin sqrt((cosh(R-delta)-1)/(2 sinh(R)^2)).

For fixed dimension d>=2 and fixed delta as R grows, its probability is asymptotic to C_d exp(-(d-1)(R+delta)/2). With m good neighbors in a Delta-list, the honest unstructured comparison is classical Delta/m versus quantum sqrt(Delta/m), not always Delta versus sqrt(Delta).

The one-step guaranteed-progress proxies delta*p and delta*sqrt(p) are maximized asymptotically at 2/(d-1) and 4/(d-1), respectively. This suggests a different progress threshold, but supplies neither adaptive good-neighbor density nor a query-independent graph construction. In H2, sorted angular access already defeats the raw unstructured comparison. The landmark argument is a further obstacle.

## Generic quantum LSH accounting: do not rediscover as novelty

With k concatenated hashes and L approximately p1^(-k) tables, classically obtain bucket pointers/sizes, form prefix lengths and use coherent read-only memory to search the bucket union. A generic expected-cost proxy is

    T_Q = soft-O(k L tau_hash + tau_distance sqrt(1+n L p2^k)).

Balancing gives k=log(n)/log(1/(p1 p2)), query exponent rho/(1+rho), and space exponent 1+rho/(1+rho), where rho=log(1/p1)/log(1/p2), if omitted costs are subpolynomial. The naive rho/2 ignores finding the query's buckets. This is a standard mechanism, not a new result.

In the native hyperbolic LSH source, importing the collision law also requires respecting its bounded query/data domain and hash-evaluation/radius parameters. The H2 expression p(r)=1-r/(pi sinh R) hides a concatenation length proportional to sinh R/r. Higher-dimensional projection needs an explicit tail/domain check before reuse. This is an unresolved import audit, not an assertion that the published paper is false.

## Candidate questions

1. Is there a natural growing-dimensional time-space-precision model where hyperbolic geometry enables a coherent structured-filter sampler improving on the established quantum LSF tradeoff? Give the geometric lemma, not a black-box search substitution.
2. Can a query-independent multiscale navigable graph sustain a provable progress-versus-degree tradeoff along adaptive routes, with an advantage surviving classical geometric indexing and landmark reconstruction?
3. If a comparison-only or restricted-local model is essential, is that restriction naturally motivated, rather than designed to manufacture a Grover separation?

## Desired response

Audit the landmark proof first. Then either produce one concrete new lemma supporting a whole-query/route advantage, with preprocessing, space, precision, QRAM/coherent access and classical baseline explicit, or recommend stopping this direction for a precise mathematical reason. Do not claim a new quantum algorithm or novelty without those steps.
