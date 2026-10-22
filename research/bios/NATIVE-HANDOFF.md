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

The current project's sound-related read at source `80079070` remains unbound by this BIOS investigation. The [peripheral report](DEVICES.md) cannot establish its semantics, reaching state or acceptable host return. Preserve unknown values until actual evidence resolves them.

## Suggested acceptance cases

These are proposals, not tests run against MML1: failed event allocation; enabling without delivery; repeated delivery and consumption; null/non-null callback; invalid or stale handle; nested critical-section entry/exit; continuation restoration; command rejection before admission; response-phase mismatch; unread response and outstanding IRQ debt; reset recovery without replaying effects; transfer configured but not complete; short executable read; disconnected input; save failure before commit; generation replacement with outstanding work. Link each adopted case to a genuinely reached game path and the selected native policy.

## Continuing research queue

| Priority | Unresolved question | Next evidence and completion boundary |
|---|---|---|
| 1 | Full event lifecycle and callback ordering — partially answered | [Kernel services](KERNEL-SERVICES.md) establishes selected allocation/delivery/wait/test/enable/disable branches. Runtime callback order, reentrancy, malformed handles and game-specific reachability remain open |
| 2 | IRQ chain entry, priority, acknowledgement and return — partially answered | [Interrupt depth pass](INTERRUPTS.md) establishes vector copy, saved context, four-slot traversal and custom/default continuation. Nested faults, dynamic registrations, hardware timing and game hooks remain unresolved |
| 3 | CD reset/unmute/error state transitions — partially answered | [ROM CD lifecycle](CD-LIFECYCLE.md), [decoded submission](DECODED-CD.md) and [saved-state lifecycle](CD-STATE-LIFECYCLE.md) separate software setup, command issue, restoration and selected errors. A static initialization path now exists; unchecked setup calls, live interleavings, remaining states and game-specific reaching conditions remain open |
| 4 | Sound-related interface boundary — partially answered | [Sound paths](SOUND.md) and [primary Sony sources](SOUND-PRIMARY-SOURCES.md) distinguish selected settings, mode and current-volume concepts. No inspected vendor source binds `0x1f801db8`; the separate game-path read, numeric semantics and owner remain open |
| 5 | File/device abstraction — partially answered | [Filesystem findings](FILESYSTEM.md) establishes selected I/O behavior; [diagnostics](FILE-DIAGNOSTICS.md) narrows helper `0x6ae0` to an initial-template formatter/output route. Live dispatch/backend return behavior, complete parsing, backend units and actual game calls remain unresolved |
| 6 | Controller/card lifecycle | Resolve caller buffers, checksums, handshake failures, callback scheduling and persistence boundary beyond selected transaction candidates |
| 7 | RAM installation phases and dispatch completeness | Reconcile initial copied bytes with subsequent table/vector writes; document proven service bindings without publishing reconstructed tables |
| 8 | Unidentified and transformed ROM regions — partially answered | [Staging findings](STAGING.md) establishes nested copies, correct-profile instruction corroboration and a bounded 372032-byte decoded image analyzed by REA. Selected CD/sound paths are documented; the remaining candidate routines, additional media/resources and omitted zero-fill state remain under investigation |
| 9 | CPU/GTE and hardware conformance | Vendor semantics and independently permitted measurements are needed; generic MIPS32 decompilation cannot validate load delays, GTE arithmetic or hardware timing |

## Update workflow

The user authorized continued independent research, subagents, necessary local tools and hourly updates on 2026-10-22. Publish reviewed research batches to GitHub promptly, update this queue with answered/partial/unresolved status, and preserve concurrent work. The hourly chat heartbeat continues the research and reports findings, commits, checks and blockers. It grants no authority to publish original firmware or game content or to resume implementation work.
