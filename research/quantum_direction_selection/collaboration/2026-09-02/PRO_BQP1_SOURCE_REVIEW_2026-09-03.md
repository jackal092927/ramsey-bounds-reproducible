# Pro BQP1 source-interface review — complete response

Collected 2026-09-03T19:56:12.693Z. The browser showed a completed response, **Worked for 5m 56s**, after user message 8 and the BQP1 source packet. This is external model review, not independent correctness, novelty, literature, or unrestricted-class certification.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: f11cb4ed83bdbc7d738b6b159e7267850f49ad92.
- Actual task: [BQP1 source submission](PRO_BQP1_SOURCE_SUBMISSION_2026-09-03.md).
- Input: [PRO_BQP1_SOURCE_PACKET_2026-09-03.md](PRO_BQP1_SOURCE_PACKET_2026-09-03.md), 36077 bytes, SHA-256 4f68ce7c35596f5ae0c1aaa80891de9cc27880b0d9d673818b2dc05cfeb38934.
- Visible account at collection matched the registered personal Pro identity already verified in this browser session; the public archive omits the account email.
- Exact browser completion time was not exposed; collection time and displayed duration are separate facts.

The response below was transcribed from the rendered DOM. All **98** equation elements were recovered from displayed `data-math-source` attributes; headings, lists, emphasis and the status table were retained. Four visible attachment citation labels are preserved as 〔…〕. The answer contains no external links. [The capture record](PRO_BQP1_SOURCE_REVIEW_CAPTURE_2026-09-03.json) retains the displayed text, exact equation sources and rendered HTML digest. The Copy response action did not replace the operating-system clipboard, which still held message 7, so that stale clipboard content was rejected rather than used as a cross-check. Pro explicitly did not reopen Rudolph or the geometric sources; those statements were treated as packet hypotheses. Adopted conclusions are recorded separately.

---

# Verdict

The eight-label source construction is **mathematically valid under the supplied hypotheses**. The compressed acceptance operator is exactly

\[
M_x=
\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0)
\otimes I_{\mathrm{dummy}},
\]

not merely trace-equivalent to that matrix. Coherent label inputs, verifier-output entanglement, and reversible scratch do not create off-diagonal label blocks.

Consequently, assuming the corrected geometric transfer theorem, additive approximation of true normalized persistence for nested **weighted** clique complexes with inverse-polynomial gaps above both complete endpoint kernels is

\[
\boxed{\mathsf{BQP}_1^{G_2}\text{-hard}},
\qquad
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}.
\]

The target ratio is exactly \(3/4\) in YES and \(1/8\) in NO. Error \(1/24\) is safe.

I did **not** independently source-check Rudolph’s Definition 2.2, Theorems 2.3 or 3.4. As instructed, I treat the packet’s descriptions of those statements as hypotheses. I likewise treat the geometric transfer theorem and its finite palette as supplied. The bounded task and its source assumptions are stated explicitly in the packet. 〔PRO_BQP1_SOURCE_PACKET_2026-09-…〕

There is no invalid inference in the proposed composition. One essential scope condition is that \(Q_x\) has a fixed clean input, so its compressed acceptance operator is the scalar \(p_x\). With a mixed witness or unresolved input space, the five conditional blocks would contain an operator, not the scalar \(p_x\).

# 1. Exact operator calculation

Let \(Z\cong(\mathbb C^2)^{\otimes3}\) be the label register and \(D_{\rm dum}\) the ignored mixed dummy register. Let \(\mathcal H_Q\) contain all verifier qubits, initialized to a fixed clean state \(\lvert 0_Q\rangle\). Write

\[
\Pi_q=\lvert1\rangle\!\langle1\rvert_q\otimes I_{\mathrm{rest}}
\]

for the verifier’s output projector, so

\[
p_x=
\langle0_Q|Q_x^\dagger\Pi_qQ_x|0_Q\rangle.
\]

Let \(C\) be the reversible classical circuit that, using clean scratch and a fresh clean decision bit \(a\), computes

\[
A(z,q)
=
[z=000]\lor
\bigl(q\land[z\in T]\bigr),
\qquad
T=\{001,010,011,100,101\},
\]

into \(a\), and then uncomputes its scratch. It preserves \(z\) and \(q\). Therefore it is block diagonal in the label basis:

\[
C=\sum_z |z\rangle\!\langle z|\otimes C_z.
\]

Conjugating the final decision projector

\[
\Pi_a=|1\rangle\!\langle1|_a
\]

gives, after restriction to the clean decision/scratch input,

\[
C^\dagger\Pi_aC
=
\sum_z |z\rangle\!\langle z|\otimes E_z,
\]

where

\[
E_z=
\begin{cases}
I_{\mathcal H_Q},&z=000,\\[2mm]
\Pi_q,&z\in T,\\[2mm]
0,&z\in\{110,111\}.
\end{cases}
\]

Now let the total unitary be

\[
U_x=C(I_Z\otimes Q_x),
\]

with identities on the dummy register suppressed, and let \(J\) append all clean verifier, decision, and scratch qubits. The compressed acceptance operator on \(Z\otimes D_{\rm dum}\) is

\[
\begin{aligned}
M_x
&=
J^\dagger U_x^\dagger\Pi_aU_xJ\\
&=
\sum_z |z\rangle\!\langle z|\,
\langle0_Q|Q_x^\dagger E_zQ_x|0_Q\rangle
\otimes I_{\rm dummy}\\
&=
\operatorname{diag}
(1,p_x,p_x,p_x,p_x,p_x,0,0)
\otimes I_{\rm dummy}.
\end{aligned}
\]

This proves the claimed operator identity from the packet. 〔PRO_BQP1_SOURCE_PACKET_2026-09-…〕

### Why the possible objections fail

**Coherent labels.** Off-diagonal terms \(|z\rangle\langle z'|\) cannot arise because both the reversible predicate and its conjugated measurement preserve the label and are block diagonal in \(z\).

**Entanglement of \(q\) with verifier workspace.** In a conditional block, compression produces

\[
\langle0_Q|Q_x^\dagger\Pi_qQ_x|0_Q\rangle=p_x.
\]

No product-state assumption about the final output bit is used.

**Scratch.** Computing the predicate into a fresh decision bit and reversing the scratch yields the displayed clean compression exactly. The decision bit must be fresh; the construction should not be described as irreversibly overwriting \(q\).

**Dummy bits.** They are untouched by every unitary and measurement, so the operator tensors with their identity.

# 2. Exact gate compatibility

The construction remains exactly inside \(G_2\).

- \(Q_x\) is run unconditionally, so no controlled-\(Q_x\), controlled \(H\otimes H\), or controlled internal gate is needed.
- The fixed Boolean predicate can be implemented using \(X\), CX and CCX with clean ancillas.
- Negative controls are implemented by conjugating the corresponding wire with \(X\).
- Any constant-size multi-controlled classical operation can be decomposed exactly into CCX gates with clean scratch.
- The output is one fresh qubit measured in the computational basis.

Thus the source circuit uses only

\[
X,\quad \mathrm{CX},\quad \mathrm{CCX},\quad H\otimes H.
\]

No single \(H\), mixed-spectator conversion, approximate synthesis, or complex phase is introduced by this lemma.

# 3. Complete spectrum

Let \(m\) be the number of ignored mixed dummy bits. Every displayed label eigenvalue then has multiplicity \(2^m\), and

\[
D=8\cdot2^m=2^{m+3}.
\]

## YES case

Perfect completeness gives \(p_x=1\). Hence

\[
M_x=
\operatorname{diag}(1,1,1,1,1,1,0,0)
\otimes I_{\rm dummy}.
\]

Therefore

\[
\frac{\operatorname{Tr}M_x}{D}=\frac68=\frac34,
\]

and

\[
\frac{\dim\ker(I-M_x)}{D}=\frac68=\frac34.
\]

On the orthogonal complement of the perfect eigenspace, \(M_x\) is exactly zero:

\[
M_x|_{\ker(I-M_x)^\perp}=0.
\]

## NO case

Here \(0\le p_x\le1/3\). The only eigenvalue-one block is \(z=000\). Thus

\[
\frac{\dim\ker(I-M_x)}{D}=\frac18.
\]

The normalized trace is

\[
\frac{\operatorname{Tr}M_x}{D}
=
\frac{1+5p_x}{8}
\le
\frac{1+5/3}{8}
=
\frac13.
\]

Every nonperfect eigenvalue is either \(p_x\) or \(0\), so

\[
M_x|_{\ker(I-M_x)^\perp}\preceq\frac13I.
\]

This includes both edge cases \(p_x=0\) and \(p_x=1/3\).

# 4. Growing denominator

Adding \(m=\operatorname{poly}(|x|)\) ignored mixed bits gives

\[
D=2^{m+3},
\]

while the perfect multiplicities are

\[
\begin{cases}
6\cdot2^m,&x\in L,\\
1\cdot2^m,&x\notin L.
\end{cases}
\]

Thus the normalized fractions remain

\[
\frac34
\quad\text{and}\quad
\frac18.
\]

There is no mathematical degeneracy: a target algorithm approximating the ratio still decides the original language. The denominator can be exponentially large relative to the succinct graph description while the number of added qubits and graph vertices remains polynomial.

This is nevertheless **padding-generated normalization**. It should not be advertised as evidence that the computational difficulty originates from nontrivial operations on the mixed dummy subsystem.

# 5. Conditional hardness theorem

## Theorem

Assume:

1. the packet’s supplied characterization of uniform exact \(\mathsf{BQP}_1^{G_2}\) verifiers with clean all-zero inputs, one computational-basis output measurement, perfect completeness, and soundness at most \(1/3\);
2. the corrected geometric transfer theorem, including its finite gadget certificates and all-chain concentration conclusion.

Then there is a polynomial mapping from an input \(x\) to nested weighted clique complexes

\[
X_{\rm in}(x)\subseteq X_{\rm out}(x)
\]

and a common degree \(d\), such that

\[
\beta_d(X_{\rm in})=D,
\]

\[
\beta_d(X_{\rm out})
=
\operatorname{rank}
\left[
H_d(X_{\rm in})\to H_d(X_{\rm out})
\right]
=
\dim\ker(I-M_x),
\]

and hence

\[
q_x:=
\frac{\beta_d(X_{\rm in}\to X_{\rm out})}
{\beta_d(X_{\rm in})}
=
\begin{cases}
3/4,&x\in L,\\[1mm]
1/8,&x\notin L.
\end{cases}
\]

Both endpoint degree-\(d\) Laplacians have inverse-polynomial gaps above their complete kernels. Under the theorem’s conservative locality-six parameters, the weighted gap floor remains

\[
E=\Omega\!\left(\frac{\eta^{28}g}{t^{26}}\right),
\]

with the history-Hamiltonian \(g\) inverse polynomial. The exact geometric conclusions being invoked are those stated in the supplied restricted theorem. 〔PRO_BQP1_SOURCE_PACKET_2026-09-…〕

The midpoint of the two target values is

\[
\theta=\frac{3/4+1/8}{2}=\frac7{16}.
\]

Any additive error

\[
\varepsilon<\frac{3/4-1/8}{2}=\frac5{16}
\]

suffices. In particular, error \(1/24\) is safely sufficient. Thus the promise-decision version obtained by thresholding at \(7/16\), and the corresponding additive-approximation problem, are conditionally

\[
\boxed{\mathsf{BQP}_1^{G_2}\text{-hard}.}
\]

# 6. Covered cyclotomic gate families

I did not check the cited Rudolph results. Under the supplied statements:

- Theorem 3.4 gives, for every fixed finite gate set \(\mathcal G\) over the covered power-of-two cyclotomic fields,
   
   \[
   \mathsf{BQP}_1^{\mathcal G}
   \subseteq
   \mathsf{BQP}_1^{G_2}.
   \]
- Theorem 2.3 supplies exact soundness reduction to the required constant while preserving perfect completeness for gate sets containing \(G_2\).

Therefore, for each such fixed \(\mathcal G\), compose:

\[
\mathsf{BQP}_1^{\mathcal G}
\longrightarrow
\mathsf{BQP}_1^{G_2}
\longrightarrow
\text{eight-label source}
\longrightarrow
\text{weighted true normalized persistence}.
\]

Subject to those source statements being uniform and polynomial-overhead as supplied, the target is also

\[
\boxed{\mathsf{BQP}_1^{\mathcal G}\text{-hard}}
\]

for every covered fixed gate family separately.

This is not a gate-independent \(\mathsf{BQP}_1\) theorem covering arbitrary exact gates.

# 7. Why the earlier obstruction is avoided

The same-fraction obstruction concerned trace distinctions carried entirely by eigenvalues strictly below one. This construction starts from perfect completeness:

\[
p_x=1
\quad\text{versus}\quad
p_x\le\frac13.
\]

The five conditional label blocks become exact eigenvalue-one blocks precisely when \(p_x=1\). In the NO case they remain strictly below one. The construction therefore deliberately converts perfect completeness into a perfect-space multiplicity difference.

It does **not** repair arbitrary-threshold \(\mathsf{SDQC}_1\). If both promise cases had \(p_x<1\), all five conditional blocks would be nonperfect in both cases, and both perfect fractions would equal \(1/8\), regardless of the trace gap.

# Status table

| Claim | Status |
| --- | --- |
| Eight-label compressed operator identity | **Proved** |
| Robustness to coherent labels and verifier garbage | **Proved** |
| Exact \(G_2\) gate compatibility | **Proved** |
| Fractions \(3/4\) versus \(1/8\) | **Proved** |
| Growing denominator via idle mixed bits | **Valid**, though padding-generated |
| Weighted true-normalized-persistence hardness for \(\mathsf{BQP}_1^{G_2}\) | **Valid conditional on the supplied geometric theorem** |
| Hardness for each covered cyclotomic \(\mathsf{BQP}_1^{\mathcal G}\) | **Conditional on supplied Rudolph Theorems 2.3 and 3.4** |
| Rudolph source statements | **Not independently checked here** |
| Unweighted conclusion | **Not concluded in this gate** |
| Ordinary BQP or unrestricted SDQC1 hardness | **Not implied** |
| Novelty or paper readiness | **Not assessed** |

The packet itself applies the same firewall between the limited gate-dependent result and the withheld stronger claims. 〔PRO_BQP1_SOURCE_PACKET_2026-09-…〕

# Next finite gate

Independently verify Rudolph’s Definition 2.2 and Theorems 2.3 and 3.4 at the exact interface needed here: uniformity, polynomial overhead, clean all-zero initialization, one computational-basis output bit, preservation of perfect completeness, final soundness at most \(1/3\), and exact use of \(G_2\) without hidden controlled gates or approximate compilation.
