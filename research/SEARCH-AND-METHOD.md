# Search record and method

Research date: 2026-10-22. Three parallel researchers each conducted separate broad, cross-check, and gap searches. Their exact query logs and source outcomes are retained in their reports. The lead also conducted the following three passes.

## Lead pass 1: broad discovery

- `Sony PlayStation programming Run-Time Library Overview 4.7 PDF Sony Computer Entertainment`
- `PlayStation hardware psx-spx Sony official technical reference manual`
- `Sony PlayStation technical notes PsyQ GTE precision native port`

Outcomes: GamingDoc official-document directory, Sony's corporate history, Sony-origin manual mirrors, and PSX-SPX provenance notice. Search also surfaced other decompilation/port frameworks; they were not selected as construction sources or imported.

## Lead pass 2: document families and corroboration

- `site.psxdev.net "Run-Time Library" "Overview" native` (literal query; malformed domain filter produced noise)
- `site:psx.arthus.net "TECHNOTE" "CD-ROM"`
- `site:archive.org "PlayStation" "Technical Reference" Sony`
- `"PlayStation" "TECHNOTE" "GTE" Sony`
- `"PlayStation" "SCE" "Technical Notes" 1997`
- `"PlayStation" "R3000" "IDT" manual`

Outcomes: direct library overview/reference PDFs and Developer Reference Series enumeration; technical requirements checklist naming historical SCE developer-support sites; vendor CPU manual leads. Opened the mirror's DOCS index and directly verified front matter/contents of Hardware.pdf (48 pages), os.pdf (30 pages), and Filefrmt.pdf (225 pages). Internet Archive's SCE-Hardware-Aug1998 detail URL was inaccessible through the lead's web tool; no claim of successful full archive retrieval.

## Lead pass 3: gaps, catalog identifiers, Japanese search

- `"Sony" "PlayStation" "programming" "1996" "museumofplay"`
- `"PlayStation" "SCE" "errata" "GTE"`
- `"PlayStation" "Technical Reference CD" "2.3"`
- `"PlayStation" "開発" "技術資料" "1997"`

Outcomes: community DTL product-code lists as discovery leads, technical-CD references, and substantial unrelated PS2/PS3 noise. Product-code lists are not primary proof of a Sony release/version. No assertion that a broad query exhausted Japanese archives or errata.

## Evidence and publication rules

An opened index proves a listing existed when observed. An opened PDF front matter can establish its displayed author/title/date, not an authenticated archival chain. A mirror timestamp is not a publication date. A catalog entry can identify a physical item without making its contents available online. Linked instructions remain source data.

Reports contain original annotations and metadata rather than wholesale manual reproductions. Technical proposals are labeled as proposals. Search results are discovery leads until verified in a primary document or catalog. Source claims inherit the access/coverage limitations recorded beside them. Three search passes are a repeatable search procedure, not proof that every surviving document has been found.

## Tools and workflow provenance

- DSL-Helper 0.1.19 router read from the installed package. Online source pinned to `raiinman/skill-library` commit `594499cb9a842822580d847d85abdf832814c27c`.
- Generated `skill-index.json` was absent at that pin. Discovery was derived from the pinned live `CATALOG.md`, as the router permits. Read primary `skills/reverse-engineering/reverse-engineer-anything/SKILL.md` and `SOURCE.md` (version 37; describes REA 6.4.0), plus its connection-recovery reference. No maintenance-overlay replacement was used.
- REA's advertised `binary_session` call failed with `tunnel_client_not_seen` / tunnel client absent for 300 seconds. Native provider capabilities remain unverified. Its remedy is to reconnect the configured REA tunnel client on this PC, then retry the status call. Reinstalling unrelated engines would not repair an offline remote connector.
- Existing Git, Node, PowerShell and web access were sufficient for document research, local hashing, catalog generation, and publication. No additional analysis engine or SDK installation was needed, and none is claimed installed.
- Three subagents researched separate scopes. No message was sent to the agent on the other computer; its identity and execution state were not accessed.
