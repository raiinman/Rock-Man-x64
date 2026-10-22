# File descriptors and device-dispatched I/O: bounded BIOS findings

This pass follows a few substantial service boundaries in the supplied firmware. It does not establish complete ISO 9660 parsing, every device implementation or MML1 usage. The original ROM profile uses `0xbfc00000`; copied-kernel coordinates refer to the separately documented inferred physical mapping at `0x500`. Within that slice, original ROM file offset equals the low-memory coordinate plus `0xfb00`. None of these observations executes the BIOS.

REA decompilation identifies candidate behavior; complete recovered instruction bodies and independent Capstone 5.0.6 decoding of retained REA bytes cross-check the important branches. Full bytes, disassembly and pseudocode remain private.

## Gates and service identities

**Observed:** The retained B0 pointer table at `0x874` binds selectors `0x32` through `0x36` to low-memory routines `0x2958`, `0x2a64`, `0x2b28`, `0x2c94` and `0x2e00`. Their behaviors support open, seek, read, write and close interpretations respectively. Original-ROM wrappers at `0xbfc0d890`, `0xbfc0d8a0` and `0xbfc0d8b0` explicitly select B0 `0x32`, `0x36` and `0x34`. The selectors are written in jump delay slots, which the C-like wrapper pseudocode omits.

Evidence: B0 table `ev_77656636b4ffa128bfe02798e968a3cd5879f9cdb83559ff508d590cbf7be750`; open wrapper `ev_d4ba064ed1b5655a030201a8bae7354d08d702eac038c7d70e858d1653e15772`; close wrapper `ev_0025fefae3fde830692ff642c19c022a67449ed322ab3f0d41a16edaf34e7d1f`; read wrapper `ev_0f385b970446f3a8af94349c1542d4270ffa202e932f8d0703b2f7cda544addd`.

Do not infer that the initial ROM template already supplies the same A0 bindings. The separate table template beginning at original offset `0x4300` has a common target in its first ten entries. The copied helper at `0x540`, selected by C0 `0x1c`, can replace the first ten A0 entries by copying the relevant B0 entries. Active table contents therefore depend on installation order and later writes. This report relies on the verified B0 bindings and does not certify final runtime A0 contents.

Evidence: ROM template `ev_c049691ada28ce1dd13058c9779c60064b9bc2371db4fa7df93647ccaa9e84c5`; C0 binding `ev_93bbaf368a31f66adc7f7ca78bb8870d18af2ebe0a44c0fc2e9a0e5b17fc6321`; retained copied helper bytes `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`.

## Descriptor ownership and open failure

A [later diagnostic-path investigation](FILE-DIAGNOSTICS.md) identifies the selected helper as an A0 selector-`0x3f` veneer whose initial template selects formatted output. The helper itself is not a halt routine. Conditional results below remain conditional on the live dispatch/output route returning.

**Observed:** The free-descriptor helper at `0x3060` scans first-word occupancy fields in `0x2c`-byte records from `0x8648` to exclusive endpoint `0x8908`: sixteen records. It returns a record pointer when the first word is zero. Its exhausted path calls a diagnostic helper before the code that would return null; the behavior of that diagnostic helper must be resolved before claiming that exhaustion always returns normally.

The independent decode of the adjacent descriptor lookup at `0x30c8` rejects signed negative descriptors and values at least sixteen, returning null; accepted indices select the corresponding record. The operation-specific routines then also test that record's first word. Range validity and open-record occupancy are separate checks.

Evidence: allocator's recovered body `ev_bc055066058d5befae3bdce4717be04b30feff5fd765a7029517a62c9a6893a3`; retained REA bytes for the independently decoded lookup `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`.

Open at `0x2958` distinguishes at least three failure boundaries. A null record from the allocator sets global error value `0x18` and returns `-1`. A path/device lookup result of `-1` sets `0x13`, clears the record's occupancy word and returns `-1`. After choosing a device, open stores caller mode, parsed device-unit information, device identity and device flags into the record, then calls the device's open callback. That callback's zero result is the successful branch. Success initializes the logical cursor to zero and returns the descriptor index. A nonzero callback result copies the record's error field into the global error, clears occupancy and returns `-1`.

These are numeric firmware error observations, not a promise that a host C runtime's errno values or lifetime policies are interchangeable.

Evidence: complete recovered open body `ev_6cf21ee9509590926889431ac9df717d48adecd3c3b907403d55a96720ba19bb`; decompiler corroboration `ev_c56267dad18753da89bce9c30d8afc01ef477067c575eeeede4ecc5da95d459d`.

## Device lookup is a separate layer

**Observed:** The selected lookup at `0x3108` walks device records beginning at `0x6ee0`, uses `0x50`-byte record strides and takes the device count from `0x7200`. A nonzero name pointer participates in a comparison-helper call; a zero comparison result returns that device record. The helper dispatches through a live A0 gate, so its exact behavior also depends on installed table contents. This pass does not establish filename case folding or universal name matching from the generic lookup alone.

The adjacent path routine at `0x31e8` skips initial spaces, separates a prefix around a colon, derives an additional numeric value from trailing prefix characters and asks for a device record. A missing record produces `-1`. Ghidra reports irregular inferred stack/register expressions in this routine, so the pseudocode is insufficient to certify parser bounds, malformed-input handling, maximum prefix length or every unit-number syntax. Those remain explicit gaps.

Evidence: device lookup body `ev_9c17614af9b6a15a4e3a259c79e486b12e55c122ef088d89c4fe61dfd037d912`; path decompilation `ev_93e875d7d3b661e97178e2c636ae3beb529216cae08055d4a7356ffd92759ead`; independent low-memory decoding from source-byte evidence `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`.

**Native proposal:** Keep a logical descriptor owner, device identity, parsed unit, cursor and operation result distinct. Do not convert every BIOS path directly into a host filesystem path or assume that successful device lookup opened a file. Constrain parser behavior only after an identified game path establishes the required inputs.

## Read dispatch, alignment and cursor changes

**Observed:** Read at `0x2b28` rejects a missing or unoccupied descriptor with global error nine and `-1`. After a separate helper call, it selects one of two device paths based on a stored flag. The direct read callback receives the descriptor record, caller buffer and length. The other path stores the buffer and requested length into the record and calls a different device callback with operation value one.

For a block-oriented device flag, the latter path divides the record's logical cursor by the device's unit size and checks the remainder. A nonzero remainder calls a diagnostic helper; if that helper returns, the routine returns `-1` before invoking the device transfer callback. It then integer-divides the requested length by the same size and stores the quotient as the transfer count. The inspected generic path does not reject a nonzero length remainder. A zero unit size has an explicit trap path. These details do not establish which flags or size a specific CD device installs.

Only the latter path visibly advances the generic cursor after a positive callback result, adding that result directly. Its zero and negative results do not take that increment branch. A negative result copies the record's error field to the global error. The direct callback path has no corresponding generic increment in this body, so device-owned state updates need separate investigation. Returned-count units and actual media work must be established from the chosen backend, not guessed from this interface.

Evidence: complete recovered read body `ev_8cef0928530e7a8b49899d4415722308b48d64970d41040a5ced1adcb2694c32`; decompilation `ev_0d53661fa0e3db5348382bf00a436c56ef76219f4599aaa7b1ea8090451d7baa`.

## Seek and close have specific source semantics

**Observed:** Seek at `0x2a64` also refuses invalid/unoccupied descriptors with error nine and `-1`. Mode zero replaces the logical cursor; mode one adds the offset. Mode two returns the existing cursor without adding an end-of-file size in this generic routine. Other modes call a diagnostic helper; if that helper returns, they set global and record error `0x16` and return `-1`. This is not evidence for a direct translation of mode two into host `SEEK_END`, nor a complete account of all device-specific seeking.

Evidence: complete recovered seek body `ev_71793f2299237d5aae6795845923fc7b3dba737599875faf7696f82fcb01eeb0`.

Close at `0x2e00` first validates range and occupancy. It calls the selected device close callback, then clears occupancy in the branch delay slot regardless of that callback's zero/nonzero result. A nonzero result copies the record error globally and returns `-1`; success returns the original descriptor value. Thus “close failed” does not mean this generic record remains open, and success is not uniformly numeric zero. A native policy that retains a descriptor on close failure would be an explicit behavioral choice, not the observed firmware rule.

Evidence: complete recovered close body `ev_2950a51eea442af0a88bd6cb59987cdc4d66de1c89e762d87b7bbc57d29177e1`; decompilation `ev_d5177bca65b9e5f0d07dfc6b01ae4a34de7f927c918aeaf7c3fc92c75a86967e`.

## What the inspected ROM loader checks

**Observed:** Loader helper `0xbfc03a18` opens with caller mode one and rejects a negative descriptor. It invokes header helper `0xbfc03c90`, whose read requests `0x800` bytes and succeeds only when the returned count is at least that amount. That helper then copies selected header fields into its output area.

If the header helper fails, the outer helper closes and returns zero. On the successful-header path it obtains payload destination and length from the output fields, calls read, closes, invokes another helper and returns one. The recovered body does not inspect the payload-read result or close result before that one. This is a bounded observation about this loader helper; it does not authenticate a loaded executable, verify a complete payload or prove that downstream boot succeeded. It also does not establish that a native MML1 implementation should reproduce these weak checks.

Evidence: complete recovered outer-loader body `ev_ea49205f3c7cdff993f3aebd6ed9beda66cb9d6d077a011fed76e6ea8a5732b7`; header body `ev_3a0c9a24c0fff1db28a43d7688f7e6af4a38c7ca9d19b1c0525c48b8b9c071d5`; header decompilation `ev_6b7a32a39b4e9ec4ec13a4e3c24aed0b9986473fc03bde47aff4fd11e46536a8`.

## Follow-up validation proposals

For a proven game dependency, prioritize invalid and stale descriptor identity, allocator exhaustion, missing device, device-open failure, direct versus block callbacks, misaligned cursor, non-multiple length, zero unit size, short reads, cursor updates and close failure after release. Test mode two independently rather than assuming familiar host seek constants. Record which source caller actually checks each result and which native policy adds stronger validation.

Still unresolved: diagnostic-helper control flow on allocation exhaustion, complete path parsing, live device registrations and flags, backend result units, actual ISO/media transactions, directory support, exact EOF behavior, malformed media and concurrency. Private evidence IDs identify retained analysis records; the complete analysis is not independently reproducible from this documentation-only repository.
