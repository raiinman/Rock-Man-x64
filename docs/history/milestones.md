# Chronological milestone ledger

All entries belong to the project history available on **2026-10-22**. Unless an exact UTC time appears, an entry is sequence/date-only. Related research and validation proceeded in parallel.

## 0. Initial comparison and explicit change of direction

At **14:07:37 UTC**, the user requested a version comparison. The **14:12:26 UTC** response compared PS1, N64, Windows, PSP and modern fan projects using public descriptions/documentation; it was not a performance benchmark. At **14:17:31 UTC**, an existing N64 recompilation was briefly recommended as a possible foundation. The user rejected that direction at **14:17:58 UTC**. The native Windows plus integrated IDE goal was explicit at **14:18:57 UTC**, followed by the independent PS1 direction at **14:19:26 UTC**. No existing project implementation was adopted. The honest scope claim is no reuse in the subsequent reconstruction, not that outside projects were never examined.

## 1. Scope and private source acquisition

The settled target was the original PS1 game rebuilt as native Windows software with an integrated IDE, not an emulator wrapper. Existing ports and mods were explicitly excluded. The original game source material was supplied privately; original disc bytes were preserved unchanged and treated as read-only input, with editable work kept separate.

The PS1 source commitment was recorded at **14:23:10 UTC**, archive upload reported at **14:27:15 UTC**, and private source access supplied at **14:28:53 UTC**. Download/integrity success was reported at **14:31:13 UTC**. The supplied archive passed member CRC checks and safe extraction. Track 1 contains 207,145 raw sectors; Track 2 is a separate audio track. Disc inventory found 247 files. Executable headers identified the boot executable and the separate `ROCK_NEO.EXE`; header recognition alone did not prove their handoff or execute either program.

**Limit:** an internally consistent archive and hashes establish identity of the supplied material, not independent authenticity against an authoritative disc reference.

## 2. Disc integrity and bounded export

The raw-sector investigation recorded **760 unequal duplicated XA subheaders**. A later EDC pass found all **102,633 Form1 sectors** matched; all **104,512 Form2 EDC fields** were zero and remained unverified. No header was repaired or one copy silently preferred.

A conservative exporter produced **208 Form1 files** while leaving **39 unsupported media files** out of logical export. ISO-sized slices were not misrepresented as full XA streams. Original raw tracks remained necessary evidence.

## 3. Establish a native Windows build route

Official compiler/Wine installation approval was requested at **14:31:48 UTC**. The initial cloud environment supported portable C++ but lacked a ready Windows compiler/runtime. A system-install attempt failed during sandbox setup before package installation. Signed official packages were subsequently staged in the workspace without changing system packages.

A genuine Windows x64 PE smoke program compiled successfully. Wine initially aborted before application output. At the explicit **14:44 UTC** diagnosis checkpoint, a process-local environment adjustment resolved the initial Wine failure; the next failure was denied local Unix-domain socket creation. An independent socket probe corroborated that IPC restriction.

**Result:** Windows cross-compilation became available. Windows execution did not follow from that build or from a failed Wine launch.

## 4. Recover textures and local model parts

Independent asset scanning identified 3,737 candidate headers, including 1,851 validated type-1 texture candidates, across the 205 BIN files. These were custom repacked structures, not a collection of ordinary TIM files.

The first full-width linear texture interpretation was wrong. Original upload behavior established **32-word × 32-row sector tiles**; decoding and tests were corrected accordingly. Passing size checks had not established correct image semantics.

A bounded local polygon decoder accepted 24 discovered PBD-P payloads. Original rendering code corroborated triangle/quad record structure and explained duplicate packets as double-buffered workspaces, not duplicate faces. Early local-part exports did not contain a complete character hierarchy or animation.

## 5. Build the native inspector and safe editor foundation

A C++17 Win32/GDI inspector gained real file enumeration, hex views, image and OBJ inspection, orbit/zoom, per-part XYZ edits, undo/redo, and save/reload. Source-bound sidecars preserve edits without patching originals; malformed, mismatched or incomplete sidecars reject transactionally.

The inspector later read supported original BIN textures and meshes directly, rather than requiring image/OBJ intermediates. Unsupported data remained inspectable as bytes rather than being guessed into a scene. Direct scene-instance editing retained source placement identity and independent instance deltas.

**Preview 01** froze an early source/binary snapshot without original game assets. Active editor work continued separately; later controls and importer work must not be attributed to that unchanged preview.

## 6. Reconstruct diagnostic character poses and sequence stepping

Original code established the 15-joint hierarchy and mapping of 18 mesh parts. Static bit-origin propagation recovered a packed primary-pose expansion, including sparse axes and an overlapping-store effect. A portable translation was checked across **456 single-input-bit basis vectors and 48 output components**.

The diagnostic character comprises 18 parts, 317 vertices and 316 faces, with source-derived textures and floating-point transforms. CPU texture rasterization added inspection value, not full original GPU/GTE fidelity.

The primary sequence updater was recovered and checked across **262,144 transitions** against a separately expressed instruction-algebra oracle. The active inspector exposes **55 nonempty sequences among 64 slots**, pose selection and one-original-update stepping. It does not assume a frame rate. The `FF` control is a repeating hold, not an automatic stop; duration zero expires after 256 update calls.

## 7. Recover a static environment, then distinguish it from startup

The ST1C environment subset yielded eight source placements and 854 four-corner faces. A direct C++ decoder matched **863 reference rows**, preserving placement, coordinates, UVs, flags and material evidence. Original renderer analysis later corroborated the coordinate scale role, narrowing earlier interpretation uncertainty.

This is union geometry from a supported subset, not verified visibility, complete collision or a running scene. The initially inspected ST1C environment is **not** the first startup scene.

Separate startup analysis resolved the zero-state path to **scene 1/subscene 0 and ST01**, not an asserted title screen. The established direct resource order is INIT_DAT → DEMO_DAT → ST01; it is not a complete boot dependency set.

## 8. Native import and resource preparation

The active inspector gained a bounded raw-track import flow with hashing, validation, progress, cancellation and rollback, and refusal to overwrite existing destinations. Raw-track sniffing prevents a large disc image being treated as an ordinary small asset BIN. The import UI's existence and portable tests did not establish actual-Windows validation of that newer interaction.

Complete physical resource plans were recovered for the three established startup files, including palette operations and **nonexecuting** sound-bank/sequence preparation. Palette records required correct physical strides rather than blindly trusting nominal counts. Resource parsing, sound preparation and a verified image are not equivalent to committed loads, sound registration or playback.

## 9. Recover first-scene services and bounded source functions

ST01 overlay analysis established dispatch-table installation, ordered completion callbacks, four setup-service boundaries, c0 pool allocation, object eligibility and bounded object updates. Manual portable implementations used caller-owned state and explicit unsupported outcomes.

A closed ahead-of-time translation proof covered a verified setup function and a small object state-0 slice. These are fixed, source-identity-gated translations into compiled C++, not a general recompiler or runtime instruction interpreter. Agreement with a manual translation is useful regression evidence, not original-machine execution.

A diagnostic fixture connected four services and one state update, then stopped on unknown object eligibility. That fixture must remain visibly separate from production startup. It did not make the scene reachable from real initialization.

## 10. Native entry, heap, events and early global initialization

The native session began advancing the actual executable-entry prefix, tracking known and unknown RAM bits, BSS clearing and original-address metadata without treating original addresses as host pointers. The inherited return address remained unknown rather than becoming a fictional zero.

An owned native heap completed the first platform-service boundary. Post-heap continuation then reached critical/event setup. The connected event sequence created and enabled a real owned record without generating an occurrence merely because registration succeeded. Pending unsupported callbacks were retained.

The event-stage record reports **56 regression tests**. At **17:12 UTC**, the explicitly recorded global-prefix checkpoint reached a pending interrupt-mask write. Later stages superseded these stops; they remain meaningful historical boundaries.

## 11. Interrupt configuration, saved context, hook, timer and DMA

The next sequence implemented narrowly typed interrupt-register operations and source-preserving acknowledgment semantics, followed by saved context capture, reviewed stack-pointer adjustment and owned hook installation. Known-bit and owner/generation checks prevented altered or stale state from being accepted.

The context stage recorded **61 tests**, hook stage **63**, and timer stage **65**. Timer initialization was an explicit native semantic policy, not generic bus-width or physical timing equivalence. Reset observation was not a live count; no timer tick was invented.

IRQ policy and restoration barriers retained eligible/unknown interrupt work instead of silently acknowledging it. DMA interrupt configuration followed, with **69 regression tests**, exhaustive acknowledgment/knownness checks, allocation-failure testing and successful Windows cross-builds. This configured owned state; it did not execute DMA transfers.

## 12. Native ISO lifecycle and CD diagnostics

CD-driver removal required an actual owner/lifecycle contract, not a successful no-op. Independent native cold start and unknown inherited state became distinct launch modes. Accepted reads and callbacks could keep teardown pending; only genuine completion retired obligations. Unknown inherited state stopped separately.

The frozen startup/lifecycle Windows kit later passed four contract checks, reaching the still-unsupported diagnostic-output boundary. The next slice added an actual session-owned diagnostic byte sink, then stopped before its first CD-controller byte write. Its own Windows kit passed four checks. Diagnostic output was real native state, but not CD completion or boot.

## 13. CD controller and command-admission prefix

An owner-bound native controller implemented the reviewed configuration subset while retaining unknown source-facing status and enable bits. Its frozen Windows validation passed four checks and stopped before the source command routine.

The admission-prefix stage advanced to an unaccepted status-command write. Its four Windows checks matched the expected cold/inherited/fixture boundaries. GPU/timer observations carried zero known masks; their filler values were not evidence of readiness or measured zero.

## 14. Windows testing authorization and original image acquisition

An unsigned policy-safe PowerShell runner was blocked at **15:46:03 UTC** with an authorization failure. The user explicitly required protections remain unchanged. Direct synthetic executable observations were recorded later on the VPS (see the validation history). At **18:03:41 UTC**, the user abandoned the VPS route and explicitly authorized testing on their own Windows computer. This superseded the earlier cloud-only boundary, not a blanket permission for future machine access.

Under that authorized Windows-testing workflow, the original private archive was acquired through the connected file service. Archive identity and entry safety were checked before extraction, and raw tracks/CUE were hashed. This was **data preparation only**, not mounting, a runtime read, or execution.

A later native media-preflight stage established an immutable raw-sector service, production-image identity and actual sector reads. All **11 Windows processes** passed their frozen contracts. Preflight still did not accept a command, produce a response, invoke a callback or boot the game.

### Presentation deliverables (18:42–18:55 UTC)

At **18:42 UTC**, a Discord-ready status draft was provided, not posted externally. At **18:46 UTC**, a development character PNG and native C++ animation GIF were shared as development renders—not Windows or gameplay screenshots. The GIF used **10 fps for presentation**, not verified original animation timing. At **18:55 UTC**, an explanatory **3840 × 2160** poster was delivered from generated **1672 × 940** artwork upscaled with Lanczos; it was not gameplay or native-4K game rendering.

These communication artifacts are not native boot or execution evidence. Their images, private links and underlying assets are excluded from this public documentation payload.

## 15. Status response, notification and true source completion

The bounded status-response stage prepared or published one response, depending on explicitly enabled native policy. Its **19 Windows cases** comprised 16 exit-0 results and three expected exit-1 refusals. The notification-enabled path latched an IRQ source but stopped at unimplemented exception-chain routing: response publication was not response consumption or command completion.

The next **native IRQ-chain** milestone completed the first status command through the actual translated handler/consumer, logical B0 return and original wait. It retained distinct earlier profiles and explicit refusals. **88 regression tests** and **29 actual Windows cases** passed (22 exit 0, seven intentional exit 1; 14 complete JSON comparisons).

This is the last frozen, Windows-validated runtime milestone at the documentation pause. It stops **before reset command `0A`**; no game boot is claimed.

## 16. Unfrozen CD configuration and isolated validation

The newer opt-in candidate adds reset `0A` ACK plus separately completed reset, then unmute `0C`. Reset uses the same immutable image allocation, prepares a new reader, actually probes sectors and EOF, and only then publishes completion. Native mute-request state does not establish silence or audio playback.

The supported connected path performs **four IRQ returns and 11 logical clock calls**, then stops at source address `80079070` attempting a sound-register read at `1F801DB8`. High-level CD initialization has not returned.

Shared-output aggregate attempts became inconclusive after a transport failure left runner state uncertain. Final acceptance moved to an isolated copy with separate outputs and pinned inputs. At the pause, **92 tests, 19 tool tests, 21 CLI cases and 18 Windows cross-builds** had passing reports, but remaining standalone-component checks and final receipts were not yet accepted. Two component failures were attributed to missing preview fixtures. At **21:39:13 UTC**, the already-running isolated aggregate drained: **19 completed stages, 17 successful, two missing-fixture failures; acceptance false, frozen false, retries false**. Asset comparison (13,305 records) and queued-handler fixtures passed. No new repair/retry work was started after the pause. This is not a promoted release or actual Windows execution of the candidate.

## 17. Scratch-only future work

A pure mixer-arithmetic prototype exists only in scratch: **102,822 checks, 34,193 frames, 20,000 randomized cases and three fault mutants**, with address/undefined-behavior sanitizer passes and LeakSanitizer unavailable. It is not integrated, a sound-device implementation, decoding or playback.

A packaging helper has **15 synthetic tests** in scratch. No new configuration kit had been created at the pause. Neither scratch effort supersedes the frozen IRQ-chain release.

## 18. Public identity and documentation pause

At **20:51:48 UTC**, the user explicitly requested a public repository named **Rock Man x64**, targeting `raiinman/Rock-Man-x64`, and requested the `raiinman/dox` repository in the setup workflow. Development paused safely for repository setup. Setup was verified complete at **20:57:49 UTC** and reported at **20:57:53 UTC**. Build check-ins were disabled at **21:01:07 UTC**; the user explicitly resumed development at **21:01:46 UTC**, and check-ins were enabled at **21:01:50 UTC**. That authorization changed the earlier no-public-repository boundary, but did not authorize redistribution of original assets or private evidence.

At **21:37:34 UTC**, the user asked to pause development and bring GitHub up to date from the beginning through the present. Build check-ins were disabled at **21:37:55 UTC**. This history is the resulting documentation work; already-running validation was allowed to drain without new development or retries. It does not imply that candidate validation, publication, source upload or a new release was completed merely because they were requested.

## 19. Resumption, configuration Windows acceptance and connected mixer

Development resumed at 22:04 UTC. The configuration stage subsequently passed 40 Windows cases; the newer connected CPU software mixer then established a genuine high-level CdInit return in Linux testing, stopping at the next unsupported CdSync boundary. A reporting-only correction preserves old-profile bytes without changing runtime capability. Audio freeze sealing and target execution remain pending. The [validation history](validation-history.md) records exact scope, counts and retained failures; none of these milestones establishes playback or game boot.

## 20. Sealed mixer and mode-00 candidate — October 22 work, October 23 update

The mixer freeze subsequently completed, retaining 419 source files, 20 reproducible Windows executables and 30 CLI profiles. All 51 actual Windows cases passed: 30 expected successes and 21 intentional refusals, with 30 JSON and 21 text comparisons. The true high-level initializer return is established without device output, decoding, playback or game boot.

A separate erratum records inherited contract summaries of 40/18/21 instead of the actual 51/20/30. Definitions and comparisons were complete; the freeze was preserved unchanged. New generic packaging preflight passed 22 synthetic tests and rejects those stale summaries rather than silently repairing history.

A subsequent mode-00 candidate connects genuine same-image Form1 configuration and response/IRQ/callback continuation, with one real event examined and no match invented. Pinned earlier-case regression and ten new profiles passed, as did targeted direct-pinned sanitizer fail-N checks. The candidate remains unsealed and not Windows-tested, with no verified terminal full-project aggregate. Earlier mistaken pinned-log attribution, copied-byte expectation and insufficient/invalid failure-injection assertions are retained in [validation history](validation-history.md). Graphics startup remains static planning, not implementation or GPU initialization.

## 21. Isolated recovery accepted; release and Windows runner gates — October 23, 01:05 update

All 13 stages of the isolated recovery passed, including 92 project tests, 19 tool tests and 13,305 metadata rows, with 427 source and 4,181 input identities unchanged. The original interrupted attempt remains inconclusive and excluded. A newer unsealed Linux contract passed all 69 cases across 26 executables and 40 CLI profiles (39 expected exit 0, 30 intentional exit 1). Both Windows cross-build passes completed with all 26 pairs byte-identical and actual executable/profile mapping verified; no Windows mode execution or sealed release is implied.

Three successive synthetic Windows supervisor candidates failed their first success case, accepted zero checks and retained the failures. Owned-job cleanup completed, but later suite cases were unrun. Console-detached candidate 6 subsequently passed all 15 synthetic Windows checks in one invocation, including deliberate descendants, timeouts and forced-supervisor-termination cleanup. The 14-file kit remained unchanged, with no protection override or unresolved cleanup. This is not Windows mode execution. Offline toolchain provenance improved while nine host dependencies retain a package-origin gap. None of this establishes game boot, playback or hardware equivalence.

## 22. Actual Windows mode validation and bounded graphics progress — October 23, 02:05 update

The mode-00 stage passed all 69 actual Windows cases in one invocation: 39 expected successes, 30 intentional refusals and 40 complete CLI JSON comparisons. All 605 kit files, including 26 case executables and support material, and separately three pre-existing original inputs remained unchanged; no original inputs were packaged; owned jobs emptied without security changes. Review relied on the identified authorized execution report, not an independent download of raw local receipts. A separate acceptance record preserves frozen historical metadata. No final/public release, game boot or playback follows from this validation.

A later graphics-entry prefix passed 12 connected Linux cases, the 69-case regression and targeted 11-checkpoint allocation testing. A first fixture compilation failure and reviewed fixture-only repair are preserved; production runtime bytes did not change. A newer diagnostic continuation passed 19 connected cases and its 69-case Linux regression, plus 29 targeted allocation checkpoints, with independent bounded Linux acceptance. It publishes a real diagnostic, clears bounded RAM, follows the initialized callback and stops at A0:49. Neither graphics stage has Windows parity or a repeated 13-stage aggregate. Inspected Sony manuals do not establish that exact service contract; a community lead is not implementation authority.

## 23. IDE command validation and combined Linux candidate — October 23, 03:05 update

Source bytes/Back passed 50 actual Windows synthetic command/state checks; standalone visual QA was blocked before launch by unavailable capability, leaving pixel correctness unverified. The combined development candidate passed all 16 full-project-plus-source-test stages and independent review of its 69-case Linux contract. Combined connected-19 is pending and allocation-29 remains unrun. Owned snapshot v1 exposed an import-contract gap; v2 correction awaits independent rereview, not real capture or debugger acceptance. A0:49 remains pending; no game boot or playback is claimed.

## 24. Combined Linux closure and bounded owned capture — October 23, 04:05 update

All four combined Linux phases are accepted: the 16-stage aggregate/source-test set, 69 regression cases, 19 connected cases and 29 targeted allocation checkpoints. Actual owned capture separately passed four Linux/UBSan cases, totaling 60 captures and 253 injected allocation failures. Production checkpoints are distinct from synthetic field/lifetime coverage; this is not exhaustive private-state introspection, Windows capture or a live debugger.

Exporter/frozen-viewer v1 review found directory-replacement deletion, foreign temporary-file publication and Windows reparse traversal gaps before any actual exporter or Windows viewer run. Findings and earlier build/integration failures are retained. V2 corrections received source/synthetic acceptance after independent review; no end-to-end exporter/viewer acceptance is claimed. A0:49 remains pending.

## 25. Portable export/import and Windows validation repair — October 23, 05:05 update

One actual Linux exporter invocation advanced 2,175 command batches to the existing refusal, produced a private 2,846-byte artifact and passed portable import/model rendering of 6,108 bytes. Three existing-output constructor refusals preserved that artifact; they were not additional startup runs. Independent review accepted this bounded result, not GUI or full IDE completion.

Windows viewer preparation required a metadata unblock and companion-fixture correction. A culture-sensitive BOM check then falsely rejected the positive offline control before any native executable ran. The corrected v2 validator passed 24 checks across four cultures and 33 offline controls. The subsequent actual 111-check native run passed 36 checks, then failed bounded file load at check 37; 74 checks remained unrun. Cleanup completed without timeout, but no full native acceptance or pixels are established.

An independently reviewed original-loader finding is static only: conditional earlier A0:49, unresolved firmware-return-relative writes and unchecked synchronization failure prevent treating the native cold-start trace as proof of inherited GPU/firmware history. A0:49 remains pending.
