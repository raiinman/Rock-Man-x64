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
