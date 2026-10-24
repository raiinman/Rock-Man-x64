# Read-only interactive documentation tracker

## Purpose

Make the reviewed public roadmap understandable on a spacious, interactive canvas without creating another source of truth or publishing private runtime materials.

## Ownership

- Own `index.html`, `styles.css`, `model.mjs`, `views.mjs`, `app.mjs`, `build_site.py`, `check_site.py` and the reading guide.
- `docs/status/` owns canonical evidence, acceptance criteria, recorded observations, the generator and generated receipt. This UI only projects them.
- Public GitHub Pages hosting is explicitly approved. `.github/workflows/AGENTS.md` owns delivery/settings boundaries; this interface and builder never configure or deploy anything themselves. The updater's five-path write allowlist is unchanged.

## Local Contracts

- Use original dependency-free HTML/CSS/ES modules. No proprietary character art, copied project source, remote fonts/scripts, telemetry, accounts, writes, service workers or local storage.
- Read the exact canonical `dashboard-data.json` and `tracker-state.json` copied into the build artifact. Verify the JSON's SHA-256 against the receipt and both canonical file hashes against the deployed manifest before displaying data; a mismatch or invalid shape shows an error, not stale or invented acceptance. Display and pin repository citations to the exact deployed snapshot revision. These hashes are consistency checking, not a signature or independent proof of the private evidence.
- Compute each percentage from that named checklist's reviewed flags. Overall means accepted unequal-size roadmap milestones, never an average of workstreams, game-finished percentage, weighted effort or ETA.
- Preserve last evidence review versus repository activity. Hourly check-ins are authored, time-identified reviews under the existing documentation cadence, not an animated UI clock or automatically advanced acceptance. Show only recorded deltas; changed definitions rebaseline. Never infer active work from commits, partial tests or an agent-like UI.
- Status filters repeat reviewed acceptance and explicit blocked/NO-GO classes. `in_progress` requires an explicit compatible status in reviewed data. Pending means unaccepted, not necessarily untouched.
- Keep citations and exact evidence limits accessible in expanded criteria. Native boot remains unestablished; research execution is not native acceptance. Preserve restricted-source provenance.
- `check_site.py` rejects extra files/directories, links, mismatched bytes/reviews/revisions and oversized artifacts before upload. The public artifact is exactly five UI files, two canonical JSON files and its manifest.
- The builder writes only a new external artifact directory with a fixed file list. It never modifies source files, launches a server, fetches dependencies or deploys. The optional self-contained HTML is a separately labeled private preview, not an alternative canonical evidence file.

## Work Guidance

- Use original deep warm armor-red/charcoal/ivory/gold styling, restrained mechanical gloss and tiny cyan selection accents, never pink/magenta or invented telemetry. Overview is a full-page equal-area categorical milestone heatmap with large accepted/total counts; textual status and symbols must remain understandable without color. Tile area does not imply equal effort. Click/keyboard detail regions show exact criteria/evidence and restore focus when closed; retain Roadmap, Workstreams, Findings and Change history.
- Support responsive heatmap and list/board views, search, status filters, keyboard-operated controls, native expandable criteria and shareable hash routes. Do not pretend dragging cards would change public project state.
- Draw decorative diagonal direction markers with CSS geometry, not a font-specific Unicode glyph; retain link text and hide decorative geometry from assistive technology.
- Escape every data string; keep evidence links HTTPS or validated repository-relative paths. Production CSP admits only same-origin code/styles/data and no forms or embedded objects.
- Preserve the repository chart/ledger fallback. Do not call a snapshot live or claim publication without verifying the actual public artifact.

## Verification

- Run `node --test docs/web/tests/site.test.mjs` and `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s docs/web/tests -p 'test_*.py'`.
- Run the canonical status generator's existing checks separately when assembling a publication; UI tests do not replace evidence/history checks.
- Build a new artifact and optional standalone preview with `build_site.py`; verify fixed output paths, byte-identical canonical data, CSP hashes and escaped embedded JSON.
- Node controller fixtures use a mock DOM. They do not establish browser behavior, pixels, screen-reader acceptance or responsive layout. Record actual browser checks separately and never bypass a denied browser route to obtain them.

## Child DOX Index

- [tests/AGENTS.md](tests/AGENTS.md) owns bounded offline projection, controller and artifact checks.
