# Pro selected-cycle guard review — complete response

Collected 2026-09-03T17:22:01.737Z. The browser showed a completed response, **Worked for 8m 39s**, after user message 5 and the selected-cycle guard attachment. This is external model review, not independent correctness or source certification.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: 9f2e0880db89fb570b439156e6926b664828dcee.
- Actual task: [selected-cycle guard submission](PRO_SELECTED_GUARD_SUBMISSION_2026-09-03.md).
- Input: [PRO_SELECTED_GUARD_PACKET_2026-09-03.md](PRO_SELECTED_GUARD_PACKET_2026-09-03.md), 13966 bytes, SHA-256 33c6a76d54e3242f515ce905e7cb7c9cfc1b367be406c4846e7394f7ec1db365.
- Exact browser completion time was not exposed; collection time and displayed duration are separate facts.

The response below was transcribed from the rendered DOM. All **124** equation elements were recovered from displayed `data-math-source` attributes. Seven visible attachment citation labels are preserved as 〔…〕. The answer contains no external links. [The capture record](PRO_SELECTED_GUARD_REVIEW_CAPTURE_2026-09-03.json) retains the displayed text and exact equation sources. No new primary literature checking was performed during collection. Adopted conclusions are recorded separately.

---

# Verdict


The selected-cycle guard lemma is **valid under the stated old finite certificate**. I find no invalid inference and no counterexample satisfying its hypotheses.


Three points should be stated more precisely:


1. The zero-weight identity is a statement about the **target-degree differential pair**
  
  
  
  \[
  \ker D_{Z,0}^{(D)}=V'\oplus Q',
  \]
  
  
  not the kernel of the entire graded differential.

2. The positive-gap argument uses the augmented/reduced Laplacian of \(S_\beta\) in every degree \(-1,0,1\), not merely its ordinary degree-one gap.

3. The projected-pair proof should explicitly define the harmonic projection degreewise. Once this is done, inputs involving the unselected bowtie petal and inputs in the other private bidegrees contribute zero rather than producing hidden weight-one terms.


Allowing \(Q\) to be an arbitrary orthogonally projected subspace supported on private coordinates is legitimate. The all-chain concentration proof uses private support, orthogonality, a zero-weight gap on \((V\oplus Q)^\perp\), and injectivity of \(T_1|_Q\); it never requires \(Q\) to be spanned by individual simplices. The note explicitly makes this revised scope part of the criterion. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕



---


# Selected-cycle guard closure theorem


Let \(Y\) contain an induced top-dimensional register \(R\), \(\dim R=d\), with



\[
V=Z_d(R).
\]


Assume



\[
B_d(Y)\cap V=\mathbb C\phi,
\qquad
\ker D_{Y,0}^{(d)}=V\oplus Q,
\]


where \(Q\) is an orthogonal subspace supported on private chain coordinates. Assume further that a private-output projection gives



\[
T_Y(\lambda)=\lambda T_{Y,1},\qquad
T_{Y,1}V=0,\qquad
\|T_{Y,1}q\|\ge b\|q\|
\quad(q\in Q).
\]


Let \(B\) be a seven-vertex bowtie, let \(S_\beta\) be one induced four-cycle, and let \(\gamma_\beta\) be its normalized oriented cycle. Form \(Z\) by joining all vertices of \(B\) to \(R\), while joining only the vertices of \(S_\beta\) to the private vertices of \(Y\). Then, with



\[
R'=R*B,\qquad D=d+2,
\]


the guarded gadget satisfies



\[
B_D(Z)\cap Z_D(R')
=
\mathbb C(\phi\otimes\gamma_\beta),
\]



\[
\ker D_{Z,0}^{(D)}
=
V'\oplus Q',
\qquad
V'=V\otimes Z_1(B),
\qquad
Q'=Q\otimes\mathbb C\gamma_\beta,
\]


and admits a private projected pair



\[
T_Z(\lambda)=\lambda T_{Z,1},
\qquad
T_{Z,1}V'=0,
\qquad
\|T_{Z,1}q'\|\ge b\|q'\|
\quad(q'\in Q').
\]


Thus it satisfies the same finite concentration criterion for the projector



\[
\Pi_\phi\otimes
|\gamma_\beta\rangle\langle\gamma_\beta|.
\]



---


## 1. Clique union and exact boundary intersection


A clique in \(Z\) containing an old private vertex can use only vertices of \(S_\beta\) from the new bowtie. Its old vertices form a clique of \(Y\). Hence it lies in \(Y*S_\beta\).


A clique containing no old private vertex has its old part in \(R\), and its bowtie part is an arbitrary clique of \(B\). Hence it lies in \(R*B\). Conversely, both stated joins occur by construction. Therefore, as full clique complexes,



\[
Z=(Y*S_\beta)\cup(R*B),
\qquad
(Y*S_\beta)\cap(R*B)=R*S_\beta.
\]


This establishes the claimed clique-union description. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕


Put \(R'=R*B\). Simplicial excision and the reduced join-chain formula give, in **all degrees**,



\[
\begin{aligned}
\widetilde C_*(Z,R')
&\cong
\widetilde C_*(Y*S_\beta,R*S_\beta)\\
&\cong
\widetilde C_*(Y,R)
\,\widehat\otimes\,
\widetilde C_*(S_\beta).
\end{aligned}
\]


This is also evident directly from bases: a simplex surviving modulo \(R'\) contains an old private vertex, and therefore has a unique decomposition into a relative simplex of \((Y,R)\) and a simplex of \(S_\beta\). Deleting an old vertex gives the relative differential; deleting an \(S_\beta\) vertex gives the second tensor differential.


Since



\[
\widetilde H_s(S_\beta)=
\begin{cases}
\mathbb C[\gamma_\beta],&s=1,\\
0,&s\ne1,
\end{cases}
\]


the relative Künneth formula yields



\[
H_{D+1}(Z,R')
\cong
H_{d+1}(Y,R)\otimes
\mathbb C[\gamma_\beta].
\]


Let \(\delta_Y\) and \(\delta_Z\) be the connecting maps. If \(c\) is an old relative cycle with \(\partial c\in C_d(R)\), then, up to the harmless global join-orientation sign,



\[
\delta_Z([c]\otimes[\gamma_\beta])
=
[\partial c]\otimes[\gamma_\beta].
\]


Thus



\[
\operatorname{im}\delta_Z
=
(\operatorname{im}\delta_Y)
\otimes\mathbb C[\gamma_\beta].
\]


Because \(R\) is top-dimensional,



\[
\operatorname{im}\delta_Y
=
B_d(Y)\cap Z_d(R)
=
\mathbb C\phi.
\]


Because \(R'=R*B\) is top-dimensional in degree \(D\), it has no \(D\)-boundaries, and exactness of the pair sequence gives



\[
B_D(Z)\cap Z_D(R')
=
\operatorname{im}\delta_Z
=
\mathbb C(\phi\otimes\gamma_\beta).
\]


No assumption that all old homology is represented inside \(R\) is used. Additional classes in \(H_{d+1}(Y,R)\) either lie in \(\ker\delta_Y\) or have boundary in the already prescribed one-dimensional image. They cannot enlarge the new intersection. This validates the note’s connecting-map argument. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕


For every \(\lambda>0\), diagonal weight gauge preserves the boundary space and fixes every \(R'\)-simplex because all \(R\)- and \(B\)-vertices have weight one. Hence the same boundary intersection holds at every positive weight.



---


## 2. Zero-weight decomposition in all bidegrees


At \(\lambda=0\), a boundary term that deletes an old private vertex has coefficient zero. Consequently:


- register simplices map only to register simplices;

- simplices containing an old private vertex map only to simplices still containing an old private vertex.


Thus the zero-weight chain complex splits orthogonally in every degree:



\[
(C_*(Y),\partial_{Y,0})
=
(C_*(R),\partial_R)
\oplus
(C_*^{\mathrm{priv}}(Y),\partial_{\mathrm{priv},0}).
\]


For \(Z\), every private simplex uses only \(S_\beta\) on the bowtie factor, so



\[
C_*^{\mathrm{priv}}(Z)
\cong
C_*^{\mathrm{priv}}(Y)
\,\widehat\otimes\,
\widetilde C_*(S_\beta).
\]


The corresponding private Laplacian is a tensor sum on each bidegree.


At target degree \(D=d+2\), the possible \(S_\beta\)-degrees are



\[
s=1,\ 0,\ -1,
\]


with old private degrees respectively



\[
r=d,\ d+1,\ d+2.
\]


Thus cells of \(Y\) above the old target degree are included. The only bidegree in which the \(S_\beta\) factor is harmonic is



\[
(r,s)=(d,1).
\]


There the private kernel is



\[
Q\otimes\mathbb C\gamma_\beta.
\]


For \(s=0\) or \(s=-1\), the augmented reduced Laplacian of the nonempty connected cycle \(S_\beta\) is strictly positive. Hence even an old private harmonic vector in degree \(d+1\) or \(d+2\) cannot create a new target zero mode.


The register summand has target kernel



\[
Z_D(R*B)=Z_d(R)\otimes Z_1(B)=V'.
\]


Therefore



\[
\boxed{
\ker D_{Z,0}^{(D)}
=
V'\oplus
\bigl(Q\otimes\mathbb C\gamma_\beta\bigr).
}
\]


Its positive gap is bounded below by a positive constant depending only on:


- the old target-degree private gap;

- the finitely many positive augmented gaps of \(S_\beta\);

- the target-degree positive gap of the fixed register \(R*B\).


This proves both the kernel identity and the uniform zero-weight gap without any reference to the unknown positive-\(\lambda\) geometric kernel. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕



---


## 3. Projected private pair on the full target domain


Let \(P_\gamma\) denote orthogonal projection onto

\(\mathbb C\gamma_\beta\) in degree one of \(S_\beta\), extended by zero in its other degrees. In the down- and up-output spaces, retain precisely



\[
\operatorname{ran}R_Y^{\mathrm{out}}
\otimes\mathbb C\gamma_\beta.
\]


Call the resulting projection \(R_Z^{\mathrm{out}}\), and define



\[
T_Z(\lambda)=R_Z^{\mathrm{out}}D_Z(\lambda).
\]


Under the join bigrading, only the input bidegree \((d,1)\) can survive this output projection. On that bidegree, the local part is the old projected pair tensored with \(P_\gamma\).


Every outside-differential contribution vanishes because



\[
\partial_{S_\beta}\gamma_\beta=0,
\qquad
P_\gamma\operatorname{im}\partial_{S_\beta}^*=0.
\]


This handles both directions:


- differentiating an input already in the harmonic line;

- projecting the differential or coboundary of an arbitrary \(S_\beta\)-chain onto that line.


Hence private inputs in bidegrees \((d+1,0)\) and \((d+2,-1)\) contribute zero. Register inputs involving the unselected bowtie petal merely undergo the contractive restriction/projection onto \(\gamma_\beta\); no weight-one outside term survives.


Consequently, on the **entire** degree-\(D\) chain space,



\[
T_Z(\lambda)=\lambda T_{Z,1}.
\]


For \(v\in V\) and \(z\in Z_1(B)\),



\[
T_{Z,1}(v\otimes z)
=
(T_{Y,1}v)\otimes P_\gamma z
=
0,
\]


so \(T_{Z,1}V'=0\).


Finally, for \(q\in Q\),



\[
T_{Z,1}(q\otimes\gamma_\beta)
=
(T_{Y,1}q)\otimes\gamma_\beta,
\]


and therefore



\[
\|T_{Z,1}(q\otimes\gamma_\beta)\|
\ge
b\|q\otimes\gamma_\beta\|.
\]


The old bulk constant is preserved exactly. The range still consists of chains containing an old private vertex, so retained outputs remain orthogonal between independently attached gadgets. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕


The reported finite check that raw central coordinates need not cancel, whereas the selected harmonic sum does, is consistent with this proof and explains why replacing \(Q'\) by the full central coordinate span would be wrong. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕



---


## 4. Basis cone, interface, iteration, and exponent


For the basis atom



\[
Y=R\cup(v*S_0),
\]


the relative connecting map has one-dimensional image generated by the selected petal cycle. Hence



\[
B_1(Y)\cap Z_1(R)=\mathbb C\gamma_0.
\]


At zero weight, the target private pair is the augmented reduced differential pair of \(S_0\) in degree zero. Since \(S_0\) is connected,



\[
\widetilde H_0(S_0)=0,
\]


so this private pair is injective. Therefore \(Q=0\). Taking the zero output projection satisfies the projected-pair condition vacuously. Petal exchange gives the \(|1\rangle\) atom.


For the guarded construction, the private-to-register interface can arise only by deleting the unique old private vertex of a simplex containing exactly one private vertex. Its coefficient is \(\lambda\). For each private vertex, deletion is a signed partial isometry; hence



\[
LL^*\preceq
N_{\mathrm{priv}}\lambda^2I.
\]


The guard adds no private vertices, so this interface constant does not grow under iteration.


Applying the construction repeatedly tensors



\[
Q\longmapsto
Q\otimes\mathbb C\gamma_{\beta_1}
\otimes\cdots\otimes
\mathbb C\gamma_{\beta_s},
\]


while the intended projector becomes the old active projector tensored with the selected computational-basis guard. All constants remain uniform over the finite family of guard strings of total locality at most six.


At locality \(m\), the guarded register target degree is



\[
2m-1.
\]


The conservative diagonal-scaling argument therefore gives



\[
\gamma_+(\Delta)
\ge
c\lambda^{\,2(2m-1)+4}
=
c\lambda^{4m+2}.
\]


For \(m\le6\),



\[
\boxed{\kappa\le26.}
\]


The basis-cone and iteration conclusions in the note are therefore correct. 〔PRO_SELECTED_GUARD_PACKET_2026-…〕


# Status


**Selected computational-basis guards are closed**, conditional on the old active gadget satisfying the finite certificate. This closure is an abstract proof for the explicit alternative construction \(Z=(Y*S_\beta)\cup(R*B)\), not a certification of the source’s different joined-implementing-sphere graph.


The exact remaining finite gate is unchanged: establish the criterion for the nontrivial one-qubit difference atoms and the two-qubit two-term atoms. No full-palette, source-priority, complexity-class, optimal-gap, or paper-readiness conclusion follows from this guard lemma alone.
