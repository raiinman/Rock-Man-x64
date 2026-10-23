# Current project status

**Checkpoint: 2026-10-23 hourly documentation update.** The software-mixer stage is sealed and Windows-verified. A newer mode-00 candidate has bounded Linux evidence but remains unsealed and not Windows-tested.

Rock Man x64 is **not a playable game, complete IDE or full native boot**. This repository is documentation-only; these reported private results cannot be independently reproduced from it.

## Last sealed and Windows-verified stage: software mixer

All **51 actual Windows cases** passed: 30 expected exit-0 outcomes and 21 intentional exit-1 refusals. All 30 complete JSON and 21 contract-scoped text comparisons matched; stderr was empty, no timeout occurred, and checked input, executable and package identities remained unchanged. Windows execution is separate from the earlier Linux sanitizer evidence; Windows sanitizers are not claimed.

The immutable stage contains 419 source files, 20 reproducibly cross-built Windows executables and 30 CLI profiles. Its Linux 51-case contract also passed. These are private validation artifacts, not a public release or download.

High-level `CdInit` genuinely returns 1 with full knownness and the source stack restored, then stops before unsupported non-null-result `CdSync`. Its connected same-owner CPU mixer performs PCM processing under shared Session serialization. Current gain, staged coefficients and applied coefficients remain distinct. It does **not** own an output endpoint, decode game audio, provide playback, establish physical SPU equivalence or boot the game.

### Frozen metadata defect, not an execution failure

Three inherited contract-summary fields incorrectly retained **40 cases / 18 executables / 21 CLI profiles**, rather than the actual **51 / 20 / 30**. The Windows runner checked and executed the actual definitions, so all 51 comparisons remain valid. The historical freeze and hashes were preserved unchanged; the stale summaries were not silently repaired.

A separate generic packager now checks derived totals, references and strict JSON before reading private inputs or creating a package. All **22 synthetic packaging tests** passed, including an independent rerun. The old inconsistent freeze is rejected by that new preflight; no override or resealing is implied.

## New mode-00 candidate: not accepted, sealed or Windows-tested

The candidate applies a genuine same-image **2048-byte Form1 reader**, through actual parameter FIFO writes, response consumption, IRQ return and callback continuation. The same-owner event registry was examined exhaustively for this path: **one registered event examined, zero matched**. No matching BIOS event was fabricated. The B0:07 return remains unknown and is overwritten before the source caller uses it; no numeric success is fabricated. Existing permission remains preserved. The actual source routine returns 1 with the restored source stack, then stops at **`8001b44c`**, the next unsupported startup boundary. This is native policy, not a hardware timing claim.

| Evidence | Recorded result | Limit |
|---|---|---|
| Actual pinned regression run | 51 earlier cases, 20 builds and 30 CLI profiles passed | Linux builds/execution, not Windows execution |
| New mode profiles | Ten passed: one positive and nine refusals | Bounded connected path, not full startup |
| Independent review | Three synthetic UBSan groups: 50, 32 and 36 checks; 53 original control-flow targets checked | Review and synthetic evidence, not original-machine execution |
| Direct-pinned ASan/UBSan failure injection | Normal-path group: 23,323 checks; nonzero-path group: 10,940 checks | Targeted fail-N coverage, not exhaustive allocation coverage; leak detection unavailable |
| Full project aggregate | No verified terminal receipt | The original aggregate attempt remains inconclusive and excluded; a fresh isolated rerun started, with no final-pass claim |

Before pinning, review found and guarded a stale-reader/raw-mode lifecycle bypass. Earlier feature profiles remained unchanged. Independent review closed the partial-publication concern after the targeted checks; this does not replace outstanding full-project acceptance.

Failed and inconclusive attempts remain part of the record. An earlier shared-tree regression log was briefly mistaken for pinned evidence; the actual pinned run subsequently passed. The first new-profile assertion expected eight copied bytes, but two real eight-byte copies correctly total 16; the failed expectation was retained. Initial allocation-failure bounds of 64 and 512 were insufficient. A later whole-call rollback assertion was also invalid: response publication can complete before IRQ diagnostic allocation fails. Narrow same-operation, retained-debt, no-duplicate and retry checks passed without adding runtime rollback.

## Research and next steps

The separate [BIOS research library](../../research/README.md) informs partial-commit and callback cautions; it is not runtime or hardware proof. Sony documentation distinguishes setting/current concepts, but DB8/DBA numeric meaning, reset values, timing and signedness remain unresolved. Per-voice patent circuitry does not establish master readback semantics. Historical pending-Windows research wording does not supersede the newer 51-case mixer receipt.

A fresh isolated rerun began at 00:04 UTC with an observed first-suite heartbeat. The original aggregate attempt remains inconclusive and excluded; this does not establish that its descendant processes stopped.

Next: complete the fresh isolated candidate aggregate, review final identities and artifacts, then consider an immutable freeze and separately authorized Windows validation. A release builder is only being prepared. Graphics continuation is **static planning only**: bounded ResetGraph diagnostics, RAM fill and a live initialized callback may reach the next firmware-service boundary. It is not implemented or executed, and does not establish GPU initialization.

No full startup return, normal first-scene lifecycle, player control, collision/gameplay, AI, combat, full rendering fidelity, save compatibility or audio playback has been demonstrated.

See [validation](validation.md), [handoff](decisions-and-handoff.md), [history](../history/validation-history.md) and [capabilities](../technical/capability-matrix.md).
