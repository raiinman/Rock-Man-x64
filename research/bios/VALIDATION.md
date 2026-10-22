# Validation and publication boundary

2026-10-22, initial BIOS findings batch. Validation concerns the research documentation and retained private analysis, not game execution or hardware conformance.

- Every cited `ev_` identifier was resolved against retained REA records, and its subject digest was checked against the stated original-ROM or derived-kernel profile. The index is generated from actual record metadata, with source content excluded.
- Relative Markdown targets were checked for existence. External links were checked for URL syntax; this check does not authenticate every external document. Selected manufacturer, Sony-origin and Ghidra references were separately opened during research.
- Changed publication files were reviewed as original Markdown prose and metadata. BIOS bytes, derived images, disassembly tables, wholesale pseudocode, raw private reports, credentials and personal local paths are excluded.
- Root and research contracts were reread; the new child contract and parent index were updated. Existing history/status/technical contracts remain unchanged because the investigation adds research evidence and does not change implementation.
- Three domain researchers produced private drafts; a separate review of their combined public prose checked mapping consistency, method distinctions and overclaims. Nonzero-read wording and original-profile scope were corrected before publication.
- The original firmware digest was rechecked after the first analysis batch. REA sessions use immutable private snapshots. Session cleanup is checked when the research session is closed; an active subsequent research pass is not a completed-cleanup claim.
- Whitespace, changed-file types, relative links, evidence subjects, accidental local-path patterns and staged content were checked before publication. Normal fast-forward publication uses an explicit expected-remote-head check; a changed head is reconciled before retrying. Remote commit and exact changed content are verified after push.

The repository excludes the private source artifacts and raw receipts. These analysis results are not independently reproducible from this documentation alone. Successful decoding, a recovered instruction body or a passing documentation check does not establish PS1 boot, physical timing, MML1 dependencies, Windows execution, rendering, playback or gameplay.

## Interrupt depth batch

The IRQ-entry conclusions were independently reviewed against the actual REA-returned span and supplemental decode. All 1,088 bytes matched the original source coordinate transformation; 272 decoded instructions covered the selected span. Callback-pointer capture, test-result forwarding, successor-read timing, ordinary versus context return, and the conditional EPC adjustment were checked explicitly. The newly cited IDs are resolved by the same evidence-index check. The derived kernel session was exported and closed before the next ROM investigation began; its private runtime directory was checked for cleanup. This review establishes static consistency, not runtime IRQ behavior.
