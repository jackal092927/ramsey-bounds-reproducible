# Independent referee of the retained-spine numerical certificate

Date: 2026-08-12  
Role: independent adversarial replay of the numerical enclosure only

## Verdict

```text
claim C_* <= U(1)-10^(-8):                 PROVABLE AS STATED
analytic cover of the complete square:     PASS
independent 320-bit Arb replay:             PASS
terminating decimal base upper bound:      PASS
frozen upstream transfer theorem replay:   OUT OF SCOPE (pinned PASS input)
```

I found no missing region, endpoint, branch, or inequality reversal in the
frozen numerical certificate.  Conditional on the already refereed transfer
theorem and its stated Yang--Mao/P6 trust boundary, I approve

\[
 C_*\le U(1)-10^{-8}
\]

and therefore

\[
 R(k,k)\le
 \exp\!\left((U(1)-10^{-8})k+o(k)\right).
\]

The exact certified base is
\(\exp(U(1)-10^{-8})\), and Arb proves the safe terminating-decimal
statement

\[
 \exp(U(1)-10^{-8})<3.780698389989140.
\]

Thus it is also safe to report

\[
 R(k,k)\le(3.780698389989140)^{k+o(k)}.
\]

The frozen numerical note and its checker were not edited during this review.

## Frozen inputs and review artifact

```text
f8117f7dfd12113ee153fd9a32786ee2e6393cd6396a2b1f2790a4c3bc6c86fa  RETAINED_SPINE_NUMERIC_CERTIFICATE.md
fa19734aa1a29ea14c643cc98ae964ae8c99e6d2bcd0386c88888933c25e427a  check_retained_spine_numeric.py
8682a2dc07763b65104140cccb6fbfb94ac9617dc7ba0349122478a81bc1c892  independent_check_retained_spine_numeric.py
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
```

The new independent checker uses `python-flint==0.9.0` at 320-bit precision.
It hard-codes the fourteen decimal P6 coefficients and requires exact string
equality with the frozen JSON payload, evaluates all polynomials by Horner's
rule, and does not import either author checker or the old rate routines.

## Claim and dependency map

Write \(x=\sigma_R\), \(y=\sigma_B\),

\[
 r_0=1.6\cdot10^{-6},\qquad \Delta=10^{-8},
\]

\[
 A=U(1)-2c_\eta,\qquad E=U'(1)-c_\eta.
\]

The claim depends on four items:

1. on the complement of the small square, equation (18) of the pinned
   transfer note bounds the direct branch \(D\);
2. on the closed small square, the two page branches and the reservoir branch
   are each at most \(U(1)-\Delta\);
3. since \(B=\max\{P_R,P_B,Q\}\), item 2 bounds \(B\), while item 1 bounds
   \(D\); hence every point has \(\min\{D,B\}\le U(1)-\Delta\);
4. maximizing over the closed square yields the claimed bound for \(C_*\).

The review below reconstructs both pieces of the domain cover, including all
closed boundaries.

## Independent reconstruction of the outer region

Partition the part with \(\max\{x,y\}\ge r_0\) into the two closed ordered
triangles \(x\le y\) and \(y\le x\).  These triangles cover the whole outer
region and overlap harmlessly on the diagonal.

On \(x\le y\), equation (18) gives

\[
 U(1)-D(x,y)\ge xA+(y-x)E.
\]

The independent Arb replay proves \(E\ge A>0\).  Consequently

\[
 xA+(y-x)E\ge xA+(y-x)A=yA
 \ge r_0A.
\]

The symmetric calculation on \(y\le x\) gives the lower bound \(xA\), again
at least \(r_0A\).  The replay certifies

\[
 r_0A-\Delta
 =5.78775713351096985498434347\ldots\times10^{-10}>0.
\]

This is a non-strict closed-region argument, followed by a strictly positive
numerical margin, so the boundary \(\max\{x,y\}=r_0\) is included.

The only point at which both homogeneous remainders vanish and the ratio in
the derivation of (18) is undefined is \((1,1)\).  There

\[
 U(1)-D(1,1)=A\ge r_0A>\Delta.
\]

If exactly one remainder vanishes, the other ordered-triangle formula has a
positive denominator and ratio zero; equivalently, the same conclusion
follows from \(U(0)=0\) and continuity.  Thus no axis endpoint is omitted.

## Independent reconstruction of the inner square

Let \(S=[0,r_0]^2\).  The positive-part operations in the page definition are
inactive on \(S\), because \(1-\tau-r_0>0\).  For the first page branch,

\[
 (1-y)-(1-\tau-x)=\tau+x-y\ge\tau-r_0
 =4.84\cdot10^{-5}>0.
\]

Therefore \(1-y\) is always the larger homogeneous coordinate, including all
four edges of \(S\), and

\[
 P_R(x,y)=c_\eta(x+y)+\tau q+(1-y)U(z),
 \qquad z=\frac{1-\tau-x}{1-y}.
\]

The function \(z\) decreases with \(x\) and increases with \(y\), giving the
complete exact interval

\[
 z\in\left[1-\tau-r_0,\frac{1-\tau}{1-r_0}\right]
 =[0.9999484,0.999951599922559876\ldots].
\]

The second page branch has the same argument after transposing \(x,y\); its
coordinate-ordering margin is again at least \(\tau-r_0\), and it has exactly
the same \(z\)-interval.

Differentiation gives

\[
 \partial_xP_R=c_\eta-U'(z),\qquad
 \partial_yP_R=c_\eta-U(z)+zU'(z).
\]

The independent checker re-proves \(U''<0\) on \((0,1]\) using an analytic
pole bound up to \(1/16384\) and 16,384 closed Arb cells thereafter.  This is
a different partition from the author's \(10^{-4}\)/8,192-cell replay.  Since
\(U'\) is decreasing and \(g(z)=U(z)-zU'(z)\) has
\(g'(z)=-zU''(z)>0\), the weakest signs of both displayed derivatives reduce
to the upper endpoint \(z_+=(1-\tau)/(1-r_0)\).  Direct 320-bit evaluation
gives

```text
c_eta-U'(z_+)                    = -0.10420835417362051499... < 0
c_eta-U(z_+)+z_+ U'(z_+)         =  0.09759661892930348360... > 0
```

Hence \(P_R\) decreases in \(x\) and increases in \(y\), so its maximum is
at \((0,r_0)\).  By transposition, the other page branch is maximized at
\((r_0,0)\), with the same value.  The independent enclosure is

\[
 U(1)-\Delta-P_{\rm axis}
 =5.27402580532801144043691534\ldots\times10^{-8}>0.
\]

The reservoir branch is coordinatewise increasing because \(c_\eta>0\), so
its maximum is at \((r_0,r_0)\).  The replay gives

\[
 U(1)-\Delta-Q(r_0,r_0)
 =0.7603954110115865932708875\ldots>0.
\]

Thus both page branches and \(Q\) are below the target throughout the closed
inner square.  It follows that

\[
 B=\max\{P_R,P_B,Q\}\le U(1)-\Delta
\]

there.  Together with the direct bound on the outer region, this proves the
complete max/min claim with no uncovered boundary.

## Arb replay and upward rounding

The author's checker was run unchanged and returned `PASS`.  The independent
checker also returned `PASS`, with the proof-critical values

```text
outer margin over 1e-8:       5.78775713351096985498434347...e-10
page margin:                  5.27402580532801144043691534...e-8
reservoir margin:             0.7603954110115865932708875...
certified exponent:           1.3299087518219930723187812632...
certified base:               3.7806983899891396098255654219...
frozen P6 base:               3.7806984277961236987518816497...
rigorous base improvement:    3.78069840889263162278290346...e-8
```

The Arb ball for the certified base lies strictly below the exact terminating
decimal `3.780698389989140`; this comparison, rather than truncation of the
printed midpoint, supplies the upward-rounded published numeral.  The
independent replay also proves that the frozen P6 base lies above that
terminating decimal and directly encloses a positive base improvement.

## Claim boundary and residual trust

This review approves only the conditional computer-assisted asymptotic bound
stated in the verdict.  It does not independently prove the Yang--Mao v1
regularization/book theorems, the frozen P6 off-diagonal theorem, or the
already refereed combinatorial retained-spine transfer.  It does not provide
a finite-\(k\) threshold, an approximation to the optimizer defining \(C_*\),
external peer review, a proof-assistant formalization, or a global novelty
claim.  The remaining numerical trust boundary is Arb containment in
`python-flint==0.9.0`.

