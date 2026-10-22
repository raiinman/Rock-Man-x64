# Reset, copied kernel, and bootstrap findings

This is original research prose derived from the supplied 524288-byte firmware, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. Addresses prefixed `0xbfc` refer to the caller-selected ROM mapping. Their file offsets are the address minus `0xbfc00000`. RAM extents below are derived destinations of static copy/clear loops, not captured runtime memory.

The useful native-port result is a separation between machine startup, BIOS service installation, and disc application loading. None establishes that MML1 calls a particular service. The game executable and a runtime trace have not been inspected in this investigation.

## Important analysis limitations

REA used Ghidra 12.1.4 and `MIPS:LE:32:default`, profile digest `0bbf3f2fe69b8dd315230293abd97f3e42a736f36bbee860431e138012accf9e`. This generic MIPS32 language is a decoding superset; modern CP0 register names, default ABI types, and optimized decompiler output are not exact PS1 hardware descriptions. The original profile used in this section maps only the ROM image. RAM, device registers, aliases and copied code do not become runtime state automatically.

In particular, `read_function_instructions` for the reset entry reports a Ghidra function body of only `0xbfc00000..0xbfc00063`, 100 bytes. This is an actual function-boundary limitation, not merely a display page size. The decompiler follows further instructions independently. Selected later addresses return `undecodable` from the Listing-based inspection tool even though their bytes are available and can be decoded separately. This does not prove invalid firmware.

The cache setup and initial register notes below use REA `read_bytes` evidence plus independent little-endian MIPS instruction-field decoding. They must not be attributed to a successful REA instruction inspection. Private full reports contain bytes and pseudocode and are not published with this prose.

## Identification

The trailing ROM banner, beginning at file offset `0x7ff32`, identifies itself as version 4.1, dated 1997-12-16, region marker A. This corroborates the supplied filename but is not an independent authenticity certification. An earlier header at file offsets `0x100` and `0x104` contains words `0x19951204` and `3`, and an early model tag references CEX-3000/1001/1002. These older internal fields should not replace the trailing revision identification or be promoted into an unexplained revision mismatch. Their precise role was not established.

Evidence: `ev_da9eac6c977b8f25f51aa1cb8f85cc95ef9bfb7fc6bcdfa973d7ec200469c5da` (trailing 128-byte read); `ev_2e53f2274439bf70ecebef896af7a66d0ecf75719bec80c930625717cbc30414` (early 80-byte read).

## Reset and initial machine state

At file offset `0x0`, reset begins with an early write to `0x1f801010`, followed by a write of `0xb88` to `0x1f801060`. These are directly present in the initial Listing instructions. The continuation programs additional registers in `0x1f801000..0x1f801020` before normal firmware setup. These constants describe machine initialization; they do not provide a Windows rendering, audio, or scheduling contract.

REA reset pseudocode observes two zero-store loops while CP0 Status contains `0x10000`, followed by Status clearing. Independent instruction-field decoding additionally finds three distinct writes to `0xfffe0130`: `0x804` at `0xbfc00234`, `0x800` at `0xbfc00288`, and `0x1e988` at `0xbfc00364`. The first two disappear from the optimized pseudocode, which retains the final write. Eight consecutive loads from `0xa0000000` at `0xbfc00334..0xbfc00350` also disappear from pseudocode. The lesson is practical: ordinary-memory decompiler optimization can discard device/cache operations; pseudocode is not a complete hardware transaction log.

The first isolated-store pass visits addresses spaced 16 bytes apart across `0x00000000..0x00000ff0`, in 128-byte batches. The second visits every aligned word across `0x00000000..0x00000ffc`, again in 128-byte batches. Both are consistent with cache initialization rather than a reliable claim that ordinary low RAM was cleared. The IDT R30xx software reference explains that Status IsC redirects accesses into isolated cache. Its architecture description supports this interpretation, but it does not establish the PS1-specific meaning of every `0xfffe0130` bit. That register's exact bit semantics and cache timing remain outside this static result.

At file offsets `0x368..0x3a0`, firmware clears numeric CP0 register fields 7, 3, 5, 6, 9, 11, 12 and 13. Generic decoder names such as HWREna, EntryLo1, PageMask, Wired, Count and Compare must not be treated as evidence that those later MIPS facilities exist on the PS1.

The subsequent ordinary-memory zero loop covers uncached addresses `0xa0009000..0xa000c15f`, length `0x3160` (12640 bytes). At file offsets `0x3cc..0x3dc`, independent instruction decoding establishes initial SP `0x801fff00`, GP `0xa0010ff0`, and FP equal to SP. The firmware writes small initialization values at physical `0x60`, `0x64` and `0x68`, and zeros the four halfword locations `0x1f801d80`, `0x1f801d82`, `0x1f801d84` and `0x1f801d86`. The jump at file offset `0x418` leads to the later bootstrap continuation at `0xbfc06ec4`.

Evidence: `ev_ea07b4427aa1f9b88bc836568e91636039cd0f17ae9d7dd128cd27f9300975a0` (initial Listing body and its explicit extent); `ev_1afa9bd91e125b1e3815e38df41b82222a5c22994c817a3b38312f8af92bb338` (reset pseudocode); `ev_cfcb35ebae53d0dfb3e039b77623e021fb8c5d3931c4c8cc973894d7164337a6` (436-byte read beginning file `0x22c`); `ev_172399cc11841079a1c4712957fb5dc44e7711a9b810a86955f0bff2e01c3496` (88-byte read beginning file `0x3cc`). External architecture support: [IDT R30xx Family Software Reference Manual, revision 1.0, 1994](https://cgi.cse.unsw.edu.au/~cs3231/doc/R3000.pdf), chapter 3, Status and chapter 5, cache isolation. This is a manufacturer-authored manual on a university mirror, not a Sony publication or a PS1-specific cache specification.

## ROM-to-RAM installation

The routine at `0xbfc00420`, file offset `0x420`, copies exactly `0x8bf0` (35824) bytes from ROM `0xbfc10000..0xbfc18bef` into uncached RAM `0xa0000500..0xa00090ef`, then transfers control to `0xa0000500`. This is supported by both complete function instruction evidence and pseudocode. Do not confuse the copy destination with a second ROM base. The copied payload contains absolute low-memory references and should be analyzed in its intended RAM address context when possible.

For this one region, a derived correspondence is:

`source file offset = 0x10000 + (physical RAM address - 0x500)`

It is valid only inside the statically observed copied range, and only for the initial bytes before later writes. Runtime execution, relocation success and later contents were not observed. Cached and uncached aliases share the proposed physical destination by architecture interpretation; the analysis does not capture a running alias map.

The initial copied entry at physical `0x500` contains an indirect transfer to physical `0x598`. At the corresponding ROM source offset `0x10098`, an independently decoded loop clears physical `0x7460..0x891f`, length `0x14c0`, then returns. At source offset `0x10040`, a helper copies `0x28` bytes from physical `0x93c..0x963` to `0x200..0x227`, followed by `0x10` bytes from `0x964..0x973` to `0x2ec..0x2fb`. These are initial source-byte interpretations; a later initialization phase overwrites a wider table region, so they are not a final post-boot RAM map.

Evidence: `ev_734d7a1596cf41cff422cd1d76f1e3d49e9ba22d7bece81515f73ca337a5754e` (copy pseudocode); `ev_7c1ebfe940a01d2e231363c64aa157563ee61f64ba4a55f34ffca5b9ee93610f` (complete 60-byte function instruction body); `ev_ef3a558d61dc18e9afee2482ed389cc1047dd53fd77a03548f95ec3c3ec00e8f` (384 source bytes beginning offset `0x10000`, independently decoded).

## Low-memory service installation

Routine `0xbfc042a0`, file `0x42a0`, copies 48 bytes from RAM `0xa0000510..0xa000053f` into physical `0x000000a0..0x000000cf`. This establishes three contiguous 16-byte dispatch stubs at A0, B0 and C0. The copy itself is directly observed; assigning a specific service to a selector still requires table and target analysis.

Routine `0xbfc042d0`, file `0x42d0`, copies ROM words beginning `0xbfc04300` up to the exclusive bound `0xbfc04604` into RAM starting at physical `0x200`. The observed transfer is `0x304` (772) bytes and ends at physical `0x503`. Do not turn that extent into a claim of 193 documented services: the loop's boundary is a copying fact, while table structure, aliases and spare/overlapping words require separate analysis. It also demonstrates why the initial copied RAM image is not permanent: this copy reaches the original entry word at physical `0x500` after that entry has already been used.

Evidence: `ev_875ea61d642a08484352a659d45d664dfc9ce0664e91aff74731a04ca37d0647` (stub copy); `ev_fd17c375398dc1b1e9622f860b5d31e14f1fadbd91468a59c490e374b2436ae8` (table copy).

## Bootstrap paths and optional expansion entry

The startup continuation checks an expansion-region identifying string at `0x1f000084`. When the comparison succeeds, a helper calls the function pointer stored at `0x1f000080`. This is an optional firmware-controlled path. Static examination does not establish whether the user's physical hardware has such an expansion device.

The helper at `0xbfc01a60` writes a one-byte progress value to `0x1f802041` and invokes another helper. Its small integer callers are therefore progress instrumentation, not ordinary BIOS service selector numbers.

The boot preparation routine at `0xbfc06784` constructs disc paths for `SYSTEM.CNF;1` and a default `PSX.EXE;1`, then enters the larger routine at `0xbfc067e8`. That routine installs the copied kernel, installs low-memory dispatch data, resets interrupt/device state, initializes working structures, and attempts a setup-file read. It requests at most `0x800` bytes into a firmware buffer; if opening fails, or the read produces zero, it selects defaults and a default executable path. A nonzero returned count causes buffer termination and parsing; negative-return behavior was not validated. The observed parser recognizes fields corresponding to thread/event/stack configuration and a boot path; the full malformed-input behavior has not been validated.

The executable-loading helper at `0xbfc03a18` opens a named file, delegates header processing, then reads payload into the destination and size fields returned by that processor. It closes the file and calls another helper before reporting success. The caller later passes the resulting execution descriptor through `0xbfc0d570` toward `0xbfc03cf0`. The header helper at `0xbfc03c90` requires a full `0x800`-byte header read and copies `0x3c` bytes beginning at header offset `0x10` into the execution descriptor. This helper does not itself check an executable signature. The execution helper at `0xbfc03cf0` saves caller context and zeroes the address/length pair at descriptor offsets `0x18`/`0x1c` in word steps when the length is nonzero, before calling the entry pointer. Pseudocode alone omits initial stack and GP setup: independent instruction-field decoding of file offsets `0x3d28..0x3d5c` shows that a nonzero descriptor field at `+0x20` makes SP and FP equal to that field plus the field at `+0x24`; the entry comes from `+0x0` and GP from `+0x4`. A return restores saved caller context. A separate receipt verified 30 instruction-field patterns against the full input digest across file offsets `0x3cf0..0x3d7b`; a later complete REA Listing body corroborates this independent decoding (`ev_d392941725a49984d2c8576838595aa9d5521f9027e9de71737d008ed91921e5`). Neither method observed runtime execution. The stack addition uses signed-overflow-trapping ADD. The zero-fill branch enters for any nonzero length and repeats while the remaining signed count is positive; malformed sizes are not proved safe. Do not infer successful boot, valid BSS bounds, malformed-file handling or the actual game entry from these helpers. There is no evidence here that the MML1 disc layout or startup configuration matches the default path.

Evidence: `ev_0661695b9e6772af62f70f90b9834a0c285d94b42660dbc2e3201def6764d874` (expansion comparison); `ev_9ab93aa3d1fac2b6d9ac52c3dd33f219a4ff12bbad74a49317ae6b743b3d329a` (expansion indirect call); `ev_796367124c5c66e028dc33e70904b2be13ff8a4b571b39d1140954d8f459d151` (progress output); `ev_533d40e258cface174d519ae3a55cce20e45bd02b560dce96d1da535222be0ec` (boot paths); `ev_fe2751fd837d5c5d52e513e9b278f8268d2ae3b8c0f7b53c0a6f0f72c165cf6d` (boot setup); `ev_10ce94b28ad28b25a2ec1879658bf6a916f2b29a348a272d4f50dfddf478fc86` (configuration parser front end); `ev_400d2291bfe50513879205f7c77c0abe0a7c801936b7b897f445d0e946ce62c3` (named executable loader); `ev_465ed4c62b7306e1e42357ab6df18dbc8a7f12e3a8c02711cba4bd8e76876f0b` (handoff wrapper); `ev_6b7a32a39b4e9ec4ec13a4e3c24aed0b9986473fc03bde47aff4fd11e46536a8` (full-header read and descriptor copy); `ev_21f5036c4939221137fd71118bd78a64ddb551438da53f996cbff07cd4d541c8` (execution descriptor and context pseudocode).

## Proposed work for the native MML1 implementation

- Identify the actual game's executable entry, GP, initial stack, BSS range and boot configuration from game-specific evidence. The firmware stack `0x801fff00` is not automatically the game stack.
- Inventory actual calls into A0/B0/C0 and direct hardware accesses before implementing host services. Firmware presence establishes availability, not game usage.
- Translate required guest addresses, data layouts, selector values, return values and callback ordering into explicit Windows contracts. Address aliases matter where game data stores guest pointers; they do not imply that hardware cache initialization must be replayed on Windows.
- Keep host startup distinct from guest firmware boot chores. The native application can initialize its own services without reproducing expansion probes, ROM copying or cache-isolation loops, unless specific game behavior proves an observable dependency.
- Validate configuration and executable parsing with small independent fixtures before applying findings to original game data. Treat parser failures, short reads, bounds and descriptor initialization as separate test cases.
- For any claim about interrupts, cache effects or boot completion, obtain runtime evidence on an appropriate PS1 target or independently justified hardware instrumentation. This static corpus supplies locations and hypotheses, not that validation.
