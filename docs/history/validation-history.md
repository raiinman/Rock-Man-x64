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

A prior stage's actual Windows pass does **not** validate active inspector additions or the newer configuration candidate.

## Latest candidate at the pause

**Unfrozen, not actual-Windows-validated:** the CD configuration candidate advances reset/unmute and stops before an unsupported sound-register read. The isolated run reports 92 regression tests, 19 tool tests, 21 CLI cases and 18 Windows cross-builds passing. At the pause, remaining standalone checks and final acceptance receipts were still pending/unaccepted. The already-running aggregate drained at **21:39:13 UTC**: 19 completed stages, 17 successful and two failures due to missing preview fixtures; acceptance, frozen and retry flags remained false. No new post-pause retries or Windows configuration run occurred. Earlier shared-output attempts were inconclusive and excluded from final acceptance.

The isolated workflow requires separate outputs, pinned source/input identity, explicit command/exit receipts, CLI assertions, static artifact checks and final preservation/completion receipts. Until accepted, partial green subsets do not establish a final aggregate or release.

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
