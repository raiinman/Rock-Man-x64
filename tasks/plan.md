# Initial spec adoption plan

## Assumptions and destination

This is the bounded spec adoption for Rock Man x64, not a replacement game roadmap. The pinned public tree has no preexisting `tasks/` plan; existing technical specs, research plans and canonical tracker are preserved. Private implementation plans and their unfinished work stay with their owners. No claim is made that other private workspaces lack plans.

## Dependency-ordered checkpoints

| Order / task | Complete vertical outcome | Depends on | Evidence / stop condition |
|---|---|---|---|
| 1 — `adopt-discover` | Establish exact public baseline, applicable DOX, existing specifications/plans and acceptance authority | None | Complete tree and relevant contracts inspected; preserve all prior files; no absence claim beyond inspected scope |
| 2 — `adopt-specify` | Add typed capability map and thin specs tied to existing objectives/criteria, with assumptions and private gaps explicit | 1 | Every in-repo ID has a provider contract; no cycles, invented API or new acceptance; external tooling stays separate |
| 3 — `adopt-validate` | Validate the actual local documentation candidate and perform DOX/privacy review | 2 | Public suites/drift/links/whitespace pass; preserved paths and acceptance unchanged; limitations recorded outside public evidence |
| 4 — `adopt-review` | Resolve exact candidate review, then prepare the true documentation tracker review/zero-delta observation | 3 | Actual review basis/time; no altered old observations or acceptance; generated outputs and exact diff rechecked |
| 5 — `adopt-publish` | Publish only the approved documentation diff and verify remote result | 4 plus applicable bounded publication authority | Re-read current head; expected-head non-force update; exact content/preservation and real workflow outcome verified |

No native implementation step is hidden in this plan. Ongoing code/research/tooling workers retain their tasks and authority. A later selected behavior change follows Specify -> Plan -> Tasks -> Implement in its owning workspace with genuine RED/GREEN or characterization evidence; this plan does not commission it.

## File-scoped drafting breakdown

The existing `adopt-specify` ID remains the aggregate drafting checkpoint. The groups below are a truthful breakdown of the **already drafted local candidate**, added for review and future bounded corrections. They do not assert a newly reconstructed execution chronology, distinct past events or native acceptance. Each group touches at most five files; dependency arrows describe review order, not invented historical scheduling.

| Subtask / dependency | Scoped files | Acceptance and verification |
|---|---|---|
| `adopt-specify-shared` / `adopt-discover` | `CAPABILITIES.md`, `SPEC.md`, `AGENTS.md`, `README.md` | Explicit assumptions, six shared areas, typed acyclic dependencies and provider-first eligibility; verify public provenance, links, DOX/navigation and unchanged acceptance authority |
| `adopt-specify-providers` / shared | `SPEC-original-data-access.md`, `SPEC-reference-research.md` | Provider-owned media/evidence contracts link existing sources without widening supported input or provenance; verify exact provider scope, links and criterion IDs |
| `adopt-specify-consumers` / providers | `SPEC-native-inspection.md`, `SPEC-native-startup.md` | Consumers reference provider boundaries and retain diagnostic/startup separation and unsupported stops; verify edge/criterion traceability and no private implementation claims |
| `adopt-specify-gated-targets` / consumers | `SPEC-native-runtime-control.md`, `SPEC-native-game-delivery.md` | S2 NO-GO and the complete existing product target remain distinct from foundations; verify no invented API, execution authority or accepted criterion |
| `adopt-specify-reporting` / shared; reviewed module scopes for cross-links | `SPEC-documentation-tracker.md` | Canonical acceptance and five-output contract remain unchanged; verify reporting can proceed at any reviewed checkpoint and publication is still pending |
| `adopt-specify-records` / validated specification scope | `tasks/AGENTS.md`, `tasks/plan.md`, `tasks/todo.md` | Adoption-only tasks retain aggregate IDs, unfinished review/publication and honest draft state; verify exact scoped file lists, checked-state truthfulness and no duplicate game roadmap |

These are documentation drafting/review slices. Their acceptance is the listed document contract, not a behavioral RED/GREEN claim. The aggregate `adopt-validate` checkpoint owns cross-file consistency, preservation, public documentation suites and generated-drift verification.

## Completion and unresolved gates

The local candidate is ready for review only after checkpoint 3. Adoption is not published or tracker-complete until checkpoints 4 and 5 actually finish. New private facts, stopped-work retries, provenance changes or wider publication need the applicable separate decision; do not infer permission from a task label. The [execution list](todo.md) tracks these five checkpoints without duplicating roadmap milestones. Its delivery-receipt rule closes checkpoint 5 from the actual commit-bound workflow and exact readback, not from a recursively published checkbox; this plan is not an ongoing implementation queue.
