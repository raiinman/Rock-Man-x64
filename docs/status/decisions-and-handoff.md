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

The software-mixer stage is sealed and passed all 51 actual Windows cases. Its historical summary-counter defect is recorded separately; the unchanged frozen definitions, not stale summary fields, governed execution. The generic packager now rejects inconsistent totals and references before private-input handling, with 22 synthetic tests passed.

The newer mode-00 candidate is **unsealed and not Windows-tested**. Pinned regression coverage, ten new profiles and targeted ASan/UBSan fail-N checks passed. The isolated recovery aggregate passed all 13 stages, preserving 427 source and 4,181 input identities; the original attempt remains inconclusive and excluded. A newer unsealed Linux contract passed 69 cases across 26 executables and 40 CLI profiles (39 expected successes, 30 intentional refusals). Both 26-target Windows cross-builds passed and all 26 pairs were byte-identical; actual executable/profile mapping passed without placeholders. Review final artifacts and provenance, complete the separately authorized real 69-case Windows adapter and independent review, then consider final sealing and separately authorized Windows mode execution.

## Next source boundary

The candidate connects the actual result copies, parameter FIFO, same-image Form1 reader and response/IRQ/callback continuation. It examines the genuine same-owner event registry without inventing a matching event, preserves permission and reaches a true source return before the next unsupported startup boundary, `8001b44c`. This is not full startup. Preserve committed publication and outstanding IRQ debt across diagnostic allocation failure; do not impose unsupported whole-call rollback.

A separate graphics-startup RAM/control prefix has moved from static planning into implementation in progress. Implementation and validation are in progress, without independent acceptance; no original-image execution, accepted milestone or GPU-initialization proof exists.

Separately reviewed BIOS analysis supplies test hypotheses, not runtime/hardware proof. Custom-hook return, ordinary callback return and final exception restoration remain distinct. [Community documentation](../../research/bios/DB8-BOUNDARY.md) defines the DB8/DBA current-volume pair and signed 16-bit field; Sony numeric binding, original-machine proof for the claims, reset/timing and game hardware equivalence remain unverified. Per-voice circuitry and corrected voice-sweep reports do not prove master readback behavior.

## Explicitly unresolved scopes

- Connected reset reissue and already-unmuted command admission are not dynamically established merely because guards exist.
- The 16-operation history limit, operation-ID and revision exhaustion need appropriate supported-path evidence before broader claims.
- Nonzero user callbacks, unexpected successor IRQs, reissued status/history recovery, timeout cancellation and unmapped errors remain bounded or unsupported.
- Numeric-port native policy is not a proven physical register map; software current gain is not an audio-device measurement.
- Decoder, Track 2, playback, output endpoint, timing and audible output need separate design, authority and verification.
- First-scene integration still needs genuine reaching-state and lifecycle proof; diagnostic materialization does not close that gap.
- Rendering fidelity, collision, input, gameplay, saves and full IDE workflows remain future work.

## Release and publication boundary

The configuration and newer software-mixer stages are frozen and privately Windows-validated. The mode-00 candidate remains unsealed and must not be described as accepted or Windows-tested before final receipts. Documentation publication does not authorize publishing source, assets, previews, executable bytes, private package contents or private receipts.

Future public updates should record the exact accepted boundary, changes since the prior checkpoint, validation category and remaining unknowns. Public reference research should remain clearly distinguished from implementation and execution evidence. Do not call the process legally clean-room certified.

See [architecture](../technical/architecture.md), [service contracts](../technical/native-service-contracts.md), [current status](current-status.md) and [validation](validation.md) for the supporting detail.

## Runner and provenance gates

Synthetic Windows supervisor candidates 3–5 each failed their first success case and accepted zero checks. Preserve all failed receipts; a current owned-member basename does not authenticate the image or prove historical process continuity. Owned-job cleanup completed, but later synthetic cases were unrun. Console-detached candidate 6 subsequently passed all 15 synthetic Windows checks in one invocation, including deliberate descendants, timeouts and forced-supervisor-termination cleanup. The 14-file kit remained unchanged, with no protection override or unresolved cleanup. This is not Windows mode execution. No protections were changed and no uncontained fallback is accepted.

Cross-toolchain distribution payload and signed-index/package checks improved offline provenance. Nine host shared-library dependencies remain hash-pinned without independently verified package origin. Select and document bounded provenance assurance rather than claiming full environment authentication from deterministic output alone.
