# Supplied original-game startup observations

The owner supplied a private two-track BIN/CUE image and authorized bounded original-game startup tracing. Container and ISO header inspection identify `SLUS_006.03;1`, with a 305,152-byte boot executable whose SHA-256 is `469670a017e9301ea6c7cd75cc5cfc1b919b839a62f73e69a979f8dafbe80cac`. This artifact must be matched to the native project's input before correlating state. Owner supply and a disc label do not establish implementation clearance.

## Two distinct startup windows

Both captures used the pinned BIOS and emulator identified in the [BIOS baseline](BIOS-BOOT-BASELINE.md), fresh private profiles, interpreter/software rendering and the normal boot animation. The supplied CUE and both tracks were hash-checked before and after execution. Neither run injected an executable, loaded a saved state or patched the game.

The first window completed 900 vertical blanks in 17.8274 host seconds, exiting normally. Its final display shows the PlayStation licensed boot screen. The BIOS log had identified the boot executable, but the declared-entry breakpoint had not fired. Three pre-entry A0:49 callbacks were retained. This is not evidence of reaching game execution.

That observation motivated a separate extended window of 1,800 vertical blanks with a 45-second wall bound. It completed in 34.212538 seconds, exited normally and retained 31 ordered CPU checkpoints plus four display frames without observer errors. A breakpoint at the header-declared game entry fired at vertical blank 1094. Three A0:49 entry callbacks followed at vertical blank 1102. The final display visibly shows the game's **“now loading…”** screen.

The three post-entry records came from three registered address aliases with the same observed program counter and register values. They are not asserted to represent three unique service calls. Entry arguments and caller-state samples remain private. The observed location does not authenticate fetched opcode bytes, prove an effective dispatch target, establish a service return or supply the preceding GPU command stream.

Extended result metadata SHA-256: `992fd5809a5a74a8506772f92abe9fee457d8af191885f9cf12b76ee89b67480`. Original observer SHA-256: `13ea55d8ba6ca7a7b89163d1bdc33aeffe6043d747f840af322e2e2c233b4506`. Final converted display SHA-256: `fad53fec2098790db4a8588b48f199de481befefdbb0acde68ce0e825bc03cc6`. Raw captures, game files and display images are private. Screenshot channel interpretation remains as stated in the BIOS baseline.

## Next correlation boundary

The development coordinator has been sent artifact identity and a bounded post-entry observation summary. Delivery is distinct from acknowledgment. Match input, caller and native generation before selecting a dispatch/GPU producer follow-up; never replace missing native state with these sampled values. The existing owner-lifecycle source gate remains separate.

This establishes a concrete original-game observation for further research. It does not establish native Rock Man x64 boot, gameplay completion, physical-console equivalence or clean-room eligibility. Apply the [provenance review workflow](PROVENANCE-REVIEW.md); test design, behavioral oracle and implementation lineage remain separate review obligations.
