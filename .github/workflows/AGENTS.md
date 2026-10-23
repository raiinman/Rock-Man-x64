# Documentation tracker and Pages workflow

## Purpose

Refresh reviewed documentation after eligible default-main pushes, then publish the exact post-updater public tracker snapshot to GitHub Pages.

## Ownership

- `update-progress.yml` is the single workflow: `update`, then `build-site`, then `deploy-site`.
- `docs/status/tools/` owns the evidence generator, fixture suite and five-file repository guard. `docs/web/` owns the read-only interface, fixed eight-file artifact and its checks.

## Local Contracts

- Main push only, with the current-default-branch and updater-bot checks. No PR, pull_request_target, dispatch route or untrusted artifact consumption.
- The existing updater alone has `contents: write`; its repository-scoped token is constrained operationally by the reviewed exact-output guard, not by per-file token permissions. Checkout authenticates with the job token but does not persist it; the final push separately receives it. No PAT/new secret.
- Updater outputs remain exactly the marked README block, dashboard Markdown, change ledger, evidence SVG and tracker-state JSON. Refuse extra dirty/staged paths, unsafe SVG or README changes outside markers. Run existing tests/checks before staging.
- Serialize the complete workflow with `cancel-in-progress: false`; retain expected-head checks and normal non-force push. A superseded updater exports no snapshot. A successful no-op exports its exact triggering commit; a successful generated push exports the verified final commit only after the remote check.
- `build-site` receives only `contents: read`, checks out that exact exported commit, checks it against current main, checks canonical drift, runs bounded UI/artifact tests and uploads only the eight-file checked public site. No standalone preview, repository tree, private inputs, installed dependencies or source mutation enters the artifact.
- `deploy-site` receives only `contents: read`, `pages: write`, `id-token: write`. It does not check out or run repository source. Its fixed read-only API check refuses a superseded head before invoking the pinned official deployment action. Its only deployment target is the `github-pages` environment; preserve existing protection rules.
- Official actions and the upload composite's nested action are inspected immutable SHAs. No configure-pages auto-enablement, new credentials, game commands or unrelated deployment.
- Build/deploy run after the updater in the same workflow: bot-generated commits need not trigger another push. A failed/skipped updater cannot publish a new site. Rechecks narrow, but cannot atomically eliminate, a main-push/deployment race; the next eligible workflow publishes the newer snapshot. The visible artifact revision is authoritative for what a page contains.
- GitHub's deployment record refers to the original workflow-triggering commit; the artifact manifest/header binds the actual post-updater snapshot. Verify both, not merely the green workflow icon.

## Work Guidance

- Repository activity is not native acceptance. No data prose parser or public UI promotes capability.
- Pages must use the GitHub Actions publishing source; no custom domain, new token, protection relaxation or alternate hosting route is needed.
- On failure, preserve the exact error. Retry only with materially relevant evidence/fix and verify uncertain outcomes first; do not route around denied settings, token or browser policies.

## Verification

- Run canonical tracker fixtures/drift checks plus Node/Python `docs/web/tests/` controls.
- Inspect exact permission, trigger, output, pin, artifact, skip and race behavior. Local fixtures cannot certify remote token or Pages access.
- After publication verify the updater commit parent and five changed paths, the built manifest/JSON hashes, actual Pages deployment/URL, and real browser desktop/mobile/keyboard behavior. Keep the repository chart fallback.

## Child DOX Index

None.
