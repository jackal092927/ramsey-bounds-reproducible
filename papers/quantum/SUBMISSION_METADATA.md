# ITCS 2027 submission metadata

Prepared: 2026-08-31

## Title

Quantum Query Algorithms for the Constructive Diagonal Ramsey Theorem

## Abstract for HotCRP

The constructive diagonal Ramsey problem asks for a clique or an independent
set of the size guaranteed by Ramsey's theorem, using adjacency queries to the
input graph. Given coherent adjacency-oracle access to an N-vertex simple
graph, we give a bounded-error quantum algorithm that, for every K >= 2 and
N >= 4^(K-1), finds and verifies a homogeneous K-set using
O(2^K K log(K/eta)) edge queries with failure probability at most eta. At the
Ramsey scale N = 2^n, it finds a homogeneous set of order floor(n/2)+1 using
O(sqrt(N) log(N) log(log(N)/eta)) queries. The standard explicit
Erdos--Szekeres recursion uses O(N) queries.

The algorithm implements the constructive Ramsey recursion without
materializing its nested candidate sets. It represents each candidate set by
a short conjunction of adjacency constraints, samples from this implicit set
using capped quantum search with an unknown number of marked items, and uses a
scale-aware concentration schedule that assigns more accuracy to inexpensive
early levels than to expensive late levels. We also give an estimation-free
size-biased recursion, extend it to every fixed number of edge colours, and
prove a randomized classical lower bound of Omega(N^(1-1/sqrt(2))) in the same
parameterization. This lower bound does not establish a quantum--classical
separation. The result improves the query complexity of finding guaranteed
homogeneous sets; it does not improve a numerical Ramsey bound or make a
gate-complexity claim.

## Suggested topics and keywords

- Quantum query complexity
- Quantum algorithms
- Design and analysis of algorithms
- Computational complexity
- Extremal and algorithmic combinatorics
- Diagonal Ramsey theorem
- Clique or independent set
- Adjacency-oracle algorithms
- Total search problems

## Author record

The PDF is anonymous.  The sole human author, current Fresno affiliation, and
Fresno contact address have been confirmed and entered in HotCRP.  Identifying
values are intentionally omitted from this anonymous source-tree record.
Generative-AI systems are not listed as authors or co-authors, in accordance
with the ITCS 2027 policy.

## HotCRP registration state

- Submission: `#193`
- Lifecycle state: **REGISTERED DRAFT / NO PDF UPLOADED / NOT READY FOR REVIEW**
- Registered: 2026-08-31 PDT
- Profile: verified ORCID saved in the Fresno HotCRP account; the identifier is
  intentionally omitted from this anonymous source-tree record
- Topics: Algorithmic Combinatorics; Graph Algorithms; Graph Theory; Quantum
  Algorithms; Quantum Complexity; Sublinear Algorithms; TCS + Math
- AI-assisted reviewing: allowed
- AI-preparation survey: formatting and language; literature; mathematical
  assistance; substantial role
- Best Student Paper: not selected

## Submission files

- Anonymous PDF: `papers/quantum/main.pdf`
- Source: `papers/quantum/main.tex` and included files
- AI policy and readiness checklist: `papers/quantum/SUBMISSION_CHECKLIST.md`

## Deadlines

- Abstract registration: 2026-09-02 16:59 PDT
- Full paper: 2026-09-04 16:59 PDT
