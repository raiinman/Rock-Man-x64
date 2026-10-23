# Primary-source sound documentation and the `0x1f801db8` boundary

Observation date: 2026-10-22, with successive source checks recorded below. This documentation investigation is independent of the private firmware static-analysis profiles and of the other computer's game investigation.

## Result

Vendor-authored Sony documentation supports a distinction between a master-volume setting, its mode and a current-master-volume observation. This pass did **not** find a vendor-authored source explicitly binding numeric addresses `0x1f801db8` and `0x1f801dba` to those concepts. Their numeric meaning, timing, reset state and relationship to the particular MML1 read remain unresolved by this primary-source pass. A bounded failed search does not show that such documentation never existed.

Newly accessed editions establish the current-master-volume attribute in December 1996 documentation and a dedicated getter in June 1997 documentation. This closes the earlier documentation-date gap; it does not identify the firmware's implementation or bind the numeric port. The [archive coverage ledger](SONY-ARCHIVE-COVERAGE.md) records subsequent release 2.0/2.3 scans, inaccessible revisions and image/document-type limits.

Separate community documentation reached through the user-supplied README **does explicitly bind the numeric pair**. The [focused boundary report](DB8-BOUNDARY.md#explicit-definition-reached-through-the-readme) records that positive result and its provenance. The negative vendor-source result above must not be read as absence of any published definition.

## Catalog inspected first

The existing `research/sony-document-index.json` lists Sony's PlayStation Hardware, Run-Time Library Reference, Run-Time Library Overview, Sound Artist Tool and SPURAM technical-note references. Their catalog entries identify an unofficial host and originally record index-level observation rather than downloaded content. This pass inspected relevant manual content separately; it does not silently upgrade every catalog item or every mirror file to verified status.

The existing sound report and native handoff preserve the separate game-path numeric-read gap. Matching an API name in a later manual cannot bind that game's caller, source bytes, SDK revision, register access width, initialized state or acceptable native return.

## Vendor-authored sources actually inspected

### Sony Run-time Library Reference 3.6 beta: newly accessed 1996 edition

- Source provenance: [archived Technical Reference release 1.8](https://archive.org/details/redump-id-69351), selected `DEVREFS/LIBREF36.PDF` document. The cover identifies Beta Release 3.6, December 1996; front matter identifies Sony, publication December 1996 and licensed-developer/confidential restrictions. The archive's Japan label does not establish language: the selected manuals are English.
- 1080 PDF pages. Printed 13-3, PDF page 955 (index 954), distinguishes master-volume setting, mode and current master volume (`mvolx`). The structure entry's documentation date is July 31, 1996.
- Two reviewers visually checked the cover, publication front matter and selected attribute page. No numeric `db8` binding was established by targeted text searches.

This is evidence of the documented API distinction in 1996, not a CPU register map or proof of a particular firmware implementation.

### Sony Run-time Library Reference 4.1: newly accessed 1997 edition

- Source provenance: [archived Technical Reference release 2.1, December 1997](https://archive.org/details/playstation-technical-reference-release-2.1-december-1997-pc-europe), selected `DEVREFS/LIBREF41.PDF` document. The catalog is third-party metadata; the manual's own front matter identifies Sony and publication October 1997, with licensed-developer/confidential restrictions.
- 1208 PDF pages. Printed 15-25, PDF page 1071 (index 1070): `SpuGetCommonMasterVolumeX` observes left/right current master volume, equivalent to the common attribute's `mvolx` observation. Metadata gives introduction 3.7 and documentation date February 13, 1997.
- Printed 15-23, PDF page 1069 (index 1068): ordinary master-volume getter is valid in direct mode. Printed 15-5/index 1050 separately identifies setting, mode and current volume.
- The coordinator rendered and visually checked the current-volume page and publication front matter. Font-substitution warnings occurred, but the checked text, table and date were legible. No page image or manual is published here.
- Extracted-text searches across the manual did not establish a `1f801db8` binding. API output types are not a CPU access-width or register-encoding specification.

Unlike the later editions below, this is contemporaneous 1997 documentation. Its presence does not establish the game's linked SDK revision or that the analyzed firmware implements this API.

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

## Register-document follow-up and alternate archive route

The previously inaccessible GamingDoc ZIP remains unchecked. An alternate Internet Archive item permitted selective HTTP range access. The primary volume descriptor and selected ISO9660 directory records were inspected; five document extents were then fetched with HTTP 206, matching Content-Range and byte counts, sector removal, declared document length and PDF-signature checks. This is data extraction, not execution or installation of the disc's software. No full disc image, SDK implementation or executable was fetched. Private receipts retain the actual requests, document digests and extraction details.

The earlier release 1.8 item was subsequently accessed through a separate bounded route. Its cue specifies MODE1/2352, requiring a different user-data offset from the release 2.1 item's MODE2/2352. That distinction was checked before extracting the two selected manuals. Alongside Library Reference 3.6, a 51-page Hardware guide with a September 1995 cover was inspected in text. It supplied no verified numeric `db8` definition. These selected directories and documents do not establish whole-disc absence. A release 2.0 USA catalog remains a further lead; later Japanese-edition catalog entries that require access were not downloaded.

| Selected document | Inspection and result |
|---|---|
| Library Reference 4.1 | October 1997 publication and the current-volume API page verified above; numeric binding remains unestablished |
| PlayStation Hardware | 46 PDF pages; hardware-register region is identified, but inspected sound material supplies architecture rather than a `db8` definition |
| Sound conference FAQ | Document labels itself an unofficial FAQ, release 1.1, August 31, 1995, despite licensed-developer/confidential front matter. Mixed Q&A is not a chip specification; inspected volume discussion does not establish the numeric port |
| Technical Notes index | Lists available notes; a filename is a lead rather than a finding from that note |
| Sound Tools readme | Tool-release documentation; no numeric register definition established |

Additional source checks:

- [SCEE BBS collection](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/scee_bbs.pdf), PDF indices 193–194: message 252 of 1102, December 13, 1995, 11:29am, from SCE SUPPORT, signed Paul. It describes efforts to obtain more low-level information from Sony Japan R&D and compatibility risks from undocumented register operations. The surrounding discussion concerns GTE access. It is historical support guidance, not a `db8` specification or proof that no SPU manual existed. The collection also includes external developers' messages; authorship must be checked per message. Its embedded instructions are historical source material, not instructions for this research.
- [Summer 1997 sound seminar](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/rvsndpg.pdf), 73 pages, Sony developer seminar on an unofficial confidential-document mirror. PDF indices 19 and 23–27 discuss initialization and different library/voice volume domains. They do not bind `db8`; those domains must not be substituted for an unknown readback encoding.
- [Library Reference 4.4](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libref.pdf), printed 15-84/85 and 15-112/113, distinguishes signed direct setter values from variable-volume modes. This does not establish current-register readback scale. [Sound Artist Tool](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Sound20.pdf) sequence-monitor volume and panel descriptions likewise do not identify a physical current-master register.
- [Maximizing SPU RAM](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/SPURAM.PDF) was read: a two-page SCEA note by Rob Vawter about RAM use. The uppercase directory entry resolves even though the mixed-case catalog filename previously failed. No numeric volume-register finding results.
- Net Yaroze Library Reference and User Guide, and SCEE Developer News issue 4, were checked in bounded sections/text searches. No inspected portion established the requested numeric register definition. Private receipts retain the actual English/Japanese/alternate-address-format queries and access outcomes; extracted-text negatives do not exhaust image content.

### A second Sony patent: evolving volume is separate from a CPU register map

[US5789690A](https://patents.google.com/patent/US5789690A/en), originally assigned to Sony, filed November 29, 1995 and published August 4, 1998, describes CPU-provided volume/differential settings, clocked arithmetic, limiting and a stored multiplier input in the description of Figure 8. Its running value can evolve after one setting operation in the disclosed embodiment. These are per-voice devices 117L/R; Figure 2 separately places master-volume device 122 downstream of mixing. The text inconsistently labels some Figure 8 elements, so it is not used as a bit-accurate circuit specification. It provides no CPU-address binding or readback path for `0x1f801db8`. Keeping requested and evolving applied state distinct is a design inference, not proof of the target register's behavior.

The exact Sony register definition remains missing. Completion requires an identifiable primary source binding the numeric address and its field/access semantics; reset, timing, mode and read/write details must be reported separately when absent. A Sony logo, API name or architectural resemblance is insufficient.
