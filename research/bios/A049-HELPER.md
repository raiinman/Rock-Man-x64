# A0:49 follow-up: helper state and observation scope

## Why this matters to boot

The native diagnostic stops before fulfilling A0:49. [PSX-SPX's GPU page](https://psx-spx.consoledev.net/dev/ps1/kernelbios/gpu-functions/) describes that service as synchronizing before submitting a GPU command word. That is restricted-provenance research context, not permission to copy its implementation or fill unknown native device state. The original-game emulator captures already reach the opening story; the native port needs an accepted model of the required effects and continuation.

The [prior caller investigation](A049-CONSUMER.md) identifies the next callee and its first helper. This follow-up inspects the selected helper through its return, then the existing callee continuation through its first conditional branch and delay slot. No deeper branch path or further callee was followed.

## Static helper result

Conditional on ordinary nonfaulting execution of the inspected original-file code, the helper obtains a pointer P from an ordinary-RAM global, reads an unsigned 16-bit value through P, writes the incoming low halfword through P, and returns the old value. On this caller path the input is zero. This is an ordered read and write, not an atomic exchange or proof of successful hardware access.

The pointer global's **original-file initializer** is `0x1f801074`. [PSX-SPX's interrupt page](https://psx-spx.consoledev.net/interrupts/) identifies that address as I_MASK, with zero mask bits disabling the corresponding interrupt sources. This supports a conditional interrupt-mask interpretation. A mutable pointer's file initializer does not establish the value reaching a particular runtime access or physical-console behavior.

Across the inspected caller continuation, six-instruction callee prefix and seven-instruction helper, the incoming A0:49 `v0` has no explicit operand read before the helper's halfword load replaces it. That supports a bounded direct register-dataflow discard on this normal path. It does not prove absence of asynchronous/exception observation, service side effects, or a valid implementation policy. The GPU synchronization/submission obligations cannot be dropped because this register is overwritten.

## Where the helper result goes

The next inspected callee continuation stores the helper-returned value as a word in an ordinary-RAM global, then overwrites `v0`. It also clears one global word, loads it and copies that sampled value to another global. Intervening mutation and aliasing are not excluded, so the load is not unconditionally asserted to return zero.

The continuation selects its first branch using the saved argument's low three bits; the branch compares before its delay slot changes the `v0`. Both branch paths remain outside scope. This identifies a concrete saved-state consumer, not a full interrupt save/restore lifecycle or a minimum GPU completion contract.

## Evidence and provenance

The original executable identity was rechecked against the retained source receipt. Private header-mapped contextual slices retain complete digests; the selected helper covers seven instructions and the continuation twelve instructions. REA returned the complete 28-byte helper window and corroborated the halfword load/store and return. An independent SoL Medium reviewer checked selected instruction fields, MIPS-I delay ordering and the continuation's store/branch arithmetic. The reviewer verified slice identity, not the complete original executable digest.

This is original-game static reverse-engineering research with source/exposure and test-design lineage retained. Original bytes, disassembly, private paths and raw evidence are excluded from GitHub. Apply [provenance review](PROVENANCE-REVIEW.md) before implementation use. No native code was changed, no S2/initializer gate was enabled and no implementation clearance is claimed.

## Focused original-game observation

The owner requested investigating whether a game/BIOS run could resolve the missing state. An original register-only instrument joins a selected A0:49 caller, its return, callee entry, the helper's post-pointer-load register state, the delayed halfword result and callee resumption. It performs no observer memory/MMIO reads, guest writes or program injection. Its inputs are the retained hash-pinned BIOS, emulator and supplied disc, using a fresh profile and bounded output/screenshots.

The first new scope ended normally after 2,400 frames in 44.462234 seconds. It observed the declared game-entry callback at frame 1,094, but captured no selected A0:49/helper chain. Its final retained image shows a loading screen. The measurement therefore remains incomplete; the pointer and helper result were not obtained. This is neither evidence of a game crash nor proof that the request was absent. Instrument lifetime, callback aliasing and service behavior are not diagnosed as the cause.

The loading-screen endpoint justified one separately bounded extension, with its own exclusive retained lock: 7,200 frames and 150 seconds. Earlier successful profiles, the 2,400-frame result and all launch locks remain preserved. Runtime observations remain emulator evidence, not physical PS1 or native-game acceptance.


The extended scope also exited normally: 7,200 frames in 124.162397 seconds, 121 checkpoints and four screenshots. Its final image reaches the opening story. It again records only the declared-entry callback at frame 1,094, without the selected caller/helper chain. The strict occurrence join therefore remains incomplete; neither the helper's runtime pointer nor its result was measured. No callback-lifetime, alias, absent-request or game-service failure is inferred. Both attempts and their locks remain retained; no further automatic extension is selected.

The new instrument passed nine host-only controls and a separate prelaunch source review of each fixed scope. A later independent source audit found an existing closure-retention path, so an unrooted-breakpoint diagnosis was rejected rather than published as a fix. The actual measurement-coverage cause remains unresolved. New debugger work should establish callback coverage/selection before another target run, rather than borrowing the prior run's occurrence or rereading MMIO.

An independent retained-file audit verified the extended observer digest, receipt pin agreement, 121-checkpoint sequence, four raw image sizes, normal process exit, incomplete helper journal and both distinct lock files. It did not independently rehash the source media or inspect pixels; the author separately reviewed the converted final image. Private runtime reports and inputs are not independently reproducible from this public documentation repository.

## Observer callback contract correction

A subsequent host audit found a definite instrumentation defect against the [official PCSX-Redux breakpoint API](https://pcsx-redux.consoledev.net/Lua/breakpoints/): returning `false` removes that breakpoint permanently. The original wrapper returned that value even when a phase, selector or caller filter ignored an unrelated callback. Such an earlier hit can therefore prevent observation of the later selected occurrence under this documented contract.

The private observer now retains ignored watches and removes only a successfully completed one-shot stage, a stopped/closed observer or a failed handler. Seven new host-only controls execute the actual helper-observer Lua fragment under an API-contract mock, using the retained host Lua runtime without an emulator process or guest execution. They reproduce the old loss after an early A0 hit, wrong selector/caller and premature downstream hits; the corrected wrapper retains those watches and completes the synthetic joined sequence. Duplicate completed stages, removal of all seven completed watches, faults and stopped observers are checked. Together with the existing nine controls, all sixteen pass. Full generated-script/listener integration and terminal flushing are outside these new Lua controls. An independent SoL Medium reviewer confirmed the API interpretation and policy.

This establishes a code defect and host correction, not the measured cause of either game run: neither retained run contains callback counts proving an ignored earlier hit. Both incomplete results and their locks remain unchanged. No replacement capture or deeper runtime window was launched. The correction uses public debugger API documentation as a tooling input; original-game address selection and register expectations retain their separate source/test-design lineage. Native behavior and implementation clearance are unchanged.
