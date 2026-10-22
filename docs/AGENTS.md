# Project documentation contract

## Purpose

Maintain an approachable, comprehensive public record of the project's history, technical work, verification boundaries, and current development state without publishing private implementation materials.

## Ownership

- This file owns the documentation-wide rules and `README.md` reading guide.
- Child contracts own chronology, technical explanation, and present status respectively.
- The independent `research/` subtree remains governed by its own contract; link to it rather than silently rewriting its evidence or provenance.

## Local Contracts

- Follow the root publication boundary. This subtree accepts reviewed Markdown documentation only.
- Use sanitized original summaries, not raw private logs, transcripts, code excerpts, or extracted content.
- Separate the current checkpoint from historical stages. Preserve failed approaches and corrections in history while removing stale claims from current summaries.
- Describe private results as reported evidence with explicit scope; the public repository does not contain the inputs or implementation needed to reproduce them.
- Use the evidence vocabulary in `README.md`; identify platform and distinguish implementation, testing, cross-build, Windows validation, and pending work.
- Never imply that test counts prove game boot, gameplay, rendering fidelity, sound output, or complete hardware behavior.

## Work Guidance

- Keep the root overview short and direct readers to this index; put durable detail in the owning child subtree.
- Update status, relevant technical limitations, and history together when a milestone or correction changes the project record.
- Keep dates and milestone labels explicit. Do not invent timestamps or turn planned work into completed history.
- A documentation update does not authorize resuming development or publishing private artifacts.

## Verification

- Review the exact changed file list and Markdown content against the public-content boundary.
- Check internal links against the assembled repository tree, refresh Child DOX Index entries, and check whitespace.
- Review milestone numbers and validation labels for consistency across root overview, history, technical pages, and current status.
- Preserve untouched research and DOX license blobs when publishing; verify exact remote contents after the commit.

## Child DOX Index

- [history/AGENTS.md](history/AGENTS.md) owns start-to-current chronology and decision history.
- [technical/AGENTS.md](technical/AGENTS.md) owns architecture, component explanations, and technical limits.
- [status/AGENTS.md](status/AGENTS.md) owns the latest checkpoint, evidence matrix, unfinished work, and next-step conditions.
