# Lower S3 closure audit

**Date:** 2026-08-30  
**Scope:** the weighted reverse-propagation implication formerly assumed as
item S3 in the lower-bound component  
**Mode:** adversarial reconstruction from the canonical definitions, followed
by an independent AI second-opinion review

## Verdict

The implication from the one-step kernel estimate (2.37) to the conditional
survival estimate (2.38) is a local lemma. It requires no numerical
certificate and no theorem imported from HMS or Lin--Niu. The lower theorem
remains source-relative because items S1, S2, S4, and S5 are still
version-pinned source assumptions.

## Proof boundary

For each exposure step, write the weighted potential as

\[
\mathcal P_i^T=U_i+V_i,\qquad
\mathcal P_{i-1}^T=U_i+W_i.
\]

The indicator-kernel definition gives the exact conjugation identity

\[
\mathbb E[\mathbf 1_{A_i^R}e^{-\mathcal P_i^T}
          \mid\mathcal F_{i-1}]
=e^{-\mathcal P_{i-1}^T}\mathcal K_i^T.
\]

Combining this identity with
\(I_{i-1}=A_i^R\cap I_i\), conditional monotonicity, and the tower property
proves the reverse step. The proof checks both terminal levels:

- \(s=r\), using \(\mathcal H_C(0)=1\);
- \(s=r-1\), using \(1\le\mathcal H_C(1)=e\).

The second case is the load-bearing base because the kernel premise is indexed
only by \(i<r\).

## Integrability and null events

On \(A_i^R\), every Gaussian coordinate has a finite upper cutoff. For
nonnegative \(T\), the negative part of
\(\sum T_{jq}X_jX_q\) grows at most linearly along the unbounded directions of
that truncated orthant. Gaussian linear exponential moments are finite, so
the conditional exponential moment in the kernel is finite.

The canonical kernel now uses
\(\mathbb E[\mathbf 1_{A_i^R}e^{-V_i}\mid\mathcal F_{i-1}]\) as its primary
form. It therefore remains well-defined when
\(\mathbb P(A_i^R\mid\mathcal F_{i-1})=0\). In the actual Bartlett model that
probability is almost surely
\(\prod_{j>i}\Phi(-b_{ij})>0\).

## Source and evidence disposition

The pinned HMS and Lin--Niu arguments contain the scalar reverse-induction
prototype, but neither states the arbitrary triangular-weight lemma verbatim.
They are not needed for its proof. Arithmetic replay remains diagnostic only;
it neither proves nor is needed to prove S3.

The external second-opinion reviewer independently confirmed the conjugation,
indexing, and two-base-case argument. Its warning about a spectral threshold
for an untruncated indefinite Gaussian quadratic form does not apply after the
coordinatewise upper truncation; the preceding linear-growth domination
settles the relevant integrability question.

## Claim change

This closure removes one unnecessary assumption without changing any formula,
constant, limit order, or Ramsey conclusion. It does not discharge S1, S2, S4,
or S5 and does not turn the lower theorem into a source-independent
unconditional result.
