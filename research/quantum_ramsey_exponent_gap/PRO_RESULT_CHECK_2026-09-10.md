# Quantum Ramsey exponent-gap discussion: received and partially checked

Date: 2026-09-10. The new response is **COMPLETED / RECEIVED**; its proposed
algorithmic theorem remains **CONDITIONAL**, not integrated into the manuscript.

Source: [shared discussion](https://chatgpt.com/share/6aa33288-b370-83e8-972e-471d74e76b52).
Canonical detailed audit, proof gates, and exact arithmetic:
[QuantumTDA result check](https://github.com/jackal092927/QuantumTDA/tree/main/research/2026-09-10-pro-progress).

The response proposes a robust implicit-set compiler for two-reservoir book
recursion. If its unresolved Compiler Lemma C holds, the displayed parameters
yield N^(0.4990971866...+o(1)) queries, or the weaker fixed exponent 0.4995 after
absorbing the subpolynomial overhead. Exact rational parameter inequalities
passed an independent local check; the robust induction has not been proved.
The currently established bounds therefore remain Omega(N^(1/12)) and
O-tilde(N^(1/2)). They are not matched by this response.

A separately reconstructed hybrid argument supports the response's scoped
common-witness obstruction: q-query simulation of each edge from an L-item
unique-search oracle leaves a fixed K-witness valid in all but O(q^2 K^2)
instances. When q^2 K^2=o(L), a decoder required to handle every legal witness
must itself use Omega(sqrt(L)) queries. This obstructs that class of cheap
all-witness unique-search reductions; it is not a general Ramsey lower bound.
Likewise, a search-hard terminal set on a prescribed recursion path does not
lower-bound finding any homogeneous K-set.

Next proof target: close or refute the compiler's robust branch invariant,
including finite panels, inverse-polynomial score margins, step counts, and
all off-diagonal terminal calls. Preserve the original target size, oracle
costs and success probability. Do not treat a known combinatorial existence
bound as an oracle-efficient algorithm.

No new Pro request was sent, no manuscript was changed, and no submission was
updated in this checkpoint. A separate older Ramsey-review conversation was
located but could not be fully read because browser operations timed out;
this note does not certify that it contains no further objections.
