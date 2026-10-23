# Selected A0:39 heap initialization: static effects

## Identity and selected binding

This checks the authorized 524,288-byte BIOS, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. REA/Ghidra 12.1.4 verified the original ROM mapping at `0xbfc00000`, with analysis profile `0bbf3f2fe69b8dd315230293abd97f3e42a736f36bbee860431e138012accf9e`. This generic MIPS32 little-endian profile does not execute PS1 instructions, RAM aliases or exception behavior. Mapping evidence: `ev_66897ec8c4eba93fde08b6b040c3ab079c7ce37f1da988ee4e5ca40d44fec4f6`.

The retained [A0 installation and dispatcher findings](KERNEL-SERVICES.md#selected-a049-route-and-missing-live-state-proof) supply the initial gate/dispatcher and separately installed table. For selector `0x39`, the selected word is physical `0x2e4`, sourced from original ROM offset `0x43e4`. A new complete REA read of that word identifies target `0xbfc01e24`: `ev_47a5fe27b7c76772c568d27e15a33f36045eb52cc132a355cf612ddacf9518cd`. This establishes the initial selected binding, not the actual game's mutable dispatch or a native interception.

REA returned all 56 requested bytes at that target: `ev_dace1ff729af3b4234d5c2b87443a2ddde1a83a04ec8098dcf58960592265a4a`. Ghidra did not recover a procedure at that address, so a function-instruction request failed; no recovered-function extent or pseudocode is claimed. Independent field decoding and a separate Capstone 5.0.6 review agree on 14 instructions, ending with a return at `0xbfc01e54` and its store delay slot at `0xbfc01e58`. The selected span, ROM offsets `0x1e24..0x1e5b`, has SHA-256 `61509bda07b9609ebdd2cae2fdf9ab2cf154b62ab2bf6f9892b96b672f657c4b`. No firmware execution occurred.

## Arguments and ordered memory effects

**Independent instruction interpretation:** Let `A` be incoming `a0` and `S` incoming `a1`, both 32-bit values. Let `T` be `S` rounded down to a multiple of four by logical shifts. On the normal path, the leaf performs five 32-bit stores in this order:

| Order | Guest address | Stored value |
|---|---|---|
| 1 | `0xa0009000` | `A` |
| 2 | `A` | Zero |
| 3 | `0xa0009008` | `A + T + 4`, modulo 2^32 |
| 4 | `0xa0009004` | Original `S`, including its low two bits |
| 5 | `0xa000900c` | Zero, in the return delay slot |

The endpoint calculation is a value written to a global; the leaf does not write at that calculated endpoint. It clears one word through the supplied address, not the whole supplied region. The address itself is not aligned, masked or range-checked by these instructions. Size rounding affects the endpoint calculation while the original size is retained separately. Addition uses non-trapping unsigned forms; there is no explicit overflow, minimum-size, capacity, boundary or failure branch.

These are ordered effects, not an unconditional final-memory specification for arbitrary pointers. If the supplied address aliases a global word, stores can overwrite earlier results. Alignment, accessibility, memory-map/alias policy, exceptions and interruptions remain execution prerequisites. The fixed stores target RAM aliases under the usual PS1 map, but the supplied-address store can target another region, including MMIO, depending on `A`. The body performs no loads, nested calls or stack accesses, and does not disable interrupts. Later allocator operations and the meanings or invariants of these globals need their own evidence.

## Registers, return and limits

The leaf writes `at`, `t6`, `t7`, `t8` and `t9`. On normal return, `at` holds `0xa0010000`; the temporaries hold the shifted size, rounded size, `A+T` and `A+T+4`, respectively. It contains no writes to `a0`, `a1`, `v0`, `v1`, saved registers, `sp`, `ra` or HI/LO. There is no stack frame or explicit success/failure result. In particular, this leaf leaves `v0` unchanged; a fabricated success constant is not supported by these instructions.

These are leaf-only static properties. The initial dispatcher additionally changes `t0` and `t1`; an actual whole call also depends on its effective gate, table, code, CPU state and any interception policy. A fault can leave only a prefix of the stores completed. No physical behavior, fault recovery or full game-time ABI occurrence was measured.

The [community memory-allocation reference](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/kernelbios/memory-allocation.md) identifies this service as heap initialization. That naming supports the investigation but does not establish this digest's binding or the game's arguments. A native allocator policy can deliberately differ, provided it retains explicit ownership and a distinct policy outcome; it must not be labeled a completed BIOS-equivalent call on these facts alone. The separate [A0:49 investigation](A049-RECORDER.md) still lacks the game's preceding GPU and dispatch state.

Original bytes, decoding records, supplied caller details and complete REA evidence remain private. This documentation is not a public reproducibility package.
