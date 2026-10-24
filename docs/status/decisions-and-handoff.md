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
