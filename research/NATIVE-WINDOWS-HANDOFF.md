# Handoff to the independent MML1 Windows agent

Date: 2026-10-22. This is a proposed research and engineering agenda, not a finding about MML1's actual implementation. No MML1 executable, disc, assets, codebase, or other computer was inspected in this research session.

## Why PS1 knowledge helps

It explains the contract the original program expected from its machine. Reconstructing the game requires identifying which parts of that contract affect observable behavior. Rebuilding the entire console is a much larger, separate objective. A native game can replace platform services with native facilities while preserving the behavior the game depends on. These are engineering conclusions, not claims that this particular game uses a particular SDK release or feature.

Sony's [Hardware manual](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Hardware.pdf) is an architectural overview rather than fabrication data. Its contents distinguish CPU/memory, graphics, sound, CD-ROM, peripherals, and data expansion. Sony's [Operating System manual](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/os.pdf) separates boot, register/calling conventions, services, and programming concerns including overlays. The [library overview](https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBOVR46.PDF) adds API-level organization. These are Sony-origin archival references on third-party hosts with restricted-source provenance; they are not automatically approved implementation inputs.

## Establish the evidence boundary first

The research library records sources the research team has encountered; it does not certify their suitability for your independent implementation process. Researchers have read Sony document front matter, contents, and selected passages. Do not call this research corpus itself clean room. Preserve the distinction between:

1. The user's own game/console observations and independently written measurements.
2. Source metadata and historically published vendor/standards documents.
3. Sony developer documents marked confidential/licensed-only on archival mirrors.
4. Community specifications whose upstream source provenance may include Sony developer material.
5. Third-party implementations, which are outside the requested construction approach.

The [PSX-SPX homepage](https://psx-spx.consoledev.net/) expressly states that its material includes confidential Sony source/documentation. Treat it as a provenance issue to resolve, not as an automatically independent specification. No legal clearance conclusion is made here.

## A practical sequence

| Stage | Questions to resolve using permitted game evidence | Deliverable / acceptance evidence |
|---|---|---|
| 1. Identity | Which region, disc revision, executable, language, and runtime library family are actually present? | Local hashes, disc/executable metadata, explicit version record. Avoid using a document's date as proof of the game's SDK. |
| 2. Dependencies | Which system services are reached? Which are direct hardware accesses versus library calls? | Evidence-linked inventory with entry point, caller, arguments, result, side effects, and unknowns. |
| 3. Data and arithmetic | Which structures contain addresses, offsets, packed flags, fixed-width values, or fixed-point quantities? | Documented layouts and original test vectors. Separate host pointers from serialized console addresses. |
| 4. Minimal native path | What is required to load one scene and accept one input? | Native executable, assets loaded from user-owned data, repeatable scene entry. |
| 5. Graphics fidelity | Which draw ordering, clipping, texture addressing, color, and blending details change the image? | Matched captures for selected scenes, with differences categorized. |
| 6. Audio/media | What playback, looping, envelope, synchronization, and stream completion behavior is observable? | Audio timing comparisons, repeatable stream transitions, defined error handling. |
| 7. Time and persistence | Which events advance simulation, input, audio, loading, and saves? | Deterministic input replay; scene/save round trips; callback ordering log. |
| 8. Broaden coverage | Which content paths remain unobserved? | Feature matrix and residual unknowns rather than an unsupported completion percentage. |

## Contracts worth testing explicitly

The following are proposed tests and questions. They do not establish that MML1 exhibits each behavior.

- **Integer semantics:** sign extension, arithmetic versus logical shifts, multiplication intermediate width, wrap versus saturation, division boundaries, and conversions between packed values and host types. Make assumptions explicit rather than relying on the host compiler's accidental behavior.
- **Address identity:** a serialized address is data, not a Windows pointer. Determine any aliasing or relocation the program actually relies on. Give every address conversion a documented input domain and bounds check.
- **Geometry:** record the exact input/output relation for transforms, projection, clipping, flags, and depth decisions used by the game. A visually plausible floating-point substitute can still change gameplay or draw ordering. Determine tolerance from evidence.
- **Rendering:** keep submission order observable. Establish what happens at shared edges, outside draw areas, on texture boundaries, with palette changes, and with blending. Decide whether accurate original appearance or an enhanced mode is being validated.
- **Asynchrony:** immediate I/O completion can change callback order and state transitions. A native scheduler should preserve the ordering dependencies actually observed, even when storage is much faster.
- **Audio:** test loop endpoints, voice interruption, pitch changes, music transitions, and sound/video synchronization. Good samples alone do not prove equivalent playback behavior.
- **Input and saving:** separate logical buttons from host mappings; verify pressed/held/released transitions, disconnect behavior where relevant, persistent data layout, failure cases, and scene restoration.
- **Overlays:** distinguish code/data loaded into reused addresses from permanent state. Resolve what must survive scene transitions before translating address-based code into host objects.

## A compact evidence record

For each reconstructed behavior record: ID; game revision; evidence origin; reproduction steps; input; expected output/state; timing/order constraints; confidence; implementation location; regression fixture; unresolved alternatives. Keep proprietary bytes and personal local paths outside public records.

## BIOS supplied to this research session

Read-only filesystem observation: 524,288 bytes; SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`. The user's filename identifies a US v4.1 image dated 1997-12-16. That version label was **not independently authenticated** by content or a trusted hash catalog. A size/hash identifies the supplied file; it does not establish model compatibility or runtime behavior.

The initial discovery pass encountered an offline remote REA tunnel. A later local REA/Ghidra investigation succeeded and supersedes that access limitation: see the [BIOS findings and continuing handoff](bios/README.md). Its content inspection corroborates the trailing version/date banner while retaining the authenticity limitation. The reports cover startup, a copied kernel, selected services and peripheral paths with retained Evidence IDs. No BIOS bytes, disassembly or extracted implementation were committed. Firmware analysis still cannot establish MML1's actual platform dependencies.

## What this handoff does not resolve

The game's actual SDK version, platform dependency set, asset formats, arithmetic fidelity requirements, timing model, and present decompilation coverage remain unknown. The documentation tells us where to investigate; permitted observations of the actual game must decide what to implement.
