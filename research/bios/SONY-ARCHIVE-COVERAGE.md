# Sony Technical Reference archive coverage for `0x1f801db8`

This ledger tracks the specific archives and document sets investigated. It is not a catalog of every Sony archive ever produced. The exact numeric register definition remains unresolved. Related API, architecture and tool descriptions are kept separate from an address binding.

## Archive inventory

| Archive or revision | Access and inspected scope | Result and remaining boundary |
|---|---|---|
| [Release 1.8](https://archive.org/details/redump-id-69351) | Validated selective reads of directories and two manuals: Hardware and Library Reference 3.6 beta | Current-volume attribute documented in 1996; no numeric binding established. Selected manuals are English despite the item region label |
| [Release 2.0 USA](https://archive.org/details/redump-id-71992) | June 1997 catalog; wider text scan of 116 root-documentation PDFs, 8,499 pages, following an initial 19-document depth pass | No verified numeric binding in this scoped text scan; image and excluded-directory limits below |
| [Release 2.1 Europe](https://archive.org/details/playstation-technical-reference-release-2.1-december-1997-pc-europe) | Validated selective reads of five documents, including October 1997 Library Reference 4.1 | Current-volume getter documented; numeric map remains unresolved |
| [Release 2.3 alternate mirror catalog](https://psx.arthus.net/docs/) | September 1998 catalog inside the publicly reachable compressed container; all 409 PDF members text-scanned, 9,555 pages, following a 24-document depth pass | No numeric binding established; selected images and presentations inspected separately, with remaining visual limits below |
| Japanese 4.3, 4.4 and 4.6 entries | Public metadata on the [larger archive catalog](https://archive.org/details/IBM-PCCompatibleDevelopmentSoftwareForPlayStation1-Redump.org) marks each corresponding file private and the item access-restricted | Contents uninspected; no file download attempted. These versions are not equivalent to the separately accessed English manual revisions |

The selected-document passes above are distinct from subsequent wider text scans. A negative extracted-text result is not a visual search of every diagram, a whole-disc absence proof, or evidence that Sony never wrote the specification.

## Wider scans and image limits

For release 2.3, all 409 PDF members in the container were extracted as documents and text-searched: 9,555 pages, zero PDF parse failures. Contiguous and punctuation/whitespace-normalized searches covered the full `1f801db8/1f801dba` pair, the candidate base, standalone `1db8/1dba`, and selected `1b8/1ba` offset forms. No numeric candidate emerged. The `MVOLXL/MVOLXR` labels appeared as API arguments on Library Reference printed 15-25 / PDF index 1098; that is not a register map.

There are 478 pages with fewer than 100 extracted text characters and 1,150 pages containing raster images. These categories include ordinary blank/title pages and illustrations; they are not counts of proven missing text. A one-page entirely low-text joystick document was visually identified as an analog-joystick parts diagram. Selected sound-tool panels, conference volume slides and the four-page Hardware sound chapter were separately rendered and reviewed without finding the numeric definition. The image-bearing set has not received exhaustive visual review; vector diagrams can also exist without raster-image objects.

The non-PDF index has no DOC, RTF, HTML, HTM, HLP or CHM members. Ten TXT members are listed under viewer/document-system directories; their contents were not extracted. All seven conference PowerPoint files were subsequently text-scanned as nonexecuting documentation data: 806 text atoms and zero bounded-record parse failures. No target address, selected offset or `MVOLXL/MVOLXR` match emerged. Authorship is mixed, including an SN Systems presentation, rather than uniformly Sony. This is not a rendered-slide or complete presentation-structure proof; presentation images remain a gap.

Release 2.0's wider root-documentation pass completed 116 PDFs / 8,499 pages, with zero document-fetch or page-parse errors. The same numeric forms produced no candidate; the label hits were the known current-getter API arguments. Its 67 short-text pages use a stricter threshold of fewer than 20 extracted characters, unlike the release 2.3 threshold above. It also flags 1,176 pages with direct image objects; nested image objects and all visual content were not exhaustively enumerated or reviewed.

The release 2.0 directory walk discovered 338 PDF paths and selected 116 under the root documentation branches. The 222 excluded PDF paths were in program/graphics SDK, sample, viewer and document-system branches. Four HTTP 500 directory-read gaps were outside the selected scope and remain access gaps, not empty-directory results. No whole-disc absence claim follows. Broader reviews of the previously selected release 1.8 and 2.1 document sets continue separately.

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
