# A0:49 immediate consumer boundary

## Result and scope

A new bounded static inspection of the owner-supplied original game identifies the first caller-side transfer after the historical return: conditional on returning to the historical continuation at `0x8007cc14`, the original caller immediately makes another direct call, preparing its first argument from the current saved register `s1` in the transfer delay slot. The next callee is at `0x8007f6b4`. That callee's body was not inspected in this task.

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

**Parallel task proposed to native development:** identify the native continuation corresponding to the next call and state its minimum required inputs/effects. Research's next bounded question is the selected original callee's entry contract. Any extension must keep its scope and permitted provenance explicit; the completed slice does not authorize native execution, initializer retries or S2 enablement.
