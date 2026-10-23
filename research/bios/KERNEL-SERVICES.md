# BIOS kernel services: static findings for the native-port investigation

This note describes the supplied firmware, not verified MML1 dependencies. Service names below are candidate interpretations unless linked to a recovered dispatch selector. No target execution occurred. Complete REA evidence stays private; evidence identifiers below refer to those retained records.

The primary image was mapped at `0xbfc00000` with generic `MIPS:LE:32:default`. Code intended for low RAM decodes with misleading `0xb000....` absolute call targets in that view. These are artifacts of applying the MIPS jump rule at the ROM address; they are not evidence that the BIOS deliberately calls that address range. Relative branches and local stores still require instruction checks. The separately derived low-RAM profile is needed before asserting a complete service call graph.

## Event allocation

**Observed:** The routine at ROM analysis address `0xbfc1188c` reads the event-table pointer from uncached low memory `0xa0000120`. A helper returns a slot index or `-1`. On failure the routine returns `-1`. On success it uses a `0x1c`-byte record stride, writes four caller-supplied values into the record, sets one status field to `0x1000`, and returns an index carrying tag `0xf1000000`. The complete recovered instruction body agrees with this arithmetic and stores. This supports an event-allocation interpretation; it does not show that enabling, delivery and waiting are interchangeable.

Evidence: pseudocode `ev_128252a3de7a207a55755f43452e963a9470a65013b8bd99b5d2ca5be6e00c26`; complete recovered body `ev_35f036afe065bca83af9dca8b899aa0a06a5b9a69cb769a29e34130d39365ad0`.

**Native design implication:** Preserve allocation failure, handle identity, callback identity and lifecycle state separately. Opening an event must not manufacture an occurrence or run a callback. A numeric handle is a source identity, not a host pointer. Determine whether the particular game path uses events before implementing this as a compatibility requirement.

## Thread allocation

**Observed:** ROM routine `0xbfc11b18` obtains its table pointer from `0xa0000110`, asks a helper for a slot, preserves `-1` failure, and uses `0xc0`-byte records. A successful record receives state values `0x4000` and `0x1000`, two copies of the second argument, and the other caller inputs; the returned handle carries tag `0xff000000`. These are instruction-checked firmware observations. They support a thread-creation interpretation; actual scheduling and all saved-register meanings need the context-save/restore paths.

Evidence: pseudocode `ev_6f122ee6eaf45a4ebd80d9cbb95286e1ee82214ff8729f19cf47e7040dbd69ab`; complete recovered body `ev_5b82e1e951e1ae908cf5a9f3a321566a2ed62dc98f07175c40647cfb03069753`.

**Native design implication:** A source task is a logical register/stack/continuation context. These observations do not establish a requirement to use Windows threads, nor permission to resume a task with invented unknown register state. Creation, activation, context change and release need separate evidence and tests.

## Exception discrimination

**Observed:** ROM routine `0xbfc11500` reaches the current context through `0xa0000108`, masks the saved cause field with `0x3c`, treats zero separately, and recognizes `0x20` as another branch. In that second branch it advances a saved PC field by four and uses a saved selector to choose among four entries in a low-RAM table at `0x6c60`. An out-of-range selector follows a different error/event path. The low-RAM table and callback targets require the relocated profile; the ROM import alone does not resolve them.

Evidence: pseudocode `ev_eea4d8ce85e26882e7adba1f73def0ea05b04d2807ff2a548c04b02930b89e21`; complete recovered body `ev_0bd6773fbd9ad001167a06da55df93496d4e38c57fee198e71b70b4bffa5cf11`.

**Inference:** The `0x20` path is consistent with MIPS syscall exception discrimination, and the zero path with an interrupt exception. This function alone is not the complete exception entry, branch-delay exception treatment or return-from-exception contract. Verify those through the save/restore entry and instruction semantics before deriving an adapter.

## External context and provenance

Sony's August 1998 [Operating System manual](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/os.pdf), printed pages 2-6 and 3-3, describes a table of system tables at `0x100`, including task and event management, and distinguishes event and thread services. It treats threads as register, stack and CPU-state contexts. This is useful corroborating terminology, not proof of this firmware's exact implementation or MML1 use. The Sony-authored document is hosted on an archival mirror and marks itself confidential for licensed developers. No source code or manual text is reproduced here.

## Low-memory dispatch recovered from the copied kernel

**Observed with a separate static profile:** A private slice of source offsets `0x10000` through `0x18bef` was mapped at physical analysis address `0x500`. This models the installer-observed copy destination `0xa0000500` through its RAM alias. It neither executes the copy nor supplies live RAM, device state or the A0 table installed separately. Offset zero of this derived input therefore corresponds to original ROM offset `0x10000`; add `0xfb00` to a low-memory address for its original ROM offset. The slice is 35,824 bytes; SHA-256 `af3a156ada0cc06777f205ed47bcda257a53a798deca91610f426916147074b2`.

The copied stubs at `0x510`, `0x520` and `0x530` enter dispatchers at `0x5c4`, `0x5e0` and `0x600`. The installer places those stubs at service gates `0xa0`, `0xb0` and `0xc0`. They index pointer tables using a selector in register `t1`, scaled by four: A0 uses base `0x200`, B0 `0x874`, C0 `0x674`. This is a table indirection boundary; the gate address is not a unique service identity. The A0 table's separate installation is covered by the startup analysis.

Selected bindings are enough to identify the investigated behaviors: B0 selector `0x07` reaches event delivery at `0x1b44`; `0x08` reaches event allocation at `0x1d8c`; `0x0e` reaches thread allocation at `0x2018`; `0x17` reaches context restoration at `0xf40`; and `0x20` reaches event undelivery at `0x1c5c`. C0 selectors `0x02` and `0x03` reach queue insertion and removal at `0x1420` and `0x1444`.

Evidence: stub bytes `ev_0f17432bfb631039775e3f9e186a88777346f995d0657b66dad3d461ff794243`; dispatcher bytes `ev_2b121b87722336aee4015663c4beb74842c2bc9ffaab2c831e22d0861f80395b`; selected B0 binding derivation `ev_77656636b4ffa128bfe02798e968a3cd5879f9cdb83559ff508d590cbf7be750`; selected C0 binding derivation `ev_93bbaf368a31f66adc7f7ca78bb8870d18af2ebe0a44c0fc2e9a0e5b17fc6321`. Stub installation: `ev_875ea61d642a08484352a659d45d664dfc9ce0664e91aff74731a04ca37d0647`. These are selected original observations, not a published dispatch-table dump.

### Selected A0:49 route and missing live-state proof

Combining those retained stub/dispatcher bytes with the [later table installation](STARTUP.md#low-memory-service-installation) gives a selected static route: the installed A0 gate enters physical `0x5c4`, whose table base is `0x200`. An incoming selector `0x49` selects physical word `0x324..0x327`; its installer source is original ROM offset `0x4424..0x4427`, containing target `0xbfc03fac`. The [wrapper analysis](DEVICES.md#a049-submission-and-a-documentation-discrepancy) then applies conditionally to that target. The selector calculation shifts `t1` in place, leaving `0x124` for this input; the body does not first mask it to eight bits or perform a bounds check. These are static instruction and selected-word observations, not a dispatch-table dump or a captured game-time route.

The minimum live-state join must establish the fetched gate and dispatcher, the selected table word and relevant writes or replacements since installation, including partial writes through RAM aliases. A native interception before those fetches needs its own explicit binding rather than an assertion that guest dispatch was observed. Known caller arguments and an initial BIOS table alone cannot prove the effective target at this occurrence. The existing stub/dispatcher Evidence IDs above support the chain; independent decoding of the digest-checked original bytes corroborates the selected route.

## Event lifecycle and delivery

**REA-decompiled observation:** At `0x1b44`, delivery scans records bounded by the event-table pointer and byte size from `0xa0000120`/`0xa0000124`. Only records with state `0x2000` and matching class/specification participate. For mode `0x2000`, delivery changes state to `0x4000`. For mode `0x1000`, it invokes a non-null callback directly instead. The latter branch does not perform the former branch's state transition. At `0x1c5c`, undelivery changes matching mode-`0x2000` records from state `0x4000` back to `0x2000`.

Evidence: delivery `ev_f59e3438c2c7da1267c2f0386debf9756dc56f86fd2d6ae8dda05be4e6d44eed`; undelivery `ev_a6511e3833a6d9f06681f2c387a30e62fccc0e02ecbd56887ee47d7715c40ea3`.

**Independent instruction interpretation of REA-returned bytes:** Several adjacent service-table targets were not defined as functions by Ghidra. REA returned complete bytes for their selected span; Capstone 5.0.6 independently decoded that span as little-endian MIPS32. These conclusions therefore have a different analysis method from the REA decompiler evidence:

- B0 `0x09`, target `0x1e1c`, clears the selected record's state and returns one: a close/release interpretation.
- B0 `0x0a`, target `0x1e44`, immediately consumes state `0x4000` by setting `0x2000` and returning one. If initially `0x2000`, it repeatedly reads until `0x4000`, then consumes it. Other initial states return zero: a wait-and-consume interpretation. No timeout appears in this recovered body.
- B0 `0x0b`, target `0x1ec8`, consumes `0x4000` in the same way but returns zero without waiting for other states: a test-and-consume interpretation.
- B0 `0x0c`, target `0x1f10`, changes a nonzero state to `0x2000`; B0 `0x0d`, target `0x1f4c`, changes a nonzero state to `0x1000`. A zero state remains zero; both routines return one. These support enable/disable interpretations.

These entry points use the handle's low 16 bits to select a record. The short recovered bodies do not establish validation of tag or bounds. Their numeric success result must not be mistaken for proof of an occurrence or valid allocation. Allocation itself scans for state zero and returns `-1` when no complete slot remains. The record count uses table byte size divided by `0x1c`.

Evidence: selected lifecycle span `ev_1ae84031f0ee7b188fec5f56b88f0282edf5b66b2bb11ab9ad76c410652dbdab`; allocation scan `ev_3efd2cc138d09295fdae3fc69d17942356904655169d63d5be05627f6b5df637`; B0 binding evidence above. No disassembly is reproduced in this note.

**Native contract proposal:** Keep allocated, enabled, delivered and callback modes distinct. Test consumes a pending delivery; wait must allow another execution context to produce the delivery. Translate its logical waiting semantics into an owned native continuation rather than assuming that a host busy loop is required. Preserve callback order and reentrancy explicitly when an identified game path needs them. Invalid-handle refusal can be a named native safety policy; do not claim it is the exact BIOS behavior.

## Threads, critical sections and exception return

**Observed:** The relocated exception discriminator `0x1a00` resolves the four-way table that the ROM view could not recover. Selector one tests saved status bits `0x404`, records a boolean result in the saved return register and clears those bits. Selector two sets them. Selector three replaces the current-context pointer with a supplied context and writes success into the outgoing saved return slot. Selector zero also enters restoration. Unknown selectors follow an event/error path. These support critical-section enter/exit and context-switch interpretations; the exact runtime interrupt consequences still depend on R3000A status semantics.

Evidence: relocated discriminator `ev_8261269138c9f1c72282b7b47c1447a935b1670015789a877e5cc00a580b6fe4`; case-pointer bytes `ev_88d3008dd38f2754e734ab45b8736ebf83847d530fd188b57cf2c93520f6a125`.

The complete recovered body at `0xf40` restores HI, LO, CP0 Status and saved general registers, then jumps to a saved continuation with `RFE` in the delay slot. Ghidra's C-like output renders this as an indirect call; the instruction evidence establishes that ordinary host-function call/return syntax is an inadequate description. Restoration selects the context through the live table-of-tables pointer at physical `0x108`. It is not a blanket rollback of all RAM.

Evidence: `ev_7e6e762829e837e45dc4d3b3dfd816755c919f3c30bf76c788f0392ee34aa5a1`.

Thread allocation scans complete `0xc0`-byte records for first-field state `0x1000` and returns `-1` when exhausted. Independent decoding of REA bytes shows B0 selector `0x0f` at `0x20a8` marks the selected slot `0x1000` and returns one. B0 `0x10` at `0x20d4` builds a context pointer from the handle's low 16 bits and invokes the syscall wrapper with selector three. This supports close-thread and change-thread interpretations without claiming preemptive scheduling or Windows-thread equivalence.

Evidence: free-slot scan `ev_f8ffc44a8bb8a3c82a9677ecea73895cad5e9185d2a1f7276f8fbcf5b978e267`; independent thread-lifecycle decoding from REA bytes `ev_129d3c3deda804f042f01f7f721cba8d28bd481d05401e35bcd374fa180bde63`.

## Interrupt callback chains

**Observed:** C0 `0x02` at `0x1420` prepends the supplied node to a selected list, using the table pointer from `0xa0000100`, and returns zero. C0 `0x03` at `0x1444` searches that list, handles a head removal separately, unlinks a matching node and returns its pointer; a missing match returns null. This demonstrates list order and identity, not just an interrupt-enabled boolean.

Evidence: complete recovered insertion body `ev_5d3ec0532a7c132f613d1601d50b7f3d8d0ee1f2b52d9394812cee64dd413973`; removal body `ev_80e9f7aa60f3329a14f3a2a3df474d37d4484319e6bcd6e2626c85a6f8d39ca2`.

**Proposed validation agenda:** When actual game evidence reaches these boundaries, test insertion order, duplicate/removal policy, callback identity, absent-node removal, nested delivery, interrupt gating, saved-PC restoration, branch-delay cases and exactly-once continuation ownership. This research does not establish which cases the private MML1 prototype already supports, and does not resume its implementation work.
