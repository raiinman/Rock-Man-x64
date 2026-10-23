# Sony Technical Reference archive coverage for `0x1f801db8`

This ledger tracks the specific archives and document sets investigated. It is not a catalog of every Sony archive ever produced. The exact numeric register definition remains unresolved. Related API, architecture and tool descriptions are kept separate from an address binding.

## Archive inventory

| Archive or revision | Access and inspected scope | Result and remaining boundary |
|---|---|---|
| [Release 1.8](https://archive.org/details/redump-id-69351) | Wider root-documentation pass: 104 PDFs, 7,164 pages, following the two-manual depth pass | No verified numeric binding; selected manuals are English despite the item region label |
| [Release 2.0 USA](https://archive.org/details/redump-id-71992) | June 1997 catalog; wider text scan of 116 root-documentation PDFs, 8,499 pages, following an initial 19-document depth pass | No verified numeric binding in this scoped text scan; image and excluded-directory limits below |
| [Release 2.1 Europe](https://archive.org/details/playstation-technical-reference-release-2.1-december-1997-pc-europe) | Wider root-documentation pass: 115 PDFs, 7,897 pages, from 118 selected entries, following the five-document depth pass | Three form-PDF fetch gaps; no verified numeric binding |
| [Release 2.3 alternate mirror catalog](https://psx.arthus.net/docs/) | September 1998 catalog inside the publicly reachable compressed container; all 409 PDF members text-scanned, 9,555 pages, following a 24-document depth pass | No numeric binding established; selected images and presentations inspected separately, with remaining visual limits below |
| Japanese 4.3, 4.4 and 4.6 entries | Public metadata on the [larger archive catalog](https://archive.org/details/IBM-PCCompatibleDevelopmentSoftwareForPlayStation1-Redump.org) marks each corresponding file private. Ordinary canonical download GETs were attempted for all three and each returned HTTP 401 | No payload obtained. Public Wayback and independent-mirror searches described below have not yielded these three archives |

The selected-document passes above are distinct from subsequent wider text scans. A negative extracted-text result is not a visual search of every diagram, a whole-disc absence proof, or evidence that Sony never wrote the specification.

## Wider scans and image limits

For release 2.3, all 409 PDF members in the container were extracted as documents and text-searched: 9,555 pages, zero PDF parse failures. Contiguous and punctuation/whitespace-normalized searches covered the full `1f801db8/1f801dba` pair, the candidate base, standalone `1db8/1dba`, and selected `1b8/1ba` offset forms. No numeric candidate emerged. The `MVOLXL/MVOLXR` labels appeared as API arguments on Library Reference printed 15-25 / PDF index 1098; that is not a register map.

There are 478 pages with fewer than 100 extracted text characters and 1,150 pages containing raster images. These categories include ordinary blank/title pages and illustrations; they are not counts of proven missing text. A one-page entirely low-text joystick document was visually identified as an analog-joystick parts diagram. Selected sound-tool panels, conference volume slides and the four-page Hardware sound chapter were separately rendered and reviewed without finding the numeric definition. The image-bearing set has not received exhaustive visual review; vector diagrams can also exist without raster-image objects.

The non-PDF index has no DOC, RTF, HTML, HTM, HLP or CHM members. Ten TXT members are listed under viewer/document-system directories; their contents were not extracted. All seven conference PowerPoint files were subsequently text-scanned as nonexecuting documentation data: 806 text atoms and zero bounded-record parse failures. No target address, selected offset or `MVOLXL/MVOLXR` match emerged. Authorship is mixed, including an SN Systems presentation, rather than uniformly Sony. Two sound decks subsequently received the separate active-slide and visual review below; the other five presentations retain visual gaps.

Release 2.0's wider root-documentation pass completed 116 PDFs / 8,499 pages, with zero document-fetch or page-parse errors. The same numeric forms produced no candidate; the label hits were the known current-getter API arguments. Its 67 short-text pages use a stricter threshold of fewer than 20 extracted characters, unlike the release 2.3 threshold above. It also flags 1,176 pages with direct image objects; nested image objects and all visual content were not exhaustively enumerated or reviewed.

The release 2.0 directory walk discovered 338 PDF paths and selected 116 under the root documentation branches. The 222 excluded PDF paths were in program/graphics SDK, sample, viewer and document-system branches. Four HTTP 500 directory-read gaps were outside the selected scope and remain access gaps, not empty-directory results. No whole-disc absence claim follows.

Release 1.8's widened pass read 104 selected PDFs / 7,164 pages, excluding one sample manual. Six initial FAQ fetch failures were recovered through a public metadata-listed storage host; no final selected-document fetch or parse gaps remained. The pass flags 69 pages below 20 extracted characters and 1,021 with direct image objects. A nonexecuting text scan of the one unpaired technical-note DOC identified a November 1996 technical requirements checklist, without a target candidate; this was not a rendered DOC review.

Release 2.1's widened pass read 115 PDFs / 7,897 pages. Three selected form PDFs returned HTTP 500: two fault-database forms and one fault-report form. There were no selected directory or retained-PDF parse errors. It flags 378 pages below 100 extracted characters and 1,056 with raster images. Only the known Library Reference API labels appeared; no verified numeric candidate emerged. These flags do not count proven missing text.

Cold rechecks of releases 1.8, 2.0 and 2.1 with pypdf and FontTools retained the negative numeric result without parser warnings. Release 2.3 also received an independent pypdf / FontTools check of all 409 PDFs / 9,555 pages, alongside the original MuPDF extraction. It produced no document/page exceptions or Python warnings, but logged object-stream warnings for two tool-manual PDFs. It counted 481 short-text pages rather than MuPDF's 478. Its 24 normalized `01BA` string matches were inspected and came from checklist glyph/text sequences, not register offsets. Thus the combined conclusion is no verified numeric candidate, rather than no string match from every extractor. Neither decoder check replaces image review.

A separate retained-document scan closed the bare-hex-token gap: 654 distinct PDF digests / 27,327 pages across these four archive scopes, with no document/page extraction errors. Standalone `1B8/1BA/DB8/DBA` tokens, including optional `0x`, leading zeros and trailing `h`, produced zero matches. Seventeen positive/negative pattern checks passed. This tests extracted tokens only; it does not inspect image-only tables or prove that an unknown table uses those offset conventions.

## Selected image-text follow-up

A separate OCR pass completed 218 selected pages across ten release 2.3 sound/hardware PDFs, with zero processing errors. Selection used the union of retained low-text and image-page flags in filename-matched sound/hardware documents. Source digests and page indices were retained. A scope audit caught three PDFs stored under a different private extraction root; their digests were verified and their five selected pages included before completion.

RapidOCR with CPU inference searched for the full address pair, selected short forms and current-volume labels; no candidate emerged. A separate search of all cached recognized rows for standalone bare hex offsets also produced no matches. The already visually checked SPU2 current-volume page served as a positive OCR control and yielded its labels; that control is not PS1 register evidence. OCR errors remain possible, and a negative result is not a visual absence proof.

This closes the selected PDF image-text pass, not all archive images. Filename selection excludes other manuals, vector graphics can evade image flags, and presentation images require separate review.

## Sound-presentation graphics review

The retained July 1998 conference decks `AUDIO98.PPT` and `XMPLAY.ppt` were inspected independently by two research agents, then exported through LibreOffice and visually reviewed across all 23 and 27 slides respectively. Binary current-edit/persist-directory decoding independently resolved those active-slide counts and order, avoiding reliance on concatenated text from older saves. Source SHA-256 digests are `d3c9d82a0dd4e1ddfcddf8a2b10bf45d3fd1b9d585ee670c2ac362c4e73c0317` and `b490740c849d5aa5bd55bda96a4e5c5e6b7532df39093c0c760d38f262ffa99e`.

Each entire Pictures stream contains four PNG resources, all extracted, verified and visually inspected: conference branding, Sony/PlayStation logos and a registered-mark symbol. No embedded metafile or register-table image was found in those streams. AUDIO98's picture references were resolved to its masters. All 50 exported slides were separately inspected for content drawn outside embedded pictures; no target address, register map or numeric DB8 definition appeared. The exported text search likewise produced no selected address/offset/current-label candidate.

AUDIO98's zero-based slides 1–4 distinguish direct settings, hardware volume ramps and voice-volume observation. Slide 4 describes the voice getter with an `X` suffix as observing actual volume, but the lower stopping-example text names the ordinary getter. That inconsistency is preserved; no correction or hardware formula is inferred. Its displayed voice-current range does not establish master-register encoding. Slides 7 and 11 discuss approximate update/queue behavior in voice-status and key-on/off contexts; those statements do not establish DB8 readback cadence. XMPLAY's volume discussion concerns tracker channels, samples and player APIs, without a master-register binding.

The cover and branding attribute AUDIO98 to Rob Vawter, SCEA; the decks also carry SCEE Technology Group conference styling. These are attribution observations on third-party-hosted copies. Initial renderer attempts produced no PDFs, including a nonzero process result; successful later exports were checked for actual PDF presence, page counts and content. Body text was legible in the reviewed export; a small trademark mark touches the page edge. This is a static LibreOffice rendering, without validation against original PowerPoint, animations, hidden content or speaker delivery. Source files, extracted images, rendered PDFs and raw reports remain private. Other presentation graphics and the inaccessible Japanese revisions remain separate gaps.

## User-supplied assembly repository lead

The [playstationAssembly repository](https://github.com/micklemacklemore/playstationAssembly/tree/ad4b36aa8ece040ce5889ea69847f82d8487081d) was checked at commit `ad4b36aa8ece040ce5889ea69847f82d8487081d`. Its complete, untruncated tree has five exercise directories and 13 text files. All 13 files were fetched as inert text and checked against Git blob identities: 33,550 bytes / 1,132 lines. Nothing was built or executed.

The exercises cover elementary MIPS arithmetic, GPU rectangles, subroutines and input/timers. No SPU include file, register catalog or Sony manual occurs in this tree. Full-address, short-offset, current-volume-label and SPU-term searches produced no target reference. Selected exercises contain the general I/O base literal, but the checked text lacks the relevant SPU offsets; this is a bounded source-text result, not a runtime address proof.

The README points to community memory-map documentation, tutorials, assembly examples and MIPS books. Those are source-discovery links, not Sony-authored numeric register definitions. Linked repositories and example code were not imported as native-port construction input. This repository does not resolve the Sony DB8 documentation gap in its checked revision. The check covers the pinned current tree; history, other branches, issues, forks and external documents are outside this result.

## Wayback and independent-copy checks

Following the actual 401 download responses, public Wayback CDX queries for the three exact Internet Archive file URLs and their item page returned HTTP 403. Wayback availability queries returned HTTP 429 and were not repeatedly retried. These are query-access failures, not evidence that captures do not exist.

Two historical mirror indexes were actually retrieved with HTTP 200: [Arthus, November 24, 2020](https://web.archive.org/web/20201124063005id_/http://psx.arthus.net/docs/) and [Schnappy, October 1, 2022](https://web.archive.org/web/20221001025752id_/http://psx.schnappy.xyz/docs/). Both linked the already inspected September 1998 release 2.3 container; neither supplied a link to the sought Japanese 4.3/4.4/4.6 archives. A [December 7, 2021 library-manual capture](https://web.archive.org/web/20211207003841id_/https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBREF46.PDF) returned HTTP 200 and a PDF prefix, but explicitly warned that Wayback content was truncated by length: 1,048,576 bytes received against archived crawler metadata of 4,591,901 bytes. That is an incomplete payload, not a successful full-manual retrieval or evidence of the Japanese disc's identity.

A [September 25, 2022 capture of that manual](https://web.archive.org/web/20220925062633id_/https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBREF46.PDF) subsequently yielded a complete English Library Reference 4.6: 4,591,901 bytes, matching Content-Length, PDF signature and terminal EOF, SHA-256 `fbe6479257fa4668b874fe356bf92f7d7d45d7900ec92d64a2974cff9e2590d7`. Its rendered front matter identifies September 1999; 1,220 pages parsed. The current-master-volume getter appears at printed 15-25 / PDF index 1003, also rendered and inspected. The full extracted-text pass produced no verified numeric register candidate; 64 broader normalized token matches were reviewed and rejected. Twenty-seven pages had fewer than 100 extracted characters; exhaustive visual review is not claimed. This is an additional retained manual with already familiar API distinctions, not recovery of the Japanese 4.6 Technical Reference disc.

Internet searches used the exact archive titles, DTL-D2340/D2350/D2360 identifiers, English revision terms and Japanese technical-reference terms. No independently downloadable copy of those three archives was obtained in these checks. Sony's mirrored [DTL-H2500/H2700 manual](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Dtlh2500.pdf) lists DTL-D2340 as the Technical Reference 4.3 document CD separately from DTL-S2340, the runtime-library CD. This helps identify the requested media; it does not provide its contents or the target register definition. English runtime-library revision labels are not proof of identity with Japanese Technical Reference discs.

A later chip-document search found [third-party catalog references](https://www.dl7avf.info/katalog/quellen.html) to Sony Semiconductor Europe Data Books 96.6 and 96.11, but no downloadable data-book document or verified coverage of the relevant SPU parts. The linked alphabetic part-index page returned 404. This remains a catalog lead, not a Sony register specification, and the access failure does not prove that such documentation never existed.

## New primary evidence from release 2.0

Library Reference 4.0 identifies publication June 1997. Printed 13-24, PDF index 1105, describes the separate left/right current-master-volume getter, introduced in 3.7 with documentation date February 13, 1997. Its relationship to the common current-volume attribute is explicit. This extends the documented getter chronology beyond the October edition; it does not bind `db8` or identify MML1's library revision. Two reviewers checked the rendered publication and getter pages.

A Sony-branded beginner sound presentation under `TRAINING/WINTER95` describes fixed, linear and exponential master-volume variation at slide index 23. The folder label is retained as location metadata, not independent publication-date proof. The diagram is qualitative: no register address, bit width, readback scale or calibrated update timing is established. Both reviewers inspected the rendered slide.

See [primary-source details](SOUND-PRIMARY-SOURCES.md) for earlier editions, exact pages and provenance restrictions. The archived manuals are third-party-hosted copies carrying Sony attribution and licensed-developer/confidential front matter; successful transfer checks do not authenticate their origin or grant redistribution rights.

## Tool and later-platform leads

Sony's August 1998 [SDevTC manual](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/sdevtc.pdf) describes its Registers Pane as CPU-register display, printed 16-25 / PDF index 194. The pane is therefore not evidence of an SPU register definition. Development-board and performance-analyzer manuals were checked in bounded text sections without establishing the sought map.

The [Sony SPU2 Overview manual](https://github.com/ninjadynamics/PS2Docs/blob/main/SPU2_Overview_Manual.pdf), version 6.0, April 2002, is a separate platform reference on an unofficial mirror. Page 67 / PDF index 66 describes `MVOLXL/MVOLXR`, a 16-bit value with format notation `int 1:0:15`, and updates per `Ts` outside constant mode. Page 35 separates this observation from the programmed master-volume controls. The current-value page was rendered and inspected. No explicit PS1 compatibility binding or `0x1f801db8` definition was established in this manual. Its format and timing must not be transferred to PS1 by name resemblance.

## Access checks and publication boundary

Raw-disc access validates the cue layout, sector mode and user-data offset before reading documents. HTTP 206 status, exact Content-Range, bounded response length, declared document length, PDF signature and document digest are retained privately. Release 1.8 uses a different sector layout from releases 2.0 and 2.1.

Release 2.3 required a different route: the compressed container was retained privately, its index inspected, and all PDF members plus selected presentations extracted as documentation data. No SDK library, header, implementation source file or executable was extracted or executed. Archive bytes, manual copies, renders, raw text, scripts and complete private receipts are excluded from GitHub.

The next useful result is an identifiable Sony table, description or documented base-plus-offset relationship binding the target address. Any field, access, mode, reset and timing claims then need separate support. The [focused boundary report](DB8-BOUNDARY.md) tracks those unresolved claims and the separate native-port evidence.
