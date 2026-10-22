# File-service diagnostics: dispatch and return boundaries

This static follow-up narrows the previously unresolved diagnostic helper used by file-descriptor exhaustion and unsupported seek modes. It concerns the supplied 524288-byte firmware, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. It does not establish an executed diagnostic, current output-device state or MML1 usage.

## The copied helper is a dispatch veneer

Independent Capstone 5.0.6 decoding of retained REA kernel-source bytes identifies physical helper `0x6ae0` as a three-instruction tail veneer to service gate A0, with selector `0x3f` assigned in the jump delay slot. Its original source bytes are at file offsets `0x165e0..0x165eb`. The veneer preserves the caller's return address and transfers through the live gate; it contains no self-contained halt or fatal loop. It also contains no independent guarantee that the selected service will return.

REA source evidence: `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`. The complete retained kernel selection was matched against the digest-verified original file before this independent interpretation. This is independent decoding of REA-returned bytes, not a newly recovered Ghidra function body.

## The initial ROM template selects a formatter-shaped path

An independent little-endian word read at original file offset `0x43fc`—template base `0x4300` plus selector `0x3f` multiplied by four—finds target `0xbfc018e0`. This word is in the ROM template used by the separately observed A0 installation routine. The observation identifies an initial-template binding; it does not capture the active RAM table after installation, replacement or patching.

Independent decoding of original source offsets `0x18e0..0x191f` shows that this target collects caller arguments into an argument-list area, passes numeric first argument one, and calls `0xbfc00da0`. It subsequently restores its saved return address and stack and uses an ordinary return instruction. The bounded core span `0xbfc00da0..0xbfc018df` scans an input byte string, distinguishes a percent marker and conversion-related values, and repeatedly calls another output veneer. It has ordinary return paths for a null input pointer and for reaching the string terminator. These operations support a formatted-output interpretation; they are not evidence that every argument, format or device path returns normally.

These template and formatter observations come from independent original-file reads after whole-image size/digest verification. They are deliberately distinguished from the retained REA kernel-byte evidence. A private receipt records the selected source spans, hashes, decoder coverage and method; the selected spans are not claimed to be newly certified whole-function boundaries.

The A0 template-copy observation is separately supported by `ev_fd17c375398dc1b1e9622f860b5d31e14f1fadbd91468a59c490e374b2436ae8`. That record establishes the copy procedure, not the runtime contents of the gate or a new REA read of the `0x43fc` word.

## The output route adds another live boundary

The formatter's selected output veneer at ROM `0xbfc0d880` transfers through B0 with selector `0x3d` set in its delay slot. An independent word read of the retained copied-kernel template binds that selector to physical `0x406c`. The selected body at that address has character-shaped handling, including special branches for tab and newline values. Its ordinary emission path calls the previously investigated generic write routine at physical `0x2c94` with numeric descriptor one, a byte-sized source region and requested count one.

This supplies a concrete connection to descriptor/device-dispatched I/O. It does not establish that descriptor one is open, which device it owns, whether its callback blocks or returns, or whether any output appears. It also does not certify final A0 or B0 contents. The copied B0 word and character-output region are independently decoded from the retained REA kernel-source evidence above; the ROM veneer is an independently decoded original-file span.

## Narrower qualifications for the filesystem findings

The earlier phrase “unresolved diagnostic helper” can now be replaced with a more specific boundary: the caller invokes an A0 selector-`0x3f` diagnostic path whose initial ROM template selects formatted output. This is positive evidence against describing helper `0x6ae0` itself as a fatal halt. Ordinary return paths exist in the template-selected output chain.

The existing conditional caller results should remain conditional. Descriptor exhaustion reaches the trailing null-record return if that dispatch and its output work return. Unsupported seek mode reaches the error-field assignments and `-1` result after the same diagnostic boundary returns. Neither the veneer nor the initial template proves that every possible live-table, format, descriptor or backend state returns normally. The remaining uncertainty is a specific dispatch/output dependency, rather than a completely unidentified helper.

For the native-port investigation, distinguish a diagnostic notification policy from file-operation success or failure. A host logging function returning does not establish that the source operation succeeded; conversely, this firmware evidence does not require turning a recoverable file-service diagnostic into a process termination. The adopted behavior must follow identified game dependencies and an explicit native policy.

All original bytes, disassembly, raw reports and private receipts remain outside the public repository. No firmware instruction was executed, and these private analysis results are not independently reproducible from the documentation-only public contents alone.
