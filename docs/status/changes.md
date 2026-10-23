# What changed, why it matters, and what comes next

Generated from reviewed evidence data. Entries describe actual reviewed changes; an unrelated repository push does not add a capability milestone.

[Current tracker](../../README.md#progress-in-numbers) · [Maintenance](TRACKER.md)

## 2026-10-23 · numeric-checklist-baseline-01

**Evidence class:** documentation. **Runtime capability advanced:** no.

**Changed:** Added versioned named checklists, completed/remaining counts, percentages and a first recorded numeric baseline. Replaced the ambiguous evidence-square overview.

**Why:** You can see which concrete goals are accepted and which remain, without mistaking test totals for game completion.

**Next:** Append the next reviewed observation when a checklist changes; preserve definitions or create a clearly labeled new version.

**Evidence:** [source 1](../../docs/status/dashboard.md#named-checklists) · [source 2](../../docs/status/TRACKER.md).

## 2026-10-23 · tracker-living-01

**Evidence class:** documentation. **Runtime capability advanced:** no.

**Changed:** The progress page is now generated from one reviewed evidence file instead of hand-edited render snapshots.

**Why:** Future documentation updates can refresh the visible tracker and explain the change in plain English. A repository push alone cannot promote a capability.

**Next:** Keep the evidence file and this change ledger current in each authorized project-documentation update.

**Evidence:** [source 1](../../docs/status/TRACKER.md).

## 2026-10-23 · load-contract-review-01

**Evidence class:** source-review. **Runtime capability advanced:** no.

**Changed:** Load and Windows host-I/O reviews separated cancellation requests from real completion, resource settlement and worker retirement.

**Why:** A timeout or asynchronous handle does not prove safe bounded shutdown. The live-controller gate remains unmet.

**Next:** An accepted backend/product close contract is needed; weakening the product guarantee requires an explicit owner decision.

**Evidence:** [source 1](../../docs/status/dashboard.md#12-cancel-requested-is-not-work-retired) · [source 2](../../docs/status/current-status.md#ide-runtime-controller-source-only-feasibility-no-go).

## 2026-10-23 · observer-linux-01

**Evidence class:** synthetic-linux. **Runtime capability advanced:** yes, only within the cited scope.

**Changed:** Ten observer scenarios passed alongside the unchanged twelve mailbox scenarios in three Linux build modes.

**Why:** Delayed notifications recover sampled data; failures preserve stale/as-of labels without replaying native requests. The modes are repetitions, not extra unique tests.

**Next:** Review production load and owner retirement before integrating the observer with live controls.

**Evidence:** [source 1](../../docs/status/current-status.md#data-only-observer-linux-synthetic-acceptance) · [source 2](../../docs/status/validation.md#observer-candidate-validation--october-23).


## Numeric review history

Only recorded observations appear here. The first entry is a baseline, not a newly completed runtime milestone. A new checklist version starts a new comparison basis.

| Recorded review | Checklist version | Completed / total | Change note |
|---|---|---|---|
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | inspection v1 | 4 / 7 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | observation v1 | 2 / 4 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | loader v1 | 3 / 4 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | s2 v1 | 0 / 4 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | boot v1 | 0 / 1 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
| 2026-10-23 · `2026-10-23-numeric-baseline-01` | roadmap v1 | 5 / 20 | First numeric baseline from existing accepted records: five bounded roadmap foundations plus fifteen pending product goals, and five separate local checklists. No new runtime milestone or historical delta is invented. |
