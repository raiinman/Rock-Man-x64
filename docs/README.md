# Project documentation

This is the public, sanitized record of Rock Man x64 from its initial goal through resumed development on **2026-10-22**, following the documentation pause. It documents a private prototype and its limits; it does not distribute that prototype or supply a reproducible game build.

## Reading paths

| Question | Start here |
|---|---|
| Where are we, visually, and what did we learn? | [Living tracker and findings ledger](status/dashboard.md) |
| How did the project begin, and how did the plan change? | [History](history/README.md) |
| What was investigated or implemented, and how do the pieces relate? | [Technical documentation](technical/architecture.md) |
| What actually passed, what is pending, and what is the next boundary? | [Current status](status/current-status.md) |
| Which PS1 references were found, and what are their provenance limits? | [Research library](../research/README.md) |
| How should these documents be maintained? | [Documentation contract](AGENTS.md) and [root contract](../AGENTS.md) |

Read history first for chronology, technical pages for mechanisms, and status last for the exact current boundary. Historical counts belong to their dated stage and must not be substituted for the latest validation result.

## Detailed map

- **History:** [milestone ledger](history/milestones.md), [decisions and recoveries](history/decisions-and-recoveries.md), [validation history](history/validation-history.md).
- **Technical:** [architecture](technical/architecture.md), [capability matrix](technical/capability-matrix.md), [native service contracts](technical/native-service-contracts.md).
- **Tracker upkeep:** [team completion contract](status/TRACKER.md), [plain-English change ledger](status/changes.md).
- **Status:** [living tracker and findings ledger](status/dashboard.md), [current checkpoint](status/current-status.md), [validation and provenance](status/validation.md), [decisions and handoff](status/decisions-and-handoff.md).

## Evidence vocabulary

| Label | What it establishes | What it does not establish |
|---|---|---|
| Proposed | A plan, investigation, or intended behavior | Implementation or validation |
| Implemented | A reported private component or change exists | Correctness, integration, or target-platform execution |
| Synthetic/component-tested | Behavior passed the described isolated inputs and assertions | Full hardware fidelity or game behavior |
| Linux-tested | The stated tests ran in a Linux environment | Native Windows execution |
| Cross-compiled | Target binaries were built from a different environment | Successful target execution |
| Windows-verified | The stated stage was executed and checked on Windows | Any feature outside that stage or later candidate |
| Pending/paused | Work is unfinished, unverified, or awaiting evidence | A pass, failure, or permission to resume |

Use combinations when appropriate: a component may be implemented, Linux-tested, and cross-compiled while still awaiting Windows validation. Keep the test input, scope, environment, and missing evidence attached to every result.

## Publication boundary

- The public record contains explanatory Markdown, original documentation graphics, sanitized tracker metadata and narrowly scoped documentation-updater tools and the separately maintained research catalog—not original assets, source code, binaries, extracted data, private runtime captures or private packages.
- Private evidence is summarized, not reproduced. Readers cannot independently rerun the private validation suites from this repository.
- No playable game, native game boot, audible output, or general hardware conformance is implied by the documented milestones.
- Research references and engineering observations are different evidence classes. A linked manual, proposed dependency, or cataloged format does not establish that MML1 uses it or that the prototype implements it.
- Independent implementation is a project constraint, not a legal certification. Source provenance and uncertainties remain visible.

[Back to project overview](../README.md)
