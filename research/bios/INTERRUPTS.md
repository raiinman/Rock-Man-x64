# Exception entry and IRQ callback chains: second-depth findings

These are static firmware observations under the separately documented low-memory profile. They do not establish actual MML1 use or resume native implementation. The coordinates below are physical analysis addresses in a private derived slice, not an execution trace. Original-ROM file offset equals the listed address plus `0xfb00` within that slice.

This pass uses REA `read_bytes` evidence followed by independent Capstone 5.0.6 little-endian MIPS32 decoding for code that Ghidra did not define as functions. That method is distinct from a successful REA decompilation. Complete private bytes, decoder output and reports remain outside Git.

## Vector installation and entry

**Observed:** C0 selector `0x07` points to `0xeb0`. The selected routine copies a 16-byte stub from `0xf0c` to cached addresses `0x80000080` and `0x80000000`, then transfers to a separate helper. The stub transfers to `0xc80`; C0 selector `0x06` also contains that target. Padding precedes the substantive context-saving sequence at `0xc90`. The static copy target is observed; neither executed installation nor later integrity of either vector has been established.

Evidence: entry/installer span `ev_799537ba79f5f3d2fdc17a9a8e330360fada862ea979334ef275d5c509001622`; C0 bindings `ev_93bbaf368a31f66adc7f7ca78bb8870d18af2ebe0a44c0fc2e9a0e5b17fc6321`.

Entry follows the table-of-tables current-context pointer at physical `0x108`, then addresses the register-save area eight bytes into that context. It initially saves AT, return registers and RA before calling a helper at `0xea0`, which reads CP0 Cause and EPC. Later stores preserve argument, temporary, saved, GP, SP and frame-pointer registers, CP0 Status and Cause, HI and LO. This is an explicit saved context with status and register metadata; it is not a copy of all source RAM.

Before invoking callbacks, the entry selects a kernel stack from a pointer at `0x6cf0`, establishes a kernel GP and sets FP to the selected SP. The retained copied data contains stack pointer value `0x85d8` at `0x6cf0`. This is a firmware-image initializer observation, not proof of the final runtime stack after all initialization and patching.

Evidence: entry span above; original-ROM source bytes `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb` for the initializer, with the low-memory coordinate transformation explicitly applied.

## Saved PC adjustment and the branch-delay gap

**Observed:** At `0xcc0`, entry masks the helper-returned Cause with `0x3c`. When that masked value is zero, it reads the instruction word at the helper-returned EPC, shifts its high byte down, masks with `0xfe`, and compares with `0x4a`. A match advances the value about to be saved as the continuation by four. Other paths preserve the EPC-derived value. The saved continuation becomes the later context-return target.

**Architecture interpretation:** The opcode test is consistent with the MIPS coprocessor-2 command encoding class. The inspected bytes establish the condition and PC arithmetic, not Sony GTE command behavior, pipeline completion or the hardware rationale for the adjustment.

No Cause.BD test or separate EPC-plus-four instruction fetch appears in the inspected entry sequence before this decision. That is a bounded observation, not proof that all BIOS paths ignore branch-delay state. The generic analyzer and independent decoder do not execute R3000A hazards. Keep branch-delay exceptions and interrupts around coprocessor-2 commands unresolved until supported by suitable CPU-level evidence.

The manufacturer-authored [IDT R30xx Family Software Reference Manual, revision 1.0](https://cgi.cse.unsw.edu.au/~cs3231/doc/R3000.pdf), chapter 3, explains that Cause.BD changes how EPC identifies an exception in a branch delay slot. Its family-level rules are useful context, not an assertion that every Sony implementation detail is identical. This source is hosted on a university mirror.

Evidence for firmware condition: entry span `ev_799537ba79f5f3d2fdc17a9a8e330360fada862ea979334ef275d5c509001622`.

## Four list slots, separate test and handler callbacks

**Observed:** The walker begins at `0xde4`. It obtains a list-header base through physical `0x100`, defines an exclusive endpoint 32 bytes later and advances by eight bytes per slot. Consequently this recovered loop visits four header slots in ascending address order. Calling those slots priorities is an interpretation of their registration role; the actual callback allocation and runtime registrations determine what occupies them.

Within a slot, each node supplies its successor at offset zero, handler pointer at offset four and test pointer at offset eight. Both callback pointers are read before invoking the test. A null test skips invocation. A zero test return skips the handler. A nonzero test return invokes a non-null handler with that exact result placed in argument register A0. This is more specific than treating the test as a boolean gate while discarding its value.

An ordinary handler return resumes traversal. Its return value does not decide whether to continue: the walker reads the current node's successor and continues through the list, then through later header slots. The successor is read after callbacks, so live edits to that field can affect traversal. The captured callback pointers and the later successor read have different observation times. The walker does not explicitly construct test arguments at its call site. This traversal description assumes callbacks preserve the saved registers used by the walker; arbitrary register-corrupting callbacks and their consequences have not been validated.

Evidence: entry/walker span `ev_799537ba79f5f3d2fdc17a9a8e330360fada862ea979334ef275d5c509001622`. Related insertion/removal instruction evidence remains `ev_5d3ec0532a7c132f613d1601d50b7f3d8d0ee1f2b52d9394812cee64dd413973` and `ev_80e9f7aa60f3329a14f3a2a3df474d37d4484319e6bcd6e2626c85a6f8d39ca2`.

**Bounded examples:** The copied initializer records at `0x6d58`, `0x6d68`, `0x6d78` and `0x6d88` pair tests at `0x1794`, `0x17f4`, `0x1858` and `0x18bc` with handlers at `0x1920`, `0x1958`, `0x1990` and `0x19c8`. For example, REA decompilation of test `0x1794` checks device status/mask conditions and delivers an event; its paired handler `0x1920` can enter the context-return routine at `0xf40`. A handler that transfers through that return routine does not take the ordinary return-to-walker path. Therefore “handler returned” must distinguish callback return, jump-buffer continuation and exception-context restoration.

Initializer evidence: original-ROM source bytes `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`; representative test `ev_692470dbf7400ae2b05904bd392935aac2478685e852dafcd09b3d861a98325d`; paired handler `ev_159047a73e753c6efcfb1a7cd0f34b0b30e456aec9c827f2338dede634e2fa45`. The pairings above describe initializer contents and do not prove that those nodes were installed in a specific slot at an observed runtime instant.

## End-of-chain continuation and final exception return

**Observed:** At `0xe44`, exhausting all four lists follows a different restoration path from `0xf40`. It reads a pointer from `0x75d0`, restores a jump-buffer-style RA, SP, FP, saved registers and GP, sets return register V0 to one and jumps to that saved RA. This sequence contains no RFE. The B0 table binds selector `0x19` to `0xf20`, whose short routine stores a supplied pointer into `0x75d0`; selector `0x18` reaches `0xf2c`, whose short routine selects the default buffer at `0x6cf4`.

The copied default buffer's first word is `0xf40`. Conditional on that default buffer actually being selected and unchanged, the exhausted-chain continuation reaches the final exception-context restoration path. A custom installed buffer can instead transfer control to its own saved continuation. Static initial bytes at `0x75d0` are zero; they do not establish that runtime initialization failed or that a zero pointer is used during interrupts.

Evidence: end-of-chain and setters in `ev_799537ba79f5f3d2fdc17a9a8e330360fada862ea979334ef275d5c509001622`; B0 bindings `ev_77656636b4ffa128bfe02798e968a3cd5879f9cdb83559ff508d590cbf7be750`; default-buffer initializer in `ev_3c855c29d0d01d7d76022a5b2a6a7263131dcc9202745065daa80ba4d94bafcb`.

The final return at `0xf40` selects the current context through physical `0x108`, restores HI/LO, saved Status and registers, then uses the saved continuation with RFE in the jump delay slot. Selecting the current context again matters: a prior callback or syscall can change the current-context pointer. A host adapter must not silently restore the original context merely because it was current on entry.

Evidence: complete recovered return instructions `ev_7e6e762829e837e45dc4d3b3dfd816755c919f3c30bf76c788f0392ee34aa5a1`.

## Native validation proposals and remaining limits

For an identified game dependency, test four-slot traversal order; null tests and handlers; zero and nonzero test results; forwarding a nontrivial test value to A0; ordinary handler returns; early context returns; successor edits during callbacks; installed continuation replacement; and current-context changes before final restoration. Preserve source RAM side effects when a callback returns. Represent source register state and the host call stack separately.

Nested exceptions remain a specific gap. The inspected entry writes into the current context and chooses a kernel stack, but this does not establish a general nesting protocol, bounds for nested frames, callback permission to re-enable interrupts or recovery from faults inside tests. Likewise, raw pointer-table membership does not establish the safety of arbitrary caller-supplied nodes or jump buffers. Keep unsupported paths explicit and distinguish a chosen native refusal policy from verified BIOS semantics.

No dynamic callback order, interrupt timing, branch-delay behavior or MML1 use is established by this pass. The full evidence is private and is not independently reproducible from the documentation-only repository.
