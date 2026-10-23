# Rock Man x64

An independent effort toward a **native Windows x64 Mega Man Legends 1 + integrated IDE/editor**. The goal is not finished: **native game boot is not established, and the production S2 controller remains NO-GO.**

This public repository contains documentation, research metadata and original explanatory graphics—not the private prototype, game assets, a source release or a playable build.

<!-- ROCK-MAN-TRACKER:START -->

## Living progress tracker

**Where we are:** Parts of startup and the inspection tools have passed bounded tests. Native game boot is still unestablished, and live IDE controls are not safe to enable yet.

**What changed:** The data-only observer can recover delayed notices and label old snapshots honestly. New load reviews narrowed the shutdown problem; they did not solve it.

**Why it matters:** We can inspect a stopped runtime without pretending it advanced. Safe cancellation and ownership still have to be proved before live controls can be connected.

**Next useful step:** Establish a reviewed loading and shutdown contract, then review native-owner retirement and real UI integration. Keep the unresolved graphics service stopped.

**Last evidence review:** 2026-10-23 · `2026-10-23-native-evidence-02` · [reviewed basis 9ce9b94](https://github.com/raiinman/Rock-Man-x64/commit/9ce9b9497f496584c438b76b39d1b36f2f1e4d58).
**Latest repository change observed:** [c127531](https://github.com/raiinman/Rock-Man-x64/commit/c1275311c5c841405d000203f4b02aa9645145d4) · 2026-10-23T13:22:45-07:00 — docs: automate living tracker with evidence-gated progress and plain-English updates.
**Authored evidence update supplied:** the evidence file and its review identifier changed in the observed commit. Stages still mean only what the cited reviewed record establishes.

| Workstream | Evidence bar | In plain English |
|---|---|---|
| Native CD mode-00 | 🟦🟦🟦🟦⬜ | Windows checks pass for this startup slice. |
| Graphics diagnostic | 🟦🟦🟦⬜⬜ | The Linux diagnostic reaches a known stop. |
| Owned startup capture | 🟦🟦🟦⬜⬜ | Bounded owner snapshots work in Linux tests. |
| Export \+ frozen viewer | 🟦🟦🟦🟦⬜ | Portable model import and Windows synthetic viewer checks each pass. |
| Source bytes / Back | 🟦🟦⬜🟦⬜ | Windows navigation commands preserve tested state. |
| Mailbox \+ observer | 🟦🟦🟦⬜⬜ | The data-only channel and observer pass Linux synthetic tests. |
| Loader continuation | 🟦🟦🟦⬜⬜ | Native-policy compatibility stops before the initializer. |
| S2 live IDE controller | 🟨⬜⬜⬜⬜ | Live runtime controls remain disabled. |

**Left → right:** source review · synthetic/component · Linux · Windows · full game/IDE. 🟦 bounded evidence · 🟨 completed NO-GO review · ⬜ no acceptance claimed. **These are evidence classes, not five equal units of work or percent complete.**

[What changed / why / next](docs/status/changes.md) · [Exact scopes and discoveries](docs/status/dashboard.md) · [How updates work](docs/status/TRACKER.md)

_Configured for eligible main pushes: docs-only activity refresh and regeneration. Check Actions for the actual run; reviewed evidence alone moves capability stages._

<!-- ROCK-MAN-TRACKER:END -->

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
