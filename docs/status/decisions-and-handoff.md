# Decisions and next step handoff

Development resumed on 2026-10-22 at 22:04 UTC after the documentation pause. This page records the selected direction and the evidence needed before further milestones; it does not authorize implementation, device access, packaging or release.

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

The isolated IDE Source bytes/Back feature passed independent portable/build-only review, strict and sanitizer tests, and byte-identical Windows cross-builds of the inspector and harness. Actual Windows UI, state, reparse and pixel validation remain unrun. Its reader-derived offsets show current-disk bytes, not a fingerprint-authenticated copy of the earlier decode. Preserve source-bound editing and original-input immutability while selecting any next work.

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
