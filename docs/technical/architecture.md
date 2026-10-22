# Architecture and reconstruction approach

Rock Man x64 targets a native Windows x64 game with an integrated development environment. The current implementation is a collection of native inspection tools, recovered asset and source-behavior subsets, and a bounded startup runtime. It is **not yet a playable game or a complete IDE**. This public repository documents that work; it does not currently provide its private implementation or original data.

Start with [current status](../status/current-status.md), then the [capability matrix](capability-matrix.md). The [service contracts](native-service-contracts.md) explain why a successful local operation is not equivalent to console boot.

## Independent implementation

The project reconstructs behavior from privately supplied original data, static analysis, and independently written native code. The subsequent implementation policy excludes reuse of existing game port, mod or recompilation code and emulator/BIOS implementations. Early platform comparisons did examine external project descriptions and briefly considered an existing recompilation foundation before that direction was rejected. Do not read the implementation policy as a claim that external projects were never examined. It is not a legal certification of a clean-room process.

Static reconstruction identifies bounded functions, data dependencies and control-flow obligations. Reviewed subsets become compiled C++ routines or generated ahead-of-time C++ handlers. Original addresses serve as checked identifiers and provenance, never executable host pointers. There is no general-purpose MIPS interpreter executing the original game instruction stream. Static symbolic bit propagation used to understand a packed-data decoder is analysis, not runtime CPU emulation.

The original executable remains required as private input for verified data, tables and identity checks. Native replacements for platform services use explicit product policies where console behavior has not been established. A native allocator, timer observation or interrupt service is not a BIOS implementation merely because it serves a corresponding source call.

## Layers and data flow

```text
User-supplied original media, kept read-only
  -> bounded raw-sector / ISO inventory and importer
  -> verified immutable data and logical file views
  -> asset readers and statically recovered helpers
       -> diagnostic character / scene inspection
       -> native CPU rasterizer -> Win32 presentation
       -> source-bound editing sidecars
  -> production Session and translated startup continuations
       -> owned native services and partial-knowledge RAM
       -> command / response / IRQ obligations
       -> first unsupported dependency, retained explicitly
```

Diagnostic asset inspection and production startup are separate paths. Successfully displaying a character does not prove that original startup loaded it. A synthetic first-scene checkpoint cannot grant production service authority.

## Media boundary

The native importer reads the supported raw MODE2/2352 Track 1 layout, validates ISO directory structure and extracts selected 2048-byte Form1 payloads into a new destination. It does not accept arbitrary cooked ISOs, archive files or every disc layout. XA/STR media and Form2 content are not silently converted into Form1 files. Source identity and exported-file hashes are recorded; the source is never opened for writing.

Validation and cancellation happen before and during output. Exclusive output creation, rejection of unsafe names and existing destinations, and rollback of owned outputs protect existing files. Power loss may leave a partial new destination. Hostile concurrent replacement of filesystem ancestors is outside the portable importer's threat model. Separate sector-integrity research does not mean the importer performs EDC/ECC repair.

A production raw-media service instead retains one immutable image allocation, owns its cursor and probes actual bounded sector reads. Possessing an imported file tree is not equivalent to possessing this sealed production capability. The independent-native cold-start contract does not infer firmware ownership from the original console.

## Assets and rendering

Independent readers cover tiled textures, local PBD mesh records, packed character poses, sequence updates and a conservative static STG/HED/IDX environment subset. Texture detiling follows the recovered upload traversal rather than the earlier incorrect full-width linear interpretation. Mesh part and joint identities remain traceable to original records.

Recovered character hierarchy and packed pose semantics support diagnostic assembly. Sequence stepping is measured in original update invocations, not an assumed frame rate. The diagnostic transform path uses floating-point approximations and is not complete fixed-point/GTE fidelity.

The software rasterizer is native CPU code. It supports diagnostic textured character rendering, depth testing and inspection overlays. Affine nearest-texel sampling and its transparency policy are explicit approximations, not complete PlayStation GPU blending, wrapping or rasterization equivalence. Static scene inspection uses union geometry rather than claiming the game's exact visibility selection.

## Editor boundary

The Win32/GDI inspector supplies file search, hexadecimal views, images, mesh and scene inspection, pose/sequence controls, per-part or per-instance translation changes, undo/redo and save/reload. These are useful building blocks for the IDE target, not a finished game-authoring environment.

Edits live in sidecars bound to source fingerprints and record identities. They do not patch disc images or original assets. Validation rejects mismatched or incomplete sidecars before changing live transforms. Saves use temporary owned output and atomic replacement; failures preserve the old destination and current edits. The noncryptographic sidecar fingerprint is an accidental-mismatch guard, not a security authenticity guarantee.

## Runtime boundary

A Session owns source identity, generation-tagged RAM, known-bit masks, continuations, service capabilities, interrupt routing and response obligations. It must perform actual work before reporting completion: allocate real heap state, publish a real diagnostic record, validate a real immutable media reader, or retire the actual active interrupt continuation.

Startup advances only through recovered code and owned services. Unsupported addresses, unknown operands, missing permission, stale ownership and unimplemented callbacks remain explicit stops. No generic success return, invented frame, synthetic device completion or assumed unused object slot is allowed to bridge a gap.

## Data and publication

Original media, executable bytes, extracted assets, previews, detailed instruction witnesses and private packages are not public deliverables. This repository publishes newly synthesized technical narrative, status and decisions. It provides neither a game download nor instructions for obtaining unauthorized copies. Readers need their own appropriate original data for any future source-dependent tooling.

See [validation and provenance](../status/validation.md) for what can and cannot be independently checked from documentation alone.
