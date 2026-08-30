# Independent adversarial review request

Please act as a hostile but mathematically careful referee for the attached
single unified Ramsey-theory manuscript.  Do not infer validity from the
authors' status labels, hashes, or prior review reports.  Reconstruct each
logical implication from the manuscript itself and explicitly separate:

1. a theorem proved in the manuscript;
2. a theorem valid only after granting a precisely stated, version-pinned
   source interface;
3. a numerical inequality established by the described certificate semantics;
4. a historical computation that was not rerun in your review; and
5. a conjecture, bounded `UNKNOWN`, or non-implication.

Use exactly these verdicts for every major claim:

- `PROVABLE AS STATED`
- `PROVABLE AFTER WEAKENING OR EXTRA ASSUMPTION`
- `NOT CURRENTLY JUSTIFIED`

The three headline claims to attack are:

- the conditional/source-relative diagonal upper bound
  `R(k,k) <= (3.780685290)^(k+o(k))`, including the longer certified upper
  endpoint;
- the fixed-large-`C`, source-relative lower-exponent addition
  `Hhat_*(C) = (1+o(1))/(64 log C)`, with the order of limits fixed `C`, then
  `ell -> infinity`, then `C -> infinity`; and
- the fixed-seed one-sided deletion repair radius at least seven, with free
  additions, while exact seven remains `UNKNOWN` and no implication
  `R(3,18) >= 101` is claimed.

In particular, check the following failure modes rather than merely
summarizing the prose:

- whether every Yang--Mao page/reservoir quantity and scalar gate used in the
  upper transfer is defined and whether the max--min case split has the right
  direction;
- whether the outer-wedge derivative reductions really put each maximum at
  the stated endpoint and whether the displayed outward-rounded decimal
  proves the stronger decimal claim;
- whether the six-stage certificate-correctness theorem states enough
  continuum obligations to imply a uniform Ramsey rate without circularly
  assuming its conclusion;
- whether all lower-theorem source parameters are defined, the `p` versus
  `p_C` cutoff is consistent, the three-factor Holder/CGF comparison is proved
  on one conditional history, extraction pays every deletion multiplicity,
  and the red/blue crossing has a displayed positive gap;
- whether the `1/64` cap is restricted to an actually defined admissible
  scalar class;
- whether the finite CNF is a relaxation in the correct logical direction,
  the three triangle-edge branches are exhaustive, the budget-five and
  exact-six layers combine correctly, and `UNKNOWN` is never converted into
  false nonexistence; and
- whether claims of reproducibility distinguish current-run proof replay from
  stored provenance, portable source pinning from platform-specific binary
  hashes, and local assets from a public release that may not yet exist.

Return a publication-style report with:

1. an executive accept/minor-revision/major-revision/reject verdict;
2. a claim-by-claim verdict table;
3. numbered fatal and major issues with page, theorem, equation, or appendix
   references;
4. minor correctness and presentation issues;
5. a dependency/trust-boundary map for each headline theorem;
6. the smallest safe corrected statement for every claim that does not pass
   as written; and
7. a final checklist of exact repairs required before submission.

Do not claim that you ran repository code or replayed proof traces unless you
actually did so.  Treat the manuscript as one paper containing three
logically independent results; do not recommend splitting it into separate
papers merely because the methods differ.
