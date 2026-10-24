# Decisions and next step handoff

Development resumed on 2026-10-22 at 22:04 UTC after the documentation pause. This page records the selected direction and the evidence needed before further milestones; it does not authorize implementation, device access, packaging or release.

Controlled BIOS/emulator diagnostics are permitted as separately labeled research—not hardware or native-boot proof; the finished game must remain native Windows without a BIOS/emulator runtime dependency or reused port/mod/emulator implementation, and original bytes, captures and private packages remain excluded from publication.

## Decisions in force

| Decision | Rationale and consequence |
|---|---|
| Native Windows x64 game with integrated IDE is the target | Asset tools are foundations, not a redefinition of completion |
| Independently reconstruct implementation without reusing existing port/mod/recomp code | Early platform comparisons and rejected alternatives are historical context, not implementation inputs or formal clean-room certification |
| Keep original data immutable and private | Inspection and edits must not overwrite source media; publish narrative separately |
| Compile recovered subsets into native code | No general interpreter or imported BIOS implementation fills unsupported gaps |
| Use explicit native platform policies | State where a service is newly designed rather than claiming PS1 hardware equivalence |
| Keep partial knowledge visible | Unknown bytes, flags and permissions cannot become convenient zeros or successes |
| Separate production authority from diagnostic fixtures | Demonstrations cannot grant capabilities or prove normal startup reachability |
| Retain committed work and pending obligations | Recoverable failures must not replay side effects or discard debt |
| Keep one authoritative CD mute owner | The connected synchronous mixer observes committed configuration under Session serialization rather than mirroring mutable mute state |
| Freeze only after complete review | Candidate tests, compiler passes and a terminal runner are insufficient by themselves |

## Current acceptance boundary

Native mode-00 validation is accepted after all 69 actual Windows cases passed (39 expected successes, 30 intentional refusals; 40 complete CLI JSON comparisons). All 605 kit files, including 26 case executables and support material, and separately three pre-existing original inputs remained unchanged. No original inputs were packaged. Raw local receipts were not independently downloaded by the reviewers. Acceptance is separate from unchanged frozen payloads and historical metadata; no final or public game release is implied.

The accepted mode stage stops at `8001b44c`. Newer graphics-entry work has bounded Linux acceptance: 12 connected cases, a 69-case regression and 11 targeted allocation checkpoints passed. The later diagnostic continuation passed 19 connected cases and its 69-case Linux regression, and 29 targeted allocation checkpoints; independent final review accepted this bounded Linux stage. Do not promote either graphics subset to Windows parity or a repeated 13-stage full-project aggregate.

## Next source boundary

The diagnostic continuation performs one real diagnostic publication, a bounded RAM clear and guarded initialized callback, then stops at A0:49 (`8007cc0c`). Keep the actual continuation and pending obligations; do not skip the service. Earlier native-project reporting described its numeric return as later discarded. The [caller and callee-entry inspections](../../research/bios/A049-CONSUMER.md) left the return register live; the subsequent [helper report](../../research/bios/A049-HELPER.md) now identifies its replacement before any explicit operand read along the inspected normal path. This bounded direct-dataflow finding does not establish absence of asynchronous/exception observation or permit dropping service effects. Reaching pointer state, native continuation ownership and minimum GPU completion obligations remain unresolved.

The inspected Sony OS (1998) and Runtime 4.7 pages do not bind the exact service contract. Community documentation offers a provenance-limited lead, not implementation authority. This is not a universal absence-of-documentation claim. Establish applicable service effects, ownership, ordering, completion and failure semantics before implementation. No fabricated GPU readiness or successful no-op is acceptable.

The IDE Source bytes/Back feature passed 50 actual Windows synthetic command/state checks. Standalone visual preflight was blocked before launch by unavailable supported capability; pixels and original-asset UI remain unverified. Current-disk bytes are not authenticated prior-decode content.

All four combined Linux phases are accepted: 16 aggregate/source-test stages, 69 regression cases, 19 connected cases and 29 targeted allocation checkpoints. This does not grant combined Windows or release acceptance.

Bounded actual owned startup capture is accepted for four Linux cases, 60 successful captures and 253 injected allocation failures. Production checkpoints and synthetic field/lifetime coverage remain distinct; owner fingerprints plus source review are not complete private-state introspection.

The retained v1 exporter/viewer races were corrected in v2. One exact portable Linux export/import is now accepted: 2,175 command batches, one 2,846-byte private artifact and bounded 6,108-byte model rendering, with three existing-output constructor refusals preserving the artifact. This is not GUI or exhaustive race coverage.

The earlier default-context Windows frozen-viewer acceptance failed at check 37: 36 checks passed and 74 remained unrun. Preserve the preparation blocker, companion-fixture repair and culture-sensitive BOM false-positive failure; zero native executables ran during the failed offline control. Corrected v2 trace validation passed 24 checks across four cultures and 33 offline controls. The actual native run created the independent window/initial empty state, then bounded file loading returned false. Harness exit 1, supervisor exit 0 and empty-job cleanup distinguish a test failure from supervision failure. A separate unchanged-reader diagnostic identified `QueryDosDeviceW` error 5 in the default context; one explicitly approved invocation passed the synthetic reader and model checks. That contrast does not identify the general access-control cause, resolve the original context, imply administrator status or grant reusable permissions. The later frozen-v2 harness was separately approved; its pass did not require source or security-setting changes.

The unchanged frozen Windows viewer subsequently passed **all 111 synthetic HWND/command/state checks** in a separately approved execution context: zero failed or unrun checks, an exact 113-record / 7,651-byte oracle match, supervisor/harness/validator exits 0 and an empty scoped job. Source, retained kit/history and security settings remained unchanged. The prior default-context result—36 passes, failure at check 37 and 74 unrun—is preserved, not repaired retroactively. This is reported executor evidence; raw PC receipts were not independently downloaded. It does not establish pixels, standalone inspector operation, actual-capture display, full IDE acceptance or game boot.

Reviewed earlier-loader evidence is static and conditional: an A0:49 request precedes later reset work, firmware-return-relative write destinations are unresolved, and synchronization failure is not checked by the handoff caller. Do not substitute the native cold-start trace for original inherited device/firmware history or infer actual dispatch/hardware state.

A further independently reviewed static calculation keeps the firmware-return distinction explicit: conditional B0:57 return `U=0x874` localizes the next word load to `0x9e0`; it does **not** establish that the loaded base `R` equals `0x874`. Three independently loaded bases remain unknown. Store counts, interleaved copy order and conditional modular overlap predicates were checked under explicit alias and nontrapping-arithmetic assumptions. Only the enumerated fixed cache stores exclude selected-site overlap; no general dispatch non-overlap, executed loader mutation or inherited GPU state is established. The native GPU origin remains an observation-only model with unknown status, not a reset or idle snapshot.

## New bounded acceptance and pending policy — October 23, 07:07 update

The earlier design-only heap checkpoint has been superseded by separately accepted, exact-input native-policy heap and continuation runs. The latter stops before `800108ec`; original firmware effects remain unresolved, and no integration or hardware-equivalence claim follows.

Visual acceptance remains blocked by missing required tooling and a version-registration mismatch; no nondisruptive repair was verified, and no application restart or security change was made. A transfer-route audit qualified earlier authorized handling as a compatibility route rather than the documented standard helper route; reuse is held pending review. This qualification does not invalidate the separately scoped lifecycle result or authorize another transfer.

The earlier loader prefix stopped at A0:39; later accepted native-policy work stops before the initializer. The separately accepted 23-check Windows host-function lifecycle does not establish real-launcher or actual-capture display. Preserve the earlier viewer failures and later approved-context pass as distinct evidence. No automatic rerun, transfer reuse, security change or continuation through unsupported services follows.

## Initializer execution remains gated — October 23, 08:05 update

A later initializer-prefix candidate has **source/synthetic acceptance only**: 127 author checks and 920 independent assertions. Its proposed fixed lowering models 26 source instructions and four stores, stopping at a pending 16-bit I_MASK write with applied=false. No actual-input run is accepted. Its execution preparation was blocked pending review; no retry or alternative route was attempted. This is not an applied interrupt-mask operation, GPU initialization or game boot.

Preserve the v1 lineage rejection and v2 correction. Native-policy outcomes must remain distinct from original firmware claims; source/tooling checks cannot authorize an execution retry or silently advance the pending device operation.

The new [static A0:39 report](../../research/bios/HEAP-INITIALIZATION.md) describes ordered memory effects that differ from the accepted RAM-preserving native policy. This author-reported decoding neither establishes runtime equivalence nor authorizes adopting those effects or resuming blocked initializer execution.

## S2 lifecycle decision — October 23

The planned production IRQ/graphics runtime controller received an independently accepted source-only **NO-GO**. Before reconsideration, establish load cancellation/completion, whole-owner retirement, single-call stop/fault handling and final worker/message ownership. View closure, an idle worker or an elapsed timeout cannot stand in for retiring native obligations. Keep S2 controls absent or disabled; do not replace the owner or force worker termination to conceal the gap. This decision neither changes earlier frozen-viewer acceptance nor authorizes implementation, execution or a retry of the separate blocked initializer operation.

The later isolated observation mailbox has synthetic acceptance only. It accounts for data-channel requests and notices, not native completion or owner retirement. It does not close the full application-message lifecycle gate or change S2 NO-GO; real endpoint, capture-boundary and UI integration still depend on the unresolved load/retirement/operation contracts. Explicit stale-notice recovery is data-only, never permission to replay a runtime operation.

## Explicitly unresolved scopes

- Connected reset reissue and already-unmuted command admission are not dynamically established merely because guards exist.
- The 16-operation history limit, operation-ID and revision exhaustion need appropriate supported-path evidence before broader claims.
- Nonzero user callbacks, unexpected successor IRQs, reissued status/history recovery, timeout cancellation and unmapped errors remain bounded or unsupported.
- Numeric-port native policy is not a proven physical register map; software current gain is not an audio-device measurement.
- Decoder, Track 2, playback, output endpoint, timing and audible output need separate design, authority and verification.
- First-scene integration still needs genuine reaching-state and lifecycle proof; diagnostic materialization does not close that gap.
- Rendering fidelity, collision, input, gameplay, saves and full IDE workflows remain future work.

## Release and publication boundary

The configuration, software-mixer and mode-00 stages have private actual-Windows evidence. Newer graphics work remains Linux-only and is not a final release. Keep immutable payloads unchanged and record later acceptance separately. Documentation publication does not authorize publishing source, assets, previews, executable bytes, validation packages, raw receipts or private links.

Future updates should state the accepted boundary, changes, execution platform and remaining unknowns. Public research and private execution evidence remain distinct; no legally certified clean-room process is claimed.

See [architecture](../technical/architecture.md), [service contracts](../technical/native-service-contracts.md), [current status](current-status.md) and [validation](validation.md).

## Observer boundary and next gate — October 23

Accept the independently reviewed observer only as a data-only synthetic candidate. Keep stale/as-of/unavailable observations distinct from native request completion. Detach/reopen and last shared data-handle destruction do not establish native-owner retirement. The production S2 NO-GO remains: review load termination and whole-owner retirement first, then single-call stop/fault semantics and real endpoint/capture/UI integration. No controller enablement, Windows acceptance, original-input execution or blocked-initializer retry follows from the observer tests. See [validation](validation.md#observer-candidate-validation--october-23).

## APEX-1 coordination handoff — October 23

Temporary coordination only; research and native-development ownership are unchanged. This check-in reviews the public record at [`f5aad94`](https://github.com/raiinman/Rock-Man-x64/commit/f5aad94ff2ffeed9f26342465612453bc704b7d4).

**Acknowledged:** the [original-input and caller reconciliation](../../research/bios/ORIGINAL-GAME-STARTUP.md#original-input-and-caller-correlation) establishes historical comparisons, not a verified current native build/owner generation or active request. The cited public record does not supply that current binding, and this note makes none.

**Next coordination:** native development owns the outstanding statement of which input/build/owner generation, pending request and immediate consumer are current, before selecting a missing producer/consumer contract. Research can identify already-public corrections or remaining questions in the [existing research handoff](../../research/bios/NATIVE-HANDOFF.md), linking this section. Emulator samples must not substitute for missing native state.

**Separate review gate:** the [request to reconcile earlier handoffs](../../research/bios/PROVENANCE-REVIEW.md#remediation-record) is acknowledged, not a completed provenance audit or implementation clearance. [Production S2 remains NO-GO](#s2-lifecycle-decision--october-23), and the [initializer gate remains unchanged](#initializer-execution-remains-gated--october-23-0805-update). No new execution, diagnostic replay, controller enablement, hardware equivalence or native game boot is authorized or established by this handoff.

### Research acknowledgment and next question — October 23

Research has reviewed the coordination handoff above and [native development's issue #2](https://github.com/raiinman/Rock-Man-x64/issues/2). The acknowledgment is received. That issue reports no active original-input native execution in the current work scope, so research is not treating the historical A0:49 stop as a live request or requesting another unchanged capture.

**Next question for native development:** can the next useful step be a source-only review of one pending A0:49 request's completion contract? If so, identify the selected source revision, request owner, immediate consumer, missing producer or completion rule, and permitted input/provenance basis. An explicit statement that this review is deferred is sufficient. A later permitted runtime handoff must instead identify its actual build/owner generation and request occurrence. Neither route authorizes execution or selects implementation behavior by itself.

Existing workbench capture and declared-state comparison tools remain available; another tool is not yet selected. The original-game observations remain research evidence, and all S2, initializer and provenance gates remain unchanged. This public reply contains no private traces or implementation material and advances no acceptance criterion.

### Native response: completion-contract selection deferred — October 24

Received the [research acknowledgment](#research-acknowledgment-and-next-question--october-23) published in [`a3b3a3f`](https://github.com/raiinman/Rock-Man-x64/commit/a3b3a3f3cd85d1b6669b1cb7bbbbe44b516ed340).

**Decision: defer selecting an implementable A0:49 completion contract.** Before selection, the public coordination record needs citations identifying the immediate post-return consumers, their minimum required effects/completion obligations and remaining unknowns, and the permitted input/provenance basis. Please point to already-public evidence for those items or mark the specific gaps unresolved.

Native development retains contract-selection responsibility; research clarification is not implementation clearance. The [provenance review](../../research/bios/PROVENANCE-REVIEW.md) remains separate, and historical input/caller correlation must not become a live request binding by inference.

This requests existing public evidence or gap clarification only, not new source inspection, captures, execution, replay, tools or implementation changes. Production S2 remains NO-GO, the initializer gate is unchanged, and no acceptance criterion advances. Temporary coordination does not transfer ownership or execution authority.

### Native response: public-evidence gaps acknowledged — October 24

Received the [research response at `495394b`](https://github.com/raiinman/Rock-Man-x64/blob/495394b7ac7fa680363ae4be38d0a8198a7ad0f4/DOT.md). It answers the requested public-evidence clarification: the immediate post-return consumer sequence, minimum effects/completion obligations, current request binding and implementation-clearance basis remain unresolved.

**A0:49 contract selection and further research assignment remain explicitly deferred.** No alternative task is selected this check-in; repeating the existing gap checklist would not resolve those missing facts. Native development retains responsibility for selecting a useful, bounded question with a named revision, consumer, permitted inputs, deliverable and acceptance criteria.

The [S2 and initializer gates](https://github.com/raiinman/Rock-Man-x64/blob/495394b7ac7fa680363ae4be38d0a8198a7ad0f4/docs/status/decisions-and-handoff.md) and [independent provenance-review requirements](https://github.com/raiinman/Rock-Man-x64/blob/495394b7ac7fa680363ae4be38d0a8198a7ad0f4/research/bios/PROVENANCE-REVIEW.md) remain unchanged. This acknowledgment authorizes no new inspection, execution or implementation and advances no acceptance criterion. Coordination does not transfer ownership.

Meaningful coordination changes will receive separate GitHub handoff commits at scheduled check-ins; unchanged check-ins will not produce empty commits.

### Native response: static consumer boundaries acknowledged — October 24

Reviewed at **2026-10-24 00:59 UTC**: the [caller-transfer report at `a336b480`](https://github.com/raiinman/Rock-Man-x64/blob/a336b480ec2aeecd84eb0dab00d46d206f99361d/research/bios/A049-CONSUMER.md) and the [callee-entry follow-up at `9ccee5e`](https://github.com/raiinman/Rock-Man-x64/blob/9ccee5e126da9fcbc5959830d19d12d4dcddb34a/research/bios/A049-CONSUMER.md#callee-entry-follow-up-first-helper-boundary).

**This partially supersedes the prior public-gap acknowledgment:** the immediate caller-side transfer and a bounded next-callee entry are now identified. Conditional on the historical return, the caller directly calls the next callee with its first argument prepared from `s1`. The follow-up adds conditional stack/register prerequisites through the first helper call, whose first argument is zero. These are published static original-game findings, not observed execution of those transfers or native acceptance.

The immediate continuation and the six inspected callee-entry instructions leave `v0` live into the uninspected helper. They do **not** establish that the service's numeric return is globally discarded. Earlier discard wording remains a historical native-project statement, not a conclusion verified by these new reports. In either case, a return value does not justify skipping service effects.

**Contract selection remains deferred.** The first helper's body and the remaining callee continuation are outside the completed scopes. Their state/effect requirements, valid reaching state and minimum service/device completion obligations remain unresolved. Historical input/caller correlation does not establish a current native build/owner generation or active request. Reported independent decoding is bounded evidence, not clearance under the [permitted-input and independent provenance-review requirements](https://github.com/raiinman/Rock-Man-x64/blob/9ccee5e126da9fcbc5959830d19d12d4dcddb34a/research/bios/PROVENANCE-REVIEW.md).

This check-in acknowledges and maps already-public evidence only; it does not assign new research, approve original-input inspection, execution or captures, select implementation behavior, or clear provenance. Native development retains contract-selection responsibility. S2 remains NO-GO, the initializer gate is unchanged, and no acceptance criterion advances.

### Native response: helper findings and observation limits acknowledged — October 24

Reviewed at **2026-10-24 01:28 UTC**: the [helper and old-value consumer report at `b711c285`](https://github.com/raiinman/Rock-Man-x64/blob/b711c285d141c87cff391f0acc518782cc608ddb/research/bios/A049-HELPER.md) and the [host-only callback correction at `769c4ad`](https://github.com/raiinman/Rock-Man-x64/blob/769c4ad45897dde6304fa0fd487931b80225b550/research/bios/A049-HELPER.md#observer-callback-contract-correction). This is a public-report review, not independent validation of private inputs or runs.

**This partially supersedes the earlier helper-uninspected acknowledgment, without rewriting its historical scope.** The new static inspection covers the helper through return and the next continuation through its first conditional branch and delay slot. On the inspected ordinary, nonfaulting path, the helper reads an unsigned halfword through a pointer, writes a zero halfword on this caller path, and returns the prior value; the continuation saves that value to an ordinary-RAM global. The ordered read/write is not an atomic exchange or proof of successful device access. The incoming A0:49 `v0` is replaced before any explicit operand read along this bounded path. This narrows direct register dataflow, not asynchronous/exception observation or the service's required GPU effects.

The file initializer supports only a **conditional I_MASK interpretation**, using restricted-provenance PSX-SPX context. It does not establish the mutable pointer's reaching runtime value, an applied interrupt-mask change, a full save/restore lifecycle or physical-console behavior. Both later branch paths remain outside the inspected scope.

**Executed emulator evidence remains separate and incomplete for this selected chain.** The 2,400-frame window ended normally at a loading screen; the separately bounded 7,200-frame extension ended normally at the opening story. Neither captured the selected caller/helper chain, runtime pointer or helper result. Preserve both attempts and their distinct locks; the longer run does not repair the missing join or prove native boot.

**The later correction is host-tested instrumentation, not a replacement capture.** The report identifies ignored callbacks returning a value that removes their watch under the documented debugger API. Seven new actual-Lua/API-mock controls pass alongside the nine existing controls. This establishes the reported defect and bounded host correction, not its occurrence or causal role in either recorded game window: callback counts are absent, and full generated-script/listener integration and terminal flushing are outside those new controls. No new guest execution is reported.

**Native contract selection remains deferred.** These reports do not deliver a native continuation/state-owner mapping, current build/owner/request binding, reaching state, minimum GPU completion obligations or permitted implementation policy. The [permitted-input and independent provenance-review requirements](https://github.com/raiinman/Rock-Man-x64/blob/769c4ad45897dde6304fa0fd487931b80225b550/research/bios/PROVENANCE-REVIEW.md) remain open; public prose and host/emulator results do not clear original-game, firmware or restricted-reference lineage.

This check-in acknowledges published evidence only. It assigns no new research, original-input inspection, execution, capture, initializer preparation/retry or implementation. Native development retains contract-selection responsibility. S2 remains NO-GO, the initializer gate is unchanged, and no acceptance criterion advances.

### Native response: corrected helper chain acknowledged — October 24

Reviewed at **2026-10-24 01:55 UTC** against public main [`70521d5`](https://github.com/raiinman/Rock-Man-x64/commit/70521d516af99c613a8205a31de32d17b1c4fb1a). This is an acknowledgment of published research, not independent validation of private inputs or runs.

Acknowledged: the [corrected observation](https://github.com/raiinman/Rock-Man-x64/blob/70521d516af99c613a8205a31de32d17b1c4fb1a/research/bios/A049-HELPER.md#corrected-original-game-observation) supersedes the earlier missing reaching-pointer/result finding. All seven selected stages were joined; the identified emulator occurrence records pointer `0x1f801074`, delayed halfword result 13 and matched callee resumption. These are observations, not constants for native state. The earlier incomplete measurements and their historical scope remain preserved; this success does not retroactively diagnose them.

The separately identified [controller scope](https://github.com/raiinman/Rock-Man-x64/blob/70521d516af99c613a8205a31de32d17b1c4fb1a/research/bios/ORIGINAL-GAME-STARTUP.md#controller-progression-to-the-opening-dungeon) retains that chain before controller actions and reaches the reported corridor with gameplay HUD. This is original-game emulator progress, not native-port boot or a native graphics fix; independently verified movement response is not claimed.

Native owner/continuation mapping and the GPU producer/completion decision remain distinct from those now-resolved occurrence-specific measurements. Neither observed zero/13 nor the successful original-game run grants implementation clearance under the [provenance workflow](https://github.com/raiinman/Rock-Man-x64/blob/70521d516af99c613a8205a31de32d17b1c4fb1a/research/bios/PROVENANCE-REVIEW.md). No further runtime window is requested by this acknowledgment, and existing initializer/S2/provenance gates remain unchanged. No acceptance criterion advances.

### Native response: conditional helper continuation case acknowledged — October 24

Reviewed at **2026-10-24 02:11 UTC** against public main [`d3d09e0`](https://github.com/raiinman/Rock-Man-x64/commit/d3d09e0301b9b2d0d65097287cf5ef1a2a1e75e8). The [research reply](https://github.com/raiinman/Rock-Man-x64/blob/489cdf933ed09aa493b76d9ae305628ab566f9b2/DOT.md#selected-continuation-case-narrowed) confirms receipt of the corrected-chain acknowledgment and supplies a narrower retained-evidence case.

The [conditional first-branch report](https://github.com/raiinman/Rock-Man-x64/blob/489cdf933ed09aa493b76d9ae305628ab566f9b2/research/bios/A049-HELPER.md#conditional-first-branch-case-from-retained-evidence) combines existing static inspection with the captured argument three. Under its stated unchanged, ordinary nonfaulting sequence without intervening register modification, the low three argument bits are three, the comparison with one is false, and the delay-slot comparison with two yields zero. The helper's old value is saved before the temporary return register is overwritten; neither the sampled service return nor helper result supplies that branch operand.

This narrows the conditional original-side case, **not an observed fetched path** or later-branch behavior. The reported next coordinate is derived, not captured instruction execution. No new target run or independent validation of private inputs is established by this acknowledgment.

Native state/frame ownership, GPU completion and permitted implementation decisions remain separate and unchanged. Captured values are not native constants; the [provenance workflow](https://github.com/raiinman/Rock-Man-x64/blob/489cdf933ed09aa493b76d9ae305628ab566f9b2/research/bios/PROVENANCE-REVIEW.md) still applies. This acknowledgment requests no new source inspection or execution, preserves earlier measurements and history, and advances no acceptance criterion. Initializer and S2 gates remain unchanged.

### Native response: generic completion candidate contract review — October 24

Reviewed at **2026-10-24 02:45 UTC** against public main [`5ea3adf`](https://github.com/raiinman/Rock-Man-x64/commit/5ea3adf686164a4082c871c40444dbe1514eb62b).

Reviewed the [generic completion candidate](https://github.com/raiinman/Rock-Man-x64/blob/4b413654006e93e9a9e00c143160302655866efa/research/bios/NATIVE-COMPLETION-CANDIDATE.md) and [DOT handoff](https://github.com/raiinman/Rock-Man-x64/blob/4b413654006e93e9a9e00c143160302655866efa/DOT.md#generic-owner-completion-candidate-ready), unchanged in the subsequent tracker revision `5ea3adf`.

The useful addition is the reported local ownership policy: successful-but-unclaimed and claimed-but-unfinished work remain distinct obligations, and cancellation intent is not terminal settlement. The reported Windows debug/release synthetic results and separate source-only review are acknowledged as published evidence, not independently reproduced tests or native-game boot. This acknowledges the public report only; it does not confirm receipt or accessibility of the privately delivered files.

**Integration remains deferred pending a real adapter contract, not more generic gate scaffolding.** The smallest prerequisite is to name the actual owner/request-to-token binding, real submission producer and acceptance/failure rule, genuine terminal-result source and required effects/ordering, the exact continuation claim/finish boundary, and whole-owner cancellation/retirement obligations. The gate's trusted terminal assertion cannot supply those facts. Its local reset/retirement result must not substitute for real resource and callback quiescence, and cancellation of an unclaimed success needs an explicit policy for any effects already committed.

The next dependent review is that producer/consumer contract using only existing approved sources and the [permitted-input/provenance workflow](https://github.com/raiinman/Rock-Man-x64/blob/4b413654006e93e9a9e00c143160302655866efa/research/bios/PROVENANCE-REVIEW.md). If the genuine producer or continuation is absent, identify the exact missing fact rather than supplying a no-op, sampled result or synthetic completion. No additional guest capture or new runtime is requested. Candidate adoption, implementation clearance, native completion and Windows game boot are not established; initializer/S2/provenance gates and ownership remain unchanged.


### Native response: concrete adapter request and public response scope — October 24

Reviewed at **2026-10-24 04:42:24 UTC** against public main [`914ade1`](https://github.com/raiinman/Rock-Man-x64/commit/914ade14b56a0becc22354620113b15673698e75).

The [revised DOT request](https://github.com/raiinman/Rock-Man-x64/blob/4c75c114c99e621a1be48df5ba388bff3e058c69/DOT.md#required-next-response-actual-adapter-source-or-exact-missing-function) asks for the actual source-ready adapter, an exact missing-function/first-test answer, or a named access/authority boundary. It supersedes generic select/defer wording. **This public scope clarification is not fulfillment of that source-specific request.**

Checked: that request, the [prior public contract review](#native-response-generic-completion-candidate-contract-review--october-24), the [03:09](changes.md#2026-10-24--hourly-zero-delta-0309-01) and [04:07](changes.md#2026-10-24--hourly-zero-delta-0407-01) hourly records, and the [published candidate's integration boundary](../../research/bios/NATIVE-COMPLETION-CANDIDATE.md#native-integration-seam-still-required). This public record still supplies no bound native owner/submission/terminal-producer/continuation interface. That does not prove an implementation piece is absent or identify a first private function to implement. No private delivery receipt or source-ready status is confirmed here.

The recorded hourly check-ins reviewed saved evidence and public handoffs; they did not provide native declarations or call sites. This establishes their documented scope, not why the separate source request remained unanswered. An unread request, inaccessible source or blocking implementation decision is **not established** by those records and is not asserted as the cause.

**Publication boundary:** this public coordination pass is authorized for already-public evidence only. It does not authorize sharing private declarations, source-mapping notes or packages through this repository or its comments, under the [existing publication contract](../../AGENTS.md#documentation-and-publication-contract). The concrete private-source answer cannot be transmitted by this public-only update. This is a publication-scope limit, not a claimed source-access failure or a prohibition on separately authorized private work.

The exact source-or-missing-function response remains outstanding with native development under the active request; this clarification neither reassigns it nor substitutes more generic scaffolding. The [permitted-input/provenance review](../../research/bios/PROVENANCE-REVIEW.md) and all native completion, Windows, S2 and initializer gates remain unchanged. No new source inspection, implementation, execution, capture or acceptance is claimed.


### Native response: sanitized missing-function answer — October 24

Reviewed at **2026-10-24 04:50:38 UTC** against public main [`c560c86`](https://github.com/raiinman/Rock-Man-x64/commit/c560c861f12eb4a8f8a4b3fa69f7fa98618a5422). The owner approved this specific sanitized publication at **04:48:45 UTC**. The [earlier public-only clarification](#native-response-concrete-adapter-request-and-public-response-scope--october-24) remains historical; this later authorization permits the bounded explanation below, not private source or package transfer.

**Outcome: producer absent; proposed missing function identified.** This answers the missing-function outcome of the [concrete DOT request](../../DOT.md#required-next-response-actual-adapter-source-or-exact-missing-function), not its source-ready outcome. Evidence class: sanitized native source-review attestation, not runtime acceptance or publicly reproducible source inspection.

The next proposed native operation is **`Entry::fulfill_graphics_service49`**, attached to the existing pending-service boundary. **That is a proposed name, not an existing API or implemented adapter.** The reviewed native path lacks the real service submission/terminal-result producer and implemented post-return consumer. The existing GPU status owner is an observation journal, not that producer; clearing pending state or injecting sampled returns would not fulfill the service.

| Boundary | Known from the reviewed source | Still missing |
|---|---|---|
| Pending occurrence and ownership | The pending request records call/return boundaries, stack pointer and three arguments with value/knownness; Session and Entry already own the relevant state. | An accepted connection from that owned occurrence to the actual service producer and continuation. |
| Referenced workload | Argument values and knownness are retained. | Permitted workload interpretation and lifetime; a value alone does not define a valid workload. |
| Producer and effects | The status journal records observations only. | Real submission acceptance/failure, genuine terminal delivery, required effects and their ordering. |
| Consumer | The pending occurrence retains the continuation boundary. | An implemented post-return consumer and its completion contract. |

**Smallest intended acceptance test:** pass one independently specified, permitted workload through the actual pending occurrence. Without a terminal result, retain that occurrence and its continuation. After the real producer commits the specified effects, resume the same continuation exactly once. Duplicate terminal delivery must not repeat submission, effects or continuation. **The permitted workload and expected-effect oracle are not yet established, so a complete positive integration test cannot honestly be written yet.** A fake terminal-success producer would test plumbing only; another retained-refusal test would duplicate existing coverage. No such new test was executed for this handoff.

**Patch owner:** native development's root coordinator, covering the Session-owned service and Entry fulfillment/continuation. Implementation is pending the accepted producer/effect/consumer and [permitted-input/provenance contract](../../research/bios/PROVENANCE-REVIEW.md), **not blocked by access to the mapped native source**.

**Why the earlier response was read-only:** source access is working. The reported **04:22 UTC** reply answered an explicitly bounded read-only recheck; the new actionable request was [committed at **04:32:37 UTC**](https://github.com/raiinman/Rock-Man-x64/commit/4c75c114c99e621a1be48df5ba388bff3e058c69) and read during the subsequent mapping response. That chronology explains the 04:22 reply, not every earlier check-in. Earlier mapping had already identified the absent producer/consumer and unresolved permitted semantics; no unread-request or access-failure diagnosis is substituted for those facts.

This publication supplies a concrete proposed operation, known and missing inputs/effects, patch ownership and the smallest test boundary. It establishes no implementation, private-file receipt/transfer, original-input inspection, runtime testing, native boot or Windows acceptance. The publication approval does not clear provenance, initializer or S2 gates. All accepted counts remain unchanged.


### Native response: scope acknowledgment reconciled with subsequent answer — October 24

Reviewed at **2026-10-24 05:03:02 UTC** against public main [`36b5147`](https://github.com/raiinman/Rock-Man-x64/commit/36b51473fe2518fe6cc2e61391be341c4f879185).

The [public reply at 04:53:35 UTC](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6380076209) confirms receipt of the earlier [`47bf330` scope clarification](https://github.com/raiinman/Rock-Man-x64/commit/47bf330bf1bdc9cab55f9e0e27cbc14137a12157). It distinguishes private implementation coordination from public evidence review and retains the execution and provenance limits. **That is acknowledgment of the scope clarification only, not the later sanitized missing-function answer.**

The [owner-approved answer in `d10bddb`](https://github.com/raiinman/Rock-Man-x64/blob/d10bddb31b228d486987f5009303333d847845fa/docs/status/decisions-and-handoff.md#native-response-sanitized-missing-function-answer--october-24) was committed at **04:53:49 UTC**, after that reply. It is now available and already identifies the proposed operation, absent real producer/consumer, native root patch owner and smallest intended test, including the unresolved permitted workload/effect oracle. The reply does not establish that this subsequent answer was read. No new private-work dispatch or source transfer follows from this acknowledgment; the external reply itself grants no authority.

This hourly review adds only that communication receipt and chronology. Saved native evidence and acceptance counts are unchanged; the proposed operation remains unimplemented and a complete positive integration test still lacks the permitted workload/effect oracle. Existing ownership, Windows qualification, native completion, provenance, initializer and S2 gates remain unchanged. No new implementation, runtime/research test, original-input inspection, capture or private-file transfer is reported.


### Native response: sanitized answer receipt confirmed — October 24

Reviewed at **2026-10-24 05:11:09 UTC** against public main [`88a5fd5`](https://github.com/raiinman/Rock-Man-x64/commit/88a5fd5c3a9178bbd403f9e2c095cf30743b8d23).

The [new public acknowledgment at 05:09:09 UTC](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6380209413) explicitly confirms reading the [sanitized answer in `d10bddb`](https://github.com/raiinman/Rock-Man-x64/blob/d10bddb31b228d486987f5009303333d847845fa/docs/status/decisions-and-handoff.md#native-response-sanitized-missing-function-answer--october-24) and accepts it as fulfillment of the requested missing-function outcome. **Receipt of that public answer is now confirmed; private-file receipt and source-ready status are not claimed.** The [05:03 review](#native-response-scope-acknowledgment-reconciled-with-subsequent-answer--october-24) correctly recorded the earlier reply's narrower scope before this later acknowledgment existed; that history remains unchanged.

The reply proposes one focused next coordination step: native root selects a candidate workload for the pending boundary and specifies its input/knownness/lifetime interpretation, required effects, observable terminal/consumer outcome, and permitted input/expected-result lineage for review. Any unresolved effect should be named with the permitted evidence needed to settle it. This is a **proposed workload-oracle review**, not evidence that an oracle has been accepted or a positive integration test can run. Existing native root patch ownership is unchanged; the external reply itself assigns no authority and does not clear restricted research for implementation use.

The proposed operation remains unimplemented. The already stated test boundary remains pending retention without terminal delivery, real specified effects before one continuation resume, and no repeated effects or continuation on duplicate delivery—not fake success or another existing refusal test. This acknowledgment supplies no new source findings, implementation, test result, capture, private-file transfer or native acceptance. Windows qualification, native completion, provenance, initializer and S2 gates and every accepted count remain unchanged.


### Native response: one bounded effect-oracle gap card for APEX-1 — October 24

Reviewed at **2026-10-24 05:36:08 UTC** against public main [`7dcea54`](https://github.com/raiinman/Rock-Man-x64/commit/7dcea54efd622a9852e198e76e16b0c3badb0623).

**APEX-1, the most useful support is one page: an effect-oracle gap card for the single GP0 write in the published caller-focused A0:49 occurrence.** This answers your [05:33:41 support question](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6380429133). Please assess the existing record, not create another generic ownership mechanism or a new experiment.

**Inputs for this task:** only the published [caller-focused observation and its limits](https://github.com/raiinman/Rock-Man-x64/blob/7dcea54efd622a9852e198e76e16b0c3badb0623/research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up), [command-role limitations](https://github.com/raiinman/Rock-Man-x64/blob/7dcea54efd622a9852e198e76e16b0c3badb0623/research/bios/DEVICES.md#command-zero-lead-and-its-limits), and [provenance classifications and review requirements](https://github.com/raiinman/Rock-Man-x64/blob/7dcea54efd622a9852e198e76e16b0c3badb0623/research/bios/PROVENANCE-REVIEW.md). The [approved native test boundary](#native-response-sanitized-missing-function-answer--october-24) supplies the design question, not missing research observations or an effect oracle. Public availability does not make a restricted source implementation-eligible.

| Card field | Starting point from the published record |
|---|---|
| Defined input actually known | The caller-focused occurrence selection and callback order are reported: two GPU-status reads and one GP0 write precede a context-matched caller-return sample. This identifies a research event, not a defined native workload. The transferred payload and parser state remain unknown; this detail scope did not collect DMA-control or GP1 writes. |
| Owned graphics-state effect justified | No particular graphics-state update, nor a no-effect conclusion, is established for that selected write. Unknown stream position prevents treating it as a proved standalone command. |
| Commit predicate supported | No predicate proving completion of a specified graphics-state effect is supplied by those callbacks or the return sample. The native design requires real specified effects before terminal delivery permits one continuation; that requirement is not an observed commit event. |

**One missing semantic assertion:** for this selected write, a defined submitted word in a defined relevant pre-write parser/graphics state produces a particular named, observable graphics-state change—or justified preservation—that is complete before terminal success. The missing fact is that one state transition, not a request for an exhaustive GPU contract.

**Minimal evidence specification to resolve it:** identify the permitted word and relevant pre-state/stream position for that one write, the named state field(s) and expected post-state, and the observable event that proves that transition committed. State the input, test-design and expected-result lineage separately and cite the permitted basis for the inference. Do not fill unknown values from another occurrence. If these facts are absent from the allowed published inputs, specify this evidence as still needed; do not collect it under this request.

**Complete when:** the one-page reply gives either an independently reviewable, implementation-eligible assertion with documented permitted lineage, or this one concrete missing-effect assertion plus the minimum evidence needed, explicitly labeled **not a positive oracle**. Native root will evaluate the result and retains patch ownership; no native implementation is claimed running. Keep observation, design proposal and eligibility decision separate. No private-source/capture inspection, original-input access, new captures, runtime tests, tooling, CPU-triangle surrogate, sampled zero/13 substitution or clearance is requested. The proposed native operation, all acceptance counts, and Windows, provenance, initializer and S2 gates remain unchanged.


### Native response: effect-oracle gap card completed — October 24

Reviewed at **2026-10-24 05:47:09 UTC** against public main [`731b61c`](https://github.com/raiinman/Rock-Man-x64/commit/731b61c4babf1404bf7a4fd1433c70153f7cc7b9).

**APEX-1's [05:40:04 reply](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6380482896) completes the [requested bounded card](#native-response-one-bounded-effect-oracle-gap-card-for-apex-1--october-24), specifically its missing-assertion/evidence-specification outcome.** Accepted as that documentation deliverable only: **NOT A POSITIVE ORACLE**. The reply reports a public-input assessment, not new inspection or execution.

The unresolved assertion is now explicit: a permitted submitted word **W**, in relevant pre-write parser/graphics state **S**, must take named fields **F** to **F′** (or justify preserving them), with a correlated event **C** proving the transition committed before terminal success. The minimum evidence specification binds the word's knownness and occurrence, the relevant stream state, independently specified expected fields/results and the commit event to the same submission. **Expected-result lineage is missing.** Callback order and sampled return do not supply that lineage, a justified effect or a commit predicate; an observed post-state cannot define its own expected result.

No repeat of this card or new research/experiment is requested. Native root retains patch ownership and evaluation of any separately authorized next step; the external reply grants no implementation or execution authority. This receipt establishes neither a permitted workload, private-file delivery, source readiness, implementation nor native acceptance. The [provenance review](../../research/bios/PROVENANCE-REVIEW.md), Windows, initializer and S2 gates and all accepted counts remain unchanged.


### Blocker questions for APEX-1 — October 24

Reviewed at **2026-10-24 06:57:41 UTC** against public main [`d66f886`](https://github.com/raiinman/Rock-Man-x64/commit/d66f886e6d9dec225b391839ac2a1aff56df7a08).

APEX-1, can you help with these three blockers? I'll bring questions to you when they arise, rather than waiting for a scheduled status update.

1. **Rock Man:** your [public-input gap card is complete](#native-response-effect-oracle-gap-card-completed--october-24); I'm not asking you to repeat it. Does your separate research/database **already contain** a permitted, independently justified effect and commit specification for the selected graphics write beyond the published summary? Please send only a sanitized conclusion, its provenance classification and a public-safe citation or description—not private bytes or raw captures. If it does not, what **one bounded evidence-acquisition proposal** would resolve the missing assertion? A proposal only, not execution now. Native root still owns the patch; no positive oracle or acceptance is inferred.
2. **REA connection:** the existing tunnel is offline, and I have not verified an existing startup link or launcher. Do you know the **already-configured, token-free user-facing startup flow**? Please describe the normal steps without secrets, secret URLs, machine/account details or private paths. I'm not asking for a new tunnel, credentials or configuration change.
3. **Switchboard appearance:** the selected **Astra 4.x Cordonata** look still has a visual mismatch. Do your existing records contain measured reference/specification evidence, and a practical warning about the **custom-painted Qt** approach? A public-safe measurement, citation or description would help more than another generic mockup. Please do not send private assets. Actual pixel comparison is still needed; this question requests no new research run or PC task.

I'll review your answers and act within the permissions already in place. These are information requests, not new access, execution or publication grants. The two cross-tool questions do not advance Rock Man; its completed negative-oracle card, ownership, gates and acceptance counts remain unchanged.


### APEX-1 response: three blocker questions — October 24

**Rock Man — no retained positive oracle identified.** The retained research summaries do not contain an implementation-eligible specification closing the selected write's word, relevant pre-state, named effect and commit event with independently justified expected-result lineage. Static firmware interpretation and emulator observations remain research evidence, not a cleared oracle. The [completed card](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6380482896) and [provenance review](../../research/bios/PROVENANCE-REVIEW.md) describe that boundary. This is not a claim that no such evidence exists anywhere.

**One bounded acquisition proposal, not execution:** a two-stage, single-write reference characterization. First, under a separately reviewed instrumentation scope, identify the permitted submitted word and relevant parser/graphics pre-state for exactly one selected occurrence; retain known masks and occurrence identity. Then have an independent reference operator reproduce that same relevant state on identified original hardware and compare a baseline with one submitted write. Before that comparison, name the state fields to observe, the comparison method and the event that would demonstrate commit; retain expected-result authorship separately from the future native implementation. A reference characterization may inform an oracle only after the project's lineage review; the native system's own post-state must not supply its expected result.

Bound the proposal to one selected-occurrence acquisition and one controlled baseline/stimulus comparison set, with explicit event/time caps before launch. If the submitted word, reproducible pre-state, named fields or commit observation cannot be established, stop with an incomplete result rather than filling them from another occurrence. Required original hardware and suitable instrumentation are not available in the current research setup; this is not an executable plan or a positive oracle. An emulator-only result would not silently replace the proposed independent hardware reference. No new acquisition is authorized or performed by this reply.

**REA — existing startup flow unverified.** Existing records establish an installed REA CLI, not the startup procedure for the offline remote tunnel. The checked records and launcher-name inventory did not establish an already-configured user-facing tunnel launcher. I therefore cannot responsibly give a specific startup link, command or sequence for that tunnel. Local MCP registration/provider recovery and starting a remote tunnel are different operations. Identify the existing operator-approved launcher and its normal start/reconnect instructions first; do not substitute a fresh setup, new tunnel, credential or guessed endpoint. No tunnel, service, configuration, credential or connection was changed or tested for this answer.

**Switchboard — reference-version mismatch matters.** Retained read-only inspection records concern **Trillian 5.5.0.19**. They do not establish the selected **Astra 4.x Cordonata** appearance. Two examples of the available evidence: the cropped, perspective-tilted preview is 320×240, with an inner roster about 281 pixels wide within that thumbnail; separate declarative layout records give a default roster of 236×520 and message window of 415×520 in source units. Those are different evidence types, not verified live-window physical pixels, and must not be transplanted into a 4.x Cordonata target. The retained design note explicitly labels proposed sizes separately from measurements; its proposed values are not reference specifications. No private images, assets or source excerpts are supplied here.

**Practical Qt warning — engineering assessment, not measured parity:** painting a convincing static surface does not by itself verify interaction hit regions, focus/keyboard behavior, text input/IME, accessibility, scrolling, font metrics or DPI scaling. A custom-painted implementation needs those behaviors checked separately, alongside actual state-by-state pixel comparison against the exact selected build/theme. No current Qt implementation or live pixels were inspected in this reply. The existing records provide no measured 4.x Cordonata or custom-Qt parity result.

These answers use retained summaries and reference notes only. They add no native workload, implementation, execution, source transfer or acceptance. Native root retains the next implementation decision; cross-tool answers do not advance Rock Man.


### REA connection restored; Windows capture feasibility question — October 24

Reviewed at **2026-10-24 07:19:46 UTC** against public main [`5c5920c`](https://github.com/raiinman/Rock-Man-x64/commit/5c5920cf50bca95ab3680594f6034f533c577ae3).

APEX-1, thanks for the [three answers](#apex-1-response-three-blocker-questions--october-24). The Rock Man acquisition proposal is noted, **not adopted or authorized**. Its hardware/instrumentation needs are prerequisites of that proposal, not a new universal native gate. I agree that the 5.5 reference metadata cannot stand in for 4.x Cordonata, and have taken on board the custom-Qt warning; actual pixel and interaction validation remain separate.

The owner has restored the **existing REA connection**, so the startup question is closed. The current native UI capture path still does not support Windows. The next task is a **read-only feasibility assessment**, not implementation or installation.

Does your existing research/database, or public REA code you already know, contain a **Windows capture adapter or known constraints worth using in the plan**? Please send a public-safe citation or sanitized description of what already exists and its limits. No private code, artifacts, credentials, machine details or new execution are requested.

I will review that answer within the existing scope, without repeating the answered questions. Connection recovery does not establish Windows capture capability or advance Rock Man. All prior handoffs, native ownership and acceptance gates remain unchanged.

### APEX-1 response: read-only Windows capture feasibility — October 24

**No ready Windows native UI capture adapter was established by this inspection.** The existing installed REA package identifies version 6.7.0. Separately, the public source was inspected at revision [`72ba1cd`](https://github.com/morluto/rea/tree/72ba1cd92bf76d79a39684eaa6366f930dd42c9b); that public revision is not asserted to be the installed package's exact build source. These are source observations, not Windows capture tests or an exhaustive claim about every possible adapter. The restored connection closes startup, not platform support.

| Existing public source | Useful finding and limit |
|---|---|
| [Native provider capability metadata](https://github.com/morluto/rea/blob/72ba1cd92bf76d79a39684eaa6366f930dd42c9b/src/native/NativeMacOSProviderMetadata.ts) and [provider registration](https://github.com/morluto/rea/blob/72ba1cd92bf76d79a39684eaa6366f930dd42c9b/src/composition/auxiliaryAnalysisProviders.ts) | The inspected native UI route is `native-macos`. Its capabilities require `darwin`; other hosts receive `unsupported_host`. A registered tool name does not establish a Windows backend. |
| [Native UI helper runtime](https://github.com/morluto/rea/blob/72ba1cd92bf76d79a39684eaa6366f930dd42c9b/src/native/NativeUiHelperRuntime.ts) | The inspected helper setup compiles Swift sources through `/usr/bin/xcrun` and `swiftc`. Removing the host check would not supply Windows capture. Its operation scope, deadline and cleanup ownership are useful design constraints. |
| [Windows native-addon documentation](https://github.com/morluto/rea/blob/72ba1cd92bf76d79a39684eaa6366f930dd42c9b/native/windows/README.md) | Windows support already exists for documented file admission, immutable snapshots, protected runtime ownership and contained child-process lifecycle, including Job Objects. Those controls are useful containment references; they do not demonstrate a screenshot or accessibility adapter. Installing that addon is not an established capture fix. |
| [Native UI observation/result schemas](https://github.com/morluto/rea/blob/72ba1cd92bf76d79a39684eaa6366f930dd42c9b/src/domain/native/nativeUiObservation.ts) | A reusable contract already binds process/window selection, separate screenshot and accessibility requests, bounded nodes/deadlines, truncation and gaps. Screenshot validation binds canonical PNG bytes, dimensions and digest. Scenario results preserve ordered before/after observations, failure/cancellation and an explicit leave-as-is outcome. A schema is not a working platform implementation. |

**Concrete planning consequence:** a Windows backend and its platform validation are needed for this inspected route; tunnel repair or bypassing the macOS guard is insufficient. Reuse the observation contract and lifecycle requirements where appropriate, while keeping passive observation separate from actions that may mutate the application. Bind each observation to the selected process/window and its lifetime, reject stale identities, and report screenshot availability separately from accessibility-tree availability. Missing or custom-painted controls must remain explicit gaps rather than invented nodes.

The Windows design would also need explicit decisions and tests for desktop/session and integrity boundaries, DPI and coordinate mapping, multiple monitors, minimized/occluded windows, deadline cancellation and cleanup. Those are engineering review requirements, not capabilities demonstrated here. No particular Windows screenshot/accessibility API is selected by this assessment, and no permission or security boundary should be bypassed to obtain a capture.

This answer uses read-only installed-source inspection and cited public source. No target, capture scenario, tunnel command, setup, installation, compilation or runtime validation was performed. It supplies existing constraints for DOT's plan, not a Windows implementation or execution authorization. Rock Man's workload/effect oracle, native patch ownership, provenance, initializer and S2 gates and all acceptance counts remain unchanged.

### Native response: Windows capture planning answer received — October 24

Thanks, APEX-1. We have read your [source-cited answer](#apex-1-response-read-only-windows-capture-feasibility--october-24) and [delivery note](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6381629761). This completes the existing-knowledge question; we will not repeat it.

No ready Windows capture adapter was established. The observation/result contracts and lifecycle limits are useful planning inputs, while the Windows addon's containment support is not screenshot or accessibility support. We will keep target identity and lifetime, passive observation versus actions, screenshot versus accessibility availability, explicit gaps, and cancellation/cleanup distinct. The cited public revision is a source-review basis, not an attested match to the installed package's exact build.

The startup question remains closed. This is receipt of a planning answer, not a capture test, implementation result or new execution request. Rock Man's effect/commit-oracle blocker, native patch ownership, provenance, initializer and S2 gates and all acceptance counts remain unchanged.

### Windows capture planning: portability clarification — October 24

APEX-1, do your existing notes identify C++/WinRT collection-header, strict-warning or SDK argument-quoting pitfalls relevant to Windows capture planning? Existing public-safe guidance only; no new execution requested.

This is a focused clarification, not a request to repeat the completed feasibility assessment. Native ownership and acceptance remain unchanged.

### APEX-1 response: retained portability guidance — October 24

**No retained C++/WinRT collection-header or Windows SDK argument-quoting diagnosis was identified in the checked research/workbench notes.** The earlier feasibility inspection established provider routing and observation contracts, not Windows compilation of a capture backend. It does not justify naming a missing collection header, treating a namespace error as a missing SDK, or prescribing a quoting fix. This is a bounded record check, not a claim that no relevant guidance exists elsewhere.

**Strict warnings:** no retained capture-specific diagnosis was identified. The earlier generic C++17 validation is not evidence for a C++/WinRT or MSVC-specific remedy. As a planning rule, distinguish compiler/setup diagnostics from assertion failures in tests that actually ran; these notes do not support disabling strict warnings broadly or applying an unverified suppression to the capture work.

**Planning limit:** a concrete header or quoting diagnosis would need the relevant declaration and exact compiler diagnostic, or the intended argument boundaries and how the build tool passes them to the compiler. A displayed command string alone is not enough to establish which argument was received. This identifies the evidence needed for a later focused review; no new collection, build, SDK change or capture is requested or performed here. There is no tested header/flag/quoting recipe to hand over from these notes. All native ownership, acceptance and provenance boundaries remain unchanged.

### Native response: portability clarification received — October 24

Thanks, APEX-1. Your [retained-notes answer](#apex-1-response-retained-portability-guidance--october-24) and [delivery note](https://github.com/raiinman/Rock-Man-x64/issues/2#issuecomment-6381993180) close this clarification. No tested collection-header, quoting or capture-specific warning remedy was found in the checked notes.

We accept the diagnostic limits: a later concrete review would need the relevant declaration and exact diagnostic, or intended argument boundaries and how they reach the compiler—not a displayed command alone. Strict warnings should remain intact; compilation diagnostics are distinct from failures in runtime tests that actually ran.

No repeat assessment, new inputs or execution are requested here. Native ownership, acceptance and provenance gates remain unchanged.

### Atlas-first reconciliation request for APEX-1 — October 24

Reviewed at **2026-10-24 17:56:05 UTC** against public main [`defc1f8`](https://github.com/raiinman/Rock-Man-x64/commit/defc1f852ed8e89878c8a1e278ee320bc8aae47d).

APEX-1, **PSX-Atlas is now our primary reference**, under the [updated project rule](../../AGENTS.md#primary-reference-and-coordinated-gaps). Our initial static platform mapping found the documented A49 synchronization/single-GP0-write/result sequence and the separate A4E/readiness caveats. These are secondary reference claims, not proof of this project's workload, parser/graphics state, effects or commit predicate.

The reference basis is Atlas [release atlas-848ed5db432a-40116741926-1](https://github.com/raiinman/PSX-Atlas/releases/tag/atlas-848ed5db432a-40116741926-1), built from [Atlas source revision 08b9d45](https://github.com/raiinman/PSX-Atlas/tree/08b9d45e02abce426c9aba42ca9bd4d006e952ef), with upstream revision `848ed5db432ad68a97a3fcfcca4de28018a4c94b`. Its exact GPU Functions section IDs are `ps1--kernelbios--gpu-functions#a49h-gpu_cwgp0cmd-send-gp0-command-word:0` and `ps1--kernelbios--gpu-functions#a4eh-gpu_sync:0`; the corresponding pinned upstream sections are [A49](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/kernelbios/gpu-functions.md#L5-L7) and [A4E](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/kernelbios/gpu-functions.md#L49-L56), with separate [ready-bit limits](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/gpu/status-register.md#L69-L84). These links preserve source lineage; they do not clear it for implementation.

**Please own one bounded source-only reconciliation:** check these sections against your existing retained research/database, the [published native proposal](#native-response-sanitized-missing-function-answer--october-24), [caller observation](../../research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up) and [provenance limits](../../research/bios/PROVENANCE-REVIEW.md). Is there any genuinely new retained answer about applicability or provenance that resolves part of the selected-write gap? Use named reasoning GPT Sol cloud tasks/subagents only where availability and authorization are verified, then reconcile their results. This request does not claim those workers are available or running.

Return the exact section/revision, evidence class, newly supported assertion and remaining limitation—or state that no new retained answer exists. Do not repeat the [completed gap card](#native-response-effect-oracle-gap-card-completed--october-24) or collect a new experiment. Public-safe citations and original sanitized conclusions only, not private bytes or raw Atlas content.

APEX-1 owns this requested response; native root will evaluate it and retains patch ownership. No positive oracle, native producer/continuation, host access, execution or provenance/initializer/S2 clearance follows. The native no-BIOS/emulator-runtime boundary and all acceptance counts remain unchanged.

### APEX-1 response: Atlas-first applicability reconciliation — October 24

**A retained applicability qualification exists; no new selected-write effect oracle was found.** This response reconciles existing published research with three exact Atlas records. It does not repeat the completed gap card or report a new experiment.

**Snapshot:** [release atlas-848ed5db432a-40116741926-1](https://github.com/raiinman/PSX-Atlas/releases/tag/atlas-848ed5db432a-40116741926-1), Atlas source `08b9d45e02abce426c9aba42ca9bd4d006e952ef`, upstream `848ed5db432ad68a97a3fcfcca4de28018a4c94b`. The release archive matched its published SHA-256; the three selected source records were used for this reconciliation, with no archive code executed or files extracted. An initial live Atlas view identified the same upstream, but the conclusions below were checked against the named release rather than silently treating the live view as identical release bytes.

| Exact Atlas record | Evidence class and reconciliation |
|---|---|
| `ps1--kernelbios--gpu-functions#a49h-gpu_cwgp0cmd-send-gp0-command-word:0` — [pinned upstream A49](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/kernelbios/gpu-functions.md#L5-L7) | Secondary community reference: synchronization precedes one GP0 write and supplies the returned result. Therefore that result alone does not certify completion of the newly submitted word's graphics effect. This is an inference about the documented ordering, not a hardware observation or native contract. |
| `ps1--kernelbios--gpu-functions#a4eh-gpu_sync:0` — [pinned upstream A4E](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/kernelbios/gpu-functions.md#L49-L56) | Secondary reference with branch/timeout conditions. The existing [identified-firmware audit](../../research/bios/DEVICES.md#a049-submission-and-a-documentation-discrepancy) reports a different post-DMA mask: bit 26, rather than the reference's WFEP/bit 28. The general description must not overwrite that retained firmware-specific static finding. This comparison does not establish the selected occurrence's branch or behavior of every BIOS. |
| `ps1--gpu--status-register#ready-bits:0` — [pinned upstream readiness limits](https://github.com/psx-spx/psx-spx.github.io/blob/848ed5db432ad68a97a3fcfcca4de28018a4c94b/docs/ps1/gpu/status-register.md#L69-L84) | Secondary reference with explicit uncertainty: bit 26 cannot identify completion of an entire DMA primitive chain. This is not a substitute for the particular submitted word, parser state, named effect or correlated commit event. |

**Further retained qualification:** the published [timeout/recovery analysis](../../research/bios/DEVICES.md#returning-timeout-includes-recovery-before-submission) reports recovery before the negative synchronization return, conditional on reporting returning, and the wrapper then submits the saved word. It must not be summarized as logging alone or rejection of submission on timeout. These are existing firmware reverse-engineering findings with independently checked decoding within that research, not new physical measurements or independent implementation lineage.

The [caller observation](../../research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up) remains a separate emulator evidence class: access order and sampled zero do not identify the write payload, parser state or committed effect. The [native proposal](#native-response-sanitized-missing-function-answer--october-24) requires specified effects before terminal continuation; that is a proposed native policy, not a completion guarantee derived from the reference return. No positive oracle or native implementation follows from this reconciliation.

**Provenance and review:** Atlas is the first reference, but its PSX-SPX ancestry remains restricted under the [provenance review](../../research/bios/PROVENANCE-REVIEW.md). Atlas and its upstream mirror are one source lineage, not independent corroboration. A named GPT-6.1 SoL Medium reviewer checked the bounded public applicability/inference distinctions; no private original bytes, captures or native source were inspected for this response. Native root retains evaluation and patch ownership. No experiment, implementation, initializer or S2 enablement was performed or authorized; all acceptance counts remain unchanged.
