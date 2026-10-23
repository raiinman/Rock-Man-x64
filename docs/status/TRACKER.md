# Keeping the living tracker current

## What changes automatically, and what never does

The approved `update-progress.yml` workflow is configured for pushes to `main`,
only while `main` is the default branch. It reads the exact triggering commit,
runs the documentation-tool tests, regenerates the five allowlisted outputs and
makes a non-force documentation commit only if that triggering head is still
current. It never builds the game, deploys, changes settings, creates secrets or
grants implementation clearance. Actual execution must be checked in
[Actions](https://github.com/raiinman/Rock-Man-x64/actions/workflows/update-progress.yml).

**Repository activity is not evidence acceptance.** The latest observed commit
and the last evidence review are displayed separately. If the evidence data and
its review identifier did not both change, a newer repository change is marked
review-pending, not converted into a native capability. If they did both change,
the tracker says an authored evidence update was supplied; changed stages or stage citations without a new review identifier are refused before generation. That is still not an
independent machine review or proof of the underlying test result.

No text parser, commit counter or time-based animation advances the bars. The
five positions represent overlapping evidence classes—not equal effort, a stable
task denominator or percentage complete. An unchanged bar is the right result
when no new accepted evidence exists. Plain-English findings can still improve.

## Team completion requirement

Every meaningful Rock Man change is incomplete until its owner:

1. Updates `dashboard-data.json`: describe **what changed**, **why it matters**,
   **what comes next**, current blockers and the exact evidence class/source.
   Add a stable-ID change entry; preserve prior failures and corrections.
2. Updates `last_evidence_review` with a new review identifier, actual review date,
   reviewed repository basis and a concise scope summary. Do not advance the date
   or identifier merely because the updater ran. Research authors may add
   research findings; they may not promote native evidence from reference work.
3. Changes a workstream stage only after review of its cited evidence. Each filled
   stage requires a source. A source-only NO-GO is not implementation or runtime
   acceptance; a Windows synthetic pass is not pixel or game-boot acceptance.
4. Adds plain-English `plain_status` and `next` changes where relevant. Keep
   uncertainty, blocked/denied/pending status and source-provenance limits visible.
5. Runs the updater, tests and drift check below. Generated files are never edited
   manually. Review the rendered text/SVG and exact diff for scope and privacy.
6. Publishes through the authorized update path, then verifies the actual workflow
   result and generated commit. A green local check alone is not a published or
   remotely refreshed tracker. Report a failed/skipped/pending update explicitly.

Unrelated projects, private source/input bytes, captures, personal paths,
credentials and private packages remain excluded. A successful updater never
clears PSX-SPX, Sony/firmware or test-oracle provenance.

## Source and outputs

- **Reviewed source:** `dashboard-data.json` (schema 2).
- **Observed repository metadata:** `tracker-state.json`; generated receipt,
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

## Trigger, race and authorization boundaries

- The only action is official `actions/checkout` pinned to immutable
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
