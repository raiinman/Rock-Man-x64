# DOT: research handoff and work request

**For DOT / native development. Status: corrected original-side helper chain measured; native state-owner and GPU completion decision requested.**

The research workbench is available. Please select one actionable task and reply in this file or [issue #2](https://github.com/raiinman/Rock-Man-x64/issues/2), identifying the relevant revision, permitted inputs, deliverable and acceptance criteria. If A0:49 work is deferred, assign the next useful research or workbench question. This page is a public coordination entry point, not a native capability receipt.

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

The [new controller scope](research/bios/ORIGINAL-GAME-STARTUP.md#controller-progression-to-the-opening-dungeon) also reaches the opening dungeon corridor with the gameplay HUD. Its original-game success is separate from the native blocker. Your latest acknowledgment covers the earlier static/incomplete scopes; the corrected reaching-pointer/result observation now supersedes those specific research unknowns. Please return a concrete native mapping/decision or exact remaining dependency, rather than treating the earlier missing measurement as unchanged.
