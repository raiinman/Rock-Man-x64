# Visual progress and findings ledger

**Snapshot: 2026-10-23.** Visuals summarize the published project record at commit [`e32df90`](https://github.com/raiinman/Rock-Man-x64/commit/e32df907d72f65e0067a0b56ad56c1f65bb74de7), plus the separately labeled source-only load/host-I/O reviews described in finding 12. This is not a live dashboard, a source release or a completion percentage.

**Native game boot is not established. Production S2 remains NO-GO.** Private validation is reported evidence that cannot be independently reproduced from this documentation-only repository. Original inputs, private captures, packages and implementation remain excluded.

[Back to the visual overview](../../README.md) · [Current status](current-status.md) · [Structured evidence data](dashboard-data.json)

## Evidence tracks

![Workstream evidence-stage bars](visuals/progress-dashboard.svg)

The bars are independent evidence classifications, not a sequential recipe or equal units of work. Synthetic/component describes inputs and scope; Linux/Windows describe the execution platform, so those cells can describe the same run. **Do not add filled segments or suite counts into a game-completion score.** “Full app” means end-to-end game or complete IDE acceptance, not a component integration. A dash means no acceptance claimed here, not a failed test or proof no other evidence exists.

| Workstream | Source | Synthetic/component | Linux | Windows | Full app | Exact scope and source |
|---|---|---|---|---|---|---|
| Native CD mode-00 | Reviewed | Bounded evidence | Bounded evidence | Bounded evidence | — | 69 Windows cases · 30 intentional refusals. Stops at the unsupported graphics-startup continuation. [Evidence](current-status.md#accepted-native-windows-mode-00-stage) |
| Graphics diagnostic | Reviewed | Bounded evidence | Bounded evidence | — | — | 19 connected Linux cases · A0:49 pending. No Windows parity or GPU initialization established. [Evidence](current-status.md#diagnostic-continuation-bounded-linux-acceptance) |
| Owned startup capture | Reviewed | Bounded evidence | Bounded evidence | — | — | 60 captures · 253 allocation-failure injections. Bounded Linux/UBSan owner observations, not a live debugger. [Evidence](current-status.md#bounded-actual-owned-capture) |
| Export + frozen viewer | Reviewed | Bounded evidence | Bounded evidence | Bounded evidence | — | Linux model import / 111 Windows synthetic checks. Different bounded Linux/Windows scopes; no actual-capture GUI display or pixel acceptance. [Evidence](current-status.md#separately-approved-windows-viewer-result) |
| Source bytes / Back | Reviewed | Bounded evidence | — | Bounded evidence | — | 50 Windows synthetic command/state checks. No Linux execution claim in this row; visual preflight blocked before launch. [Evidence](current-status.md#combined-candidate-and-ide-update) |
| Mailbox + observer | Reviewed | Bounded evidence | Bounded evidence | — | — | 12 mailbox + 10 observer scenarios · Linux only. Data-only channel; no Windows or native-controller integration. [Evidence](current-status.md#data-only-observer-linux-synthetic-acceptance) |
| Loader continuation | Reviewed | Bounded evidence | Bounded evidence | — | — | Native policy · stops before the initializer. No BIOS equivalence; later initializer remains synthetic-only and execution-blocked. [Evidence](current-status.md#later-native-policy-heap-and-continuation-acceptance) |
| S2 live IDE controller | NO-GO review | — | — | — | — | Source review complete · production admission NO-GO. Load termination, owner retirement, stop/fault and real UI/capture integration remain unresolved. [Evidence](current-status.md#ide-runtime-controller-source-only-feasibility-no-go) |

The export/frozen-viewer row deliberately joins two **different bounded scopes**: [one actual Linux artifact-to-portable-model import](current-status.md#actual-portable-exportimport-and-bounded-windows-viewer-acceptance), and [111 synthetic Windows HWND/command/state checks](current-status.md#separately-approved-windows-viewer-result). It does not claim actual-capture display on Windows. Source bytes/Back has no Linux execution claim in this dashboard.

## Reconstruction findings

![Six reconstruction findings](visuals/findings-01.svg)

## 01 The texture layout was not linear

**What we learned:** The first full-width texture interpretation was wrong. Recovered upload traversal established tiled storage instead.

**Why it matters:** A file can pass size checks while its pixels are decoded in the wrong order. The decoder was corrected.

**Evidence:** ASSET + ORIGINAL-UPLOAD ANALYSIS. Visible marker: **32 × 32 — word / row sector tiles**.

**Remaining unknown:** These are custom repacked structures, not ordinary TIM files or universal texture coverage.

**Sources:** [Source 1](../history/milestones.md#4-recover-textures-and-local-model-parts) · [Source 2](../technical/architecture.md#assets-and-rendering).

## 02 The pose packing is mapped

**What we learned:** Bit-origin reconstruction recovered sparse axes and an overlapping-store effect in one packed pose helper.

**Why it matters:** There is a testable mapping behind the pose decoder, not just a plausible-looking model.

**Evidence:** STATIC + COMPONENT EVIDENCE. Visible marker: **456 → 48 — input-bit vectors / outputs**.

**Remaining unknown:** A fixed-block check, not a complete animation system or provenance clearance.

**Sources:** [Source 1](../history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping) · [Source 2](../technical/capability-matrix.md).

## 03 Sequence calls are not frames

**What we learned:** The primary updater was checked against a separate oracle. A zero duration expires after 256 update calls.

**Why it matters:** A repeating hold is not an end signal. Assuming a frame rate would change the animation semantics.

**Evidence:** COMPONENT / INSTRUCTION-ALGEBRA ORACLE. Visible marker: **262,144 — transitions checked**.

**Remaining unknown:** 55 nonempty sequences are exposed; timing and a complete animation system are not established.

**Sources:** [Source 1](../history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping).

## 04 Geometry is real; gameplay is not

**What we learned:** A bounded environment decoder matched 863 reference rows, retaining coordinates, UVs, flags and material evidence.

**Why it matters:** The scene has structured reconstruction evidence beyond an isolated visual guess.

**Evidence:** STATIC + DECODER COMPARISON. Visible marker: **8 / 854 — placements / four-corner faces**.

**Remaining unknown:** Visibility, broader orientations, collision and material semantics remain incomplete.

**Sources:** [Source 1](../history/milestones.md#7-recover-a-static-environment-then-distinguish-it-from-startup) · [Source 2](../technical/capability-matrix.md).

## 05 A character is more than loose parts

**What we learned:** Recovered hierarchy and part mapping support a diagnostic character with 317 vertices and 316 faces.

**Why it matters:** Part identities connect to a skeleton; duplicate render packets were workspaces, not extra faces.

**Evidence:** STATIC + DIAGNOSTIC ASSEMBLY. Visible marker: **15 / 18 — joints / mesh parts**.

**Remaining unknown:** Transforms are approximate. Full animation and original GPU/GTE fidelity are not established.

**Sources:** [Source 1](../history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping) · [Source 2](../history/milestones.md#4-recover-textures-and-local-model-parts).

## 06 The first inspected map is not boot

**What we learned:** The zero-state startup path resolves to ST01. Its established direct order is INIT_DAT → DEMO_DAT → ST01.

**Why it matters:** The earlier ST1C environment cannot be substituted for the first startup scene or called a title screen.

**Evidence:** STATIC STARTUP + RESOURCE ANALYSIS. Visible marker: **ST01 — scene 1 / subscene 0**.

**Remaining unknown:** This is not the complete dependency set, an executed native scene or a boot result.

**Sources:** [Source 1](../history/milestones.md#7-recover-a-static-environment-then-distinguish-it-from-startup).

## Frontier findings

![Six frontier findings](visuals/findings-02.svg)

## 07 Native policy is not BIOS equivalence

**What we learned:** Selected A0:39 analysis reports five ordered word stores. The accepted native heap policy deliberately preserves guest RAM.

**Why it matters:** A passing native-policy test does not prove the original firmware performed the same effects.

**Evidence:** FIRMWARE STATIC / NATIVE-POLICY CONTRAST. Visible marker: **5 stores — static heap-service effects**.

**Remaining unknown:** Actual game-time dispatch, allocator invariants and inherited GPU state remain unresolved.

**Sources:** [Source 1](current-status.md#new-static-heap-evidence-does-not-establish-equivalence) · [Source 2](../../research/bios/HEAP-INITIALIZATION.md#arguments-and-ordered-memory-effects) · [Source 3](../../research/bios/PROVENANCE-REVIEW.md).

## 08 Observe without inventing a step

**What we learned:** A four-case envelope captured bounded owner state, including the actual pending A0:49 request.

**Why it matters:** Inspection can report where execution stopped without pretending the pending service completed.

**Evidence:** ACTUAL OWNED CAPTURE · LINUX/UBSAN. Visible marker: **60 + 253 — captures + injected failures**.

**Remaining unknown:** Fingerprints are not full-state introspection. No Windows capture or live-debugger acceptance.

**Sources:** [Source 1](current-status.md#bounded-actual-owned-capture).

## 09 Old data is allowed to look old

**What we learned:** Delayed wakes recover sampled data; failed observations retain explicit stale/as-of labels without replaying requests.

**Why it matters:** An old snapshot must never silently masquerade as current runtime state.

**Evidence:** LINUX SYNTHETIC · THREE BUILD MODES. Visible marker: **10 + 12 — observer + mailbox scenarios**.

**Remaining unknown:** Mode repetitions are not unique tests. No timing guarantee, LeakSanitizer pass or native-owner retirement.

**Sources:** [Source 1](current-status.md#data-only-observer-linux-synthetic-acceptance) · [Source 2](validation.md#observer-candidate-validation--october-23).

## 10 The original game reached story

**What we learned:** An author-reported emulator capture progressed past loading into the opening story, with observed entry and caller boundaries.

**Why it matters:** This is executed reference research, not merely a catalog of manuals or a static hypothesis.

**Evidence:** EXECUTED EMULATOR RESEARCH. Visible marker: **EXECUTED — emulator research — not native**.

**Remaining unknown:** Not native-port boot, physical-console proof, complete gameplay or implementation clearance.

**Sources:** [Source 1](../../research/bios/ORIGINAL-GAME-STARTUP.md#past-loading-capture-and-first-call-detail) · [Source 2](../../research/bios/PROVENANCE-REVIEW.md).

## 11 A0:49 is not a safe no-op

**What we learned:** Research observed GPU-access callbacks before a context-matched caller return; access payloads remain unknown.

**Why it matters:** Ignoring a return value does not mean the call had no effects. A success constant would invent state.

**Evidence:** STATIC + BOUNDED EMULATOR OBSERVATION. Visible marker: **OPEN — native service / gpu frontier**.

**Remaining unknown:** Effective dispatch, full ABI, GPU history and current native binding remain open.

**Sources:** [Source 1](../../research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up) · [Source 2](../../research/bios/ORIGINAL-GAME-STARTUP.md#original-input-and-caller-correlation) · [Source 3](current-status.md#evidence-limits-and-next-steps).

## 12 Cancel requested is not work retired

**What we learned:** New load and host-I/O reviews separate cancellation intent, actual completion, resource settlement and execution retirement.

**Why it matters:** A timeout or an overlapped handle cannot be relabeled as a safe, bounded shutdown.

**Evidence:** SOURCE + PRIMARY-DOCUMENT REVIEW ONLY. Visible marker: **S2 NO-GO — load / owner / shutdown gates**.

**Remaining unknown:** No admitted production backend, controller implementation or new Windows test. L1/P1 remain unmet.

This is a new **sanitized source/design-review summary**, not a newly executed milestone. The load review found that the whole production operation includes admission, input validation, native-owner construction, image loading and later publication; an image-reader cancellation flag alone cannot establish retirement of the whole operation. The host-I/O review found a real matching-operation completion authority for conditional resource draining, but no sufficient universal bounded application-close guarantee. L1 and P1 remain unmet. No producer implementation, build, synthetic/runtime test, Windows run or native integration was performed by these reviews.

Microsoft documents that cancellation requests do not wait for completion and that asynchronous-handle I/O can still execute synchronously. **Inference:** an observation timeout, chunk size or overlapped flag is not by itself a producer-retirement deadline. This is not a claim that every load hangs or that no suitable backend could ever exist. The next dependency is an accepted backend/product close contract, not another observer test or a guessed success state. No product guarantee is revised here; weakening it would require an explicit owner decision, and the independent native-owner and provenance gates would remain.

**Sources:** [Source 1](current-status.md#ide-runtime-controller-source-only-feasibility-no-go) · [Source 2](https://learn.microsoft.com/en-us/windows/win32/api/ioapiset/nf-ioapiset-cancelioex) · [Source 3](https://learn.microsoft.com/en-us/windows/win32/fileio/synchronous-and-asynchronous-i-o).

## Additional validation receipts worth keeping separate

| Receipt | What it establishes | What it does not |
|---|---|---|
| 69 mode-00 Windows cases, including 30 intentional refusals | Bounded success/refusal behavior on Windows | Graphics startup, GPU initialization or native boot. [Evidence](current-status.md#accepted-native-windows-mode-00-stage) |
| 96,596 fault cuts at 29 targeted allocation checkpoints | No late commits observed in that specific Linux sweep | Exhaustive allocation coverage or Windows parity. [Evidence](current-status.md#diagnostic-continuation-bounded-linux-acceptance) |
| 111 Windows viewer checks; earlier check-37 failure retained | A later approved-context synthetic command/state pass | Pixel QA, a general access fix or actual-capture display. [Evidence](current-status.md#separately-approved-windows-viewer-result) |
| 23 standalone host-function lifecycle checks | Scoped Windows host lifetime behavior and cleanup | Real-launcher, pixel or actual-capture acceptance. [Evidence](current-status.md#standalone-viewer-lifecycle-and-remaining-access-gates) |

## Provenance and maintenance

- Executed emulator research and static firmware interpretation are separate from native implementation evidence. Neither physical-console equivalence nor independent implementation follows from agreement with a reference.
- PSX-SPX is credited to Martin “nocash” Korth and community contributors and remains a **restricted-provenance research reference, not cleared implementation authority**. Sony/firmware provenance and retained exposure history are not erased by paraphrasing. See the [research provenance contract](../../research/bios/PROVENANCE-REVIEW.md).
- The graphics are original text-and-shape explanations. They contain no original game artwork, private screenshots, captured frames, code, external embeds or remote services.
- Every visible marker and workstream is mirrored in [dashboard-data.json](dashboard-data.json). Update the date, stage, source and remaining unknown together, then render and inspect all changed graphics. See [status maintenance](AGENTS.md) and [graphics maintenance](visuals/AGENTS.md).
- Research/catalog and license files are untouched by this visual presentation update. Existing failures and later acceptances remain in the historical record.
