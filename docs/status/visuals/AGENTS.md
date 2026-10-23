# Status graphics

## Purpose

Make verified progress, interesting discoveries and unresolved boundaries visible without publishing private implementation materials.

## Ownership

- `progress-dashboard.svg` is generated from the parent reviewed data; do not edit it manually.
- `findings-01.svg` is the archived 2026-10-23 reconstruction board, not the live tracker.
- `findings-02.svg` is the archived 2026-10-23 frontier board, not the live tracker.
- The parent owns the generated Markdown and reviewed JSON; those are the authoritative current facts and accessible source map. The approved updater regenerates only `progress-dashboard.svg`.

## Local Contracts

- Original static vector artwork only: no game art, screenshots, desktop/chat content, extracted data, private paths, embedded raster captures, executable code or external resources.
- Use standalone SVG text and shapes with a viewBox, title and description. Do not add scripts, event handlers, foreign objects, external fonts, remote images or services.
- Preserve the native-boot-unestablished and S2 NO-GO boundaries until exact new evidence supports a change. A source review is not a runtime pass.
- Never infer a feature-completion percentage from test counts, filled segments or a partial inventory.

## Work Guidance

- Keep the charcoal/cream/cyan/amber technical-editorial design readable at repository-page width.
- Pair every finding with why it matters, evidence class and remaining unknown; keep the parent ledger synchronized.
- Explain original concepts using abstract shapes only. Do not reconstruct game assets or reproduce a user's reference screenshot.

## Verification

- Parse all SVGs as XML and check for executable/external content.
- Compare displayed labels and counts with the parent's evidence metadata and source links.
- Render each SVG to a local PNG and inspect for clipping, overlaps, contrast and legibility. Local renders are review artifacts, not original-game captures.
- Verify the changed-path allowlist, links, whitespace and preserved research/license blobs before publication.

## Child DOX Index

- None.
