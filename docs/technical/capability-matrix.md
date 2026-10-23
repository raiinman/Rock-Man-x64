# Capability inventory

This matrix describes bounded private implementation work, not downloadable features in this documentation-only repository. “Implemented” does not imply Windows execution, end-to-end integration or gameplay. [Validation categories](../status/validation.md) and [current status](../status/current-status.md) qualify those claims.

| Area | Established scope | Important boundary |
|---|---|---|
| Disc inventory | Archive integrity, raw-track identity, ISO file inventory and logical export | Integrity is not independent disc authenticity; media anomalies remain documented |
| Native importer | Bounded raw Track 1 reader, safe new-directory export, progress and cancellation | Not a universal ISO/CUE/ZIP reader, audio decoder or disc repair tool |
| Sector integrity research | Form1 EDC investigation and separate raw-sector evidence | Form2 zero EDC values do not establish integrity; duplicated XA-subheader anomalies are not repaired |
| Textures | Recovered tiled layout, palette-aware diagnostic decoding | Not universal texture coverage or full GPU texture state |
| PBD local geometry | Bounded part records, vertices and triangle/quad interpretation | Not every model/container variant |
| Character assembly | Recovered 15-joint hierarchy; diagnostic 18-part assembly with 317 vertices and 316 faces | Approximate transforms; not full animation or rendering fidelity |
| Packed pose helper | Static bit-origin reconstruction and native decoder; 456 input-bit basis vectors across 48 outputs | A fixed block proof, not a complete animation system |
| Sequence helper | Primary/secondary update rules; primary inspector exposes 55 nonempty sequences | Update calls are not Hz; repeating hold is not an end-of-playback signal |
| Static environment | Supported STG/HED/IDX union geometry; representative 8 placements and 854 four-corner faces | Visibility lists, broader orientations, collision and material semantics remain incomplete |
| CPU rasterizer | Diagnostic textured character output, depth and selection overlay | Not complete PS1 GPU/GTE behavior or a game frame |
| Native inspector | Win32/GDI asset browser, hex/image/mesh/scene views, pose controls and edit history | Not a complete IDE, script compiler or playable editor session |
| Sidecar persistence | Source-bound transforms, validation and atomic replacement | Local edits, not original asset rewrite or game patches |
| Resource plans | Ordered resource records and bounded copy/upload/cache operations | Sound preparation is nonexecuting; palette cache is not completed hardware residency |
| First-scene functions | Recovered setup, allocation, callbacks and bounded dispatch subsets | Synthetic diagnostic reachability does not prove production initialization |
| Ahead-of-time handlers | Independently generated native C++ for selected recovered routines | No general CPU interpreter; untranslated successor remains a stop |
| Startup | Entry/BSS, heap, event/context/hook and selected native device/routing policy prefixes | Bounded path, not full boot or general firmware replacement |
| CD ownership and status | Sealed immutable reader, genuine status operation and retained response/notification ownership | Native service state is not physical drive state |
| IRQ chain | Frozen stage completes first status command through actual source-handler return | That historical stage stops at reset `0A`; the newer configuration stage is separately Windows-verified |
| CD reset and unmute | Frozen actual reader/configuration transactions; 40 Windows cases and four source IRQ returns | Configuration stage stops at the sound-read boundary; high-level initializer has not returned there |
| Native CPU software mixer | Sealed same-owner CPU processing and genuine high-level CdInit return; 51 actual Windows cases passed | Stops at next CdSync boundary; no decoder, output endpoint, playback or physical SPU equivalence |
| Mode-00 candidate | Same-image Form1 reader, actual FIFO/response/IRQ/callback path; pinned Linux profiles and targeted sanitizer checks passed | Unsealed, no Windows test or verified terminal full-project aggregate; no invented matching event or hardware timing claim |
| Packaging | Configuration and mixer stages sealed; stricter derived-count/reference/JSON preflight passed 22 synthetic tests | Mixer summary-counter defect retained in unchanged historical freeze; mode candidate not sealed; no public package or source release |
| Gameplay | Target only | No demonstrated player control, collision, AI, combat, save compatibility or complete scene lifecycle |

## Why the subdivisions matter

A parser can accept a structure whose rendering semantics remain incomplete. A source helper can match an independent oracle without being reachable from production startup. A Windows executable can compile without ever running on Windows. A Windows console checkpoint can pass without establishing the GUI's interaction behavior. None of these should be collapsed into a single completion percentage.

The current integration frontier and outstanding acceptance work are in [current status](../status/current-status.md); proposed work is in [decisions and handoff](../status/decisions-and-handoff.md).
