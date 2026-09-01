# ITCS 2027 paper plan

## Submission identity

- Working title: **Quantum Query Algorithms for Constructive Ramsey Search**
- Venue: ITCS 2027
- Format: anonymous, single column, 11pt
- Scope: the quantum-query result only
- Explicitly excluded: the finite `R(3,18)` seed analysis, exact-seven search,
  circulant computations, and the classical asymptotic Ramsey-bound parts of
  the unified manuscript

## Central message

The elementary constructive proof of the diagonal Ramsey theorem can be
implemented without explicitly materializing its nested candidate sets.  By
representing each set as a short conjunction of pivot constraints and using
capped uniform quantum search, one obtains a verified homogeneous `K`-set in
an `N`-vertex graph with `N >= 4^(K-1)` using

`O(2^K K log(K/eta))`

edge queries.  At the succinct Ramsey scale `N=2^n`, this is
`O(sqrt(N) log(N) log(log(N)/eta))`, compared with `O(N)` queries for the
standard explicit constructive recursion.

## Claims-evidence matrix

| Claim | Evidence in the paper | Reproducible check |
|---|---|---|
| Bounded-error implicit-majority algorithm | Theorem 1.1; Sections 2--5 | exact-rational recurrence audit |
| Exact homogeneous output | nested-set invariant and final verification in Section 4 | finite graph diagnostics |
| Worst-case query bound | scale-aware error schedule and geometric sum in Section 5 | exact schedule evaluation |
| Estimation-free alternative | size-biased survival lemma and Proposition 5.1 | exhaustive split-tree dynamic program |
| Fixed-colour extension | Corollary 5.3 | symbolic recurrence check |
| Classical lower landscape | Proposition 5.2 and Appendix B | independent exponent calculation |
| Literature discrepancy is real at the stated parameterization | Section 6 direct substitution | printed exponent translation in audit script |

The executable checks are sanity checks, not substitutes for the proofs.

## Main-paper structure

1. **Introduction.** Problem, theorem, significance, precise comparison,
   contributions, technical overview, and nonclaims.
2. **Oracle model and capped uniform search.** Model alignment and the search
   primitive used by both algorithms.
3. **Two implicit-set recursions.** The estimation-free and sharper
   scale-aware algorithms.
4. **Correctness and survival.** Full nested-set and concentration proofs.
5. **Query complexity and the classical landscape.** Main upper bound,
   size-biased alternative, randomized classical lower bound, and multicolour
   extension.
6. **Prior art and lower-bound discrepancy.** Closest quantum work and the
   Jain--Li--Robere--Xun/Liu--Zhandry parameter audit.
7. **Reproducibility, limitations, and open problems.** Exact evidence
   boundary and research agenda.
8. **Conclusion.** One-paragraph statement of the contribution.

The first ten pages must contain the theorem, its proof architecture, the
complete correctness and complexity arguments, significance, and literature
positioning.  References and technical appendices may follow.

## Appendices

- Appendix A: capped BBHT termination, conditional uniformity, and fixed-cap
  batch collection.
- Appendix B: full derivation of the randomized classical lower bound.

## Figure plan

No figure is required.  The paper's contribution is a short algorithm and its
analysis; a decorative pipeline figure would consume space without replacing
any load-bearing definition or proof.

## Claim firewall

The submission does **not** claim:

- a new numerical Ramsey bound;
- a quantum speedup in gate complexity or on hardware;
- a separation from every randomized classical query algorithm;
- a resolution of the published near-linear quantum lower-bound statement;
- a topological quantum algorithm.

## Submission gates

1. Compile with no undefined references or citations and with embedded fonts.
2. Keep all central claims and their proof ideas within the first ten pages.
3. Preserve anonymous metadata and remove identity-bearing repository URLs.
4. Re-run the quantum self-check and full repository quick test.
5. Resolve, or explicitly and accurately disclose, the lower-bound conflict
   before external submission.

