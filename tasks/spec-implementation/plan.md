# Implementation Plan: Rock Man x64 specifications

## Overview and baseline

Decompose the [shared specification](../../SPEC.md) and seven [capabilities](../../CAPABILITIES.md) into provider-first, verifiable increments for the existing native Windows game and integrated IDE. This document is the owner-requested planning deliverable, not authority to implement or execute it. Public `main` and local baseline were verified as `9583bb09929b38fdcd61042e432bd74433910e76`. Re-read actual head and contracts before integration.

The owner approved this separate destination. [Initial adoption plan](../plan.md) and [execution list](../todo.md) are preserved verbatim, including their external delivery-receipt convention. Their adoption publication was independently reported verified by the coordinator; an unchanged checkbox is not evidence of a missing delivery. Existing native/research queues retain their owners. This plan does not replace the separate existing implementation assignment, launch a worker wave or duplicate unanswered handoffs.

## Bounded support evidence: existing-file play

As reviewed October 30, 2026, 12:55:26 AM Arizona (MST), [one original-IDE existing-file play slice](../../docs/status/current-status.md#original-ide-existing-file-play--october-30) has reported portable integration and independent scoped review plus an inert Windows-target build. The [canonical build map](../../docs/status/dashboard.md#build-and-specification-plan) owns its bounded check and limits. This supports the SI-24 journey discussion without completing SI-24, its dependencies or any historical acceptance criterion. File selection/strict loading do not authenticate provenance; provider, provenance and execution gates remain unchanged. No task checkbox or dependency is changed by this evidence note.

As reviewed October 30, 2026, 3:31:38 AM Arizona (MST), a [separate bounded Windows existing-file play record](../../docs/status/current-status.md#original-ide-existing-file-play-windows-check--october-30) adds paused-child/editor-state observations and distinct owner movement/close testimony. Extra-child final revalidation stopped automation; later read-only follow-up observed process absence and the original launch session exit 0, with retained exported contents and no new test-state file. This supplements the earlier portable/inert-build record without accepting SI-24, changing dependencies or clearing production/provenance gates. The canonical build map remains the sole evidence-state authority.

## Bounded original mission evidence: front door

As reviewed October 30, 2026, 7:01:12 AM Arizona (MST), the [original mission front door](../../docs/status/current-status.md#original-mission-front-door--october-30) has reported independently reviewed portable/model integration and two inert Windows-target builds. New/Continue state intent, saved continuation and outer-loop lifecycle evidence stay distinct from actual Windows execution. The canonical build map owns the bounded check; no production startup, gameplay/save refinement, integrated-IDE task, dependency or historical acceptance is completed by this support record.

As reviewed October 30, 2026, 8:57:26 AM Arizona (MST), [Save & Return](../../docs/status/current-status.md#original-save--return--october-30) and [accepted-shot audio](../../docs/status/current-status.md#original-accepted-shot-audio--october-30) have separate reported portable/model reviews and inert Windows-target evidence. Adapted publication, callback settlement, owned-worker cleanup and earlier-variant/final-focused applicability remain bounded. No Windows execution, production save/audio/runtime acceptance, broad task state or dependency changes. The canonical build map owns the two checks.

As reviewed October 30, 2026, 10:12:08 AM Arizona (MST), the [original reactive stationary guard](../../docs/status/current-status.md#original-reactive-stationary-guard--october-30) has reported independent portable/model checks and two inert Windows-target builds. Natural traversal, analytic/seeded boundaries, reused dependencies and cross-policy owner/state nonadoption retain their specific limits. No general LOS/moving AI, Windows/user or production acceptance, task state or dependency changes. The canonical build map owns the bounded record.

As reviewed October 30, 2026, 11:52:33 AM Arizona (MST), [optional original lateral patrol](../../docs/status/current-status.md#original-lateral-patrol--october-30) has reported independent portable/model review and inert Windows-target checks. Author optimized/O0 sanitizer and independent optimized/O1 sanitizer cohorts, explicitly seeded boundaries, failed compile/oracle history and distinct save policies retain their limits. No Windows/device/visual, broad AI/gameplay/IDE or production acceptance, task state or dependency changes. The canonical build map owns the bounded record.

## Architecture decisions and readiness

- The [capability map](../../CAPABILITIES.md#directional-dependencies) owns typed consumer-to-provider edges. Runtime/data order is original-data-access before inspection/startup; runtime-control requires startup and separately resolved lifecycle gates. Product acceptance composition and evidence/reporting edges are not source imports.
- Review a provider contract before its consumer. Inspection and startup are independent after their particular media boundary is satisfied. Research is an evidence prerequisite only when the selected behavior requires it. Reporting may proceed at any honest checkpoint, including NO-GO.
- Preserve accepted foundations; do not rebuild inventory, diagnostic assets, offline editor, bounded CD startup or portable capture merely to restate their specs. A changed behavior gets a genuine focused RED/GREEN, or characterization for a refactor, and meaningful regression in its owning private workspace.
- Tasks 01–15 describe bounded readiness and conditional native slices. Tasks 16–24 and 26–27 are **scope-refinement tasks**, not implementation-ready production work: providers, oracles and private layout are unspecified in the adopted product spec. Each produces one bounded specification/test proposal and privately owned child tasks before any implementation. No guessed runtime API, test command or broad gameplay build is introduced.
- Product refinement order is a review order selected to expose scene/lifecycle risk first. It does not establish unverified source dependencies. Actual providers and authorization must be recorded before dependent implementation; refine oversized work in place. Task 25 applies before implementation use of every evidence-dependent slice, even where its index appears later.
- Existing settled authorization carries forward. Obtain only missing authority for a selected slice; this planning deliverable neither cancels nor permanently parks already-authorized native work. SI-03/SI-04 are prerequisites only where that slice actually consumes their findings/contracts; record any newly identified dependency rather than imposing it on unrelated refinement.
- The task list target is [todo.md](todo.md). Its unchecked boxes record planned work, never acceptance. [Canonical evidence](../../docs/status/dashboard-data.json) alone owns criterion text, versions, accepted flags and numeric history; existing private worker queues own implementation execution. Reconcile an existing matching task instead of issuing a duplicate.

## Dependency graph

Arrows below mean prerequisite -> dependent task, distinct from the capability map's consumer -> provider convention. Within the startup lane, execute SI-01–03, SI-25 and SI-04–06 in the listed order. Other lanes follow their explicit prerequisites and need not wait for unrelated A0:49 work. SI-25 is a cross-cutting provenance gate before implementation use, not a late clearance shortcut.

```text
01 -> 02,03 -> 04 -> 05 -> 06
02 -> 07 -> 08                  inspection can proceed independently
02 -> 09 -> 10                  read-only observation
04 -> 11 -> 12 -> 13 -> 14 -> 15; 10 -> 14; 05 -> 15
01 -> 16 -> 17,18,19,20,23; 18,19,20 -> 21
02 -> 22; 08,10,15 -> 24
01 -> 25; 25 gates each selected implementation's provenance
24,25 -> 26; 06,17,21,22,23,24,26 -> 27
28 -> 29 -> 30                  plan review/reporting need not wait for product work
```

Completion of a refinement dependency authorizes only the next refinement review. It does not prove an implemented provider exists. Task 27 explicitly requires completed underlying implementation/evidence before any future execution.

## Task List

### Provider and current blocker

- [SI-01: Bind a selected private slice to its owner](todo.md#si-01)
- [SI-02: Qualify the read-only media provider](todo.md#si-02)
- [SI-03: Reconcile one retained research gap](todo.md#si-03)
- [SI-25: Review the selected implementation provenance](todo.md#si-25)
- [SI-04: Bind the actual startup producer seam](todo.md#si-04)
- [SI-05: Implement one authorized startup continuation](todo.md#si-05)
- [SI-06: Qualify the selected native Windows startup path](todo.md#si-06)

### Independent diagnostic qualification

- [SI-07: Verify the real inspection launcher](todo.md#si-07)
- [SI-08: Verify actual-capture viewer behavior](todo.md#si-08)
- [SI-09: Qualify data-only observation on Windows](todo.md#si-09)
- [SI-10: Integrate one read-only observation endpoint](todo.md#si-10)

### Production control safety

- [SI-11: Specify bounded production loading](todo.md#si-11)
- [SI-12: Specify whole-owner retirement](todo.md#si-12)
- [SI-13: Specify single-call stop and fault](todo.md#si-13)
- [SI-14: Specify the real controller endpoint lifecycle](todo.md#si-14)
- [SI-15: Implement one permitted controller operation](todo.md#si-15)

### Production scope refinement

- [SI-16: Refine the first production scene slice](todo.md#si-16)
- [SI-17: Refine one production rendering slice](todo.md#si-17)
- [SI-18: Refine one integrated animation slice](todo.md#si-18)
- [SI-19: Refine one controls and camera journey](todo.md#si-19)
- [SI-20: Refine one world interaction slice](todo.md#si-20)
- [SI-21: Refine one gameplay progression journey](todo.md#si-21)
- [SI-22: Refine one decoded audio output slice](todo.md#si-22)
- [SI-23: Refine one game save and restore slice](todo.md#si-23)
- [SI-24: Refine the integrated IDE journey](todo.md#si-24)
- [SI-26: Refine the native Windows package journey](todo.md#si-26)
- [SI-27: Define end-to-end product acceptance](todo.md#si-27)

### Planning review and delivery

- [SI-28: Review the exact planning candidate](todo.md#si-28)
- [SI-29: Integrate the canonical documentation review](todo.md#si-29)
- [SI-30: Verify approved publication](todo.md#si-30)

## Checkpoints and parallel ownership

The task list contains a checkpoint after each two or three tasks. A checkpoint records exact completed, blocked and not-run outcomes, verifies provider boundary preservation, and resolves consequential open questions before dependent work. Unrelated authorized work can continue. No checkpoint grants initializer, S2, source access or execution authority.

After 01–03, inspection qualification (07–10), startup seam work (04–06) and bounded research reconciliation may be independently assigned to their existing owners only after availability/authority is verified. Loading/retirement/stop/endpoint reviews remain sequential because they share lifecycle state. Production refinement for rendering, animation, controls, collision, audio and persistence may proceed independently after each actual provider contract is agreed; shared scene/API changes require a single named provider owner and reconciliation before consumers change. Do not assume workers are running. Follow the root non-primary model preference and wave-completion rule for any later assignment; this plan spawns none.

## Traceability to authoritative acceptance

These references locate the original criteria; the task list does not redefine or duplicate them. “All” means every existing item in that named checklist, not a new milestone set.

| Specification | Tasks | Existing criteria / boundary |
|---|---|---|
| [Original data](../../SPEC-original-data-access.md) | 01–02 | roadmap/source-inventory; inspection input vs production media authority |
| [Inspection](../../SPEC-native-inspection.md) | 07–10 | roadmap/diagnostic-assets, roadmap/offline-editor, roadmap/portable-observation retained; inspection/all; observation/all; roadmap/windows-viewer |
| [Startup](../../SPEC-native-startup.md) | 03–06 | roadmap/cd-startup retained; loader/all; boot/native-boot; roadmap/native-boot separately |
| [Runtime control](../../SPEC-native-runtime-control.md) | 11–15 | s2/load, s2/retirement, s2/stop, s2/integration; roadmap/live-controller |
| [Game delivery](../../SPEC-native-game-delivery.md) | 16–27 | roadmap/scene-lifecycle, renderer, animation, controls-camera, collision, gameplay, audio, game-saves, integrated-ide, provenance, package, end-to-end; Windows viewer/control/boot supplied separately |
| [Research](../../SPEC-reference-research.md) | 03, 25; selected slices as needed | Existing Atlas-first/provenance/hand-off contract; roadmap/provenance remains a separate implementation review |
| [Tracker](../../SPEC-documentation-tracker.md) | 28–30 at any reviewed stage | Existing TRACKER.md and five-output contract; no additional game milestone |

## Standing Definition of Done

Apply the supplied planning-and-task-breakdown skill and its definition-of-done reference within [shared project requirements](../../SPEC.md#living-specifications-and-definition-of-done). Every task clears its acceptance criteria **and** applicable correctness/quality, integration/documentation and review gates. For documentation-only refinement, validate requirements, ownership, evidence, links, privacy and consistency instead of inventing runtime tests. For later authorized behavior changes, retain actual baseline, focused genuine RED/GREEN or characterization, failure paths, meaningful regression, independent review and exact platform limits. Never call unverified behavior done. Address applicable data handling, observability and recovery in the selected contract without commissioning unrelated security changes. Record spec/DOX/task updates and acceptance-owner decision separately. Release tasks additionally require package/journey evidence and actual publication authority.

Only the public commands in [SPEC.md](../../SPEC.md#verified-commands-and-flags) are verified here. Native focused test, build, regression and manual procedures are **evidence dependencies** owned by the private target; Task 01 must obtain exact commands/flags and current receipts before a later slice runs. Do not substitute generic compiler/build/test invocations or publish private source identities. Public checks do not establish native correctness, visible pixels, audible output or game boot.

## Risks, blockers and revisit triggers

| Risk / exact gap | Impact | Owner / mitigation / revisit trigger |
|---|---|---|
| Current private baseline, source roles, full commands and ongoing task state unavailable publicly | Blocks selected private implementation, not this plan | Existing native owner; Task 01 returns a verified private receipt or named access/authority blocker |
| Completed missing-function explanation is publicly acknowledged: the proposed A0:49 service entry and real submission/terminal producer/post-return consumer are absent | Blocks dependent continuation and boot claims; not an outstanding research assignment | Native adapter owner; Task 04 reuses the completed explanation and reviews a newly selected real seam only if one exists; otherwise retain the known absence and choose an independent authorized lane. No repeated gap card |
| Initializer preparation remains blocked | No actual-input initializer work commissioned | Existing review owner; only materially new applicable permission/evidence can reopen the separate task; this plan never retries it |
| Real launcher/pixels/actual-capture GUI and Windows observer evidence absent | Inspection platform criteria stay pending | Existing inspection/observation owners; Tasks 07–10 wait for verified access/procedure/authority and actual receipts |
| S2 loading, whole-owner retirement, stop/fault and endpoint finalization unresolved | Runtime controls stay disabled, NO-GO | Production provider/controller owners; Tasks 11–15 require actual contracts, proof and eligibility decision; four gates alone are not sufficient proof |
| Unselected production behavior has no agreed provider/oracle/source layout | Speculative implementation would be misleading | Product/domain owners; Tasks 16–27 refine one outcome per domain and discover real dependencies before private implementation tasks |
| Restricted references and original/private material | Blocks affected use/publication | Existing provenance owner; Task 25 preserves exposure/history; exact clearance required before use; public original summaries only |
| Concurrent presentation work and changing public head | Conflicting writes or false publication claims | Coordinator owns combined tracker/navigation integration and exact-diff review; Tasks 29–30 re-read head, preserve concurrent work and verify actual workflow |

## Open questions and next decision

No scope decision prevents reviewing this planning candidate. Before dependent private work: which existing owner/task holds the exact seam, what is the actual baseline/procedure and permitted oracle, what producer/effects are missing, and what authority covers the specific run? Those remain evidence dependencies with the task owners above. Do not guess private paths or activity. Switchboard stays paused. Atlas-inspired navigation, front-page/heatmap redesign and separate analysis tooling are outside this implementation plan.

The immediate deliverable is Tasks 28–30's planning review path, not execution of Tasks 01–27. This worker prepares and validates the candidate; the parent reviews the exact diff, integrates one canonical tracker review and handles any separately approved publication. No push or deployment is performed here.
