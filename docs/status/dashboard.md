# Living evidence tracker and findings

Generated from reviewed evidence data. This is documentation, not a playable game or a public test package.

**Last evidence review:** 2026-10-23 · `2026-10-23-native-evidence-02` · [reviewed basis 9ce9b94](https://github.com/raiinman/Rock-Man-x64/commit/9ce9b9497f496584c438b76b39d1b36f2f1e4d58).
**Latest repository change observed:** [c127531](https://github.com/raiinman/Rock-Man-x64/commit/c1275311c5c841405d000203f4b02aa9645145d4) · 2026-10-23T13:22:45-07:00 — docs: automate living tracker with evidence-gated progress and plain-English updates.
**Authored evidence update supplied:** the evidence file and its review identifier changed in the observed commit. Stages still mean only what the cited reviewed record establishes.

## Current explanation

**Now:** Parts of startup and the inspection tools have passed bounded tests. Native game boot is still unestablished, and live IDE controls are not safe to enable yet.

**Changed:** The data-only observer can recover delayed notices and label old snapshots honestly. New load reviews narrowed the shutdown problem; they did not solve it.

**Why:** We can inspect a stopped runtime without pretending it advanced. Safe cancellation and ownership still have to be proved before live controls can be connected.

**Next:** Establish a reviewed loading and shutdown contract, then review native-owner retirement and real UI integration. Keep the unresolved graphics service stopped.

[Plain-English change ledger](changes.md) · [Update contract](TRACKER.md) · [Reviewed source data](dashboard-data.json)

## Evidence tracks

| Workstream | Source | Synthetic | Linux | Windows | Full app | Scope / next |
|---|---|---|---|---|---|---|
| Native CD mode-00 | Reviewed | Bounded evidence | Bounded evidence | Bounded evidence | — | 69 Windows cases · 30 intentional refusals. Stops at the unsupported graphics-startup continuation. **Next:** Resolve the unsupported graphics continuation; do not invent a service result. [evidence](../../docs/status/current-status.md#accepted-native-windows-mode-00-stage) |
| Graphics diagnostic | Reviewed | Bounded evidence | Bounded evidence | — | — | 19 connected Linux cases · A0:49 pending. No Windows parity or GPU initialization established. **Next:** Establish the missing A0:49 effects and permitted implementation basis. [evidence](../../docs/status/current-status.md#diagnostic-continuation-bounded-linux-acceptance) |
| Owned startup capture | Reviewed | Bounded evidence | Bounded evidence | — | — | 60 captures · 253 allocation-failure injections. Bounded Linux/UBSan owner observations, not a live debugger. **Next:** Keep capture observation separate from native stepping and UI acceptance. [evidence](../../docs/status/current-status.md#bounded-actual-owned-capture) |
| Export \+ frozen viewer | Reviewed | Bounded evidence | Bounded evidence | Bounded evidence | — | Linux model import / 111 Windows synthetic checks. Different bounded Linux/Windows scopes; no actual-capture GUI display or pixel acceptance. **Next:** Verify real-launcher, pixels and actual-capture display separately. [evidence](../../docs/status/current-status.md#separately-approved-windows-viewer-result) |
| Source bytes / Back | Reviewed | Bounded evidence | — | Bounded evidence | — | 50 Windows synthetic command/state checks. No Linux execution claim in this row; visual preflight blocked before launch. **Next:** Obtain a permitted visual check; do not infer pixels from command tests. [evidence](../../docs/status/current-status.md#combined-candidate-and-ide-update) |
| Mailbox \+ observer | Reviewed | Bounded evidence | Bounded evidence | — | — | 12 mailbox \+ 10 observer scenarios · Linux only. Data-only channel; no Windows or native-controller integration. **Next:** Review production lifecycle contracts before any native controller connection. [evidence](../../docs/status/current-status.md#data-only-observer-linux-synthetic-acceptance) |
| Loader continuation | Reviewed | Bounded evidence | Bounded evidence | — | — | Native policy · stops before the initializer. No BIOS equivalence; later initializer remains synthetic-only and execution-blocked. **Next:** Preserve the initializer execution gate and unresolved firmware effects. [evidence](../../docs/status/current-status.md#later-native-policy-heap-and-continuation-acceptance) |
| S2 live IDE controller | NO-GO review | — | — | — | — | Source review complete · production admission NO-GO. Load termination, owner retirement, stop/fault and real UI/capture integration remain unresolved. **Next:** Establish loading, ownership, stop/fault and real UI/capture contracts. [evidence](../../docs/status/current-status.md#ide-runtime-controller-source-only-feasibility-no-go) |

Platform and synthetic cells can describe the same run. They are not additive, equally weighted units or a game-completion percentage. Full app means end-to-end game or complete IDE, not a component integration.

The exporter/frozen-viewer row combines **different scopes**: one actual Linux artifact-to-portable-model import and Windows synthetic HWND/command/state checks. It does not establish actual-capture GUI display on Windows. See [evidence](../../docs/status/current-status.md#actual-portable-exportimport-and-bounded-windows-viewer-acceptance) and [evidence](../../docs/status/current-status.md#separately-approved-windows-viewer-result).

<details>
<summary>Generated visual fallback for the same reviewed stages</summary>

![Generated evidence-stage bars](visuals/progress-dashboard.svg)

</details>

## Reconstruction findings

## 01 The texture layout was not linear

**Found:** The first full-width texture interpretation was wrong. Recovered upload traversal established tiled storage instead.

**Why it matters:** A file can pass size checks while its pixels are decoded in the wrong order. The decoder was corrected.

**Evidence:** ASSET \+ ORIGINAL-UPLOAD ANALYSIS. 32 × 32 — word / row sector tiles.

**Still unknown:** These are custom repacked structures, not ordinary TIM files or universal texture coverage.

**Sources:** [source 1](../../docs/history/milestones.md#4-recover-textures-and-local-model-parts) · [source 2](../../docs/technical/architecture.md#assets-and-rendering).

## 02 The pose packing is mapped

**Found:** Bit-origin reconstruction recovered sparse axes and an overlapping-store effect in one packed pose helper.

**Why it matters:** There is a testable mapping behind the pose decoder, not just a plausible-looking model.

**Evidence:** STATIC \+ COMPONENT EVIDENCE. 456 → 48 — input-bit vectors / outputs.

**Still unknown:** A fixed-block check, not a complete animation system or provenance clearance.

**Sources:** [source 1](../../docs/history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping) · [source 2](../../docs/technical/capability-matrix.md).

## 03 Sequence calls are not frames

**Found:** The primary updater was checked against a separate oracle. A zero duration expires after 256 update calls.

**Why it matters:** A repeating hold is not an end signal. Assuming a frame rate would change the animation semantics.

**Evidence:** COMPONENT / INSTRUCTION-ALGEBRA ORACLE. 262,144 — transitions checked.

**Still unknown:** 55 nonempty sequences are exposed; timing and a complete animation system are not established.

**Sources:** [source 1](../../docs/history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping).

## 04 Geometry is real; gameplay is not

**Found:** A bounded environment decoder matched 863 reference rows, retaining coordinates, UVs, flags and material evidence.

**Why it matters:** The scene has structured reconstruction evidence beyond an isolated visual guess.

**Evidence:** STATIC \+ DECODER COMPARISON. 8 / 854 — placements / four-corner faces.

**Still unknown:** Visibility, broader orientations, collision and material semantics remain incomplete.

**Sources:** [source 1](../../docs/history/milestones.md#7-recover-a-static-environment-then-distinguish-it-from-startup) · [source 2](../../docs/technical/capability-matrix.md).

## 05 A character is more than loose parts

**Found:** Recovered hierarchy and part mapping support a diagnostic character with 317 vertices and 316 faces.

**Why it matters:** Part identities connect to a skeleton; duplicate render packets were workspaces, not extra faces.

**Evidence:** STATIC \+ DIAGNOSTIC ASSEMBLY. 15 / 18 — joints / mesh parts.

**Still unknown:** Transforms are approximate. Full animation and original GPU/GTE fidelity are not established.

**Sources:** [source 1](../../docs/history/milestones.md#6-reconstruct-diagnostic-character-poses-and-sequence-stepping) · [source 2](../../docs/history/milestones.md#4-recover-textures-and-local-model-parts).

## 06 The first inspected map is not boot

**Found:** The zero-state startup path resolves to ST01. Its established direct order is INIT\_DAT → DEMO\_DAT → ST01.

**Why it matters:** The earlier ST1C environment cannot be substituted for the first startup scene or called a title screen.

**Evidence:** STATIC STARTUP \+ RESOURCE ANALYSIS. ST01 — scene 1 / subscene 0.

**Still unknown:** This is not the complete dependency set, an executed native scene or a boot result.

**Sources:** [source 1](../../docs/history/milestones.md#7-recover-a-static-environment-then-distinguish-it-from-startup).

## Frontier findings

## 07 Native policy is not BIOS equivalence

**Found:** Selected A0:39 analysis reports five ordered word stores. The accepted native heap policy deliberately preserves guest RAM.

**Why it matters:** A passing native-policy test does not prove the original firmware performed the same effects.

**Evidence:** FIRMWARE STATIC / NATIVE-POLICY CONTRAST. 5 stores — static heap-service effects.

**Still unknown:** Actual game-time dispatch, allocator invariants and inherited GPU state remain unresolved.

**Sources:** [source 1](../../docs/status/current-status.md#new-static-heap-evidence-does-not-establish-equivalence) · [source 2](../../research/bios/HEAP-INITIALIZATION.md#arguments-and-ordered-memory-effects) · [source 3](../../research/bios/PROVENANCE-REVIEW.md).

## 08 Observe without inventing a step

**Found:** A four-case envelope captured bounded owner state, including the actual pending A0:49 request.

**Why it matters:** Inspection can report where execution stopped without pretending the pending service completed.

**Evidence:** ACTUAL OWNED CAPTURE · LINUX/UBSAN. 60 \+ 253 — captures \+ injected failures.

**Still unknown:** Fingerprints are not full-state introspection. No Windows capture or live-debugger acceptance.

**Sources:** [source 1](../../docs/status/current-status.md#bounded-actual-owned-capture).

## 09 Old data is allowed to look old

**Found:** Delayed wakes recover sampled data; failed observations retain explicit stale/as-of labels without replaying requests.

**Why it matters:** An old snapshot must never silently masquerade as current runtime state.

**Evidence:** LINUX SYNTHETIC · THREE BUILD MODES. 10 \+ 12 — observer \+ mailbox scenarios.

**Still unknown:** Mode repetitions are not unique tests. No timing guarantee, LeakSanitizer pass or native-owner retirement.

**Sources:** [source 1](../../docs/status/current-status.md#data-only-observer-linux-synthetic-acceptance) · [source 2](../../docs/status/validation.md#observer-candidate-validation--october-23).

## 10 The original game reached story

**Found:** An author-reported emulator capture progressed past loading into the opening story, with observed entry and caller boundaries.

**Why it matters:** This is executed reference research, not merely a catalog of manuals or a static hypothesis.

**Evidence:** EXECUTED EMULATOR RESEARCH. EXECUTED — emulator research — not native.

**Still unknown:** Not native-port boot, physical-console proof, complete gameplay or implementation clearance.

**Sources:** [source 1](../../research/bios/ORIGINAL-GAME-STARTUP.md#past-loading-capture-and-first-call-detail) · [source 2](../../research/bios/PROVENANCE-REVIEW.md).

## 11 A0:49 is not a safe no-op

**Found:** Research observed GPU-access callbacks before a context-matched caller return; access payloads remain unknown.

**Why it matters:** Ignoring a return value does not mean the call had no effects. A success constant would invent state.

**Evidence:** STATIC \+ BOUNDED EMULATOR OBSERVATION. OPEN — native service / gpu frontier.

**Still unknown:** Effective dispatch, full ABI, GPU history and current native binding remain open.

**Sources:** [source 1](../../research/bios/ORIGINAL-GAME-STARTUP.md#caller-focused-follow-up) · [source 2](../../research/bios/ORIGINAL-GAME-STARTUP.md#original-input-and-caller-correlation) · [source 3](../../docs/status/current-status.md#evidence-limits-and-next-steps).

## 12 Cancel requested is not work retired

**Found:** New load and host-I/O reviews separate cancellation intent, actual completion, resource settlement and execution retirement.

**Why it matters:** A timeout or an overlapped handle cannot be relabeled as a safe, bounded shutdown.

**Evidence:** SOURCE \+ PRIMARY-DOCUMENT REVIEW ONLY. S2 NO-GO — load / owner / shutdown gates.

**Still unknown:** No admitted production backend, controller implementation or new Windows test. L1/P1 remain unmet.

The newer load and host-I/O findings are source/design reviews only: no implementation, build, synthetic/runtime test or Windows run occurred in those reviews. Cancellation intent, actual I/O completion, resource settlement and execution retirement remain distinct. No product guarantee is revised here; weakening the bounded-close requirement needs an explicit owner decision. Native-owner and provenance gates remain independent.

**Sources:** [source 1](../../docs/status/current-status.md#ide-runtime-controller-source-only-feasibility-no-go) · [source 2](https://learn.microsoft.com/en-us/windows/win32/api/ioapiset/nf-ioapiset-cancelioex) · [source 3](https://learn.microsoft.com/en-us/windows/win32/fileio/synchronous-and-asynchronous-i-o).

## Provenance

Private evidence is summarized and not independently reproducible here. PSX-SPX remains a restricted-provenance research reference, not cleared implementation authority.

Executed emulator research is author-reported reference behavior, not native game boot, physical-console equivalence or implementation clearance. PSX-SPX remains credited to Martin “nocash” Korth and community contributors and is not cleared implementation authority. [Full provenance boundary](../../research/bios/PROVENANCE-REVIEW.md).

<details>
<summary>Earlier explanatory graphics — dated 2026-10-23, not the live tracker</summary>

These archived explanatory boards are secondary references. The reviewed data and generated text above own current status.

![Earlier reconstruction findings](visuals/findings-01.svg)

![Earlier frontier findings](visuals/findings-02.svg)

</details>
