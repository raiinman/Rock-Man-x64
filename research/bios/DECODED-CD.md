# Decoded-image CD commands 0x0b and 0x0c

This pass concerns the independently transformed firmware image: 372032 bytes, SHA-256 `7920530e46981bab09bef02c72f35964bca25c879a72f3bf1c5313921143fbe7`, mapped at `0x80030000..0x8008ad3f`. REA verified that separate input and mapping. These are static BIOS-frontend observations, not MML1 source facts, live device results or native-port acceptance. The decoded coordinates have no direct linear original-ROM file-offset formula.

Evidence for this profile: `ev_78f80837d85451d3532d2da712775871c1ef5749c85e53f301268d070367ffa1`. The earlier ROM CD report uses a different subject and coordinate profile; similar logic does not make their memory fields interchangeable.

## Normal submission routines recovered

**Observed:** REA defines the routine containing command-byte store `0x80065860` at entry `0x800657c0`; it defines the routine containing store `0x8006591c` at entry `0x8006587c`. Each recovered body is 188 bytes. Their common structure supports normal submitters for numeric commands `0x0b` and `0x0c`, rather than an error-recovery-only interpretation.

Evidence: containing-function records `ev_0c66bf81159518a7d667982fdf78e27f4644cf0905d9674f86cedde16f53e4ec` and `ev_1c82bd7a74201c06a3794c636b62ac34a577286d394510dee5c2d2139f2667f4`; complete instructions `ev_86f70346e7565d0549e7ae2395780eee3599da6834cb5319c844fe74236e911c` and `ev_d539802f93f7c45e5daf47e3286afd0987c7ea819745df3db4d64f86d60ef2f7`.

The current software discriminator is at `0x801130d4`. Current values three, `0xe6` or `0xeb` permit proceeding only when a separate software flag at `0x801130dc` is nonzero. Value `0xffff` also permits proceeding; other values return zero. A rejected path returns before this routine's preparation helper and command stores. This is a software-state eligibility rule, not a universal hardware-ready or drive-idle predicate.

For the three admitted active-state values, the routine stores the previous discriminator into `0x801130d8`. The admitted `0xffff` path does not write that saved slot in the inspected body. Its later value therefore depends on prior initialization and writes; current-idle status alone does not prove a saved-idle value.

## Preparation, command store and returned result

Both submitters next call `0x8006777c`. That helper writes one through a pointer initialized to CD address `0x1f801800`, writes `0x40` through a pointer initialized to `0x1f801803`, and performs four word stores to source address zero with values zero through three. It returns normally. These are actual instruction-level accesses; their hardware control-bit meaning is separate from naming the helper “clear” or “acknowledge.”

After the helper, the submitter writes index zero through the CD index pointer, writes command byte `0x0b` or `0x0c` through the command pointer initialized to `0x1f801801`, and only then writes the new software discriminator. It returns one after those stores. Ordering matters: command publication precedes the discriminator update in these recovered bodies. This is not evidence of a runtime race, because interrupt delivery and execution interleaving were not exercised.

Neither inspected submitter contains a ready-bit polling loop, waits for completion or proves an applied mute configuration. The one result denotes the recovered submission path reaching its return after the stores. It does not establish physical command acceptance, completed unmute, mixer coefficients, decoded audio or audible output.

Evidence: helper instructions `ev_d9d0a176926191493787be4427045050a91a0ac8d011b5ecc01ed850969a4010`; initialized CD pointers `ev_eb2daf480e3f93e840dca63d6dd70137efd759c0734b6630c2d2400f4f31a162`; complete submitter instructions above. The initialized pointers are image observations, not proof that runtime code never changes them.

## A distinct conditional response path

The decoded router at `0x80065ff4` checks permission/assertion conditions through an interrupt-register pointer, selects CD index one, reads a cause value and dispatches its low three bits. Cause three reaches `0x80066328`. These static conditions do not establish an observed interrupt arrival or timing guarantee.

For software states `0x0b` and `0x0c`, that dispatcher reads a response byte through the pointer initialized to `0x1f801801`, stores it at `0x80113140`, and reaches helper `0x800672f8`. The helper copies saved discriminator `0x801130d8` into current discriminator `0x801130d4`, sets the saved slot to `0xffff`, and invokes a B0 selector-seven veneer with arguments shaped as event class `0xf0000003` and specification `0x20`. The helper then returns normally.

The response read, discriminator restoration, saved-slot clearing, notification request and source return are separate actions. The response byte is not interpreted as a verified physical mute state in this selected helper. A completion path restoring saved state also cannot be replaced by unconditional idle assignment without changing the observed behavior.

Evidence: router instructions `ev_ffdd1fe39e08b4a51d6c7f440354a66779a9c8f8d57fe941d6dfb816d331519f`; cause-three dispatcher instructions `ev_b333933491da5a25bb69138e3e58b18d647703742ae2826a03e847aedb21530d`; completion helper instructions `ev_d8a6fc5ac39cdff487a2caa84d42328141b4a6f3807e788eb9d2c2c650f8a165`; veneer instructions `ev_8ebcacf3fe065d195aad392b56da4eb28eca8481bf0cc2f93d0271430e3c943e`. Earlier low-kernel B0-table evidence `ev_77656636b4ffa128bfe02798e968a3cd5879f9cdb83559ff508d590cbf7be750` and event-delivery evidence `ev_f59e3438c2c7da1267c2f0386debf9756dc56f86fd2d6ae8dda05be4e6d44eed` identify selector seven's behavior; this does not show which event registrations are live here.

## An actual frontend caller, with bounded retries

REA reports a resolved direct caller of command `0x0c` at `0x800390fc`. Its recovered body first invokes `0x80068580`; the complete helper instructions set argument A0 to two and execute syscall. The earlier low-kernel analysis interprets selector two as changing saved interrupt-status bits, but this decoded call alone does not prove effective interrupt delivery.

The caller then makes at most nine submission attempts, stopping after a nonzero submitter return or exhausting its counter. The recovered body adds no wait for the later response or notification between those attempts. Thus successful submission and eventual response remain separate even in this identified frontend call path. This routine's return is not proof of completed physical unmute or game boot.

Evidence: caller instructions `ev_872e4270d4f9115058c37e7b21740c1f610c6cb8ee990164eae7c263c14a2115`; syscall helper `ev_f99501cae9535676ac053e9c248fd64de0fd5b681d74cb4113d111a983dac4be`; resolved caller inventory `ev_09bf46ba21acfffc0ab79adaae63f15fe2bc7d2ff1633011c332f21c35eaead1`. The command `0x0b` submitter has no resolved direct caller in its current inventory. That negative result does not exclude indirect calls, table dispatch or unidentified code.

## Native investigation implications and limits

For an identified MML1 dependency, validate submission eligibility and refusal separately from response arrival. Preserve the previous operation's discriminator and the separate flag; record actual saved-slot initialization; model the preparation accesses and instruction ordering; and keep one returned from submission distinct from a later event or source continuation. Host configuration ownership and callback safety remain explicit native policies in addition to these firmware facts.

Still unresolved are complete saved-state initialization across frontend paths, indirect command `0x0b` callers, error/cancellation transitions, concurrent arrivals, hardware timing and the relationship to any game-specific library. The generic MIPS32 profile supplies neither R3000A timing nor devices, and the larger statically zero-cleared RAM range is not synthesized in this payload-only profile. Complete private evidence is not independently reproducible from this documentation-only repository.
