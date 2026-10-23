# Project history

**Coverage:** the original project request through the documentation pause on **2026-10-22 at 21:37:34 UTC**, with the already-running validation drain recorded at **21:39:13 UTC**. This is a retrospective reconstructed from retained project records, validation reports and the project conversation—not a contemporaneous public commit history.

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
