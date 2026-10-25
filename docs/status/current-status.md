# Current project status

For the latest reviewed project-wide summary and public coordination, use the [living tracker](dashboard.md) and [dated handoff](decisions-and-handoff.md). The checkpoint below identifies the latest implementation update documented on this page; it is not the date of every later research or coordination review.

**Checkpoint: 2026-10-24, reviewed at 02:07 UTC.** The isolated diagnostic-preview caller now withholds budget-stopped or failed raster output from ordinary completed-frame presentation. Independent source/synthetic review passed; Windows artifacts were linked, not executed. Earlier editor/rasterizer repairs, native mode-00 acceptance and revision-scoped heatmap browser evidence retain their separate limits. Native boot and A0:49 remain unresolved; the roadmap stays 5/20.

Rock Man x64 is **not a playable game, complete IDE or full native boot**. This repository is documentation-only. Reported private results cannot be independently reproduced from it.

## Diagnostic preview outcome repair — October 24

An independently reviewed, isolated host-side repair makes the character preview distinguish a finished raster traversal from an incomplete or failed attempt. A retained pre-fix synthetic reproduction exhausted the unchanged work budget after drawing partial content, yet still requested ordinary presentation once. The correction retains the draw outcome, withholds that incomplete raster from the ordinary presentation path, suppresses misleading wireframe and selects an honest notice. Exactly reaching the cap without further work remains a completed traversal, not a false failure. Renderer arithmetic, caps and frozen candidates are unchanged; no automatic retry or queue was added.

Reported evidence: **11 policy scenarios**, **five source-extracted caller checks** and **four independent controls** passed optimized Linux and ASan/UBSan. The caller checks repeat key policy outcomes rather than adding five unique rendering scenarios; repeated configurations and reviewer overlap are not new scenarios. The prior nine sample-bounds scenarios, eleven shared-edge scenarios and existing synthetic rasterizer regression also passed. Review covered three named allocation-failure sites, not a full sweep. [Failure, repair and validation limits](../history/validation-history.md#diagnostic-preview-outcome-repair-evidence--october-24).

Actual execution used cloud Linux with synthetic RGBA data. Windows-target application/test links passed, but **neither artifact ran on Windows or Wine**. A completed CPU traversal permits only a presentation attempt: the Windows display-call result is still unchecked, so successful display and actual window pixels remain unverified. No original assets, game execution, native producer/frame-owner integration or A0:49 completion was involved. S2, initializer and provenance gates remain unchanged. This 02:07 UTC documentation review reads the sealed receipts; it reruns no native tests and adds **zero milestone acceptance**.

## Isolated editor and rasterizer repairs — October 24

Three isolated, unfrozen candidates received independent source and Linux synthetic acceptance: **editor Reload/history failure preservation**, **unique shared-edge coverage** for adjacent opaque coplanar triangles with identical represented shared endpoints, and **sample-center bounds** admitting valid last-row/column and single-pixel-surface samples. These repair existing components; they are not installed replacements for frozen viewers or new game milestones.

The respective author inventories contain **11, 11 and 9 scenarios**, each run in optimized and ASan/UBSan modes with affected synthetic regressions. Each candidate also passed **two independent focused controls** in both modes. Repeated modes and parameter sets are not extra unique scenarios. [Validation history](../history/validation-history.md#editor-and-rasterizer-repair-evidence--october-24) retains the pre-fix failures, corrections and limits.

Actual execution was cloud Linux with GCC 14.2.0. MinGW GCC 14-posix completed Windows-target application/test links; **none of these new candidates was executed on Windows or Wine**. LeakSanitizer was disabled. Editor rollback excludes earlier successful Save/field application and later display operations. Renderer coverage is not arbitrary-overlap order independence or hardware pixel fidelity; bounds changes can alter work counts and partial frames under the unchanged work cap. No original-input/game test or native boot was established. A0:49, S2, initializer and provenance gates, frozen criteria and accepted milestone counts remain unchanged.

## Live heatmap QA and decorative-arrow correction — October 24

Bounded actual desktop-browser checks of the [first checked heatmap snapshot](https://github.com/raiinman/Rock-Man-x64/commit/b1afbcb7a113c4b25b8c899ab5325b74eaf36961) passed filtering, detail navigation, keyboard/focus and Back/Forward interactions. A [later snapshot](https://github.com/raiinman/Rock-Man-x64/commit/680b893a94f3baf4233882b41d0d10db6fda45ed) received only the separately recorded fresh-load/revision, 20-tile/5-accepted count, skip-link and width checks—not a repeat of every interaction. See the [bounded QA record](../history/validation-history.md#live-heatmap-desktop-qa-and-marker-repair--october-24).

The earlier missing-glyph defect in decorative arrows remains recorded; text and navigation stayed usable. After the font-independent CSS correction, **actual supported cloud-browser pixels passed at 00:33–00:34 UTC** on [snapshot b99453317da4](https://github.com/raiinman/Rock-Man-x64/commit/b99453317da43b04346551c0daa8fb46045e94be). All 20 tile arrows, the footer provenance arrow and the expanded native-boot evidence arrow rendered correctly. The 1180 × 757 desktop view retained 20 tiles: 5 accepted, 1 blocked, 14 pending and 0 in progress, with no horizontal overflow; the full page still extended below the viewport. Bounded Enter/Tab/Close checks retained detail focus, accessible evidence text and focus restoration.

This hourly documentation review reads that saved receipt; **no new browser run was performed**. Only repaired pixels and minimal detail navigation were repeated at that revision, not the earlier filters/search/Back/Forward coverage or later snapshots. Phone/touch, cross-browser and full accessibility/screen-reader coverage remain unrun, and native Windows runtime/pixel acceptance remains separate. The roadmap stays 5/20 with no new acceptance. [Repair verification and limits](../history/validation-history.md#deployed-heatmap-arrow-repair-verification--october-24).

## Live tracker and owner-observed Inspector — October 23

The **[interactive project tracker is live](https://raiinman.github.io/Rock-Man-x64/)**. After owner authentication and approved Pages setup, [run 40038248046, attempt 2](https://github.com/raiinman/Rock-Man-x64/actions/runs/40038248046/attempts/2) completed deployment successfully. At that first successful delivery, the checked eight-file artifact and observed page identified snapshot `f5aad94ff2ffeed9f26342465612453bc704b7d4`. This is public documentation delivery, not a native-game milestone. Browser coverage and its limits are recorded in [the validation history](../history/validation-history.md#live-tracker-and-owner-observed-inspector-evidence--october-23).

Separately, the owner reported that the experimental Inspector loads. A screenshot reviewed by the publication owner shows an Inspector window displaying an executable byte/hex view. **Evidence class: owner-reported and screenshot-observed launch/render only.** This is not a controlled test or a hash-bound identification of the running artifact. It does not establish actual snapshot import, cancellation, timer recovery, cleanup, native-session integration or game boot; no private screenshot, path, bytes or file identity is published.

The earlier stalled launch request remains inconclusive rather than being reclassified as a crash or retroactively passed. All roadmap/checklist counts, S2/native-owner, initializer and provenance gates remain unchanged.

The default documentation view is now an equal-area categorical roadmap heatmap: one tile per named milestone, with visible status labels and linked criteria. It keeps the same accepted counts and does not measure effort or game completion. Publication and actual browser checks of this new presentation must be verified separately from the earlier site.

A later coordination-only [run 40041118527](https://github.com/raiinman/Rock-Man-x64/actions/runs/40041118527) stopped before refresh/build/deploy because the generated receipt carried a stale JSON byte checksum. Its authored acknowledgment and evidence are preserved. A later canonical receipt-only repair passed updater, site build and deployment in [run 40042360611](https://github.com/raiinman/Rock-Man-x64/actions/runs/40042360611), followed by generated activity snapshot `925b6ba107f2f811410cb049d93c7b7ffb9c9b60`. The earlier failed refresh did not remove the deployed site. Later bounded heatmap browser checks and the completed, revision-scoped arrow-repair visual check are recorded [above](#live-heatmap-qa-and-decorative-arrow-correction--october-24).

## Windows attempt and Pages delivery — October 23

The earlier authorized execution report verifies private transfer of the exact viewer package and executable, with matching checksums. **The normal Windows launch attempt is inconclusive:** the launcher stalled without returning a process handle, and no inspector was observed afterward. This does not establish a successful start or a crash; the cause is unknown. GUI-control capability remained unavailable, and denied diagnostic-log access was not retried. No runtime, pixel or import acceptance follows. [Attempt history](../history/validation-history.md#windows-attempt-and-pages-delivery-evidence--october-23).

Earlier [workflow run 40033005572](https://github.com/raiinman/Rock-Man-x64/actions/runs/40033005572) passed the documentation updater and site build, but **Pages deployment failed with HTTP 404 because Pages was not enabled**. The first attempt of run 40038248046 likewise passed updater/build and failed deployment with 404. Those failures remain part of the record. The later successful deployment above followed the required hosting setup; a passing build alone was never treated as live hosting. All milestone counts and native/S2/initializer/provenance gates remain unchanged.

## Private viewer reliability candidates — October 23

A new **unfrozen private viewer candidate** incorporates the accepted importer worker-boundary correction plus two later host-side fixes: allocation-independent UI error fallback and retained completion results when notification delivery fails. Control restoration retains the displayed view rather than re-reading the selection. The Windows-target application **fully compiles and links**. At that source/link checkpoint no Windows execution was established. The supervised launch attempt above remains inconclusive; the later owner screenshot adds only the separately labeled launch/render observation. Frozen accepted viewers and previously delivered artifacts were preserved; this is not an installed production replacement.

Independent review accepted the isolated source/synthetic boundaries after correcting an initial queue-drain defect that could misclassify quit or child-window messages. Reported Linux evidence is **13 UI scenarios** in two modes and **17 retained-result scenarios** in three modes, plus separately scoped drain and reviewer controls; repeated modes are not additional unique tests. [The validation history](../history/validation-history.md#private-viewer-reliability-evidence--october-23) retains the failure, correction and exact counts.

Recovery requires actual UI timer-message dispatch; the requested polling interval is **not a recovery deadline** and does not terminate blocked I/O. Controlled Windows launch, real UI/timer behavior, actual import/cancellation, abnormal teardown and qualified pixel acceptance remain unverified. The later owner screenshot is not a substitute for those checks. No roadmap criterion advances; native boot, S2, initializer and implementation-provenance gates remain unchanged.

## Isolated importer result-boundary candidate — October 23

An independently reviewed **isolated host-side candidate** corrects two demonstrated allocation-failure paths that could escape the importer worker entry and terminate the application. Preparation happens before launch; diagnostic allocation failure retains a meaningful failure result, and result handoff has explicit ownership. This is **not an installed fix in the accepted frozen viewer**; production sources and parsing/cancellation contracts were not replaced.

At that earlier checkpoint, evidence comprised two controlled synthetic termination reproductions, fifteen scenarios in three Linux modes, two partly overlapping reviewer thread cases, and Windows-target object compilation only. There was then **no application link, Windows execution or real import**. Completion-message delivery and allocating UI error display were still open; the later private candidate above adds separately scoped fixes, not retroactive Windows acceptance; see [the validation record](../history/validation-history.md#importer-result-boundary-evidence--october-23). No roadmap criterion advances. S2, native-owner retirement, provenance and the blocked initializer remain unchanged.

## Accepted native Windows mode-00 stage

A single actual Windows invocation passed **all 69 ordered cases**: **39 expected exit 0 and 30 intentional exit 1**, including **40 complete CLI JSON comparisons** and the declared text comparisons. All cases reported supervisor completion, direct-child termination and empty owned jobs. Adapter stderr was empty; individual case stderr matched its contract. No timeout, unresolved cleanup or security-setting change occurred.

All **605 validation-kit files**, including 26 case executables and support material, and **separately three pre-existing original inputs** remained unchanged. No original inputs were packaged. This is an identified authorized execution report; full raw local receipts were retained on the executing system and were **not independently downloaded by the reviewers**. Acceptance is recorded in a separate record. Frozen payloads and historical unrun metadata were not rewritten. This is neither a public distribution nor final game-release acceptance.

The stage applies a genuine same-image 2048-byte Form1 reader through actual FIFO, response, IRQ and callback work. It examines one same-owner event with zero matches, preserves permission and does not invent an event or numeric success. Source control and outer return complete with result 1 and full knownness, then stop at **`8001b44c`**. Streaming, playback, complete startup and GPU initialization remain unsupported.

Before the first 69-case integration, actual Windows PowerShell comparison and receipt rules passed **96 synthetic checks**. Earlier adapter-review gaps and fixes remain retained; these were validation-tool tests, not game tests.

Earlier supporting evidence remains distinct: the isolated 13-stage Linux recovery passed 92 project tests, 19 tool tests and 13,305 metadata rows with 427 source and 4,181 immutable-input identities unchanged. The Linux 69-case contract passed, and two Windows cross-builds produced 26 byte-identical executable pairs. Synthetic supervisor candidate 6 passed 15 Windows checks after candidates 3–5 failed; those failures remain in [history](../history/validation-history.md).

The preceding mixer stage's 51-case Windows result and frozen 40/18/21 summary-counter defect also remain historical evidence. Actual definitions were 51/20/30; the old freeze was not silently repaired. Neither that defect nor the new acceptance rewrites what earlier checkpoints established.

## Newer graphics entry: bounded Linux acceptance

The entry prefix passed **12 connected cases**, the **69-case Linux regression**, and targeted allocation testing across **11 checkpoints / 31,227 allocation cuts**, with a maximum observed count of **2,871**. This is targeted failure coverage, not exhaustive coverage of every allocation path.

The first regression attempt had a fixture compilation failure. A reviewed fixture-only repair enabled the passing retry without changing production runtime bytes; the failure and earlier evidence were preserved. The full 13-stage project aggregate was **not repeated** for graphics, and no graphics Windows parity is established.

## Diagnostic continuation: bounded Linux acceptance

Independent source/synthetic review and **19 connected cases** passed. The supported path publishes the exact **37-byte diagnostic once**, clears **128 bytes**, follows a guarded initialized callback and stops at pending **A0:49**, at `8007cc0c` with return continuation `8007cc14` and source stack `801fff98`. These identifiers describe a bounded stop, not executed GPU initialization.

The continuation's **69-case Linux regression passed**. Independent final review accepted **29 targeted allocation checkpoints / 96,596 fault cuts**, maximum **3,424** below the fixed 8,192 cap, with zero late commits observed in the targeted sweep, unchanged source pins and complete cleanup. This is bounded Linux acceptance. No full-project aggregate, Windows parity or release acceptance is inferred from the connected and regression subsets.

## Evidence limits and next steps

Build provenance uses an **environment-pinned** assurance: nine host dependencies are retained privately and hash-pinned, without authenticated host-package origin or independent trust-root bootstrap. Deterministic executable bytes do not establish those stronger claims.

The inspected Sony Operating System (1998) and Run-Time Library Reference 4.7 pages do **not establish the exact A0:49 service contract**. A community definition exists but remains a provenance-limited research lead, not implementation authority. This is a limitation of the inspected sources, not a claim that no definition exists anywhere. A discarded return value does not make the service effect-free or justify a successful no-op; A0:49 remains pending.

The separate [BIOS research library](../../research/README.md) is reference evidence, not proof that this runtime implements or reproduces hardware. Its [DB8/DBA review](../../research/bios/DB8-BOUNDARY.md) distinguishes community numeric/signed-field definitions from unverified Sony binding, reset/timing and game hardware equivalence. Voice-current experiments do not establish master readback behavior. The latest timeout-recovery research is a reviewed static report; transitive-helper and ABI obligations remain open, so it does not fulfill the pending runtime service.

## Combined candidate and IDE update

The isolated combined development candidate passed the **full 13-stage project aggregate plus three added source-test stages: all 16 stages passed**, including 92 project tests, 19 tool tests and 13,305 asset metadata rows. Independent terminal review checked command exits, output identities, preserved inputs and scoped cleanup. The launcher exit is supported by an identified author attestation, not an independently saved raw launcher receipt. Earlier preparation failures remain preserved.

Its later **69-case Linux contract** also passed independent terminal review: 26 builds, 40 CLI profiles, exact saved-output comparisons and 97 scoped cleanup records checked. The same combined candidate subsequently passed **all 19 connected cases and 29 targeted allocation checkpoints**, completing all four separately reviewed Linux phases. The targeted sweep recorded **96,596 fault cuts**, maximum **3,424** below the fixed 8,192 cap, and zero late commits observed in that sweep. This is targeted evidence, not exhaustive allocation or sanitizer coverage; earlier isolated results were not substituted for these runs. No combined Windows or release acceptance is implied.

The IDE **Source bytes/Back feature passed 50 actual Windows synthetic command/state checks** in one supervised invocation. The exact 52-record trace matched, all 13 kit files remained unchanged, output streams were empty and the owned job ended empty. This tests the real inspector entry point through the harness, including paging and state preservation—not standalone pixel correctness, original-asset UI or comprehensive reparse races. Raw local receipts were not independently downloaded by the reviewers. The separate visual preflight was **blocked by unavailable supported visual-control capability before launch**; no standalone window launch, capture or pixel inspection occurred. This does not invalidate the 50 command checks. Reader-derived offsets show current-disk bytes, not fingerprint-authenticated earlier decoded content.

## Bounded actual owned capture

After correction and review of the earlier availability invariant, actual same-owner startup capture passed a **four-case Linux/UBSan envelope: 60 successful captures and 253 injected capture-allocation failures**. Independent terminal review accepted unchanged pins, exact outputs and complete scoped cleanup. Production checkpoints exercised active CD/IRQ precedence, partial continuations and the actual pending A0:49 request; unloaded and fixture cases supplied separate synthetic field/lifetime coverage.

Observed owner-state fingerprints plus source review support the bounded non-mutation claim—not byte-complete introspection of every private field or every state. Successful captures are not runtime steps or exhaustive state-space coverage. Absence of captured A0:49 data does not mean every service is absent. No Windows capture, live debugger or complete viewer integration is accepted.

## Actual portable export/import and bounded Windows viewer acceptance

After the retained v1 race findings and reviewed v2 fixes, **one exact Linux producer-to-artifact-to-portable-model export/import run is accepted**. It advanced **2,175 command batches**, stopped at the existing runtime refusal, produced one **2,846-byte private artifact** and imported/rendered **6,108 bytes of model text**. These are not instruction counts, a GUI screenshot or a boot result.

Independent review verified artifact fidelity, bounded parsing, round-trip equality, frozen/untrusted/producer-reported labels, unchanged pins and scoped cleanup. **Three existing-output constructor refusals** preserved the artifact and checked metadata; these were not three more startup runs or exhaustive filesystem-race coverage. Private artifact contents are not published. A0:49 remains unfulfilled.

The earlier default-context Windows frozen-viewer run **failed at check 37 after 36 exact-prefix checks passed; 74 checks remained unrun**. Preparation encountered a path-metadata blocker and a missing companion fixture, both corrected without claiming native execution. The first positive offline control then failed because culture-sensitive prefix checking misclassified a valid trace as BOM-prefixed; **zero native executables ran in that failed attempt**. A v2 character/ordinal correction passed **24 trace-shape checks across four cultures and 33 offline controls** (one positive, 32 expected refusals). These fabricated-evidence tests validate the validator, not the viewer. The subsequent single native 111-check invocation created an independent window and verified its initial empty state, but bounded artifact loading returned false at check 37. The harness exited 1 while the supervisor exited 0; cleanup was certain with an empty owned job and no timeout. All 23 kit files and seven fixtures remained unchanged. At that checkpoint the cause was unknown; the later reader diagnostic below narrows the observed failure without proving a general security cause. Evidence is the identified execution report; raw local receipts were not independently downloaded.

## Separately approved Windows viewer result

A separate unchanged-reader diagnostic identified `QueryDosDeviceW` error 5 in the default context; one explicitly approved invocation passed the synthetic reader and model checks. That contrast does not identify the general access-control cause, resolve the original context, imply administrator status or grant reusable permissions. The later frozen-v2 harness was separately approved; its pass did not require source or security-setting changes.

The unchanged frozen Windows viewer subsequently passed **all 111 synthetic HWND/command/state checks** in a separately approved execution context: zero failed or unrun checks, an exact 113-record / 7,651-byte oracle match, supervisor/harness/validator exits 0 and an empty scoped job. Source, retained kit/history and security settings remained unchanged. The prior default-context result—36 passes, failure at check 37 and 74 unrun—is preserved, not repaired retroactively. This is reported executor evidence; raw PC receipts were not independently downloaded. It does not establish pixels, standalone inspector operation, actual-capture display, full IDE acceptance or game boot.

## Earlier-loader static finding

Independent static review found a conditional original-loader path that requests A0:49 before later GPU reset work, firmware-return-relative writes with unresolved runtime destinations, and a prehandoff synchronization result that the caller does not check. This is not actual execution, physical hardware state, effective firmware dispatch or exhaustive producer coverage. It explains why the independent native cold-start trace alone cannot establish the original loader's inherited GPU/firmware history. No instruction dump or original content is reproduced.

A further independently reviewed static calculation keeps the firmware-return distinction explicit: conditional B0:57 return `U=0x874` localizes the next word load to `0x9e0`; it does **not** establish that the loaded base `R` equals `0x874`. Three independently loaded bases remain unknown. Store counts, interleaved copy order and conditional modular overlap predicates were checked under explicit alias and nontrapping-arithmetic assumptions. Only the enumerated fixed cache stores exclude selected-site overlap; no general dispatch non-overlap, executed loader mutation or inherited GPU state is established. The native GPU origin remains an observation-only model with unknown status, not a reset or idle snapshot.

## Native loader-prefix compatibility, not firmware execution

A separately reviewed native loader prefix passed one authorized Linux original-input compatibility run: one build, one load and one native advance stopped at pending **A0:39**. It performed 4,032 modeled zero-word stores followed by an unknown saved-return-address overwrite, leaving 4,031 final known-zero words. All register masks and outside-range RAM were checked. The **20,195 modeled source-instruction count** is not a host-step, command-batch or capture count. Zero services and GPU operations completed; cleanup and pre/post integrity passed. Original instructions were not executed, and no firmware completion, inherited GPU state, A0:49 closure or game boot is established.

The first loader execution envelope received **NO GO**: an injected cleanup exception could propagate before owned-child/group cleanup was proven. That failed version remains preserved. A separate v2 keeps ownership through cleanup faults and cannot turn recovered cleanup into success; eight ordinary lifecycle controls plus three cleanup-fault regressions passed before the one authorized compatibility run.

## Later native-policy heap and continuation acceptance

Two later, separately authorized Linux compatibility runs are accepted: one initialized the persistent native heap policy and stopped at its return boundary; the other performed one load, prefix advance, heap initialization and fixed continuation, stopping **before `800108ec`**. The continuation modeled **13 source instructions and two word stores**, with zero initializer instructions or optional allocator calls. Unknown saved return-address bits were retained and not used for control; all register masks and outside-store RAM were checked. Exact authorization, outputs, pre/post integrity and reaped/empty process groups passed independent terminal review without a reviewer rerun.

These outcomes are explicitly **native policy**, not BIOS execution or equivalence. Native RAM/register preservation does not resolve original firmware side effects, dispatch history, allocator layout, GPU state or the three unresolved loaded bases. Original instructions were not executed; no integration, A0:49 completion or game boot follows.

The first continuation candidate received **NO GO** after synthetic mutation exposed an input-lineage binding gap. The separately reviewed v2 retains the successful admission category independently and rejects either allowed-category substitution before and after commit. The failed v1 and earlier cleanup-envelope rejection remain preserved; neither was relabeled as accepted.

## New static heap evidence does not establish equivalence

The [digest-specific A0:39 report](../../research/bios/HEAP-INITIALIZATION.md) now describes an initial service binding and five ordered word stores, including clearing one supplied-address word and recording heap-related globals. This is author-reported static instruction interpretation, cross-checked with a separate decoder—not firmware execution or an observed game-time call. The analysis tool did not recover a function at the selected address; the report distinguishes that limitation from its bounded instruction decoding. Private source bytes and raw evidence were not independently inspected for this documentation review.

The reported store effects differ from the accepted native heap policy's deliberate preservation of guest RAM. That policy's bounded acceptance remains valid as a native design choice, not a claim of BIOS equivalence. Effective runtime dispatch, exceptional completion, later allocator invariants and inherited GPU state remain unresolved. The new report does not authorize adopting firmware effects or advancing the initializer; execution preparation remains blocked pending review, with no retry or alternative route attempted.

## Initializer candidate: synthetic-only, execution blocked

A later initializer-prefix candidate has **source/synthetic acceptance only**: 127 author checks and 920 independent assertions. Its proposed fixed lowering models 26 source instructions and four stores, stopping at a pending 16-bit I_MASK write with applied=false. No actual-input run is accepted. Its execution preparation was blocked pending review; no retry or alternative route was attempted. This is not an applied interrupt-mask operation, GPU initialization or game boot.

## Standalone-viewer lifecycle and remaining access gates

A separate standalone-viewer candidate received source acceptance with **four additions and 457 baseline files unchanged**. Its Windows synthetic host-function lifecycle then passed **23 checks**, with an exact **25-record / 1,053-byte** oracle match, supervisor/harness/validator exits 0 and empty scoped cleanup, in the normal permitted context without security changes. This is an identified authorized executor report; raw PC receipts were not independently downloaded. It does **not** verify the real standalone launcher, pixels, actual-capture display, full IDE operation or game boot.

Visual acceptance remains blocked by missing required tooling and a version-registration mismatch; no nondisruptive repair was verified, and no application restart or security change was made. A transfer-route audit qualified earlier authorized handling as a compatibility route rather than the documented standard helper route; reuse is held pending review. This qualification does not invalidate the separately scoped lifecycle result or authorize another transfer.

Next: preserve the earlier 36-pass/check-37-failure/74-unrun viewer result and later 111-check pass alongside this separate 23-check lifecycle result. Keep visual/real-launcher/actual-capture acceptance separate; do not extend loader or A0:49 progress through invented service or device state.

## IDE runtime controller: source-only feasibility NO-GO

An independent source-only review accepted a **NO-GO for enabling the planned S2 runtime controller with the production IRQ/graphics startup profile**. Production loading is synchronous with no accepted cancellation or wall-time bound; the APIs do not supply a whole-owner retirement transition. Single-call stop/fault semantics and worker/mailbox finalization also remain unproven. A bounded byte count or requested batch is not a deadline, rollback guarantee or safe-shutdown receipt.

This is a completed design-feasibility review, **not a runtime test failure**. No code changes, builds, tests or Windows actions occurred; accepted frozen sources remain unchanged. It does not establish that every reduced profile is impossible, nor propose one as a substitute. Retain the frozen viewer and leave S2 controls absent or disabled until the lifecycle contracts are separately established. Earlier viewer successes and failures remain valid within their own scopes. Visual acceptance and the separate blocked initializer execution-preparation stage are unchanged; this review authorizes no retry or alternative route.

## Isolated observation mailbox: synthetic acceptance only

A separate data-only mailbox candidate received independent acceptance with no blocking defect found within its stated scope. **Twelve distinct synthetic scenarios** passed optimized Linux builds, AddressSanitizer/UndefinedBehaviorSanitizer with leak detection disabled, and ThreadSanitizer. These are the same scenarios in three modes, not 36 unique tests. Independent optimized and ASan/UBSan checks added two coverage dimensions: cross-translation-unit identity and live notice move/finalization accounting. A third reviewer scenario overlapped existing coverage.

LeakSanitizer attempts failed because of the host tracing environment and remain recorded; no LeakSanitizer or exhaustive leak-free claim is made. Eighteen selected accepted-source/metadata identity checks matched, not a full ancestry revalidation. The candidate transfers observations and accounts for requests/notices; completing those records does not complete native work or retire a runtime owner. Delayed stale notices require explicit data-only recovery, not automatic delivery or runtime replay.

This is **not an S2 controller, full application-message lifecycle closure, integration or Windows acceptance**. No real runtime, original input or PC action was exercised. Load termination, whole-owner retirement, single-call fault/stop semantics and real endpoint/capture/UI integration remain open; S2 stays NO-GO. Earlier accepted results and the separate initializer execution-preparation blocker are unchanged.

Neither graphics work nor Windows mode validation establishes original GPU equivalence, normal scene lifecycle, player control, collision, AI, combat, save compatibility or audio playback.

See [validation](validation.md), [handoff](decisions-and-handoff.md), [history](../history/validation-history.md) and [capabilities](../technical/capability-matrix.md).

## Data-only observer: Linux synthetic acceptance

A separate observer candidate now samples the isolated mailbox without executing or replaying native requests. Delayed/coalesced wakes recover the latest synthetic data; failed observations preserve an existing sample with stale/as-of labels (the first failure is empty). Detach/reopen obtains a fresh endpoint epoch but does not retire a native owner.

Ten new observer scenarios and the unchanged twelve mailbox scenarios passed three Linux build modes. Independent review added three focused, partially overlapping scenarios. Mode repetitions are not additional unique tests. The initial test-only compilation failure and the absence of LeakSanitizer coverage remain recorded in [validation](validation.md#observer-candidate-validation--october-23).

Production S2 remains **NO-GO**: load termination, whole-owner retirement, single-call fault/stop semantics and actual endpoint/capture/UI integration remain unresolved. No Windows execution, GUI integration, original-input run or native game boot was established. Next: review the production loading/retirement contracts before proposing controller integration; do not enable controls or retry blocked initializer preparation.
