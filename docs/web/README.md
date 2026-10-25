# Project and progress

**[Open the public tracker](https://raiinman.github.io/Rock-Man-x64/).** The [live-delivery record](../history/validation-history.md#live-tracker-and-owner-observed-inspector-evidence--october-23) separates actual hosting/browser evidence from offline checks.

The entrance explains the project and its current lack of a public playable download, then offers direct paths to the roadmap, research and documentation. Its navigation takes the owner’s Atlas control-center approach: clear destinations first, technical detail on demand. The README’s original concept illustration is labeled as documentation art and is deliberately excluded from the fixed Pages artifact.

A spacious, read-only view of the **same reviewed roadmap** used by the repository chart: Heatmap, Roadmap, Workstreams, Findings and Change history. It is original vanilla HTML/CSS/ES modules, without framework dependencies or external assets.

## Heatmap reading guide

The default view fills the page with **equal-area milestone tiles**, not a weighted effort treemap or activity calendar. Warm armor red + ✓ means accepted; charcoal + ○ means pending; amber hatching + ! means explicitly blocked; ◐ appears only for an explicitly recorded in-progress state. Every tile also spells out its status. Pending does not mean untouched. Search and status filters never change the overall denominator.

Open a tile by click or keyboard to read its exact done criterion, evidence class, project blocker, next step and pinned sources. Details are a nonmodal region: focus moves there on opening and returns to the tile on closing. The existing Roadmap list/board, bounded Workstreams, Findings and Change history remain available. Their overlapping percentages are never summed into the roadmap.

The visual direction is an original mechanical engineering display: deep warm red, charcoal, ivory and restrained gold, with cyan only for selection/focus. It uses no character art, logos, copied HUD assets or fictional telemetry. The prior site's actual browser record does not establish browser acceptance for this new heatmap; verify the deployed revision separately.

## What the numbers mean

The overall figure counts accepted, unequal-size **roadmap milestones**. It is not the percentage of a finished game or effort completed. Local checklists and bounded test suites have their own denominators and are not averaged into the roadmap. Expand a criterion to read its exact acceptance rule, evidence class and source.

Accepted uses reviewed `done` flags. Blocked repeats explicit blocked/NO-GO evidence; in progress appears only when explicitly recorded. Pending means not accepted, not that no partial work exists. The interface never edits evidence, moves tasks, starts agents or controls the native runtime.

## Source of truth and updates

- [Canonical data](../status/dashboard-data.json) owns criteria, findings and reviewed changes.
- [Generated receipt](../status/tracker-state.json) binds the exact JSON checksum and separates reviewed evidence from repository activity.
- [Tracker maintenance contract](../status/TRACKER.md) owns evidence review, append-only observations and team upkeep.
- [Repository chart and ledger](../status/dashboard.md) remain the non-interactive fallback.

The build copies those exact public files; the browser verifies their checksum before rendering. This is consistency checking, not independent authentication of private test evidence. A site artifact is a snapshot of its exact post-updater revision, displayed in the header and used to pin repository evidence links. Refresh the page to load the latest successfully published artifact; an already open page does not claim to stream live native work.

The owner approved public GitHub Pages hosting. The existing `update-progress.yml` chains updater → build-site → deploy-site, so it publishes the final generated data without relying on a bot commit to trigger another push workflow. The updater still commits only its five fixed generated paths. Build uses read-only repository access; only the separate Pages deployment job receives Pages/OIDC write scopes. No new secret, custom domain, game build or deployment service is used.

The workflow refuses superseded snapshots before build/deploy; those checks cannot atomically prevent a push immediately after the last check. The next eligible run publishes the newer snapshot. Verify every later publication against its displayed snapshot and artifact; the first live-delivery record does not certify all future deployments or every browser/accessibility behavior. See [deployment operations](DEPLOYMENT.md).

## Build and checks

From the repository root, using Python 3 and Node already available in the development environment:

```sh
node --test docs/web/tests/site.test.mjs
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s docs/web/tests -p 'test_*.py'
python docs/web/build_site.py --output ../tracker-artifact --preview-html ../tracker-preview.html --source-revision EXACT_40_CHARACTER_COMMIT
```

Run `python docs/web/check_site.py ../tracker-artifact --source-revision EXACT_40_CHARACTER_COMMIT` before upload.

Both output paths must be new and outside the source tree. No server, installation, network operation or deployment occurs. The production artifact contains only five UI files, two exact public data files and a hash manifest. The optional single-file HTML preview embeds the same code/styles and sanitized snapshot, blocks network connections, and clearly labels itself a snapshot. It is not included in the production artifact or committed as a second source of evidence.

The owner can open that standalone HTML in a normal browser without installing anything or changing security settings. If a managed browser prohibits local files, respect that policy; use an authorized delivery/hosting route rather than bypassing it. Evidence links open the public GitHub documentation when clicked.

The Node tests use a **mock DOM**, not a real browser. Artifact checks do not establish pixels, screen-reader behavior, touch layout or real keyboard acceptance. Those require an actual supported browser check and must be reported separately.
