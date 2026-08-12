# External review status

Date: 2026-08-12.

The `research-refine` workflow requested an adversarial external review of all
three routes.  Background job
`70947b84a20b4cf6901ee1e79e2b099d` terminated with:

```text
status: failed
error: Not logged in · Please run /login
threadId: null
response: null
```

No external score or verdict exists.  This is an infrastructure limitation,
not evidence for or against any Ramsey claim.  Internal audits and independent
machine checks remain separately documented; none is relabeled as external
peer review.

Since that failure, two independent internal subagents completed a full proof
replay and an adversarial follow-up for the beta-`0.0299` upper bound; both
returned `YES`, and a third subagent repaired the imported BookCor source proof.
Those results justify the local evidence label `COMPUTER-ASSISTED THEOREM`, but
they are still not external human peer review.  See `upper/findings.md`,
`upper/INDEPENDENT_PROOF_REPLAY.md`, and `upper/BOOKCOR_AUDIT.md`.

The later fourth-stage octic certificate lowers the local base to
`3.7808931385024181222...`.  Its own independent adversarial application
review has now rerun the full four-stage chain, the separately structured
direct checker, and the regression tests and returned `PASS WITH IMPORTED
DEPENDENCY`; see `upper/INDEPENDENT_STAGE4_REFEREE.md`.  This is still an
internal independent replay, not external human peer review.

Subsequent internal work now gives the stronger conditional retained-spine
bound `3.780685745`.  Its hybrid-correlation proof, complete wedge enclosure,
384-bit author checks, non-importing 512-bit replay, and independent adversarial
referee all pass.  This materially strengthens the local evidence but does not
change the external-review status: no external human referee, publication, or
priority verdict has been obtained.
