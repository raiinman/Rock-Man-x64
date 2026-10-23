# Technical documentation maintenance

Scope: public architecture and bounded capability specifications in this directory. These are documentation-only files; changes here do not authorize implementation or publication of private materials.

- Keep [architecture](architecture.md), [capabilities](capability-matrix.md) and [service contracts](native-service-contracts.md) consistent with [current status](../status/current-status.md).
- Distinguish recovered source behavior, explicit native policy, diagnostic fixtures and proposals. Do not claim full boot, a complete IDE or PS1 hardware equivalence.
- Synthesize narrative; never copy executable bytes, disassembly tables, assets, private report dumps, internal paths or identifiers.
- Verify linked documents, terminology and provenance categories before publication. A build is not a Windows run; a component check is not gameplay.
- Preserve the history of corrected interpretations and link the status/decision record rather than silently upgrading claims.

## Tooling procedure

- [Windows visual-testing readiness](windows-visual-testing.md) owns the supported setup and capability-check procedure for project UI validation. Keep proprietary runtimes and private diagnostics out of the public repository; distinguish installed files, exposed tools and actual visual acceptance.
