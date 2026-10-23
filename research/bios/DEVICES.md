# Peripheral evidence and native port implications

This is a static firmware investigation. It does not inspect MML1 code, execute firmware, establish a hardware reset state, or prove that the game calls a particular BIOS service.

## Coverage limits

Later [decoded-image CD](DECODED-CD.md) and [sound](SOUND.md) reports extend this investigation using a separately identified transform output. The ROM and copied-kernel observations below retain their original subject and mapping boundaries.

The explicit mapping imports one contiguous ROM range at `0xbfc00000`. RAM, hardware-register state, scratchpad and other ROM aliases are absent. A negative exact-address cross-reference query therefore means that the selected Ghidra reference inventory contains no reference to that address; it does not mean a peripheral is unused. Indirect base-plus-offset accesses, RAM copies, aliased addresses, unidentified code and command data all require separate work.

The generic little-endian MIPS32 analysis language is a decoding superset. Its decompiler types and register labels are analysis conventions. It does not establish R3000A load-delay behavior, PS1 GTE/COP2 semantics, bus timing, DMA ownership or physical device state. The reset decompiler labels CP0 registers using the generic language; these labels require R3000A-specific review.

## Relevance to the current native boundary

The latest [native handoff](NATIVE-HANDOFF.md) identifies the published A0:49 boundary; earlier CD and sound boundaries are historical stages. This investigation still lacks the actual game arguments, reaching state and result consumer. Preserve the distinction between observed firmware accesses and the project's deliberately selected native product contracts.

For a resumed port investigation, identify each game-facing request before implementing it: source caller and arguments; actual command admission; response bytes and phase; FIFO consumption; interrupt acknowledgement; callback and continuation ownership; and the source return. A firmware routine that writes a device address is not evidence that a Windows adapter completed the corresponding operation.

The implementation work must not gain new behavior from this research update. No rendering, sound output, playback, input or gameplay execution is established by these notes.

## ROM observations

Evidence below is tied to BIOS SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. Addresses are locations in the explicitly imported ROM reset alias. Peripheral names are investigation labels; the numeric accesses and access widths are the direct observations.

### CD command admission and asynchronous causes

ROM `0xbfc04c38` checks an idle-like software state value `0xffff`, requires a positive transfer count, clears several event classes through a helper, records the destination/count/mode, and selects a word count of `0x200`, `0x246` or `0x249` according to two mode bits. It then checks bit `0x10` at `0x1f801800`. Only its ready branch writes index zero, the low byte of the requested mode at `0x1f801802`, software state `0xfe`, and command byte `0x0e` at `0x1f801801`; it returns one on that branch and zero on the failed admission branches. These are byte-wide hardware accesses and word-wide software-state stores, confirmed from instructions. The routine returning one proves an admission path in static code, not a completed read or a completed hardware command. [D1, D2, P2]

The related routine `0xbfc04d50` independently checks the same idle-like state and ready bit, writes a mode parameter and command `0x0e`, and records software state `0x0e`. The different state identifiers show why a command number alone does not identify the whole operation or continuation. [D3]

ROM `0xbfc04dec` reads the interrupt-mask and interrupt-status words through a table entry resolving to `0x1f801070`, checking mask `0x4` in both. On the admitted path it selects CD register index one using a byte store to `0x1f801800`, reads a byte from `0x1f801803`, separates low-three-bit cause from `0x18`, acknowledges nonzero groups using byte stores, and dispatches the low-three-bit cases one through five to distinct routines. Its acknowledgement paths also contain actual word stores to address zero inside four-iteration loops; treating these as a convenient no-op would discard observed source stores. The exact effect of those stores requires the system's memory state and timing, which this static analysis does not supply. [D4, P2]

The case-three routine `0xbfc05194` dispatches again on the current software command/state. Its case `0x0c` and case `0x0b` both reach `0xbfc0615c`, which restores the saved state, clears the saved-state slot to `0xffff`, and calls an event helper. Its case `0x0e` reaches `0xbfc061a0`, which marks the current state idle-like and calls that helper. These observations demonstrate state-sensitive completion notification, not physical audio mute state or successful playback. [D5, D6, D7]

The case-five routine `0xbfc057b0` reads two response bytes. Depending on current state it stores further response bytes, raises an error-related event through a helper, or issues command `0x0a` and changes software state to `0xddd`; a repeated recovery state takes a separate path. The case-two routine `0xbfc05558` recognizes that recovery state and clears it before notification. This supplies a useful recovery-state investigation lead, but it does not establish that every reset command always has two responses or prove any MML1 reset path. [D8, D9]

### CD transfer and DMA ownership

ROM `0xbfc05f08` keeps remaining-count, destination and stride fields separate. On a positive-count branch it records the current destination, performs indexed byte writes to the CD registers, changes two memory-control words, decrements the software count, calls `0xbfc065c0` with destination and selected word count, then advances the destination by four times that word count. The last-count branch additionally issues command byte nine and selects another software state. [D10, P2]

The helper `0xbfc065c0` updates a DMA priority/control word, writes a transfer address and block-control value to the DMA channel whose base resolves to `0x1f8010b0`, then writes channel-control value `0x11000000`. Its code starts or configures a transfer; these stores do not prove that RAM received any sector data. The source pointer, remaining count, block configuration, actual transfer and later completion must remain distinct native obligations. [D11, P2]

The three selected counts imply 2048, 2328 and 2340 destination bytes by multiplication by four. This is a derived arithmetic observation about these branches, not a complete sector-format specification or a claim that all these bytes are user payload. [D1, D10]

### GPU command stream and two transfer paths

The ROM pointer table resolves the command/data address to `0x1f801810`, status/control to `0x1f801814`, and related DMA addresses to `0x1f8010a0`, `0x1f8010a4`, `0x1f8010a8` and `0x1f8010f0`. [P1]

ROM `0xbfc03d80` polls a status bit, emits a three-word upload-shaped command/header sequence, then streams `(width * height) >> 1` words from its source buffer through 32-bit stores to the command/data address. Each word packs two candidate 16-bit pixels; that packing is an inference from count and header structure, not a verified complete GPU pixel-format implementation. [G1, G2, P1]

ROM `0xbfc03ea0` uses the same header shape, writes a different direction/control request, adjusts the DMA control word, supplies the source address and block sizing, and writes channel-control value `0x01000201`. This is a separate DMA-backed route. A native renderer needs an explicit data-ownership and completion contract before either path can be represented as successful. [G3, P1]

ROM `0xbfc04138` makes its synchronization path depend on status bits. One path polls the GPU status; another polls channel-control state and subsequently GPU readiness. It has explicit failure exits calling a diagnostic helper for bounded polls, and a later readiness loop that is not bounded by that same counter. Inventing readiness would erase observable branch and failure behavior. Exact wall-clock time, frame timing, GPU rasterization, drawing rules and DMA completion are not established. [G4, P1]

### A0:49 submission and a documentation discrepancy

**Static binding and independent decoding:** The [startup table installer](STARTUP.md#low-memory-service-installation) copies ROM table words to physical `0x200`. Selecting entry `0x49` from that source gives ROM target `0xbfc03fac`; entry `0x4e` gives `0xbfc04138`. These two selected bindings were independently read from the digest-checked original BIOS. They describe installer-produced entries, not a captured game-time dispatch table or proof that later code leaves those entries intact.

The complete A0:49 wrapper calls the synchronization routine, then submits the saved first argument through a 32-bit store to `0x1f801810`, preserving the returned value. There is no conditional branch suppressing this store when synchronization returns `-1`. This resolves the timeout-submission ambiguity for this firmware's ordinary returning path; an indefinitely waiting synchronization call never reaches the store. The wrapper conclusion comes from independent instruction decoding, rather than a new REA decompilation or runtime test.

**Retained REA instructions, independently checked:** The synchronization entry examines GPU status mask `0x60000000`. When clear, it polls GPU status mask `0x10000000` (bit 28) with a counter initialized to `0x10000000`. Otherwise it polls DMA channel-control mask `0x01000000` (bit 24) with that counter, then polls GPU status mask `0x04000000` (bit 26) without a progressing timeout counter. Its successful DMA branch writes `0x04000000` to the GPU control port before returning zero. Bounded timeout exits call a diagnostic helper and return `-1`. Counter constants are instruction observations, not elapsed-time measurements. [G4, P1]

The [pinned PSX-SPX GPU-function description](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/kernelbios/gpu-functions.md) instead describes WFEP readiness after DMA completion. Under its current bit names that means bit 28, whereas this BIOS instruction stream selects bit 26. Keep the numeric masks explicit; the general description must not overwrite the identified firmware behavior. This discrepancy does not establish behavior across all BIOS versions or physical GPU timing.

**Native investigation proposal:** Once the actual game slice arrives, distinguish the no-DMA bit-28 wait, DMA busy-bit wait and post-DMA bit-26 wait. Preserve GP0 submission even when the synchronization return is ignored or negative. Confirm the dispatch binding, command word, GP0 parser state, preceding GP1/DMA state and result consumer before choosing a native policy. No implementation change or game acceptance is established here.

### Minimal branch evidence for the selected synchronization routine

The retained instructions support a smaller investigation than requiring every GPU status bit to be known. The table below is a proposed evidence checklist, conditional on the effective dispatch reaching this exact routine. It does not establish a current game state or authorize a synthetic ready value. [G4]

| Decision | Smallest relevant evidence | Limit |
|---|---|---|
| Initial branch | Both bits in GPU status mask `0x60000000` known zero, or at least one of them known one | The first proves the no-DMA branch; the second proves the other branch. An all-zero known mask proves neither |
| No-DMA immediate return | A subsequent GPU-status read with bit 28 known set | This branch does not read GPU channel-control state. A clear bit enters polling; unknown readiness does not prove a timeout |
| DMA branch progress | Channel-control bit 24 known clear, followed by a GPU-status read with bit 26 known set | These are ordered observations, not interchangeable fields from one snapshot; the successful branch also writes GPU control |
| Submitted word's role | Effective wrapper binding plus the GP0 stream position at its store | Readiness or a discarded return does not prove that the word begins a new command |

A producer and ordering history must justify each consumed observation. A prior GPU control write alone does not supply a complete later status sequence; software initialization flags or unrelated DMA interrupt bookkeeping do not supply it either. If the native startup contract omits that producer, record where the state becomes unknown and identify the chosen service abstraction explicitly. This checklist separates a missing observation from a proved busy state, failure or finite return.

### Command-zero lead and its limits

The [pinned PSX-SPX other-command page](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/gpu/other-commands.md), SHA-256 `fea217bf11b4e94282f63079bb59cda44bc9c3cd3e92233405980784b472208e`, describes GP0(00h) with an explicit uncertainty marker. A word with a zero high byte therefore provides a command-zero lead **if it is actually submitted at a command boundary**. A pointer-shaped low value does not make the observed single-word wrapper dereference that value or start an ordering-table transfer.

Primary author reports [PR 116](https://github.com/psx-spx/psx-spx.github.io/pull/116) and [PR 135](https://github.com/psx-spx/psx-spx.github.io/pull/135) bound the claim more carefully than the informal NOP label: selected parameters left the tested GPU readback and VRAM state unchanged; a later busy-copy experiment distinguished FIFO behavior. The reports concern GPU versions 0 and 2. They do not settle timing, establish every parameter or parser state, or show that this game's occurrence reached that measured condition. These are community hardware-test reports reviewed as sources, not experiments reproduced here. Their linked probe implementation was not imported or run.

The [GP0 port and command description](https://psx-spx.consoledev.net/dev/ps1/gpu/i-o-ports-dma-channels-commands-vram/) explains that following words can be parameters of an existing command. Thus command-byte classification must retain stream position. Even a proven command-zero occurrence would not erase the preceding BIOS synchronization, DMA-control effects, failure behavior or ABI obligations. A discarded service result and unknown status bits cannot supply those missing facts. The remaining native investigation is an effective-dispatch and reaching-device-state join, not permission to return fabricated success.

### Sound and input coverage

ROM `0xbfc06ca4` begins with four 16-bit zero stores to `0x1f801d86`, `0x1f801d84`, `0x1f801d82` and `0x1f801d80`, then proceeds to initialization helpers. ROM `0xbfc06ec4` also performs this four-address sequence after a service call. Those actual halfword writes give a concrete sound-related initialization lead. They do not establish initialization of all sound registers, sample RAM, voice state, decoding, mixing or any audible output. [S1, S2]

The ROM exact-address reference inventory contains no entries for the selected serial/input addresses `0x1f801040`, `0x1f801044`, `0x1f801048`, `0x1f80104a` and `0x1f80104e`, nor the selected sound-control address `0x1f801daa`. This bounded result does not establish absence of controller, memory-card or sound routines. These negative results motivated the explicit relocated-kernel investigation below; aliases, computed references and unidentified code remain coverage limits. [I1-I6]

### Relocated kernel: controller-shaped polling and card-shaped protocol

A second, explicitly derived analysis mapping places original BIOS file range `0x10000..0x18bef` at physical address `0x500`, matching the statically observed startup copy. It is not a captured runtime memory image. Within this mapping, the selected serial addresses now have 72, 18, 2, 85 and 2 exact references respectively. Their absence from the ROM reference inventory therefore did not mean absence from the BIOS. [K1-K5]

The relocated pointer table at `0x7258` resolves the serial base to `0x1f801040` and interrupt-status base to `0x1f801070`. Routine `0x4498` selects one of two ports in a control halfword, transmits bytes including one and `0x42`, checks received identifier and handshake data, copies received byte pairs into a caller-associated buffer, and distinguishes success from a failure path. It polls halfword status/control fields and checks interrupt mask `0x80`; some waits have counters while other readiness waits are unbounded. This is a controller-shaped byte transaction, not a host input event or a complete controller compatibility specification. The exact protocol identity is an inference from the static sequence; no connected device was observed. [K7-K9]

Routine `0x51f4` is a state-dependent serial transaction with transmitted values including `0x57`, checks for handshake bytes, address/checksum fields and distinct positive/negative returns. It is a memory-card-write-shaped protocol candidate. The investigation did not establish the caller's full request lifecycle, sector contents, persistence, card capacity or all error recovery paths. A Windows save adapter must bind and validate the actual game request before implementing this candidate. [K10, K11]

Instruction evidence exposes device reads discarded by the decompiler: routine `0x4498` has byte loads into the architectural zero register at `0x4530` and `0x45d8`; routine `0x51f4` has analogous reads at `0x528c` and `0x52d0`. The loaded values are discarded, but the memory access still exists. These reads disappear from the returned pseudocode. A reconstruction based only on simplified pseudocode could therefore lose FIFO or status side effects even where the decompiler appears internally consistent. Whether these specific reads consume data is a device-semantics question, not established by the instruction itself. [K8, K11]

The selected `0x1f801daa` query remains empty in this derived kernel reference inventory as well. It remains a bounded negative result, not proof that sound-control access is absent from the firmware. [K6]

## Evidence key

Only evidence identities and original conclusions belong in the public handoff. Complete private REA records include bytes and decompiler output and must remain private. The shorthand below names the exact retained Evidence records; the parent evidence ledger may normalize these into its own reference scheme.
- D1: `ev_6373d68ca314377d9738be4d09b10fedea3c01a77fbaa2b5e0ae5fa8fa389266` (read_function_instructions).
- D10: `ev_80e848422d34eb0d3d7d33154a6a45ef8a14589b47156fcc15140af209d6ff44` (read_function_instructions).
- D11: `ev_0984a04ad9b5f1de744f96c02d676c570d88e347fe041e599db6e3a33957de5c` (read_function_instructions).
- D2: `ev_de07a32c05da62eba68be96569b9dd5468190edf5e5a01e69bca0090b1e5ebfa` (procedure_pseudo_code).
- D3: `ev_cfe5b4a55d4c7f49984ab86af0bb3db17d943d23fcce9ee654bb7c98759f23ae` (read_function_instructions).
- D4: `ev_c16273bcc4059a63719814c2fb6bbb6ea4578e3785d04c56c25d8cf27d2114b1` (read_function_instructions).
- D5: `ev_9d4449b4c6fb0292f80674cb86e2f2e34ea9318c37c4b44d9f959b7fdb038826` (procedure_pseudo_code).
- D6: `ev_0365b88e768c68710fc71aba2bd8a341b525301d57a98fe6373b67aa9021f97e` (procedure_pseudo_code).
- D7: `ev_20f4d6cb1752b9ad12aa6b050c66decf7ce04d06efe0c2a3f5ce3f10b52501b2` (procedure_pseudo_code).
- D8: `ev_7e6849de83f47f4453c30a10a49ce1dcca1eeef2048d33669ab18683708e0d41` (read_function_instructions).
- D9: `ev_f5094c3985f23d33fd91ec63a5922b95a9042b8f921cdbbd669d7d13f3e2361b` (procedure_pseudo_code).
- G1: `ev_73373ce0dff686bfa43768b50607875217073be3d2285c27c127907ad23c8794` (procedure_pseudo_code).
- G2: `ev_7ffe124a27e772cc23443294cff7456dabd1bd7dd241b97c7ccae983c288df21` (read_function_instructions).
- G3: `ev_78eb474075f934f7a3fb2a87c5148caa4f2db6ea77c0a27e5397961e43831258` (read_function_instructions).
- G4: `ev_67fda4f6948b0c04d61463e1c1c2511683199c0e53e78e0c9d8ad7997ea8cb29` (read_function_instructions).
- I1: `ev_9baf06425a4ae0cf617e5412470139b8dab5b2809cdd7d9cabc95b9dd0267319` (xrefs).
- I2: `ev_36820f412dbe25f8c9fecc7dbe9af6012201fd409bc5ed38c83fed8cb8f2206c` (xrefs).
- I3: `ev_e5a6c8d3ee73699d20772181de29306d2136211fb6199ff294360aa0f17d830d` (xrefs).
- I4: `ev_9a29ed66c9cdd7a44baed8058ce5a1f6f66b42de39bc549f9db60c03e73ce22f` (xrefs).
- I5: `ev_e27e9d26d06395a7c37c37285244b612be61d5c3526129760f557fc0b7f5f249` (xrefs).
- I6: `ev_64f067f8c8e1d8cb8281715b77ce923ed4960eb18fcbe855c11f20a01322923c` (xrefs).
- P1: `ev_581d8e1b614b8855b498ce86ac161b6fc371562d2640cefe9ff2e19a9d10ffe9` (read_bytes).
- P2: `ev_35aa392f6ffca1e1777686669f3d1b657ab0a65980b96bdde97b709fb77e3c5d` (read_bytes).
- S1: `ev_34072a42e7a1d298f6e41fdedb843383055c2b4b0ed0ef33c211f1db659cf82b` (read_function_instructions).
- S2: `ev_b7e333ea54efd277b530f42c284f58bd4a40b206ae2c459e00b18f99aa9e7b28` (read_function_instructions).


- K1: `ev_a8a77986eb8ca9de6e7dcecb08beeaa7f7cdfffb8c5d923d60cb0b265bde1de9` (xrefs, derived kernel mapping).
- K10: `ev_fbc2a765b72549de4f221e5eb09df404314fe4ff0b46bc611e1691be44034a6f` (procedure_pseudo_code, derived kernel mapping).
- K11: `ev_36ef10b6a51d6c869caf0346bbc2639bfded185adb99e8aab6b2fc08398f67ec` (read_function_instructions, derived kernel mapping).
- K2: `ev_4c76629359429db48c8bd576270bb2f8bc2631b51dab82c2762fc52c6b19e47a` (xrefs, derived kernel mapping).
- K3: `ev_62e1adb3fad4cdbdaff962864c01c3409c5517a0e6e46ad4af55e3eee0091782` (xrefs, derived kernel mapping).
- K4: `ev_c8d4edc554d0f36d7655cfdab9875e29cf1c9e5205e02d046617af5928aba2aa` (xrefs, derived kernel mapping).
- K5: `ev_35e10d4223c11a9f317bfb5f080f73e6aecb2f064434ad5f8bfffc7dd9fb366b` (xrefs, derived kernel mapping).
- K6: `ev_7698ecaa6e7e148ad5dda0117569d515395b2a30e4985cb2e3f2abd4735e6ba1` (xrefs, derived kernel mapping).
- K7: `ev_d3a078a08c69478d52332e94379241ae50ec200b3565c4039aeb606f6daa84c0` (read_bytes, derived kernel mapping).
- K8: `ev_89e8c5b57fa97c887760db1f933fbce06b2437c67ce5aac7145a59c5923c7044` (read_function_instructions, derived kernel mapping).
- K9: `ev_43352254707d4993f156c38906e09753d594d293efb18143e61a4543a648363f` (procedure_pseudo_code, derived kernel mapping).
