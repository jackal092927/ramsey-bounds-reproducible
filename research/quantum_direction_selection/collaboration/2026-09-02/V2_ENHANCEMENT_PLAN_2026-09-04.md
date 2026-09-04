# Version 2 enhancement plan for the normalized persistence paper

September 4, 2026. **RESEARCH MEMO WITH PROOFS.** Version 1 is frozen at git
tag `normalized-persistence-v1` (commit `20c0f00`). Everything below is
additional; nothing here changes a v1 theorem. Each result was derived
independently in this session and, where finite data is involved, checked
against the certificate files (`check_filling_domination.py`,
`check_harmonic_overlap.py`, outputs in `V2_CHECK_OUTPUTS_2026-09-04.txt`).

## 0. Summary of what can be gained

| # | Result | Status | Impact |
|---|---|---|---|
| 1 | Exponent 26 → 10, from filling depth; locality \(m\) disappears from the theorem | Proved (Section 2); numerically tight | Quantitative, cleaner theorem |
| 2 | Harmonic spaces are \(O(\lambda\sqrt t)\)-close to logical kernels; large-overlap condition holds with \(a_{\min}\ge1-O(\eta)\); uniform harmonic mixture preparable | Proved (Section 3); numerically confirmed | Turns hardness into hard-and-in-BQP ("provable advantage" framing) |
| 3 | General source: perfect-subspace-fraction class \(\mathsf{SF}^{G_2}\); hardness with \(2^r\) intrinsic initial holes; SDQC\(_1^{G_2}\)-hardness in the fraction form used by Lowe et al.'s own proofs | Proved (Section 4) | Headline: Conjecture 1 of Lowe et al. over \(G_2\) in the form their Theorem 7 uses; kills the "denominator 8" objection |
| 4 | Exact Betti numbers of gapped clique complexes are #P-complete (weakly parsimonious), weighted and unweighted | Proved (Section 5) | New standalone result; closes the gap-promise question left by Crichigno–Kohler |
| 5 | Multi-level filtrations: normalized barcode profile hardness | Immediate corollary (Section 6) | Minor |
| 6 | Extension of the \(\mathsf{SF}\) source to all cyclotomic gate sets | Plausible, unverified (Section 7) | Would remove most gate dependence |

Recommended v2 headline: *Normalized persistence of clique complexes is
hard for perfect-completeness classes with exponentially many initial holes,
and the hard instances are solvable in BQP; exact Betti numbers of gapped
clique complexes are #P-complete.*

---

## 1. Notation

As in v1: register \(R\) (join of bowties), \(V=Z_d(R)\), gadget \(Y_j\)
with private weight \(\lambda\), padded projector \(\Pi_j=\pi_j\otimes I\),
\(H_A=\sum_{j\in A}\Pi_j\), \(K_A=\ker H_A\), \(W_A=K_A^\perp\), full
Laplacian \(\Delta_A\), harmonic space \(\cH_A=\ker\Delta_A\subseteq C_d(X_A)\).
Theorem 3.3 of v1 gives, for unit \(x\),
\[
\|(I-P_{K_A})x\|^2\le C\Bigl[t_A\lambda^2+\frac{\langle x,\Delta_Ax\rangle}{g_A\lambda^\kappa}\Bigr].
\tag{T}
\]
Theorem 4.2 of v1 gives \(H_d(X_A)\cong V/W_A\) naturally.

---

## 2. Result 1: the exponent is the filling depth

**Lemma 2.1 (Schur-complement filling bound).** Let \(A\succeq0\), let
\(v\in\ran A\), and let \(u\) satisfy \(A^{1/2}\)-preimage
\(\langle v,A^{+}v\rangle\le\|u\|^2\) (for \(A=\partial\partial^*\) this holds
for any \(u\) with \(\partial u=v\), because
\(\langle v,(\partial\partial^*)^+v\rangle=\min\{\|u\|^2:\partial u=v\}\)).
Then for every \(y\),
\[
\langle y,Ay\rangle\ \ge\ \frac{|\langle v,y\rangle|^2}{\|u\|^2}.
\]
*Proof.* Cauchy–Schwarz:
\(|\langle v,y\rangle|^2=|\langle A^{+1/2}v,A^{1/2}y\rangle|^2\le\langle v,A^+v\rangle\langle y,Ay\rangle\). \(\square\)

**Lemma 2.2 (padded version).** Let \(c_1\in C_{d_a+1}(Y_a;\mathbb Z)\) be the
certified integer filling of the integer register cycle \(v_a\) (so
\(\partial c_1=v_a\), unweighted), and let
\(p_a=\max\{\#\text{private vertices of }\sigma:\ c_1(\sigma)\ne0\}\) be its
*filling depth*. In weighted coordinates \(c_a(\lambda)=W^{-1}_{d_a+1}c_1\)
fills \(v_a\), and \(\|c_a(\lambda)\|^2=\sum_\sigma c_1(\sigma)^2\lambda^{-2\,\mathrm{priv}(\sigma)}\le\|c_1\|^2\lambda^{-2p_a}\) for \(\lambda\le1\).
For the padded gadget and any unit \(x=(v_a/\|v_a\|)\otimes h\) with
\(h\in\cH_{\rm out}\) a unit outside harmonic, \(u=(c_a(\lambda)/\|v_a\|)\otimes h\)
satisfies \(\partial u=x\) and \(\|u\|^2=\|c_a(\lambda)\|^2/\|v_a\|^2\)
(outside weights are one and \(\partial h=0\)). Hence, with
\(\Delta_j^\uparrow=\partial_{d+1}\partial_{d+1}^*\) of the padded gadget
\(j\) of type \(a\), Lemma 2.1 applied with \(v=x=\Pi_jy/\|\Pi_jy\|\) gives
\[
\boxed{\ \Delta_j^\uparrow\ \succeq\ \frac{\|v_a\|^2}{\|c_1\|^2}\,\lambda^{2p_a}\ \Pi_j\ }.
\]
*Proof.* For \(y\) with \(\Pi_jy\ne0\), put \(x=\Pi_jy/\|\Pi_jy\|\in\ran\Pi_j\); then
\(\langle y,\Delta_j^\uparrow y\rangle\ge|\langle x,y\rangle|^2/\|u\|^2=\|\Pi_jy\|^2\|v_a\|^2/\|c_a(\lambda)\|^2\). \(\square\)

**Consequence.** Summing over gadgets (the global up-Laplacian is the exact
sum of the embedded local ones, v1 Appendix A.4):
\[
\Delta_A^\uparrow\succeq c_{\rm fill}\,\lambda^{2p}\,H_A^{\rm emb},\qquad
p=\max_a p_a,\quad c_{\rm fill}=\min_a\|v_a\|^2/\|c_1^{(a)}\|^2 .
\]
This replaces v1's (logical-domination) with \(\kappa=4m+2\) by
\(\kappa=2p\). Nothing else in the proof of (T) uses \(\kappa\); the final
absorption needs only \(\kappa\ge2\), i.e. \(p\ge1\), which holds since every
filling simplex has a private vertex. **Theorem 3.3 therefore holds with
\(\kappa=2p\), independent of the locality \(m\), and Lemma 3.2(local-gap) is
no longer needed.**

**Guards and padding do not increase \(p\).** The selected-cycle guard fills
\(v\otimes\gamma_\beta\) by \(c_1\otimes\gamma_\beta\) (v1 Appendix C), and the
outside harmonic padding tensors with register cycles; neither adds private
vertices to any filling simplex.

**Palette values (from the certificate files).**

| Atom | \(d_a\) | filling terms | depth \(p_a\) | \(2p_a\) | v1 crude \(2d_a+4\) |
|---|---|---|---|---|---|
| basis cone \(v*S_\beta\) | 1 | 4 | 1 | 2 | 6 |
| \(\ket0-\ket1\) (`state_0m1`) | 1 | 24 | 3 | 6 | 6 |
| \(\ket{00}-\ket{11}\), \(\ket{01}-\ket{10}\) | 3 | 248 | 5 | 10 | 10 |
| four gain/loss atoms (`state_00m10m11` orbit) | 3 | 382 | 5 | 10 | 10 |

So \(p=5\), \(\kappa=10\) for the whole palette, versus \(\kappa=26\) in v1
(v1 paid for the guard qubits through \(m=6\)). The numerical check
`check_filling_domination.py` confirms: the operator inequality holds to
machine precision for \(\lambda\in\{1/2,\dots,1/16\}\), and the *optimal*
constant \(1/\langle\hat v,(\Delta^\uparrow)^+\hat v\rangle\) scales exactly as
\(\lambda^{2p_a}\) (ratios \(0.54\lambda^{10}\), \(0.56\lambda^{10}\),
\(0.99\lambda^{6}\)), so the bound is tight up to constants for these
gadgets. New parameter scale:
\[
E_A=\Omega\!\left(\frac{\eta^{12}g_A}{t_{\max}^{10}}\right),\qquad
FE=\Omega\!\left(\frac{\eta^{10}g}{t_{\max}^{8}}\right)\ \text{(unweighted)}.
\]
A further improvement would need gadgets with shallower fillings; the depth
\(5\) atoms are Rudolph's and appear optimal for them (numerically).

---

## 3. Result 2: harmonic spaces track logical kernels; large overlap; preparation

**Lemma 3.1 (harmonic concentration).** Under the hypotheses and parameter
choice of v1 Theorem 3.3 (with \(\lambda\le c_1\eta/\sqrt{t_{\max}}\)), every
unit \(x\in\cH_A\) satisfies \(\|(I-P_{K_A})x\|\le\eta_1:=\sqrt C c_1\eta\).
*Proof.* (T) with \(\langle x,\Delta_Ax\rangle=0\). \(\square\)

**Lemma 3.2 (equal dimensions give a projector bound).** If
\(\dim\cH=\dim K<\infty\) and \(\|(I-P_K)x\|\le s<1\) for all unit \(x\in\cH\),
then \(\|P_\cH-P_K\|\le s\), and the singular values of \(P_KP_\cH\) are all
at least \(\sqrt{1-s^2}\).
*Proof.* \(P_K|_\cH\) has all singular values \(\ge\sqrt{1-s^2}>0\), so it is
injective, so \(P_K\cH=K\) by dimension count; the principal angles
\(\theta_i\) between \(\cH\) and \(K\) satisfy \(\sin\theta_i\le s\), and
\(\|P_\cH-P_K\|=\sin\theta_{\max}\) for equal-dimensional subspaces. \(\square\)

Since \(\dim\cH_A=\dim K_A\) (v1 Theorem 3.3), Lemmas 3.1–3.2 give
\[
\|P_{\cH_A}-P_{K_A}\|\le\eta_1\quad\text{for every }A\in\mathcal A.
\tag{3.1}
\]

**Theorem 3.3 (large overlap).** For \(A\subseteq B\) in \(\mathcal A\), the
nonzero eigenvalues of \(P_{\cH_B}P_{\cH_A}P_{\cH_B}\) are all at least
\((1-2\eta_1)^2\); there are exactly \(\dim K_B\) of them.
*Proof.* \(K_B\subseteq K_A\) gives \(P_{K_B}P_{K_A}=P_{K_B}\). By (3.1),
\(\|P_{\cH_B}P_{\cH_A}-P_{K_B}\|\le\|P_{\cH_B}-P_{K_B}\|+\|P_{\cH_A}-P_{K_A}\|\le2\eta_1\).
Weyl's inequality for singular values: the singular values of
\(P_{\cH_B}P_{\cH_A}\) are within \(2\eta_1\) of those of \(P_{K_B}\), which are
\(1\) (\(\dim K_B\) times) and \(0\). By v1 Theorem 4.2 the rank of
\(P_{\cH_B}|_{\cH_A}\) (the induced map on homology) is exactly \(\dim K_B\),
so exactly \(\dim K_B\) singular values are nonzero, each \(\ge1-2\eta_1\).
The nonzero eigenvalues of \(P_{\cH_B}P_{\cH_A}P_{\cH_B}\) are their squares.
\(\square\)

This is precisely the *large overlap condition* of Lowe et al.
(Definition 3) for the pair \((P_{\cH_2},\cH_1)\), with
\(a_{\min}\ge(1-2\eta_1)^2\ge1-4\eta_1\), a constant close to \(1\) (with
\(\eta_0=1/10\) and \(Cc_1^2\le1/4\): \(a_{\min}\ge4/5\)); it can be made
\(1-1/\mathrm{poly}\) by choosing \(\eta=1/\mathrm{poly}\).

**Theorem 3.4 (preparation of the initial harmonic mixture).** The
reduction can output a polynomial-size circuit \(\mathcal P\) and the
following holds. Let \(\rho_{K_{\rm in}}\) be the uniform mixture over
\(K_{\rm in}=\mathcal V C\subseteq C_d(X_{\rm in})\) (embedded history
states) and \(\rho_{\cH_{\rm in}}\) the uniform mixture over \(\cH_{\rm in}\).
(a) \(\mathcal P\) prepares \(\rho_{K_{\rm in}}\) exactly up to the
\(1/\mathrm{poly}\) synthesis error of its real amplitudes.
(b) Projecting the output of \(\mathcal P\) onto \(\cH_{\rm in}\) by phase
estimation of \(\Delta_{\rm in}\) at resolution below \(\gamma_{\rm in}\)
succeeds with probability \(\ge1-\eta_1^2\) and returns a state
\(\tilde\rho\) with \(\|\tilde\rho-\rho_{\cH_{\rm in}}\|_1\le2\eta_1^2/(1-\eta_1^2)+1/\mathrm{poly}\).
*Proof.* (a) Three steps. (i) Prepare the maximally mixed state on the
\(r\) mixed qubits, the fixed clean string, and the clock state
\(Z^{-1/2}\sum_ts_t\ket t\) in unary (a fixed two-valued real amplitude
pattern; exact over \(\mathbb Q(\sqrt2)\), approximable to \(1/\mathrm{poly}\)
over any universal gate set). (ii) Apply \(\widehat U_t=U_t\otimes\Pi^c_{\ge t}+I\otimes(I-\Pi^c_{\ge t})\)
for \(t=1,\dots,L-1\), exactly as in Lowe et al., Lemma 8, where the split
Hadamard steps apply the unitary \(H\) (the scalars \(\sqrt2,1/\sqrt2\) are
already in \(s_t\)); this produces \(\rho_{\rm hist}=\mathcal V\rho_C\mathcal V^*\)
on qubits. (iii) Map each register qubit basis state \(\ket{b}\) to the
normalized oriented petal cycle \(\gamma_b\in C_1(\text{bowtie})\), a fixed
isometry \(\C^2\to\C^{8}\) onto the edge labels of that bowtie; the tensor
product over the \(n\) register qubits (clock and work) is the isometric
embedding \((\C^2)^{\otimes n}\cong V\subseteq C_d(R)\subseteq C_d(X_{\rm in})\)
of v1 Section 2, up to the fixed orientation signs of join simplices, which
are computed classically from the vertex order and applied as phases. The
result is \(\rho_{K_{\rm in}}\). (b) \(\mathrm{Tr}(P_{\cH_{\rm in}}\rho_{K_{\rm in}})=\frac1D\mathrm{Tr}(P_{\cH}P_K)=\frac1D\sum_i\cos^2\theta_i\ge1-\eta_1^2\)
by Lemma 3.2. The post-measurement state is
\(\sum_i\frac{\cos^2\theta_i}{\sum_j\cos^2\theta_j}\ket{h_i}\!\bra{h_i}\) in an
orthonormal basis of \(\cH_{\rm in}\) (the eigenbasis of \(P_\cH P_KP_\cH\)),
whose eigenvalues lie in \([(1-\eta_1^2)/D,\,1/((1-\eta_1^2)D)]\); the trace
distance to \(\rho_{\cH_{\rm in}}\) is therefore at most \(2\eta_1^2/(1-\eta_1^2)\).
Phase estimation of the sparse, explicitly given \(\Delta_{\rm in}\) with
\(1/\mathrm{poly}\) resolution is standard quantum TDA (Lloyd–Garnerone–Zanardi;
McArdle–Gilyén–Berta). \(\square\)

**Unweighted transfer.** For the common-copy blow-up, \(\widehat{\cH}_i=U_i\cH_i\)
and \(\widehat J U_{\rm in}=U_{\rm out}J\), so
\(P_{\widehat\cH_{\rm out}}P_{\widehat\cH_{\rm in}}=U_{\rm out}(P_{\cH_{\rm out}}P_{\cH_{\rm in}})U_{\rm out}^*\):
the large-overlap constant is unchanged. The preparation circuit is composed
with the lift isometry \(\ket\sigma\mapsto\bigotimes_{v\in\sigma}\bigl(f_v^{-1/2}\sum_{i\le f_v}\ket{v_i}\bigr)\),
which is exact since \(F=2^{2b}\) is a power of two (Hadamards on the copy
index qubits). Hence everything in this section holds for the unweighted
instances of v1 Corollary 6.1.

**Theorem 3.5 (hard and in BQP).** *Normalized harmonic persistence
(Problem 9 of Lowe et al.; v1 Definition 2.1), for weighted or unweighted
clique complexes, remains \(\BQPone^{G_2}\)-hard (and \(\mathsf{SF}^{G_2}\)-hard,
Section 4) even when restricted to instances for which (a) the large overlap
condition holds for \((P_{\cH_2},\cH_1)\) with \(a_{\min}\ge1-1/\mathrm{poly}\)
and (b) the uniform mixture over \(\cH_1=\ker\Delta_{1,d}\) can be prepared to
trace distance \(1/\mathrm{poly}\) by a polynomial-size circuit computable from
the instance. Under (a) and (b) the problem is in \(\BQP\) by Lowe et al.,
Lemma 7 (whose proof is linear in the prepared state and tolerates the
\(1/\mathrm{poly}\) preparation error).*
*Proof.* v1 Theorem 5.3 / Corollary 6.1 plus Theorems 3.3–3.4. \(\square\)

This is the same "hard even when the containment conditions hold" format as
Theorems 5, 7 and 8 of Lowe et al., and it is the standard evidence format
for exponential quantum advantage in this literature (Gyurik–Cade–Dunjko;
Gyurik et al.). Numerical confirmation on the real \(\ket0-\ket1\) atom
(`check_harmonic_overlap.py`): \(\|(I-P_V)h\|\approx0.65\lambda\) and the
overlap singular value is \(1-O(\lambda^2)\) (\(0.9998\) at \(\lambda=1/32\)).

**Remark (approximate Conjecture 2 of Lowe et al.).** (3.1) says that the
harmonic encodings \(E_i:=P_{\cH_i}|_{K_i}\) are \(\eta_1\)-approximate
isometries compatible with the inclusion; so the "functoriality" clause of
their Conjecture 2 holds up to \(O(\eta)\) in operator norm, while the exact
rank identity holds by the quotient argument. Worth one sentence in v2.

---

## 4. Result 3: the perfect-subspace-fraction source and SDQC\(_1\)

**Definition 4.1 (\(\mathsf{SF}^{G}\)).** For a finite gate set \(G\), a
promise problem \(L\) is in \(\mathsf{SF}^{G}(a,b)\) (\(a-b\ge1/\mathrm{poly}\))
if there are polynomials \(c,r\) and a uniform family of exact \(G\)-circuits
\(U_x\) on \(c(n)\) clean qubits (initialized to a fixed string) and \(r(n)\)
maximally mixed qubits, with a computational-basis acceptance measurement
\(P_{\rm acc}\), and subspaces \(S_x\subseteq(\C^2)^{\otimes r}\) with:
(i) every state of \(S_x\) is accepted with probability \(1\);
(ii) every state of \(S_x^\perp\) is accepted with probability \(\le1/3\);
(iii) \(\dim S_x/2^{r}\ge a\) if \(x\in L_{\rm yes}\) and \(\le b\) if \(x\in L_{\rm no}\).

Facts. (1) \(S_x=\ker(I-M_x)\) for \(M_x=J^*U_x^*P_{\rm acc}U_xJ\), and
\(M_x|_{S_x^\perp}\preceq\frac13I\) (v1 Appendix B.5 argument: a unit
\(\psi=s+s'\) with \(M\psi=\psi\) forces \(Ms'=s'\), contradicting (ii) unless
\(s'=0\)). (2) \(\BQPone^{G_2}\subseteq\mathsf{SF}^{G_2}(3/4,1/8)\) by the
eight-label predicate of v1 (three mixed labels). (3) The one-clean-qubit
restriction of \(\mathsf{SF}^{G}\) is exactly Lowe et al.'s \(\mathsf{SDQC}_1^{G}\)
with the decision condition imposed on the fraction \(\dim S_x/2^{q-1}\)
instead of on the acceptance probability of the maximally mixed state; call
it \(\mathsf{SDQC}_1^{G}[\mathrm{frac}]\). (4) Trace versus fraction: with
\(f=\dim S/2^r\) and \(p=\mathrm{Tr}M/2^r\), \(f\le p\le\frac{1+2f}{3}\)
(v1 Appendix B.5). Hence a trace promise \(p\ge a\) / \(p\le b\) implies the
fraction promise \(f\ge\frac{3a-1}{2}\) / \(f\le b\), which is nontrivial iff
\(b<\frac{3a-1}{2}\). (5) Conversely, by eq. (9) of Lowe et al., after
Marriott–Watrous amplification the acceptance probability of the maximally
mixed state lies in \([f,f+1/\mathrm{poly}]\), so
\(\mathsf{SDQC}_1^{G}[\mathrm{frac}]\subseteq\mathsf{SDQC}_1^{G}\) whenever
amplification is available in \(G\). (6) The proofs of Theorems 5 and 7 of
Lowe et al. decide the instance from an estimate of \(\dim S_x/2^{N-1}\)
(their Section 5.5, last paragraph: "estimation of \(\dim S/2^{N-1}\) within
\(\epsilon<(a-b)/3\) is sufficient to solve the original SDQC\(_1\)
instance"); that inference uses the fraction promise, since the acceptance
probability of the *original* verifier is not preserved by amplification.
So the class for which their local-Hamiltonian hardness results are proved
is \(\mathsf{SDQC}_1[\mathrm{frac}]\). (This should be stated neutrally in v2:
"the decision condition used in those proofs".)

**Theorem 4.2 (general hardness).** For every \(a-b\ge1/\mathrm{poly}\), the
v1 construction is a deterministic polynomial-time many-one reduction from
\(\mathsf{SF}^{G_2}(a,b)\) to normalized harmonic persistence with additive
error \(\varepsilon<(a-b)/2\), weighted or unweighted, with
\[
\beta_d(X_{\rm in})=2^{r},\qquad
\beta_d(X_{\rm in}\to X_{\rm out})=\dim S_x,\qquad
q_d=\dim S_x/2^{r},
\]
inverse-polynomial endpoint gaps, and (Section 3) large overlap and
preparable initial harmonic mixture.
*Proof.* v1 Proposition 5.2 is stated for an arbitrary clean-input space
\(C\) with \(D=\dim C\); take \(C=\ket{\rm clean}\otimes(\C^2)^{\otimes r}\),
\(D=2^r\). Fact (1) supplies \(M|_{S^\perp}\preceq I/3\), so the output gap
\(g_{\rm out}\ge1/(27L^3)\) holds. Theorems 3.3 and 4.2 of v1 give the
Betti numbers and the induced rank; Lemma 5.1 (palette) covers all \(G_2\)
gates. Precision: the YES/NO values are separated by \(a-b\). \(\square\)

**Corollary 4.3 (SDQC\(_1\)).** Normalized harmonic persistence is
\(\mathsf{SDQC}_1^{G_2}[\mathrm{frac}]\)-hard for all thresholds, and
\(\mathsf{SDQC}_1^{G_2}\)-hard (trace form, Definition 2 of Lowe et al.) for all
thresholds with \(b<(3a-1)/2\), for instance \((a,b)=(2/3,1/3)\) with target
error \(1/24\). In particular Conjecture 1 of Lowe et al. holds over the gate
set \(G_2\) in the fraction form used in their Theorems 5 and 7.

**Why this matters for v2.** (i) The initial Betti number is \(2^{q-1}\), the
full dimension of the mixed register, and the surviving fraction is the
genuinely hard quantity \(\dim S_x/2^{q-1}\): this answers the "denominator
8" objection intrinsically. (ii) The eight-label theorem becomes a
corollary rather than the main statement. (iii) The gate-set caveat is
exactly the one Lowe et al. attach to SDQC\(_1\) themselves ("no known general
perfect-completeness preserving reduction among different gate sets").

---

## 5. Result 4: exact Betti numbers of gapped clique complexes are #P-complete

**Definition.** GappedBetti: input a graph \(G\) (with or without dyadic
vertex weights), \(d\), and rational \(\gamma\ge1/\mathrm{poly}\); promise
\(\spec(\Delta_{\Cl(G),d})\subseteq\{0\}\cup[\gamma,\infty)\); output
\(\beta_d(\Cl(G))\).

**Theorem 5.1.** GappedBetti is #P-hard under polynomial-time parsimonious
reductions (from #SAT), for weighted and for unweighted clique complexes,
and it is in #P (equivalently, #BQP-complete under weakly parsimonious
reductions, Brown–Flammia–Schuch). Moreover the same holds for the
persistent Betti number \(\beta_d(X_1\to X_2)\) of gapped filtrations.
*Proof.* Hardness: given a Boolean formula \(\varphi\) on \(r\) variables,
compile its evaluation into a reversible circuit over \(\{X,\CX,\CCX\}\subset G_2\)
with the \(r\) variables on the mixed register, clean ancillas, and the
decision bit as \(P_{\rm acc}\). Then \(M_\varphi\) is diagonal with entries
\(\varphi(z)\in\{0,1\}\); \(S=\mathrm{span}\{\ket z:\varphi(z)=1\}\),
\(\dim S=\#\varphi\), and \(M|_{S^\perp}=0\preceq I/3\). Theorem 4.2 (with
only the two-term atoms and cones of the palette) gives \(X_{\rm out}\) with
\(\beta_d(X_{\rm out})=\#\varphi\), an inverse-polynomial gap above the kernel,
and also \(\beta_d(X_{\rm in}\to X_{\rm out})=\#\varphi\) with
\(\beta_d(X_{\rm in})=2^r\). Containment: with the gap promise, \(\beta_d\) is
the number of zero eigenvalues of a Hamiltonian with a \(1/\mathrm{poly}\) gap,
which is in #BQP (Cade–Crichigno, discussion after their Theorem 5) and
#BQP \(=\) #P under weakly parsimonious reductions (Brown–Flammia–Schuch).
\(\square\)

**Relation to prior work.** Crichigno–Kohler (Theorem 4) prove #P-hardness
of Betti numbers of clique complexes *without* a gap promise and note that
their instances need not be gapped; Cade–Crichigno (Theorem 5) prove
#P-completeness with a gap for general cochain complexes with 6-local
coboundaries, not clique complexes; King–Kohler and Hayakawa treat the
decision problem (\(\beta=0\) vs \(>0\)). The gapped *clique-complex*
counting statement appears to be new, and it is a two-line corollary of the
degenerate-kernel transfer theorem. It also clarifies the quantum-advantage
discussion (Schmidhuber–Lloyd, Berry et al.): even with the spectral gap that
makes the *normalized* Betti number \(\beta_d/|X_d|\) estimable, the exact
Betti number stays #P-hard. Check Schmidhuber–Lloyd's exact-Betti
statements before claiming novelty of the unweighted gapped case.

**Quantum-source version.** Replacing \(\varphi\) by a \(G_2\) verifier with
perfect subspace \(S_x\) and soundness \(1/3\) on \(S_x^\perp\) shows that
GappedBetti is hard for \(\#\BQPone^{G_2}\) (the perfect-completeness counting
class of Cade–Crichigno restricted to \(G_2\)), parsimoniously.

---

## 6. Result 5: normalized barcode profiles (minor)

For a chain \(A_0\subseteq\dots\subseteq A_s\) of term sets, v1 Theorem 4.2
gives \(\rank[H_d(X_{A_i})\to H_d(X_{A_j})]=\dim K_{A_j}\). With the
eight-label source one can add rejection terms level by level (accept label
sets \(\Lambda_1\supseteq\Lambda_2\supseteq\cdots\)) so that the vector of
normalized persistences \((q_d(X_0,X_j))_j\) equals a prescribed affine
function of \([p_x=1]\) at every level. Hence estimating any single entry of
the normalized barcode profile, or the average persistence
\(\frac1s\sum_jq_d(X_0,X_j)\), is \(\BQPone^{G_2}\)-hard under endpoint gaps at
every level. One paragraph in v2 at most.

---

## 7. Result 6 (unverified): more gate sets for the fraction source

Rudolph's Theorem 3.4 (\(\BQPone^{G}\subseteq\BQPone^{G_2}\)) is proved with a
postselection-based exact gate simulation in which the verifier accepts when
postselection fails. For an \(\mathsf{SF}\) verifier, this transformation keeps
every state of \(S_x\) perfectly accepted and, if the simulation's failure
probability is input-independent and \(\le2^{-m}\) (Rudolph Lemma 3.14), bounds
the acceptance on \(S_x^\perp\) by \(1/3+2^{-m}\), while the perfect subspace
stays exactly \(S_x\) (any perfectly accepted state must be accepted in the
success branch, which implements \(U_x\) exactly). If these two properties
hold as stated, then \(\mathsf{SF}^{G}\)-hardness follows for every finite
\(G\subseteq\mathbb Q(\zeta_{2^k})\), e.g. Clifford\(+T\), and Corollary 4.3
extends accordingly; the required soundness constant in v1 Proposition 5.2
becomes \(r=1/3+2^{-m}\), which changes only the constant in \(g_{\rm out}\).
This needs a careful reading of Rudolph Sections 3.2–3.4 and is not claimed.

---

## 8. What stays open

- Unrestricted (gate-independent) SDQC\(_1\)-hardness; ordinary BQP-hardness.
- Whether the trace-form SDQC\(_1\) with arbitrary thresholds reduces to the
  fraction form (the obstruction in v1 Appendix B.5 shows it cannot be done
  by any transformation that sees only \(f\)).
- Persistent-Laplacian gaps on the hard instances (not needed for Theorem
  3.5, since containment goes through Lemma 7 of Lowe et al.).
- A palette with shallower fillings (would push \(\kappa\) below 10).

---

## 9. Suggested v2 structure

1. Introduction: three headline theorems — (A) \(\mathsf{SF}^{G_2}\)/SDQC\(_1\)
   fraction hardness with \(2^r\) initial holes, containing \(\BQPone^{G_2}\);
   (B) hard even under the containment conditions, hence hard-and-in-BQP on
   the instance family; (C) gapped clique Betti numbers #P-complete. Then
   the transfer theorem with \(\kappa=2p=10\) and quotient naturality as the
   engine.
2. Section 3: transfer theorem, with the filling-depth constant replacing
   Lemma 3.2's crude exponent (keep the padding lemma).
3. Section 5: general source \(\mathsf{SF}^{G_2}\), Proposition 5.2 unchanged,
   Theorem 4.2 above, Corollary 4.3, eight-label corollary, counting corollary.
4. New Section 6: harmonic concentration, large overlap, preparation, BQP
   containment on the family.
5. Section 7 (unweighted) unchanged plus the two transfer remarks.
6. Related work: add the neutral sentence about the fraction condition in
   Lowe et al.'s proofs, and the Crichigno–Kohler / Cade–Crichigno counting
   comparison.

Title candidate: *Normalized Persistence and Gapped Betti Numbers of Clique
Complexes: Hardness with Exponentially Many Holes via Exact Kernel Transfer.*
