# Rock Man x64

An independent effort toward a native Windows x64 implementation of Mega Man Legends 1 (MML1) with an integrated IDE/editor, accompanied by a public record of its research, decisions, experiments, and validation limits. The game and complete IDE/editor are targets, not finished capabilities.

**This repository contains documentation and research metadata—not a game, source release, or build distribution.** A private prototype exists, but no playable game or native game boot has been established. No original game assets or prototype implementation are uploaded here.

## Read the project record

- **[Documentation guide](docs/README.md)** — start-to-current history, technical architecture, evidence levels, and the paused handoff.
- **[Project history](docs/history/README.md)** — how the goal and approach developed, what changed, and why.
- **[Technical documentation](docs/technical/architecture.md)** — the investigated pipeline, component boundaries, and known limitations.
- **[Current status](docs/status/current-status.md)** — completed validation versus the unfinished candidate, blockers, and conditions for resuming.
- **[PS1 research library](research/README.md)** — a separate source catalog and investigation agenda, including [native Windows research guidance](research/NATIVE-WINDOWS-HANDOFF.md). A reference catalog is not evidence that a game feature works.

## Current checkpoint — 2026-10-22

Development is **paused for documentation**. The last completed Windows-verified stage was the first CD status command, with a 29-case interrupt-chain suite. The subsequent reset/unmute candidate is **not frozen or Windows-validated**.

At the final paused checkpoint, the validation runner completed 19 stages: 17 successful and two component failures retained because fixtures were missing. Separate passing checks recorded at this checkpoint include 92 tests, 19 tools, 21 CLI checks, 18 cross-builds, and 13,305 asset records, plus queued-handler fixtures. These check inventories are not a breakdown of the 19 aggregate stages. Acceptance, freeze, and component-retry completion remained false; no new Windows run occurred. These are scoped private results, not a complete end-to-end pass. Separate offline DSP-core tests are not integrated into the runtime and do not establish audio output.

The [status record](docs/status/current-status.md) carries the detailed boundaries. Cross-compilation is not Windows execution; synthetic and component tests are not game boot; decoded assets are not gameplay.

## How to read the evidence

The project documentation summarizes private work in sanitized prose. Its reported private results cannot be independently reproduced from this documentation-only repository. Proposed designs, implemented components, test environments, confirmed milestones, and pending work are kept distinct. The public research library records reference provenance and gaps independently; it was not itself an inspection of the private prototype.

After an initial comparison of existing-project descriptions and approaches, the project adopted an independent-implementation constraint: no existing port, mod, or recompilation implementation reuse, and no other game decompilations or emulator implementations as construction references. The history records that decision rather than claiming no external projects were ever considered. This is not a formal or legally certified clean-room claim. Original game content, BIOS bytes, proprietary SDK code, and private validation packages are excluded.

## Documentation maintenance and licensing

Read [AGENTS.md](AGENTS.md) and the relevant child contract before editing. Preserve history and evidence limits when updating the current status; do not turn a component success into a completion claim.

The documentation hierarchy is adapted from [raiinman/dox](https://github.com/raiinman/dox) at commit [b88194c34ace1a2a3dc01831d36b8a65986a41f5](https://github.com/raiinman/dox/commit/b88194c34ace1a2a3dc01831d36b8a65986a41f5). Its project-specific indexes replace the source repository's indexes and artwork rules.

DOX copyright (c) 2026 Agent Zero; its MIT license is preserved verbatim in [DOX-LICENSE](DOX-LICENSE). That notice is for the imported DOX framework, not a newly granted license for the whole project or third-party game content.
