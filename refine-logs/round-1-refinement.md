# Round 1 refinement

The initial proposal treated joint coefficient/witness optimization as the main
near-term task.  Reproduction showed that optimization is not yet the binding
bottleneck: a one-parameter perturbation already improves the public candidate.

The refined plan therefore changes the order of work:

1. freeze the `a5=-0.07795` delta certificate and its provenance;
2. derive the implemented inequalities line by line from the source theorem;
3. write an independent interval checker from that derivation;
4. require overlap at the small/large split and explicit endpoint semantics;
5. only after both proof gates pass, resume joint optimization.

The success condition is also narrowed.  A smaller validator output is an
engineering result; a new Ramsey upper bound requires independent verification
and a complete theorem-to-certificate argument.
