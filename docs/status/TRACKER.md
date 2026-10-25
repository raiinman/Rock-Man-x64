# Keeping the living tracker current

## What changes automatically, and what never does

The approved `update-progress.yml` workflow is configured for pushes to `main`,
only while `main` is the default branch. Its updater job reads the exact triggering commit,
runs the documentation-tool tests, regenerates the five allowlisted outputs and
makes a non-force documentation commit only if that triggering head is still
current. That job never builds the game, deploys, changes settings, creates secrets or
grants implementation clearance. The separately approved downstream Pages jobs build
and deploy only the read-only documentation site; see the [delivery contract](../web/DEPLOYMENT.md).
A passing updater or site build is not a successful deployment. Actual execution must be checked in
[Actions](https://github.com/raiinman/Rock-Man-x64/actions/workflows/update-progress.yml).

**Repository activity is not evidence acceptance.** The latest observed commit
and the last evidence review are displayed separately. If the evidence data and
its review identifier did not both change, a newer repository change is marked
review-pending, not converted into a native capability. If they did both change,
the tracker says an authored evidence update was supplied; changed stages or stage citations without a new review identifier are refused before generation. That is still not an
independent machine review or proof of the underlying test result.

No text parser, commit counter or time-based animation advances the bars. The default chart uses named finite acceptance checklists, each with a versioned denominator, explicit done criteria and source links. Its percentage means accepted criteria divided by the criteria in that checklist—not effort or total game progress. The evidence-class matrix remains secondary and overlapping. An unchanged bar is correct when no new accepted criterion exists; plain-English findings can still improve.

## Team completion requirement

Every meaningful Rock Man change is incomplete until its owner:

1. Updates `dashboard-data.json`: describe **what changed**, **why it matters**,
   **what comes next**, current blockers and the exact evidence class/source.
   Add a stable-ID change entry; preserve prior failures and corrections.
2. Updates `last_evidence_review` with a new review identifier, actual review date,
   reviewed repository basis and a concise scope summary. Do not advance the date
   or identifier merely because the updater ran. Research authors may add
   research findings; they may not promote native evidence from reference work.
3. Changes a workstream stage or a named checklist acceptance only after review of its cited evidence. Each filled
   stage requires a source. A source-only NO-GO is not implementation or runtime
   acceptance; a Windows synthetic pass is not pixel or game-boot acceptance.
4. Adds plain-English `plain_status` and `next` changes where relevant. Keep
   uncertainty, blocked/denied/pending status and source-provenance limits visible.
5. Appends one numeric observation matching the new evidence review ID, date and basis commit. Record each checklist version and exact accepted criterion IDs. Do not edit earlier observations or insert multiple historical points in one transition. The updater permits one newly bound observation per review transition; a separately evidenced historical import is not supported by this path. A changed item set or done criterion needs a new version; its percentage is a rebaseline, not a same-plan improvement.
6. Runs the updater, tests and drift check below. Generated files are never edited
   manually. Review the rendered text/SVG and exact diff for scope and privacy.
7. Publishes through the authorized update path, then verifies the actual workflow
   result and generated commit. A green local check alone is not a published or
   remotely refreshed tracker. Report a failed/skipped/pending update explicitly.

Unrelated projects, private source/input bytes, captures, personal paths,
credentials and private packages remain excluded. A successful updater never
clears PSX-SPX, Sony/firmware or test-oracle provenance.

## Source and outputs

- **Reviewed source:** `dashboard-data.json` (schema 3).
- **Observed repository metadata:** `tracker-state.json` (schema 2); generated receipt,
  never an authority for native completion.
- **Generated outputs only:** the marked README tracker block,
  `docs/status/dashboard.md`, `docs/status/changes.md`,
  `docs/status/visuals/progress-dashboard.svg`, `docs/status/tracker-state.json`.
- The two dated findings boards are secondary archived illustrations. The
  generated Markdown and reviewed data own current facts.

The updater uses Python's standard library and needs no installed packages,
network calls or original inputs. From the repository root:

```sh
python3 -B docs/status/tools/update_tracker.py --write
python3 -B -m unittest discover -s docs/status/tools -p 'test_*.py' -v
python3 -B docs/status/tools/update_tracker.py --check
```

In a real Git checkout, refresh metadata for the exact known commit with:

```sh
python3 -B docs/status/tools/update_tracker.py --write --refresh-activity "$(git rev-parse HEAD)"
```

The connected documentation publication path may instead supply `--activity-json`
with the exact connector-observed commit's `sha`, `committed_at`, `subject` and
`source`. Optional boolean `evidence_data_changed` and `review_id_changed` must
come from an actual commit comparison; omit them if unverified. This input is
metadata, not code. Do not label connector observation as an executed workflow.

`--check` never refreshes activity or writes. The separate
`check_generated_changes.py` requires a Git checkout and rejects any generated
change outside the five exact output paths, changes outside README markers,
renames, symlinks or executable/external SVG content.

## What the numeric chart measures

The overall v1 roadmap and five local v1 checklists were frozen on 2026-10-23 from named goals and existing public acceptance records. They are useful measurement plans, not exhaustive project backlogs or equal-sized work units:

- **Overall roadmap:** 5/20 named milestones accepted (25% of that roadmap), comprising five bounded foundations and fifteen pending production goals. The full twenty-item [criteria ledger](dashboard.md#roadmap--accepted-roadmap-milestones) covers native boot, scene lifecycle, rendering, animation, controls/camera, collision, AI/combat/progression, audio, game saves, actual Windows inspection, live/full IDE, provenance, packaging and end-to-end acceptance. The milestones are unequal-sized; effort-weighted completion is unknown. This is not 25% of the game finished and is not calculated from local percentages.
- **Frozen inspection delivery:** 4/7 separately scoped acceptance goals. Linux capture/import and Windows synthetic viewer/host checks do not establish the remaining real launcher, pixels or actual-capture display.
- **Data-only observation path:** 2/4 named goals; platform and integration goals overlap and are not independent effort units.
- **Selected loader checkpoints:** 3/4 bounded native-policy checkpoints, not 75% of a complete loader or BIOS equivalence. The actual-input initializer remains blocked; the chart does not authorize a retry.
- **Live controller safety gates:** 0/4 necessary admission gates, not an exhaustive proof that four closures alone would finish S2.
- **Native game boot acceptance:** 0/1 binary acceptance goal, not zero development or a game-completion estimate.

The exact done criteria and sources live in [the generated ledger](dashboard.md#named-checklists). The first observation is a baseline from existing evidence, not a claim that those goals were just completed. No earlier numeric history is fabricated. Later deltas count changed accepted goals only within the same checklist version. Version changes show **rebaseline**. Validation cards (69/69, 111/111, 50/50) are pass rates for identified bounded suites, never checklist acceptance inferred from test volume.

The SVG is code-generated by the existing updater, not a manually maintained picture. GitHub README cannot execute an interactive JavaScript chart; rendering the deterministic SVG on each eligible push gives a visible chart without hosting, deployment, a new route or additional permissions. The workflow's five-output allowlist is unchanged.

## Trigger, race and authorization boundaries

- The updater job's only action is official `actions/checkout` pinned to immutable
  `11bd71901bbe5b1630ceea73d27597364c9af683` (v4.2.2); its tag target was checked
  before this proposal. No package install, external script or AI inference runs.
- The workflow grants only `contents: write` to the updater job. Checkout uses the ephemeral job token to authenticate the fetch but does not
  persist credentials. The final Git push step separately receives that token.
  Its `contents: write` permission is repository-scoped, not per-file; the fixed
  generated-path guard enforces the narrower write contract. No PAT or new
  repository secret is required.
- No pull-request or `pull_request_target` trigger executes untrusted PR code
  with a write token. Trusted default-branch authors can change the workflow;
  this is not protection against a malicious repository maintainer.
- One concurrency group prevents simultaneous updater jobs. A newer pending push
  may supersede an older pending run; the latest head is the useful outcome, not
  one generated commit per input commit. The expected-head check and normal
  non-force push refuse a race. No rebase, force-push or retry overwrites others.
- Generated pushes use `GITHUB_TOKEN`, which does not trigger another push
  workflow; the bot-actor guard is an additional loop barrier. No `[skip ci]`
  marker suppresses unrelated future checks.
- If repository policy denies the job token's push, report that exact failure.
  Do not change branch protection, workflow permissions or settings to bypass it.
  An owner-approved policy adjustment would be a separate action.

References: [GitHub trigger/token behavior](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow),
[GitHub concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency),
[checkout v4.2.2](https://github.com/actions/checkout/releases/tag/v4.2.2).

## Separate build and specification plan map

`dashboard-data.json` may contain a reviewed `build_plan` mapping. Its task IDs, plain-English labels, dependency links, explicit Planned/Implemented/Tested/Blocked states and citations project the specification task definitions into the separate `#build-plan` route and generated ledger. The generator checks the ID/dependency mapping against the cited Markdown; changing a checkbox never changes a state. Nonplanned task states require specific reviewed evidence and remain separate from milestone acceptance.

Build-check records resolve existing update IDs rather than restating test outcomes. A bounded synthetic Windows interaction does not complete a broader inspection task or prove native game boot. Record review time, scope and remaining limits; no overall game percentage or live worker state is calculated. The receipt binds this mapping separately, and mapping changes require a new evidence review identifier. All historical criteria, observations and acceptance flags retain their existing authority. The Pages artifact and five generated output paths are unchanged.

Every hourly documentation review must include `#build-plan` alongside the separate historical acceptance review. Check its canonical task states and dependencies, bounded build-evidence records, current blockers and next tasks. Record the actual performed review time in `build_plan.reviewed_at` and the bound review summary/observation, including honest zero-delta reviews; do not advance time because a job ran or infer completion from checkboxes, commits or elapsed time. Preserve all criteria and prior history. The existing hourly documentation cadence owns scheduling; this adds no separate schedule.
