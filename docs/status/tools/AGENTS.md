# Documentation tracker tooling

## Purpose

Generate the living public tracker from reviewed evidence and exact repository metadata, without game implementation, original inputs or semantic inference.

## Ownership

- `update_tracker.py`: schema checks and deterministic Markdown/SVG/receipt generation.
- `check_generated_changes.py`: Git worktree/staging allowlist, README marker and SVG safety checks.
- `test_tracker.py`: isolated offline documentation fixtures; never game or original-input tests.
- The parent owns authored evidence and maintenance prose. `.github/workflows/AGENTS.md` owns remote execution.

## Local Contracts

- Standard-library Python only, fixed output paths, no dependency installs, network calls, credentials, original inputs, services or runtime code.
- Generated targets are exactly `README.md` (marked block only), `docs/status/dashboard.md`, `docs/status/changes.md`, `docs/status/visuals/progress-dashboard.svg`, `docs/status/tracker-state.json`.
- Validate every output before mutation; refuse unsupported schema, missing evidence, private-content patterns, unsafe paths and symlinks. `--check` is read-only and never refreshes activity.
- Activity metadata cannot promote stages or change review dates/IDs. Filled stages require reviewed citations. A source-only NO-GO is not a test pass.
- Git metadata reads use exact full SHAs and argument arrays. Do not execute commit prose or introduce dynamic shell commands. No network Git operations are performed by these tools.
- Tests use owned temporary fixtures and local Git only. Do not copy private prototype/source/input trees into tests.

## Work Guidance

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
