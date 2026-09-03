# Bounded next gate: exact source complexity

September 3, 2026. Continue the same TDA conversation after your completed restricted-theorem integration review. That full response and an independent disposition are archived. We accepted your source-interface correction and now restrict to maximally mixed input qubits, computational-basis clean ancillas, and a fixed-local computational-basis output measurement.

**TEXT ONLY. No browsing, downloads, code execution, file writes, literature search, or renewed gadget audit. Return a completed hostile source-complexity analysis within 2400 words.** Treat the corrected geometric transfer theorem and its finite certificates as hypotheses for this gate.

This request has one objective: determine the strongest exact complexity consequence supported by the current theorem without silently promoting it to unrestricted \(\mathsf{SDQC}_1\)-hardness.

The supplied primary-source check records Lowe--Kim--Bondesan--Hayakawa arXiv:2607.03278v1 Definition 2 as follows. For an acceptance operator \(M\), there is a perfectly accepted subspace \(S\), every unit vector in \(S^\perp\) is accepted with probability at most \(r=1/3\), and the maximally mixed acceptance probability obeys \(p\ge a\) in YES and \(p\le b\) in NO, where Definition 2 permits arbitrary \(a-b\ge1/\operatorname{poly}\). The source explicitly says the class depends on the exact gate set. Its equation (9) says perfect-subspace-preserving amplification makes the new acceptance probability close to \(f=\dim S/D\). Sections 5.5--5.6 then use \(f\) for exact-kernel normalized persistence; Section 7 formulates exact kernel/gap/functorial realization as the missing TDA route.

Our exact algebra is
\[
f\le p\le r+(1-r)f,
\]
so the guaranteed fraction separation is
\[
\delta_f=\max\left\{0,\frac{a-r}{1-r}\right\}-b.
\]
At \((a,b,r)=(2/3,1/3,1/3)\), this is \(1/6\), and target error \(1/24\) is safe. Arbitrary trace gaps fail at the operator level: \(M_{\rm Y}=I/4\) and \(M_{\rm N}=0\) both have \(f=0\), while their traces differ and both obey \(r=1/3\).

Audit these points in order:

1. Prove or refute the displayed fraction intervals and the necessity of \(\delta_f>0\) for any reduction that reads only the exact perfect-space fraction.
2. Does exact-subspace-preserving Marriott--Watrous amplification repair arbitrary \(a,b\), or does it merely make the *new* trace close to the unchanged \(f\), thereby losing an original trace gap that came from imperfectly accepting states? Identify the first valid or invalid inference in the checked source route. Do not issue a global paper verdict.
3. Define the strongest noncircular restricted source statement. Is it defensible to call the target hard for a fixed-threshold separated class \(\operatorname{SepSDQC}_1^{\mathcal G_R}\), where \(\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\}\), or should we state only a many-one reduction from an explicitly named circuit promise? Explain what additional theorem would be needed to reach the source's arbitrary-threshold Definition 2.
4. Check exact gate/interface compatibility. The source has one clean measured qubit and a maximally mixed remainder; our theorem permits that standard inclusion plus computational-basis clean work. The spectator identity converts every single \(H\) to \(H\otimes H\) with \(M'=M\otimes I\). Does this suffice for circuits already written over \(\mathcal G_R\)? Do not use approximate universality, a complex phase simulation, or assume that amplification remains in \(\mathcal G_R\) without proof.
5. Our quotient theorem directly proves endpoint Betti dimensions and induced rank, but does not assert one exact common harmonic isometry satisfying every operator identity in the source's Conjecture 2. Can it nevertheless prove the rank conclusion needed for a restricted version of Conjecture 1 directly? Distinguish bypassing a sufficient conjecture from proving that conjecture.
6. Give the smallest remaining lemma that would upgrade the result. If no exact threshold/gate-set reduction is derivable from the supplied facts, state a hard stop and retain only the separated-promise corollary.

Return: (i) a short verdict; (ii) a corrected theorem/corollary with all threshold and gate assumptions; (iii) a status table for explicit-promise reduction, separated-class hardness, unrestricted \(\mathsf{SDQC}_1\), restricted Conjecture 1, and Conjecture 2; and (iv) one finite next proof target or a stopping conclusion. Distinguish a mathematical obstruction from novelty and class-significance risk. Do not claim BQP/DQC1 hardness, complex-gate coverage, full source priority, or paper readiness.
