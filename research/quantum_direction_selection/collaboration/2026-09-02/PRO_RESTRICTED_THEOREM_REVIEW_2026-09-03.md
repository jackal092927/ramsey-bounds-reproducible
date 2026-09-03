# Pro restricted-theorem integration review — complete response

Collected 2026-09-03T18:24:32.030Z. The browser showed a completed response, **Worked for 10m 40s**, after user message 6 and the restricted-theorem packet. This is external model review, not independent correctness, source-complexity, novelty, or literature certification.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: 23f83cf0db8fd62eed1dd2c7b90b806bb9e3a6e7.
- Actual task: [restricted-theorem submission](PRO_RESTRICTED_THEOREM_SUBMISSION_2026-09-03.md).
- Input: [PRO_RESTRICTED_THEOREM_PACKET_2026-09-03.md](PRO_RESTRICTED_THEOREM_PACKET_2026-09-03.md), 20589 bytes, SHA-256 ed873b118bf5dc19ee233e1380db811dd1d4f33c271fae5089925d1611f99b20.
- Visible account at collection matched the registered personal Pro identity; the public archive omits the account email.
- Exact browser completion time was not exposed; collection time and displayed duration are separate facts.

The response below was transcribed from the rendered DOM. All **137** equation elements were recovered from displayed data-math-source attributes. Visible attachment citation labels are preserved as 〔…〕. The answer contains no external links. [The capture record](PRO_RESTRICTED_THEOREM_REVIEW_CAPTURE_2026-09-03.json) retains the displayed text and exact equation sources. No new primary literature or source-complexity checking was performed during collection. Adopted conclusions are recorded separately.

---

# Verdict

The end-to-end integration is **mathematically valid after one source-model correction**. I find no missing local atom and no failure in the history, concentration, quotient, or gap arguments once the reported finite certificates and the previously reviewed concentration/guard lemmas are taken as hypotheses.

The first issue is an **under-specified hypothesis**, not a failed derivation: the source statement currently permits an abstract isometry \(J\) and an unspecified final projector \(P_{\rm acc}\). 〔PRO_RESTRICTED_THEOREM_PACKET_2…〕 The certified palette only covers the standard circuit model in which:

\(J=I_{\text{mixed}}\otimes |0\cdots0\rangle_{\text{clean}}\)
up to fixed computational-basis ancillas, and \(P_{\rm acc}\) is a fixed-local computational-basis output measurement, normally \(|1\rangle\langle1|\) on a designated output qubit. An arbitrary real entangled input-code isometry or arbitrary global acceptance projector need not belong to the finite palette.

With that restriction made explicit, the claimed transformation and exact normalized-persistence identities survive. The theorem should also replace the phrase “kernel dimensions in (3)–(4)” by the explicit statement

\(\dim\ker\Delta_d(X_{\rm out})=\dim S,\)
since equation (4) itself states a persistent rank, not an endpoint nullity.

## Claim status

| Integration point | Verdict |
| --- | --- |
| Four-item atom list | **Complete**, for standard clean-input and computational-basis output circuits |
| One global target degree | **Valid** |
| \(X_{\rm in}\subseteq X_{\rm out}\) by adding rejection gadgets | **Valid** |
| \(\beta_d(X_{\rm in})=D\) | **Valid** |
| Final logical kernel \(=\mathcal VS\) | **Valid** |
| Final logical gap, including \(S=0\) | **Valid** |
| Exact whole homology, not merely low-energy counting | **Valid** |
| Persistent rank \(=\dim S\) | **Valid**, including \(\dim S=0\) |
| Weighted and common-copy gap exponents | **Algebraically correct** |
| Mixed-spectator extension | **Exactly correct** |
| Fraction separation | **Exactly correct at the stated strength** |
| Standard-class hardness | **Open and not implied** |
| Finite certificate computations | **Assumed as instructed, not independently certified here** |

# Corrected restricted reduction theorem

Work over \(\mathbb R\), or equivalently its complexification. Let \(U\) be an exact polynomial-size qubit circuit over

\(G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}.\)
Assume:

  - \(k\) input qubits are maximally mixed, so \(D=2^k>0\);

  - every remaining input qubit is initialized to a fixed computational-basis clean state;

  - \(J\) is the corresponding standard inclusion;

  - acceptance is a fixed-local computational-basis projective measurement;

  - with

\(M=J^\dagger U^\dagger P_{\rm acc}UJ,\qquad
S=\ker(I-M),\)
one has

\(M|_{S^\perp}\preceq rI,\qquad r\le\frac13;\)

  - the supplied finite atom certificates, selected-cycle guard theorem, outside-harmonic padding, independent-interior hypotheses, and all-chain concentration theorem hold uniformly for the stated palette.

Then, for constant or inverse-polynomially bounded \(\eta>0\), there is a polynomial transformation to nested weighted clique complexes

\(X_{\rm in}\subseteq X_{\rm out}\)
with a common degree \(d\) and weights in \(\{1,\lambda\}\), such that

\(\boxed{\beta_d(X_{\rm in})=D,}\)
\(\boxed{\beta_d(X_{\rm out})=\dim S,}\)
and

\(\boxed{
\operatorname{rank}\!\left[
H_d(X_{\rm in})\longrightarrow H_d(X_{\rm out})
\right]=\dim S.
}\)
Consequently,

\(\boxed{
\frac{\beta_d(X_{\rm in}\to X_{\rm out})}
{\beta_d(X_{\rm in})}
=
\frac{\dim\ker(I-M)}{D}.
}\)
Both endpoint degree-\(d\) Laplacians have an inverse-polynomial floor above their entire kernels. The output statement remains valid when \(S=0\), in which case

\(H_d(X_{\rm out})=0\)
and the full output Laplacian spectrum is bounded below by the stated positive floor.

The packet’s intended theorem and explicit exclusion of standard-class hardness are stated at lines 81–127 and 258–267. 〔PRO_RESTRICTED_THEOREM_PACKET_2… +1〕

# 1. Atom exhaustion

After the gain/loss split, every local positive term belongs to the stated four families.

### Clock, input, and output terms

Illegal-clock penalties, clean-input anchors, neighboring-clock guards, and final rejection penalties are computational-basis projectors. They are covered by the basis cone and fixed selected-cycle guards.

This requires the corrected source assumption that clean ancillas and the measured rejection state are computational-basis states.

### \(X,\mathrm{CX},\mathrm{CCX}\) propagation

For a reversible classical gate \(G\), the propagation projector decomposes into orthogonal rank-one terms

\(\frac{
\bigl(|0\rangle_c|z\rangle-|1\rangle_c|Gz\rangle\bigr)
\bigl(\langle0|_c\langle z|-\langle1|_c\langle Gz|\bigr)
}{2},\)
one for each computational-basis \(z\) on the gate support.

If \(Gz=z\), the forbidden vector factors as

\((|0\rangle-|1\rangle)_c\otimes|z\rangle,\)
so the active atom is \(|0\rangle-|1\rangle\), with fixed-basis guards.

If the target flips, the active clock-target component is one of

\(|00\rangle-|11\rangle,
\qquad
|01\rangle-|10\rangle.\)
The control values and unchanged acted-on bits are fixed-basis guards. Thus controlled flips and Toffoli introduce no additional active state.

### \(H\otimes H\) propagation

Writing \(K=\sqrt2H\), the split enforces consecutively

\(f_{t+1}=Kf_t\)
on one work qubit and

\(f_{t+2}=K^{-1}f_{t+1}
=\frac{H}{\sqrt2}f_{t+1}\)
on the other. Their product is exactly \(H\otimes H\).

The two orthonormal forbidden states for each step are precisely the four three-term vectors \(u_0,u_1,d_0,d_1\). All remaining clock conditions are fixed computational-basis guards. Unacted-on qubits carry identities and are handled by outside padding; they do not require enumerating basis guards.

Hence the four atom classes listed in the certificate note are exhaustive. The packet records the atom list and the source-pinned closures at lines 159–188 and 368–383. 〔PRO_RESTRICTED_THEOREM_PACKET_2… +1〕

The maximal support is six:

  - three unary-clock bits;

  - changing target when present;

  - at most two controls.

The Hadamard atoms use at most four because the other work qubit is outside the local operator, not basis-conditioned.

# 2. Common degree, inclusion, and initial denominator

Let the complete logical register contain \(n\) bowties. Its top degree is

\(d=2n-1.\)
An atom acting on \(m\le6\) logical qubits has active target degree \(2m-1\). Joining with the remaining \(n-m\) bowties pads it to

\((2m-1)+(2(n-m)-1)+1=2n-1=d.\)
The all-bidegree outside-harmonic theorem ensures that this padding is spectral as well as topological; it is not restricted to two local bidegrees.

All initial gadgets and final rejection gadgets use the same register, the same \(\lambda\), and disjoint private vertices. No clique contains private vertices from distinct gadgets. Therefore adding only rejection gadgets gives an actual inclusion

\(X_{\rm in}\subseteq X_{\rm out}.\)
If a common vertex set is desired, future private vertices may be isolated in \(X_{\rm in}\).

For the initial logical Hamiltonian, the clock penalties first restrict every zero vector to the legal unary-clock sector. The propagation terms then force a single underlying input vector \(v\) at every time, with the prescribed weighted history amplitudes \(s_\tau\). The input anchors force \(v\) into the \(D\)-dimensional mixed-input/clean-work sector. Conversely, every such \(v\) gives a zero-energy history. Hence

\(\ker H_{\rm in}=\operatorname{ran}\mathcal V,
\qquad
\dim\ker H_{\rm in}=D.\)
The map \(\mathcal V\) is an isometry because

\(\mathcal V^\dagger\mathcal V=I_D.\)
This is the required no-extra-kernel statement, not merely construction of \(D\) candidate zeros. The packet states this characterization and the initial gap at lines 131–145. 〔PRO_RESTRICTED_THEOREM_PACKET_2…〕

# 3. Output kernel and logical gap

Let \(R\) be the final rejection projector. Since both summands are positive semidefinite,

\(\ker(H_{\rm in}+R)
=
\ker H_{\rm in}\cap\ker R.\)
On the history space,

\(\mathcal V^\dagger R\mathcal V
=
\frac{I-M}{Z},
\qquad
L\le Z\le2L.\)
For \(v\in S\), \(Mv=v\), equivalently \(R\mathcal Vv=0\). Conversely, if \(R\mathcal Vv=0\), then

\(\langle v,(I-M)v\rangle=0,\)
and positivity of \(I-M\) implies \(v\in S\). Thus

\(\boxed{\ker H_{\rm out}=\mathcal VS.}\)
On \(S^\perp\),

\(I-M\succeq\frac23I,\)
so the compressed output penalty is at least

\(\alpha\ge\frac{2/3}{2L}=\frac1{3L}.\)
Using

\(g_{\rm in}\ge\frac1{8L^2}\)
and the accepted two-positive-operator bound,

\(g_{\rm out}
\ge
\frac{\alpha g_{\rm in}}{1+g_{\rm in}}
=
\frac1{3L(8L^2+1)}
\ge
\frac1{27L^3}.\)
Nothing in this argument assumes \(S\neq0\). If \(S=0\), this is a lower bound on the minimum eigenvalue of \(H_{\rm out}\).

# 4. Exact homology and persistent rank

For any term set \(A\), put

\(H_A=\sum_{j\in A}\Pi_j,
\qquad
W_A=\sum_{j\in A}\operatorname{ran}\Pi_j.\)
Because the \(\Pi_j\) are positive projectors,

\(\ker H_A=W_A^\perp.\)
Exact local filling and independent private chain coordinates give

\(B_d(X_A)\cap V=W_A.\)
Therefore inclusion of register cycles induces an injection

\(V/W_A\hookrightarrow H_d(X_A),\)
providing exactly

\(\dim(V/W_A)=\dim\ker H_A\)
candidate homology classes.

The all-chain concentration inequality is applied to the full geometric chain space:

\(\|(I-P_{K_A})x\|^2
\le
C\left[
t\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}
{g_A\lambda^{26}}
\right].\)
With the prescribed parameters, projection onto \(K_A\) is injective on the entire geometric spectral subspace below \(E\). Hence that subspace has dimension at most \(\dim K_A\). Since the quotient injection already supplies \(\dim K_A\) exact zero modes,

\(\boxed{H_d(X_A)\cong V/W_A}\)
and

\(\boxed{
\dim\ker\Delta_A=\dim\ker H_A,\qquad
\operatorname{spec}(\Delta_A)\cap(0,E)=\varnothing.
}\)
This proves whole homology, not a count of approximate zero modes.

For \(A\subseteq B\), the two canonical isomorphisms commute with the common register inclusion, so the induced homology map is exactly

\(V/W_A\twoheadrightarrow V/W_B.\)
Its rank is

\(\dim V/W_B=\dim\ker H_B.\)
Taking \(A\) as the initial history terms and \(B\) as initial plus rejection proves the claimed numerator and denominator. The argument remains valid when \(V/W_B=0\). The packet gives this concentration-to-quotient step at lines 190–230. 〔PRO_RESTRICTED_THEOREM_PACKET_2…〕

# 5. Gap arithmetic

Use one common upper bound \(t\) on the number of rank-one terms at both levels and

\(g=\min\{g_{\rm in},g_{\rm out}\}.\)
For a sufficiently small dyadic choice

\(\lambda=\Theta(\eta/t),\)
the concentration theorem permits

\(E=\Theta(\eta^2g\lambda^{26}),\)
hence

\(\boxed{
E=\Omega\!\left(\frac{\eta^{28}g}{t^{26}}\right).
}\)
Under common-copy unweighting,

\(F=\lambda^{-2},\)
and the symmetric spectrum scales by \(F\), while the asymmetric sector starts at at least \(1\). Therefore

\(\widehat E\ge\min\{FE,1\},\)
with

\(\boxed{
FE=\Omega\!\left(\frac{\eta^{26}g}{t^{24}}\right).
}\)
These are floors, not equalities.

For the unweighted construction to remain polynomial size, \(\eta^{-1}\) must be polynomially bounded, or \(\eta\) may simply be fixed. The same labeled copy blocks must be used at both levels.

# 6. Spectator and fraction separation

For a circuit containing individual \(H\) gates, add one maximally mixed, unmeasured spectator \(a\) and replace each \(H_j\) by \(H_j\otimes H_a\). If \(h\) is the number of Hadamards,

\(U'=U\otimes H_a^h,
\qquad
J'=J\otimes I_a,
\qquad
P_{\rm acc}'=P_{\rm acc}\otimes I_a.\)
Therefore, for every parity of \(h\),

\(\boxed{
M'=J'^\dagger U'^\dagger P_{\rm acc}'U'J'
=M\otimes I_a.
}\)
Thus

\(D'=2D,\qquad
S'=S\otimes\mathbb C^2,
\qquad
\dim S'=2\dim S,\)
and the normalized fraction is unchanged. The off-perfect bound is also unchanged on

\((S')^\perp=S^\perp\otimes\mathbb C^2.\)
Finally, writing

\(f=\frac{\dim S}{D},
\qquad
p=\frac{\operatorname{Tr}M}{D},\)
the spectrum of \(M\) gives exactly

\(f\le p\le r+(1-r)f.\)
For \(r\le1/3\),

\(p\ge\frac23\Longrightarrow f\ge\frac12,\)
while positivity gives

\(p\le\frac13\Longrightarrow f\le p\le\frac13.\)
An additive error below \(1/12\), such as \(1/24\), distinguishes the cases at threshold \(5/12\). This transfers only the explicitly defined circuit promise. 〔PRO_RESTRICTED_THEOREM_PACKET_2…〕

# Smallest remaining theorem-level obstacle

The smallest remaining obstacle to a substantial TCS claim is now **source complexity**, not palette closure.

The reduction currently starts from a bespoke exact promise requiring simultaneously:

\(M|_{S^\perp}\preceq\frac13I,
\qquad
p\ge\frac23\ \text{or}\ p\le\frac13,\)
over the exact real gate set, while preserving the eigenvalue-\(1\) multiplicity. To obtain a compelling complexity theorem, one needs a gate-exact reduction from a recognized source problem to this promise—preferably with nontrivial growing \(D\), rather than the normalization-degenerate \(D=1\) specialization.

Until that is proved, the surviving result is a rigorous and nontrivial **representation/transfer theorem for an explicit circuit promise**, not a standard-class hardness theorem. Novelty relative to prior parsimonious homology and normalized-persistence work remains a separate priority question.
