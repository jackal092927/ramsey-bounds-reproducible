# Research Proposal: Certified Optimization of the Diagonal Ramsey Upper-Bound Constant

## Problem Anchor

- **Bottom-line problem:** Find a rigorous, independently verifiable improvement to a currently known bound for a classical two-color Ramsey number.
- **Must-solve bottleneck:** Candidate improvements are easy to overstate: a useful result must both beat a live authoritative baseline and come with a certificate whose mathematical link to the Ramsey bound is audited independently of the search code.
- **Non-goals:** The first phase will not attempt to determine `R(5,5)` exactly, launch an unbounded search over all small Ramsey cells, or claim that a benchmark verifier alone constitutes a proof.
- **Constraints:** Begin with local CPU computation and an empty workspace; do not assume access to AlphaEvolve or a large compute cluster; keep the first mechanism small enough to reproduce and audit; use the literature state as of 2026-08-12.
- **Success condition:** Produce parameters giving a strictly smaller certified base `c` in `R(k,k) <= c^(k+o(k))` than the strongest audited baseline, pass two independent numerical verifiers with explicit positive slack on the full continuum, and complete a human-readable theorem-to-certificate audit before making a mathematical claim.

## Technical Gap

The classical diagonal lower and upper bounds remain exponentially far apart. The lower bound is
`R(k,k) > (sqrt(2)/e + o(1)) k 2^(k/2)`, while the strongest published explicit upper-bound base is approximately `3.7992`, obtained by Gupta, Ndiaye, Norin, and Wei (GNNW) by optimizing the Campos--Griffiths--Morris--Sahasrabudhe framework.

A March 2026 HorizonMath working draft reported a candidate base near `3.6961` within a split-regime validator. This is an unusually tractable frontier: the search variables are a low-degree correction polynomial and witness functions, while verification can be reduced to interval inequalities. However, HorizonMath explicitly labels the result as pending expert review. There is therefore a real gap between finding a numerically accepted certificate and establishing a publication-grade Ramsey theorem.

The current pipeline can fail at three precise points:

1. optimizing only a sampled grid can miss a constraint violation between samples;
2. interval code can certify the implemented inequalities while the implemented inequalities are not exactly those required by the GNNW theorem;
3. a split construction near `lambda = 0` can create an unproved seam at the regime boundary.

The smallest adequate intervention is a search-and-proof separation: use ordinary numerical optimization only to propose a polynomial and witnesses, then compile them into a standalone interval certificate checked by an independently implemented verifier, together with a line-by-line derivation from the source theorem.

## Method Thesis

- **One-sentence thesis:** A certificate compiler that jointly optimizes the GNNW correction polynomial and pointwise Ramsey-region witnesses, then proves the resulting continuum inequalities by adaptive interval subdivision, can either validate and sharpen the reported `3.6961` candidate or identify the exact obstruction preventing it from being a Ramsey upper-bound theorem.
- **Why this is the smallest adequate intervention:** It changes only the finite-dimensional ansatz and its witnesses; it does not modify the combinatorial proof framework or add a second theoretical mechanism.
- **Why this route is timely:** Recent work has converted a 90-year qualitative barrier into an explicit numerical optimization problem, and the 2026 candidate exposes a generator--verifier gap that is small enough for independent reproduction but not yet closed mathematically.

## Contribution Focus

- **Dominant contribution:** A theorem-faithful, independently verified improvement of the diagonal upper-bound base within the GNNW framework.
- **Optional supporting contribution:** A reusable certificate format reporting the active constraints and bottleneck intervals, which can guide later analytic simplification.
- **Explicit non-contributions:** No claim of a new general Ramsey method; no LLM is part of the proof; no simultaneous lower-bound record search in phase one.

## Proposed Method

### Complexity Budget

- **Frozen / reused backbone:** The GNNW sufficient theorem, its published inner Ramsey region, and standard interval arithmetic.
- **New components:** One numerical search routine and one independent certificate checker.
- **Tempting additions intentionally not used:** Graph neural networks, reinforcement learning, large-language-model mutation loops, SAT search for `R(5,5)`, and simultaneous multicolor or hypergraph extensions.

### System Overview

```text
published theorem + inner region
              |
              v
 polynomial/witness optimizer ----> floating-point candidate
                                         |
                                         v
                            certificate compiler
                                         |
                          +--------------+--------------+
                          |                             |
                          v                             v
                interval verifier A          independent verifier B
                          |                             |
                          +--------------+--------------+
                                         |
                                         v
                         theorem-to-certificate audit
                                         |
                                         v
                           claim or diagnosed obstruction
```

### Core Mechanism

- **Input:** Polynomial degree `d`, coefficients `a_1,...,a_d`, a partition of `(0,1]`, and piecewise witness values `M_i,Y_i`.
- **Output:** The diagonal base `c = exp(F(1))`, certified lower margins for every required inequality, and a machine-readable certificate.
- **Parameterization:**
  `F(lambda) = (1+lambda)log(1+lambda) - lambda log(lambda) + exp(-lambda) p(lambda)`, where `p(lambda) = sum_i a_i lambda^i`.
- **Search objective:** Minimize `F(1)` subject to dense-grid proxy constraints, using continuation in polynomial degree and adaptive refinement around active intervals.
- **Witness synthesis:** For fixed `F` and `lambda`, reduce Ramsey-region feasibility to a one-dimensional optimization over `M`; choose `Y` with an explicit safety margin, then merge adjacent intervals only when the certificate remains valid.
- **Certification:** Evaluate `F`, `F'`, `X`, the Ramsey-region support inequality, and the main GNNW inequality using outward-rounded interval arithmetic. Bisect any interval whose enclosure is inconclusive. Handle `(0,lambda_0]` analytically and prove compatibility at `lambda_0` from both sides.
- **Why this is the main novelty:** The search is not novel by itself. The contribution is the proof-preserving compilation layer and independent audit that turns an optimized ansatz into a defensible Ramsey bound.

### Optional Supporting Component

The checker records which constraint is active at each interval and returns a bottleneck profile. This profile is diagnostic only; it does not affect soundness and can be deleted without changing the theorem.

### Modern Primitive Usage

- **Primitive used:** Certified numerical optimization with adaptive interval branch-and-bound.
- **Exact role:** Numerical routines generate candidates; interval arithmetic supplies the proof obligations.
- **Why no LLM/RL component is needed:** Candidate generation is low-dimensional and deterministic. Adding a learned controller would complicate attribution without strengthening the certificate. LLM suggestions may be used privately as seeds, but never as evidence.

### Integration into the Mathematical Proof

1. State the exact GNNW theorem and all quantifiers.
2. Define the chosen `F`, `M`, and `Y` in a finite certificate.
3. Prove regularity and positivity of `F` and `F'`.
4. Prove membership of `(X(lambda),Y(lambda))` in the admissible Ramsey region for all `lambda`.
5. Prove the main sufficient inequality for all `lambda`.
6. Evaluate `F(1)` with an outward-rounded upper bound and derive `R(k,k) <= exp(F(1)k+o(k))`.

The numerical search code is frozen out of the final proof path; only the certificate and verifier are needed to reproduce the result.

### Failure Modes and Diagnostics

- **Verifier-framework mismatch:** Compare every implemented expression against the numbered theorem/lemma in GNNW; reject the claim if a required hypothesis is absent.
- **Small-`lambda` seam:** Require overlapping proofs on an interval around `lambda_0`, not merely equality at one point.
- **Interval dependency blow-up:** Bisect further or replace the expression with a monotonicity bound; never fall back to sampling for certification.
- **Piecewise witness legality:** Verify that the source theorem permits nonsmooth auxiliary witnesses; otherwise replace steps by explicit smooth interpolants and recertify.
- **False improvement caused by rounding:** Report an outward-rounded upper bound for `c` and retain a gap well above numerical error.
- **Candidate cannot beat `3.6961`:** A valid obstruction map is still useful internally, but it is not a new Ramsey bound.

### Novelty and Elegance Argument

GNNW provides the proof framework and a `3.7992` parameter choice. HorizonMath supplies a `3.6961` benchmark certificate but explicitly leaves expert review pending. This project does not rebrand numerical tuning as new theory. Its narrow novelty target is to close the proof gap and then optimize beyond the audited value, with a final artifact small enough that another group can validate it without trusting our optimizer.

## Claim-Driven Validation Sketch

### Claim 1: The certificate pipeline is theorem-faithful

- **Minimal experiment:** Reproduce the published GNNW `3.7992` parameters and the reported HorizonMath candidate, then compare all margins under two independently written verifiers.
- **Baselines / ablations:** Published cubic correction; HorizonMath quintic correction; grid-only checker as a deliberately insufficient ablation.
- **Metric:** Agreement of certified `c`, positivity of every interval margin, and zero uncovered intervals.
- **Expected evidence:** Both rigorous verifiers accept the same certificate; the grid-only checker is shown not to be the proof path.

### Claim 2: Joint polynomial/witness optimization improves the audited base

- **Minimal experiment:** Search degrees 5--10 with a fixed certificate budget, compile the best candidate, and verify it independently.
- **Baselines / ablations:** Coefficient-only optimization with fixed witnesses; witness-only optimization with the published polynomial; joint optimization.
- **Metric:** Outward-rounded upper bound on `c`, minimum certified slack, certificate size, and verification time.
- **Expected evidence:** Joint optimization gives a strictly smaller `c` than the strongest theorem-audited baseline while retaining positive slack.

## Experiment Handoff Inputs

- **Must-prove claims:** Every sufficient condition holds on the continuum; the final base is below the live audited baseline; the certificate implies the stated Ramsey theorem.
- **Must-run ablations:** Published baseline reproduction, HorizonMath reproduction, grid-versus-interval check, and fixed-versus-joint witness optimization.
- **Critical metrics:** Certified base `c`, minimum interval slack, uncovered/inconclusive interval count, verifier agreement, and wall-clock time.
- **Highest-risk assumptions:** The GNNW theorem accepts the chosen witness regularity; the HorizonMath inner region is a valid subset for both orientations; the small-`lambda` analytic splice is complete.

## Compute & Timeline Estimate

- **Compute:** Initial reproduction and degree-5--10 searches should fit on a local CPU; exhaustive high-degree exploration may require parallel CPU workers but not GPUs.
- **Data / annotation cost:** None.
- **Timeline:** 1--2 days for source-theorem audit and baseline reproduction; 2--5 days for independent verifier and search; longer only if the candidate requires analytic repair.
