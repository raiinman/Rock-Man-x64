# Rock Man x64

A project working toward an independent **native Windows x64 Mega Man Legends 1 experience**, with an integrated editor for exploring and working with game data.

**Can I play it today?** There is no public playable build or game download here. Native game boot has not been established. A private prototype exists; this repository shares the documentation and research behind the work.

[**Explore the project and progress →**](https://raiinman.github.io/Rock-Man-x64/) · [**Build & spec plan**](https://raiinman.github.io/Rock-Man-x64/#build-plan) · [Read the project story](docs/history/README.md) · [Browse the research](research/README.md)

![Original concept illustration of a crimson mechanical workshop](docs/artwork/workshop-concept.png)
*Original AI-generated concept illustration for this documentation. Not a screenshot or game output.*

## What you can explore today

- **Progress:** a readable roadmap with accepted, pending and blocked milestones. Open any tile for the exact evidence.
- **The story so far:** decisions, experiments, corrections and the work still ahead.
- **Under the hood:** technical explanations and a sourced PS1 research library.

The goal includes a native game and editor. Documentation, research results and component tests are useful steps toward it; they do not establish playable gameplay, native boot or a release date.

<!-- ROCK-MAN-TRACKER:START -->

## Progress, in numbers

[![Completed and remaining goals in five named checklists](docs/status/visuals/progress-dashboard.svg)](docs/status/dashboard.md#named-checklists)

**This chart updates from reviewed data after eligible GitHub pushes.** The top bar counts accepted milestones in the named overall roadmap—not code, effort or how much of the game is finished. Local checklists and test pass rates remain separate.

**Where we are:** Four additional Linux/component results cover selected-file Refresh, standalone PCM control, rasterizer edge coverage and bounded WAV staging. Their Windows/device behavior remains separately unverified. Earlier Windows build and partial-observation records retain their own scopes. No playable native game or complete IDE is established.

**Next useful step:** The native owner continues a read-only WAV file-provider specification/review using the frozen decoder; no provider implementation or acceptance is established in this record. A bounded Windows PCM compile/tone task is admitted but has no execution result. Preserve unresolved newer OBJ reopen/cleanup, provenance, initializer and S2 gates.

**Change since previous numeric review:** Frozen inspection delivery: Δ \+0 goals; Data-only observation path: Δ \+0 goals; Selected loader checkpoints: Δ \+0 goals; Live controller safety gates: Δ \+0 goals; Native game boot acceptance: Δ \+0 goals; Accepted roadmap milestones: Δ \+0 goals.

[Exact done criteria and evidence](docs/status/dashboard.md#named-checklists) · [Recorded changes](docs/status/changes.md#numeric-review-history) · [12 important discoveries](docs/status/dashboard.md#reconstruction-findings) · [How this stays current](docs/status/TRACKER.md)

**Last evidence review:** 2026-10-26 · `2026-10-26-native-component-review-01` · [reviewed basis c4497c7](https://github.com/raiinman/Rock-Man-x64/commit/c4497c76f54fb0d4c9e301cec59ea1cd5bd01d6f).
**Latest repository change observed:** [c4497c7](https://github.com/raiinman/Rock-Man-x64/commit/c4497c76f54fb0d4c9e301cec59ea1cd5bd01d6f) · 2026-10-26T11:49:06Z — docs: refresh generated progress tracker.
**Evidence boundary:** repository activity and accepted capability are separate. A new push never counts as a native-game pass.

<!-- ROCK-MAN-TRACKER:END -->

## Follow the evidence

| I want… | Go here |
|---|---|
| Reading paths and documentation ownership | [Documentation guide](docs/README.md) |
| Public work requests and coordination | [Coordination entry point](DOT.md) · [Dated handoff](docs/status/decisions-and-handoff.md) |
| Every visual claim, its source and its limit | [Dashboard evidence ledger](docs/status/dashboard.md) |
| Exact current blockers and test scopes | [Current status](docs/status/current-status.md) · [Validation](docs/status/validation.md) |
| The full story, including failures and corrections | [Project history](docs/history/README.md) |
| Architecture and investigated capabilities | [Technical guide](docs/technical/architecture.md) · [Capability matrix](docs/technical/capability-matrix.md) |
| Capability boundaries and spec-driven workflow | [Capability map](CAPABILITIES.md) · [Shared specification](SPEC.md) |
| PS1 research and its implementation restrictions | [Research library](research/README.md) · [Provenance review](research/bios/PROVENANCE-REVIEW.md) |

Private results are summarized in sanitized prose and are **not independently reproducible from this repository**. Executed emulator research is not native-game boot. Source references, test oracles and implementation lineage remain separate; PSX-SPX is a restricted-provenance research reference, not cleared implementation authority. Independent implementation is the project constraint, not a legally certified clean-room claim.

<details>
<summary>Documentation maintenance and DOX licensing</summary>


Read [AGENTS.md](AGENTS.md) and the relevant child contract before editing. Preserve history and evidence limits when updating the current status; do not turn a component success into a completion claim.

The documentation hierarchy is adapted from [raiinman/dox](https://github.com/raiinman/dox) at commit [b88194c34ace1a2a3dc01831d36b8a65986a41f5](https://github.com/raiinman/dox/commit/b88194c34ace1a2a3dc01831d36b8a65986a41f5). Its project-specific indexes replace the source repository's indexes and artwork rules.

DOX copyright (c) 2026 Agent Zero; its MIT license is preserved verbatim in [DOX-LICENSE](DOX-LICENSE). That notice is for the imported DOX framework, not a newly granted license for the whole project or third-party game content.

</details>
