# Rock Man x64

An independent effort toward a native Windows x64 implementation of Mega Man Legends 1 (MML1) with an integrated IDE/editor, accompanied by a public record of its research, decisions, experiments, and validation limits. The game and complete IDE/editor are targets, not finished capabilities.

**This repository contains documentation and research metadata—not a game, source release, or build distribution.** A private prototype exists, but no playable game or native game boot has been established. No original game assets or prototype implementation are uploaded here.

## Read the project record

- **[Documentation guide](docs/README.md)** — start-to-current history, technical architecture, evidence levels, and the current handoff.
- **[Project history](docs/history/README.md)** — how the goal and approach developed, what changed, and why.
- **[Technical documentation](docs/technical/architecture.md)** — the investigated pipeline, component boundaries, and known limitations.
- **[Current status](docs/status/current-status.md)** — completed validation versus the unfinished candidate, blockers, and next steps.
- **[PS1 research library](research/README.md)** — a separate source catalog and investigation agenda, including [native Windows research guidance](research/NATIVE-WINDOWS-HANDOFF.md). A reference catalog is not evidence that a game feature works.

## Current checkpoint — 2026-10-23 hourly update

Development **resumed at 22:04 UTC on October 22**. The native CPU software-mixer stage is now sealed and has passed **51 actual Windows cases** (30 expected exit 0, 21 intentional refusals), including 30 complete JSON and 21 text comparisons. High-level `CdInit` genuinely returns 1; the stage stops at the next unsupported non-null-result `CdSync` boundary. It has no output-device ownership, decoder, playback, physical SPU equivalence or game-boot claim.

A newer **mode-00 candidate** connects a same-image Form1 reader through the actual parameter FIFO, response, IRQ and callback path. The isolated 13-stage recovery aggregate and a newer 69-case Linux contract passed. It remains **unsealed and not Windows-tested**: Windows runner supervision passed 15 synthetic checks after earlier failures, but the real mode adapter, final sealing and Windows mode execution remain pending. Historical failures, the frozen mixer's stale summary-counter defect, and reporting corrections remain in the [validation history](docs/history/validation-history.md).

The [status record](docs/status/current-status.md) carries the detailed boundaries. Cross-compilation is not Windows execution; synthetic and component tests are not game boot; decoded assets are not gameplay.

## How to read the evidence

The project documentation summarizes private work in sanitized prose. Its reported private results cannot be independently reproduced from this documentation-only repository. Proposed designs, implemented components, test environments, confirmed milestones, and pending work are kept distinct. The public research library records reference provenance and gaps independently; it was not itself an inspection of the private prototype.

After an initial comparison of existing-project descriptions and approaches, the project adopted an independent-implementation constraint: no existing port, mod, or recompilation implementation reuse, and no other game decompilations or emulator implementations as construction references. The history records that decision rather than claiming no external projects were ever considered. This is not a formal or legally certified clean-room claim. Original game content, BIOS bytes, proprietary SDK code, and private validation packages are excluded.

## Documentation maintenance and licensing

Read [AGENTS.md](AGENTS.md) and the relevant child contract before editing. Preserve history and evidence limits when updating the current status; do not turn a component success into a completion claim.

The documentation hierarchy is adapted from [raiinman/dox](https://github.com/raiinman/dox) at commit [b88194c34ace1a2a3dc01831d36b8a65986a41f5](https://github.com/raiinman/dox/commit/b88194c34ace1a2a3dc01831d36b8a65986a41f5). Its project-specific indexes replace the source repository's indexes and artwork rules.

DOX copyright (c) 2026 Agent Zero; its MIT license is preserved verbatim in [DOX-LICENSE](DOX-LICENSE). That notice is for the imported DOX framework, not a newly granted license for the whole project or third-party game content.
