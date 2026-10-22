# Evidence, analysis profiles and coverage

2026-10-22. The public reports are original prose and evidence metadata. The complete REA records and independent decoding receipts remain private because they contain or derive from supplied firmware. An Evidence ID is a retained-record identifier, not a public download or an independent authenticity certificate. These private results cannot be reproduced from this documentation-only repository without separately supplied authorized input and tools.

## Input identity and profiles

The original input is **524,288 bytes**, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. Its trailing banner corroborates version 4.1, 1997-12-16, marker A. Content self-identification does not authenticate manufacturer origin or model compatibility. Earlier internal revision fields are discussed in [Startup](STARTUP.md).

Analysis used the installed [REA fork](https://github.com/raiinman/rea/tree/96d82e3550b488de843fe9b64ef2a9e52ed14bc1), Ghidra 12.1.4, BinaryLoader, `MIPS:LE:32:default`, default compiler specification and default analysis. The raw loader does not discover these choices from a header; they are explicit investigation inputs.

| Property | Original ROM profile | Derived kernel profile |
|---|---|---|
| Input | Complete supplied firmware | Private exact slice from original offset `0x10000`, length `0x8bf0` |
| Input SHA-256 | `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278` | `af3a156ada0cc06777f205ed47bcda257a53a798deca91610f426916147074b2` |
| Imported extent, exclusive end | `0xbfc00000..0xbfc80000` | `0x500..0x90f0` |
| Seed entry | `0xbfc00000` | `0x500` |
| Ghidra analysis-profile digest | `0bbf3f2fe69b8dd315230293abd97f3e42a736f36bbee860431e138012accf9e` | `b7f73fb28e17b7a4174edfd3465561c301b9938d83b3ad87f171c3fa4687b6cb` |
| Defined procedure inventory | 328 | 111 |
| Defined string inventory | 106 | 17 |
| Load-image Evidence | `ev_66897ec8c4eba93fde08b6b040c3ab079c7ce37f1da988ee4e5ca40d44fec4f6` | `ev_3e52a92396a17aae7a11604024c66010adbb23ff6a82aae7ab28cc79c66b2a0c` |
| Overview Evidence | `ev_fde33245e6f28ca8523a7a158da8756f33c20eda3f433cf2323c427761cfb5ee` | `ev_b81e6c84f1dfcc509b4d5155db21642a795691431b65000324b07509751966bd` |

REA's overview is a composed workflow with its own profile digest wrapping the underlying Ghidra profile. The digests above identify the underlying provider parameters. Ghidra's separate image-base field is zero; the observed memory blocks above establish the actual imported coordinates.

The derived mapping follows the installer-observed uncached destination `0xa0000500` through the physical RAM alias, so embedded low-memory pointers resolve. It is an **analysis construction** containing initial source bytes. It supplies neither actual RAM nor later installed tables, vectors, device state or a runtime trace. For an address inside this copied region only, original file offset equals physical analysis address plus `0xfb00`. Subsequent writes can invalidate the initial-byte correspondence at runtime.

## Methods and evidence classes

REA provided inventories, pseudocode, exact-address references, byte reads, load-image checks, selected instruction inspections and recovered function instruction bodies. Three parallel agents investigated startup, kernel services and devices; a coordinator reviewed coverage and publication. The first ROM pass queried 110 distinct procedure addresses; this is query coverage, not 110 completely understood routines. The derived profile adds context for overlapping source code and previously unresolved relationships; its counts must not be added as unique BIOS functions.

Supplemental checks independently extracted MIPS instruction fields for reset and executable handoff. The latter verified 30 selected instruction patterns against the original digest. Kernel lifecycle spans lacking Ghidra-defined functions were independently decoded from REA-returned bytes with Capstone 5.0.6. These methods are identified at their conclusions. Capstone's MIPS32 decoding is also a superset; numeric instruction fields and MIPS-I context still need review. Independent decoding does not convert a failed REA instruction inspection into a success.

The [cited evidence index](EVIDENCE-INDEX.md) maps every cited retained record to its actual operation and subject profile. Full records contain private paths and source bytes and are intentionally excluded. The original input digest was checked before analysis; later verification and cleanup are recorded in [Validation](VALIDATION.md).

## Limitations that affect conclusions

- **Defined inventory is partial discovery.** Procedure/string counts concern Ghidra definitions, not every valid routine/string. Missing exact-address references do not prove missing behavior. The serial-reference difference between profiles is a direct example.
- **Function boundaries can be misleading.** The reset Listing body contains only 100 bytes although pseudocode follows later code. Several valid service targets lack defined functions. A bounded instruction body is not a complete control-flow proof.
- **Pseudocode omits accesses and machine state.** Reports demonstrate folded intermediate writes, repeated loads, zero-register device reads, SP/GP setup and a misleading call representation of exception return. Treat it as an analytical aid.
- **No exact PS1 execution semantics.** The generic MIPS32 language does not establish R3000A load delays, precise exception timing, cache effects, PS1 GTE/COP2 semantics or peripheral behavior. The [Ghidra 12.1.4 MIPS definitions](https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_12.1.4_build/Ghidra/Processors/MIPS/data/languages/mips32Instructions.sinc) describe the analysis language, not console hardware.
- **No machine execution.** No BIOS boot, physical device transaction, game path, rendered frame, audible output or Windows runtime behavior was observed. Runtime-dependent conclusions remain unresolved.
- **Provenance is explicit.** Firmware was user supplied. Sony developer manuals are archival, restricted-provenance context; manufacturer architecture references are not PS1-specific measurements. No other game port, decompilation or emulator implementation was used as construction input.

## Coverage state

Startup/copying, selected dispatch bindings, event lifecycle, thread allocation/change, exception discrimination/return, IRQ list edits, CD/GPU access paths and selected serial transactions are **partially answered static scopes**. Complete exception entry/priority behavior, complete CD lifecycle, sound semantics, filesystem layering, transformed code, GTE arithmetic and all timing are **open research scopes**. MML1 dependency mapping is **unresolved without identified game evidence**. Follow the [continuing queue](NATIVE-HANDOFF.md) rather than interpreting this batch as exhaustive BIOS coverage.
