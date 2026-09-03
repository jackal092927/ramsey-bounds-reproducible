# Mathematical review resolution

September 2, 2026 PDT. Read with the [raw independent response](CLAUDE_NARROW_REVIEW.md), not as a replacement for it. A completed model review is criticism to evaluate, not a proof certificate.

## 1. Logical Hamiltonian versus geometric Laplacian

The review's strongest objection would be fatal if the concentration estimate concerned a logical operator's distance to its own kernel. That is **not** the hypothesis in the full local proof.

- $H_A$ acts on the logical space $V=Z_d(R)$, with known kernel dimension $r_A$.
- $\Delta_A$ acts on all chains $C_d(X_A)$, with initially unknown nullity.
- The estimate applies to **every** normalized chain with $\Delta_A$-energy below $E$, and projects it toward the embedded $\ker H_A$, not toward $\ker\Delta_A$.

Thus it bounds the dimension of the entire geometric low-energy subspace by $r_A$. Independent filling supplies at least $r_A$ geometric zero modes. Together these imply equality and a geometric gap. This is a conditional transfer argument, not a proof that the concentration hypothesis is automatic. The separate padding/interface argument is precisely where that substantive hypothesis is addressed.

The review's attached-torus example shows that independent filling alone cannot exclude extra homology. Agreed. It does **not** satisfy the full concentration hypothesis: with logical kernel zero, any additional geometric harmonic unit vector would be required to have norm at most $\eta<1$. Therefore the example does not refute the stated conditional lemma and does not force a new relative-acyclicity assumption. The notation has nevertheless been made explicit in the main proof to prevent the operator switch in a short presentation.

All three boundary-decomposition requirements raised by the review were already present: coefficients are $\mathbb C$; $V$ is the full top cycle space; and $\dim R=d$, so there are no register $(d+1)$-chains. The gap threshold depends on term count and the logical gap. No uniform-in-term-count constant gap was claimed.

## 2. Weighted path: accepted request, proof added

The arithmetic of the two rational transitions was accepted by the reviewer. Its request for a full weighted Poincare and input-anchor argument was valid: the old sentence naming those inequalities did not derive the displayed constant.

[The palette addendum, Section 3](UNARY_PALETTE_ADDENDUM.md) now supplies the missing derivation. With $1\le w_t\le2$ and edge coefficients at least $1/2$:

- Weighted mean-zero clean inputs satisfy $N_C\le2L^2 E_C$ by the weighted variance identity.
- Dirty inputs satisfy $N_B\le8L^2 E_B$ by telescoping from the penalized initial position; no mean-zero condition is needed.
- The legal and illegal clock sectors are invariant, and illegal strings have energy at least one.

Consequently $g_1\ge1/(8L^2)$. The explicit two-kernel estimate then gives $g_2\ge1/(120L^3)$. The proof includes a zero-dimensional final common kernel; nonemptiness is not needed. Only the initial dimension must be positive to normalize the counting problem.

The gain and loss steps are consecutive, never nested, and the circuit never ends mid-pair. This was already required in the construction and is now emphasized. Without it the review's exponential-weight warning would be valid.

## 3. Root's additional corrections to the secondary net proof

These are local adversarial checks, not findings of the narrow external review:

- Replaced a conditional-on-final-size runtime argument by the tower property plus a pathwise future-center bound.
- Charged coherent predicate uncomputation and finite-precision comparisons; input-oracle construction is not free.
- Matched the net radius to the desired barcode error and used exact dyadic coordinates for the lower-bound family.
- An arbitrary approximate barcode may add short bars far from zero and match them to the diagonal. Its largest death coordinate is therefore **not** a stable statistic. Use maximum finite bar length, which changes by at most twice the bottleneck error.
- A classical lower bound cannot use only a distribution of positive OR instances: always answering YES would win. Use an equal mixture of the all-zero input and a uniformly random singleton, or an equivalent transcript argument.

The final net proof records these corrections. Its potential query advantage is distinct from its still-unsettled novelty.

## 4. What remains outside this review

The narrow review did not check the fixed clique gadget calculations, the whole padded concentration derivation, the unweighting spectral decomposition, or novelty against the July paper. Those remain separately identified literature/proof obligations. The two personal Pro conversations have been sent and handed off; their completed responses have not been collected. The newly developed round-2 arguments were not part of those sent packets.
