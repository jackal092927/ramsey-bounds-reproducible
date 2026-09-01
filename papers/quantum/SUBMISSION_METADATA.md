# ITCS 2027 submission metadata

Prepared: 2026-08-31

## Title

Quantum Query Algorithms for Constructive Ramsey Search

## Abstract for HotCRP

Given coherent adjacency-oracle access to an N-vertex graph, we study the
total search problem of finding a clique or independent set whose existence is
guaranteed by the diagonal Ramsey theorem. For K >= 2 and N >= 4^(K-1), we
give a bounded-error quantum algorithm that outputs a verified homogeneous
K-set using O(2^K K log(K/eta)) edge queries, where the failure probability is
at most eta. In particular, when N = 2^n, it finds a homogeneous set of order
floor(n/2)+1 using O(sqrt(N) log(N) log(log(N)/eta)) queries. The standard
explicit constructive Ramsey recursion uses O(N) queries.

The algorithm represents each nested candidate set by an implicit membership
predicate, samples it using capped unknown-solution quantum search, and uses a
scale-aware concentration schedule that spends accuracy where sampling is
cheap. We also give an estimation-free size-biased recursion, extend that
argument to any fixed number of edge colours, and prove a randomized classical
lower bound of Omega(N^(1-1/sqrt(2))) at the same Ramsey scale. The latter does
not separate the quantum algorithm from all randomized classical algorithms.
Finally, we identify a parameter-level incompatibility with a printed
N^(1-o(1)) quantum lower bound in prior work: direct substitution into its
cited reduction and multicollision theorem yields exponent at most 1/24
through that route.

## Suggested topics and keywords

- Quantum query complexity
- Design and analysis of algorithms
- Computational complexity
- Extremal and algorithmic combinatorics
- Ramsey theory
- Total search problems

## Author record

The PDF is anonymous. The complete human author list, ordering, affiliations,
and submission email must be confirmed before they are entered into HotCRP.
Generative-AI systems cannot be listed as authors or co-authors under the ITCS
2027 policy.

## Submission files

- Anonymous PDF: `papers/quantum/main.pdf`
- Source: `papers/quantum/main.tex` and included files
- AI policy and readiness checklist: `papers/quantum/SUBMISSION_CHECKLIST.md`

## Deadlines

- Abstract registration: 2026-09-02 16:59 PDT
- Full paper: 2026-09-04 16:59 PDT

