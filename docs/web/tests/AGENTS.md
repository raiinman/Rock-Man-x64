# Documentation UI checks

## Purpose

Check the read-only tracker's projection, safe artifact construction and controller semantics without claiming game or browser acceptance.

## Ownership

- `site.test.mjs`: Node built-in model, render-string, request and mocked-DOM controls.
- `test_pages.py`: fixed artifact, job-permission/sequence, exact updater shell on disposable local bare Git origins and mocked read-only predeployment API controls; never deploys.
- `test_build.py`: Python standard-library artifact and standalone-preview controls; invokes Node only for generated-module syntax.

## Local Contracts

- Read the current canonical public data, never private implementation or inputs.
- Mutate only isolated copies/temporary directories. Preserve the first failing record when a defect is found; do not edit snapshots to manufacture acceptance.
- No network requests, server launch, browser-policy bypass, deployment, packages or credentials.
- Keep real browser/visual/keyboard acceptance distinct from the mock DOM and static CSS checks.

## Work Guidance

- Check heatmap tile identities/counts against canonical milestones, categorical labels independent of color, filtered totals without denominator drift, focused open/close behavior, evidence escaping/pinning and future-data changes. Static layout assertions are not browser acceptance.
- Cover strict acceptance/counts, overall independence, real deltas/rebaseline, review consistency, safe URLs/escaping, filter/navigation behavior, cancellation/races and fail-closed error states.
- Artifact checks must cover exact paths, source preservation, symlink refusal, checksum mismatch, standalone CSP hashes and closing-script injection.

## Verification

- From the repository root: `node --test docs/web/tests/site.test.mjs`.
- From the repository root: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s docs/web/tests -p 'test_*.py'`.

## Child DOX Index

None.
