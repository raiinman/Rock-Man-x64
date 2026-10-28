# Documentation tracker tooling

## Purpose

Generate the living public tracker from reviewed evidence and exact repository metadata, without game implementation, original inputs or semantic inference.

## Ownership

- `update_tracker.py`: schema checks and deterministic Markdown/SVG/receipt generation.
- `check_generated_changes.py`: Git worktree/staging allowlist, README marker and SVG safety checks.
- `test_tracker.py`: isolated offline documentation fixtures; never game or original-input tests. Its pinned-action check owns the updater job; `docs/web/tests/test_pages.py` independently checks the approved downstream Pages jobs.
- The parent owns authored evidence and maintenance prose. `.github/workflows/AGENTS.md` owns remote execution.

## Local Contracts

- Standard-library Python only, fixed output paths, no dependency installs, network calls, credentials, original inputs, services or runtime code.
- Generated targets are exactly `README.md` (marked block only), `docs/status/dashboard.md`, `docs/status/changes.md`, `docs/status/visuals/progress-dashboard.svg`, `docs/status/tracker-state.json`.
- Validate every output before mutation; refuse unsupported schema, missing evidence, private-content patterns, unsafe paths and symlinks. `--check` is read-only and never refreshes activity.
- Activity metadata cannot promote stages or change review dates/IDs. Filled stages and accepted checklist criteria require reviewed citations. A source-only NO-GO is not a test pass.
- Evidence schema 3 and receipt schema 2 require named, versioned criteria and append-only numeric observations. Count only explicit boolean acceptance; never derive milestone acceptance from test counts. Same-version denominator/criterion edits, mismatched observation/review metadata, missing receipts, history rewrites and unreviewed promotions fail closed. New versions are labeled rebaseline; no delta is compared across versions. Only one new bound observation may be appended per review transition, checked against receipt and Git parent; the initial migration contains exactly one baseline. No invented intermediate observation may manufacture a delta.
- The generated chart is the default README display. The overall roadmap uses the same guarded checklist schema/digest/history as the five local plans; compute it from its own item booleans, never local percentages or test totals. Keep counts/percentages/blockers readable, preserve the twelve findings, and keep the five output paths and updater-job permissions unchanged. The separately approved Pages jobs do not broaden this generator or its repository-write guard.
- Git metadata reads use exact full SHAs and argument arrays. Do not execute commit prose or introduce dynamic shell commands. No network Git operations are performed by these tools.
- Tests use owned temporary fixtures and local Git only. Do not copy private prototype/source/input trees into tests. Mutation tests must initialize explicit synthetic definitions, IDs, acceptance flags and history independent of live project data. Separately validate current real data/render drift read-only. Cover baseline, zero-delta and actual Git-parent +1 transitions, and verify the complete suite against a disposable future-count dataset without resetting that dataset.

## Work Guidance

- Render the recorded build-map review instant in `America/Phoenix`, with an English calendar date, explicit AM/PM and Arizona timezone label, using standard-library timezone support. This is display-only: keep canonical UTC validation/date binding, evidence digests, historical records and repository activity unchanged; never read the current clock to format a review.
- Validate optional `build_plan` task IDs/dependencies against the cited task-definition file, explicit states against their evidence, and build-check update references. Bind mapping changes to `reviewed_build_plan_sha256` and a new review identifier; emit its nonpercentage repository ledger without extending the output allowlist.
- Keep generated prose plain English, with changed/why/next, useful limits and sources.
- Keep the fixed output contract synchronized with the workflow. Widening outputs or privileges needs explicit review and authority, not an incidental generator change.
- Every meaningful tool change updates tests, applicable contracts and exact generated output; retain failed checks until corrected and rerun.

## Verification

- Run `python3 -B -m unittest discover -s docs/status/tools -p 'test_*.py' -v`.
- Run `python3 -B docs/status/tools/update_tracker.py --write`, then `--check`.
- Use the generated-path guard in a clean actual Git checkout before and after generation; review the exact diff and render changed SVGs.
- Local fixtures do not certify Actions permission or remote publication. Verify the actual workflow separately.

## Child DOX Index

- None.
