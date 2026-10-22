# The unresolved `0x1f801db8` boundary

The research requirement is to bind the observation at source `0x80079070` to its actual consumer and distinguish the selected native behavior from hardware semantics. The public project record attests that this instruction reads numeric address `0x1f801db8`, after the bounded CD configuration path. Its latest update reports that a newer connected native mixer passes this boundary under an explicit software policy. Neither this BIOS investigation nor the inspected vendor sources establishes the physical register's exact behavior.

## What is established

| Evidence class | Result | Limit |
|---|---|---|
| Project attestation | [Current status](../../docs/status/current-status.md), updated in commit `2013042`, distinguishes a Windows-verified configuration stage stopping at the sound read from a newer connected Linux mixer stage returning from `CdInit` with result 1 and stopping at `0x800779cc` | The private executable and reaching-state receipts were not inspected here; the mixer stage's freeze and Windows acceptance remain pending in that update |
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

The remaining question is precise: which bits of which observation does the actual game consumer require, under which reaching state? This batch narrows the firmware search and the handoff; it does not claim that the numeric mapping is solved.

## Current documentation completion boundary

The user's current priority is Sony's exact register definition. The [document search](SOUND-PRIMARY-SOURCES.md) now includes selective archived-disc access, vendor support discussions and a second patent. Each required claim still needs its own evidence:

| Claim about `0x1f801db8` | Status in inspected Sony material |
|---|---|
| Numeric address bound to a named register/channel | Unresolved |
| Register field width, signedness and encoding | Unresolved; an API output type is insufficient |
| Supported CPU access widths and read/write effects | Unresolved |
| Programmed setting versus evolving/current value | API/architecture distinction documented; numeric binding unresolved |
| Mode-dependent change, cadence and sweep arithmetic | Related modes and clocked circuitry documented; target-register rules unresolved |
| Reset state, limits, saturation and paired-read coherence | Unresolved |

Passing the explicit native adapter remains separate evidence. This documentation work cannot certify hardware equivalence from that pass.
