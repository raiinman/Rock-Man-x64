# Configuration and executable handoff

These are static firmware findings. The game executable and its actual boot configuration were not inspected. ROM addresses use the original profile described in [Evidence](EVIDENCE.md); file offsets subtract `0xbfc00000`.

## Configuration and defaults

Routine `0xbfc06784` constructs disc paths for `SYSTEM.CNF;1` and default `PSX.EXE;1`. The larger setup path at `0xbfc067e8` attempts to open and read configuration into a working buffer, requesting `0x800` bytes. Open failure and a zero read select defaults. A nonzero read is terminated and parsed. The native port must identify its own game revision's configuration; a firmware fallback name is not proof of that disc's executable name. Evidence: `ev_533d40e258cface174d519ae3a55cce20e45bd02b560dce96d1da535222be0ec`, `ev_fe2751fd837d5c5d52e513e9b278f8268d2ae3b8c0f7b53c0a6f0f72c165cf6d`.

The parser front end at `0xbfc008a0` clears three numeric outputs and a boot-path output, then delegates numeric parsing and boot parsing separately. The numeric helper at `0xbfc00944` scans line starts for a matching label, skips classification-table whitespace around an equals sign, and accumulates hexadecimal digits. The separate helper at `0xbfc00b7c` splits the boot specification and argument tail. These are observations of recovered code, not a hardened input grammar or a guarantee about malformed input. In particular, line termination, bounded copying, short reads, negative return values and missing fields need explicit validation before designing a host parser. Evidence: `ev_10ce94b28ad28b25a2ec1879658bf6a916f2b29a348a272d4f50dfddf478fc86`, `ev_6bc3ee441ca9d1ffde45021bd48f389700d2fc95414d4510c3015da6a2e433f5`, `ev_925e80b473357533d81fe1d3f4e0011d74a91ed954b759ea3edece85ce9e3de8`.

## Header and payload are separate stages

The named-file loader at `0xbfc03a18` opens the file and returns zero on open failure. Its helper at `0xbfc03c90` requests `0x800` header bytes, accepts a return greater than `0x7ff`, and copies `0x3c` bytes beginning at header offset `0x10` into an execution descriptor. That helper does not itself compare an executable magic value. This bounded negative observation does not prove that no other layer checks identity.

The caller then requests payload data using the destination and length from descriptor offsets `0x08` and `0x0c`, closes the file, invokes a further helper and reports one. Its returned pseudocode does not check the payload-read return before this success. Thus the static success value cannot be used as proof that a complete payload was delivered. The direct recovered instruction body corroborates the caller sequence. Evidence: `ev_6b7a32a39b4e9ec4ec13a4e3c24aed0b9986473fc03bde47aff4fd11e46536a8`, `ev_400d2291bfe50513879205f7c77c0abe0a7c801936b7b897f445d0e946ce62c3`, `ev_ea49205f3c7cdff993f3aebd6ed9beda66cb9d6d077a011fed76e6ea8a5732b7`.

## Execution descriptor and register setup

Routine `0xbfc03cf0` saves the caller's context, conditionally zero-fills a region, transfers to the descriptor entry and restores caller state if that entry returns. Its pseudocode is useful for broad structure but omits stack and GP setup. Evidence: `ev_21f5036c4939221137fd71118bd78a64ddb551438da53f996cbff07cd4d541c8`.

A separate private check extracted little-endian MIPS instruction fields from original file offsets `0x3cf0..0x3d7b`, verified 30 instruction patterns, and rechecked the whole input digest. A later focused REA query corroborated those findings with the complete 140-byte Listing body, containing 35 instructions: `ev_d392941725a49984d2c8576838595aa9d5521f9027e9de71737d008ed91921e5`. Neither method observed execution. They establish descriptor entry at `+0x00`, GP at `+0x04`, zero-fill address/length at `+0x18/+0x1c`, stack base/size at `+0x20/+0x24`, and saved caller context beginning at `+0x28`. If stack base is nonzero, a signed-add instruction computes base plus size and assigns SP and FP. The entry receives the forwarded caller arguments with GP loaded from the descriptor. A return restores saved RA, SP, FP, GP and S0 and reports one.

The zero-fill loop enters for a nonzero length, subtracts four before each store and repeats while the signed remainder is positive. A negative nonzero length would still enter once. Stack addition can trap on signed overflow. These are reasons to keep untrusted descriptor validation separate from translation of this firmware behavior; they are not recommended host memory semantics. The check did not execute any descriptor or prove alignment, accessible memory, correct sizes or successful application boot.

## Proposed native validation

Bind an actual game artifact to entry, GP, stack, initialized data and zero-fill ranges. Use explicit guest addresses rather than host pointers. Test open failure, partial header, complete header with short payload, impossible ranges, absent configuration and configuration truncation. Keep parsing, data delivery, state initialization and entry invocation separately observable. Select host safety and error policy explicitly where it differs from firmware behavior. None of these proposed tests is a current game implementation result.
