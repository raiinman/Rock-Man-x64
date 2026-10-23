# Current project status

**Checkpoint: 2026-10-23, 01:05 UTC hourly documentation update.** The software-mixer stage is sealed and Windows-verified. A newer mode-00 candidate has bounded Linux evidence but remains unsealed and not Windows-tested.

Rock Man x64 is **not a playable game, complete IDE or full native boot**. This repository is documentation-only; these reported private results cannot be independently reproduced from it.

## Last sealed and Windows-verified stage: software mixer

All **51 actual Windows cases** passed: 30 expected exit-0 outcomes and 21 intentional exit-1 refusals. All 30 complete JSON and 21 contract-scoped text comparisons matched; stderr was empty, no timeout occurred, and checked input, executable and package identities remained unchanged. Windows execution is separate from the earlier Linux sanitizer evidence; Windows sanitizers are not claimed.

The immutable stage contains 419 source files, 20 reproducibly cross-built Windows executables and 30 CLI profiles. Its Linux 51-case contract also passed. These are private validation artifacts, not a public release or download.

High-level `CdInit` genuinely returns 1 with full knownness and the source stack restored, then stops before unsupported non-null-result `CdSync`. Its connected same-owner CPU mixer performs PCM processing under shared Session serialization. Current gain, staged coefficients and applied coefficients remain distinct. It does **not** own an output endpoint, decode game audio, provide playback, establish physical SPU equivalence or boot the game.

### Frozen metadata defect, not an execution failure

Three inherited contract-summary fields incorrectly retained **40 cases / 18 executables / 21 CLI profiles**, rather than the actual **51 / 20 / 30**. The Windows runner checked and executed the actual definitions, so all 51 comparisons remain valid. The historical freeze and hashes were preserved unchanged; the stale summaries were not silently repaired.

A separate generic packager now checks derived totals, references and strict JSON before reading private inputs or creating a package. All **22 synthetic packaging tests** passed, including an independent rerun. The old inconsistent freeze is rejected by that new preflight; no override or resealing is implied.

## New mode-00 candidate: Linux recovery accepted; unsealed and not Windows-tested

The candidate applies a genuine same-image **2048-byte Form1 reader**, through actual parameter FIFO writes, response consumption, IRQ return and callback continuation. The same-owner event registry was examined exhaustively for this path: **one registered event examined, zero matched**. No matching BIOS event was fabricated. The B0:07 return remains unknown and is overwritten before the source caller uses it; no numeric success is fabricated. Existing permission remains preserved. The actual source routine returns 1 with the restored source stack, then stops at **`8001b44c`**, the next unsupported startup boundary. This is native policy, not a hardware timing claim.

| Evidence | Recorded result | Limit |
|---|---|---|
| Actual pinned regression run | 51 earlier cases, 20 builds and 30 CLI profiles passed | Linux builds/execution, not Windows execution |
| New mode profiles | Ten passed: one positive and nine refusals | Bounded connected path, not full startup |
| Independent review | Three synthetic UBSan groups: 50, 32 and 36 checks; 53 original control-flow targets checked | Review and synthetic evidence, not original-machine execution |
| Direct-pinned ASan/UBSan failure injection | Normal-path group: 23,323 checks; nonzero-path group: 10,940 checks | Targeted fail-N coverage, not exhaustive allocation coverage; leak detection unavailable |
| Isolated recovery aggregate | All 13 stages passed: 92 project tests, 19 tool tests and 13,305 metadata comparison rows | 427 source and 4,181 input identities unchanged; original attempt remains inconclusive and excluded |
| New unsealed Linux contract | 69 cases passed across 26 Linux-built executables and 40 CLI profiles: 39 expected exit 0 and 30 intentional exit 1 | Linux contract validation, not Windows execution |
| Windows cross-build | Two passes built all 26 target executables; all 26 pairs byte-identical | Actual executable/profile mapping checked; no Windows mode execution or final seal |

Before pinning, review found and guarded a stale-reader/raw-mode lifecycle bypass. Earlier feature profiles remained unchanged. Independent review closed the partial-publication concern after the targeted checks; this does not replace release sealing or target-platform acceptance.

Failed and inconclusive attempts remain part of the record. An earlier shared-tree regression log was briefly mistaken for pinned evidence; the actual pinned run subsequently passed. The first new-profile assertion expected eight copied bytes, but two real eight-byte copies correctly total 16; the failed expectation was retained. Initial allocation-failure bounds of 64 and 512 were insufficient. A later whole-call rollback assertion was also invalid: response publication can complete before IRQ diagnostic allocation fails. Narrow same-operation, retained-debt, no-duplicate and retry checks passed without adding runtime rollback.

## Research and next steps

The separate [BIOS research library](../../research/README.md) informs partial-commit and callback cautions; it is not runtime or hardware proof. The reviewed [DB8/DBA research](../../research/bios/DB8-BOUNDARY.md) identifies a community-published numeric left/right current-volume pair and signed 16-bit definition. Sony-authored numeric binding, claim-specific original-machine proof, reset/timing behavior and game hardware equivalence remain unverified. Per-voice patent circuitry and the corrected voice-sweep report do not establish master readback behavior. Historical pending-Windows research wording does not supersede the newer 51-case mixer receipt.

The fresh isolated recovery completed with all 13 stages passing. The original aggregate attempt remains inconclusive and excluded; this does not establish that its descendant processes stopped, and timings are not benchmarks.

Windows supervisor candidates 3, 4 and 5 each failed the first synthetic success case, with zero accepted checks; later cases remained unrun. The fixture itself exited successfully with exact output, but the supervisor refused additional/inconsistent process association. Candidate 5 recorded a current owned member basename consistent with a console host, not authenticated executable identity or historical process continuity. Cleanup observed the owned job empty and direct child ended. These were synthetic runner failures, not a Windows mode test or policy refusal; no protection changes or uncontained fallback were used. Console-detached candidate 6 subsequently passed all 15 synthetic Windows checks in one invocation, including deliberate descendants, timeouts and forced-supervisor-termination cleanup. The 14-file kit remained unchanged, with no protection override or unresolved cleanup. This is not Windows mode execution.

Offline compiler-provenance review verified retained cross-toolchain distribution payloads and signed-index/package linkage. Nine host shared-library dependencies are hash-pinned but lack independently established distribution origin; complete build-environment provenance is not claimed.

Next: implement and independently review the real 69-case Windows adapter, resolve bounded provenance assurance and review final sealing before Windows mode validation. A separate private graphics-entry RAM/control prefix is **implementation and validation in progress**, without independent acceptance. No original-image execution or GPU-initialization milestone is established.

No full startup return, normal first-scene lifecycle, player control, collision/gameplay, AI, combat, full rendering fidelity, save compatibility or audio playback has been demonstrated.

See [validation](validation.md), [handoff](decisions-and-handoff.md), [history](../history/validation-history.md) and [capabilities](../technical/capability-matrix.md).
