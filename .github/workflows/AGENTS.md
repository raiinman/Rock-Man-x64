# Living tracker workflow

## Purpose

Refresh documentation after eligible default-main-branch pushes using reviewed source data and separate repository activity metadata.

## Ownership

- `update-progress.yml` is the sole approved workflow here.
- `docs/status/tools/` owns the offline updater/tests/allowlist. `docs/status/TRACKER.md` explains contributor obligations.

## Local Contracts

- Push trigger on `main` only, with an explicit current-default-branch check; no PR, pull_request_target, deployment or arbitrary dispatch route.
- Official checkout is pinned to an inspected immutable SHA. No external dependency installation or code downloads beyond that checkout.
- Only the updater job receives `contents: write`. Checkout uses the ephemeral job token for fetching but does not persist credentials; the final push separately receives that token. `contents: write` is repository-scoped, not per-file: the reviewed fixed-path guard enforces the generated-only contract. No PAT, additional secret or settings change.
- Exact generated-output allowlist: marked README block, dashboard Markdown, change ledger, evidence SVG and tracker-state JSON. Refuse extra dirty/staged paths or README edits outside markers.
- Run scoped fixture tests, updater and drift/allowlist checks before staging. Commit only named outputs, preserving authored evidence, research, license and unrelated changes.
- Serialize updater runs, avoid self-trigger loops, compare the remote head to the exact triggering SHA and use a normal non-force push. If superseded, do not overwrite, rebase or force; a newer pending run handles the newer head.
- Actual run success and exact generated output must be verified after publication. Local checks cannot establish remote token permissions. A policy denial requires an explicit owner decision; no bypass.

## Work Guidance

- New pushes refresh activity, not accepted native capability. Evidence stages move only through reviewed authored data; research remains separately classified.
- Do not add skip-ci markers, deployments, artifacts containing private inputs, game commands or expanded permissions.

## Verification

- Run the documentation fixture suite and inspect trigger, token, output, loop and race guards.
- Verify action pin identity before changing it; preserve no-force and expected-head behavior.
- Read the actual remote run and compare changed output paths and commit parent before declaring the tracker refreshed.

## Child DOX Index

- None.
