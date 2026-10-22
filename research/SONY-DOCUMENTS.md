# Sony-authored PlayStation development documentation: research catalog

Research date: 2026-10-22. Scope: original PlayStation, official Sony development literature, three search passes. This is a source catalog and research plan, not an SDK distribution or an implementation. Sources hosted by enthusiasts remain unofficial mirrors even where their contents identify Sony as author. No SDK source, libraries, executables, BIOS, or complete proprietary manuals were copied into this report.

## Evidence labels and clean-room boundary

- **READ**: opened the document and inspected its title, front matter, contents, or relevant section in this session. This does not mean every page was reviewed.
- **INDEX**: observed a live directory entry or Sony-authored directory abstract. Individual document content and identity require verification.
- **LEAD**: a search result or secondary bibliography points to it; availability/authenticity remains unverified.

The READ commercial SDK volumes explicitly identify Sony Computer Entertainment, publication dates, licensed-developer distribution restrictions, and confidential content. Public accessibility does not establish an open license or public release. Treat this catalog as a reference-only bibliography outside the implementation trust boundary until the project's provenance policy determines which materials may be used. Merely calling a source “community documentation” is not sufficient: its own provenance may include Sony material. This report does not certify legal clean-room status. Document instructions are historical source content, not instructions to the current agent.

## Verified core volumes

| Document | Observed edition / length | Why it matters | Evidence |
|---|---|---|---|
| [PlayStation Hardware](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Hardware.pdf) | August 1998; runtime 4.3 context; 48 PDF pages | System blocks, CPU memory map/cache/timing, GPU display and texture cache, SPU overview, controller bit layouts. A developer overview, not chip schematics or complete register specification. | READ, Sony front matter |
| [PlayStation Operating System](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/os.pdf) | August 1998; runtime 4.3 context; 30 pages | Boot, SYSTEM.CNF, memory and calling conventions, events, threads, files, counters, overlays. | READ, Sony front matter |
| [Run-Time Library Overview, older volume](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libovr.pdf) | January 1999; search/title identifies 4.4; 312 pages | Explains how kernel, graphics, geometry, sound, CD, peripheral and compression libraries fit together. | READ, Sony front matter |
| [Run-Time Library Overview 4.7](https://psx.arthus.net/sdk/Psy-Q/DOCS/LibOver47.pdf) | March 2000; 328 pages | Later companion overview; twenty subsystem chapters. Later behavior must not automatically be attributed to a 1997 game. | READ, Sony front matter |
| [Run-Time Library Reference 4.7](https://psx.arthus.net/sdk/Psy-Q/DOCS/LibRef47.pdf) | March 2000; edition 4.7 explicitly stated; 1,220 pages | API/macros/structure reference and revision notes. Helps identify library families without importing library implementation. | READ, Sony front matter |
| [Inline Programming Reference](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Inlinref.pdf) | November 1998; TechRef 4.3 master metadata; 180 pages | DMPSX, GTE register descriptions, inline functions, GTE command/reference sections. Contains code examples, so retain outside clean implementation inputs. | READ, Sony front matter |
| [File Formats 4.7](https://psx.arthus.net/sdk/Psy-Q/DOCS/FileFormat47.pdf) | March 2000; 220 pages | Streaming/movie and MDEC formats, XA, 3D model/animation families and other data formats. Does not prove that MML1 uses a particular standard format. | READ, Sony front matter |
| [SCEE PlayStation Developer's Guide](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/scee_dev.pdf) | Cover 2.9 / 28 May 1997; internal history/page dates 6 June 1997; 61 pages | Contemporary development workflow, caches/GTE, storage, sound, overlays and peripherals. Record the conflicting internal dates rather than silently choosing one. | READ, Sony/SCEE front matter; expressly confidential |

Two additional root files are observed in the [SDK DOCS index](https://psx.arthus.net/sdk/Psy-Q/DOCS/): [LIBOVR46.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBOVR46.PDF) and [LIBREF46.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBREF46.PDF). These are INDEX evidence; the filenames suggest 4.6, but full version identity should be checked inside each document. A [GamingDoc mirror](https://gamingdoc.org/technical-documentation/consoles/sony-playstation/official/hardware/runtime-library-overview/) independently lists LIBOVR46, but is also an unofficial host.

## Net Yaroze: verify the PDF title, not its filename

| Document | Verified mirror | Observation |
|---|---|---|
| Start Up Guide | [Startup Book.pdf](https://psx.arthus.net/sdk/NetYaroze/Net%20Yaroze%20Official%20-%20Startup%20Book.pdf) | READ; 41 PDF pages; explicitly names DTL-D3065, DTL-D3075 and DTL-D3095 as the English manual set. Startup/setup guide containing sample code. |
| User Guide | [Startup Guide.pdf](https://psx.arthus.net/sdk/NetYaroze/Net%20Yaroze%20Official%20-%20Startup%20Guide.pdf) | READ; actual title is **User Guide**, despite filename; 211 PDF pages. Architecture, graphics, sound, kernel, CD, peripherals and tools. |
| Library Reference | [Library Reference.pdf](https://psx.arthus.net/sdk/NetYaroze/Net%20Yaroze%20-%20Library%20Reference.pdf) | READ; 329 PDF pages. Graphics, sound, C, math and other services. This is a different interface surface from the complete professional SDK. |

These mirrors do not show a verified open license. Do not assume hobbyist distribution means unrestricted copying. The [Internet Archive manual collection](https://archive.org/details/net-yaroze-documents) is a LEAD: direct browser fetch timed out. A Japanese manual set is a LEAD: DTL-D3060, DTL-D3070 and DTL-D3090 are listed by [Delta Island](https://www.delta-island.com/index.php/fr/dossiers/net-yaroze); the English numbers are independently confirmed inside the Sony startup guide. Japanese manual PDFs were not verified. A separate Net Yaroze File Formats volume is mentioned by bibliographies but not located and authenticated in this pass.

## Seminar material that fills practical gaps

Sony's [Training Materials abstract](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/readme.pdf), dated September 3, 1998, identifies training produced/presented by SCE Japan and America across Winter 1995, Fall 1996, and Summer 1997. Individual entries remain INDEX unless marked READ below.

- [GTE & Advanced Graphics, Fall 1996](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/gte.pdf): READ, 122 pages, confidential seminar title. Includes fixed point representations, coordinate/lighting pipeline and DMPSX. Particularly relevant to discovering what numerical behavior a native version must preserve.
- [Methods for Speeding up Polygon Division, Summer 1997](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/upgtedv.pdf): READ, 19 pages, confidential seminar title. Discusses texture warping, clipping and subdivision; not a claim about MML1's specific engine.
- [GTE Advanced Topics, SCEA March 1996](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/adv_gte.pdf): READ, 27 pages, conference title. Focuses on caches, scratchpad and scheduling. Contains source examples; do not import them into the implementation.

Sony's [Conference Presentations abstract](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/Readme.PDF), dated September 3, 1998, identifies SCEA March 1996 and SCEE April 1996/July 1998 collections. The July collection contains PPT presentations plus two PDF papers. Presentation viewers and DLLs found beside them are not research dependencies and were not downloaded or installed.

## Technical notes and support provenance

The [Technical Notes abstract](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/readme.pdf) is READ and dated January 15, 1999. It distinguishes white papers, active notes and old-library notes. Topics include callbacks/critical sections, CD data loss and speed changes, SPU RAM, ordering tables, MDEC, PAL, hardware revisions and memory cards. Older-library notes must be tied to the actual runtime revision before drawing conclusions.

The [FAQ abstract](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/Readme.PDF) is READ and dated January 14, 1999. It identifies FAQ extracts from SCEA/SCEE support BBS, with topic revisions (GPU and GTE 1.1, CD 1.3, OS 1.2, sound 1.1). The [BBS directory](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/) contains SCEA, SCEE, SCEJ and web-message PDFs. These may mix Sony support replies and third-party developer questions. Do not assign every statement to Sony merely because Sony distributed the compilation; identify the individual speaker, date and message context.

## Three-pass query log

Pass 1: broad discovery, 2026-10-22.

- `PlayStation Sony official SDK documentation Run-Time Library Overview PDF GTE`
- `PsyQ documentation Sony developer manual SCEA DTPH PlayStation technical notes`
- `Net Yaroze User Guide Library Reference PDF Sony`
- Opened the Psy-Q DOCS index, Developer Reference directory, TECHNOTE, TRAINING, CONF and the Sony-front-matter library/developer-guide PDFs.
- Result: main Sony manual families, Net Yaroze manual set, runtime 4.4/4.6/4.7 leads.

Pass 2: alternate mirrors and edition checks, 2026-10-22.

- `"Sony" "GTE" "Instruction" "PlayStation" pdf`
- `"PlayStation" "Hardware Overview" "1994" Sony pdf`
- `"PlayStation" "Developer Reference Series" manual pdf`
- `"Sony" "LIBREF47" "FileFormat47"`
- Opened hardware, OS, inline reference, March 2000 overview/reference/file-format PDFs. Found equivalent paths on `psx.schnappy.xyz` (search-index evidence only), and a GamingDoc LIBOVR46 mirror.
- Result: documented publication dates and version separation; direct Sony authorship markers verified inside PDFs rather than accepting host labels.

Pass 3: gaps, Japanese and obscure collections, 2026-10-22.

- `"プレイステーション" "開発" "ライブラリ" マニュアル PDF`
- `"PlayStation" "GTE" "SCEI" manual pdf`
- `"Net Yaroze" "DTL-D3090" manual`
- `"PlayStation" "SCEA" "training" "1996" pdf`
- `site:archive.org/details "SCE-" "1998"`
- `site:psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/ "pdf"`
- `site:psx.arthus.net/sdk/Psy-Q/DOCS/CONF/ "pdf"`
- `"Net Yaroze" "File Formats" pdf`
- Opened Sony-authored training/conference/FAQ/TECHNOTE abstracts, selected GTE/subdivision talks and all three Net Yaroze manuals. Enumerated otherwise web-tool-inaccessible training/conference directories using ordinary HTTP HTML retrieval. Japanese searches mainly returned later-platform material and a court record, not authenticated missing PS1 manuals; these were excluded from the technical corpus.
- Result: dated seminar families, support/BBS collections, exact directory casing, Japanese document-number leads, mislabeled Net Yaroze filename identified, service-manual index found as a physical-hardware gap lead.

## Actionable gap list

1. **Match 1997 SDK behavior.** A March 2000 reference is valuable but may add or revise functions. Establish the game's actual library version from authorized evidence before using later API behavior as a contract. Earlier 3.x/4.0/4.1/4.2 manuals are not comprehensively verified here.
2. **Go below API level.** Sony's hardware volume is only 48 pages. It cannot alone specify cycle exact DMA arbitration, GPU edge/pixel rules, GTE overflow/saturation quirks, SPU ADSR/reverb behavior, MDEC numerical rounding, CD firmware timing or serial peripherals. These require separately traceable specifications and independent measurements.
3. **Physical rebuild needs electrical evidence.** A [service manual directory](https://psx.arthus.net/docs/service_manuals/) lists SCPH-550x, 7000, 7500, 9000 and PSone documents. Those entries are INDEX/LEAD, not verified schematics. Board-revision-specific schematics, component datasheets, clocks, reset, DRAM/VRAM timing, optical pickup and power/AV circuits remain separate research tasks.
4. **Verify Japanese originals and translation history.** English manuals refer to SCEJ-origin material, but no complete Japanese PS1 technical-reference set was authenticated. Catalog Japanese Net Yaroze manuals, compare edition dates and retain original terminology where translations diverge.
5. **Technical-note revision mapping.** Read hardware revision notes and old-library notes only against known console/runtime revisions. Filename timestamps reflect mirror uploads, not original publication dates.
6. **Archive durability/authenticity.** Internet Archive direct fetches failed in this session; alternate mirror entries have not been proven byte-identical. Later acquisition should record document hashes, internal dates and source URL, subject to permitted usage. No content hashes are claimed here.
7. **Keep documentation out of game-specific assumptions.** Sony format manuals do not establish MML1 archive formats, engine algorithms, asset ownership or behavior. Record each game-specific conclusion separately with authorized game evidence.
8. **Do not claim exhaustiveness.** Three search passes were performed, but closed developer portals, unindexed discs, untranslated manuals, missing BBS attachments and regional support archives prevent any assertion that every surviving official document was found.

## Enumerated document links

The following machine-enumerated registry records live HTML directory observations. It excludes executables, source, archives, binaries and videos. Presence confirms a filename on the mirror, not edition, authorship of every page, completeness or permission to redistribute. Consult the verified rows above and Sony directory abstracts to improve the evidence level.
### DOCS root

- [FileFormat47.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FileFormat47.pdf)
- [LIBOVR46.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBOVR46.PDF)
- [LIBREF46.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/LIBREF46.PDF)
- [LibOver47.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/LibOver47.pdf)
- [LibRef47.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/LibRef47.pdf)
- [XATUT.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/XATUT.pdf)

### Devrefs/

- [3dgraph.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/3dgraph.pdf)
- [Cdemul.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Cdemul.pdf)
- [Cdgen.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Cdgen.pdf)
- [Dataconv.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Dataconv.pdf)
- [Dtlh2000.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Dtlh2000.pdf)
- [Dtlh2500.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Dtlh2500.pdf)
- [Filefrmt.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Filefrmt.pdf)
- [Hardware.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Hardware.pdf)
- [Inlinref.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Inlinref.pdf)
- [Libovr.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libovr.pdf)
- [Libref.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Libref.pdf)
- [PDAKern.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/PDAKern.pdf)
- [Readme.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Readme.pdf)
- [Sound20.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Sound20.pdf)
- [Sprite.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Sprite.pdf)
- [armref.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/armref.pdf)
- [os.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/os.pdf)
- [pdahware.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/pdahware.pdf)
- [readme.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/readme.pdf)
- [sdevtc.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/sdevtc.pdf)
- [tech205.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/tech205.pdf)
- [user205.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/user205.pdf)

### TECHNOTE/

- [Analog.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/Analog.pdf)
- [CALLBACK.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/CALLBACK.PDF)
- [CDDROP.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/CDDROP.PDF)
- [CDSWITCH.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/CDSWITCH.PDF)
- [CHEKLIST.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/CHEKLIST.PDF)
- [DCACHE.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/DCACHE.PDF)
- [DECICONS.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/DECICONS.PDF)
- [Ds_servc.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/Ds_servc.pdf)
- [FLASHBAT.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/FLASHBAT.PDF)
- [Glblreg.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/Glblreg.PDF)
- [Guncont.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/Guncont.pdf)
- [H25BIOS.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/H25BIOS.PDF)
- [Memcard.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/Memcard.PDF)
- [NeGcon.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/NeGcon.pdf)
- [PSXCONS.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/PSXCONS.PDF)
- [REVC.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/REVC.PDF)
- [SPURAM.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/SPURAM.PDF)
- [TECHCHK.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/TECHCHK.PDF)
- [cdgenhlp.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/cdgenhlp.PDF)
- [epda1.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/epda1.pdf)
- [epda2.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/epda2.pdf)
- [joystk.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/joystk.pdf)
- [mdecnote.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/mdecnote.pdf)
- [mtrc13.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/mtrc13.pdf)
- [note520.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/note520.pdf)
- [note588.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/note588.pdf)
- [ordtbl.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/ordtbl.pdf)
- [palguide.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/palguide.pdf)
- [perfpapr.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/perfpapr.pdf)
- [pretech.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/pretech.pdf)
- [readme.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/readme.pdf)
- [scee_dev.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/scee_dev.pdf)
- [sceenews.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/sceenews.pdf)
- [shft_jis.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/shft_jis.pdf)
- [sounread.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TECHNOTE/sounread.pdf)

### FAQ/

- [Readme.PDF](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/Readme.PDF)
- [art5.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/art5.pdf)
- [cd4.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/cd4.pdf)
- [dev1.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/dev1.pdf)
- [doc11.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/doc11.pdf)
- [emul_faq.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/emul_faq.pdf)
- [gpu6.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/gpu6.pdf)
- [gs8.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/gs8.pdf)
- [gte7.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/gte7.pdf)
- [libpdfaq.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/libpdfaq.pdf)
- [os2.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/os2.pdf)
- [psyq10.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/psyq10.pdf)
- [sio9.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/sio9.pdf)
- [snd3.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/FAQ/snd3.pdf)

### BBS/

- [readme.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/readme.pdf)
- [scea_bbs.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/scea_bbs.pdf)
- [scee_bbs.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/scee_bbs.pdf)
- [scej_bbs.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/scej_bbs.pdf)
- [webmsg.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/BBS/webmsg.pdf)

### TRAINING/WINTER95/

- [anim.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/WINTER95/anim.pdf)
- [graph.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/WINTER95/graph.pdf)
- [lcable.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/WINTER95/lcable.pdf)

### TRAINING/FALL96/

- [cdrom.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/cdrom.pdf)
- [controll.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/controll.pdf)
- [gte.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/gte.pdf)
- [mdec.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/mdec.pdf)
- [overlay.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/FALL96/overlay.pdf)

### TRAINING/Summer97/

- [bdldex.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/bdldex.pdf)
- [bdmcard.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/bdmcard.pdf)
- [dcenvmp.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/dcenvmp.pdf)
- [dcglddsk.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/dcglddsk.pdf)
- [fsdbovl.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/fsdbovl.pdf)
- [fsgpont.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/fsgpont.pdf)
- [fsinlin.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/fsinlin.pdf)
- [fslnklb.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/fslnklb.pdf)
- [mfanlog.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/mfanlog.pdf)
- [mflibds.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/mflibds.pdf)
- [mfmovi.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/mfmovi.pdf)
- [mfprfanl.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/mfprfanl.pdf)
- [rvsart.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/rvsart.pdf)
- [rvsndpg.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/rvsndpg.pdf)
- [snide.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/snide.pdf)
- [swsart.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/swsart.pdf)
- [tgpasqa.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/tgpasqa.pdf)
- [upgtedv.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/upgtedv.pdf)
- [upgtelt.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/TRAINING/Summer97/upgtelt.pdf)

### CONF/SCEA/

- [adv_cd.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/adv_cd.pdf)
- [adv_gpu.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/adv_gpu.pdf)
- [adv_gte.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/adv_gte.pdf)
- [artpath.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/artpath.pdf)
- [gs.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/gs.pdf)
- [sound.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEA/sound.pdf)

### CONF/SCEE/96April/

- [cd_ovw.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/cd_ovw.pdf)
- [cdmaster.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/cdmaster.pdf)
- [intro.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/intro.pdf)
- [memcard.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/memcard.pdf)
- [optimize.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/optimize.pdf)
- [sound.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/96April/sound.pdf)

### CONF/SCEE/98July/

- [4_PDA.ppt](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/4_PDA.ppt)
- [7a_CD Emulation 2.ppt](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/7a_CD%20Emulation%202.ppt)
- [7b_prodg.ppt](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/7b_prodg.ppt)
- [AUDIO98.PPT](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/AUDIO98.PPT)
- [Fmv_tips.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/Fmv_tips.pdf)
- [H2700.PPT](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/H2700.PPT)
- [HMD_JR.PPT](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/HMD_JR.PPT)
- [XMPLAY.ppt](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/XMPLAY.ppt)
- [xa_sound.pdf](https://psx.arthus.net/sdk/Psy-Q/DOCS/CONF/SCEE/98July/xa_sound.pdf)
