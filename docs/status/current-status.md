# Current project status

**Checkpoint: 2026-10-22, hourly development update.** Development resumed at 22:04 UTC. The CD configuration stage is now frozen and Windows-verified; the newer software-mixer stage has connected Linux evidence but its freeze and Windows validation remain pending.

Rock Man x64 is **not a playable game, complete IDE or full native boot**. This repository remains documentation-only. The private results below cannot be independently reproduced from this repository.

## Last frozen and Windows-verified stage

The CD configuration/reset/unmute stage passed **all 40 Windows cases**: 27 expected exit-0 results and 13 intentional exit-1 refusals. All 21 complete JSON comparisons matched exactly and all 19 text comparisons matched their contract. Stderr was empty, there were no timeouts, and before/after input, executable and package integrity checks were unchanged.

The supported path performs native reset `0A` acceptance and completion followed by actual unmute `0C` configuration. Four IRQ returns precede the final `CdSync` result 2. Low-level helper `800791a8` genuinely returns 0. This frozen stage then stops at sound-read boundary `80079070`; **high-level CdInit has not returned in this stage**. Native configuration is not physical drive reset or audible output.

## New connected native software-mixer stage

The newer implementation binds sealed same-owner mixer state, actual CPU PCM processing and authoritative mute capture under shared Session serialization. Functional readiness is established lazily after actual unmute, not fabricated to bypass the source branch. Current software gain, staged coefficients and applied coefficients remain distinct.

Its high-level `CdInit` routine returns at `80077800` to `8001b3f4` with fully known result **1** and source stack pointer `801fffa0`. It then stops at **`800779cc`**, before the next unsupported non-null-result `CdSync` wrapper proceeds. This is not completion of later mode-setting or startup.

| Evidence | Recorded result | Boundary |
|---|---|---|
| Connected ASan/UBSan checks | 20,222 checks | Owned native integration, not physical SPU conformance |
| Production PCM oracle | 20,000 frames | CPU processing, not device output |
| Source boundaries | 136 checked | Bounded translated path, not full boot |
| Pre-reporting aggregate | All 18 stages passed: 92 regression tests, 19 tool tests, ten components | 438 tracked source/input/test/tool identities unchanged during that aggregate |
| Reporting-only correction | One CLI reporting source changed; 437 other files unchanged | No additional runtime capability |
| Corrected CLI coverage | 21 old reports byte-exact; nine new positive/refusal profiles and affected tests/verifiers passed | Compositional verification, not a second full aggregate |

The correction removes contradictory new-profile legacy summaries and derives both high-level-return fields from the genuine source receipt. Historical inconsistent reports are retained, not accepted as current truth. Some intermediate reporting branches were source-reviewed only; production reset-after-readiness coverage remains absent.

The mixer **does not open or own an output device**; physical endpoint presence was not enumerated. There is no disc decoder, playback, physical SPU equivalence or game boot. The physical meaning of numeric sound address `1f801db8` remains unresolved; this adapter is an explicit native policy.

## Freeze and acceptance still pending

Audio freeze preparation was approved at 22:51 UTC. Staging contains 419 source files, 20 Windows target executables and 30 CLI profiles for a 51-case contract (30 success and 21 refusal cases). These are staging counts, not proof of an accepted freeze or Windows execution.

An initial Linux 51-case contract passed. Runner hardening now requires fresh output directories; seven negative path/symlink checks passed. An earlier rebuild attempt encountered a changing runner script and exited 127; that failed attempt is retained and excluded from acceptance. The settled guarded rebuild passed: all 20 Windows target executables were byte-identical and all 419 source files matched the corrected snapshot. A second Linux 51-case pass completed; one final unchanged run capturing explicit before/after runner hashes remains pending. The audio freeze is not yet sealed. This is release-tooling validation, not a failed Windows game execution. No prior overwrite was evidenced; prior Windows checks used fresh task directories.

## Research and next source boundary

The separate [BIOS research at the reviewed revision](https://github.com/raiinman/Rock-Man-x64/blob/e748ffd5fd30c355077b93329126746e7b756773/research/bios/NATIVE-HANDOFF.md) reports static Ghidra, Capstone and decoded-firmware analysis. It has not been independently reproduced here as BIOS runtime, hardware or game proof. Custom B0:19 hook versus B0:17 return distinctions support targeted tests; B0:07 event dispatch corroborates future callback mapping, not a live event match. DB8 hardware semantics, A0 setjmp/longjmp/heap behavior and a real mode-00 Form1 reader remain unresolved.

The next source plan is **prepared, not implemented**: non-null eight-byte `CdSync` result copy, actual parameter FIFO, real mode-00 Form1 reader, and response callback/event continuation. Implementation remains held until the audio freeze is sealed. See [handoff](decisions-and-handoff.md).

## What remains absent

No demonstrated full startup return, normal first-scene lifecycle, player control, collision/gameplay, AI, combat, full rendering fidelity, save-game compatibility or audio playback. Asset previews and diagnostic scene functions are not substitutes for those milestones.

Continue with the [capability inventory](../technical/capability-matrix.md), [validation ladder](validation.md) or [next-step handoff](decisions-and-handoff.md).
