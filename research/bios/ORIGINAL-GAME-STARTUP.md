# Supplied original-game startup observations

The owner supplied a private two-track BIN/CUE image and authorized bounded original-game startup tracing. Container and ISO header inspection identify `SLUS_006.03;1`, with a 305,152-byte boot executable whose SHA-256 is `469670a017e9301ea6c7cd75cc5cfc1b919b839a62f73e69a979f8dafbe80cac`. This artifact must be matched to the native project's input before correlating state. Owner supply and a disc label do not establish implementation clearance.

## Retained startup windows

The first two captures used the pinned BIOS and emulator identified in the [BIOS baseline](BIOS-BOOT-BASELINE.md), fresh private profiles, interpreter/software rendering and the normal boot animation. The supplied CUE and both tracks were hash-checked before and after execution. Neither run injected an executable, loaded a saved state or patched the game.

The first window completed 900 vertical blanks in 17.8274 host seconds, exiting normally. Its final display shows the PlayStation licensed boot screen. The BIOS log had identified the boot executable, but the declared-entry breakpoint had not fired. Three pre-entry A0:49 callbacks were retained. This is not evidence of reaching game execution.

That observation motivated a separate extended window of 1,800 vertical blanks with a 45-second wall bound. It completed in 34.212538 seconds, exited normally and retained 31 ordered CPU checkpoints plus four display frames without observer errors. A breakpoint at the header-declared game entry fired at vertical blank 1094. Three A0:49 entry callbacks followed at vertical blank 1102. The final display visibly shows the game's **“now loading…”** screen.

The three post-entry records came from three registered address aliases with the same observed program counter and register values. They are not asserted to represent three unique service calls. Entry arguments and caller-state samples remain private. The observed location does not authenticate fetched opcode bytes, prove an effective dispatch target, establish a service return or supply the preceding GPU command stream.

Extended result metadata SHA-256: `992fd5809a5a74a8506772f92abe9fee457d8af191885f9cf12b76ee89b67480`. Original observer SHA-256: `13ea55d8ba6ca7a7b89163d1bdc33aeffe6043d747f840af322e2e2c233b4506`. Final converted display SHA-256: `fad53fec2098790db4a8588b48f199de481befefdbb0acde68ce0e825bc03cc6`. Raw captures, game files and display images are private. Screenshot channel interpretation remains as stated in the BIOS baseline.

## Next correlation boundary

The development coordinator has been sent artifact identity and a bounded post-entry observation summary. Delivery is distinct from acknowledgment. Match input, caller and native generation before selecting a dispatch/GPU producer follow-up; never replace missing native state with these sampled values. The existing owner-lifecycle source gate remains separate.

This establishes a concrete original-game observation for further research. It does not establish native Rock Man x64 boot, gameplay completion, physical-console equivalence or clean-room eligibility. Apply the [provenance review workflow](PROVENANCE-REVIEW.md); test design, behavioral oracle and implementation lineage remain separate review obligations.

## Past-loading capture and first-call detail

The owner subsequently authorized tracing beyond the loading screen. A third, separately identified cold-start profile bounds the run to 7,200 vertical blanks and 150 host seconds. It uses the same pinned original disc, BIOS and emulator, with no injected executable, game patch, saved state or input injection. Earlier profiles and launch receipts remain retained.

The new original observer selects only the first post-entry A0:49 occurrence. It samples one ordinary-RAM table word identified by retained BIOS static research, immediately arms a callback at that candidate target, and separately watches the entry caller's return address. Candidate and return callbacks check entry context; GPU callbacks record bounded access address/width/order with payload unknown. A slot snapshot and a matching target callback do not authenticate the dispatcher's actual load or fetched instruction bytes. A caller-return callback is a sampled boundary, not full ABI preservation or instruction-retirement proof.

The observer's design depends on restricted-provenance BIOS analysis, and the workbench provenance ledger now records that dependency. Public breakpoint API documentation guides instrumentation mechanics only. Neither an observed return nor agreement with a reference clears derivation, licenses an implementation handoff or enables the native controller.

The third capture completed 7,200 vertical blanks in 126.900721 seconds, exited normally and retained 121 ordered checkpoints and four display frames without reported observer errors. The final display shows an opening story sequence over the ocean with an aircraft: the original game progressed beyond the earlier loading image. This is not native-port boot or a completed game.

At the selected first post-entry occurrence, the sampled RAM word named the retained BIOS candidate; a callback at that address followed with matching entry context. Two GPU-status read callbacks and one GP0 write callback preceded a context-matched caller-return callback whose sampled return register was zero. Payloads remain unknown. Eight detail records include the terminal summary; no detail drops or context mismatches were reported. The later original-game A0:49 occurrence remains outside this first-call detail window. Its return-address sample is numerically eight bytes beyond the published native diagnostic stopping coordinate; this is a correlation lead pending exact input, caller and generation matching, not proof from fetched game instructions.

Result metadata SHA-256: `a9a34c6d399af6e241ee957cb776f8cce5bc6526b87fd5eade655f1e0368b961`. Observer SHA-256: `7cfdb48e5af2b7842fa45cdc46cd544b43089d9f2819d983228c80c2daefbea3`. Detail-journal SHA-256: `f309ed42b41744d75bc813d39dc868a3c47ce3fb80414263f9f76ac69a017556`. Final display SHA-256: `acc70c2cf8f4023f98a22d2e08f615441264deaf195c50744edf7e39679d00bb`. Captures and raw caller samples remain private; this documentation-only repository cannot reproduce the run independently.

## Caller-focused follow-up

The later occurrence justified a new fixed caller-focused observation within the owner's continued-tracing request. This fourth profile keeps the same 7,200-frame/150-second bounds and artifact pins, but selects the first post-entry A0:49 callback whose recorded return address matches the newly identified caller. It does not reuse the earlier call's return or GPU samples. The old first-call profile remains unchanged and independently readable.

The selection combines original-game callback evidence with a numerical correlation to the published native diagnostic coordinate. The provenance ledger records the native project attestation as a test-design dependency alongside the retained BIOS research. Matching a number does not establish an identical input, fetched call instruction or native generation. Source-derived findings remain held for review rather than entering game implementation automatically.

The caller-focused run completed 7,200 frames in 127.319572 seconds, exited normally and retained 121 checkpoints and four images with no reported observer errors. The final image again shows the opening story. At the selected occurrence, a candidate-target callback with matching context followed the RAM-slot snapshot. Two GPU-status read callbacks and one GP0 write callback preceded a context-matched caller-return callback with sampled return register zero. The second status-read callback occurred at a different firmware coordinate than in the earlier first-call window. This is an observation difference, not a reconstructed DMA/GP1 history: neither DMA-control nor GP1 writes were collected by this detail scope. A sampled scratch register at return is not a substitute for the unknown GPU read payload.

Eight detail records include the terminal summary, with no reported detail drops, context mismatches or saturation. The numeric caller match makes this a more focused research lead for DOT; exact native input/generation, actual dispatch load, full ABI, parser state, transferred payload and implementation acceptance remain open. No native code was changed.

Result metadata SHA-256: `edeacaf2090f0f7e6de763e01e3b656b78bebb856f14d83cc6d37f81899069a6`. Observer SHA-256: `8a616a2f83cab6213730021f958187d518682aceba5b659482ef9f6601d12403`. Detail-journal SHA-256: `38dc4f7ef6100fe7295114484118c764873b1c9908a65cc03103f7817d05369f`. Final display digest matches the separately retained third capture. Independent host validation checks the retained files; this public repository contains metadata and original prose only.

## Original-input and caller correlation

A later read-only ISO directory check distinguishes the disc's 305,152-byte boot executable from a separate 825,344-byte executable in the same image. SHA-256 over the latter's exact logical file bytes matches the original-input digest supplied in DOT's historical handoff. The earlier comparison used the boot executable's identity; those two artifact roles should not be treated as conflicting original inputs. This check inspected directory metadata and hashed bytes without extracting code, decoding instructions or launching another capture. It establishes contained-file identity against an attestation, not the bytes actually loaded at runtime.

Reconciliation of the retained handoff also finds explicit caller-return, stack-pointer and argument values that all match the later captured boundary. This is stronger than the earlier numerical eight-byte relationship alone. The native callsite and veneer remain project-attested; this research has not authenticated fetched game instructions or proved equivalent execution history.

| Match dimension | Result | Remaining boundary |
|---|---|---|
| Contained original executable | Size and SHA-256 match DOT's reported historical original input | Runtime loading and transformed memory remain unverified |
| Later A0:49 caller context | Three observed fields match the explicit historical attestation | Same dynamic occurrence and complete reaching state are not established |
| Native source and accepted receipt | Historical identities were supplied by the project | Current binary, owner generation and active pending request are not independently verified |

The new coordination question is a current-binding statement referring to the identities already supplied: whether the active build still uses that input and generation, and which pending request and immediate consumer are current. It does not ask for unavailable GPU history from the unchanged caller slice. The next implementation review should select an actual producer/consumer mismatch only after that binding and the project's provenance review. Observed zero returns do not authorize a successful no-op, readiness constants or controller enablement. No game code changed and no implementation clearance was granted.
