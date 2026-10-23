# Evidence and validation history

## Evidence classes

| Class | Establishes | Does not establish |
|---|---|---|
| Archive, raw-track and source hashes | Identity and preservation of the supplied bytes | Independent source authenticity, legal rights or complete media integrity |
| Static original-byte analysis | Specific instructions/data relationships and bounded recovered semantics | Original-machine execution or whole-game equivalence |
| Parser/reference comparisons | Agreement for supported structures and supplied corpus | Complete format coverage, visual fidelity or gameplay |
| Synthetic tests and failure injection | Defined behavior, rejection, rollback and retry properties under the tested conditions | The original game's full intended behavior |
| Native Linux execution/sanitizers | Portable component behavior and checked memory/undefined-behavior properties | Windows execution or GUI acceptance |
| Windows x64 cross-build/PE inspection | A real Windows artifact with inspected architecture/imports | Successful execution of that artifact |
| User screenshot/report of Windows execution | The displayed output and reported interaction | Unrecorded exit codes or pixel correctness outside the captured evidence |
| Delegated actual Windows contract run | Reported exact cases, exits, outputs and before/after integrity checks | Direct execution by the documentation author, full gameplay or independently downloadable public receipts |
| Frozen package manifest and result receipt | Which identified package was tested and preserved | Newer active-source features or an unfrozen successor |

These are **different evidence layers**, not interchangeable labels for “tested.” The original source instructions were analyzed, not run in a CPU emulator as a substitute for the native project.

## Earlier portable and cross-build checkpoints

Examples of specific bounded checks include:

- All Form1 EDCs matched; Form2 remained unverified.
- Native asset conformance covered 205 files and **13,305 exact native/reference record comparisons** at the recorded aggregate checkpoint.
- Pose unpacking covered **456 basis vectors × 48 output components**; sequence logic covered **262,144 transitions**.
- Direct scene decoding matched **863 rows** for the supported sample.
- Palette-record tests covered **1,059 original records**, including distinct cache and direct paths.
- Source-connected suites grew through **56 event**, **61 context**, **63 hook**, **65 timer** and **69 DMA** tests before later CD work.
- Address/undefined-behavior sanitizers and allocation-failure sweeps accompanied many native components. LeakSanitizer was unavailable in the restricted environment where documented; that limitation is not silently converted into a leak-check pass.

These counts belong to their historical scopes. They should neither be added into a single “independent test” total nor read as uniform end-to-end coverage.

## Windows progression

### User-observed Windows VPS checks

The saved records contain explicit observation timestamps:

| Observation time, UTC | Evidence | Scope/limit |
|---|---|---|
| 2026-10-22 16:52:59 | Core-test PASS shown; shell prompt returned | Frozen synthetic inspector core; exit code not captured; old adapter wording did not prove original-data tests |
| 2026-10-22 16:57:18 | Rasterizer PASS shown; prompt returned | Synthetic rasterizer; exit code not captured; not GUI or game boot |
| 2026-10-22 17:20:19 | Saved GUI trace shown and user reported the window appeared | Native window/message loop and synthetic interactions; no desktop-pixel screenshot, exit code not captured |

These are observation times, not inferred build or completion timestamps. The earlier script-signing restriction and later authorized Windows-machine workflow are part of the operational history; neither justifies weakening security controls.

### Delegated authorized Windows test-machine results

The retained reports describe real native Windows execution. They were preserved as reports; some complete original receipts remained private on the test machine. No machine names, account paths or access identifiers are published here.

| Frozen stage | Accepted results | Actual boundary |
|---|---|---|
| Inspector | Core, rasterizer and GUI synthetic runs passed after the separately approved core retry | Real Win32 controls/message loop and edit/save/reload interactions, not game boot or complete visual validation |
| Startup / ISO lifecycle | Four checks, all exit 0; full expected JSON matches | Cold startup reaches diagnostic-output dependency; inherited ownership and diagnostic fixture remain separate |
| CD diagnostics | Four checks, all exit 0; full JSON matches | Native byte sink works; next controller write remains uncommitted |
| Controller | Four checks, all exit 0; full JSON matches | Native controller configuration established; source command routine still unsupported |
| Admission prefix | Four checks, all exit 0; full JSON matches | Status command byte is pending, not yet accepted |
| Media preflight | 11 processes exit 0; six text and five JSON comparisons match | Real production raw-sector service/reads; still preflight only |
| Status response | 19 cases: 16 exit 0 and three expected exit 1; nine full JSON comparisons | Prepared or published native response; notification-enabled path stops at routing |
| IRQ chain | 29 cases: 22 exit 0 and seven expected exit 1; 14 full JSON comparisons | First status command consumed/routed/completed through translated handler and logical return; stops before reset `0A` |

Expected negative cases are successful **refusals**, not crashes being counted as passes. Frozen runtime reports record empty stderr, no timeouts and before/after integrity checks. Text comparisons permitted only their stated normalization/pattern rules; full JSON comparison is stronger than matching a single success line.

A prior stage's actual Windows pass does **not** validate active inspector additions or later candidates; the configuration stage's subsequent Windows result is recorded separately below.

## Candidate at the 21:37 UTC pause

**Unfrozen, not actual-Windows-validated:** the CD configuration candidate advances reset/unmute and stops before an unsupported sound-register read. The isolated run reports 92 regression tests, 19 tool tests, 21 CLI cases and 18 Windows cross-builds passing. At the pause, remaining standalone checks and final acceptance receipts were still pending/unaccepted. The already-running aggregate drained at **21:39:13 UTC**: 19 completed stages, 17 successful and two failures due to missing preview fixtures; acceptance, frozen and retry flags remained false. At that paused checkpoint, no new post-pause retries or Windows configuration run had occurred. Earlier shared-output attempts were inconclusive and excluded from final acceptance.

The isolated workflow requires separate outputs, pinned source/input identity, explicit command/exit receipts, CLI assertions, static artifact checks and final preservation/completion receipts. Until accepted, partial green subsets do not establish a final aggregate or release.

## Resumption and isolated validation — 2026-10-22

Development resumed at **22:04 UTC**. At **22:06 UTC**, isolated cloud validation completed with 92 regression tests, 19 tool tests, nine components, 21 CLI cases (14 exact older-JSON comparisons), and 18 static Windows builds. The character and inspector retries passed after missing private fixtures were supplied; their initial failures remain retained. Earlier shared-tree attempts remain inconclusive and excluded.

The configuration validation also recorded 677 focused boundaries and 1,354 repeated allocation denials, plus preserved identities for 214 source files, 2,334 immutable copied inputs, 76 preview inputs and 2,086 existing release files. The 19 effective successful stages included corrected-fixture retries, not an uninterrupted clean pass. Expanded callback/successor refusal checks did not prove connected reset reissue, 16-operation exhaustion or broader recovery.

Final artifact review was confirmed by **22:08 UTC**, followed by approval to proceed with freezing at **22:09 UTC**. At that earlier resumption update, immutable freeze/rebuild and the Linux 40-case contract were **in progress**, not completed. No new Windows execution had occurred, so the 29-case IRQ-chain stage remained the latest Windows-verified milestone at that time. High-level CD initialization, game boot and playback were unestablished.

## Selected non-content identities

Hashes identify retained private evidence; they are not download links or public availability claims.

| Artifact | SHA-256 |
|---|---|
| Supplied source archive | `a5b2cdf74812861f59e90b255188731bde762366d2da3c2cbfd01bcd18954597` |
| Raw data track | `bfc887af814ad014998004897f805c5ab987770e7477b66dd5fd83c0bc40c9a1` |
| Raw audio track | `ce5509fad13f6210656c9d29fb536b47abe5f824467177652c91b5c500470c77` |
| Analyzed main executable | `10d2008f2837c466b8a3c3f56ff9b0946096ef29d7f26f09010d78ed4b2568f0` |
| Analyzed ST01 input | `ba205cdcb02c5bf4dc669273f12e505f83288bcfe0a69b792a5f56d6d4159aa8` |
| Frozen IRQ-chain private test package | `6f3ab2ad4cbab85dc72311837aa87e725a5c7e319b5a766b0fdf725a7a7ab979` |
| Retained IRQ-chain Windows result receipt | `a46be1d6d13c68ae497d60f3d0bc19ed823e9557a6f29205629d781550a8d8b6` |

## Public reproducibility boundary

This documentation-only repository does not include the private source corpus, original executable instruction tables, extracted assets, previews, private test packages or raw executor receipts. The reported original-data and Windows results therefore cannot be independently reproduced **from this repository alone**. Evidence is retained privately, and this narrative distinguishes evidence types rather than presenting inaccessible private paths as public citations.

No instruction listing, ROM bytes, asset preview or private package content is embedded in this history. Hashes and sanitized milestone descriptions permit identity tracking without distributing those materials.

## Subsequent configuration acceptance and connected mixer — 2026-10-22

The frozen configuration/reset/unmute stage subsequently passed **40 actual Windows cases** (27 expected exit 0, 13 intentional exit 1): 21 complete JSON matches, 19 contract-scoped text matches, empty stderr, no timeouts and unchanged before/after integrity checks. Low-level helper `800791a8` returns 0, but that stage stops at sound-read boundary `80079070` without a high-level CdInit return.

The newer connected native CPU mixer establishes same-owner processing and genuinely returns from high-level CdInit with fully known result 1, then stops at `800779cc` before unsupported non-null-result CdSync. Connected ASan/UBSan reports 20,222 checks, with 20,000 production PCM oracle frames and 136 source boundaries checked. Its pre-reporting aggregate passed all 18 stages (92 regression tests, 19 tool tests, ten components), with 438 tracked source/input/test/tool identities unchanged.

Review found contradictory legacy reporting literals. An isolated reporting-only correction changed one CLI source file, leaving 437 other files unchanged. All 21 old reports remained byte-exact; nine new positive/refusal profiles and affected tests/verifiers passed. This is compositional validation, not a second full aggregate or new runtime capability. Original inconsistent reports are retained as history, not accepted current output; some intermediate reporting branches received source review only.

Freeze preparation was approved at 22:51 UTC. An initial Linux 51-case contract passed. Fresh-output-directory hardening passed seven negative path/symlink checks. An earlier rebuild encountered a changing runner script and exited 127; that receipt is retained and excluded from acceptance. The settled guarded rebuild then passed with 20 byte-identical target executables and 419 source files matching the corrected snapshot; a second Linux 51-case pass completed. The final unchanged rerun with explicit before/after runner hashes remains pending. This release-tooling failure was not a Windows execution failure. The audio stage is not yet frozen or Windows-validated and has no device output, playback, physical SPU equivalence or game boot.

## Later mixer sealing and actual Windows result — October 22 work, October 23 update

The formerly pending final freeze checks completed. The sealed mixer stage contains 419 source files, 20 reproducibly built Windows executables and 30 CLI profiles. Its Linux 51-case contract passed, followed by **51 actual Windows cases**: 30 expected exit 0 and 21 intentional exit 1, with 30 complete JSON and 21 text comparisons. No timeout or stderr occurred; checked package, executable and input identities were unchanged. Windows sanitizer execution is not claimed. High-level CdInit returns 1 with full knownness and restored source stack, then stops at unsupported non-null-result CdSync. There is no output-device ownership, decoding, playback, physical SPU equivalence or game boot.

The frozen contract retained stale summary counters **40/18/21**, despite actual definitions and inventories of **51/20/30**. The runner checked and executed all actual definitions, so the 51 comparisons remain valid. This is a real metadata defect, not a silently corrected freeze or invalidated Windows run. A separate generic preflight now validates derived counts, references and strict JSON before private-input reads/package creation. All 22 synthetic tests passed and were independently rerun; the historical inconsistent freeze is now rejected by that preflight and remains unchanged.

## New mode-00 candidate: pending acceptance

The actual pinned Linux receipt passed 51 earlier cases, 20 builds and 30 CLI profiles. An older regression log compiled the shared tree and was briefly misidentified as pinned evidence; that interpretation was corrected before the actual pinned run passed. Ten new mode profiles passed (one positive, nine refusals). Their initial eight-byte expectation was wrong: two genuine eight-byte copies total 16, confirmed by a pinned-source fixture. The failed expectation is retained.

Independent review recorded 50/32/36 synthetic UBSan checks and 53 original control-flow targets. Direct-pinned ASan/UBSan fail-N groups subsequently passed 23,323 normal-path and 10,940 nonzero-path checks. Leak detection was disabled because of the tracing environment; these are targeted checks, not exhaustive allocation coverage. Earlier bounds of 64 and 512 were insufficient; measured generic advancement reached 2,719 allocations. A later whole-call atomicity assertion was invalid because committed response publication can precede an IRQ diagnostic allocation failure. Narrow same-operation/debt/no-duplicate/retry assertions passed without runtime rollback, closing that independent-review concern.

A stale-reader/raw-mode lifecycle bypass was guarded before pinning and earlier feature profiles remained unchanged. The connected candidate applies the genuine same-image Form1 reader, consumes actual response/IRQ/callback work, examines one same-owner event with zero matches, preserves permission and reaches a real source return. It does not fabricate an event or numeric success: the B0:07 return remains unknown and is overwritten before the source caller uses it. **No verified terminal full-project aggregate, immutable freeze or Windows execution exists at this checkpoint.** The original aggregate attempt remains inconclusive and excluded. A fresh isolated rerun started at 00:04 UTC, but has no terminal full-project receipt yet. Graphics continuation is only a static plan.

## Subsequent accepted recovery and unsealed contract — October 23, 01:05 update

The fresh isolated recovery subsequently passed all **13 stages**, including **92 project tests, 19 tool tests and 13,305 metadata rows**. Before/after checks preserved **427 source and 4,181 input identities**. The original interrupted aggregate remains inconclusive and excluded; this success does not prove its descendants stopped or turn observed timings into benchmarks.

The first isolated attempt stopped because copied generated evidence files were read-only. The retry changed permissions on only three private generated files without changing their bytes, and removed one demonstrably rebuilt executable from immutable-input classification while retaining its output identity. The original manifest and failed attempt are preserved; the accepted identity scope remains 427 source and 4,181 immutable inputs.

The newer unsealed Linux contract passed **69 cases / 26 executables / 40 CLI profiles**, comprising **39 expected exit-0 and 30 intentional exit-1** outcomes. These are Linux-built/executed checks. Two separate passes cross-built 26 Windows targets each, with all 26 pairs byte-identical. Actual candidate validation checked PE32+ executable mapping and 40 real profiles, with no placeholders. No new Windows mode execution, sealing or playable release is implied.

Synthetic Windows supervisor candidates **3, 4 and 5** each failed the first success case with zero accepted checks. The fixture exited 0 with exact output, but the supervisor refused additional/inconsistent process association. Candidate 5's membership-confirmed current-handle basename was consistent with a console host; it was not authenticated image identity or proof of historical process continuity. Cleanup observed an empty owned job and ended direct child. Later timeout, descendant, argument and output-validation cases remained unrun. No policy refusal, protection change or uncontained fallback occurred. Console-detached candidate 6 subsequently passed all 15 synthetic Windows checks in one invocation, including deliberate descendants, timeouts and forced-supervisor-termination cleanup. The 14-file kit remained unchanged, with no protection override or unresolved cleanup. This is not Windows mode execution.

Offline provenance checks verified retained cross-toolchain distribution payload closure and signed-index/package linkage. Nine host shared dependencies are hash-pinned without independently established package origin. Complete build-environment provenance and stronger reproducibility claims remain unestablished.

Separately, a graphics-entry RAM/control prefix has moved from static planning into implementation and validation in progress, without independent acceptance. No original-image execution, accepted graphics milestone or GPU initialization is established.

## Actual Windows mode-00 acceptance — October 23, 02:05 update

Before the first real 69-case integration, actual Windows PowerShell comparison/receipt rules passed 96 synthetic checks. Earlier adapter-review gaps and fixes remain retained, not rewritten as an uninterrupted clean pass. These were validation-tool checks, not game tests. Provenance assurance remains environment-pinned: nine host dependencies are retained privately and hash-pinned, without authenticated host-package origin or independent trust-root bootstrap.

A single invocation passed **69/69 actual Windows cases**, comprising **39 expected exit 0 and 30 intentional exit 1**, **40 complete CLI JSON comparisons** and declared text comparisons. Every case reported supervisor completion, direct-child termination and an empty owned job; no timeout or unresolved cleanup occurred. Adapter stderr was empty and per-case stderr matched its contract. All **605 kit files**, including 26 case binaries and support material, and **separately three pre-existing original inputs** remained unchanged. No original inputs were packaged. No security settings changed.

The accepted source path completes control/outer return with fully known result 1 and stops at `8001b44c`. Streaming, playback and game boot remain unsupported. Acceptance relies on the identified authorized execution report: full raw local receipts were retained on the executing system and not independently downloaded by the reviewers. Frozen payloads and historical unrun fields remain unchanged; a separate acceptance record captures the later result. This is not final/public game-release acceptance.

## Newer graphics Linux checks and retained failure

The graphics-entry prefix passed **12 connected cases**, the **69-case Linux regression** and **11 targeted allocation checkpoints / 31,227 allocation cuts**, with a highest observed allocation count of **2,871**. Its first full-regression attempt had a fixture compilation failure. A reviewed fixture-only repair enabled a passing retry with production runtime bytes unchanged; the original failure and evidence remain preserved. Targeted coverage is not exhaustive allocation coverage, and the full 13-stage project aggregate was not repeated on graphics.

A later diagnostic continuation passed independent source/synthetic review, **19 connected cases** and its **69-case Linux regression**. The path publishes the exact 37-byte diagnostic once, clears 128 bytes, follows a guarded initialized callback and retains pending A0:49 at `8007cc0c`. Independent final review accepted **29 targeted allocation checkpoints / 96,596 fault cuts**, maximum **3,424** below the fixed 8,192 cap, zero late commits observed in the targeted sweep, unchanged source pins and complete cleanup. This is bounded Linux acceptance. Neither graphics continuation has Windows parity or proves GPU initialization.

The inspected Sony OS (1998) and Runtime 4.7 pages did not establish the exact service contract. A community definition is a provenance-limited research lead, not implementation authority; the inspection does not establish universal absence of documentation. The call stays pending rather than being replaced by a no-op or fabricated success.

## IDE Windows commands and combined Linux validation — October 23, 03:05 update

The IDE Source bytes/Back harness passed **50/50 actual Windows synthetic command/state checks**, with the exact 52-record trace, empty output streams, unchanged 13-file kit and an empty owned job. The harness invoked the real inspector entry point; the standalone inspector was not separately launched. This is not pixel correctness, original-asset UI, comprehensive reparse-race coverage or prior-content authentication. Raw local receipts were retained on the executing system, not independently downloaded by the reviewers.

Separate standalone visual QA was blocked **before launch** because supported visual-control capability was unavailable. No window launch, capture or pixel inspection occurred; earlier command receipts remain unchanged. This was not a denied or uncertain execution, and no alternative automation route was substituted.

The combined Linux candidate passed **all 16 stages**: the original 13-stage aggregate plus three source-test stages, including 92 project tests, 19 tool tests and 13,305 asset metadata rows. Independent terminal review verified exits, logs, immutable identities and scoped cleanup. Launcher exit 0 is supported by an identified author attestation rather than an independently saved raw launcher receipt. Earlier preparation failures and inconclusive attempts remain preserved.

The later combined **69-case Linux contract** passed independent review of 26 builds, 40 CLI profiles, exact saved-output comparisons and 97 cleanup records. Separate combined connected-19 is pending and allocation-29 remains unrun; isolated predecessor results cannot be substituted. No combined Windows, release, GPU or boot acceptance is implied.

Owned snapshot DTO work has source review and synthetic codec/lifetime checks, not actual connected capture. Review found v1 imported availability combinations weaker than the documented producer invariant, plus a need to clarify that absent A0:49 data does not mean every service is absent. A v2 correction exists and awaits independent rereview. The failed leak-check attempt was retained; subsequent sanitizer success with leak detection disabled is not leak-check success. Capture/non-mutation, export and viewer integration remain unaccepted.

## Combined Linux closure and actual capture — October 23, 04:05 update

The separately run combined connected-19 and allocation-29 phases passed independent review, completing acceptance of all four combined Linux phases alongside the earlier 16-stage aggregate and 69-case regression. The targeted allocation sweep recorded 96,596 fault cuts, maximum 3,424 below the fixed 8,192 cap, and zero late commits observed in that sweep. It is not exhaustive allocation/sanitizer coverage or combined Windows acceptance.

The first actual-capture envelope was rejected during preflight for lifecycle and failure-integrity issues, before any actual capture run. A corrected v2 runner passed synthetic checks before the successful actual-capture invocation; no failed actual-capture run is claimed.

After the availability-invariant correction and review, actual owned startup capture passed a four-case Linux/UBSan envelope: 60 successful captures and 253 injected allocation failures. Production checkpoints covered loaded state, active CD/IRQ precedence, partial continuations and the actual pending A0:49 request. Unloaded/fixture cases supplied distinct synthetic field and lifetime coverage. Pins, exact outputs and scoped cleanup passed independent terminal review. Observed public owner fingerprints plus source review establish a bounded non-mutation result, not byte-complete private-state introspection. No viewer, Windows, GPU, boot or release acceptance follows.

Before actual exporter/Windows viewer execution, independent v1 review reproduced a destructive directory-replacement race and foreign temporary-file publication race; viewer review identified a Windows reparse-traversal gap. These were synthetic/review findings, not reported original-data loss in an actual run. Earlier build-warning, test-invocation and setup failures remain retained. V2 fixes resolved all three findings in independently reviewed source and received source/synthetic acceptance. Evidence is still source/synthetic/cross-build only. Actual exporter execution, captured-artifact delivery and Windows viewer behavior remain unaccepted.

## Actual portable export/import — October 23, 05:05 update

One exact Linux producer invocation passed, reporting **2,175 command batches** and runtime refusal. Its private artifact was **2,846 bytes**; portable import/model rendering produced **6,108 bytes**. Independent review verified complete bounded decode, codec round-trip fidelity, model-text equivalence, frozen/untrusted/producer-reported labels, unchanged pins and scoped cleanup. Three existing-output constructor refusals preserved artifact bytes and selected metadata. They are not three more startup runs, publication attempts or exhaustive race tests. No visible GUI, Windows, full IDE, service fulfillment or boot follows from this acceptance.

## Windows viewer preflight failures and corrected validator

Preparation first encountered a path-metadata blocker, then a missing companion fixture. Those were resolved without claiming native execution. The v1 positive offline control subsequently failed because culture-sensitive prefix checking treated a valid trace as BOM-prefixed; zero native executables launched in that failed attempt. The failure is preserved, not relabeled as a viewer failure.

The v2 character/ordinal correction passed **24 trace-shape checks across four cultures**, then **33 offline controls**: one positive and 32 expected negative outcomes, with no unrun controls or timeouts. These use fabricated evidence and validate comparison/receipt rules, not native GUI behavior. The subsequent single native **111-check invocation passed 36 checks then failed bounded file load at check 37; 74 checks remained unrun**. An independent window and initial empty state were established, not successful artifact loading or pixel correctness. The harness exited 1; supervisor exited 0 with certain empty-job cleanup and no timeout. All 23 kit files and seven fixtures remained unchanged. The cause is unknown, not an established security denial. This is an identified execution report, not independently downloaded raw local receipts. The earlier offline BOM failure remains a separate event.

## Static original-loader history limit

Independent static review identified a conditional earlier A0:49 request before later GPU reset work, firmware-return-relative memory writes whose actual destinations are unresolved, and a synchronization result ignored by the handoff caller. This is positive original-code analysis, not an executed occurrence, hardware/dispatch proof or exhaustive queue/producer audit. Native independent-cold-start evidence cannot establish that original inherited history.

## Unchanged reader and frozen viewer in separately approved contexts — October 23, 06:09 update

A separate unchanged-reader diagnostic identified `QueryDosDeviceW` error 5 in the default context; one explicitly approved invocation passed the synthetic reader and model checks. That contrast does not identify the general access-control cause, resolve the original context, imply administrator status or grant reusable permissions. The later frozen-v2 harness was separately approved; its pass did not require source or security-setting changes.

The unchanged frozen Windows viewer subsequently passed **all 111 synthetic HWND/command/state checks** in a separately approved execution context: zero failed or unrun checks, an exact 113-record / 7,651-byte oracle match, supervisor/harness/validator exits 0 and an empty scoped job. Source, retained kit/history and security settings remained unchanged. The prior default-context result—36 passes, failure at check 37 and 74 unrun—is preserved, not repaired retroactively. This is reported executor evidence; raw PC receipts were not independently downloaded. It does not establish pixels, standalone inspector operation, actual-capture display, full IDE acceptance or game boot.

Independent review accepted the bounded result from the identified executor report, not an independent download or replay of raw Windows receipts. This is a later acceptance checkpoint, not a rewrite of the earlier 36-pass/check-37-failure/74-unrun attempt. No future unrestricted execution permission follows.

## Conditional loader range verification

A further independently reviewed static calculation keeps the firmware-return distinction explicit: conditional B0:57 return `U=0x874` localizes the next word load to `0x9e0`; it does **not** establish that the loaded base `R` equals `0x874`. Three independently loaded bases remain unknown. Store counts, interleaved copy order and conditional modular overlap predicates were checked under explicit alias and nontrapping-arithmetic assumptions. Only the enumerated fixed cache stores exclude selected-site overlap; no general dispatch non-overlap, executed loader mutation or inherited GPU state is established. The native GPU origin remains an observation-only model with unknown status, not a reset or idle snapshot.

## Original-input native prefix and separate Windows lifecycle — October 23, 07:07 update

A separately reviewed native loader prefix passed one authorized Linux original-input compatibility run: one build, one load and one native advance stopped at pending **A0:39**. It performed 4,032 modeled zero-word stores followed by an unknown saved-return-address overwrite, leaving 4,031 final known-zero words. All register masks and outside-range RAM were checked. The **20,195 modeled source-instruction count** is not a host-step, command-batch or capture count. Zero services and GPU operations completed; cleanup and pre/post integrity passed. Original instructions were not executed, and no firmware completion, inherited GPU state, A0:49 closure or game boot is established.

The first loader execution envelope received **NO GO**: an injected cleanup exception could propagate before owned-child/group cleanup was proven. That failed version remains preserved. A separate v2 keeps ownership through cleanup faults and cannot turn recovered cleanup into success; eight ordinary lifecycle controls plus three cleanup-fault regressions passed before the one authorized compatibility run.

A separate standalone-viewer candidate received source acceptance with **four additions and 457 baseline files unchanged**. Its Windows synthetic host-function lifecycle then passed **23 checks**, with an exact **25-record / 1,053-byte** oracle match, supervisor/harness/validator exits 0 and empty scoped cleanup, in the normal permitted context without security changes. This is an identified authorized executor report; raw PC receipts were not independently downloaded. It does **not** verify the real standalone launcher, pixels, actual-capture display, full IDE operation or game boot.

The earlier default-context 36-pass/check-37-failure/74-unrun result and separately approved 111-check pass remain preserved. The new lifecycle evidence is not an actual snapshot displayed by the standalone application; visual tooling and transfer-route review remain independent gates.

## Separate heap/continuation compatibility and synthetic-only successor — October 23, 08:05 update

Two later, separately authorized Linux compatibility runs are accepted: one initialized the persistent native heap policy and stopped at its return boundary; the other performed one load, prefix advance, heap initialization and fixed continuation, stopping **before `800108ec`**. The continuation modeled **13 source instructions and two word stores**, with zero initializer instructions or optional allocator calls. Unknown saved return-address bits were retained and not used for control; all register masks and outside-store RAM were checked. Exact authorization, outputs, pre/post integrity and reaped/empty process groups passed independent terminal review without a reviewer rerun.

The first continuation candidate received **NO GO** after synthetic mutation exposed an input-lineage binding gap. The separately reviewed v2 retains the successful admission category independently and rejects either allowed-category substitution before and after commit. The failed v1 and earlier cleanup-envelope rejection remain preserved; neither was relabeled as accepted.

These outcomes are explicitly **native policy**, not BIOS execution or equivalence. Native RAM/register preservation does not resolve original firmware side effects, dispatch history, allocator layout, GPU state or the three unresolved loaded bases. Original instructions were not executed; no integration, A0:49 completion or game boot follows.

A later initializer-prefix candidate has **source/synthetic acceptance only**: 127 author checks and 920 independent assertions. Its proposed fixed lowering models 26 source instructions and four stores, stopping at a pending 16-bit I_MASK write with applied=false. No actual-input run is accepted. Its execution preparation was blocked pending review; no retry or alternative route was attempted. This is not an applied interrupt-mask operation, GPU initialization or game boot.

## Static A0:39 effect report after native-policy acceptance — October 23, 09:05 update

The [new heap investigation](../../research/bios/HEAP-INITIALIZATION.md) supplies author-reported, digest-specific static evidence for an initial binding and a short leaf with five ordered stores. Field interpretation and a separate decoder reportedly agree; no recovered function or firmware execution is claimed. This adds concrete potential memory effects beyond the earlier uninspected-body gap, but does not measure a game occurrence or prove full-call ABI behavior. Private source bytes and raw receipts were not independently inspected for this documentation review.

The native heap/continuation results remain separately accepted within their explicit native-policy scope. RAM preservation in those runs is not evidence that original firmware preserved the same bytes. Earlier cleanup and lineage failures, the corrected candidates and the blocked initializer execution-preparation stage remain unchanged. No new native execution or game-boot milestone is recorded.

## S2 source-only lifecycle review — October 23

A completed independent review accepted the production IRQ/graphics controller feasibility **NO-GO**. Selected source identities were checked against accepted records; this was not complete ancestry revalidation or fresh execution evidence. No builds, tests, code changes or Windows actions occurred. Missing load termination, whole-owner retirement, single-call fault/stop and final message-ownership contracts prevent claiming a safe controller lifecycle from the existing interfaces.

The finding is profile-specific, not proof that all hypothetical reduced profiles are impossible or that ordinary destruction necessarily crashes. The earlier 111-check frozen-viewer and 23-check host-function results do not exercise a native-session worker and remain separately scoped. Visual acceptance and the initializer execution-preparation blocker remain unchanged; no blocked operation was retried.

## Synthetic mailbox evidence and sanitizer limits — October 23

Twelve author scenarios passed in optimized Linux, ASan/UBSan with leak detection disabled, and ThreadSanitizer modes. Independent optimized and ASan/UBSan tests covered cross-translation-unit host identity and cross-channel live-notice assignment/finalization; another reviewer scenario confirmed already-covered stale-wake recovery. The reviewer inspected the author logs but did not independently rerun the author suites. Finite schedules and sanitizer silence are not exhaustive race or liveness proof.

Both leak-enabled attempts failed because LeakSanitizer could not operate under host tracing. Targeted deletion/lifetime assertions passed, but no LeakSanitizer pass or exhaustive leak-free result follows. An initial reviewer self-move test expression failed warnings-as-errors compilation and was corrected in the test; no initial execution or primitive compilation defect was claimed. Eighteen selected accepted-source/metadata hashes matched, not complete ancestry revalidation.

Acceptance is isolated data-channel behavior only: no native session, original input, actual GUI endpoint, Windows execution or runtime regression was exercised. The data-channel finalization receipt cannot prove native-owner retirement. S2 and the separate initializer execution blocker remain unchanged.
