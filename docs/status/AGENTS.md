# Status documentation maintenance

Scope: checkpoint, validation and decision records in this directory. Maintain documentation only unless separately authorized.

Index: [visual dashboard and evidence ledger](dashboard.md), [dashboard metadata](dashboard-data.json), [current checkpoint](current-status.md), [validation and provenance](validation.md), [decisions and handoff](decisions-and-handoff.md).

- Date each material checkpoint and identify its frozen/unfrozen, accepted/pending and execution-platform status.
- Prefer terminal per-stage receipts over stale overviews. A runner exit 0 cannot erase failed child stages; missing-fixture repair is not a passed rerun.
- Separate private project attestation, static analysis, synthetic checks, connected runtime, Windows execution and design proposals.
- Retain pending and inconclusive outcomes. Do not invent new checks or repeat denied/uncertain actions to improve the record.
- Exclude original data, raw private receipts, machine/user/account identifiers, internal paths and private links. Check navigation and cross-page counts before publication.
- Record a later acceptance as a new checkpoint, not a retroactive rewrite of what was known at pause.

## Visual dashboard contract

- Own `dashboard.md` and `dashboard-data.json`; the ledger mirrors every visible workstream and finding, with evidence class, source, importance and remaining unknown. The snapshot date and underlying public commit must be explicit.
- Bars represent independent evidence classes, not equal units of implementation or a game-completion percentage. Platform execution and synthetic inputs overlap; do not sum them as independent milestones. An empty segment means no acceptance claimed in this dashboard, not a failed test or proof no work exists.
- Summarize new private reviews only in original sanitized prose. Source/design acceptance, including a NO-GO finding, is not implementation or runtime acceptance. Preserve PSX-SPX and firmware provenance limits and distinguish executed emulator research from native game boot.
- Keep structured metadata, graphics and accessible prose in sync. Check all relative paths and section anchors; compare stage/count changes to the exact cited evidence, render SVGs, and inspect readability before publication. Local generators, preview PNGs and review receipts are not public runtime artifacts.

## Child DOX Index

- [visuals/AGENTS.md](visuals/AGENTS.md) owns the original static dashboard and findings graphics.
