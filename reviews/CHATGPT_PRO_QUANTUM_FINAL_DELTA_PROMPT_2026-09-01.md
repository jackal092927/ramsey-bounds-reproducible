# Final narrow ChatGPT Pro review packet

Use the existing registered ChatGPT Pro conversation for `quantum Ramsey
algorithm`.  Do not start a new conversation.

## Reviewer role

Act as a hostile ITCS/FOCS quantum-algorithms referee.  This is a final
differential review, not a new brainstorm.  Concentrate on mathematical
correctness and precise literature comparison.  Treat tests, successful
compilation, and prior AI opinions as non-proofs.

## Main theorem under review

For `K >= 2`, `N >= 4^(K-1)`, and failure parameter `eta`, the manuscript
claims a verified-output quantum algorithm for a clique or independent set of
size `K` in an arbitrary promised valid graph, using

```
O(2^K K log(K/eta))
```

coherent edge queries in the worst case.  At `N = 2^n` and
`K = floor(n/2)+1`, this becomes
`O(sqrt(N) log(N) log(log(N)/eta))`.

The proof uses capped BBHT sampling from implicit pivot-defined sets, adaptive
concentration, a first-bad-level argument, and a scale-aware error budget.  A
separate size-biased recursion gives a weaker bound and a multicolour
extension.  The proof does not use JLRX or Liu--Zhandry.

## Narrow questions

1. Reconstruct the upper-bound query sum and try to identify a hidden
   dependence on set size, amplitude preparation, adaptivity, or error
   conditioning that invalidates the stated worst-case bound.
2. Inspect the new proof-of-concept experiment paragraph.  Confirm that the
   manuscript does not misdescribe seeded finite tests or a 16-state sampler
   calculation as a full coherent simulation, hardware result, or speedup
   experiment.
3. Audit the following JLRX comparison from primary sources.

   - JLRX FOCS 2024 Definition II.6 uses graph size `G = 2^n`; the convention
     after Definition II.7 uses default target `K = n/2`.
   - Its unnumbered “Query complexity of RAMSEY” paragraph in Section III
     states a quantum query lower bound `G^(1-o(1))`, citing its graph-hash
     reduction and Liu--Zhandry.
   - Writing `H` for the multicollision range and fixing multiplicity `t`,
     the sufficient parameter condition in JLRX Theorem I.3 is
     `G >= H^(4t)/4^t`.
   - Liu--Zhandry gives fixed-`t` exponent
     `alpha_t = (2^(t-1)-1)/(2^t-1)` in `H`.
   - Direct substitution therefore gives exponent
     `alpha_t/(4t)`, maximized at `t=2` as `1/24`, rather than `1-o(1)`.

   Try to rescue the JLRX near-linear statement by finding a different model,
   normalization, reduction direction, growing-`t` theorem, or omitted query
   overhead.  If it cannot be rescued, judge whether the manuscript's phrase
   “does not follow from the cited parameter substitution” is fully justified.
   Keep this side consequence separate from JLRX's principal TFNP separation
   theorems.
4. Review the newly added references only for substantive relevance and
   bibliographic correctness: Impagliazzo--Naor 1988; Krajicek 2001 and 2005;
   Pasarkar--Papadimitriou--Yannakakis ITCS 2023; Childs--Eisenberg 2005;
   Qu et al. 2013; Ranjbar et al. 2016; Zhu 2012; Le Gall et al. 2016;
   Campos et al. 2026; corrected Liu--Zhandry EUROCRYPT 2019 metadata; and the
   existing Zhang--Xin--Dey 2024 hypergraph pointer.  Flag strategic,
   tangential, or misleading citations.
5. Search specifically for papers that dominate, subsume, or directly collide
   with this exact constructive Ramsey query upper bound.  Do not recommend
   citations merely because an author is on the ITCS program committee.

## Required output

Lead with the strongest fatal or major mathematical objection, if any.  Then
give separate verdicts for:

- upper theorem correctness;
- experiment-claim calibration;
- JLRX parameter audit;
- novelty and closest-prior-art coverage;
- self-citation appropriateness.

For every objection, provide exact source locations or a concrete calculation.
Use `VERIFIED`, `INFERENCE`, or `UNKNOWN`.  If no fatal issue is found, state
the strongest remaining submission risk and the minimum wording change.
