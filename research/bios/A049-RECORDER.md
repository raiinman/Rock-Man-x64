# Original A0:49 recorder: calibration and one synthetic call

## Scope and identity

The owner authorized building and running one calibration followed by one synthetic A0:49 test. Both completed once, using original SDK-free guest fixtures and observational Lua profiles in PCSX-Redux CLI `29142.20261022.44.x64`, changeset `afad8da748b38415a17a3080e027cf2f44983cfb`. This is execution inside that emulator model, separate from the native game and physical PS1 behavior. No emulator implementation source or other game port was used.

The supplied BIOS remains 524,288 bytes, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`; the executable emulator SHA-256 is `9643b4a589c1f5b4eee8294cc04c7aaaf393ff2d439585739a13716eb0600dc1`. Each process had a 30-second wall limit, a 2,048-event recorder limit and bounded output. Exclusive launch records prevent accidental repetition. Both exited zero in approximately five seconds, before either limit. The guest is loaded through the emulator's executable-loading path after BIOS initialization; this is not a retail game boot. Recording starts at fixture entry, so absent callbacks below describe that armed interval only.

Private generators, guest images, instrumentation, captures, output and invocation receipts remain outside this repository. Digests below identify retained evidence, not public downloads; this documentation alone is not a reproducibility package.

| Original fixture | Guest SHA-256 | Capture SHA-256 | Observations |
|---|---|---|---|
| RAM calibration | `5f3b790cd036ac2e1326722f087e96fceaf6cd3321d42c8cc2dd7962a2a2b679` | `961e357bb7b86c239d3a802c8a1824a417f4c076e8772aa6fbdade83a5c3a3ea` | 16 events; 5.06 seconds |
| Single A0:49 fixture | `ac461e3990fcc55169eb54173ce2e0c40feefb16a4b32d72cca0bb34d0dca14f` | `e8cbdbb84f049c68c5219f0555185fd9e68aa65104eda4f42e5166cb5e884136` | 22 events; 5.03 seconds |

The calibration instrumentation SHA-256 is `b4aced85d64e661feb743477fcbadc77f12faee2161f3b9410b8972d5efe1808`; the final A0:49 instrumentation SHA-256 is `4d661318ccff9a1b74dbaca3fa30452625faf0b77f4cb4358b0aad94ac92f5ff`. Their versions differ intentionally because they observe different fixtures.

## What calibration established

The new guest used main RAM, explicit register patterns and an explicit interrupt-disabled input. It performed two distinguishable stores after a separate initialization store, a load with independent delay instructions, and a taken branch with an observable delay-slot effect. No device read was performed by this calibration.

For these operations, data-access callbacks exposed the pre-store RAM samples. Following execution markers exposed the newly stored values. The load callback and immediate successor marker retained the old destination-register pattern; the next independent marker and guest-produced ledger showed the loaded pattern. The branch delay slot appeared once, the skipped fallthrough marker was absent, and the terminal ledger matched the expected result. Entry samples precede guest register initialization and are not treated as initialized inputs.

This establishes useful phase distinctions for these controlled patterns. The [documented callback](https://pcsx-redux.consoledev.net/Lua/breakpoints/) still has no transferred-value field. Register/RAM snapshots, access events and the guest ledger remain separate evidence classes. Callback order is not a cycle counter, and execution-PC markers are not fetched-opcode or retirement payloads. No Lua MMIO read was added to recreate a CPU load result.

## What the single A0:49 fixture established

Declared fixture inputs were a bounded stack, interrupts disabled, a GP1 DMA-direction-off request and literal argument zero. No readiness values, BIOS tables or firmware timeout counters were patched. These inputs are not recovered MML1 startup state.

The recorded execution-PC sequence passed through the A0 gate, physical dispatcher `0x5c4`, selected table load at `0x5d0`, wrapper `0xbfc03fac` and synchronization entry `0xbfc04138`. The table RAM sample was `0xbfc03fac`. More usefully, the dispatcher's destination register still contained slot address `0x324` at the load-delay marker and contained `0xbfc03fac` at the subsequent jump marker. This joins a reported route and loaded target rather than relying only on a table peek. It does not reveal instruction-cache contents or directly prove fetched opcode bytes.

Two GPU-status CPU-read callbacks were followed by independently positioned post-load register samples, each showing `0x14802000`. Its direction mask `0x60000000` was clear and bit 28 was set, consistent with the observed no-DMA path. No watched channel-control read occurred during this fixture. The sample is a model result for this occurrence, not a reusable ready constant or physical reset specification.

At the wrapper's GP0 store, the source register was zero and the target register selected `0x1f801810`; a write callback and following execution marker bracketed that instruction. The fixture then reached its return marker with `v0 = 0`, and its ledger confirmed the return. The stack pointer returned to its declared value, and sampled `s0`/`s1` values were preserved. This is selected-register and stack-pointer evidence, not full stack-memory or ABI preservation. A direct bus payload, GPU command acceptance and parser/FIFO effects were not measured.

## Verification and next use

A separate agent reviewed the generated headers and instruction fields before launch, then independently checked both completed captures, ordinals, route, delayed register samples, ledger and receipt hashes. Five host-side negative guards passed for incomplete/malformed captures and process time/output limits. The runtime event limit was not deliberately exhausted; no extra firmware run was performed to stress it.

The recorder can now distinguish access reports, sampled state, delayed CPU-register results and a reported route for this bounded model experiment. DMA-directed synchronization, timeout/recovery, full formatter ABI and MML1's preceding dispatch/GPU/parser history remain untested. The [native handoff](NATIVE-HANDOFF.md) still requires that game-specific join. Advancing a native A0:49 request cannot be justified by copying this fixture's status or return value.
