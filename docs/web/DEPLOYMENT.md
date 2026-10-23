# Public tracker deployment

## Authorized target

Only this repository's original read-only documentation tracker on GitHub Pages. No private runtime, assets, inputs, reports or package enters the site. Hosting approval does not change milestone acceptance or authorize other services.

Required repository setting: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Preserve any existing `github-pages` environment protection; ordinary Pages setup may create that environment. Do not weaken protection, add a custom domain, mint credentials or change unrelated settings. The expected project URL is `https://raiinman.github.io/Rock-Man-x64/`; verify the deployment's actual returned URL before announcing it. [GitHub publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## Exact sequence

The existing main-push workflow is deliberately one chain:

1. **update** runs the established evidence/history tests, refreshes activity, checks the five generated paths and uses an expected-head non-force push. It exports only a verified final commit, or the current trigger commit when no generated change is needed. A superseded run exports nothing.
2. **build-site** checks out that exact commit with read-only repository access, refuses a superseded head, checks canonical drift, runs UI/artifact tests and builds a new external directory. The checked artifact is exactly `index.html`, `styles.css`, `model.mjs`, `views.mjs`, `app.mjs`, two canonical JSON files under `data/`, and `build-manifest.json`. The standalone owner preview is excluded.
3. **deploy-site** performs a fixed read-only current-main check and invokes the official Pages deployment action, with only repository read, Pages write and OIDC-token write permissions. It executes no checked-out repository code. The artifact is retained for one day.

A bot-token commit does not need to trigger another workflow: the downstream jobs already belong to the originating run. A failed/skipped updater cannot produce a deployment. [GitHub token trigger behavior](https://docs.github.com/en/actions/concepts/security/github_token), [linked Pages build/deploy jobs and permissions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

The predeployment head check is not atomic with publication. A main push immediately afterward can briefly leave an older artifact visible until the next eligible run completes. The page's **Site snapshot** revision identifies its actual data; the evidence-review date is a separate measurement. GitHub's deployment record references the originating workflow commit, while the artifact binds the post-updater commit. Do not confuse them.

## Pinned official actions

- [checkout v4.2.2](https://github.com/actions/checkout/blob/11bd71901bbe5b1630ceea73d27597364c9af683/action.yml)
- [upload-pages-artifact v4](https://github.com/actions/upload-pages-artifact/blob/7b1f4a764d45c48632c6b24a0339c27f5614fb0b/action.yml); its nested upload-artifact is also pinned at `ea165f8d65b6e75b540449e92b4886f43607fa02`.
- [deploy-pages v4](https://github.com/actions/deploy-pages/blob/d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e/action.yml)

No automatic Pages-enablement action, dependency installation, new secret or alternate hosting route is used.

## Publication verification

- Verify the exact remote source commit, successful updater and generated commit parent/path set.
- Verify build/deploy terminal outcomes; a skipped superseded deployment is not a newly published site.
- Fetch the public manifest and both canonical JSON files. Match source revision, evidence review and file hashes to the checked artifact; check public access and the actual returned site URL.
- In a supported browser, check desktop/phone widths, all five routes, list/board/filter/search, direct criteria, Back/Forward, keyboard focus/skip link, rapid input+filter changes, retries and repeated navigation. Record screenshots and actual results separately from mock-DOM tests.
- Keep the README chart and evidence ledger available if the site fails. No test or green workflow implies native game boot.

If a deployment fails after a setting is corrected, inspect its exact error and rerun the failed downstream job while its artifact remains available. A complete rerun of an old trigger may correctly skip because main already advanced; do not force a stale deployment or fabricate a progress update. Obtain a fresh eligible reviewed update when needed. Verify uncertain outcomes before retrying and never bypass a denied permission or browser route.
