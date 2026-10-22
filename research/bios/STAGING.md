# Additional staged firmware region

This is a newly identified static coverage region in the same 524288-byte BIOS, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. It does not establish executed boot state, a complete user-interface implementation, or any MML1 dependency. Initial staging bytes are not necessarily final executable bytes.

## Outer copy and transfer

The complete 76-byte instruction body at ROM `0xbfc06ff0` supplies destination `0x80030000`, source `0xbfc18000` and count `0x67ff0` to helper `0xbfc02b50`. It calls helper `0xbfc01920` and then transfers through a function pointer holding `0x80030000`, forwarding its saved caller argument. The 60-byte body of `0xbfc02b50` confirms a byte-at-a-time copy for a positive count with a nonzero destination. These are static control-flow and copy semantics, not a captured RAM image.

The initial copy therefore selects original source offsets `0x18000..0x7ffef`, length 425968 bytes, for destination addresses `0x80030000..0x80097fef`. Full REA source bytes were checked against the original file selection before preparing a private derived staging image. Its SHA-256 is `0d350f1eff02f76136184fccfbc4b4d272a3a74aa4cd16b358b4d37d5dc9e3e1`. The initial copied range overlaps part of the previously examined kernel-source range; the two regions are not disjoint partitions of the BIOS.

Within this initial mapping only:

`original file offset = 0x18000 + (staging address - 0x80030000)`

The staging image does not begin with the eight-byte PS-X EXE signature. That bounded byte observation does not identify every possible container format or rule out executable material later in the region. An executable-file loader and this firmware-internal staging path are different entry mechanisms.

Evidence: `ev_c927f563644cfc5adeed21e65b262dc8bd3dbe68990d8c2f819e518eead128b8` (outer routine pseudocode); `ev_9eab138a2e3919a794d53e0c414e6a451837960dd87e23258c2032d8f8619139` (complete outer instructions); `ev_b7752a4b146483736cdcf574dd675d65dc43e5758b09005cff6f3b251c0c542b` (copy helper pseudocode); `ev_031cfdf22ea01fcb3dfffa63968499aec626d5d51103036feff02ce4799d79d2` (complete copy helper instructions); `ev_090ec5f2088e159af1e72c476e82a0448ab10d95744f755f2e01070a206c3225` (first 256 source bytes); `ev_584573cb8fb43e87fdb4f9088c530d8bb9120875999caa09e2792e26ad6e1e86` (complete source-byte selection).

## Nested-loader lead, pending a correctly mapped REA profile

Independent MIPS instruction-field decoding of the initial source bytes identifies a short loader stub. Under the intended `0x80030000` staging address, it selects source `0x8003004c`, destination `0x80190000` and byte count `0x30db4`, performs word copies, calls A0 with selector `0x44`, and jumps to `0x801c0ca4`. Selector semantics should be bound separately; the numeric request alone is not an implementation of cache synchronization.

The nested copy would select original offsets `0x1804c..0x48dff`, length 200116 bytes, and initially place them at `0x80190000..0x801c0db3`. Its source-coordinate correspondence, conditional on this statically interpreted copy, is:

`original file offset = 0x1804c + (nested address - 0x80190000)`

Consequently the nested jump target `0x801c0ca4` corresponds to original offset `0x48cf0`, and the remaining selected tail has length `0x110` bytes. This formula differs from the outer formula because the second copy starts 76 bytes into the first staging image. Do not apply either formula to subsequently transformed output without a new derivation.

An independent preliminary decode of that tail finds byte-stream reads, literal and earlier-output copy paths, output stores, a further A0 selector `0x44` call and a jump toward `0x80030000`. That supports investigating a packed-data transformation stage. It is not yet a verified compression-format identification or recovered final image. Raw linear disassembly of all staged data is not a meaningful count of executable coverage. Correctly mapped REA inspection, bounds, back-reference behavior, termination and output provenance are the next questions.

The nested observations use independent interpretation of bytes retained in the complete source-byte Evidence record above. They are not successful REA decompilation of the nested target and do not execute original instructions. All derived image files, bytes and decoder output remain private.

## Relevance and next boundary

The initial ROM-only and copied-kernel profiles cannot settle graphics, sound or frontend coverage if another stage transforms firmware into a different address range. This staging lead explains a concrete missing mapping, but does not by itself prove that the unexplored region contains the required sound service or that MML1 depends on it. Any additional recovered image needs its own input digest, transformation description, address map, evidence profile and coverage limits before conclusions from it join the native-port handoff.
