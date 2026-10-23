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
