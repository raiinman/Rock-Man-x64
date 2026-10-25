# Project history

**Coverage:** the initial project record through the documentation pause on **2026-10-22 at 21:37:34 UTC**, the already-running validation drain at **21:39:13 UTC**, and the later dated resumed-development checkpoints below. This is a retrospective reconstructed from retained project records, validation reports and the project conversation—not a contemporaneous public commit history. For the latest reviewed project summary and coordination, use the [living tracker](../status/dashboard.md) and [dated handoff](../status/decisions-and-handoff.md).

- [Chronological milestone ledger](milestones.md): the work from source acquisition to the latest candidate.
- [Decisions, failures and recoveries](decisions-and-recoveries.md): what changed, what failed, and what remains unresolved.
- [Evidence and validation history](validation-history.md): what each type of evidence actually establishes.

## The starting goal

Independently reconstruct the original PlayStation **Mega Man Legends** as a fully native Windows game with an integrated IDE. After an initial platform/project comparison, the project rule became not to reuse existing ports, mods, recompilation implementations or game-specific reverse-engineering projects. General technical documentation and ordinary development toolchains are distinct from those prohibited game implementations.

The initial comparison examined public descriptions/documentation of existing projects before the no-reuse direction; none was adopted as the implementation foundation. “Independent reconstruction” describes the working approach. The supplied original binary is analyzed directly; a formal legally separated clean-room process has **not** been established or certified.

## The stopping point at the documentation pause

The last frozen, actual-Windows-validated runtime stage is **native IRQ chain**: 88 regression tests and 29 Windows contract cases (22 successful exit-0 cases and seven intentional exit-1 refusals). The first status command completes through the translated handler, logical interrupt return and original wait. It stops before reset command `0A`.

The newer **CD configuration candidate is unfrozen**. Its supported path goes through reset `0A` acknowledgment and completion, then unmute `0C`, with four IRQ returns and 11 logical clock calls. It stops at an unsupported sound-register read. Its isolated validation was not accepted at the pause; the already-running aggregate subsequently drained with two fixture-related failures and acceptance still false. It is **not** a new Windows-validated release.

There is still no native game boot, playable scene, complete integrated IDE or audio playback claim. The public repository documents research and progress; it does not distribute the private game inputs or a playable game.

## Reading dates correctly

Most saved milestones are dated **2026-10-22**, without trustworthy per-milestone completion times. Their sequence below follows dependencies and explicit records. Workstreams overlapped, so ordered milestones are not a minute-by-minute schedule. Exact times are used only where a record or conversation explicitly supplies them. File modification times are not treated as proof of completion.

Private implementation documents sometimes retain historical statements such as “Windows execution unverified” or “no public repository authorized.” These were correct boundaries when written, not the final state: later actual Windows reports and the explicit documentation-publication request supersede them. Private originals and derived assets remain excluded.

## Later resumed-development checkpoint

Development resumed at 22:04 UTC. The configuration stage subsequently passed 40 Windows cases. The later native CPU mixer was sealed and passed 51 actual Windows cases, with a preserved stale-summary metadata defect. The later mode-00 stage passed all 69 actual Windows cases after its Linux recovery and contract checks. Failed synthetic Windows supervisor attempts remain recorded separately. Newer graphics entry and diagnostic continuations have Linux-only evidence and still stop at an unsupported service; see current status for their acceptance limits. See [validation history](validation-history.md) for the preserved failures, correction and evidence limits, and [current status](../status/current-status.md) for the latest checkpoint.

The later 03:05 update records 50 Windows IDE command checks, visual QA blocked before launch, and combined 16-stage/69-case Linux validation with separate connected/allocation gates still pending. Snapshot DTO review is not capture acceptance.

The 04:05 update closes all four combined Linux phases and records separately accepted bounded actual capture. Exporter/frozen-viewer v1 race findings remain visible while v2 corrections have source/synthetic acceptance; no actual exporter or Windows viewer acceptance is implied.

The 05:05 update adds bounded actual portable export/import, retained Windows-validator preparation failures and a corrected offline validator. The native frozen-viewer run failed bounded file load after 36 passes, with 74 unrun; new original-loader findings are static evidence, not execution or hardware proof.

The 06:09 update records the unchanged reader's context-dependent diagnostic and a separately approved frozen-viewer 111-check pass. Earlier failure remains preserved; acceptance is synthetic HWND/command/state only. Conditional loader range review does not establish actual firmware dispatch or GPU history.

The 07:07 update adds one accepted native loader-prefix original-input compatibility run stopping at A0:39, preserves the rejected first cleanup envelope and separately reviewed v2 recovery, and records 23 Windows standalone host-function lifecycle checks. Visual/real-launcher/actual-capture acceptance and transfer-route reuse remain gated; no firmware or game-boot claim follows.

The 08:05 update records separate native-policy heap and continuation compatibility acceptances, stopping before the initializer with BIOS effects unresolved. It preserves the rejected lineage-binding candidate and reviewed v2 correction. The later initializer prefix is source/synthetic accepted only; execution preparation is blocked pending review without a retry or alternative route.

The 09:05 update adds a research-provenance checkpoint: author-reported static A0:39 effects differ from the accepted RAM-preserving native policy. It records no new execution or equivalence; the initializer execution-preparation blocker and all earlier failed stages remain unchanged.

The later October 23 S2 feasibility review concluded source-only NO-GO for the planned production IRQ/graphics runtime controller. Missing loading/retirement and worker-lifecycle contracts were identified without code changes or tests; earlier viewer results and the separate initializer blocker remain unchanged.

The subsequent isolated observation mailbox passed 12 synthetic scenarios in three instrumentation modes, with two additional independent coverage dimensions. LeakSanitizer environment failures remain preserved. This is data-channel acceptance only, not S2 readiness, native-owner retirement or Windows integration.

The later October 23 observer candidate adds ten synthetic scenarios on top of the unchanged twelve mailbox scenarios, with three partially overlapping independent reviewer scenarios. Linux instrumentation repeats are not unique tests. The initial test-build failure was corrected without warning suppression; LeakSanitizer was not run. This remains data-only observer acceptance, not production S2, Windows UI or native game boot. See [milestone 32](milestones.md#32-data-only-observer-acceptance--october-23).
