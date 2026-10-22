# Sound and CD-related MMIO in the derived BIOS frontend

## Target and method

This pass uses a separate REA static-analysis profile for a private, independently transformed BIOS frontend. Its subject is the derived 372032-byte artifact with SHA-256 `7920530e46981bab09bef02c72f35964bca25c879a72f3bf1c5313921143fbe7`, mapped at `0x80030000..0x8008ad3f`. It is not the original 524288-byte ROM or a captured RAM image. The bounded data transform does not execute BIOS instructions; the REA analysis also does not execute them.

The original ROM identity, transform source range and transform review belong in the corresponding methodology report. This profile supplies no zero-filled tail, hardware state, copied kernel, original ROM alias or additional RAM mappings. Missing reference and function results therefore have those explicit boundaries. Generic MIPS32 decompiler conventions do not supply R3000A load-delay, PS1 COP2/GTE or physical device behavior.

Numeric address `0x1f801db8` is a priority because the project's separate native handoff mentions an unresolved sound-related numeric-port read. Matching that numeric address in this frontend would establish a firmware investigation lead only. No MML1 executable, reaching state or dependency on this frontend is inspected here.

The [primary-source pass](SOUND-PRIMARY-SOURCES.md) corroborates Sony's distinction between volume settings, mode and current volume, including newly accessed 1997 library documentation. It does not establish a vendor-authored numeric binding for `0x1f801db8` or identify this firmware's getter with that API.

The [focused numeric-boundary report](DB8-BOUNDARY.md) adds whole-image encoding scans, their explicit limits and the game-consumer evidence needed to assess the subsequently attested native observation.

## Evidence and interpretation

The derived profile's initial auto-analysis inventory contains 744 candidate procedures and 111 defined strings. Those are discovery counts, not complete code coverage or successful frontend execution. [S0]

### Register-base pointers and the unresolved `0x1f801db8` read

Four separately read pointer words at derived coordinates `0x8008a700`, `0x8008ab40`, `0x8008ab50` and `0x8008a554` all resolve to base `0x1f801c00`. The selected instruction bodies use these pointers plus offsets, so literal or exact-address searching alone is not enough to characterize sound-device access. [P1-P4]

The initial exact-address reference queries for `0x1f801db8` and `0x1f801dba` return no entries. That is a bounded statement about the Ghidra-defined reference inventory. It does not establish that these addresses are absent from computed, indirect, unidentified or differently mapped paths. The selected common getter described below was inspected at instruction level and does not read either address in its recovered body. This frontend pass therefore does not resolve the separate game-path numeric read or justify a constant-zero answer to it. [X1, X2, S3]

By comparison, the same reference inventory identifies accesses to the neighboring paired addresses `0x1f801d80/82`, `0x1f801d84/86`, `0x1f801db0/b2`, and control/status-shaped addresses `0x1f801daa`, `0x1f801dac` and `0x1f801da6/da8`. These leads were followed into the selected routines below. Numeric accesses are direct evidence; assigning complete physical register semantics requires a separately identified hardware specification and suitable validation.

### Common attribute setter: selected writes are individual operations

Routine `0x80062e74` reads a caller-supplied field mask. A zero mask selects all of its implemented fields; otherwise individual bits select writes. Its instruction body contains halfword writes to the three paired address groups above and to `0x1f801db4/b6`, plus halfword read-modify-write sequences at `0x1f801daa` and `0x1f801dac`. The field mask and the control-bit values are separate inputs. [S1, P1]

Several control changes use two device stores: one clears selected bits, another reads and combines the requested bits. These are sequential register accesses. The routine does not establish one atomic hardware revision or supply a host-side transactional mixer contract. A native design can choose a stronger policy, but that policy must be distinguished from the observed accesses. The body returns zero after its selected operations; no audio endpoint, audible signal or physical state confirmation is established by that return. [S1]

### Common getter: reading attributes is not measuring sound output

Routine `0x800631cc` reads halfwords from the paired addresses `0x1f801d80/82`, `0x1f801d84/86`, `0x1f801db0/b2` and `0x1f801db4/b6`, and writes the values into distinct caller-output fields. It also reads and extracts bits from `0x1f801daa` and `0x1f801dac`, combines two neighboring status-shaped halfwords at `0x1f801d9c/9e`, and reads `0x1f801dae`. Its returned zero is independent of whether a host endpoint exists. [S3, P1]

The selected operation dispatcher `0x80062280` routes selector `0x100` to the common setter and selector `0x101` to this getter. Other selected cases change or query control bits, cached software transfer-address state or transfer-related registers. Its unsupported-selector path invokes a diagnostic helper and, if that helper returns, returns zero. Therefore zero alone cannot certify that a selector was supported or an operation produced sound. [S2]

These getters observe selected device-address values in code. They do not prove the hardware meaning of a separate `0x1f801db8` read, actual software DSP coefficients in the native prototype, a decoded stream, host mixer output or audible volume.

### Paired scale-and-store helper

Routine `0x80061988` sign-extends two caller halfword values, computes `(sign-extended input * 0x7fff) / 0x7f` using signed integer division, and stores the resulting low halfwords at `0x1f801d84` and `0x1f801d86`. No clamp is present in this small recovered body. This is a concrete numeric conversion and pair of device writes, not proof that every caller supplies a valid volume range or that these values are physical current gain. A native adapter must establish the caller's input range, units and destination semantics. [S4, P4]

### Initialization and status polling

Routine `0x80061d0c` modifies a DMA-control word through another pointer, writes a control halfword at `0x1f801daa`, invokes a helper, and polls status-shaped bits at `0x1f801dae`. The incremented software counter is compared with 5001 (`0x1389`); on the timeout branch it invokes a diagnostic helper and, if that helper returns, continues initialization rather than producing a distinct failure return there. The routine writes several global and paired register values, performs a small transfer through the helper below, then initializes 24 register groups using stride `0x10`, with multiple halfword stores per group. It finishes with additional writes and returns zero. [S5, P1]

This is substantial initialization code absent from the original ROM-only reference view. It still does not demonstrate that reset succeeded, sample RAM accepted the data, every voice is physically ready or playback started. The bound is an instruction-loop counter, not a calibrated time interval. Exact hardware acknowledgement and cache/bus effects are outside this analysis.

### Transfer helper: address, FIFO writes, control and readiness remain separate

Routine `0x80062050` writes a cached software transfer-address value to `0x1f801da6`, calls a helper, and compares status samples from `0x1f801dae`. It then handles a requested count in chunks capped at `0x40`, takes halfwords from the caller buffer and writes them to `0x1f801da8`, changes control bits at `0x1f801daa`, and performs further status polling. The source-copy loop advances its local count by two per halfword. This observation does not establish that arbitrary odd requested counts are safe; source bounds and caller constraints must be checked separately. [S6, P1]

Different timeout sites have different continuations. Some call the diagnostic helper and continue to the next stage if it returns; the final control-clear wait can return after a diagnostic call. The routine has a void-shaped return in the decompiler, rather than a demonstrated transfer-completion result. Routine `0x80061f98` wraps it with another status/control wait and returns the original requested-count argument; that return is not independent proof that the entire request reached physical sound RAM. [S6, S7]

The code separates a software cached transfer address, device-address programming, buffer reads, FIFO-shaped stores, control changes and readiness observations. A native replacement needs equivalent ownership and completion obligations for whichever game path is actually required; replacing the wait with assumed readiness loses the observed failure and progress structure.

### Decompiler coverage warning demonstrated in the frontend

At `0x8003de34`, the returned pseudocode collapses the routine to an infinite loop while marking multiple blocks unreachable. The recovered instruction body still contains numerous device reads and writes, including accesses through explicitly formed addresses `0x1f801da6` and `0x1f801daa`. Thus this investigation does not use the simplified pseudocode as a complete device-access trace. The mismatch does not establish which path executes or whether initialization succeeds. It establishes that instruction evidence and its limits must accompany the decompiler view. [S8, S9]

## Native-port investigation priorities

- Bind the actual game instruction and reaching state for the unresolved numeric read before assigning host gain semantics. Firmware frontend code is a separate subject.
- Keep requested settings, selected register values, cached transfer state, source buffers, transfer progress and actual audio output distinct.
- Preserve individual reads and writes, including control read-modify-write sequences and ignored reads, when tracing a required game path.
- Treat diagnostic and timeout continuations as explicit branches. A zero return or echoed requested count is not a universal completion receipt.
- Require separate evidence for sample decoding, voice processing, stereo mixing, CD mixing, output-device ownership, audible output, time calibration and physical hardware equivalence.

The decoded frontend is a firmware component, not MML1. None of these observations proves that MML1 calls these routines, shares their parameter layout or uses this SDK/library revision.

## Evidence references

Private complete Evidence contains derived BIOS bytes and decompiler output and must not be published. The identifiers below support the sanitized conclusions only.


- P1: `ev_1d640146efefb75e30e5a121141ba912a1b754cf61a7cec4a37f4cf09ed5d1db` (read_bytes, derived frontend subject).
- P2: `ev_65e4049321a21eb846d95368ff47438a5cafd956205be5786324b5b47d6f60a5` (read_bytes, derived frontend subject).
- P3: `ev_4b9d6ce75b6168dc157c93f15384579b5a096dc6c0f5d84f3baba156f9f265e6` (read_bytes, derived frontend subject).
- P4: `ev_7a4fd1181783635af8858c0f81c1cc9dc33bc92413c2d5c3b794e3f6739871fa` (read_bytes, derived frontend subject).
- S0: `ev_6ebd1b4ebc735c23efec42bd8c72a16009f360421122132af10c69340734f54a` (binary_overview, derived frontend subject).
- S1: `ev_05cc1aa150b614727376f7fcd9ee8a643233303fb5c7bf02f2cffc684eed069d` (read_function_instructions, derived frontend subject).
- S2: `ev_10c755be9c6a065ba3a70d084fa73da74a17bf1ca309f4e907c5d99a80fb25bf` (read_function_instructions, derived frontend subject).
- S3: `ev_9fbb722e970956404c1d0b8528444ada48ed6e472dde077800480db577afefc1` (read_function_instructions, derived frontend subject).
- S4: `ev_9915014938bc4078bccc1b1632481b9c6792edf372749325e3d26f3fcb2e6539` (read_function_instructions, derived frontend subject).
- S5: `ev_b1fd724341cef846fab8f83776ae0e788ad7f73e9e1c7d7f2bee42f27ba22e83` (read_function_instructions, derived frontend subject).
- S6: `ev_b343b6f34e6cef378d01e019129c20287861a9fdab838c8593d91e65064869fb` (read_function_instructions, derived frontend subject).
- S7: `ev_faf05604c3cb1c5f3540859e67140fdc1c5f4076f0b9c3b748e8dc600cd89770` (read_function_instructions, derived frontend subject).
- S8: `ev_d7184bd4295e454e378159d97c2742701fbbad66f67c5194b05da1c31bdc93b6` (procedure_pseudo_code, derived frontend subject).
- S9: `ev_1f1fa468d491c17fd727098729a7fb928107bf0f90b2d5353ebb80238e64a3ef` (read_function_instructions, derived frontend subject).
- X1: `ev_7a8cb033dd1d8692f585ccabce8a5a9108019b88d0594e9a7935da6d763bb700` (xrefs, derived frontend subject).
- X2: `ev_67131e2d46105c98dd4de9f4842b33b2568ed6c3178b964d251c05aeb67b228f` (xrefs, derived frontend subject).
