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

The diagnostic continuation performs one real diagnostic publication, a bounded RAM clear and guarded initialized callback, then stops at A0:49 (`8007cc0c`). Keep the actual continuation and pending obligations; do not skip the service because its numeric return is later discarded.

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

The loader heap proposal is accepted as **native-policy design only**. Any future completion must have a distinct native-policy outcome and persistent allocator ownership; preserving native bytes or registers cannot erase unresolved BIOS effects or establish hardware equivalence. A new implementation candidate is not yet independently accepted. The accepted loader prefix still stops at A0:39.

Visual acceptance remains blocked by missing required tooling and a version-registration mismatch; no nondisruptive repair was verified, and no application restart or security change was made. A transfer-route audit qualified earlier authorized handling as a compatibility route rather than the documented standard helper route; reuse is held pending review. This qualification does not invalidate the separately scoped lifecycle result or authorize another transfer.

The accepted native loader compatibility run stops pending A0:39; the separately accepted 23-check Windows host-function lifecycle does not establish real-launcher or actual-capture display. Preserve the earlier viewer failures and later approved-context pass as distinct evidence. No automatic rerun, transfer reuse, security change or continuation through unsupported services follows.

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
