# Project documentation contract

## Purpose

Maintain an approachable, comprehensive public record of the project's history, technical work, verification boundaries, and current development state without publishing private implementation materials.

## Ownership

- This file owns the documentation-wide rules and `README.md` reading guide.
- Child contracts own chronology, technical explanation, present status and the read-only documentation UI respectively.
- The independent `research/` subtree remains governed by its own contract; link to it rather than silently rewriting its evidence or provenance.

## Local Contracts

- Follow the root publication boundary. This subtree accepts reviewed Markdown documentation; the authorized living status tracker also accepts original SVG explanations, clearly labeled original concept artwork, sanitized JSON evidence metadata and its documentation-only generator/tests. The requested `web/` interface also accepts original static HTML/CSS/ES modules, its local artifact builder and bounded tests, using canonical status data without a second authored snapshot. These do not authorize game/runtime implementation code, game assets, private runtime captures or services.
- The root bounded image exception permits only the three reviewed owner-delivered images in `gallery/`, with captions and provenance limits. They are public repository/README media, excluded from the fixed Pages artifact; this does not admit other private captures, source or packages.
- Use sanitized original summaries, not raw private logs, transcripts, code excerpts, or extracted content.
- Separate the current checkpoint from historical stages. Preserve failed approaches and corrections in history while removing stale claims from current summaries.
- Describe private results as reported evidence with explicit scope; the public repository does not contain the inputs or implementation needed to reproduce them.
- Use the evidence vocabulary in `README.md`; identify platform and distinguish implementation, testing, cross-build, Windows validation, and pending work.
- Never imply that test counts prove game boot, gameplay, rendering fidelity, sound output, or complete hardware behavior.

## Work Guidance

- Keep the root overview current, plain-English and short; generate visible numeric checklist charts and changed/why/next from reviewed source data, link the complete ledger, and put durable detail in the owning child subtree. Percentages may describe only explicit versioned finite checklists, never overall game completion or effort. Keep suite pass rates separate and compare recorded observations only within the same checklist version.
- Update status, relevant technical limitations, and history together when a milestone or correction changes the project record.
- Keep dates and milestone labels explicit. Do not invent timestamps or turn planned work into completed history.
- Tracker upkeep is part of every meaningful Rock Man change: maintain reviewed data and change explanations, regenerate/check outputs, and verify the actual updater result after publication. Never promote native evidence from research or repository activity.
- Keep the separate build/spec-plan map distinct from historical acceptance: explicit reviewed states, bounded build evidence, dependency/source links and review time, without task-checkbox inference or an overall game-completion ratio.
- Keep the interactive overview spacious and heatmap-first: equal-area, clearly labeled milestone cells across the main canvas, with the overall accepted/total count visible; put complete criteria, caveats and suite statistics in expandable or dedicated views. Tile area/color are not measures of effort, activity or game completion. Preserve the generated repository chart as the fallback. Public filters and navigation are read-only, never evidence edits or simulated running tasks.
- A documentation update does not authorize resuming development or publishing private artifacts.

## Verification

- Review the exact changed file list, Markdown, metadata and graphics against the public-content boundary. Render static graphics and inspect all text, stage labels, counts and caveats; reject executable SVG content and external embeds.
- Check internal links against the assembled repository tree, refresh Child DOX Index entries, and check whitespace.
- Review milestone numbers and validation labels for consistency across root overview, history, technical pages, and current status.
- Preserve untouched research and DOX license blobs when publishing; verify exact remote contents after the commit.

## Child DOX Index

- [gallery/AGENTS.md](gallery/AGENTS.md) owns the three specifically approved public prototype images and their captions, outside Pages delivery.

- [artwork/AGENTS.md](artwork/AGENTS.md) owns original documentation-only concept imagery and its provenance.
- [history/AGENTS.md](history/AGENTS.md) owns start-to-current chronology and decision history.
- [technical/AGENTS.md](technical/AGENTS.md) owns architecture, component explanations, and technical limits.
- [status/AGENTS.md](status/AGENTS.md) owns the latest checkpoint, evidence matrix, unfinished work, and next-step conditions.
- [web/AGENTS.md](web/AGENTS.md) owns the original static, read-only interactive tracker, local build/preview and UI verification boundary.
