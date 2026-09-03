# Pro bounded concentration review — complete response

Collected 2026-09-03T16:26:26.285Z. The browser showed a completed response, **Worked for 8m 39s**, after user message 4 and the bounded attachment; no Stop answering control was present. This is an external model review, not an independent correctness or source certificate.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: f4ec1b73ca99fa909b728e8165fb3e87fa9214b3.
- Actual task: [bounded submission](PRO_BOUNDED_PROOF_SUBMISSION_2026-09-03.md).
- Input: [PRO_BOUNDED_PROOF_PACKET_2026-09-03.md](PRO_BOUNDED_PROOF_PACKET_2026-09-03.md), 15805 bytes, SHA-256 034eeb1c1c3bdd86405db1a086ff23251ef06cbad63ed33ce88fd6651505e1a2.
- The visible personal account matched the local channel registry. Account email is omitted from this public archive.
- Exact browser completion timestamp was not exposed; collection time and displayed duration are separate facts.

The entire response below was transcribed from its rendered DOM. All **138** equation elements were recovered from displayed `data-math-source` attributes; headings, lists and emphasis were retained. The four visible attachment citation labels are preserved as 〔…〕. The answer contains no external links. [The capture record](PRO_BOUNDED_PROOF_REVIEW_CAPTURE_2026-09-03.json) retains the original displayed text and all equation sources. No new primary literature checking was performed during collection. Any adopted conclusions are recorded separately in the disposition.

---

# Verdict


The implication is **valid under the hypotheses stated in the bounded packet**. I find no counterexample satisfying all of them.


Two justifications were compressed rather than false:


1. the nonzero-singular-value inequality under invertible diagonal scaling remains valid for rank-deficient boundaries, but it needs a distance-to-kernel proof;

2. the padding argument must be stated over **all** join bidegrees. Once that is done, the unique outside-harmonic bidegree is indeed the only one contributing to the zero-weight kernel.


No estimate involving the unknown geometric harmonic projector is used before the min–max step. The logical operator \(H\) and geometric Laplacian \(\Delta_X\) remain distinct throughout. The theorem is conditional on the finite local certificate; this audit says nothing about complete palette closure, novelty, or paper readiness. The governing statement and hypotheses are those in the attached note. 〔PRO_BOUNDED_PROOF_PACKET_2026-0…〕



---


# Conditional concentration theorem


Let \(t\ge1\), \(0<g\le1\), and let \(P\) project onto the embedded logical register cycle space \(V\). Let



\[
H=\sum_{i=1}^t\Pi_i
\quad\text{and}\quad
H\succeq g(P-P_K),
\]


where \(P_K\) projects onto \(\ker H\subseteq V\).


Assume the fixed finite gadget palette satisfies:


- exact filling



  \[
  B_d(Y_i)\cap V=\operatorname{ran}\Pi_i;
  \]

- independent gadget interiors and no register \((d+1)\)-simplices;

- after padding, the zero-weight differential pair satisfies



  \[
  \ker D_{i,0}=V\oplus Q_i
  \]


  orthogonally, with a palette-uniform positive gap on its complement;

- a projected private pair



  \[
  T_i(\lambda)=\lambda T_{i,1},\qquad
  T_{i,1}P=0,\qquad
  \|T_{i,1}Q_iz\|\ge b\|Q_iz\|;
  \]

- retained \(T_i\)-outputs are private to gadget \(i\);

- the interface maps satisfy



  \[
  L_iL_i^*\preceq N_*\lambda^2I;
  \]

- all outside-register nonharmonic modes have a uniform positive gap.


Then there are palette-dependent constants \(c,C>0\) such that, for



\[
0<\lambda\le \frac{c}{t},
\]


every unit degree-\(d\) chain \(x\) satisfies



\[
\boxed{
\|(I-P_K)x\|^2
\le
C\left[
t\lambda^2+
\frac{\langle x,\Delta_Xx\rangle}{g\lambda^\kappa}
\right].
}
\]


For maximum active locality \(m\),



\[
\kappa=4m+2.
\]


All constants depend only on the finite certified palette, including its zero-weight gaps, private-pair lower bounds, matrix norms, interface constant, and outside spectral gap—not on \(t\), the outside-register dimension, the logical dimension, \(g\), or \(\lambda\).



---


## 1. Rank-deficient singular-value scaling


Let \(A\) be any nonzero matrix, possibly rank deficient, and let \(L,R\) be invertible. Then



\[
\boxed{
\sigma_{\min}^+(LAR)
\ge
\sigma_{\min}(L)\,
\sigma_{\min}^+(A)\,
\sigma_{\min}(R).
}
\]


Indeed, let \(K=\ker A\). For a unit vector



\[
x\perp\ker(LAR)=R^{-1}K,
\]


we have



\[
\begin{aligned}
\operatorname{dist}(Rx,K)
&=\inf_{z\in R^{-1}K}\|R(x-z)\|\\
&\ge \sigma_{\min}(R)
   \operatorname{dist}(x,R^{-1}K)\\
&=\sigma_{\min}(R).
\end{aligned}
\]


Since \(A\) annihilates \(K\),



\[
\|ARx\|
\ge
\sigma_{\min}^+(A)\operatorname{dist}(Rx,K),
\]


and left multiplication by \(L\) gives the result. Thus rank deficiency causes no failure. Zero-rank blocks are simply omitted.


For a degree-\(k\) weighted boundary,



\[
\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k.
\]


With vertex weights in \(\{1,\lambda\}\) and \(0<\lambda\le1\),



\[
\sigma_{\min}(W_{k-1}^{-1})\ge1,
\qquad
\sigma_{\min}(W_k)\ge\lambda^{k+1},
\]


hence



\[
\sigma_{\min}^+(\partial_{w,k})
\ge
\lambda^{k+1}
\sigma_{\min}^+(\partial_{1,k}).
\]


In degree \(d_a\), Hodge decomposition gives



\[
\gamma_+(\Delta_{d_a})
\ge
\min\left\{
\sigma_{\min}^+(\partial_{d_a})^2,
\sigma_{\min}^+(\partial_{d_a+1})^2
\right\}
\ge
c_a\lambda^{2d_a+4}.
\]


The second exponent is the worse one for \(0<\lambda\le1\). If \(d_a=2m_a-1\), this is



\[
2d_a+4=4m_a+2.
\]


For \(m_a\le m\), a finite-palette minimum yields



\[
\boxed{\gamma_+(\Delta_{d_a})\ge c\lambda^{4m+2}.}
\]


This is only a sufficient floor, not an optimal valuation.



---


## 2. Padding over every bidegree


Using reduced chains, the target-degree chain space of the join decomposes as



\[
C_d(Y_a*R_{\mathrm{out}})
=
\bigoplus_{r+s=d-1}
C_r(Y_a)\otimes C_s(R_{\mathrm{out}}),
\]


and on each bidegree



\[
\Delta_{\mathrm{join}}
=
\Delta_{Y_a,r}\otimes I+
I\otimes\Delta_{\mathrm{out},s}.
\]


Both summands are positive semidefinite, so the kernel on that bidegree is



\[
\ker\Delta_{Y_a,r}\otimes
\ker\Delta_{\mathrm{out},s}.
\]


By hypothesis, the outside complex has reduced harmonics only in degree \(q\). At global degree



\[
d=d_a+q+1,
\]


the condition \(s=q\) forces \(r=d_a\). Thus the only outside-harmonic bidegree is



\[
(d_a,q).
\]


Every other actual bidegree—including those with local simplices above \(d_a\)—has a uniform positive outside contribution. Hence the padded zero-weight kernel is exactly



\[
V\oplus(Q_a\otimes\mathcal H_{\mathrm{out}}),
\]


and the positive gap outside it is uniform. At positive \(\lambda\), the padded whole gap is at least



\[
\min\{c\lambda^\kappa,\delta_{\mathrm{out}}\}
\ge c'\lambda^\kappa.
\]


Padding \(T_a\) with the outside harmonic projector removes all outside boundary and coboundary terms, so its injectivity and \(O(\lambda)\) norm bounds persist.



---


## 3. Shared-register interface estimate


Write



\[
x=\omega_0+\sum_{i=1}^t\omega_i,
\qquad
x_i=\omega_0+\omega_i,
\]


and define



\[
e=\|D_Xx\|^2,\qquad
U=\sum_i\|\omega_i\|^2.
\]


Let



\[
a=\partial_R\omega_0,\qquad
y_i=L_i\omega_i,\qquad
y=\sum_i y_i,\qquad
r=a+y.
\]


The single-gadget register boundary is



\[
a+y_i=r-(y-y_i).
\]


Moreover,



\[
\sum_i\|y-y_i\|^2
=
(t-2)\|y\|^2+\sum_i\|y_i\|^2.
\]


Let



\[
\rho=\lambda^{-2}\|[L_1\ \cdots\ L_t]\|^2.
\]


Because the input blocks are orthogonal,



\[
[L_1\ \cdots\ L_t][L_1\ \cdots\ L_t]^*
=
\sum_iL_iL_i^*
\preceq N_*t\lambda^2I,
\]


so \(\rho\le N_*t\). Also,



\[
\|y\|^2\le\rho\lambda^2U,
\qquad
\sum_i\|y_i\|^2\le N_*\lambda^2U.
\]


Consequently,



\[
\sum_i\|y-y_i\|^2
\le
\chi\lambda^2U,
\qquad
\chi=(t-2)_+\rho+N_*=O(t^2).
\]


All nonregister down-boundary outputs and all up outputs split by gadget. Therefore



\[
\boxed{
\sum_i\|D_i(\lambda)x_i\|^2
\le
2te+2\chi\lambda^2U.
}
\]


Shared outputs of the \(L_i\) cause no error; output orthogonality was never used.



---


## 4. Geometric leakage without geometric-kernel assumptions


Set



\[
A_{i,0}=I-P-Q_i.
\]


The zero-weight gap and



\[
D_i(\lambda)=D_{i,0}+\lambda D_{i,1}
\]


give



\[
\begin{aligned}
S_A
&:=\sum_i\|A_{i,0}x_i\|^2\\
&\le
C\sum_i\|D_{i,0}x_i\|^2\\
&\le
C\left(
te+\chi\lambda^2U+t\lambda^2
\right),
\end{aligned}
\]


because



\[
\sum_i\|x_i\|^2
=
1+(t-1)\|\omega_0\|^2
\le t.
\]


Since \(T_iP=0\),



\[
T_iQ_ix_i=T_ix_i-T_iA_{i,0}x_i.
\]


Private-pair injectivity and \(\|T_i\|=O(\lambda)\) imply



\[
S_Q:=\sum_i\|Q_ix_i\|^2
\le
C\left(
\lambda^{-2}\sum_i\|T_ix_i\|^2+S_A
\right).
\]


The retained \(T_i\)-outputs are gadget-private, so



\[
\sum_i\|T_ix_i\|^2\le e.
\]


Hence



\[
S_Q\le C(e/\lambda^2+S_A).
\]


Now let



\[
N=\|(I-P)x\|^2.
\]


Orthogonality gives



\[
N\le U+t\|(I-P)\omega_0\|^2=S_A+S_Q.
\]


Using \(U\le N\),



\[
N
\le
C\left[
(t+\lambda^{-2})e+t\lambda^2
\right]
+C\chi\lambda^2N.
\]


Since \(\chi=O(t^2)\), choosing \(\lambda\le c/t\) makes the last coefficient at most \(1/2\). Absorption yields



\[
\boxed{
N\le
C\left[
t\lambda^2+(t+\lambda^{-2})e
\right].
}
\]


No comparison with \(\ker\Delta_X\) or its projector has occurred. This is exactly the leakage mechanism described in the packet. 〔PRO_BOUNDED_PROOF_PACKET_2026-0…〕



---


## 5. Logical coercivity


Exact filling gives



\[
\operatorname{ran}\Pi_i\subseteq B_d(Y_i).
\]


On the boundary subspace, the full local Laplacian equals its up part. Therefore the local whole positive gap implies



\[
\Delta_i^\uparrow
\succeq
c\lambda^\kappa P_{B_d(Y_i)}
\succeq
c\lambda^\kappa\Pi_i.
\]


The global \((d+1)\)-columns partition by gadget, so, even though their degree-\(d\) outputs may overlap,



\[
\Delta_X^\uparrow
=
\sum_i\iota_i\Delta_i^\uparrow\iota_i^*
\succeq
c\lambda^\kappa H^{\mathrm{emb}}.
\]


Thus



\[
\langle x,(P-P_K)x\rangle
\le
\frac{\langle x,H^{\mathrm{emb}}x\rangle}{g}
\le
\frac{e}{cg\lambda^\kappa}.
\]


Since \(P_K\le P\),



\[
\|(I-P_K)x\|^2
=
N+\langle x,(P-P_K)x\rangle.
\]


Combining with the leakage estimate,



\[
\|(I-P_K)x\|^2
\le
C\left[
t\lambda^2+(t+\lambda^{-2})e+
\frac{e}{g\lambda^\kappa}
\right].
\]


For \(\lambda\le c/t\), \(\kappa\ge2\), and \(g\le1\),



\[
t+\lambda^{-2}
\le C\lambda^{-\kappa}
\le \frac{C}{g\lambda^\kappa}.
\]


Therefore



\[
\boxed{
\|(I-P_K)x\|^2
\le
C\left[
t\lambda^2+
\frac{e}{g\lambda^\kappa}
\right].
}
\]



---


# Multiplicity, gap, and persistence


Choose



\[
\lambda\le c\min\{t^{-1},\eta t^{-1/2}\},
\qquad
E\le c'\eta^2g\lambda^\kappa,
\qquad
0<\eta<1.
\]


Every unit vector in



\[
\mathcal L_{<E}
=
\operatorname{ran}\mathbf1_{[0,E)}(\Delta_X)
\]


has nonzero projection onto \(\ker H\). Hence



\[
\dim\mathcal L_{<E}\le\dim\ker H.
\]


Independent interiors and exact filling give



\[
B_d(X)\cap V
=
\sum_i\operatorname{ran}\Pi_i.
\]


Thus



\[
V\Big/\sum_i\operatorname{ran}\Pi_i
\hookrightarrow H_d(X)
\]


supplies \(\dim\ker H\) exact zero modes. Consequently,



\[
\boxed{
\dim\ker\Delta_X=\dim\ker H,
\qquad
\operatorname{spec}(\Delta_X)\cap(0,E)=\varnothing.
}
\]


Equal dimensions plus concentration give



\[
\boxed{
\|P_{\ker\Delta_X}-P_K\|\le\eta.
}
\]


If \(\ker H=0\), then \(\mathcal L_{<E}=0\), so the entire geometric spectrum is at least \(E\).


For nested term sets \(A\subseteq B\),



\[
H_d(X_A)\cong V/W_A,
\qquad
W_A=\sum_{i\in A}\operatorname{ran}\Pi_i,
\]


naturally with respect to inclusion. The induced map is the surjection



\[
V/W_A\twoheadrightarrow V/W_B,
\]


so



\[
\boxed{
\operatorname{rank}[H_d(X_A)\to H_d(X_B)]
=
\dim\ker H_B.
}
\]


This remains valid when \(\ker H_B=0\); the persistent rank is then zero. If the initial kernel has known dimension \(D>0\), true normalized persistence is



\[
\frac{\dim\ker H_B}{D}.
\]


These deductions are exactly the standard dimension/naturality consequences following the all-chain bound. 〔PRO_BOUNDED_PROOF_PACKET_2026-0…〕



---


# Conservative scales


With \(m\le6\),



\[
\kappa=26.
\]


Taking



\[
\lambda=\Theta(\eta/t)
\]


gives



\[
\boxed{
E=\Omega\!\left(\frac{\eta^{28}g}{t^{26}}\right).
}
\]


Under the separate common-copy theorem, \(F=\lambda^{-2}\), so the unweighted gap floor is



\[
\min\{FE,1\},
\qquad
\boxed{
FE=\Omega\!\left(\frac{\eta^{26}g}{t^{24}}\right).
}
\]


These are lower-bound floors, not equalities or runtime estimates. 〔PRO_BOUNDED_PROOF_PACKET_2026-0…〕


A modest refinement is possible: the absorption really requires only



\[
\chi\lambda^2\le c_0,
\]


not the universal substitution \(\lambda\le c/t\). Thus instances with certified interface congestion \(\chi=o(t^2)\) may use larger weights, subject also to the final error condition \(t\lambda^2=O(\eta^2)\). This does not alter the conservative worst-case theorem.
