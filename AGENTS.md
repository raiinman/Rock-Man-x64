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

- On 2026-10-22 the user authorized continued in-depth BIOS research, subagents and necessary local tools, and asked that reviewed findings reach GitHub promptly for the other agent. The latest research update cadence is every half hour, superseding the earlier hourly request. This research continues separately from game implementation; `research/bios/AGENTS.md` owns its operating detail.
- On 2026-10-23 the user clarified that progress must be a living tracker updated with GitHub changes, not a set of render snapshots. Lead with an automatically generated numeric horizontal chart, completed/total and remaining counts, checklist percentages, blockers and recorded review deltas, alongside plain-English changed/why/next. Freeze named acceptance criteria and denominator versions, including a separately defined overall roadmap. Its accepted/total milestone ratio must not average local bars or claim equal effort, code completion or a finished-game percentage. Never backfill a fake history. Every meaningful Rock Man change must maintain the authoritative tracker data, cited evidence class, blockers and real review revision, regenerate/check outputs, and verify the actual published workflow result. `docs/status/AGENTS.md` owns that team completion contract.
- On 2026-10-23 the user requested a spacious, interactive documentation tracker like the Xeno visualizer, with an overall roadmap, workstreams, findings and change history. The latest direction makes a full-page equal-area milestone heatmap the primary web view, with original mechanical engineering/armor styling inspired broadly by Tony Stark, Mega Man X and Zero: deep warm red (not pink/magenta), charcoal, ivory, restrained gold and tiny cyan selection accents. Use no copied assets/logos or fake telemetry. Keep large readable counts, textual status/symbols, expandable evidence and the existing keyboard-accessible list/board/detail routes. `docs/web/AGENTS.md` owns this read-only documentation UI. The owner also requested hourly reviewed heatmap check-ins: record the actual review time in the reviewed change/summary prose, including honest zero-delta checks, without treating repository activity as evidence acceptance or adding fake live timers. The existing documentation cadence owns scheduling. The owner subsequently approved public GitHub Pages hosting on 2026-10-23; the documentation-only build/deploy jobs are governed by `.github/workflows/AGENTS.md`. This does not authorize game builds, other services, credentials or unrelated settings.
- The user approved the numeric checklist chart on 2026-10-23 and requested an original glossy red/crimson design with accents, not the standard blue palette. This is a presentation preference, not authority to change evidence or reuse proprietary art/logos; `docs/status/visuals/AGENTS.md` owns its implementation.
- The user explicitly approved the narrowly scoped documentation-only GitHub Actions updater on 2026-10-23. The later explicit Pages approval adds only public hosting of the read-only tracker and its required Pages source/environment configuration; no game builds, other services, new credentials or unrelated settings are authorized.

## Child DOX Index

- [`.github/AGENTS.md`](.github/AGENTS.md) owns the approved documentation updater and chained public-tracker Pages build/deployment, with separated permissions.
- [`research/AGENTS.md`](research/AGENTS.md) owns the PS1 research library, source catalogs, search records, and handoff guidance.
- [`docs/AGENTS.md`](docs/AGENTS.md) owns the project documentation index and delegates history, technical architecture, and current status and the read-only documentation UI to its child contracts.
- The root owns `README.md`, `AGENTS.md`, `DOX-LICENSE`, and `DOT.md`, the public-safe research/native coordination entry point. `DOT.md` must lead with the owner-selected active source handoff, including source-ready, exact missing-function or named access/authority-blocker outcomes; retain superseded requests as history rather than treating an hourly status review as an answer.

## Project Scope

- Project: Rock Man x64.
- This repository supports an independent MML1 native Windows effort and a sourced PS1 reference library.
- The user authorized PS1 hardware and official Sony development research, parallel research agents, necessary tool installation, and saving findings to this repository on 2026-10-22.
- Research authorization does not establish facts about the other computer's game implementation. Record game-specific behavior only when supported by identified game evidence.
- Respect the user's independent implementation constraint: do not import other game ports, decompilation projects, or emulator implementation code as implementation help.
- Controlled BIOS/emulator diagnostics are permitted as separately labeled research—not hardware or native-boot proof; the finished game must remain native Windows without a BIOS/emulator runtime dependency or reused port/mod/emulator implementation, and original bytes, captures and private packages remain excluded from publication.
- Keep private notes, credentials, unrelated projects, original game data, and private validation packages out of this public repository.
- The current deliverables are documentation, metadata, original explanatory graphics and the narrowly scoped documentation-maintenance tooling and read-only documentation UI. There is no game runtime or game build command here.

## Documentation and Publication Contract

- Development resumed at the owner's request on 2026-10-22 at 22:04 UTC after the documentation pause. Maintain hourly public GitHub documentation updates while development proceeds; summarize only verified changes and keep pending work explicit. This standing documentation authorization does not expand the publication boundary.
- This public repository is a documentation and research record, not a source, build, asset, or playable-game distribution. A private prototype exists; do not describe repository emptiness as absence of all project development.
- Document chronology, decisions, failures, corrections, evidence boundaries, and unfinished work, not just successful milestones.
- Separate proposed, implemented, component/synthetic/Linux-tested, cross-compiled, and Windows-verified states. A build or test count does not establish gameplay, native boot, rendering accuracy, or audible output.
- Publish reviewed Markdown for the project-history update. The authorized living tracker may additionally contain sanitized JSON evidence metadata, original SVG explanations and documentation-only generator/tests under `docs/status/`. The approved `.github/workflows/update-progress.yml` may run those tools on eligible main-branch pushes and commit only their five exact generated outputs. The requested `docs/web/` interface may contain original HTML/CSS/JavaScript, a local artifact builder and tests that only project the same public tracker data. It must not duplicate authored evidence, add public editing, run game code or launch services. These are documentation infrastructure, not game/runtime implementation or private-runtime previews. Preserve unrelated research work and all existing license text; do not change research catalogs, unrelated workflows/settings/deployments, collaborators or secrets. The named workflow may additionally chain the explicitly approved static Pages build and deployment after the updater; it must deploy only the checked public documentation artifact, never private-runtime content. The updater itself retains its exact five-file write allowlist.
- Do not publish game/runtime implementation code, original assets, ROM or executable bytes, dumps or disassembly tables, binaries, private-runtime previews or captures, private packages or download links, private file identities, personal paths/account details, internal messages, private memory, or credentials.
- Summarize private evidence in sanitized original prose; never copy raw private reports. State that private test results are not independently reproducible from this documentation-only repository.
- Keep source provenance explicit. Independent implementation is a project constraint, not a legally certified clean-room claim.
- Preserve `DOX-LICENSE` verbatim. Its MIT notice covers the imported DOX framework; do not infer or add a whole-project license without owner approval.
- Before publication, review the exact changed Markdown, metadata, documentation tooling/workflow and graphics; check relative links and DOX indexes, scan for forbidden content and local paths, and check whitespace. Render and inspect graphics, verify every stage/count against its source, and exclude scripts, remote embeds, original assets and private captures from SVGs.
- Re-read the current remote head and relevant contracts before publishing. Build on the current tree, preserve unrelated changes, use an expected-head lease without force-push, and reconcile a changed head before retrying.
- Verify the resulting remote commit, exact file contents, preserved paths, links, and public visibility before reporting publication complete.
