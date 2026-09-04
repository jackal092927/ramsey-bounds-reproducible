# Version 2 proof audit

Status: **derived and internally checked in session; no external review yet.**

| Step | Claim | Where | Audit |
|---|---|---|---|
| Filling bound | `<y,Ay> >= |<x,y>|^2 / ||u||^2` for `A >= 0`, `x = A^{1/2}`-reachable, `||u||^2 >= <x,A^+x>` | Lemma A (`lem:filling-domination`) | Cauchy--Schwarz; minimum-norm preimage identity |
| Padded filling | `u = (W^{-1}c_a/||v_a||) (x) h` fills `(v_a/||v_a||) (x) h` | App. A.4 | outside weights one, `d h = 0` |
| Depth | `||W^{-1}c_a||^2 <= ||c_a||^2 lambda^{-2 p_a}` | Def. 3.3 | monomial weights, `lambda <= 1` |
| Guards/padding | do not change depth | App. A.4 | fillings tensor with register cycles |
| Exponent | `kappa = 2p`, only use of `kappa` is logical domination; absorption needs `kappa >= 2` | Thm 3.4, App. A.5 | checked against v1 proof line by line |
| Harmonic concentration | `||(I-P_K)x|| <= eta_1` for harmonic `x` | Lemma 6.1 | transfer bound at zero energy |
| Equal dimensions | `||P_H - P_K|| <= s` | Lemma 6.2 | principal angles |
| Large overlap | nonzero eigenvalues of `P_HB P_HA P_HB >= (1-2eta_1)^2`, exactly `dim K_B` of them | Thm 6.3 | Weyl + rank from Thm 4.2 |
| Preparation | `rho_{K_in}` preparable; projection error `2 eta_1^2/(1-eta_1^2)` | Thm 6.4 | Lemma 8 of Lowe et al. + bowtie encoding + phase estimation |
| Perfect subspace | `S = ker(I-M)`, `M|_{S^perp} <= I/3` from perfect completeness and soundness | Lemma B.x (`lem:perfect-subspace`) | direct |
| General source | `SF^{G_2}` reduction, `beta_in = 2^r`, `q = dim S/2^r` | Thm 5.4 | Prop. 5.2 with `C = clean (x) full mixed register` |
| SDQC1 forms | fraction form all thresholds; trace form iff `b < (3a-1)/2` | Cor. 5.5, App. B.5 | `f <= p <= (1+2f)/3` |
| Counting | `beta_d(X_out) = #phi`, gap; containment in #BQP | Thm 5.7 | classical source has `M|_{S^perp} = 0`; BFS/CC for containment |
| Unweighted transfer | overlap unitarily equivalent; lift isometry exact | Cor. 7.2 | `F = 2^{2b'}` |

Source facts used and checked in session: Lowe et al. arXiv:2607.03278v1
Definition 2, Definition 3, Problem 9, Lemma 7, Lemma 8, Theorems 5 and 7
proofs (fraction used), eq. (9), Conjecture 2, Lemma 11; Brown--Flammia--
Schuch #BQP definition and #BQP = #P (weakly parsimonious); Cade--Crichigno
Theorem 5 and #BQP_1 remark; Crichigno--Kohler Theorem 4 (no gap);
Schmidhuber--Lloyd Theorem 1 (clique-dense regime, no gap); Rudolph Theorem
3.4 mechanism (postselection-based; extension to SF left open).

Remaining risks: (1) no external review of the new sections; (2) the
counting containment relies on the standard phase-estimation verifier
argument as in Cade--Crichigno, stated rather than reproved; (3) the
preparation circuit's synthesis error is stated as `1/poly` without an
explicit accounting; (4) the trace-form SDQC1 discussion characterizes Lowe
et al.'s proofs and should be phrased with care in a submission.
