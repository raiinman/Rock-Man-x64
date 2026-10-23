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

| Evidence class | Result | Limit |
|---|---|---|
| Project attestation | [Current status](../../docs/status/current-status.md), updated in commit `69afad7`, records the sealed, Windows-validated mixer stage and a later unsealed mode-00 candidate | Private executable and reaching-state receipts were not inspected here; newer project milestones remain owned by that status page |
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
| Reset state, limits, saturation and paired-read coherence | Unresolved |

Passing the explicit native adapter remains separate evidence. This documentation work cannot certify hardware equivalence from that pass.
