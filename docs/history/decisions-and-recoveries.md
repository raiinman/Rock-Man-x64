# Decisions, failures and recoveries

This record preserves unsuccessful attempts and unresolved questions alongside successful milestones. Dates are 2026-10-22 unless otherwise stated; sequence is not a precise execution timetable.

| Issue or decision | What happened | Recovery or current boundary |
|---|---|---|
| Native reconstruction rather than an existing port | An early comparison/recommendation considered existing projects; the user rejected that foundation. The settled goal combined a Windows game and integrated IDE, while excluding existing game ports/mods and game-specific reverse-engineering implementations. | Independent analysis of supplied originals and new native implementations; no formal legal clean-room certification. |
| Preserve original inputs | Archive and track identities were recorded before analysis. | Read-only original inputs; edits use bound sidecars. Public documentation does not distribute them. |
| XA header anomalies | 760 duplicated subheaders differed; Form2 EDCs were zero. | Preserve both copies, label integrity unverified, do not invent repairs or infer audibility. Form1 validation is a separate successful result. |
| Initial Windows-toolchain installation | The elevated install failed during sandbox setup before package operations. | Official signed packages were staged locally without system installation or changes to the denied location. |
| Wine startup failure | Initial invalid-pointer abort occurred before program output. | A process-local environment adjustment removed that failure; normal Wine IPC was then denied. No passing Wine smoke result or sandbox bypass is claimed. |
| Launcher packaging mistake and correction | Read-only inspection confirms an older inspector package launcher contained an execution-policy bypass option. | It was replaced by a policy-safe package removing that option and telling users not to change protections. There is no evidence here that the old launcher successfully ran or changed Windows protections. |
| Windows VPS script-signing block | At 15:46:03 UTC the user reported the policy-safe unsigned runner was blocked with an authorization failure. | The restriction was not evidence that native code failed. No policy relaxation is claimed. Later direct synthetic tests and, after explicit authorization at 18:03:41 UTC, the separate Windows test-machine workflow supplied execution evidence. |
| Linear texture interpretation | Initial textures were incorrectly treated as full-width scanlines. | Original upload traversal proved tiled layout. Decoder and a tile-order regression were corrected; length-only tests were recognized as insufficient. |
| Container stride assumptions | Declared archive sector counts did not always equal physical stride, especially texture/palette records. | Recover per-kind physical traversal; reject unsupported kinds instead of scanning ahead and calling the request complete. |
| Duplicate polygon packets | Two copies could have been mistaken for separate geometry. | Renderer evidence established double-buffered packet workspaces. |
| Pose and sequence assumptions | Root placement, sparse packed axes, overlapping writes, zero duration and `FF` control required explicit recovery. | Preserve observed semantics. Manual updates are not an invented animation frame rate; diagnostic float transforms are not fixed-point/GTE parity. |
| Scene interpretation | Static ST1C geometry was visually useful but not startup. Unknown orientation and visibility fields remained. | Recover ST01 separately; retain union/subset labels and reject unsupported variants rather than inventing placement or gameplay identity. |
| Dispatch linkage correction | One installed nonzero table value was data, not an executable handler. | Establish the second-level lookup before translating the bounded surface path; numeric tags never become native function pointers. |
| Fixture versus real startup | Explicit fixtures could connect later setup/update work before real initialization was available. | Keep diagnostic mode separate and report its first unknown input. Do not supply fictional graphics arenas or readiness to make the game appear booted. |
| Missing native service semantics | Heap/events/context/IRQ/DMA/ISO/CD dependencies initially stopped forward progress. | Implement one owned contract at a time, keeping unknown masks, pending obligations and retry boundaries rather than accepting no-op success. |
| Timer width/timing uncertainty | Source requested a specific word-width mode write, but broader physical equivalence was unproved. | Support a narrow native semantic policy; do not generalize it to hardware timing or treat reset snapshots as live counts. |
| Cold versus inherited resources | Original firmware resources could not be assumed absent from an unspecified launch. | Explicit independent-native cold-start policy; unknown-inherited mode refuses teardown instead of erasing unproven resources. |
| Initial Windows inspector core failure | The first sandboxed core run failed atomic sidecar replacement; the previous save was preserved. | A separately approved normal-permissions run passed. The precise underlying Windows error was not captured, so the cause is not overstated. |
| Windows GUI evidence limits | A real window/message loop and synthetic controls were exercised; screenshots of rendered desktop pixels were unavailable in the delegated run. | Record HWND/control/message-loop evidence accurately. Paint dispatch does not prove pixel correctness or original-asset GUI parity. |
| Evidence transfer limitation | An evidence-upload helper failed before preparation because the required upload operation was unavailable. | Preserve the executor report and original local receipts. Do not claim a transferred evidence archive or successful upload. |
| Raw-image readiness | Download/extraction and hash checks initially established only input preparation. | Separate later immutable-media lease and real-sector-read tests from acquisition. Still no inference of boot from either. |
| Response versus completion | Status could be prepared/published and IRQ latched while routing/consumption were absent. | Distinct preflight, response, notification and IRQ-chain milestones. Only the chain milestone claims first source-command completion. |
| Configuration aggregate uncertainty | A shared-tree runner lost transport; its process outcome could not be established. A subsequent aggregate began before uncertainty was resolved. | Neither attempt counts as final acceptance. Move to isolated copies/outputs and pinned source/input identities; no denied cross-namespace inspection workaround. |
| Isolated fixture omissions | Two standalone component checks lacked expected preview fixtures. | Treat as actual failed checks needing fixture repair and rerun, not a clean aggregate pass. The already-running aggregate drained at 21:39:13 UTC with 17 successful stages of 19, acceptance false and no retries. No repair work was resumed after the pause. |
| Scratch mixer/packager scope | Arithmetic and packaging helper tests succeeded outside the project. | Keep them scratch-only; no integration, audio playback or new release implied. |
| Publication boundary changed | Early notes prohibited public publication; the user later explicitly requested a public repository and full history. | Publish sanitized documentation only within the current task. No ROM, extracted assets, raw instruction evidence, private archives or access details. |
| Development paused for documentation | The latest request prioritized recording the entire history. | Do not quietly resume development, native testing, Windows-machine execution or release creation as part of documentation. |

## Recurring engineering decisions

- Unknown values carry explicit knownness; zero-filled storage is not evidence of zero.
- Original numeric addresses are data/provenance tags, never permission to execute original code or dereference host memory.
- Allocation failure must not hide committed work or cause it to replay. Owner/generation/revision checks and no-allocation commit boundaries support this rule.
- Accepted reads, callbacks, responses and routing obligations remain pending until real supported work discharges them.
- Unsupported behavior is an honest endpoint, not a successful stub.
- Frozen releases remain unchanged while newer candidates are investigated.
- Test-count growth is historical evidence, not a percentage-complete metric.

## Subsequent corrections retained — October 23 documentation update

- **Mixer contract counters:** frozen summaries remained 40/18/21 while the actual definitions were 51/20/30. All 51 Windows comparisons passed against actual definitions. Preserve the old freeze; separate strict preflight now rejects inconsistency, with 22 synthetic tests passed.
- **Pinned evidence attribution:** an older regression log compiled a shared tree, not the final pinned candidate. That attribution was corrected; the later actual pinned 51-case run passed.
- **Result-copy expectation:** the first new-profile assertion expected eight bytes instead of the cumulative 16 from two actual copies. Retain the failed test expectation and the corrected pinned-fixture evidence.
- **Allocation failure coverage:** early bounds of 64/512 were insufficient, and a later whole-call rollback assertion incorrectly rejected legitimate committed response publication followed by IRQ diagnostic failure. Targeted same-operation, debt, no-duplicate and retry checks then passed; no runtime rollback was added and exhaustive coverage is not claimed.
- **Lifecycle guard:** a stale-reader/raw-mode bypass was found and guarded before the candidate pin. Earlier feature profiles remained unchanged.
- **Acceptance boundary:** the mode-00 candidate remains unsealed and not Windows-tested; the original aggregate attempt is inconclusive and excluded. A fresh isolated rerun started, with no terminal full-project receipt yet. Static graphics planning is not executed GPU initialization.

## Recovery and synthetic Windows runner failures — October 23, 01:05 update

- **Recovery aggregate:** the later isolated 13-stage attempt passed with unchanged source/input identities; preserve the earlier inconclusive attempt instead of recasting it as successful.
- **Synthetic supervisor candidates 3–5:** each rejected the first success fixture because of additional/inconsistent process association and accepted zero checks. Exact fixture output and exit 0 did not satisfy supervisor acceptance. Later tests were not run. Cleanup observed the owned job empty and direct child ended.
- **Identity limit:** the fifth candidate's current-member basename was diagnostic evidence only, not authenticated image identity or historical process continuity. No basename whitelist or uncontained fallback was used.
- **Next runner candidate:** console-detached candidate 6 subsequently passed all 15 synthetic Windows checks, including deliberate descendants, timeouts and forced-supervisor-termination cleanup; its 14-file kit remained unchanged, with no protection override or unresolved cleanup. Synthetic runner acceptance remains distinct from a real Windows mode contract.
- **Provenance:** retained cross-toolchain distribution linkage improved, but nine host shared dependencies have pinned hashes rather than independently established package origins. Do not equate deterministic binaries with full provenance.

## Windows acceptance and graphics fixture recovery — October 23, 02:05 update

- **Mode Windows closure:** all 69 actual cases passed. Preserve frozen payloads and historical unrun fields; record later acceptance separately. The report is delegated execution evidence, not an independent download of raw local receipts or a final game release.
- **Graphics regression fixture:** the first attempt failed compilation. A reviewed fixture-only repair enabled the passing 69-case retry without changing production runtime bytes. Preserve the failed attempt and avoid describing it as an uninterrupted clean pass.
- **Graphics evidence boundary:** the entry prefix has bounded Linux acceptance; newer diagnostic connected/regression and targeted allocation checks also received bounded Linux acceptance. No graphics Windows parity or repeated full-project aggregate is claimed.
- **A0:49 contract gap:** inspected vendor manuals do not bind the exact service. A community definition exists with provenance limits, but does not authorize implementation. A discarded return value cannot erase effects or justify a no-op; the real service boundary remains pending.

## Command tests versus visual QA and capture — October 23, 03:05 update

- **IDE Windows:** 50 synthetic command/state checks passed; separate visual capability was unavailable before launch. Keep the command result while leaving pixels and original-asset UI unverified.
- **Combined validation:** all 16 aggregate/source-test stages and the 69-case Linux contract passed terminal review. Preserve earlier preparation failures and the author-attested launcher-exit limit; connected/allocation phases remain separate pending gates.
- **Snapshot contract:** independent source/synthetic review found imported availability metadata weaker than the producer invariant. A v2 correction awaits independent rereview before capture acceptance; synthetic serialization does not establish non-mutating runtime capture. A retained failed leak-check attempt is not erased by later sanitizer success with leak detection disabled.

## Capture acceptance and exporter race findings — October 23, 04:05 update

- **Combined closure:** connected-19 and allocation-29 passed separately, completing four-phase bounded Linux acceptance rather than borrowing predecessor results.
- **Actual capture:** four Linux cases passed after the earlier availability correction. Production checkpoints, synthetic fields/lifetimes and observed owner fingerprints remain explicitly scoped; no exhaustive private-state or live-debugger claim.
- **Exporter/viewer v1:** deterministic synthetic review exposed unrelated replacement deletion, substituted temporary content publication and Windows reparse traversal gaps before actual exporter/Windows viewer execution. Preserve v1 failures; v2 corrections resolved all three findings within independently accepted source/synthetic scope, not actual end-to-end acceptance.

## Portable publication and Windows validator correction — October 23, 05:05 update

- **Portable export/import:** one exact actual Linux artifact/model path passed. Existing-output constructor refusals establish bounded no-clobber behavior, not repeated startup or exhaustive concurrent-race coverage.
- **Windows preparation:** retain the path-metadata blocker and companion-fixture correction without exposing private environment details.
- **BOM false positive:** culture-sensitive prefix comparison rejected a valid positive offline trace; no native executable ran. A character/ordinal correction passed four-culture shape checks and 33 offline controls. The later native run failed bounded file load after 36 checks passed, leaving 74 unrun. The cause is unknown; retain the failure and diagnose the exact reader without blind retry.
- **Loader history:** conditional static calls, unresolved firmware-return-relative writes and unchecked synchronization failure prevent inferring inherited hardware state from the independent native startup model.

## Context-dependent reader and later bounded acceptance — October 23, 06:09 update

A separate unchanged-reader diagnostic identified `QueryDosDeviceW` error 5 in the default context; one explicitly approved invocation passed the synthetic reader and model checks. That contrast does not identify the general access-control cause, resolve the original context, imply administrator status or grant reusable permissions. The later frozen-v2 harness was separately approved; its pass did not require source or security-setting changes.

The unchanged frozen Windows viewer subsequently passed **all 111 synthetic HWND/command/state checks** in a separately approved execution context: zero failed or unrun checks, an exact 113-record / 7,651-byte oracle match, supervisor/harness/validator exits 0 and an empty scoped job. Source, retained kit/history and security settings remained unchanged. The prior default-context result—36 passes, failure at check 37 and 74 unrun—is preserved, not repaired retroactively. This is reported executor evidence; raw PC receipts were not independently downloaded. It does not establish pixels, standalone inspector operation, actual-capture display, full IDE acceptance or game boot.

A further independently reviewed static calculation keeps the firmware-return distinction explicit: conditional B0:57 return `U=0x874` localizes the next word load to `0x9e0`; it does **not** establish that the loaded base `R` equals `0x874`. Three independently loaded bases remain unknown. Store counts, interleaved copy order and conditional modular overlap predicates were checked under explicit alias and nontrapping-arithmetic assumptions. Only the enumerated fixed cache stores exclude selected-site overlap; no general dispatch non-overlap, executed loader mutation or inherited GPU state is established. The native GPU origin remains an observation-only model with unknown status, not a reset or idle snapshot.

## Cleanup ownership recovery and still-blocked visual work — October 23, 07:07 update

The first loader execution envelope received **NO GO**: an injected cleanup exception could propagate before owned-child/group cleanup was proven. That failed version remains preserved. A separate v2 keeps ownership through cleanup faults and cannot turn recovered cleanup into success; eight ordinary lifecycle controls plus three cleanup-fault regressions passed before the one authorized compatibility run.

Visual acceptance remains blocked by missing required tooling and a version-registration mismatch; no nondisruptive repair was verified, and no application restart or security change was made. A transfer-route audit qualified earlier authorized handling as a compatibility route rather than the documented standard helper route; reuse is held pending review. This qualification does not invalidate the separately scoped lifecycle result or authorize another transfer.

The separately accepted native loader-prefix run is not firmware execution. The new 23-check Windows host-function lifecycle is not real-launcher/pixel acceptance; neither rewrites earlier viewer failures or grants broader execution permissions.
