# BIOS research

## Purpose

Preserve original, evidence-linked findings from the authorized firmware investigation for the native MML1 research handoff.

## Ownership

This folder owns firmware analysis reports, coverage, evidence metadata, validation proposals and the continuing research queue. Parent research documents own the wider source catalog.

## Local Contracts

- Publish original Markdown prose and evidence metadata only. Keep BIOS bytes, derived slices, disassembly tables, wholesale pseudocode and raw private reports outside Git.
- Bind firmware observations to size/digest, source coordinates and analysis profile. Identify a derived mapping separately from original ROM and actual runtime memory.
- Distinguish REA observations, independent instruction decoding, architecture interpretation, proposed host policy and unresolved questions. Do not present private evidence IDs as publicly downloadable artifacts.
- BIOS availability does not establish game usage, successful execution or implementation acceptance. Research continues independently of implementation work.

## Work Guidance

- Reuse retained evidence and private receipts before making a new import. Follow a specific unresolved question and preserve failed or bounded observations.
- Check instruction evidence and function extents before treating pseudocode as a complete description of device accesses, register state or control flow.
- Update the research queue and publish reviewed batches promptly; provide the user's requested half-hour updates through the existing chat heartbeat.
- Use the user's selected [PSX-SPX development documentation](https://psx-spx.consoledev.net/dev/) as the default technical reference. Read relevant pinned pages, corrections and linked measurement reports before seeking specific gaps in Sony archives or designing experiments. Preserve community versus vendor authorship and uncertainty; default-reference status does not establish hardware verification. Avoid repeated broad archive scans and unchanged probes.
- Prioritize the native port's current identified blocker and its actual evidence. Retain the `0x1f801db8` mute/update question as a separate investigation rather than assuming it still blocks the port. Maintain `DB8-BOUNDARY.md`, `SOUND-PRIMARY-SOURCES.md` and `SONY-ARCHIVE-COVERAGE.md`; distinguish register definitions, API/architecture evidence, game attestations and native proposals. The archive ledger owns checked scopes and access/image gaps.
- The user explicitly authorized coordination with the APEX-2 agent. Confirm its current task, input identity, arguments, reaching state and failure before choosing a diagnostic. Keep private traces and coordination records outside GitHub; preserve concurrent work and sealed validation packages. A sent request, a delivered file and an acknowledged reply are different states.
- Before proposing new diagnostic tools, reconcile the existing research debugger, capture runner and workbench capabilities with the port agent's precise question. Share a verified capability inventory and distinguish implemented collectors from generic breakpoint infrastructure; avoid duplicating the debugging setup or using unrelated probe results to fill a missing state producer.
- Follow promising documentation links through their cited sources; a repository inventory alone does not check its external references. The README trace has now found an explicit community definition. Preserve that positive result while tracing authorship, source revisions and claim-specific support; shared-source mirrors do not count as independent corroboration. Sony provenance, original-machine verification and the game consumer remain separate completion boundaries. Documentation research does not authorize importing emulator implementation code.
- Preserve other agents' concurrent GitHub changes. Re-read the remote head and contracts before publication.

## Verification

- Check relative links, cited Evidence IDs against private records, profile/subject separation, accidental local paths, forbidden payloads and whitespace.
- Verify the exact published commit and changed file contents. Record private validation limits in the public report.

## Child DOX Index

No child contracts; this file owns this folder.
