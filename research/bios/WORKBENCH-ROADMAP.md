# PS1 workbench requirements and implementation status

This original research-team proposal has 87 detailed requirements across 15 domains. It was sent for development-agent prioritization; a new comprehensive DOT response has not been received. No item is presented as DOT-selected. The [capability report](WORKBENCH.md) records the implemented tools and their verification limits.

Status concerns the private research application only: **implemented** means the described bounded workbench path exists and has host/browser checks within its stated scope; **waiting input** requires identified evidence or an agreed integration contract; **proposed** is unimplemented. None means native boot, hardware conformance, S2 acceptance or execution authority.

Current totals: 45 implemented, 10 waiting for input and 32 proposed. P0 targets the current evidence and collaboration gaps; P1 supports nearby investigations; P2 covers later PS1 reuse. The broad CPU/GPU/IRQ/CD/SPU worksheets remain proposed unless the row describes a narrower existing decoder or report view.

## Evidence intake

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| intake-01 | P0 | Bound JSON size, depth and item counts | implemented | Reject oversized or deeply nested documents without changing saved work. |
| intake-02 | P0 | Reject duplicate and unsafe object keys | implemented | Reject repeated keys, including escaped duplicates and prototype-related keys. |
| intake-03 | P0 | Preview exact editor-text digest | implemented | Label SHA-256 as the editor text identity, never source authentication. |
| intake-04 | P0 | Keep imports local to the browser | implemented | File selection must cause no upload or execution. |
| intake-05 | P0 | Persist named private evidence cases | implemented | Reload preserves saved cases and duplicate names never overwrite them. |
| intake-06 | P0 | Agree the native DOT interchange schema | waiting input | DOT identifies schema, artifact generation, observation roles and refusal cases. |
| intake-07 | P0 | Verify externally supplied manifests | proposed | Distinguish digest consistency, source authenticity and calibration applicability. |

## Dispatch and producer provenance

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| producer-01 | P0 | Trace explicit value and address dependencies | implemented | An unknown loaded value cannot inherit the known address or base value. |
| producer-02 | P0 | Find the first missing producer | implemented | Return missing dependencies reachable from the selected consumer. |
| producer-03 | P0 | Reject cyclic or dangling relations | implemented | Bad edges cannot create a resolved dependency chain. |
| producer-04 | P0 | Preserve artifact and occurrence boundaries | implemented | Cross-identity facts require explicit justified relations. |
| producer-05 | P0 | Separate original templates from effective dispatch | implemented | An initial table binding cannot become observed game-time dispatch. |
| producer-06 | P0 | Compare overlapping known bits | implemented | Contradictions use common known bits; unknown differences are not conflicts. |
| producer-07 | P0 | Bind fetched-code evidence separately | waiting input | DOT supplies a new bounded route and instruction-fetch provenance if needed. |

## Owner and operation lifecycle

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| lifecycle-01 | P0 | Review an ordered operation ledger | implemented | Completion must bind the admitted operation and generation. |
| lifecycle-02 | P0 | Distinguish cancellation request from completion | implemented | A cancellation request retains outstanding load obligations. |
| lifecycle-03 | P0 | Account for callbacks and messages | implemented | Worker exit cannot discard remaining token debts. |
| lifecycle-04 | P0 | Check one-call stop and fault paths | implemented | Duplicate stop admission and unknown outcomes stay visible. |
| lifecycle-05 | P0 | Flag stale and duplicate notice consumption | implemented | Wrong-generation delivery cannot discharge an owner obligation. |
| lifecycle-06 | P0 | Keep S2 source contracts independent | implemented | Even favorable declarations keep production controls disabled. |
| lifecycle-07 | P0 | Review the actual whole-owner transition | waiting input | DOT supplies the identified source transition and pending-obligation policy. |

## Trace comparison

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| compare-01 | P0 | Gate comparisons by declared identities | implemented | Different fixture, instrument or unknown identity blocks equivalence claims. |
| compare-02 | P0 | Preserve partial-known-value differences | implemented | Compare only intersecting known bits and retain unknown remainder. |
| compare-03 | P0 | Show ordinal-aligned differences | implemented | Explicitly label positional matching as descriptive, not execution equivalence. |
| compare-04 | P0 | Project retained observations into a common trace | implemented | Keep access-only callbacks value-free and label projection limits. |
| compare-05 | P0 | Align explicit anchors and repeated loops | proposed | Report ambiguous alignments instead of choosing a hidden best match. |
| compare-06 | P0 | Display bounded side-by-side timelines | proposed | Unmatched events and truncated prefixes remain visible. |

## Memory and write provenance

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| memory-01 | P1 | Resolve declared address expressions modulo 32 bits | implemented | U plus offset is a computed address, never the loaded R. |
| memory-02 | P1 | Inspect known bytes and masks | implemented | Unknown bytes cannot become zero-filled memory. |
| memory-03 | P1 | Check stores against dispatch watch ranges | implemented | Detect partial-width overlap and wrap at the address-space boundary. |
| memory-04 | P1 | Keep conditional and observed effects separate | implemented | Unknown conditions produce candidates, not observed memory. |
| memory-05 | P1 | Make segment alias assumptions explicit | implemented | Physical-segment arithmetic does not imply cache coherence or RAM mirrors. |
| memory-06 | P1 | Detect conflicting before/after claims | implemented | Order, source and common masks accompany every contradiction. |
| memory-07 | P1 | Import a new loader producer cut | waiting input | DOT supplies return-relative arithmetic, loaded-value provenance and path conditions. |

## CPU and static MIPS lens

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| cpu-01 | P1 | Decode a documented instruction subset | implemented | Unsupported operations stop dependent reasoning instead of being treated as NOP. |
| cpu-02 | P1 | Display register definitions and uses | implemented | Loads remain symbolic unless identified memory evidence is supplied. |
| cpu-03 | P1 | Annotate load delays and branch delays | implemented | Separate source instruction order from observed retirement. |
| cpu-04 | P1 | Compute branch and jump targets statically | implemented | Use explicit PC mapping and preserve delay-slot conditions. |
| cpu-05 | P1 | Mark conservative call clobbers | proposed | A callee summary must identify its artifact and scope. |
| cpu-06 | P1 | Track signedness and overflow assumptions | proposed | Unsigned modulo arithmetic cannot certify signed exception behavior. |

## GPU command and state history

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| gpu-01 | P1 | Decode selected GPU status known bits | implemented | Unknown bits remain unknown and field labels cite primary project documentation. |
| gpu-02 | P1 | Inspect supplied GP0 packet boundaries | proposed | Truncated packets and unknown parser origin block command classification. |
| gpu-03 | P1 | Track ordered GP1 state producers | waiting input | Start from the last justified origin; later reset cannot fill earlier state. |
| gpu-04 | P1 | Review FIFO, parser and pending work separately | proposed | A ready bit cannot stand for all completion obligations. |
| gpu-05 | P1 | Track VRAM transfer ranges and ownership | proposed | Supplied payload provenance must remain separate from access callbacks. |
| gpu-06 | P1 | Compare display and drawing state | proposed | Register snapshots do not establish presented pixels. |
| gpu-07 | P1 | Inspect ordering-table and draw-command evidence | proposed | Unknown linked-list pointers stop traversal under byte/event bounds. |

## DMA and synchronization

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| dma-01 | P1 | Decode channel control known bits | implemented | Mode-dependent fields remain labeled and partial masks remain unknown. |
| dma-02 | P1 | Review selected A0:49 branch evidence | implemented | Target identity and source order gate the no-DMA and DMA mask checks. |
| dma-03 | P1 | Review block and linked-list transfer descriptions | proposed | Ranges, direction, alignment and truncation are explicit. |
| dma-04 | P1 | Separate IRQ, busy-clear and consumer completion | proposed | No one signal silently discharges unrelated transfer debt. |
| dma-05 | P1 | Add DMA and returning-timeout evidence cases | waiting input | Requires a new identified scope; the completed no-DMA fixture is not rerun. |

## Interrupts, events and continuations

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| irq-01 | P2 | View event allocation, enable and delivery independently | proposed | Enabling an event cannot manufacture an occurrence. |
| irq-02 | P2 | Track registration mutations and owner generations | proposed | Stale callbacks retain their source and disposition. |
| irq-03 | P2 | Review IRQ entry, acknowledgement and return | proposed | One observed edge cannot establish nested ordering. |
| irq-04 | P2 | Compare logical continuations and host scheduling | proposed | Host-thread success cannot certify guest continuation effects. |
| irq-05 | P2 | Review reentrancy and critical-section assumptions | proposed | Missing interleavings remain coverage gaps. |

## CD and media service lifecycle

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| cd-01 | P2 | Track command admission and response phases | proposed | Command acceptance is not transfer completion. |
| cd-02 | P2 | Keep response, IRQ debt and notification separate | proposed | Unread response and pending acknowledgement remain owned. |
| cd-03 | P2 | Compare current, saved and recovery state | proposed | A history reset cannot replay an earlier effect. |
| cd-04 | P2 | Review sector and buffer ownership evidence | proposed | No disc or asset bytes are imported automatically. |
| cd-05 | P2 | Bind native media outcomes to the reached consumer | waiting input | Requires a new identified caller and private schema. |

## SPU and sound investigation

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| spu-01 | P2 | Inspect retained current-volume observations | implemented | No physical update cadence or mute semantics inferred from emulator samples. |
| spu-02 | P2 | Decode selected SPU control fields | implemented | Width, masks and documentation provenance stay visible. |
| spu-03 | P2 | Review voice and sample producer histories | proposed | Unknown sample state cannot become silent audio evidence. |
| spu-04 | P2 | Track configured, current and output volume separately | proposed | A getter or setting API does not prove numeric hardware binding. |
| spu-05 | P2 | Join the actual DB8 consumer | waiting input | Requires identified game read, interpretation and subsequent use. |

## Services, ABI and heap effects

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| abi-01 | P1 | Track caller arguments and result consumers | proposed | Ignoring a result does not erase required side effects. |
| abi-02 | P1 | Review register and memory preservation | proposed | Leaf-only evidence cannot certify the entire dispatch route. |
| abi-03 | P1 | Display selected heap static effects | implemented | Original report remains distinct from accepted native allocator policy. |
| abi-04 | P1 | Record exceptional and partial completion | proposed | A fault may preserve only a prefix of ordered effects. |
| abi-05 | P1 | Bind formatter and backend helpers | waiting input | Requires a precise new static question, not an unchanged broad scan. |

## Controller and memory-card evidence

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| input-01 | P2 | Track serial transaction stages | proposed | Handshake assumptions and actual supplied bytes remain scoped. |
| input-02 | P2 | Review controller-buffer ownership | proposed | A buffer registration is not a completed physical input transaction. |
| input-03 | P2 | Inspect save staging and commit boundaries | proposed | Failed persistence must preserve the previous accepted save. |
| input-04 | P2 | Review hotplug and stale generation effects | proposed | Generation replacement cannot hide pending operations. |

## Diagnostics and collaboration

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| plans-01 | P0 | Export bounded non-executable plans | implemented | Time/event/watch limits never authorize target execution. |
| plans-02 | P0 | Generate a request from selected analysis gaps | implemented | The question cites exact input digest and unresolved obligation. |
| plans-03 | P0 | Expose requirement source and status | implemented | Research proposals must not be labeled DOT-selected. |
| plans-04 | P0 | Accept DOT priorities by requirement ID | waiting input | A new acknowledged reply selects concrete inputs and acceptance checks. |
| plans-05 | P0 | Preserve immutable private correspondence | implemented | Delivery, acknowledgment and reviewed evidence stay separate. |
| plans-06 | P0 | Export reviewed public prose separately | proposed | Raw payloads, private paths and source words remain excluded. |

## Recovery and verification

| ID | Priority | Requirement | Status | Acceptance boundary |
|---|---|---|---|---|
| recovery-01 | P1 | Restore server on demand after reboot | implemented | The desktop launcher checks the versioned local endpoint. |
| recovery-02 | P1 | Retain notebook revision conflicts | implemented | A stale tab cannot overwrite newer saved notes. |
| recovery-03 | P1 | Provide bounded browser-local case export | implemented | Storage refusal preserves previous saved data. |
| recovery-04 | P1 | Verify host contracts without target launches | implemented | Tests cover invalid inputs and preserve launch locks. |
| recovery-05 | P1 | Exercise a wider browser and viewport matrix | proposed | Record exact observed environments instead of claiming universal UI acceptance. |

## Next concrete integration decision

Request a new identified original-loader producer summary or owner transition scope. For the A0:49 investigation, conditional address arithmetic does not supply the loaded pointer, subsequent writes, effective dispatch or GPU parser state. For S2, a consistent observation-channel ledger cannot supply native cancellation/completion or whole-owner retirement contracts. Select one bounded question and matching input before specializing an adapter or diagnostic; preserve completed recorder launch locks and the separate initializer block.

The four implemented CPU rows describe the bounded static instruction lens only; propagation, execution, full call summaries and broader CPU conformance remain outside that subset. Additional BIOS startup, full-text reference and provenance-review capabilities are described in WORKBENCH.md; this original 87-row proposal is not an exhaustive inventory.
