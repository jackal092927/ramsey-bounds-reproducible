# ChatGPT Pro quantum-review disposition

Date checked: 2026-08-31  
Scope: mathematical correctness, novelty risk, and experimental claim boundary  
Status: **completed and dispositioned**

## External verdict

The completed ChatGPT Pro review classified the headline result as a correct
and apparently novel Ramsey total-search quantum-query upper bound:

```text
Q(K, eta) = O(2^K K log(K/eta))
Q(N, eta) = O(sqrt(N) log(N) log(log(N)/eta)) at N = 2^n.
```

It found no fatal mathematical error. It regarded the ITCS case as plausible
but borderline on significance: a reviewer may characterize the method as
BBHT inserted into the textbook Ramsey recursion unless the paper makes the
robust survival invariant, exact batch uniformity, and scale-aware accuracy
allocation explicit. It agreed that the direct JLRX/Liu--Zhandry parameter
transfer gives exponent at most `1/24`, while recommending author
clarification before submission.

This AI review is an author-side adversarial check, not independent human peer
review and not proof of the theorem.

## Mathematical objections and dispositions

| Objection raised | Disposition in the standalone paper |
|---|---|
| Adaptive success proof might condition on its own successful history | Lemma 4.2 conditions on the complete history and uses a first-bad-level/tower-property argument. |
| Accepted quantum samples might fail to be independent uniform samples | Lemma 2.2 and Appendix A factor block success from marked-item identity and condition on the complete success pattern. |
| BBHT is commonly stated with expected running time | Appendix A fixes a deterministic truncation cap before oracle outcomes and derives a fixed-size batch cap. |
| The source of the next pivot might be implicit | Section 3 explicitly obtains each pivot from the current implicit set and specifies the final vertex. |
| The JLRX local relation permits malformed adjacency encodings | Corollary 2.1 canonicalizes an arbitrary circuit and returns either a locally verified invalidity certificate or a homogeneous set at the same asymptotic query cost. |
| “Near-quadratic speedup” is potentially misleading | The paper says “square-root query improvement, up to polylogarithmic factors,” and explicitly disclaims gate, hardware, and all-classical separation claims. |
| Tiny simulations could be oversold | Section 7 and Appendix C label them modular proof-of-concept/regression checks and state exactly what is and is not simulated. |

The three significance reinforcements requested by the review are already in
the current paper: the arbitrary-encoding corollary, a fixed-colour extension,
and a stronger randomized-classical lower bound in the same parameterization.

## Experimental follow-up executed locally

The theorem self-check returned `QUANTUM_RAMSEY_AUDIT_PASS`. With seed
`20260831`, the proof-of-concept run used `K=3`, `N=16`, and 1,000 trials for
each of complete, empty, parity, one fixed random graph, and fresh random
graphs. All 5,000 runs returned verified homogeneous triples. The smallest
final candidate-set sizes were 13, 13, 6, 2, and 2, respectively.

The isolated 16-state Grover audit covered marked-set sizes
`1,2,3,4,8,15`; block success ranged from `0.4026746749` to
`0.5973253251`, and conditional nonuniformity was zero to machine precision.
These data do not establish practical or hardware quantum advantage.

## Remaining submission gate

The review removes “pending Pro verdict” as a gate. It does not remove the
closest-source gate: the paper should seek clarification from the JLRX authors
or retain its current carefully scoped incompatibility statement. The
mathematical upper theorem itself remains locally classified as provable as
stated.
