# Research provenance and implementation review

The owner requires an independently implemented game and an auditable clean-room process. This research library does not certify that requirement. Testing behavior against a reference does not remove source derivation or establish independent authorship. Existing exposure and source records must be preserved when work is replaced.

## Source boundaries

| Material | Current classification | Implementation disposition |
|---|---|---|
| PSX-SPX community specifications | Restricted-provenance research reference; the upstream notice identifies copied or rephrased confidential Sony material | Not cleared as an implementation source |
| Sony manuals and SDK material | Vendor-source research with its original provenance | Not cleared by public availability or paraphrasing |
| BIOS static analysis | Firmware reverse-engineering observations, with retained source identity | Requires an explicit project review; original prose alone does not establish independent derivation |
| BIOS emulator captures | Observations of the identified firmware inside an identified emulator | Functional evidence only; not physical hardware proof, independent implementation proof or game boot |
| Original host tests and synthetic fixtures | Separately authored instruments whose models, inputs and expected results still need source lineage | Passing tests do not clear the implementation or its oracle |
| Native-project progress reports | Project attestations | Neither independent inspection nor provenance acceptance by this research |

PSX-SPX is credited to Martin “nocash” Korth and its community contributors. Its [upstream source notice](https://github.com/psx-spx/psx-spx.github.io/blob/038d444bf28e8ac1b203667c7155eb80d8b7dec2/docs/README.md) remains authoritative for the source's stated provenance. A local research shelf does not transfer authorship or grant redistribution rights.

## Remediation record

For each affected implementation claim, record the source and exposure history, current consumer, test-design source, expected-result source, independently observed results and the proposed replacement. Separate test authoring from implementation authoring under an agreed project policy. A fresh implementation must have a documented permitted input contract; calling an exposed author or session “fresh” does not erase prior access.

Replace or exclude flagged material where required, retaining the superseded record. A designated independent reviewer must evaluate the replacement and its lineage under the agreed policy before the project clears that item for implementation. Missing policy, exposure records or review remain open gates. No automated flag removal, rewritten summary, emulator pass or source citation grants that clearance.

The research team has asked the development coordinator to reconcile earlier handoffs with this boundary. Delivery of that request is not acknowledgment or completion of an audit. This report establishes a review workflow, not a legal determination or a claim that the current game is clean room.
