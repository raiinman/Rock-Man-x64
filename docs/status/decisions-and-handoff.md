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
| Keep one authoritative CD mute owner | A future synchronous mixer observes committed configuration under serialization rather than mirroring mutable mute state |
| Freeze only after complete review | Candidate tests, compiler passes and a terminal runner are insufficient by themselves |

## Immediate acceptance closure after resumption

The smallest open loop is the **existing CD configuration candidate**, not a new feature:

1. Completed: corrected-fixture character and inspector retries, settled source/input and preservation checks, and the 22:06 UTC cloud-validation receipt. Original failed attempts remain retained.
2. Completed: final artifact review confirmed by 22:08 UTC and approval to proceed with freezing at 22:09 UTC.
3. In progress: immutable freeze/rebuild and the Linux 40-case contract. Do not label these complete until their final receipts are checked.
4. Next: finish the private freeze/package verification and execute the exact candidate on Windows. Cross-builds do not substitute for this run.
5. Only after that bounded checkpoint, consider native audio-owner/mixer integration under its own evidence and ownership requirements.

The existing frozen IRQ-chain stage remains the latest Windows-verified baseline. The desired outcome is an accepted or explicitly rejected bounded configuration checkpoint, not a game-boot or playback claim.

## Next integration boundary

The new candidate stops at the sound-related numeric-port read at source `80079070`; high-level CD initialization has not returned. A proposed mixer adapter must establish its native coefficient/state ownership and actual source reads/writes rather than returning a convenient zero to pass the branch.

The scratch DSP core provides arithmetic evidence only. Any integration must first establish initialized/probed processor ownership, current versus requested gain, staged versus applied matrix, stale-generation rejection and serialized authoritative configuration capture. It must preserve the existing CD response and IRQ obligations.

The source path requires genuine leaf, wrapper, callback-setter and high-level initializer returns. Static research identifies later command-mode work, including command `0E`, as a further boundary, not permission to jump directly there. Stop earlier if a live pointer, callback, synchronizer or source branch is unsupported. No branch should be forced merely to reach a named milestone.

## Explicitly unresolved scopes

- Connected reset reissue and already-unmuted command admission are not dynamically established merely because guards exist.
- The 16-operation history limit, operation-ID and revision exhaustion need appropriate supported-path evidence before broader claims.
- Nonzero user callbacks, unexpected successor IRQs, reissued status/history recovery, timeout cancellation and unmapped errors remain bounded or unsupported.
- Numeric-port native policy is not a proven physical register map; software current gain is not an audio-device measurement.
- Decoder, Track 2, playback, output endpoint, timing and audible output need separate design, authority and verification.
- First-scene integration still needs genuine reaching-state and lifecycle proof; diagnostic materialization does not close that gap.
- Rendering fidelity, collision, input, gameplay, saves and full IDE workflows remain future work.

## Release and publication boundary

The new packager's 15 synthetic tests are scratch evidence only. There is no new private kit to distribute. Documentation publication does not authorize publishing source, assets, previews, executable bytes, private package contents or private receipts.

Future public updates should record the exact accepted boundary, changes since the prior checkpoint, validation category and remaining unknowns. Public reference research should remain clearly distinguished from implementation and execution evidence. Do not call the process legally clean-room certified.

See [architecture](../technical/architecture.md), [service contracts](../technical/native-service-contracts.md), [current status](current-status.md) and [validation](validation.md) for the supporting detail.
