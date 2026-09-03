# Pro source-complexity review — complete response

Collected 2026-09-03T19:27:37.090Z. The browser showed a completed response, **Worked for 8m 41s**, after user message 7 and the source-complexity packet. This is external model review, not independent correctness, novelty, literature, or unrestricted-class certification.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: b78da7ab9472f6d2c0858634b56f3c1210a3e931.
- Actual task: [source-complexity submission](PRO_SOURCE_COMPLEXITY_SUBMISSION_2026-09-03.md).
- Input: [PRO_SOURCE_COMPLEXITY_PACKET_2026-09-03.md](PRO_SOURCE_COMPLEXITY_PACKET_2026-09-03.md), 28196 bytes, SHA-256 7f38dd8353d90b9fe7c471dfb0e83bcd5bdca31a7ee5a011cbbd64ad91a12c15.
- Visible account at collection matched the registered personal Pro identity already verified in this browser session; the public archive omits the account email.
- Exact browser completion time was not exposed; collection time and displayed duration are separate facts.

The response below was transcribed from the rendered DOM and cross-checked against ChatGPT's copied Markdown. All **113** equation elements were recovered from displayed `data-math-source` attributes. Visible attachment citation labels are preserved as 〔…〕. The answer contains no external links. [The capture record](PRO_SOURCE_COMPLEXITY_REVIEW_CAPTURE_2026-09-03.json) retains the displayed text and exact equation sources. Pro explicitly did not reopen the named primary source; its source statements came from the supplied packet. Adopted conclusions are recorded separately.

---

# Verdict

**Arbitrary-threshold \(\mathsf{SDQC}_1\) does not reduce, from the supplied definitions alone, to the exact perfect-space fraction**
\[
f=\frac{\dim\ker(I-M)}{D}.
\]

The obstruction occurs **before** gate compilation or TDA geometry: an arbitrary inverse-polynomial gap in the normalized trace
\[
p=\frac{\operatorname{Tr}M}{D}
\]
need not imply any gap in \(f\). Exact perfect-subspace-preserving Marriott–Watrous amplification does not repair this; it preserves \(f\) and drives the amplified trace toward that same \(f\), potentially erasing a distinction carried entirely by imperfectly accepting states.

The strongest surviving consequence is:

> a polynomial reduction from an explicitly defined, exact-real-gate, perfect-eigenspace-separated circuit promise whose thresholds satisfy a positive perfect-fraction separation condition.

In particular, the standard constants
\[
(a,b,r)=\left(\frac23,\frac13,\frac13\right)
\]
are valid and yield
\[
f_{\mathrm{YES}}\ge\frac12,\qquad
f_{\mathrm{NO}}\le\frac13.
\]

I did not independently reopen Lowe–Kim–Bondesan–Hayakawa for this bounded task. The source statements used below are the targeted reading recorded in the packet: Definition 2 allows arbitrary inverse-polynomial trace thresholds, equation (9) concerns amplification toward the perfect-space fraction, and the exact gate set is explicitly material. 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

---

# 1. Exact characterization of the possible fractions

Let

\[
0\preceq M\preceq I,\qquad
S=\ker(I-M),
\]

and assume

\[
M|_{S^\perp}\preceq rI,\qquad 0\le r<1.
\]

Set

\[
f=\frac{\dim S}{D},
\qquad
p=\frac{\operatorname{Tr}M}{D}.
\]

The eigenvalues on \(S\) are exactly \(1\); those on \(S^\perp\) lie in \([0,r]\). Therefore

\[
\boxed{
f\le p\le f+r(1-f)=r+(1-r)f.
}
\]

Thus:

\[
p\ge a
\quad\Longrightarrow\quad
f\ge
\ell:=
\max\left\{0,\frac{a-r}{1-r}\right\},
\]

while

\[
p\le b
\quad\Longrightarrow\quad
f\le p\le b.
\]

Hence the guaranteed fraction separation is

\[
\boxed{
\delta_f=\ell-b
=
\max\left\{0,\frac{a-r}{1-r}\right\}-b.
}
\]

These are the intervals recorded in the packet. 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

## Necessity, not merely sufficiency

Under only these operator promises, the possible fraction sets are exactly

\[
F_{\mathrm{YES}}=[\ell,1],
\qquad
F_{\mathrm{NO}}=[0,b],
\]

up to the rational discretization \(fD\in\mathbb Z\).

To see the nontrivial direction, suppose \(q\in[\ell,b]\) and choose \(D\) with \(qD\in\mathbb Z\). Let \(S_0\) have dimension \(qD\). Define

\[
M_{\mathrm N}=I_{S_0}\oplus0_{S_0^\perp}.
\]

Then

\[
f(M_{\mathrm N})=q,\qquad
p(M_{\mathrm N})=q\le b.
\]

For the YES operator, assuming \(q<a\), set

\[
\alpha=\frac{a-q}{1-q},
\qquad
M_{\mathrm Y}=I_{S_0}\oplus\alpha I_{S_0^\perp}.
\]

Because \(q\ge(a-r)/(1-r)\),

\[
\alpha\le r.
\]

Moreover,

\[
p(M_{\mathrm Y})
=
q+(1-q)\alpha
=
a,
\]

while

\[
f(M_{\mathrm Y})=q=f(M_{\mathrm N}).
\]

Therefore, whenever \(\delta_f\le0\), admissible YES and NO operators can have **identical exact perfect-space fractions**. No reduction whose target statistic is exactly \(f\), followed by postprocessing that sees only \(f\), can distinguish all such instances.

The packet’s special case

\[
M_{\mathrm Y}=\frac14I,\qquad M_{\mathrm N}=0
\]

is the choice \(a=1/4\), \(q=0\), \(r=1/3\). 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

Accordingly,

\[
\boxed{\delta_f>0}
\]

is necessary and sufficient for a promise-level reduction that simply realizes the exact perfect-space fraction.

This does not rule out a fundamentally different exact transformation that creates a new perfect subspace encoding the original trace.

---

# 2. Why perfect-space-preserving amplification does not repair arbitrary thresholds

Suppose an exact amplification maps the acceptance operator \(M\) to \(\widetilde M\) such that:

1. the perfectly accepted space is unchanged, possibly tensored with a fixed ancilla space;
2. eigenvalue \(1\) remains exactly \(1\);
3. every eigenvalue in \([0,r]\) is mapped to an amplified acceptance value at most \(\varepsilon\).

Then the perfect fraction is unchanged:

\[
\widetilde f=f.
\]

The amplified normalized trace satisfies

\[
f
\le
\widetilde p
\le
f+\varepsilon(1-f),
\]

so

\[
|\widetilde p-f|\le\varepsilon.
\]

This is precisely what an equation asserting that amplified acceptance is close to the normalized perfect-space dimension means. It is a valid statement. But it does not imply that the original trace promise separates \(f\).

For the two same-\(f\) operators above, amplification sends both traces toward the same number \(q\). Their original distinction may have resided entirely in the eigenvalues below \(1\), and amplification suppresses those eigenvalues.

Therefore:

- **valid inference:** amplification preserves the exact perfect subspace and makes amplified trace approximate \(f\);
- **first invalid inference:** using an arbitrary original trace gap \(p_{\mathrm Y}\ge a\), \(p_{\mathrm N}\le b\) to conclude that the unchanged fractions \(f_{\mathrm Y}\) and \(f_{\mathrm N}\), or the amplified traces converging to them, remain separated.

The failure is algebraic, not a TDA issue. Exact gate-set compatibility of amplification is a second, later obstacle.

---

# 3. Strongest noncircular source promise

Define the promise problem

\[
\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)
\]

as follows.

The input is a polynomial-size exact circuit over

\[
\mathcal G_R=
\{X,\mathrm{CX},\mathrm{CCX},H\},
\]

with:

- maximally mixed input qubits;
- computational-basis clean ancillas;
- the standard inclusion
  \[
  J=I_{\mathrm{mixed}}\otimes|c\rangle_{\mathrm{clean}};
  \]
- a fixed-local computational-basis acceptance measurement \(P_{\mathrm{acc}}\).

Let

\[
M=J^\dagger U^\dagger P_{\mathrm{acc}}UJ,
\qquad
S=\ker(I-M),
\qquad
D=\dim\operatorname{dom}J.
\]

Promise:

\[
M|_{S^\perp}\preceq rI,
\]

and either

\[
p=\frac{\operatorname{Tr}M}{D}\ge a
\]

or

\[
p\le b,
\]

where

\[
\boxed{
\delta_f=
\max\left\{0,\frac{a-r}{1-r}\right\}-b
\ge\frac1{\operatorname{poly}(n)}.
}
\]

This source is noncircular: its decision promise is stated using the circuit’s trace acceptance probability, not using the target persistence ratio.

## Corrected reduction corollary

Assuming the previously accepted finite-palette geometric theorem, there is a polynomial many-one transformation to nested weighted clique complexes

\[
X_{\mathrm{in}}\subseteq X_{\mathrm{out}}
\]

such that

\[
\beta_d(X_{\mathrm{in}})=D,
\]

\[
\beta_d(X_{\mathrm{out}})
=
\operatorname{rank}
\left[
H_d(X_{\mathrm{in}})
\to H_d(X_{\mathrm{out}})
\right]
=
\dim S,
\]

and therefore

\[
\boxed{
q(X_{\mathrm{in}},X_{\mathrm{out}})
=
\frac{\beta_d(X_{\mathrm{in}}\to X_{\mathrm{out}})}
{\beta_d(X_{\mathrm{in}})}
=
\frac{\dim S}{D}
=f.
}
\]

Both endpoint Laplacians have the previously established inverse-polynomial whole-kernel gaps. The common-copy unweighted version remains conditional on its separate theorem. 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

An additive approximation with error

\[
\varepsilon<\frac{\delta_f}{2}
\]

decides the source promise.

At

\[
(a,b,r)=\left(\frac23,\frac13,\frac13\right),
\]

one obtains

\[
f_{\mathrm Y}\ge\frac12,
\qquad
f_{\mathrm N}\le\frac13,
\qquad
\delta_f=\frac16.
\]

The decision threshold is

\[
\frac{1/2+1/3}{2}=\frac5{12},
\]

and error \(1/24\) is safely below \(1/12\).

---

# 4. May this be called \(\operatorname{SepSDQC}_1^{\mathcal G_R}\)-hard?

**Formally yes, with a qualification.**

One may define \(\operatorname{SepSDQC}_1^{\mathcal G_R}\) to be the class of languages having uniform exact \(\mathcal G_R\)-verifiers with the standard mixed/clean interface and, for example,

\[
(a,b,r)=\left(\frac23,\frac13,\frac13\right).
\]

For every language in that class, its uniform circuit constructor followed by the geometric transformation is a polynomial reduction. Thus normalized persistence is hard for that explicitly defined restricted class.

However, this is a newly delimited, gate-dependent subclass. Until a robustness or equivalence theorem relates it to the source’s arbitrary-threshold Definition 2 or another recognized class, the phrase

> “\(\operatorname{SepSDQC}_1^{\mathcal G_R}\)-hard”

has less content than the explicit circuit-promise reduction and can be mistaken for unrestricted \(\mathsf{SDQC}_1\)-hardness.

The cleanest theorem headline should therefore use the explicit promise problem. The restricted-class formulation is an optional formal corollary. The packet reaches the same boundary. 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

---

# 5. Exact gate and spectator compatibility

For circuits already over

\[
\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\},
\]

the mixed spectator exactly converts every single Hadamard into an allowed \(H\otimes H\) gate.

Add one maximally mixed, unmeasured spectator \(a\), and replace each system Hadamard \(H_j\) by

\[
H_j\otimes H_a.
\]

If the original circuit contains \(h\) Hadamards, then

\[
U'=U\otimes H_a^h.
\]

With

\[
J'=J\otimes I_a,
\qquad
P_{\mathrm{acc}}'=P_{\mathrm{acc}}\otimes I_a,
\]

one has, for either parity of \(h\),

\[
\begin{aligned}
M'
&=
J'^\dagger U'^\dagger
P_{\mathrm{acc}}'
U'J'\\
&=
M\otimes I_a.
\end{aligned}
\]

Consequently,

\[
S'=S\otimes\mathbb C^2,
\qquad
D'=2D,
\qquad
f'=f,
\]

and the off-perfect spectral ceiling remains \(r\). This suffices for source circuits already expressed exactly over \(\mathcal G_R\). 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

It does **not** show that Marriott–Watrous amplification can be implemented exactly over \(\mathcal G_R\), nor that arbitrary exact gate sets reduce to \(\mathcal G_R\). Approximate universality is irrelevant because approximate compilation need not preserve the eigenvalue-\(1\) space.

---

# 6. Relation to the two normalized-persistence conjectures

The quotient theorem directly proves, for the supported separated real-gate histories,

\[
\beta_d(X_1)=\dim\ker H_1,
\]

and

\[
\beta_d(X_1\to X_2)=\dim\ker H_2.
\]

Thus it proves the **rank conclusion** needed for a restricted version of Conjecture 1, without constructing one exact common harmonic isometry satisfying every operator identity posited in Conjecture 2.

Therefore:

- Conjecture 2 is **bypassed as a sufficient mechanism**;
- it is **not proved**;
- the restricted rank/hardness conclusion can nevertheless follow directly from quotient naturality and exact whole-kernel multiplicity.

This distinction is explicitly recognized in the source-complexity note. 〔PRO_SOURCE_COMPLEXITY_PACKET_20…〕

---

# 7. Status table

| Claim | Status |
|---|---|
| Reduction from the explicit standard-constant real-gate promise | **Established**, conditional on the accepted geometric theorem |
| Reduction for general \(a,b,r\) with \(\delta_f\ge1/\mathrm{poly}\) | **Established** |
| Hardness for an explicitly defined \(\operatorname{SepSDQC}_1^{\mathcal G_R}\) | **Formally defensible**, but this is a nonstandard restricted class |
| Arbitrary-threshold Definition-2 \(\mathsf{SDQC}_1\) | **Not established**; the direct fraction inference is false |
| Repair by perfect-space-preserving amplification | **Refuted** as a general solution |
| Exact \(\mathcal G_R\to G_2\) spectator interface | **Established** |
| Exact gate compatibility of an amplification procedure | **Unproved** |
| Restricted Conjecture-1 rank conclusion | **Established** for the supported separated source |
| Conjecture 2’s exact compatible harmonic isometries | **Not established and not needed for this restricted conclusion** |
| BQP, DQC1, or unrestricted SDQC1 hardness | **Not implied** |

# Exact remaining gate

The smallest upgrading lemma would have to state:

> Given an arbitrary-threshold Definition-2 verifier over an exact specified gate set, construct in polynomial time an exact compatible verifier whose perfect-space fraction has an inverse-polynomial YES/NO separation, while retaining a whole off-perfect spectral ceiling and the standard mixed/clean interface.

A transformation that merely preserves

\[
S=\ker(I-M)
\]

up to a fixed ancillary tensor factor cannot satisfy this lemma: the same-\(f\), different-trace operators above remain a counterexample. The transformation would have to create new exact eigenvalue-\(1\) states based on information in the imperfect spectrum, or the source definition must add the promise \(\delta_f>0\).

No such exact spectral-thresholding or gate-set theorem is supplied. The hard stop is therefore:

\[
\boxed{
\text{retain the separated real-gate promise corollary; do not claim unrestricted }
\mathsf{SDQC}_1\text{-hardness.}
}
\]
