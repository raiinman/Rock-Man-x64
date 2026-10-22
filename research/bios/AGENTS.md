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
- The user's current research priority is finding Sony documentation that explains `0x1f801db8` exactly, alongside the native MML1 consumer boundary. Maintain `DB8-BOUNDARY.md`, `SOUND-PRIMARY-SOURCES.md` and `SONY-ARCHIVE-COVERAGE.md`; preserve the distinction between a numeric register binding, related API/architecture evidence, game attestations and native proposals. The archive ledger owns checked scopes, inaccessible revisions and remaining text/image/document-type gaps so follow-ups do not repeat completed scans.
- Preserve other agents' concurrent GitHub changes. Re-read the remote head and contracts before publication.

## Verification

- Check relative links, cited Evidence IDs against private records, profile/subject separation, accidental local paths, forbidden payloads and whitespace.
- Verify the exact published commit and changed file contents. Record private validation limits in the public report.

## Child DOX Index

No child contracts; this file owns this folder.
