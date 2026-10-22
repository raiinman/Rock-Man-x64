# DOX framework

- DOX is highly performant AGENTS.md hierarchy installed here
- Agent must follow DOX instructions across any edits

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees
- Work products, source materials, instructions, records, assets, and durable docs must stay understandable from the nearest applicable AGENTS.md plus every parent AGENTS.md above it

## Read Before Editing

1. Read the root AGENTS.md
2. Identify every file or folder you expect to touch
3. Walk from the repository root to each target path
4. Read every AGENTS.md found along each route
5. If a parent AGENTS.md lists a child AGENTS.md whose scope contains the path, read that child and continue from there
6. Use the nearest AGENTS.md as the local contract and parent docs for repo-wide rules
7. If docs conflict, the closer doc controls local work details, but no child doc may weaken DOX

Do not rely on memory. Re-read the applicable DOX chain in the current session before editing.

## Update After Editing

Every meaningful change requires a DOX pass before the task is done.

Update the closest owning AGENTS.md when a change affects:

- purpose, scope, ownership, or responsibilities
- durable structure, contracts, workflows, or operating rules
- required inputs, outputs, permissions, constraints, side effects, or artifacts
- user preferences about behavior, communication, process, organization, or quality
- AGENTS.md creation, deletion, move, rename, or index contents

Update parent docs when parent-level structure, ownership, workflow, or child index changes. Update child docs when parent changes alter local rules. Remove stale or contradictory text immediately. Small edits that do not change behavior or contracts may leave docs unchanged, but the DOX pass still must happen.

## Hierarchy

- Root AGENTS.md is the DOX rail: project-wide instructions, global preferences, durable workflow rules, and the top-level Child DOX Index
- Child AGENTS.md files own domain-specific instructions and their own Child DOX Index
- Each parent explains what its direct children cover and what stays owned by the parent
- The closer a doc is to the work, the more specific and practical it must be

## Child Doc Shape

- Create a child AGENTS.md when a folder becomes a durable boundary with its own purpose, rules, responsibilities, workflow, materials, or quality standards
- Work Guidance must reflect the current standards of the project or user instructions; if there are no specific standards or instructions yet, leave it empty
- Verification must reflect an existing check; if no verification framework exists yet, leave it empty and update it when one exists

Default section order:
- Purpose
- Ownership
- Local Contracts
- Work Guidance
- Verification
- Child DOX Index

## Style

- Keep docs concise, current, and operational
- Document stable contracts, not diary entries
- Put broad rules in parent docs and concrete details in child docs
- Prefer direct bullets with explicit names
- Do not duplicate rules across many files unless each scope needs a local version
- Delete stale notes instead of explaining history
- Trim obvious statements, repeated rules, misplaced detail, and warnings for risks that no longer exist

## Closeout

1. Re-check changed paths against the DOX chain
2. Update nearest owning docs and any affected parents or children
3. Refresh every affected Child DOX Index
4. Remove stale or contradictory text
5. Run existing verification when relevant
6. Report any docs intentionally left unchanged and why

## User Preferences

When the user requests a durable behavior change, record it here or in the relevant child AGENTS.md

## Child DOX Index

- [`research/AGENTS.md`](research/AGENTS.md) owns the PS1 research library, source catalogs, search records, and handoff guidance.
- [`docs/AGENTS.md`](docs/AGENTS.md) owns the project documentation index and delegates history, technical architecture, and current status to its child contracts.
- The root owns `README.md`, `AGENTS.md`, and `DOX-LICENSE`.

## Project Scope

- Project: Rock Man x64.
- This repository supports an independent MML1 native Windows effort and a sourced PS1 reference library.
- The user authorized PS1 hardware and official Sony development research, parallel research agents, necessary tool installation, and saving findings to this repository on 2026-10-22.
- Research authorization does not establish facts about the other computer's game implementation. Record game-specific behavior only when supported by identified game evidence.
- Respect the user's independent implementation constraint: do not import other game ports, decompilation projects, or emulator implementation code as implementation help.
- Keep private notes, credentials, unrelated projects, original game data, and private validation packages out of this public repository.
- The current deliverables are documentation and metadata. There is no game runtime or game build command here.

## Documentation and Publication Contract

- Development is paused at the owner's request while the start-to-current project record is documented. Documentation work does not authorize resuming implementation.
- This public repository is a documentation and research record, not a source, build, asset, or playable-game distribution. A private prototype exists; do not describe repository emptiness as absence of all project development.
- Document chronology, decisions, failures, corrections, evidence boundaries, and unfinished work, not just successful milestones.
- Separate proposed, implemented, component/synthetic/Linux-tested, cross-compiled, and Windows-verified states. A build or test count does not establish gameplay, native boot, rendering accuracy, or audible output.
- Publish only reviewed Markdown for the project-history update. Preserve unrelated research work and all existing license text; do not change research catalogs, workflows, settings, deployment, collaborators, or secrets as part of that update.
- Do not publish implementation code, original assets, ROM or executable bytes, dumps or disassembly tables, binaries, previews, private packages or download links, private file identities, personal paths/account details, internal messages, private memory, or credentials.
- Summarize private evidence in sanitized original prose; never copy raw private reports. State that private test results are not independently reproducible from this documentation-only repository.
- Keep source provenance explicit. Independent implementation is a project constraint, not a legally certified clean-room claim.
- Preserve `DOX-LICENSE` verbatim. Its MIT notice covers the imported DOX framework; do not infer or add a whole-project license without owner approval.
- Before publication, review the exact changed Markdown, check relative links and DOX indexes, scan for forbidden content and local paths, and check whitespace.
- Re-read the current remote head and relevant contracts before publishing. Build on the current tree, preserve unrelated changes, use an expected-head lease without force-push, and reconcile a changed head before retrying.
- Verify the resulting remote commit, exact file contents, preserved paths, links, and public visibility before reporting publication complete.
