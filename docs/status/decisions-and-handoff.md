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

## Immediate acceptance closure

The frozen configuration stage has passed all 40 Windows cases. The next open loop is the **newer native software-mixer freeze**, not another gameplay claim:

1. Completed: connected Linux mixer checks and the pre-reporting 18-stage aggregate.
2. Completed: isolated reporting-only correction, 21 exact older reports, nine new positive/refusal profiles, and affected tests/verifiers.
3. Completed: guarded rebuild with 20 byte-identical target executables, 419 matching source files and a second Linux 51-case pass. Final unchanged contract execution with explicit before/after runner hashes remains in progress; freeze is not sealed. Retain the earlier excluded rebuild failure and require fresh output directories.
4. Next: verify the sealed private package and execute the exact stage on Windows. Twenty staged target executables do not establish target execution.

## Next source boundary — planned, not implemented

The integrated mixer genuinely returns from `CdInit` with result 1, then stops at `800779cc` before the next unsupported non-null-result `CdSync` wrapper proceeds. It does not provide a decoder, output endpoint or playback.

The next plan covers the actual eight-byte result copy, parameter FIFO, real mode-00 Form1 reader and response callback/event continuation. Implementation is held until the audio freeze is sealed. Preserve real source microcommits and existing response/IRQ obligations; do not skip a live pointer, callback, synchronizer or unsupported branch to reach command `0E`.

The separately authored BIOS analysis supplies targeted test hypotheses, not independently reproduced runtime/hardware evidence or permission to copy firmware behavior into the game translator. Custom-hook return, ordinary callback return and final exception restoration remain distinct. A0 context/heap contracts, DB8 semantics and live game-event mapping remain unresolved.

## Explicitly unresolved scopes

- Connected reset reissue and already-unmuted command admission are not dynamically established merely because guards exist.
- The 16-operation history limit, operation-ID and revision exhaustion need appropriate supported-path evidence before broader claims.
- Nonzero user callbacks, unexpected successor IRQs, reissued status/history recovery, timeout cancellation and unmapped errors remain bounded or unsupported.
- Numeric-port native policy is not a proven physical register map; software current gain is not an audio-device measurement.
- Decoder, Track 2, playback, output endpoint, timing and audible output need separate design, authority and verification.
- First-scene integration still needs genuine reaching-state and lifecycle proof; diagnostic materialization does not close that gap.
- Rendering fidelity, collision, input, gameplay, saves and full IDE workflows remain future work.

## Release and publication boundary

The configuration package is frozen and privately Windows-validated. The newer audio package remains in preparation and must not be described as sealed or accepted before final receipts. Documentation publication does not authorize publishing source, assets, previews, executable bytes, private package contents or private receipts.

Future public updates should record the exact accepted boundary, changes since the prior checkpoint, validation category and remaining unknowns. Public reference research should remain clearly distinguished from implementation and execution evidence. Do not call the process legally clean-room certified.

See [architecture](../technical/architecture.md), [service contracts](../technical/native-service-contracts.md), [current status](current-status.md) and [validation](validation.md) for the supporting detail.
