# A0:49 immediate consumer boundary

## Result and scope

A new bounded static inspection of the owner-supplied original game identifies the first caller-side transfer after the historical return: conditional on returning to the historical continuation at `0x8007cc14`, the original caller immediately makes another direct call, preparing its first argument from the current saved register `s1` in the transfer delay slot. The next callee is at `0x8007f6b4`. The initial pass stopped before that callee; the bounded entry follow-up below now covers its first helper boundary.

The two immediate continuation instructions neither read nor overwrite `v0`. This is **not proof that the service's numeric result is globally discarded**: the next callee may consume the still-live register. Nor does a return or this transfer establish that GPU work completed. The next concrete evidence question is the callee's input/side-effect contract, including whether it reads `v0` and what it expects from earlier service effects.

## Evidence and verification

The source is the separate game executable identified in the [original-input reconciliation](ORIGINAL-GAME-STARTUP.md#original-input-and-caller-correlation), not the disc boot executable. The selected executable's exact logical byte count and digest were checked against the retained identity receipt. Its own executable header supplies the text mapping; file-header bytes are excluded when locating the caller. Original media remained read-only.

A private 512-byte contextual slice was mapped for static analysis only. REA with Ghidra 12.1.4 verified its complete raw-image mapping, read a complete 40-byte caller window, and decoded the original call, next call and argument preparation. A separate manual instruction-field decode and an independent reviewer corroborated those four caller instructions, including both transfer delay slots. The reviewer verified the contextual slice's retained digest but did not independently hash the entire executable. This is selected-address evidence, not a recovered complete-function or runtime-fetch claim.

A separately bounded 16-byte original-file veneer inspection identifies the first call's target as an A0 gate transfer with selector 49 set in its delay slot. The caller's link address matches the historical return coordinate. This authenticates the **static original-file relationship**, not the runtime low-memory dispatcher, loaded bytes or effective BIOS binding.

The first call's argument-preparation delay slot consumes the value already in `v0` before entering the service. It cannot consume that service's future return. At the historical continuation, the next call instead prepares `a0` from `s1`; the reaching value and preservation of `s1` remain separate obligations.

## What this changes

The immediate caller-side transfer is now identified from original bytes, rather than inferred solely from matching capture fields or native attestations. Earlier public shorthand that the numeric return is discarded should remain an attributed native-project statement; this new narrow inspection alone proves no such global property.

No service fulfillment, ready bit, return value, GPU payload, completion rule or implementation policy has been selected. The original-file observation does not establish actual execution history, full ABI preservation, register validity, parser/FIFO state, GP1/DMA predecessors or current native owner/request identity.

## Provenance and next task

This is original-game static reverse-engineering research, with its source/exposure, mapping transform and prior address-selection dependencies retained privately. REA's generic MIPS32 decoder is an analysis aid; selected MIPS-I fields and delay-slot relationships were independently checked. No code was executed. Original bytes, extracted slices, disassembly and raw evidence remain private. Evidence is not implementation clearance; apply [provenance review](PROVENANCE-REVIEW.md).

**Parallel task proposed to native development:** identify the native continuation corresponding to the next call and state its minimum required inputs/effects. Research's next bounded question is the first helper's entry/side-effect contract and the remaining callee continuation. Any extension must keep its scope and permitted provenance explicit; the completed slice does not authorize native execution, initializer retries or S2 enablement.

## Callee-entry follow-up: first helper boundary

A separate bounded follow-up inspects only the next callee's first six instructions, through its first call and delay slot. Conditional on ordinary nonfaulting execution, the entry allocates 24 stack bytes, saves the incoming `s0` and link value in two word stores, and retains its incoming first argument in `s0`. It then calls `0x80076de4`, setting its first argument to zero in the delay slot. The helper's body remains outside this scope.

For entry stack pointer S, the two stores address S−8 and S−4. Neither aligned, mapped, writable stack memory nor successful stores follow from a file decode. The new link points to `0x8007f6cc`. These are concrete stack/register prerequisites that native continuation mapping must account for, rather than GPU status inferred from the earlier fixture.

None of the six entry instructions reads or writes `v0`. The register is still live when the uninspected helper begins. This narrows the consumer search one boundary further but still does not prove global discard, a complete consumer sequence, GPU completion or an implementable A0:49 service contract.

The same original-file identity was rechecked and a separate private 256-byte contextual slice retained. REA returned the complete selected 24-byte window and corroborated the helper call and zero-argument delay slot. Independent manual and reviewer decoding agreed on the six instructions and stack arithmetic; the reviewer verified the retained slice digest, not the full executable digest. No target was executed, no complete-function extent is claimed and no deeper callee was followed. Original-source and decoder/test-design provenance remain unchanged.

## Subsequent helper result

The separate [helper investigation](A049-HELPER.md) now inspects the first helper and its immediate result consumer. It establishes a bounded direct register-dataflow discard before the old A0:49 value is replaced, and a conditional interrupt-mask interpretation from the original pointer initializer. Earlier statements above describe their narrower completed scopes; they do not override this follow-up or establish global effect-free behavior.
