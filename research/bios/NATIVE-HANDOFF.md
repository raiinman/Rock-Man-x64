# Native MML1 research handoff and continuing queue

This firmware investigation supports the independent port with bounded observations and questions. It does not resume implementation work or supersede the [current project handoff](../../docs/status/decisions-and-handoff.md). The game path, source generation and implementation on the other computer were not inspected here.

## What the port agent can use now

| Area | Firmware result | Proposed game-specific validation |
|---|---|---|
| Startup | Kernel copying and boot descriptor initialization are separate from application logic | Identify the actual game's entry, GP, stack and required initialized state; avoid inheriting firmware startup constants without game evidence |
| Service selection | Low-memory stubs and tables carry indexed service requests | Bind each reached A0/B0/C0 caller and selector, argument width, result and side effects |
| Events | Allocation, status, delivery mode and callbacks have distinct roles | Opening/enabling must not create an occurrence; prove callback identity and ordering from the game path |
| Threads/exceptions | Logical contexts, cause discrimination and explicit return sequence | Preserve logical continuation and known register state; host thread creation is a separate design decision |
| CD | Admission, response cause, acknowledgement, notification, DMA setup and recovery are separate | A command ACK or return cannot satisfy completion/data/continuation obligations by itself |
| Graphics | CPU and DMA upload routes and synchronization checks differ | Bind source buffer ownership and completion; do not invent readiness or equate upload with displayed pixels |
| Sound | Selected halfword initialization writes are visible | Resolve the actual game port read/write and owner; these stores do not establish voices, decoding, playback or audible output |
| Input/saves | Relocated code exposes controller/card-shaped serial sequences | Establish actual game requests and persistence lifecycle before designing host input/save behavior |

The current project's sound-related read at source `80079070` remains unbound to physical hardware semantics by this BIOS investigation. The [current project handoff](../../docs/status/decisions-and-handoff.md), updated in `a8b0380`, now attests accepted mode-00 validation after 69 actual Windows cases. Its later graphics/diagnostic continuations have bounded Linux acceptance, with the diagnostic continuation stopping at A0:49 at `8007cc0c`. These are private project attestations, not game execution inspected by this research. The focused [`0x1f801db8` handoff](DB8-BOUNDARY.md) retains the separate physical-behavior and missing-game-slice questions. DB8 research must not be described as the port's current stopping point merely because an earlier stage stopped there.

## Current reference and port-boundary focus

The user selected [PSX-SPX development documentation](https://psx-spx.consoledev.net/dev/) as the default technical reference and authorized direct APEX-2 coordination. Consult relevant pinned pages and corrections first; use Sony archives and original experiments for specific unanswered questions. Match each investigation to the port's latest blocker, preserving the separate meanings of documentation, emulator observations, physical measurement and game evidence.

For the currently published A0:49 boundary, [pinned GPU-function documentation](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/kernelbios/gpu-functions.md) describes `GPU_cw`: synchronize, submit one word to GP0 at `0x1f801810`, and return the synchronization result. Its `gpu_sync` description provides the initial lead. A subsequent [firmware-specific static check](DEVICES.md#a049-submission-and-a-documentation-discrepancy) establishes that this BIOS submits the saved GP0 argument even after a returning `-1` synchronization result. It also exposes a discrepancy: the actual post-DMA status mask selects bit 26, whereas the pinned description says WFEP, currently bit 28. The no-DMA wait does select bit 28. Retained REA instructions and independent decoding agree; neither establishes physical timing or the actual game state.

The next decisive evidence is the effective game-time dispatch binding, prior GP1/DMA state, GP0 parser state and pending completion obligations, joined to the identified caller and result consumer. A known argument or discarded result does not justify dropping command side effects. The [command-zero source review](DEVICES.md#command-zero-lead-and-its-limits) also distinguishes a possible opcode classification from a proved command boundary or side-effect-free service. Preserve stream order; do not equate readiness with a completed image or ordering-table transfer. These are investigation proposals, not an implementation patch or certification of BIOS equivalence.

Continuing Sony-document research is tracked in the [archive coverage ledger](SONY-ARCHIVE-COVERAGE.md). Wider text passes now cover 104 selected PDFs in release 1.8, 116 in 2.0, 115 in 2.1 and all 409 PDF members of the inspected 2.3 container. No verified numeric definition emerged; fetch, text-decoder, image and presentation limits remain explicit. All three Japanese 4.3/4.4/4.6 canonical download attempts returned 401. Public Wayback indexes were retrieved, but have not supplied those archives. Related SPU2 documentation is separate comparison evidence and cannot certify a PS1 adapter.

The focused graphics follow-up inspected all 50 exported slides from the two retained sound presentations and their embedded pictures. No numeric DB8 definition emerged. Voice-volume ranges, tracker-channel controls and key-queue timing remarks remain scoped to those subjects; they do not establish master readback encoding or cadence. The archive ledger records the active-slide checks, rendering limits and remaining presentation gaps.

Following the README's external documentation subsequently found an explicit community definition of the numeric pair. See the [source definition and native boundary](DB8-BOUNDARY.md#explicit-definition-reached-through-the-readme). This is a positive documentation finding; Sony provenance, hardware verification and the actual game's consumer remain separate questions.

## Suggested acceptance cases

These are proposals, not tests run against MML1: failed event allocation; enabling without delivery; repeated delivery and consumption; null/non-null callback; invalid or stale handle; nested critical-section entry/exit; continuation restoration; command rejection before admission; response-phase mismatch; unread response and outstanding IRQ debt; reset recovery without replaying effects; transfer configured but not complete; short executable read; disconnected input; save failure before commit; generation replacement with outstanding work. Link each adopted case to a genuinely reached game path and the selected native policy.

## Continuing research queue

| Priority | Unresolved question | Next evidence and completion boundary |
|---|---|---|
| 0 | Actual current port boundary: A0:49 — documentation lead found | The pinned description and digest-specific firmware check above establish returning-timeout submission and distinct readiness masks. Obtain the actual caller arguments, parser/reaching GPU/DMA state and return consumer before designing a focused diagnostic or native acceptance proposal |
| 1 | Full event lifecycle and callback ordering — partially answered | [Kernel services](KERNEL-SERVICES.md) establishes selected allocation/delivery/wait/test/enable/disable branches. Runtime callback order, reentrancy, malformed handles and game-specific reachability remain open |
| 2 | IRQ chain entry, priority, acknowledgement and return — partially answered | [Interrupt depth pass](INTERRUPTS.md) establishes vector copy, saved context, four-slot traversal and custom/default continuation. Nested faults, dynamic registrations, hardware timing and game hooks remain unresolved |
| 3 | CD reset/unmute/error state transitions — partially answered | [ROM CD lifecycle](CD-LIFECYCLE.md), [decoded submission](DECODED-CD.md) and [saved-state lifecycle](CD-STATE-LIFECYCLE.md) separate software setup, command issue, restoration and selected errors. A static initialization path now exists; unchecked setup calls, live interleavings, remaining states and game-specific reaching conditions remain open |
| 4 | Sound-related interface boundary — partially answered, separate follow-up | [Sound paths](SOUND.md), [primary Sony sources](SOUND-PRIMARY-SOURCES.md) and the [focused boundary report](DB8-BOUNDARY.md) distinguish settings, current observation and output. A community numeric definition and bounded emulator results are available; physical mute/update semantics and the actual game consumer remain open |
| 5 | File/device abstraction — partially answered | [Filesystem findings](FILESYSTEM.md) establishes selected I/O behavior; [diagnostics](FILE-DIAGNOSTICS.md) narrows helper `0x6ae0` to an initial-template formatter/output route. Live dispatch/backend return behavior, complete parsing, backend units and actual game calls remain unresolved |
| 6 | Controller/card lifecycle | Resolve caller buffers, checksums, handshake failures, callback scheduling and persistence boundary beyond selected transaction candidates |
| 7 | RAM installation phases and dispatch completeness | Reconcile initial copied bytes with subsequent table/vector writes; document proven service bindings without publishing reconstructed tables |
| 8 | Unidentified and transformed ROM regions — partially answered | [Staging findings](STAGING.md) establishes nested copies, correct-profile instruction corroboration and a bounded 372032-byte decoded image analyzed by REA. Selected CD/sound paths are documented; the remaining candidate routines, additional media/resources and omitted zero-fill state remain under investigation |
| 9 | CPU/GTE and hardware conformance | Vendor semantics and independently permitted measurements are needed; generic MIPS32 decompilation cannot validate load delays, GTE arithmetic or hardware timing |

## Update workflow

The user authorized continued independent research, subagents and necessary local tools on 2026-10-22; the latest requested update cadence is every half hour. Publish reviewed research batches to GitHub promptly, update this queue with answered/partial/unresolved status, and preserve concurrent work. The existing chat heartbeat continues the research and reports findings, commits, checks and blockers. Its current priority is the port's actual identified blocker, using PSX-SPX first and pursuing specific evidence gaps; `0x1f801db8` mute/update semantics remain a separate open question. It grants no authority to publish original firmware or game content or to resume implementation work.
