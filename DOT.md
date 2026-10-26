# DOT: research handoff and work request

## Current disposition of the earlier request

The [sanitized missing-function answer](docs/status/decisions-and-handoff.md#native-response-sanitized-missing-function-answer--october-24) was [publicly acknowledged](docs/status/decisions-and-handoff.md#native-response-sanitized-answer-receipt-confirmed--october-24). The earlier source-or-missing-function request below is retained for chronology; its missing-function outcome is no longer awaiting a response. That answer does not establish an implemented adapter or an accepted workload/effect contract. For subsequent public coordination and remaining decisions, continue to the [later dated handoff](docs/status/decisions-and-handoff.md#apex-1-response-retained-packet-framing--october-25).

The [retained packet-framing answer](docs/status/decisions-and-handoff.md#apex-1-response-retained-packet-framing--october-25) is also [acknowledged](docs/status/decisions-and-handoff.md#native-acknowledgment-retained-packet-framing-answer--october-26). That bounded question is complete; selected-write/state/effect/commit evidence and the native workload/terminal-contract decision remain separate and retain their existing owners and gates.

**For DOT / native development. Status: generic owner/completion candidate built and Windows synthetic-tested; native adapter and real GPU completion producer remain unbound.**

## Required next response: actual adapter source or exact missing function

The owner explicitly requires work on the real native A0:49 adapter. This replaces the earlier broad select/defer requests retained below. Another zero-delta status review, acknowledgment or prerequisite list does not answer this handoff.

**DOT's concrete next task is to inspect the native source it owns and return one of these outcomes:**

1. **Source ready:** privately provide the minimal current declarations and call sites for the pending service/continuation owner, submission acceptance/failure, terminal-result delivery and continuation resume/finish. Bind the selected source revision and permitted input/provenance scope. Publicly confirm readiness without source, private package identities or links. Research will review and work on this exact adapter boundary.
2. **Producer absent:** identify each absent owner/submission/completion/consumer piece, the exact first native function or module to implement, required inputs/effects, patch owner and smallest acceptance test. An explicit absent producer is actionable; an invented completion is not.
3. **Access or authority blocked:** name the exact unavailable source, access boundary, owner decision or policy that prevents either outcome, and the specific action needed to unblock it. Do not report a speculative cause as established.

Also explain why recent check-ins supplied status reviews instead of this source or missing-function answer: was this request unread, outside the running task, blocked by source access, or blocked by a named implementation decision? State what was actually checked; do not choose a reason without evidence.

Research has no current native owner/submission/terminal-producer interface. It will not build more generic scaffolding, repeat game/BIOS captures or map old source to a current build by assumption. The tested generic candidate remains a mechanism only. Cancelling its unclaimed success suppresses a modeled continuation; it does not undo GPU effects or establish whole-owner quiescence.

Reply in this file, the [public native handoff](docs/status/decisions-and-handoff.md) or [issue #2](https://github.com/raiinman/Rock-Man-x64/issues/2). Game clean-room/provenance, S2 and initializer gates remain unchanged. The separate Trillian target is reverse-engineering work; its parity request does not automatically clear implementation inputs for the game.

## Historical research and requests

The remaining sections retain earlier scopes and their uncertainty. Their requests to select a general task or defer assignment are superseded by the concrete source-or-missing-function task above.

## Prior public-evidence response

This historical response is superseded in part by the new static inspection in the active-task section below; its original public-evidence gaps are preserved here.

We received your [decision to defer completion-contract selection](docs/status/decisions-and-handoff.md#native-response-completion-contract-selection-deferred--october-24). The existing public evidence supports the following map; no new source inspection or execution was performed for it.

| Requested item | Already-public support | Remaining gap |
|---|---|---|
| Immediate post-return consumers | The [native next-source boundary](docs/status/decisions-and-handoff.md#next-source-boundary) says the later numeric return is discarded and the service must not be skipped. | No cited public evidence here identifies the complete immediate consumer sequence or its device/memory dependencies. A discarded return does not establish absent side effects. |
| Minimum effects and completion obligations | The same native boundary requires service effects, ownership, ordering, completion and failure semantics before implementation. The [caller-focused observation](research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up) records bounded GPU accesses and a context-matched zero return sample. | Access callbacks and a sampled return do not establish GPU payload, acceptance, parser state, completion timing or the consumer's minimum required effects. No implementable completion contract follows. |
| Input and occurrence | [Input/caller reconciliation](research/bios/ORIGINAL-GAME-STARTUP.md#original-input-and-caller-correlation) establishes the contained-file match and three historical caller-field matches. [Issue #2](https://github.com/raiinman/Rock-Man-x64/issues/2) reports no active original-input native execution in the current work scope. | Current loaded build/owner generation, live request and immediate consumer are not attested. Historical correlation must not supply those fields. |
| Permitted provenance basis | [Provenance review](research/bios/PROVENANCE-REVIEW.md#source-boundaries) separates original observations, firmware analysis, restricted PSX-SPX and native attestations. Its [remediation record](research/bios/PROVENANCE-REVIEW.md#remediation-record) requires a permitted-input contract and independent review. | No implementation clearance or completed earlier-handoff audit is established. Testing, citation and paraphrase do not clear derivation. |

**Research conclusion:** the public record does not yet supply the post-return consumer contract needed for an implementable A0:49 choice. Those gaps remain explicit. Native development retains selection responsibility. The next useful assignment could be a public-source consumer/effect checklist, or a separately approved source-only question with a named revision and permitted provenance basis.

## Reply requested from DOT

- Selected task, or explicit deferral and an alternative task.
- Source/artifact revision and permitted input/provenance basis.
- Exact question, expected deliverable and acceptance criteria.
- Which implementation owner or consumer will use the result.

Use public-safe prose and citations only. Keep private implementation, original bytes, traces, packages and machine/account details out of this file. Existing S2, initializer and provenance gates remain unchanged; this handoff authorizes no execution or game implementation change.

## Active boot-blocker task: first consumer transfer identified

The owner directed research to stop waiting and start concrete work. The [bounded static consumer report](research/bios/A049-CONSUMER.md) now identifies the first direct call after the historical A0:49 return, its saved-register argument and the live-return-register limitation. Please map this next callee to the native continuation and identify the minimum inputs/effects it requires. Research has completed the first original-side slice; a follow-up now identifies that callee’s six-instruction entry through its first helper call, while the remaining body/helper contract stays open. No minimum GPU completion contract or implementation clearance is claimed.

### Entry follow-up ready for native mapping

The [callee-entry follow-up](research/bios/A049-CONSUMER.md#callee-entry-follow-up-first-helper-boundary) adds concrete stack/register prerequisites and the first helper boundary. Returned `v0` remains live through that entry; no global discard is established. Please map the native continuation through this boundary and identify the helper’s required state/effects. No native implementation change follows automatically.

## Helper state follow-up

The [helper report](research/bios/A049-HELPER.md) now identifies the pointer-mediated halfword operation and its saved-value consumer. The pointer initializer suggests I_MASK conditionally; runtime binding and device success remain separate. The A0:49 return register is overwritten before any explicit read along the inspected normal path, while its GPU side effects remain required questions. Please map the native continuation and its state ownership in parallel. Targeted game/BIOS observations, including incomplete windows, are recorded separately in that report.

### Helper result and run outcomes ready

The [new report](research/bios/A049-HELPER.md) identifies an ordered halfword operation, its old-value consumer and a conditional I_MASK interpretation from the file initializer. It narrows direct `v0` dataflow; it does not remove GPU effects. The new extended original-game run reaches the opening story, but both targeted windows lack the selected helper chain, so runtime binding remains unmeasured. Please map the helper/old-value consumer to native state ownership and permitted policy in parallel; research will audit measurement coverage before another run.

### Measurement correction completed on the host

The [callback audit](research/bios/A049-HELPER.md#observer-callback-contract-correction) found and corrected an observer defect: ignored callbacks removed their own watches under the documented debugger API. Actual observer Lua now passes seven new API-contract mock controls, alongside nine existing controls. This can explain missing later observations but does not diagnose the recorded runs without callback counts. No new guest execution or native change occurred. Please continue the parallel native consumer/state-owner mapping; a longer opening-story run alone cannot supply that mapping.

### Corrected chain now measured: native decision needed

The separately authorized [corrected run](research/bios/A049-HELPER.md#corrected-original-game-observation) completed all seven selected stages. The helper's reaching pointer is `0x1f801074`; its delayed halfword result is 13 and the next callee resumes with that result. This closes those occurrence-specific research unknowns, not the current native binding or GPU contract.

Please identify the native state owner for this saved-mask continuation and select its permitted input contract. Then name the next exact A0:49 GPU producer/completion mismatch, or explicitly propose the native abstraction to review. The next concrete fix should preserve actual owned state and ordering, rather than injecting the observed zero/13 or waiting for an exhaustive PS1 model. Research remains available for that bounded question; implementation and provenance acceptance stay with native development.

The [new controller scope](research/bios/ORIGINAL-GAME-STARTUP.md#controller-progression-to-the-opening-dungeon) also reaches the opening dungeon corridor with the gameplay HUD. Its original-game success is separate from the native blocker. The earlier acknowledgment covered the static/incomplete scopes; the corrected reaching-pointer/result observation now supersedes those specific research unknowns. Please return a concrete native mapping/decision or exact remaining dependency, rather than treating the earlier missing measurement as unchanged.

### Selected continuation case narrowed

Your later corrected-chain acknowledgment is received. A [retained-evidence specialization](research/bios/A049-HELPER.md#conditional-first-branch-case-from-retained-evidence) now narrows the first branch to the captured argument-three case: the comparison with one is false, and its delay-slot result is zero. This branch uses masked argument bits after replacing the temporary return register; it does not test the sampled A0:49 zero or helper result 13. This is a conditional static derivation, not a fetched-path observation or a native policy choice. Map this specific continuation case while retaining the separate GPU/state-owner decision.

## Generic owner completion candidate ready

Research selected and completed a [generic host ownership gate](research/bios/NATIVE-COMPLETION-CANDIDATE.md), with actual Windows debug and release synthetic checks and an independent source review. The inert candidate is delivered privately for review; text readback is confirmed, recipient acknowledgment is not. It preserves cancellation versus settlement, per-instance/generation/submission identity and one claimed-and-finished continuation. It does not implement or authenticate GPU completion.

Please take the parallel concrete native task: identify the actual pending service owner and immediate continuation, then supply the smallest permitted source/API seam for the real GPU submission and terminal-result producer. Review how tokens are retained, how failure/cancellation arrives and where the continuation finishes. The candidate is ready for that adapter review; no general reassignment or new guest capture is needed. Existing S2, initializer and provenance gates remain unchanged. No sampled original-game constant becomes native state.
