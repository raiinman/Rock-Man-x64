# Status documentation maintenance

Scope: checkpoint, validation and decision records in this directory. Maintain documentation only unless separately authorized.

Index: [visual dashboard and evidence ledger](dashboard.md), [dashboard metadata](dashboard-data.json), [current checkpoint](current-status.md), [validation and provenance](validation.md), [decisions and handoff](decisions-and-handoff.md).

- While the direct coordination channel is unavailable, review public handoffs and revisions at each checkpoint and append only public-sourced coordination deltas for APEX-1. Preserve existing messages; this temporary coordination transfers neither ownership nor execution authority.
- Date each material checkpoint and identify its frozen/unfrozen, accepted/pending and execution-platform status.
- Prefer terminal per-stage receipts over stale overviews. A runner exit 0 cannot erase failed child stages; missing-fixture repair is not a passed rerun.
- Separate private project attestation, static analysis, synthetic checks, connected runtime, Windows execution and design proposals.
- Retain pending and inconclusive outcomes. Do not invent new checks or repeat denied/uncertain actions to improve the record.
- Exclude original data, raw private receipts, machine/user/account identifiers, internal paths and private links. Check navigation and cross-page counts before publication.
- Record a later acceptance as a new checkpoint, not a retroactive rewrite of what was known at pause.

## Living tracker contract

- Own `dashboard-data.json` as the reviewed evidence source, `TRACKER.md` as the team upkeep contract, and the generated `dashboard.md`, `changes.md` and `tracker-state.json`. The root README tracker block is generated from this source too.
- Every meaningful Rock Man change must update plain-English changed/why/next, evidence class/source, blockers and actual review date/identifier/basis. Stable entry IDs preserve history. Research authors may update reference findings, never native capability acceptance by inference.
- Generated files are not manually edited. Run the generator, bounded fixture tests and `--check`; inspect the exact diff and visible text. The publication owner verifies the actual Actions result and generated commit, or reports a failed/skipped/pending refresh.
- Latest repository activity and last evidence review are separate. Unchanged evidence data or an unchanged review identifier keeps new activity review-pending. A changed authored record is not an independent automated review of underlying tests.
- The default numeric chart counts named accepted criteria in a separately defined overall roadmap and five frozen-version local checklists, with completed/total, remaining, percentages and review deltas. The overall roadmap counts named unequal-size delivery milestones, not effort or a percent of the game finished. The local checklists overlap it and are not exhaustive project inventories; never sum or average them into the overall ratio. Suite pass rates are separate. The secondary evidence-class matrix still has overlapping scopes: source review is not implementation, and synthetic/platform labels may describe the same run.
- Evidence schema 3 and generated receipt schema 2 bind checklist definitions, item states, validation counts and append-only observations to the review digest. Criterion/denominator changes require a new checklist version and an explicit rebaseline, never a same-version progress delta. The latest observation must match the evidence review ID, date and basis commit exactly. Never edit or invent older observations; preserve corrections as later records. Append at most one bound observation per review transition; do not insert fictitious intermediate reviews to manufacture change.
- Private reports are summarized only in sanitized original prose. Preserve emulator/native distinctions, PSX-SPX/firmware/test-oracle provenance, native-boot limits and unresolved S2/lifecycle gates.
- Repository activity is refreshed only from exact commit metadata (Git or the authorized connector path). No prose parser promotes capabilities. The updater never changes `dashboard-data.json` or its review history. Changed stage states/citations or numerical measurement data require a new review identifier against both the saved evidence receipt and, during Git refresh, the actual parent evidence file. Definition versions and append-only history are checked against both receipts and the Git parent.
- Archived findings graphics are secondary dated references, not the live status authority. The current generated tracker and reviewed data take precedence.

## Child DOX Index

- [tools/AGENTS.md](tools/AGENTS.md) owns the documentation-only updater, fixed-path guard and fixture tests.
- [visuals/AGENTS.md](visuals/AGENTS.md) owns the generated evidence graphic and dated explanatory boards.
