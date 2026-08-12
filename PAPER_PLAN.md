# Publication plan

Date: 2026-08-12

## Editorial decision

The workspace contains three mathematically different contributions and should
not be forced into one manuscript.  The publication bundle consists of:

1. a formal upper-bound paper;
2. a formal source-relative lower-bound paper; and
3. a proof-carrying computational report for the finite searches.

The first two are written as research papers.  The third is deliberately a
technical report because the current finite search does not improve a global
Ramsey bound.

## Paper U: diagonal upper bound

Working title: *A Computer-Assisted Retained-Spine Bound for Diagonal Ramsey
Numbers*.

Main scoped theorem:

\[
R(k,k)\le (3.780685290)^{k+o(k)},
\]

with certified unrounded base below
`3.780685288379640114`.  The theorem imports the explicitly stated
Yang--Mao v1 interfaces and the reviewed off-diagonal rate theorem.  It does
not give an effective finite-\(k\) threshold or a global optimization claim.

Core mathematical contribution:

- an exact ratio/separator argument for a cubic root filter;
- a complete two-dimensional reduction to an exact diagonal expression;
- a compact interval proof and analytic half-line tail;
- an exact rational moment/tail budget proving
  \(\mathcal G_2^{(3)}(330867/500000,
  12366348252219/1250000000000)\); and
- a certified retained-spine variational transfer.

## Paper L: fixed-ratio lower bound

Working title: *Controlled Residuals in Gaussian Ramsey Constructions*.

Main scoped theorem: for every sufficiently large fixed \(C\),

\[
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge -\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+\widehat H_*(C),
\]

where

\[
\widehat H_*(C)=\frac{1+o(1)}{64\log C}>0.
\]

The theorem is source-relative to pinned HMS v2 and Lin--Niu v2 inputs and has
an existential, non-effective threshold in \(C\).  It is not presented as an
all-\(C\), finite-Ramsey, or unconditional theorem.

Core mathematical contribution:

- rigidity of exact triangular gradient merge;
- a deterministic boundary residual;
- full-box strong concavity and square completion;
- exact weighted multiplicities and a three-factor Hölder/CGF ledger;
- nonexchangeable reverse induction and perfect-sequence extraction; and
- a narrowly scoped \(1/64\) method cap.

## Computational report

Working title: *Proof-Carrying SAT Barriers Around a 100-Vertex
\(R(3,18)\) Near Miss*.

The report proves only a fixed-seed edit statement.  For the pinned
100-vertex near miss, arbitrary additions of input nonedges together with at
most six deletions of input edges cannot produce a triangle-free graph of
independence number below 18.  Exact-seven remains `UNKNOWN`; therefore the
report does not prove \(R(3,18)\ge101\).

## Evidence policy

Every theorem is paired with:

- a human-readable proof;
- a machine-readable parameter set;
- at least one independent implementation where available;
- a SHA-256 manifest;
- an explicit dependency and trust boundary; and
- exact separation of `PASS`, `UNSAT`, `SAT`, `UNKNOWN`, and untested states.

The superceded exploratory results remain in `routes/` for provenance but are
not treated as current paper claims.

