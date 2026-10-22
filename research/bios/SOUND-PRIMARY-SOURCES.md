# Primary-source sound documentation and the `0x1f801db8` boundary

Observation time: 2026-10-22, completed 22:50 UTC. This is a documentation pass, independent of the private firmware static-analysis profiles and of the other computer's game investigation.

## Result

Vendor-authored Sony documentation supports a distinction between a master-volume setting, its mode and a current-master-volume observation. This pass did **not** find a vendor-authored source explicitly binding numeric addresses `0x1f801db8` and `0x1f801dba` to those concepts. Their numeric meaning, timing, reset state and relationship to the particular MML1 read remain unresolved by this primary-source pass. A bounded failed search does not show that such documentation never existed.

## Catalog inspected first

The existing `research/sony-document-index.json` lists Sony's PlayStation Hardware, Run-Time Library Reference, Run-Time Library Overview, Sound Artist Tool and SPURAM technical-note references. Their catalog entries identify an unofficial host and originally record index-level observation rather than downloaded content. This pass inspected relevant manual content separately; it does not silently upgrade every catalog item or every mirror file to verified status.

The existing sound report and native handoff preserve the separate game-path numeric-read gap. Matching an API name in a later manual cannot bind that game's caller, source bytes, SDK revision, register access width, initialized state or acceptable native return.

## Vendor-authored sources actually inspected

### Sony Run-Time Library Reference 4.4

- Source: [Sony Run-Time Library Reference 4.4](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libref.pdf)
- January 1999; 1222 PDF pages; Sony-authored, unofficially hosted. Front matter restricts distribution to licensed developers/publishers and identifies confidential Sony material.
- Printed 15-5, PDF page 985 (zero-based index 984): common attributes distinguish `mvol` (master volume), `mvolmode` (mode) and `mvolx` (current master volume).
- Printed 15-23, PDF page 1003 (index 1002): the ordinary getter is valid in direct mode.
- Printed 15-25, PDF page 1005 (index 1004): `SpuGetCommonMasterVolumeX` retrieves left/right current volume; metadata gives introduction 3.7 and documentation date December 14, 1998.
- Extracted-text finds for `1f801db8` and `1F801DBA` returned no matches; that is not exhaustive address absence.

These later API descriptions do not identify the 1997 firmware routines or the game's library revision. No header, prototype or implementation is reproduced.

### Sony Run-Time Library Reference 4.7

- Source: [Sony Run-Time Library Reference 4.7](https://psx.arthus.net/sdk/Psy-Q/DOCS/LibRef47.pdf)
- Observed publication: March 2000; 1220 PDF pages; same unofficial host and restricted Sony provenance.
- Printed page 15-25, PDF page 1004 (index 1003): the current-volume API distinction is independently retained in this later edition.
- The extracted-text search for `1f801db8` returned no match.

This is a revision cross-check, not evidence that the tested firmware or MML1 uses library 4.7.

### Sony PlayStation Hardware

- Source: [Sony PlayStation Hardware](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Hardware.pdf)
- Observed publication: August 1998; 48 PDF pages; vendor-authored, unofficially hosted, restricted developer-manual provenance.
- Printed pages 4-3 through 4-6, PDF pages 35 through 38 (indices 34 through 37): sound architecture separates CD-decoder mixing, SPU processing and final master-volume/output stages. Volume can vary independently of the envelope.
- The viewer's `1f80` search returned no extracted-text match.

The architectural separation supports investigating several sound authorities separately. These pages do not supply the sought numeric-register identity or an exact CPU-read contract for it.

### Other accessed catalog leads

- Run-Time Library Overview 4.4: [Sony Run-Time Library Overview](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libovr.pdf) — January 1999, 312 pages. Targeted extracted-text finds for `current master`, `master volume` and `sweep` returned no matches. This is not an assertion that all relevant content is absent.
- Sound Artist Tool: [Sony Sound Artist Tool](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Sound20.pdf) — August 1998, 74 pages. Title/front matter and a volume-related search were accessed; this did not establish a numeric register mapping. Tutorial/sample code is not used as an implementation reference or reproduced here.
- SPURAM technical-note catalog entry was reviewed as a lead; this pass did not inspect its content or claim a result from its filename.

## Three focused search passes

Queries below are the actual submitted strings. Search returned many irrelevant or non-primary results. No emulator, another port/decompilation, community PSXSPX derivative or community implementation was opened or relied upon to construct the findings. Search-result snippets from excluded categories are not primary-source evidence and do not resolve the address mapping.

### Discovery

1. `Sony PlayStation SPU "1F801DB8"`
2. `Sony "current main volume" "SPU" manual`

Outcome: numeric-label results were predominantly community documentation or implementation-related material and were excluded as authorities. The existing Sony manual catalog supplied the permitted primary-source leads instead.

### Cross-check

3. `"Sony" "MVOLXL"`
4. `"Sony" "1F801DB8" -site:psx-spx.consoledev.net -site:github.com -site:gitblind.noratr.app -site:sotn.dev`
5. `"PlayStation" "current main" "Sony" hardware manual`
6. `"SpuGetCommonMasterVolumeX" Sony manual`
7. `"1f801db8" "Sony" filetype:pdf -site:psx-spx.consoledev.net -site:static.grumpycoder.net`
8. `"MVOLXL" Sony SPU documentation -site:github.com -site:psx-spx.consoledev.net`

Outcome: query six discovered the later Sony library-reference edition; the January 1999 edition already in the catalog was then checked for the same API distinction. The other queries did not yield a verified vendor-authored numeric-address mapping in inspected material. Some results were irrelevant modern Sony news; those were not consulted.

### Gap search

9. `"Sony" "SPU" "1f801dba" -site:github.com -site:psx-spx.consoledev.net -site:gitblind.noratr.app -site:sotn.dev -site:static.grumpycoder.net`
10. `"SpuGetCommonMasterVolumeX" "1f801db8" -site:github.com -site:gitblind.noratr.app`
11. `"SPU" "MVOLXL" filetype:pdf Sony`
12. `site:psx.arthus.net "1F801DB8"`
13. `Sony CXD2922 SPU datasheet volume register`
14. `site:sony.com PlayStation SPU register volume`
15. `site:psx.arthus.net/sdk/Psy-Q/DOCS "master volume" "register"`

Outcome: no suitable vendor-authored PS1 register-address specification was verified from these results. Unrelated chip data sheets, modern consumer-support pages and excluded community sources did not answer the specific question. No PS2 register map was substituted for a PS1 specification.

## Access and extraction limitations

The five selected Sony manual URLs opened through the web tool. Extracted text is searchable but is not proof that images, table layout or alternative numeric formatting have been exhaustively searched. Screenshot requests were made for Hardware index 35 and Library Reference indices 1004 and 1002. The index-1002 screenshot request returned `TimeoutError`; the text page remained available. This access failure is preserved, rather than converted into an absence finding. No original document or screenshot is included in the proposed public report.

No authenticated Sony-hosted developer portal, licensed register-level specification, chip-internal documentation or new physical measurement was obtained. No conclusion here certifies clean-room status or implementation clearance for the mirrored materials.

## Inference and bounded next step

**Supported inference:** Distinguishing a selected volume setting from an observed current volume is consistent with Sony's documented API model. It is sensible to retain requested versus applied/current state separately in an explicitly native design. That design inference is not an address binding, hardware timing model or proof of the game's dependency.

**Not established by this source pass:** the numeric pair's physical field meaning, signedness, writeability, update cadence, sweep behavior, reset value, stable-read rules or relation to CD muting; the privately attested game load's exact width and consuming operation; and whether its native software observation matches physical behavior.

The smallest next research step is to bind the identified game's actual instruction, access width, effective address and reaching state on the other agent's authorized source path. The [focused handoff](DB8-BOUNDARY.md) distinguishes the subsequently attested native adapter from the still-unresolved physical semantics. Separately, seek an identifiable vendor-authored PS1 register-level specification or independently permitted measurement for the numeric pair. Do not certify physical behavior by naming resemblance alone.

## Focused chip, service-manual and patent follow-up

Nine additional queries were submitted after reviewing the earlier negative results:

1. `Sony CXD2922BQ datasheet sound processor register`
2. `Sony PlayStation SPU technical reference current volume register hardware manual pdf`
3. `"CXD2938" datasheet Sony SPU`
4. `"CXD2922" "pdf" Sony -site:github.com`
5. `"PlayStation" "SPURAM" technical note Sony`
6. `"SpuGetCommonMasterVolumeX" sweep manual`
7. `"Sony" "sound processing" "master volume" patent PlayStation`
8. `"Sony" "CXD2922BQ" datasheet register address`
9. `"Sony" "sound" "current volume" "register" patent`

Sony's [US5978492A patent](https://patents.google.com/patent/US5978492A/en), Figure 3 description, provides primary architecture evidence for distinct voice, PCM-mixing, reverb and downstream master-volume stages. The [focused report](DB8-BOUNDARY.md) records the inference and its limits. Extracted-text searches did not find `register` or `1f801`; this is not an exhaustive image search or a numeric register binding.

The [Sony SCPH-9000 service manual, third edition](https://gamingdoc.org/wp-content/uploads/2020/07/Sony_PlayStation_SCPH-9000_series_service_manual_3rd_edition.pdf), May 1999, is a Sony-authored 28-page manual on an unofficial GamingDoc mirror, with reproduction restrictions in its front matter. PDF indices 5–6 provide chip/block and audio-interface context. Text searches for `1F801`, `DB8` and `SPU` returned no matches; board connectivity does not establish the desired CPU-read contract.

The [Technical Reference CD 21 catalog](https://gamingdoc.org/technical-documentation/consoles/sony-playstation/official/hardware/technical-reference-cd-21-12-10-1997/) was accessed, but its linked ZIP fetch timed out. A separate local HEAD request and a GET restricted to the first 1024 bytes both failed at DNS resolution, before any HTTP response or bytes. These failures do not establish that the archive is unavailable; its contents remain uninspected. A second patent lead, US5767430A, could not be opened and supplies no finding here. Excluded community labels and implementation snippets are not authorities. No verified numeric binding emerged from this follow-up; no manuals, SDK code or archives are redistributed.
