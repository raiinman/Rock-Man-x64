# Additional staged firmware region

This is a newly identified static coverage region in the same 524288-byte BIOS, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. It does not establish executed boot state, a complete user-interface implementation, or any MML1 dependency. Initial staging bytes are not necessarily final executable bytes.

## Outer copy and transfer

The complete 76-byte instruction body at ROM `0xbfc06ff0` supplies destination `0x80030000`, source `0xbfc18000` and count `0x67ff0` to helper `0xbfc02b50`. It calls helper `0xbfc01920` and then transfers through a function pointer holding `0x80030000`, forwarding its saved caller argument. The 60-byte body of `0xbfc02b50` confirms a byte-at-a-time copy for a positive count with a nonzero destination. These are static control-flow and copy semantics, not a captured RAM image.

The initial copy therefore selects original source offsets `0x18000..0x7ffef`, length 425968 bytes, for destination addresses `0x80030000..0x80097fef`. Full REA source bytes were checked against the original file selection before preparing a private derived staging image. Its SHA-256 is `0d350f1eff02f76136184fccfbc4b4d272a3a74aa4cd16b358b4d37d5dc9e3e1`. The initial copied range overlaps part of the previously examined kernel-source range; the two regions are not disjoint partitions of the BIOS.

Within this initial mapping only:

`original file offset = 0x18000 + (staging address - 0x80030000)`

The staging image does not begin with the eight-byte PS-X EXE signature. That bounded byte observation does not identify every possible container format or rule out executable material later in the region. An executable-file loader and this firmware-internal staging path are different entry mechanisms.

Evidence: `ev_c927f563644cfc5adeed21e65b262dc8bd3dbe68990d8c2f819e518eead128b8` (outer routine pseudocode); `ev_9eab138a2e3919a794d53e0c414e6a451837960dd87e23258c2032d8f8619139` (complete outer instructions); `ev_b7752a4b146483736cdcf574dd675d65dc43e5758b09005cff6f3b251c0c542b` (copy helper pseudocode); `ev_031cfdf22ea01fcb3dfffa63968499aec626d5d51103036feff02ce4799d79d2` (complete copy helper instructions); `ev_090ec5f2088e159af1e72c476e82a0448ab10d95744f755f2e01070a206c3225` (first 256 source bytes); `ev_584573cb8fb43e87fdb4f9088c530d8bb9120875999caa09e2792e26ad6e1e86` (complete source-byte selection).

## Nested loader and byte-stream transformation

Independent instruction decoding was corroborated by a correctly mapped REA profile of the 76-byte loader stub, SHA-256 `8782a2aa10b397a9b75c4b38a2314c86f40f2d092bd27f394bfb478380ebd257`, at `0x80030000`. Under the intended `0x80030000` staging address, it selects source `0x8003004c`, destination `0x80190000` and byte count `0x30db4`, performs word copies, calls A0 with selector `0x44`, and jumps to `0x801c0ca4`. Selector semantics should be bound separately; the numeric request alone is not an implementation of cache synchronization.

The nested copy would select original offsets `0x1804c..0x48dff`, length 200116 bytes, and initially place them at `0x80190000..0x801c0db3`. Its source-coordinate correspondence, conditional on this statically interpreted copy, is:

`original file offset = 0x1804c + (nested address - 0x80190000)`

Consequently the nested jump target `0x801c0ca4` corresponds to original offset `0x48cf0`, and the remaining selected tail has length `0x110` bytes. This formula differs from the outer formula because the second copy starts 76 bytes into the first staging image. Do not apply either formula to subsequently transformed output without a new derivation.

A second code-only REA profile maps the 272-byte tail, SHA-256 `255b26c39bd18d6fd299ebf42caeaa28cd02ad67ce554b73514def153b5d2c6f`, at `0x801c0ca4`. Its complete 68-instruction body corroborates byte-stream input, literal and earlier-output copy paths, output stores, an A0 selector `0x44` call and a jump to `0x80030000`. The tail assembles an output size from three little-endian bytes, skips the fourth header byte, and consumes control words assembled in big-endian order. Its back-reference loop count includes an extra copy because the decrement is in the branch delay slot. This is static transformation logic; it does not identify a named compression format or establish successfully executed boot. Raw linear disassembly of all staged data is not a meaningful count of executable coverage.

The nested observations were independently decoded and corroborated by correctly mapped REA instruction bodies. External source/output regions are absent from these short code-only profiles, which do not execute original instructions. Stub instruction Evidence: `ev_6016a1befb9e9af6518e33a2a1aade49675325c99648de4e4d5c8834622b02ad`; stub pseudocode: `ev_0faae87663f3cdbc331bfbcf569043229807c78054bd53c2ee38c18e2253c5ac`; tail instructions: `ev_f599d860b753ffcac0b4fd431836fe0565b15c77a6d165566e2dcd064d3b3088`; tail pseudocode: `ev_6bdcc04cb4656a403aabe255ffefed4aa3817be3844fdce743a583846c609080`. All derived image files, bytes and decoder output remain private.

## Bounded independent data transform

After two independent reviews against the correctly mapped REA instruction body, a private byte-stream decoder processed only original source offsets `0x1804c..0x48cef`, excluding the code tail. It validated the whole BIOS digest, matched its source selection against the retained REA bytes, bounded input and output, rejected references before produced output and rejected output overshoot. These bounds are host validation choices, not a claim that the firmware implements the same checks. The decoder transformed data; it did not execute or emulate original machine instructions.

The declared output size was 372032 bytes. The transform consumed exactly all 199844 selected input bytes, ending at original offset `0x48cf0`, with zero selected bytes left over. The resulting private artifact has SHA-256 `7920530e46981bab09bef02c72f35964bca25c879a72f3bf1c5313921143fbe7` and proposed initial mapping `0x80030000..0x8008ad3f`. A separate read verified that the saved artifact matches this receipt. The run decoded 76648 literal tokens and 52954 reference tokens; 1528 references copied overlapping produced data. Maximum observed reference distance was 16384 bytes and maximum run was 34 bytes. These are observed statistics of this input and decoder, not universal format limits.

The firmware tail separately zero-stores from the decoded end toward `0x801c0ca4`; that operation, cache requests, transfers and all firmware calls were not run or modeled. The decoded private file contains only the 372032 produced bytes. This successful transform and exact input consumption support the static derivation but do not prove an authentic BIOS, a complete frontend, device behavior, executed initialization or a successful game boot. The derived output is separately bound by the later REA profile below.

## Relevance and next boundary

The resulting image has now been independently opened in REA at `0x80030000`, with its own derived subject digest. The initial defined inventory is 744 procedures and 111 strings. These counts describe analyzer definitions, not complete understanding or executed functionality. Load-image Evidence: `ev_78f80837d85451d3532d2da712775871c1ef5749c85e53f301268d070367ffa1`; overview: `ev_6ebd1b4ebc735c23efec42bd8c72a16009f360421122132af10c69340734f54a`. Device paths in that image are a new investigation, not inherited conclusions from the ROM profile.

**Decoded addresses have no linear original-ROM offset formula.** Their provenance is the reviewed transform and output digest. The original source formulas above apply to the copied encoded inputs and short code selections only. The output file also omits the separately identified zero-fill region, so references beyond its end do not prove that those locations are absent from a running console.

The short stub/tail pseudocode ends with a bad-instruction warning where the complete instruction bodies show transfers outside those deliberately short mappings. That warning is an analysis limitation and is not evidence that the supplied firmware contains an invalid transfer instruction.

The initial ROM-only and copied-kernel profiles cannot settle graphics, sound or frontend coverage if another stage transforms firmware into a different address range. This staging lead explains a concrete missing mapping, but does not by itself prove that the unexplored region contains the required sound service or that MML1 depends on it. Any additional recovered image needs its own input digest, transformation description, address map, evidence profile and coverage limits before conclusions from it join the native-port handoff.
