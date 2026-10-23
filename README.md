# Rock Man x64

An independent effort toward a **native Windows x64 Mega Man Legends 1 + integrated IDE/editor**. The goal is not finished: **native game boot is not established, and the production S2 controller remains NO-GO.**

This public repository contains documentation, research metadata and original explanatory graphics—not the private prototype, game assets, a source release or a playable build.

## Where we are · 2026-10-23

[![Eight evidence-stage progress bars: bounded Windows evidence for mode-00 and the frozen viewer; Linux-only graphics, capture, mailbox and loader evidence; S2 source-review NO-GO. No full game or IDE acceptance.](docs/status/visuals/progress-dashboard.svg)](docs/status/dashboard.md#evidence-tracks)

**Filled segments are evidence classes, not percent complete.** [Read the exact scopes, sources and unknowns →](docs/status/dashboard.md)

## What we actually learned

[![Six reconstruction discoveries: tiled texture storage, packed pose mapping, update-call sequence semantics, bounded environment geometry, character hierarchy and the ST01 startup distinction.](docs/status/visuals/findings-01.svg)](docs/status/dashboard.md#reconstruction-findings)

**[Six more important findings →](docs/status/dashboard.md#frontier-findings)** — native heap policy versus BIOS effects, honest snapshots, executed original-game emulator research, A0:49's unresolved effects, and why cancellation is not safe shutdown.

## Follow the evidence

| I want… | Go here |
|---|---|
| Every visual claim, its source and its limit | [Dashboard evidence ledger](docs/status/dashboard.md) |
| Exact current blockers and test scopes | [Current status](docs/status/current-status.md) · [Validation](docs/status/validation.md) |
| The full story, including failures and corrections | [Project history](docs/history/README.md) |
| Architecture and investigated capabilities | [Technical guide](docs/technical/architecture.md) · [Capability matrix](docs/technical/capability-matrix.md) |
| PS1 research and its implementation restrictions | [Research library](research/README.md) · [Provenance review](research/bios/PROVENANCE-REVIEW.md) |

Private results are summarized in sanitized prose and are **not independently reproducible from this repository**. Executed emulator research is not native-game boot. Source references, test oracles and implementation lineage remain separate; PSX-SPX is a restricted-provenance research reference, not cleared implementation authority. Independent implementation is the project constraint, not a legally certified clean-room claim.

<details>
<summary>Documentation maintenance and DOX licensing</summary>


Read [AGENTS.md](AGENTS.md) and the relevant child contract before editing. Preserve history and evidence limits when updating the current status; do not turn a component success into a completion claim.

The documentation hierarchy is adapted from [raiinman/dox](https://github.com/raiinman/dox) at commit [b88194c34ace1a2a3dc01831d36b8a65986a41f5](https://github.com/raiinman/dox/commit/b88194c34ace1a2a3dc01831d36b8a65986a41f5). Its project-specific indexes replace the source repository's indexes and artwork rules.

DOX copyright (c) 2026 Agent Zero; its MIT license is preserved verbatim in [DOX-LICENSE](DOX-LICENSE). That notice is for the imported DOX framework, not a newly granted license for the whole project or third-party game content.

</details>
