# Native service contracts and failure semantics

This specification summarizes the ownership rules behind the bounded native runtime. It distinguishes recovered source behavior from deliberately selected native policies. For the current checkpoint, see [status](../status/current-status.md).

## Session authority and knowledge

A production Session binds its source generation, RAM identity, immutable media allocation and actual service owners. Diagnostic or inherited-state sessions cannot mint production capabilities by setting public status fields. Reload and replacement must validate new input before publishing a generation; failed preparation preserves the old state. Old tokens cannot authorize work after a generation change.

RAM bytes and service observations carry known-bit masks. Unknown is not zero, idle, inactive or success. Only bits established by input, a recovered store or a genuine native operation become known. An opaque saved register can remain opaque when a path does not consume its value. Branches and service calls refuse when the required bits are unknown. Native stack state is distinct from logical source stack and register metadata.

Policies for independent cold start, heap layout, timers, device observations and CD configuration are named native product contracts. They do not establish original hardware reset state, exact BIOS allocation layout, physical timing or universal register behavior. Numeric source addresses identify adapter requests; they are not host MMIO accesses.

## Actual operations before success

A service result must correspond to work owned by the same Session. Heap initialization creates usable allocator state while preserving unknown payload bytes. Enabling an event does not create an occurrence. Installing a callback identity does not call it. Removing an ISO service revokes the actual capability and waits for owned work to drain; it does not merely flip a diagnostic label.

Likewise, a raw-media preflight verifies actual cursor positioning and reads against a retained immutable image. It is not itself a CD command response. Command admission, backend work, response publication, FIFO consumption, interrupt acknowledgement and source return are separate obligations.

## CD configuration

The frozen, Windows-verified reset/unmute stage requires the genuine immutable media owner, a fresh independent production Session and the preceding notification and IRQ-chain capabilities. Inherited, diagnostic, missing-image and unsupported reload/adoption paths cannot acquire that authority.

Reset `0A` reserves two response obligations before admission. Its first cause-3 response acknowledges acceptance from pre-reset authoritative status. Only after the actual first handler return does the scheduler prepare a separate reader against the same immutable allocation, reset its cursor, read first/middle/last sectors and probe EOF with a validation cursor. A successful atomic reader/configuration commit establishes native mute-request=true and prepares the cause-2 completion response. An ACK is not reset completion.

Unmute `0C` commits mute-request=false before its single cause-3 response. Neither operation proves decoding, playback, audio output, Track 2 support, DMA transfer or physical drive reset. Access/error history is retained rather than erased to make initialization appear clean.

Each operation binds owner, generation, RAM, media and revision identities. The fixed history has capacity for 16 operations; exhaustion must refuse before admission. Guarded capacity and reissue paths are not all dynamically established through supported connected source paths.

## Response and interrupt obligations

Unread or queued responses, unretired causes, active exceptions, router/successor debt, unknown ingress and incompatible work prevent new command admission. ACK retires the consumed phase only; it cannot discard reset's second same-operation response. Disabled or unknown permission retains work and never enables itself to make progress.

The IRQ chain captures a logical continuation separately from source-installed hook registers. Source RAM remains live; return does not restore an old RAM snapshot. Actual source frames, callback/consumer paths, FIFO reads, padding stores, result copying, acknowledgements and frame restoration must run in order. The return service restores the owned continuation exactly once, rather than falling through an ordinary function return.

New proven low-to-high arrivals have identities. A distinct arrival during active work remains successor debt; observing a still-high line does not invent another edge. Unsupported successors and nonzero user callbacks remain explicit barriers. Exception admission checks actual command phase, stack, return address and saved caller identity; an unknown or incorrect restored return address is not repaired by assumption.

For the configuration stage's normal path, four IRQ entries and returns, four FIFO reads, 28 source padding stores, 32 result-copy stores and 11 clock calls precede the final synchronizer result. These observations establish that bounded path, not a physical interrupt/timing model.

## Atomicity and allocation failure

Prepare capacity and validate all required identities before publishing a boundary. A pre-commit error must preserve its participants; after a real commit, response or reporting failure must retain the committed state and outstanding debt. Retrying must not replay completed source stores, backend reset, response consumption or IRQ return.

Atomicity is boundary-specific. A later unsupported source store must not erase earlier valid stores. Whole-function rollback would misrepresent source progress. Diagnostic allocation failure must also not turn a committed operation into one that appears never to have happened.

Allocation-denial tests repeatedly target recoverable boundaries, including failure immediately after reset commit/publication. They check ownership, preserved state and resumability, rather than merely checking that the process did not crash. They do not establish every possible future path.

## Connected native CPU software mixer

The connected implementation uses a synchronous software stereo processor with immutable applied coefficients and one authoritative CD configuration owner. Each bounded processing call captures the actual owner's committed mute configuration and the mixer's coefficient/control state under the same Session serialization guard. It records consumed revisions; it does not maintain a second mutable mute authority.

Current gain means coefficients actually installed in that software processor. Silence, muted input or lack of an endpoint cannot justify a fabricated zero current-gain reading. The connected numeric-port adapter exposes those software coefficients under an explicitly native policy; the hardware meaning of the relevant numeric addresses is not established by this implementation.

Staging matrix coefficients does not apply them. Apply validates all fields and publishes one complete revision. Source writes remain individual microcommits. Processing must validate buffers, knownness, owners and completion capacity before a no-throw output phase. Reload, reentrant mutation and stale borrowers must not create torn snapshots.

The sealed same-owner processor establishes functional readiness lazily after actual unmute and performs CPU PCM work under shared Session serialization. Connected Linux checks establish the genuine high-level initializer return, not merely a fabricated gain read. Freeze and Windows acceptance remain pending. There is no open output device, stream decoder, playback proof or physical SPU equivalence. Production reset-after-readiness coverage is still absent.

## Unsupported and recoverable outcomes

Failures should distinguish missing authority, stale generation, unknown required state, unsupported semantics, busy obligations, revision exhaustion and allocation failure. A recoverable retry retains exact continuation; an unsupported callback target remains captured even if a RAM pointer is later changed. No error becomes an invented successful firmware response.

Connected reset reissue, already-unmuted admission, history recovery, timeout cancellation, unmapped device errors, nonzero callbacks and unexpected successors remain bounded or unsupported. See the [handoff](../status/decisions-and-handoff.md) before extending them.
