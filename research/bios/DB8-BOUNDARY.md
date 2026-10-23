# `0x1f801db8`: source definitions and the native boundary

The research requirement is to bind the observation at source `0x80079070` to its actual consumer and distinguish the selected native behavior from hardware semantics. The public project record attests that this instruction reads numeric address `0x1f801db8`, after the bounded CD configuration path. Its latest update reports that a connected native mixer passes this boundary under an explicit software policy. Following the user-supplied README's documentation links establishes an explicit community-published numeric definition. The inspected Sony materials still do not supply that binding, and the game consumer remains uninspected here.

## Explicit definition reached through the README

The [PSX-SPX register section](https://psx-spx.consoledev.net/soundprocessingunitspu/#0x1f801db8-mvolxl-current-main-volume-left) identifies `0x1f801db8` as `MVOLXL`, current main volume left, and `0x1f801dba` as its right counterpart. Its grouped current-value field is 16 bits with signed range −32768 through 32767. The [original nocash specification](https://problemkaputt.de/psx-spx.htm) contains the same numeric/channel distinction. These related publications are community hardware documentation, not two independent measurements or Sony manuals.

This corrects the earlier broad unresolved wording: a published numeric definition is available; a Sony-authored definition and independently verified target behavior remain open. Setter state, current gain and output samples must remain distinct. The source section does not establish a universal reset constant, every CPU access width, direct-write behavior or paired-read atomicity. No new hardware experiment or MML1 execution was performed by this research.

The [pinned documentation source](https://github.com/psx-spx/psx-spx.github.io/blob/6d7d1bc106a7e0b616b0330fe58401ab1ba57f0f/docs/soundprocessingunitspu.md#L500) preserves the inspected definition. It already existed in the [initial 2020 conversion](https://github.com/psx-spx/psx-spx.github.io/blob/c602ea11a1d45526d57eb8598e5b22082674921e/soundprocessingunitspu.md#L422). The [later naming change](https://github.com/psx-spx/psx-spx.github.io/pull/118) cites SPU2 documentation for SPU names; that does not establish a Sony PS1 address citation. General credits and nearby hardware-test statements do not identify the evidence behind this particular mapping.

The original specification's boot-state example is explicitly emulator-observed and qualified as potentially different on hardware. It is not a power-on reset guarantee. Likewise, the nearby read/write paragraph concerns the voice-envelope register; it must not be assigned to DB8 merely because it precedes the current-volume headings.

### Following hardware-test claims to their corrections

The author of [PSX-SPX PR 198](https://github.com/psx-spx/psx-spx.github.io/pull/198) reports tracing voice-current volume on three consoles. Its timing conclusion was corrected in [PR 199](https://github.com/psx-spx/psx-spx.github.io/pull/199): the selected status-bit interval represented 512 samples rather than 256, invalidating the earlier doubled-rate inference. The later report must accompany any use of the earlier one.

Revision identity matters: the earlier definition was pinned to the repository's default `stable` branch at `6d7d1bc`. The two experimental reports were merged into the diverged `master` branch. Its separately inspected [SPU document at `038d444`](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/spu/soundprocessingunitspu.md#L539) retains the numeric definition; nearby timing text differs. These are separate recorded snapshots, rather than one interchangeable latest document.

These reports concern voice-current observation, not a demonstrated DB8/DBA experiment. The inspected descriptions do not identify console/chip models, reset phase or a raw measurement record. They therefore provide a useful experimental lead and correction history, without establishing master-current reset, writes, update timing or paired-read behavior. This research did not reproduce the reported tests.

The next useful measurement record would identify the machine, reset/boot phase, preceding master-control writes, actual DB8/DBA access widths and timing reference. Voice-current traces or rendered sound alone cannot supply those missing observations. This is an evidence request specification, not a test run or implementation change.

## What is established

### Original diagnostic probe executed in an emulator

The user subsequently authorized using the supplied BIOS with an emulator to run diagnostic tests. A portable PCSX-Redux Windows CLI build was obtained through its [official download route](https://github.com/grumpycoders/pcsx-redux#where); its [documented CLI](https://pcsx-redux.consoledev.net/cli_flags/) and [debugger API](https://pcsx-redux.consoledev.net/Lua/breakpoints/) were used. No emulator implementation source, SDK sample implementation or game code was inspected or used to construct the probe.

The executed build reports version `29142.20261022.44.x64`, changeset `afad8da748b38415a17a3080e027cf2f44983cfb`. It loaded the authorized 524288-byte BIOS identified by SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`, executed its kernel setup, then intercepted the shell to load an original standalone diagnostic executable. This is an emulator session with an explicitly loaded probe, not a retail reset measurement or MML1 boot. The original probe's SHA-256 is `a86f39e5312b9d6eb1ed6aa7dece51ba47c727ae93d56c77cd41210c693c195e`; its bytes, scripts and raw reports remain private.

The guest CPU performed halfword writes and unsigned halfword reads, recording raw control, configured left/right volume and current left/right volume into separate RAM records. A retained Lua completion breakpoint extracted those records; Lua did not substitute host values for guest SPU reads. Two completed runs each produced 56 records over seven phases:

| Probe phase | Controlled change | Observed current pair in this build |
|---|---|---|
| Initial post-load observation | No probe sound writes yet | Zero / zero |
| Direct master volume | Left/right settings `0x1234/0x2345`, control `0xc000` | Zero / zero |
| Direct mode, mute selected | Control changes to `0x8000` | Zero / zero |
| Direct mode, unmute selected | Control restored to `0xc000` | Zero / zero |
| Sweep controls | Seed settings `0x0400/0x0800`, delay, then `0x8028` for both sides | Zero / zero |
| Sweep controls, mute selected | Control changes to `0x8000` without rewriting volume settings | Zero / zero |
| Sweep controls, unmute selected | Control restored to `0xc000` | Zero / zero |

Each phase has eight observations separated by specified guest delay loops. Control and setter readbacks match all expected phase values. In the second run, debugger callbacks additionally counted 56 two-byte reads at each of DB8 and DBA, alongside 56 reads of each control/setter port. Expected writes were counted separately. An independent agent reviewed instruction encoding, load/branch delay slots, record bounds and completion checks; the coordinator checked the traced rerun. Neither review identified an obvious harness error.

The build used its interpreter CPU, software GPU and dummy audio driver. No voice playback, audible output or decoded-sample capture was tested. Mute transitions kept control bit 15 set; there was no SPU-disable phase. Guest delay-loop counts are not a calibrated physical sample clock, and sequential channel reads do not prove coherence. All-zero current values cannot distinguish an unimplemented readback, scheduling behavior or another model condition from these observations alone. No such implementation diagnosis is asserted.

This establishes harness execution and the selected emulator's observed answers. It does **not** establish that physical DB8 is zero during mute, that master updates freeze, that the configured direct value should be zero, or that the native adapter should return zero. Sony register-level documentation and original-machine measurements remain separate requirements. The emulator is a diagnostic tool here, not an implementation dependency of the native port.

#### Follow-up with separate progress observations

A separate original probe, SHA-256 `7f3ef2fbd6a7b7a7bf732673e815092692dd599b99edbbb7b57f74d83d7e4208`, used the same pinned CLI build and BIOS. Its 56 eleven-field records add RAM control, capture status, Timer2 count and masked status-change counts. It observes inherited RAM control first, then explicitly writes `0x0004`; Timer2 mode is written as `0x0200`, without a mode readback. These controls were selected from the separately pinned [SPU documentation](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/spu/soundprocessingunitspu.md) and [timer documentation](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/ps1/system/timers.md), not emulator implementation source.

Every phase contains both observed states of capture-status bit 11 and eight distinct Timer2 counts. Detected masked changes total 7, 6, 7, 6, 7, 6 and 7 across the seven phases. DB8/DBA remain zero in all records; debugger callbacks confirm 56 two-byte reads at each target. An independent review checked encoding, polling branch/load delays, record bounds, completion and digest agreement. A later workbench run completed the same diagnostic through its browser control.

These observations establish movement of emulated timer and capture-status values alongside unchanged current-volume reads. They do not establish audio generation, a master-volume clock, hardware cadence or the cause of the zeros. Status already changes in the inherited-RAM-control phase, so the write cannot be credited with starting progression. A first poll can detect a change since the preceding window; the counts are not exact edge timestamps or sample totals. No channel-coherence, DB8-write or physical-reset test was added.

The local workbench displays verified capture identity, phase-filtered observations and progress indicators, and launches the separately pinned graphical debugger. Code, raw captures, BIOS and runtime remain outside this documentation repository. Exported JSON is a capture summary rather than the complete private reproduction package.

| Evidence class | Result | Limit |
|---|---|---|
| Project attestation | [Current status](../../docs/status/current-status.md), updated in commit `a8b0380`, records accepted 69-case Windows mode validation and later bounded Linux graphics/diagnostic progress | Private game executable and reaching-state receipts were not inspected here; the current published stop is A0:49, and newer milestones remain owned by that status page |
| Community hardware documentation | The README leads to explicit numeric/channel and current-field definitions in PSX-SPX and its nocash ancestor | Shared ancestry is not independent corroboration; no Sony PS1 register citation or local measurement is established by reading them |
| Retained REA instructions | The selected firmware common getter reads other paired sound addresses, including `0x1f801d80/82` and `0x1f801db0/b2`; its recovered body does not read `db8/dba` | A different firmware component cannot identify the game leaf by a similar address or apparent library purpose; see [sound findings](SOUND.md) |
| Sony library documentation | Configured master volume, mode and current-volume observation are distinct API concepts | The inspected pages do not bind numeric `db8/dba`, establish this BIOS's API revision, or establish MML1's dependency; see the newly accessed 1996 and 1997 editions in [primary sources](SOUND-PRIMARY-SOURCES.md) |
| Native implementation attestation | The [service contract](../../docs/technical/native-service-contracts.md) reports a connected adapter exposing applied software coefficients, with staging and authoritative CD configuration kept separate | Passing the native source path does not establish physical register equivalence; no output device, decoder or playback is claimed |

## A wider firmware search

The earlier empty Ghidra xref results were supplemented with independent data-only instruction-field scans. These scans do not execute firmware and do not classify every word as code.

The decoded frontend contains 93,008 aligned little-endian words. A whole-image candidate scan found no load/store-shaped encoding with any selected immediate `0x01b8`, `0x01ba`, `0x1db8`, `0x1dba`, `0x0db8` or `0x0dba`. The first pair tests the known `0x1f801c00` base plus offset; the others test additional simple base constructions. Four exact words containing that known base match the pointer locations already documented by REA. Subject: 372032 bytes, SHA-256 `7920530e46981bab09bef02c72f35964bca25c879a72f3bf1c5313921143fbe7`.

A separate original-ROM scan covered 131,072 aligned words; a copied-kernel scan covered 8,956. Neither found a selected `0x01b8/01ba/1db8/1dba` memory-encoding candidate. The only additional `0x0db8/0dba` candidate in the ROM lies inside the known packed input stream, and is not evidence of an executed access. Original ROM: 524288 bytes, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`; copied kernel: 35824 bytes, SHA-256 `af3a156ada0cc06777f205ed47bcda257a53a798deca91610f426916147074b2`.

A further decoded-image candidate search starts at every aligned word, tracking selected constant arithmetic and in-image pointer loads for at most 96 instructions, through the first control-transfer delay slot. It recovered 76 distinct instruction/effective-address pairs in `0x1f801c00..0x1f801fff`, with none at `db8/dba`. These are candidate pairs, not executed transactions. Five synthetic checks cover pointer-load delay, old-register use during that delay, signed displacement, register-derived bases and a branch delay slot. Three positive address recoveries in the selected common getter agree with retained REA instruction evidence `ev_9fbb722e970956404c1d0b8528444ada48ed6e472dde077800480db577afefc1`.

This arithmetic search is a discovery heuristic, not a complete control-flow proof or CPU model. Unsupported special-instruction effects are incompletely represented; cross-block definitions, calls and mutable pointer contents are outside its proof. The positive checks validate selected mechanics, not complete R3000A semantics.

These are bounded negative results. They cannot exclude a separately adjusted base with a different final offset, indexing through registers, values passed across calls, mutable pointer state, aliases, unidentified mappings or code omitted from these subjects. The decoded mapping is nonlinear relative to ROM offsets and excludes the separately cleared RAM tail. Repeating an exact-address search would not resolve these limitations. Private scan scripts and receipts remain outside this public repository.

## The missing game evidence

The useful next artifact is a private, identity-bound backward and forward slice around the actual game read, with a sanitized summary suitable for this repository:

1. Bind executable identity, load mapping, containing leaf and caller chain. The firmware's `0x80079070`, if present, is a different subject.
2. Establish effective-address computation, byte/halfword/word width, signed or unsigned extension, destination and required known bits.
3. Follow the returned bits through masks, arithmetic, stores, comparisons and returns. Establish whether this is one observation, a paired read, or a loop that expects change.
4. Recover relevant preceding writes and selected mode, including any access to `0x1f801dba`. Distinguish requested settings from an actually applied value.
5. Bind the live Session, owner, generation, applied revision, reaching register state and remaining CD/IRQ obligations. Public status summaries alone do not supply these values.

No suitable game artifact or private slice is available to this investigation at this checkpoint. That is a concrete evidence boundary, not proof that the other computer lacks it.

## Consequences for a native adapter

These are research and acceptance proposals for assessing the attested native policy, not implementation changes or recovered hardware semantics:

- If the consumer needs an applied coefficient, observe the initialized native processor's authoritative applied state under the existing serialization contract. Staging a request does not apply it.
- If the consumer polls for change, define the actual native operation that advances the observed state and its ordering. A constant answer alone cannot establish progress or equivalence.
- If a signed or masked field is consumed, preserve that interpretation and known-bit requirement. Do not infer a scale or range from a similarly named later setter.
- Silence, a CD mute request, empty input and absence of a host endpoint do not establish a zero coefficient. Coefficient state and output samples are different quantities.
- A recoverable refusal must retain the actual continuation and committed CD/IRQ work. Successful adaptation must reach the genuine leaf, wrapper, callback-setter and initializer returns, stopping at the next unsupported boundary; it must not skip them.

Once the slice is established, useful acceptance cases include correct width/sign and masks; unknown or stale owner refusal; requested-versus-applied state; staged-state isolation; coherent repeated observations; refusal/resume without replay; and genuine source returns. Whether an endpoint, sweep model or time-dependent observation is necessary remains a question for the actual consumer.

Targeted [Sony mute documentation](SOUND-PRIMARY-SOURCES.md#distinct-mute-scopes-in-retained-41-manuals) distinguishes SPU mute from CD-stream mute. It supplies no DB8 invariant under either operation. The separate native observations above remain a validation proposal, rather than a newly established physical register rule.

## Additional primary architecture evidence

Sony's [US5978492A patent](https://patents.google.com/patent/US5978492A/en), filed December 1, 1995 and published November 2, 1999, describes per-voice volume controls, external PCM mixing, reverb and a downstream master-volume stage in the description of Figure 3. This supports a conceptual separation of gain stages from the samples passing through them. It does not identify `0x1f801db8`, prescribe its access width, or supply its reset, timing or sweep behavior. The patent is a primary architectural source hosted by Google Patents, not a register specification or a license determination.

The remaining game question is precise: which bits of which observation does the actual consumer require, under which reaching state? The community definition narrows this investigation; it does not supply that private slice or certify hardware equivalence.

## Current documentation completion boundary

The user's current priority is Sony's exact register definition. The [document search](SOUND-PRIMARY-SOURCES.md) and [archive coverage ledger](SONY-ARCHIVE-COVERAGE.md) include archived-disc access, wider PDF scans, vendor support discussions and patents. Each required claim still needs its own evidence:

| Claim about `0x1f801db8` | Status in inspected Sony material |
|---|---|
| Numeric address bound to a named register/channel | Unresolved |
| Register field width, signedness and encoding | Unresolved; an API output type is insufficient |
| Supported CPU access widths and read/write effects | Unresolved |
| Programmed setting versus evolving/current value | API/architecture distinction documented; numeric binding unresolved |
| Mode-dependent change, cadence and sweep arithmetic | Related modes and clocked circuitry documented; target-register rules unresolved |
| Value read during SPU mute or CD mute | Controls have distinct documented scopes; neither supplies a target readback invariant |
| Direct-setting visibility and progression during mute | No verified target latency, update phase, freeze or restart rule |
| Reset state, limits, saturation and paired-read coherence | Unresolved |

Passing the explicit native adapter remains separate evidence. This documentation work cannot certify hardware equivalence from that pass.

The user's diagnostic-disc lead now has [specific Sony tools, service-disc references and a proposed experiment matrix](SOUND-PRIMARY-SOURCES.md#sony-diagnostic-tools-and-the-proposed-register-experiment). Their documented setup/drive tests do not establish DB8 conformance. Useful further finds include a Sony PS1 SPU register specification, a CXD2922/CXD2925 programming manual, or an original-machine master-current test report with numeric readings around mute and identified timing. These are search targets, not verified document titles or a claim that a particular chip manual is publicly available. Searches can use `1F801DB8`, `MVOLXL`, `current main volume`, `master volume sweep`, `mute`, `ミュート` and `現在音量`; a voice-only result must retain that narrower scope.
