# Specification: native-runtime-control

## Assumptions and objective

[Shared specification](SPEC.md) applies. This is a **gated target, not an implemented API**. S2 remains NO-GO. Establish the necessary production lifecycle contract before permitting runtime load, stop, fault or ownership transitions through an IDE controller.

## Provider-owned interface and dependency

The retained [S2 decision](docs/status/decisions-and-handoff.md#s2-lifecycle-decision--october-23) and [current NO-GO](docs/status/current-status.md#ide-runtime-controller-source-only-feasibility-no-go) own the gate. Proposed integration depends on `native-startup`; it has no accepted callable signature here. The runtime provider must own termination, retirement and serialization semantics before a consumer can rely on them.

Data-only observation is not a controller interface. Last mailbox-handle destruction or delivery completion is not whole-owner retirement. No timer, timeout assumption or diagnostic UI state can supply missing lifecycle proof.

## Success and verification

Trace individually to `s2/load`, `s2/retirement`, `s2/stop`, `s2/integration` and `roadmap/live-controller`. The four necessary gates are not an exhaustive sufficiency proof. An eventual authorized slice needs an agreed contract, real provider/consumer integration, interruption/retry/fault/shutdown tests, relevant regression and independent review. Pure source review, synthetic mailboxes and public tests do not close these gates.

## Blocking questions and limits

Bounded loading cancellation/termination, whole-owner retirement, single-call stop/fault semantics and real endpoint/worker finalization remain unresolved. No implementation, new harness, execution or disabled-control enablement is commissioned by this specification. Verify private APIs/full commands only after a concrete permitted slice exists; do not fabricate them to make this page look implementation-ready.
