# Native completion ownership candidate

A private, original generic C++17 gate now implements owner-scoped submission and continuation ownership. It is a concrete candidate toward the native A0:49 boundary, not an implementation of the service or its GPU effects. No game code was changed or original-input native execution performed.

## What was built

Each submission carries an opaque gate-instance identity, owner, generation, request and monotonic submission identity. Stale, foreign or duplicate terminal deliveries cannot replace the current submission. A cancellation request is separate from a terminal result. A successful but unclaimed result remains an outstanding continuation obligation; it cannot be silently replaced by another submission, a generation reset or local retirement.

A continuation can be claimed once and must be explicitly finished. Cancellation can suppress an unclaimed successful continuation; it cannot settle already claimed work. Finite identity counters refuse exhaustion rather than wrap. Operations serialize their state transitions without calling external code while locked.

These are local mechanism properties. Submission admission does not mean GPU acceptance. Terminal settlement trusts the caller's assertion; the gate cannot establish the event's truth, GPU completion, parser state or effects. Local retirement covers only the modeled obligation, not worker, resource, message or whole-owner retirement. The caller must preserve object lifetime.

## Windows synthetic validation

Private inputs and implementation are excluded from this documentation repository, so these results are reported evidence rather than publicly reproducible tests.

| Step | Reported result | Meaning |
|---|---|---|
| Initial setup | Warnings-as-errors rejected unused stub fields; corrected before behavioral testing | Build setup failure, not a behavioral red test |
| Initial behavioral red | Clean build; 74 checks, 71 failures | Assertions exercised the unimplemented contract |
| First implementation slice | Admission subset 41 checks, zero failures; incomplete full suite still failed | Partial result retained rather than described as complete |
| New outstanding-success obligation | 42 checks, three failures before correction | A later successful settlement could not be silently discarded |
| Complete debug build | 442 checks, zero failures | Actual Windows host execution with synthetic requests |
| Release/NDEBUG build | 445 checks, zero failures | Same header/tests, optimized configuration; custom checks remain enabled |

The final suites include duplicate/stale/foreign tokens, reused request identifiers, exhaustion, cancellation, reset/retirement, unfinished continuations and bounded concurrent races. Assertion totals vary with legal race branches and must not be summed as unique test cases. Finite exercised interleavings are not exhaustive concurrency proof; no sanitizer result is claimed.

A separate constrained reviewer inspected the implementation and test contract and found no material state-machine bug. The reviewer did not execute it. A minor documentation overstatement about terminal-delivery return classifications was corrected without changing the tested header or tests.

## Native integration seam still required

| Native binding | Candidate contribution | Still needed from native development |
|---|---|---|
| Pending service owner | Rejects another instance/generation/submission | Actual native owner, lifetime and request-to-token mapping |
| GPU submission | Admits one modeled outstanding request | Real submission producer and its failure/acceptance contract |
| GPU terminal delivery | Rejects stale or duplicate token delivery | Genuine completion/failure producer, ordering and synchronization; a trusted assertion alone is insufficient |
| Continuation | One claim plus explicit finish | Actual consumer, required effects and the point at which its owned work is finished |
| Cancellation/retirement | Preserves modeled outstanding obligations | Whole-owner resources, worker/message ownership and existing S2 decisions |

The next concrete integration task is a minimal source/API adapter review for those bindings. Do not inject observed game return values, fabricate a GPU-ready result, release resources on cancellation intent, or enable the initializer/S2 path. No active native binding or completion producer has been supplied here.

## Delivery and provenance

An inert source-only candidate with its input/review records was delivered privately through the established relay. Seven files passed normalized text readback comparison; this is not a remote raw-byte digest audit, recipient acknowledgment, compilation or installation. No executable or toolchain was transferred.

Author and independent reviewer received a generic ownership brief in fresh sessions, with their read histories retained. PS1 addresses, original game/BIOS observations, PSX-SPX, SDK and emulator/decompilation implementation were excluded from those constrained inputs. The parent research agent's prior exposure and brief authorship remain recorded. This separation does not automatically establish independent derivation, clean-room eligibility or permitted implementation use. Integration still requires the agreed input/consumer and provenance review in [PROVENANCE-REVIEW.md](PROVENANCE-REVIEW.md).

The development process used the pinned [incremental implementation workflow](https://github.com/raiinman/skill-library/blob/594499cb9a842822580d847d85abdf832814c27c/skills/coding-workflow/incremental-implementation/SKILL.md), including real red/green slices and recorded failures. This is process attribution, not a device specification or implementation clearance.

See [DOT's concrete handoff](../../DOT.md#generic-owner-completion-candidate-ready) and the [native research handoff](NATIVE-HANDOFF.md). Native GPU semantics, actual consumer binding, Windows game boot and clean-room acceptance remain open.
