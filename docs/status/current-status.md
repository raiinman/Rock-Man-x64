# Current project status

**Checkpoint: 2026-10-22, development paused at 21:37 UTC for documentation.** The already queued verification work reached a terminal receipt at 21:39 UTC; that drain is recorded below and did not authorize new implementation or acceptance.

Rock Man x64 is **not a playable game, complete IDE or full native boot**. The public repository is documentation-only. No original assets, implementation source or new private kit is published by this checkpoint.

## Last frozen and Windows-verified stage

The `native-irq-chain` stage is the last frozen checkpoint with reported actual Windows execution. Its Windows matrix contains **29 cases: 22 expected exit-0 cases and seven expected exit-1 refusal cases**. The connected normal path completes the first status command `01` and stops before unsupported reset `0A`.

These are private project attestations, not publicly reproducible Windows logs. They establish the stated console checkpoint, not complete GUI behavior, audio or game boot. See [validation and provenance](validation.md).

## New unfrozen CD configuration candidate

The newer candidate performs native reset `0A` acceptance and completion, then actual unmute `0C` configuration. Its connected path records four IRQ returns and 11 clock calls. Final `CdSync` returns 2; the low-level command-initialization helper at `800791a8` genuinely returns 0, using return instruction `8007938c` and delay slot `80079390`.

The next sound-related leaf stops at source instruction `80079070`, reading numeric address `1f801db8`. **High-level CD initialization at `80077770` has not returned.** A low-level helper's zero result is not the high-level initializer result, and neither is game boot.

Reset and unmute here are native application configuration transactions, not physical hardware equivalence or audible output. The [service contract](../technical/native-service-contracts.md) explains the separate ACK/completion and ownership obligations.

## Verification available at pause

| Evidence | Recorded result | Interpretation |
|---|---|---|
| Focused allocation failures | 677 boundaries; 1,354 repeated allocation denials | IRQ/non-IRQ failure and retry coverage; not a universal path proof |
| Isolated main suite | 92 tests passed | Private native-source regression |
| Isolated tools suite | 19 tests passed | Tool regression, not gameplay |
| CLI matrix | 21 cases passed; 14 older JSON profiles exactly unchanged | New capability and refusal paths plus baseline preservation |
| Static Windows builds | 18 passed | Compilation only; no new-stage Windows execution |
| Standalone component scripts | Seven of nine passed | Two failed runs remain unresolved acceptance items |
| Queued asset conformance | Completed successfully after pause | Previously queued validation only |
| Queued handler fixture | Compile and execution completed successfully after pause | Source-handler fixture, not production boot |
| Terminal aggregate receipt | 19 stages completed, 17 successful | Runner exit 0 does not erase its two failed stages; acceptance false |

The character component exited 1 and inspector component exited 134 because preview fixtures were omitted from the isolated input set. This explains the immediate failures; it does **not** prove those components would pass with corrected inputs, nor establish a runtime defect. The missing set of 76 fixtures totaling 29,236,235 bytes was copied and hash-checked. **Retries had not started.**

Expanded negative tests cover return-address knownness and mismatches, captured nonzero callbacks and unexpected successor arrivals. Same-owner connected reset reissue, 16-operation exhaustion and broader recovery are not thereby dynamically proven.

Earlier shared-output verification runs became inconclusive after a transport interruption and are excluded from acceptance. They are not counted as passes or failures in place of the isolated run.

## Preservation and release state

A recorded set of 214 source hashes remained stable. The last preservation check at 21:20 UTC covered 2,086 existing release files. Original inputs, the original archive and three older shared ZIP baselines were additional preservation checks, not part of that 2,086-file count. These are time-bounded checks, not a claim that a new final preservation pass has completed.

The new configuration stage remains **unfrozen and unaccepted**. Final corrected-fixture checks, source/input/preservation hashes, completion report, review and new-stage Windows execution are pending. There is no new private package.

## Mixer and packaging research

The isolated pure DSP core reports **102,822 checks over 34,193 frames**, including 20,000 randomized cases and three rejected mutants, with strict compilation and ASan/UBSan. LeakSanitizer was unavailable under tracing. This is a scratch arithmetic result only: it has no source adapter, runtime authority, endpoint or playback integration.

The selected mixer design observes the sole authoritative configuration snapshot under serialization, rather than duplicating mute state. Numeric-port mapping remains a native policy, not a proven hardware map. A new packager has 15 synthetic scratch tests; it has not produced a new private kit.

## What remains absent

No demonstrated full startup return, normal first-scene lifecycle, player control, collision/gameplay, AI, combat, full rendering fidelity, save-game compatibility or audio playback. Asset previews and diagnostic scene functions are not substitutes for those milestones.

Continue with the [capability inventory](../technical/capability-matrix.md), [validation ladder](validation.md) or [next-step handoff](decisions-and-handoff.md).
