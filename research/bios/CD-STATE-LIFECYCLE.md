# Decoded CD saved-state initialization and lifecycle

This pass concerns the independently transformed 372032-byte firmware image, SHA-256 `7920530e46981bab09bef02c72f35964bca25c879a72f3bf1c5313921143fbe7`, mapped at `0x80030000`. It separates current discriminator `0x801130d4`, saved discriminator `0x801130d8` and admission flag `0x801130dc`. These are software fields, not authenticated operation identities or universal drive status. No firmware execution, completed initialization or MML1 use is established. Decoded addresses have no direct linear original-ROM offset formula.

The retained REA load-image record `ev_78f80837d85451d3532d2da712775871c1ef5749c85e53f301268d070367ffa1` binds this derived subject and mapping. New conclusions use complete recovered REA instruction bodies, cross-checked against independent Capstone 5.0.6 decoding of the same digest-checked artifact. Pseudocode is supporting interpretation; branch delay slots and actual stores control the claims below.

## A concrete static initialization path

**Observed:** The retained entry body calls `0x80035c34` at instruction `0x800300b8`, supplying a buffer at `0x801231d8`. That setup routine constructs two interrupt-chain nodes and installs both in slot zero. It requests six event allocations under class `0xf0000003` using mode `0x2000` and null callback arguments, stores their returned handles, requests enabling for each and then calls `0x80064c00`.

The complete 400-byte setup body does not branch on the return values of those registration, event-allocation or enable calls. Reaching its later call is consequently not evidence that all preceding operations succeeded. The verified veneers select C0 `0x02`, B0 `0x08` and B0 `0x0c`; the earlier kernel investigation supplies the corresponding queue-insert, event-open and event-enable interpretations.

Evidence: entry instructions `ev_88b3efcbdee0e085328ab0f070bfdd3c3e14133e2901bde0c13a38b255afbbc4`; setup instructions `ev_05d6d4a8c269480658a75fbb733267f455d4b57ba4057f17ff116476a0f46c5b`; setup caller inventory `ev_0797ea0389a87995c46e1b9b3fb9b87ca1e46b0c5d1803981f2c9a4e81e8cfaa`; veneer instructions `ev_8c773b5e21a79f20ea4f5e5dab3fbbd7e439ac14aaa409b8b050bf6616202d38`, `ev_2d84bdd29a4366033b4d6a490493311cf7ad3ccd48925088ab1cb183274d09da` and `ev_bc9bdd32b323261e1c48ff04130524a1db1af0d030ae6cc12a690b00a81dd7d1`.

Software initialization at `0x80064c00` writes saved discriminator `0xffff` at `0x80064c8c`, current discriminator `0xccc` at `0x80064c98`, and zero to the admission flag at `0x80064cac` in a call delay slot. It also resets selected result/recovery fields and performs interrupt/DMA-register-pointer accesses. Its helper at `0x800662b4` writes CD index one, value `0x1f` through the CD offset-three pointer and four words to source address zero. Helper `0x80066290` writes index one and `0x1f` through the CD offset-two pointer.

After those helpers, additional register-pointer stores and the previously identified syscall-two veneer, the inspected software initializer writes current `0xffff` at `0x80064d00` and returns. It does not separately rewrite saved at that final store. The setup body does not inspect helper return values or verify a device completion. No command `0x0a` store occurs in this recovered initialization body or the two inspected helper bodies. This is software-state/interface setup, distinct from the separately documented ROM reset issuer.

Evidence: initializer instructions `ev_9376b2606b01c5406301dbfa089af9575bfdf5b546285d78fd1eaaf14146ec75`; helper instructions `ev_3360ad5e6986cc2b2041735288c8260f88ab53f2c964ec6a0acf646efc84798a` and `ev_8e4dbbe174edefe3e41f05e0c7b7f13551f042bb54100d66548d3c285c2a7328`; syscall-two veneer from the earlier decoded pass `ev_f99501cae9535676ac053e9c248fd64de0fd5b681d74cb4113d111a983dac4be`.

This establishes a static path that can initialize both saved-idle and current-idle. It does not prove that the path executed, that interrupts cannot change fields along it, or that every later caller inherits those values. The payload-only REA mapping does not synthesize its larger statically cleared RAM region.

## Overwriting saved state is operation-specific

The earlier complete bodies of command `0x0b`/`0x0c` submitters save current only for admitted active states three, `0xe6` or `0xeb`; their admitted current-`0xffff` path does not overwrite saved. The selected completion helper restores current from saved and then clears saved. This makes the initializer relevant while leaving current-idle and saved-idle as distinct facts.

Evidence: submitter instructions `ev_86f70346e7565d0549e7ae2395780eee3599da6834cb5319c844fe74236e911c`, `ev_d539802f93f7c45e5daf47e3286afd0987c7ea819745df3db4d64f86d60ef2f7`; completion instructions `ev_d8a6fc5ac39cdff487a2caa84d42328141b4a6f3807e788eb9d2c2c650f8a165`.

Two additional command-two submitters differ in admission breadth. Routine `0x80064d28` accepts current `0xffff`, or `0xe6`/`0xeb` when the separate flag is nonzero. Routine `0x80064e24` additionally permits active values three, four and five when the flag is nonzero. Both also require a numeric `0x08` gate read through the CD index/status pointer before saving an admitted active discriminator. They then prepare the interface, write three parameter bytes, issue command two and mark different internal states, `0xf2` and `0xe2` respectively. A failed numeric gate returns zero before the saved-state store in these inspected paths. The meaning of that hardware bit is not established here by the name “ready.”

Evidence: complete instructions `ev_c0c02443555cdda6bba06b0ff5520e631f5d83475d91f81f4dad494a35117a01` and `ev_bfa3f4d218d921653d17de842edf1142ab9e3350934267f7e38e883655353f51`. Ghidra warns about overlapping instruction representations around `0x80064db4` and `0x80064ee4`; the eligibility and store-order conclusions were checked against the complete instructions and independent decoding rather than taken from C-like output alone.

Mode-command routine `0x80065454` accepts current `0xffff` or three. It stores the requested mode before its numeric `0x08` gate. On the admitted branch it first stores the selected current discriminator, calls the preparation helper and reloads current at `0x800654c8`. It writes a parameter byte, stores that reloaded value into saved, issues command `0x0e` and marks current `0x0e`. The reload is a distinct observation point; this pass does not assume current remained unchanged across the helper and intervening execution. Thus it can explicitly save `0xffff`, unlike the idle branches of the `0x0b`/`0x0c` routines. A not-admitted return can retain the earlier requested-mode store. There is no uniform saved-slot update or rollback rule shared by all submitters.

Evidence: complete mode-command instructions `ev_b64d61fa549ab13320737f56b3d9623f21f662c8e64cfbfae3e1ae995e9d674d`.

## The admission flag has its own lifecycle

Read-setup routines `0x80065148` and `0x80065260` clear the flag after their initial software eligibility conditions and before testing the numeric CD gate. They also establish requested mode and other transfer fields before that test. A zero return from the later gate therefore does not establish preservation of every earlier software field. Neither body initializes saved as part of that flag clear.

The earlier cause-three dispatcher sets the flag to one on selected command/internal-state branches, including the active states used by `0x0b`/`0x0c` eligibility. It does not define that flag as an operation ID or universally synchronize every saved/current update. The `0x0b`/`0x0c` bodies themselves do not clear it when saving an active discriminator.

Evidence: complete flag-clearing bodies `ev_ca3f99e774bb5180cc4939a3e7fd17dddbc401bb2331aed5eeb2f072cccc8336` and `ev_d19edf8d396e2a8bb6fe34cfd0d7c7e0e70892c60c88dd17a9f34a7641eaca59`; earlier dispatcher instructions `ev_b333933491da5a25bb69138e3e58b18d647703742ae2826a03e847aedb21530d`.

## Response and error handling do not share one clearing rule

**Observed:** In the decoded cause-two routine at `0x800666d8`, selected states eight, nine, `0x15` and `0x16` clear saved only when it contains one of three, four, five, `0xe6` or `0xeb`; they then set current `0xffff` and notify. Other inspected branches can set current `0xffff` without writing saved, including the special `0xccc` result path and the generic completion path. These are conditional branch facts, not proof that every possible incoming saved value is reachable in a valid run. They nevertheless prevent deriving a universal “current idle implies saved idle” invariant from a current-field store alone. The complete instructions also show an entry response-byte read that is absent from much of the pseudocode's effective data use.

Evidence: complete cause-two body `ev_f61d61980f36ab841f97a8c235178f4811c295d03428868e9cc5284ea0fdf1b6`.

Cause-five routine `0x80066958` consumes two response bytes before classifying current. Its current-`0x1a` branch collects additional bytes, clears saved and current and notifies with specification `0x8000`. Its current-`0xccc` branch sets a result field to two and current to `0xffff`, without a saved-slot store in that branch. The remaining inspected error branch clears a recovery field, loads saved, clears saved to `0xffff`, restores current from the captured value and notifies with `0x8000`. The final current store is in the notification-call delay slot and precedes entry to the notification helper. Error notification therefore does not uniformly mean idle or discard the suspended discriminator.

Evidence: complete cause-five body `ev_4e483f5a86eaf2566e8d062bc7808c42a125d552c2b25fc926fc7a4bedf3d08a`.

The cause-four routine `0x80066b9c` also distinguishes selected states in current from selected states in saved. Its branches can clear saved while retaining another current operation, or advance current toward idle while leaving other saved values alone. It performs notifications at intermediate points and reloads current after selected notification calls. Accordingly this body is not one atomic “clear both fields” transaction; callback/reentrancy effects require separate reaching-state analysis before claiming a final invariant.

Evidence: complete cause-four body `ev_a86cf9ef6fd7687142f07a5fcaf76873318c63437b8cbe3d6cb8d50b1bb653b2`.

## Normal restoration is also selective

Response helpers `0x80066dc8` and `0x80066e7c` perform different response-copy work before resolving saved. If saved is `0xffff`, they set current to `0xffff`; otherwise they restore current from saved and clear saved. By contrast the `0x0b`/`0x0c` helper at `0x800672f8`, and the separately inspected helper `0x80067374`, unconditionally copy saved to current and clear saved before the same specification-`0x20` notification request. These routines can share a final notification without having identical response work or saved-slot branches.

Evidence: complete response-helper bodies `ev_42998a4d778a07200969e597615fdc7070ece150885b5565db1405340066e5eb` and `ev_2b8346f1307ff456c824053517278cf3667d4587688ac77b593ab59e4d21ec6d`; completion body `ev_0c1f46ba963e21d2d2e629ecac7b527f11bfcf4a7b0d2bddc0953c9f9344c884`; earlier `0x800672f8` instructions cited above. Fields written before notification must not be assumed unchanged after arbitrary synchronous callbacks return.

## Coverage and native validation proposals

An independent whole-artifact aligned-word scan found 88 candidate stores using immediate displacements matching these three fields: 64 current, nineteen saved and five flag candidates. All fell within the selected CD region. Matching nearby high-address construction was only a candidate filter; these counts are not REA-generated complete writer inventories. Computed-pointer stores, bulk clearing, aliases and unidentified code remain outside the completeness claim. The reviewed routines above answer selected lifecycle questions, not every candidate or valid state combination.

For a genuinely reached game path, validate that saved state was initialized by an authoritative setup path, not inferred from current-idle alone. Test active-state save and restoration separately from flag eligibility; gate refusal after earlier stores; cause-two current-only completion; error restoration and notification order; allocation failure before setup; and state changes during callbacks. Preserve logical source fields and host ownership separately. A generation token, safe callback policy or stronger invalid-state refusal is a native design choice in addition to these BIOS observations.

The full analysis and transformed input remain private and are not independently reproducible from the documentation-only repository. Hardware timing, live interrupt interleaving, universal state invariants and MML1 dependencies remain unestablished.
