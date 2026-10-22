# CD command and response depth pass

## Scope

This pass reuses retained REA evidence for the ROM mapping of firmware SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. It examines instruction-level response consumption and software state around commands `0x0a`, `0x0b`, `0x0c` and `0x0e`. It does not execute a disc command, inspect MML1 callers, prove hardware timing or complete every command lifecycle. All semantic names below are analysis labels; numeric field locations and accesses are observed.

## State fields that must stay distinct

| Location | Observed role within inspected routines | Evidence |
|---|---|---|
| `0xa0009154` | Current software command/state discriminator; values include ordinary command numbers and internal states such as `0xfe`, `0xddd` and `0xffff` | C1, C2, C3, C4 |
| `0xa0009158` | Saved software state, restored by the `0x0b`/`0x0c` cause-three completion helper; independently cleared afterward | C3, C5 |
| `0xa000915c` | Flag changed by selected asynchronous acknowledgements; not established as universal hardware busy state | C2 |
| `0xa00091c8` | Error-recovery latch: zero allows issuing command `0x0a`; nonzero selects a different error path; the inspected cause-two recovery path clears it | C3, C4 |
| `0xa000917c` and `0xa0009180` | Remaining and initial transfer-count fields on the inspected read-setup path | C1 |
| `0xa0009188` and `0xa000918c` | Advancing destination and current-transfer destination fields | C1, C6 |
| `0xa0009190` and `0xa0009198` | Requested mode field and selected transfer word count | C1 |

The current-state slot is not an authenticated operation ID, host capability or complete hardware-state image. Reconstructing native ownership requires game-bound evidence and explicit policies in addition to these firmware fields.

## Acknowledgement reads hidden by decompilation

The cause-three dispatcher at `0xbfc05194` handles current states `0x10` and `0x11` by branching to specialized helpers before its common response read. Other inspected states, including `0x0b`, `0x0c`, `0x0e` and recovery state `0xddd`, pass through a byte read from `0x1f801801` at `0xbfc051e4` before the later command/state dispatch. Some resulting paths do not use that value. Their response access remains real even when the returned pseudocode makes only a state change and helper call visible. This does not prove the hardware supplied a valid response or that a given cause arrived in a live run. [C2, P]

The cause-two dispatcher at `0xbfc05558` performs a byte read into the architectural zero register at `0xbfc05574` before selecting its state case. Its value is discarded; the pseudocode omits the access. A host replacement that performs only the visible state/event assignment would lose this read. The instruction establishes an access, while the device specification is still needed to establish FIFO consumption semantics. [C4, P]

This distinction also prevents a false result-length inference: a byte unused by software is not evidence that the response had zero bytes. These two accesses must be included in any later game-bound response/FIFO trace.

## Commands `0x0b` and `0x0c`: inspected completion only

After the common cause-three response read, both software states `0x0b` and `0x0c` branch to `0xbfc0615c`. That helper loads the saved state from `0xa0009158`, stores it into the current-state slot, clears the saved slot to `0xffff`, and invokes the helper at `0xbfc0d970` with event-class-shaped value `0xf0000003` and mask `0x20`. The helper returns normally. [C2, C5]

The evidence establishes this conditional completion path and its memory-access order. The current corpus does not yet establish the normal submitter's full eligibility checks, exact state-saving order, error result semantics, callback ownership or game return. No physical mute bit, host mixer gain, applied coefficient or audible effect is observed here. The shared completion routine cannot by itself certify that a native unmute operation occurred.

## Command `0x0e`: mode-setting admission and completion

Routine `0xbfc04d50` requires current software state `0xffff`, calls a clearing helper, and records the requested mode before inspecting ready-mask `0x10` at `0x1f801800`. The ready branch writes index zero, the low mode byte to `0x1f801802`, current state `0x0e`, and command byte `0x0e` to `0x1f801801`, then returns one. Its not-ready branch returns zero after the clearing helper and mode store have already occurred. Therefore a zero return does not imply that every earlier software side effect was rolled back. [C7, P]

On a later admitted cause-three path with current state `0x0e`, the common response byte is read and routine `0xbfc061a0` marks current state `0xffff` before calling `0xbfc0d970` with mask `0x20`. It does not restore the saved-state slot in that helper. [C2, C8]

The read-setup routine `0xbfc04c38` also sends command byte `0x0e`, but marks current state `0xfe`, stores transfer count/destination/mode, and selects a word count before checking readiness. This makes command value and operation state separate facts. Its admitted cause-three path selects a different helper at `0xbfc05e58`; the later ROM pass below traces that continuation into distinct read command and transfer states. Returning zero after a failed ready check can leave its earlier count, destination and mode bookkeeping changed. [C1, C2]

## Command `0x0a`: a proven conditional recovery issuer

The cause-five handler `0xbfc057b0` reads two bytes from `0x1f801801` and stores them at `0xa00091b4` and `0xa00091b5` before inspecting the current state. For its special state `0x1a`, it copies a total of four response bytes into a result buffer, clears current and saved state, and calls the notification helper with mask `0x8000`. For its special state `0xccc`, it changes a separate recovery-result field. Those branches do not issue command `0x0a`. [C3, P]

For the remaining inspected error paths, a zero recovery latch causes the handler to set that latch to one, clear saved state to `0xffff`, write CD index zero, issue command byte `0x0a`, and mark current state `0xddd`. A nonzero recovery latch instead clears the latch and current/saved state and invokes the notification helper with mask `0x8000`; it does not issue a second reset through that branch. [C3]

If a cause-three interrupt is subsequently admitted while current state remains `0xddd`, the cause-three dispatcher reads its common response byte and takes a return path without advancing that state. If a cause-two interrupt is then admitted with that state, its initial discarded-value response read occurs, it clears the recovery latch, stores current state `0xffff`, and invokes the notification helper with mask `0x8000`. These are distinct conditional acknowledgement and completion paths in code. [C2, C4]

The static path supports a two-phase recovery hypothesis. It does not prove that a drive always generates both causes, that cause order cannot vary under failure, that reset succeeded physically, or that a game-issued normal `0x0a` shares this recovery policy. The normal initialization issuer is distinguished below; normal `0x0b`/`0x0c` issuance remains unresolved.

## IRQ and response obligations

Before these cause handlers, the parent routine `0xbfc04dec` checks interrupt permission and asserted status, selects register index one, reads the cause byte from `0x1f801803`, acknowledges selected bit groups and then dispatches cause values one through five. Its acknowledgement paths perform actual stores to address zero before downstream response reads. Cause delivery, cause acknowledgement, FIFO read, state change, notification and source return therefore remain distinct observed actions. The firmware does not justify collapsing them into a single host success flag. [C9, P]

The code also permits state-sensitive paths that consume a response without changing the current state. A native implementation must retain the exact reaching state and outstanding obligations instead of inferring completion from response consumption alone. For game-bound validation, record the command issuer, state before admission, all earlier software stores, command-byte store, each admitted cause, every response read including ignored reads, acknowledgement stores, state transition, notification, callback and actual return.

## Additional ROM pass: normal reset initialization

The normal initialization issuer was not defined as a function in the initial Ghidra inventory. A focused REA `read_bytes` window covering `0xbfc048e8..0xbfc04abb` supplies its actual bytes. An independent little-endian MIPS-I instruction-field decoder identifies the entry at `0xbfc04910`, ordinary return at `0xbfc04a98`, and a separate small result-copy routine beginning at `0xbfc04aa0`. These conclusions are derived from numeric instruction fields and branch destinations in the REA byte evidence; they are not Ghidra-produced function boundaries, a runtime trace or an original-source recovery. The private decoder reported 117 decoded words with no unsupported opcode in this window. [N1]

At `0xbfc04910`, initialization clears the result field `0xa00091c4`, recovery latch `0xa00091c8`, and another software field before a system-call veneer. It changes interrupt-mask/status and DMA-interrupt-control words, clears saved state to `0xffff`, sets current state to `0xccc`, clears software flag fields and invokes CD acknowledgement/enabling helpers. Only later does it select CD index zero and write command byte `0x0a`. The polling counter is initialized to 30000; a result field value of one selects return value one, while a result value of two or exhausted counter selects return zero. A failure return does not perform a visible whole-initialization rollback in this region. [N1, C10, P]

The cause-three dispatcher reads the common response byte for current state `0xccc` and returns without completing that state. The cause-two dispatcher reads its initial ignored byte, sets result field `0xa00091c4` to one, and clears current state to `0xffff`. The cause-five dispatcher reads its first two response bytes and sets that result field to two for current state `0xccc`; that selected branch does not clear the current-state slot. Thus the normal initializer has distinct acknowledgement, completion and error outcomes. If the polling loop times out, the loop itself does not cancel a command or drain a response. [N1, C2, C3, C4]

This normal initialization path is different from the inspected error-recovery reset: the normal issuer uses state `0xccc` and caller polling of `0xa00091c4`; the recovery issuer uses state `0xddd`, latch `0xa00091c8` and notification mask `0x8000`. The same command byte `0x0a` therefore does not establish identical software completion policy.

Failure helper `0xbfc0661c` supplies another concrete recovery issuer. It sets the recovery latch, writes two software error/result bytes (`1` and `0x80`), clears saved state, marks current state `0xddd`, selects CD index zero and writes command `0x0a`. It writes synthesized software error bytes as bookkeeping; the static code does not prove that those bytes were read from the drive. [N2, P]

The initializer's system-call veneer at `0xbfc0d960` is separately observed as a system call with selector one prepared in its instruction sequence. Its larger kernel effects require the exception-path evidence and actual reaching state; the normal-reset findings above do not assume a host runtime, a new media owner or physical reset completion merely from that call. [C10]

## Additional ROM pass: command `0x0e` as read setup

At `0xbfc05e58`, the continuation for software state `0xfe` checks software mode bit `0x100`. When clear, it changes state to `0xf6` and writes command six; when set, it changes state to `0xfb` and writes command `0x1b`. Other entering states select `0xe6`/`0xeb` instead. This bit is not transmitted as part of the earlier single low-byte mode parameter; it also chooses a later software-command branch. [N3]

A cause-three response while current state is `0xf6` or `0xfb` sets software flag `0xa000915c` after the common response-byte read. A cause-one response passes through another mandatory byte read at `0xbfc05958` and chooses the transfer helper when either current or saved state is `0xf6`/`0xfb`. The transfer helper described earlier advances the destination and remaining count, configures DMA, and issues command nine with internal state `0xfff` on its final-count branch. A later cause-two path for state `0xfff` clears current state and notifies with mask `0x20`. Those are conditional code paths, not observed sector delivery. [C2, C6, C4, N4]

The cause-four handler independently tests both current and saved read states, conditionally notifies using mask `0x80`, and clears the matching current or saved state. Other states can produce a different notification (`0x200`). Data-arrival handling, command acknowledgement, terminal condition and notification therefore have separate state-sensitive branches. Exact cause timing and complete error ordering remain unobserved. [N5]

## Notification dispatch identity

The helper at `0xbfc0d970` loads vector address `0xb0`, jumps there, and sets selector register `t1` to seven in the jump's delay slot. The instruction sequence binds these apparent event notifications to the B0 selector-seven service, rather than an arbitrary host callback. Kernel table identity and event semantics must be tied to the separately mapped kernel findings. The veneer itself does not prove that an event matched, was enabled or invoked a callback. [N6]

## Coverage of normal `0x0b`/`0x0c` issuance

The deeper pass cross-checked exact references to current state, saved state and the recovery latch, inspected the previously undefined initializer region, and followed the remaining later ROM CD command-access functions at `0xbfc0d600..0xbfc0d7bc`. Those later direct polling helpers select commands `0x1e` and `0x1a`; their pointer table independently resolves to the same indexed CD register range. They do not establish a normal `0x0b`/`0x0c` issuer. [N7-N12]

The current evidence establishes the `0x0b`/`0x0c` completion branches described above. A normal issuer, saved-state preparation, caller-owned success meaning and all error paths for those commands remain unresolved. This is a bounded search result over the identified regions and reference inventory. It does not prove that these commands are absent from the complete firmware, from relocated or staged code, or from a game's own CD library. The native port must not manufacture a BIOS unmute lifecycle from the existence of a completion case alone.

## Remaining boundaries

- Identify and bind any normal `0x0b`/`0x0c` issuer and the caller's saved-state/notification contract.
- Tie normal-init and error-recovery IRQ phases to the relocated kernel exception/router/callback evidence; static branch compatibility does not prove a live phase sequence.
- Preserve the ignored response reads and address-zero stores in instruction-level traces. Decompiler output alone is insufficient.
- Distinguish the normal initializer's software result bytes, actual device FIFO bytes, DMA completion and media data validity.
- Identify game artifact, command issuer, callbacks, required responses and actual source returns before applying these firmware observations to MML1.
- Establish physical drive timing, DMA bus behavior, sector-format rules, timeout units and error ordering from additional suitable evidence; the polling counter is not a calibrated duration.

## Evidence references

- C1: `ev_6373d68ca314377d9738be4d09b10fedea3c01a77fbaa2b5e0ae5fa8fa389266` (read_function_instructions).
- C2: `ev_88ae9400bb2eab53a740bb8c92a5a0f511828d70ee644ddec50396156c1ee894` (read_function_instructions).
- C3: `ev_7e6849de83f47f4453c30a10a49ce1dcca1eeef2048d33669ab18683708e0d41` (read_function_instructions).
- C4: `ev_de5b1ad22bb3623708bcb2fac7fbfc95294bad0cea980124e217462340a0bd33` (read_function_instructions).
- C5: `ev_601da8be3aec49838c586b9b578f8a8feb40dc79cca1b24e21c944d5e7cb420e` (read_function_instructions).
- C6: `ev_80e848422d34eb0d3d7d33154a6a45ef8a14589b47156fcc15140af209d6ff44` (read_function_instructions).
- C7: `ev_cfe5b4a55d4c7f49984ab86af0bb3db17d943d23fcce9ee654bb7c98759f23ae` (read_function_instructions).
- C8: `ev_f1e039d748176c1a72dd0a0d8756f8dac4b93e40672abbe92df7bc1840beba93` (read_function_instructions).
- C9: `ev_c16273bcc4059a63719814c2fb6bbb6ea4578e3785d04c56c25d8cf27d2114b1` (read_function_instructions).
- P: `ev_35aa392f6ffca1e1777686669f3d1b657ab0a65980b96bdde97b709fb77e3c5d` (read_bytes).

- C10: `ev_9e5b798f5755bc43b6b6597e0a054e741528cbffe91b909ea17cd480893a290c` (read_function_instructions, later ROM pass).
- N1: `ev_74b070fdb5003d8136759abf76edb201884434b71a24f46ea12f67760533846e` (read_bytes, later ROM pass).
- N10: `ev_7a2c411ad3c08616a66e8047915766618a4181abcd255ac420b18bfb24c4fec8` (read_bytes, later ROM pass).
- N2: `ev_0c7d5a28e1d7e42a2f216cadc91cf5b3744075e115b20cf801a147a02b2b13d9` (read_function_instructions, later ROM pass).
- N3: `ev_96e845f71e710db0d6752e506521b7c547f2c9bf23c3d69bcac34dfbecf5b129` (read_function_instructions, later ROM pass).
- N4: `ev_afc54fa3af0c4be743b27beca71d2b2c8a36161f8b01d0ec2dc2c6f90855038b` (read_function_instructions, later ROM pass).
- N5: `ev_3cb8ef207872cb8e61fa4e4ebed28835fa6aab9d598e48982615fd52c8163784` (read_function_instructions, later ROM pass).
- N6: `ev_906fa18ce210a48be94fc19582fe2a317c550022601fc1c0f7b7e595159d90e7` (read_function_instructions, later ROM pass).
- N7: `ev_1d2f48cf999b995d2b66b837c7b87787083ece967b350d20400a5aeaac87c581` (xrefs, later ROM pass).
- N8: `ev_359f7310842b0fce1959faf8c0c0926932e4b07962d8757ad07ea6a4f1239544` (xrefs, later ROM pass).
- N9: `ev_b471298bc9859d73e7353704dd45e8a4e63abd3f0f5953f4a63780b634bcf6b1` (xrefs, later ROM pass).

- N11: `ev_d5a5ce3f37b1eaa123051d46e6663d19a08941ab50c1c5dbe16f5b880ea46308` (read_function_instructions, later ROM pass).
- N12: `ev_4a1cb8b7c167ac856761e3341c552e51ebb060408ca0bd127e2c7a92a6a0eab7` (read_function_instructions, later ROM pass).
