# Selected-cycle guard closure for the finite certificate criterion

September 3, 2026. **LOCAL STRUCTURAL DERIVATION; INDEPENDENT EXTERNAL REVIEW PENDING.** This is an explicit alternative guard construction. It does not assert that Rudolph's joined-implementing-sphere construction has identical zero-weight data. The topological ingredients below are standard relative chains and the join formula; novelty has not been checked.

## 1. Input and graph construction

Let Y contain an induced register R of top dimension d. Every register vertex has weight one; every private vertex of Y has weight lambda. Assume the finite criterion in [FINITE_CERTIFICATE_CONCENTRATION.md](FINITE_CERTIFICATE_CONCENTRATION.md) at degree d, for the logical rank-one projector onto phi in V=Z_d(R):
\[
B_d(Y)\cap V=\mathbb C\phi,\qquad
\ker D_{Y,0}=V\oplus Q,
\]
and a private-output projection with
\[
T_Y(\lambda)=\lambda T_{Y,1},\quad
T_{Y,1}V=0,\quad
\|T_{Y,1}q\|\ge b\|q\|\quad(q\in Q).
\]
Here Q is an explicitly certified subspace supported on private coordinates, not necessarily a coordinate span.

Let B be a fresh seven-vertex bowtie register, with two four-edge petals S_0,S_1. Choose beta in {0,1}. S_beta is the full induced subgraph on its four vertices, and its normalized oriented cycle gamma_beta encodes the desired basis state. Define a graph Z by:

- retaining every edge of Y and B;
- connecting every vertex of R to every vertex of B;
- connecting each private vertex of Y to every vertex of S_beta, and to no other vertex of B.

All B vertices have weight one. No additional private vertices are introduced. Every clique containing a private vertex sees only S_beta on the new factor. Hence, as full clique complexes,
\[
Z=(Y*S_\beta)\cup(R*B),\qquad
(Y*S_\beta)\cap(R*B)=R*S_\beta.
\tag{1}
\]
The new full register is R'=R*B, of target dimension D=d+2, with
\[
V'=Z_D(R')=V\otimes Z_1(B).
\]
Tensor products here include the usual join degree shift and oriented chain isometry.

**Claim.** Z satisfies the finite criterion for
\[
\Pi'=\Pi_\phi\otimes|\beta\rangle\langle\beta|,
\qquad Q'=Q\otimes\mathbb C\gamma_\beta.
\tag{2}
\]
All constants are fixed for a fixed Y. Iterating at most four times keeps a finite, explicitly constructible palette through total locality six.

## 2. Exact boundary intersection

Use reduced chains, including degree -1. The quotient chain complex of (1) is
\[
\widetilde C_*(Z,R')
\cong
\widetilde C_*(Y,R)\,\widehat\otimes\,\widetilde C_*(S_\beta),
\tag{3}
\]
where a degree-(r,s) tensor has total degree r+s+1. This follows directly from the basis of simplices with at least one old private vertex. No chain in the quotient uses a B vertex outside S_beta.

Over the coefficient field, S_beta has reduced homology only in degree one, with generator [gamma_beta]. Therefore
\[
H_{D+1}(Z,R')
\cong H_{d+1}(Y,R)\otimes\mathbb C[\gamma_\beta].
\]
The connecting homomorphism into H_D(R') sends
\[
[c]\otimes[\gamma_\beta]\longmapsto
[\partial c]\otimes[\gamma_\beta].
\tag{4}
\]
Indeed, choose a relative cycle c with boundary in R; gamma_beta is a cycle, so the join boundary of c*gamma_beta is (partial c)*gamma_beta.

Since R and R' are top-dimensional in degrees d and D, respectively, their top homology equals their top cycle space. The old exact-filling hypothesis identifies the image of the old connecting map with C phi. Exactness of the pair sequence and (4) now give
\[
B_D(Z)\cap V'=\mathbb C(\phi\otimes\gamma_\beta).
\tag{5}
\]
This argument uses the exact old boundary intersection; it does not assume that every old homology class was already represented in R. Positive lambda is handled by the same diagonal gauge, which fixes all register coordinates.

## 3. Exact zero-weight decomposition in every degree

At lambda=0, removing the last private vertex has coefficient zero. Thus the zero-weight boundary of Y splits orthogonally, in every degree, into its register complex and a private complex:
\[
(C_*(Y),\partial_{Y,0})
=(C_*(R),\partial_R)\oplus(C_*^{priv}(Y),\partial_{priv,0}).
\tag{6}
\]
Both are actual chain complexes. The adjoint splits as well. At target degree d, the private Laplacian has kernel Q and a positive gap on its complement by the input hypothesis.

For Z the corresponding orthogonal splitting is
\[
(C_*(Z),\partial_{Z,0})
=
(C_*(R'),\partial_{R'})
\oplus
(C_*^{priv}(Y)\,\widehat\otimes\,\widetilde C_*(S_\beta),
 \partial_{priv,0}\otimes I+(-1)^{r+1}I\otimes\partial_S).
\tag{7}
\]
Consequently the private zero-weight Laplacian is the tensor sum on every actual bidegree. At target degree D=d+2, the only outside-harmonic bidegree is (d,1). All other bidegrees have the positive reduced S_beta gap, even if Y has cells above d. Equations (6)-(7) therefore prove
\[
\ker D_{Z,0}=V'\oplus(Q\otimes\mathbb C\gamma_\beta)=V'\oplus Q'.
\tag{8}
\]
Its positive gap is bounded below by the minimum of the old private target gap, the S_beta gap, and the positive gap of the fixed full register R'. No eigenspace of the unknown positive-weight geometric Laplacian is used.

This is also why taking all central coordinates fails after the guard: the new guard vertices have weight one. The private subspace must use the selected cycle's harmonic factor.

## 4. Projected private pair

In the down and up output degrees of Z, retain the old private output subspaces tensored with C gamma_beta; project orthogonally onto them. Call this projection R_Z^out. It is supported on outputs containing an old private vertex. Define
\[
T_Z(\lambda)=R_Z^{out}D_Z(\lambda).
\]
The outside differential terms vanish after this projection: gamma_beta is both closed and coclosed in the reduced chain complex of S_beta. On outputs with a private vertex, the outside complex is S_beta, not the entire B. For register inputs, restriction to S_beta is followed by the same harmonic projection.

Thus the remaining active part is the old T_Y tensor the selected harmonic component, including the contractive restriction on register inputs. It follows on the entire target chain space that
\[
T_Z(\lambda)=\lambda T_{Z,1},\qquad T_{Z,1}V'=0.
\tag{9}
\]
For q in Q, the exact chain isometry gives
\[
T_Z(\lambda)(q\otimes\gamma_\beta)
=\lambda(T_{Y,1}q)\otimes\gamma_\beta,
\]
with the fixed join orientation convention on each output summand. Since gamma_beta is normalized,
\[
\|T_{Z,1}(q\otimes\gamma_\beta)\|\ge b\|q\|.
\tag{10}
\]
The finite operator norms remain bounded. The private-to-register interface still comes only from removing one old private vertex, with coefficient lambda. The number of such vertices is unchanged, giving a fixed interface constant. Conditions (5), (8), (9)-(10) supply the required finite data.

## 5. Basis-projector base case and iteration

There is an elementary starting atom for |0><0|. Let R be a bowtie and add one private apex v, adjacent precisely to the selected petal S_0:
\[
Y=R\cup(v*S_0).
\]
The four triangles in v*S_0 fill its oriented cycle. The relative connecting map shows that no other top register cycle is killed.

At zero weight, the private chain complex is the shifted reduced chain complex of S_0. In target degree one, its Laplacian is the degree-zero reduced Laplacian of S_0, which is positive definite. Hence ker D_0=V and Q=0. The projected pair can be the zero projection; injectivity on the zero subspace is vacuous. This satisfies the same finite criterion. Exchanging the two petals gives |1><1|.

Iteration of (1) constructs a guard string of any fixed length. A basis projector on m qubits is just the cone on the join of the m selected petals, attached to the full m-qubit bowtie register. It has Q=0. For the actual certified two-qubit Hadamard atom, iteration gives Q_old tensored with the selected guard harmonic line. Existing X/Z relabelings and guard-petal swaps transport all signs and bit choices.

With total locality m<=6, the elementary diagonal-scaling argument supplies the safe exponent kappa=4m+2<=26. This statement does not improve that valuation or assert a practical gap.

## 6. Verification scope and remaining gate

[check_selected_cycle_guard.py](check_selected_cycle_guard.py) independently constructs the clique graph from the recorded source graph and checks, with integer arithmetic, the clique-union identity, relative and zero-weight boundary tensor identities, harmonic projection cancellation, transported bulk pair, logical annihilation, and an explicit guarded filling. A small basis-cone fixture separately checks its target ranks and nullity.

These checks support the explicit construction; they do not substitute for the general proof above or certify the original source's different guard operation. The original graph certificate remains the input for its numerical constants, with upstream provenance already recorded there.

The claim is submitted for a bounded hostile proof review. Remaining active types include the nontrivial one-qubit difference and two-qubit two-term atoms. Complete-palette integration, exact source-complexity significance, and priority remain open. No unrestricted quantum-class equivalence follows from this lemma.
