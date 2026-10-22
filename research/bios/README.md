# PS1 BIOS investigation for the native MML1 effort

2026-10-22. REA with real Ghidra analysis, three parallel research agents, and a coordinating evidence review. This is a substantial static investigation of the supplied firmware, with explicit remaining gaps. It does not inspect the private game prototype or establish MML1's BIOS dependencies.

Start with the [native handoff and continuing queue](NATIVE-HANDOFF.md). It connects firmware findings to proposed validation cases without changing implementation work.

| Report | What it establishes |
|---|---|
| [Startup and bootstrap](STARTUP.md) | Reset setup, decompiler omissions, copied kernel, service installation, optional expansion path and disc boot preparation |
| [Kernel services](KERNEL-SERVICES.md) | Dispatch, event/thread records, exception discrimination, critical sections and context return; evidence classes remain separate |
| [Interrupt entry and continuation](INTERRUPTS.md) | Vector installation, saved context, four-slot callback traversal, custom/default continuation and branch-delay gaps |
| [Peripheral paths](DEVICES.md) | CD admission/interrupt/recovery/DMA, GPU transfer/synchronization, sound initialization, controller/card candidates |
| [CD command lifecycle](CD-LIFECYCLE.md) | Normal reset versus error recovery, mode-setting/read continuation, ignored response reads, persistent partial side effects and unresolved mute/unmute issuers |
| [File and device I/O](FILESYSTEM.md) | Descriptor ownership, lookup, callback dispatch, cursor/alignment behavior, failure semantics and unchecked loader results |
| [Further firmware staging](STAGING.md) | A second large copy, nested loader coordinates and the bounded packed-data transformation lead |
| [Executable loading](BOOT-LOADING.md) | Configuration parsing, header/payload stages, execution descriptor and limitations of success returns |
| [Evidence and coverage](EVIDENCE.md) | Artifact identity, two static profiles, retained evidence provenance, reproducibility and open coverage |
| [Validation record](VALIDATION.md) | Publication checks and their limits |

## Findings that change the investigation

1. Startup copies **35,824 bytes** from ROM into RAM and later overwrites some initial kernel bytes with dispatch data. A ROM-only address model misses important kernel and input relationships.
2. The derived RAM mapping exposes event delivery, thread allocation and exception/context paths. Opening an event, enabling it, delivering it and consuming an occurrence are different operations.
3. CD admission, response handling, interrupt acknowledgement, notification, transfer configuration and recovery occupy distinct paths. A successful admission return is insufficient evidence of completed I/O.
4. Pseudocode loses meaningful operations: intermediate cache-control writes, repeated reads, discarded-value device loads, and execution stack/GP setup. Instruction extents and independently checked fields matter.
5. The trailing banner corroborates version 4.1 and date 1997-12-16. Older internal fields also exist. Neither a banner nor a successful decode authenticates the image.

These are firmware findings and research implications, not a claim that every PS1 subsystem is understood or that the native game boots. The public reports contain original prose and metadata; BIOS bytes, derived images, raw evidence, disassembly and copied implementation are excluded. Independent implementation is the project's constraint; this research is not legally certified clean room.
