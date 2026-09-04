# Normalized Persistence manuscript, version 2 draft

This directory is the working draft of the **second version** of the paper.
Version 1 (the ITCS 2027 candidate) is frozen in `../manuscript_v0/` and at
git tag `normalized-persistence-v1`; nothing here modifies it.

Title: *Exact Kernel Transfer to Clique Complexes: Hardness of Normalized
Persistence and Gapped Betti Numbers.*

New relative to version 1 (see `../V2_ENHANCEMENT_PLAN_2026-09-04.md` for the
proofs and `PROOF_AUDIT.md` for the dependency audit):

1. Exponent: `kappa = 2p` with `p` the private depth of the certified
   fillings (`p = 5`, so `kappa = 10` instead of `26`), via a Schur-complement
   bound (Lemma A.x `lem:filling-domination`); Lemma 3.2 no longer needs the
   locality-dependent scaling estimate.
2. General source class `SF^{G_2}` (perfect-subspace fractions), Theorem 5.4;
   `SDQC1^{G_2}` hardness in fraction form for all thresholds and in trace form
   for `b < (3a-1)/2` (Corollary 5.5); fixed-eight `BQP1^{G_2}` theorem as a
   corollary; `2^r` initial holes.
3. Gapped Betti numbers of clique complexes are #P-complete (Theorem 5.7).
4. Section 6: harmonic concentration, large-overlap condition with
   `a_min >= 1 - 1/poly`, preparation of the initial harmonic mixture, and the
   "hard and in BQP" theorem (Theorem 6.5); unweighted transfer in
   Corollary 7.2.

Build from this directory with `latexmk -pdf -interaction=nonstopmode
-halt-on-error main.tex`. The supplement is identical to version 1 except that
the two new checks `../check_filling_domination.py` and
`../check_harmonic_overlap.py` document the depth computation and the
overlap behaviour.

Evidence boundary: the new theorems were derived and checked in this session
(September 4, 2026) but have not yet had an external review; the gate-set
extension of `SF` (open problem 1 of Section 9) is not claimed.
