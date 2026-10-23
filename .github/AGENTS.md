# Approved repository documentation automation

## Purpose

Own the user-approved documentation updater and chained public-tracker Pages delivery, without expanding into game builds or unrelated infrastructure.

## Ownership

- `workflows/AGENTS.md` owns the exact updater/build/deploy triggers, job credentials, output and race boundaries.
- Root contracts own public content and the user's authorization. Documentation contracts own evidence and tooling.

## Local Contracts

- Only the approved docs-only tracker updater and its chained static-tracker Pages delivery are in scope. Required Pages source/environment configuration is authorized; preserve existing protections. No game builds, other deployments/services, secret creation, unrelated repository settings, branch-protection changes or additional workflow routes.
- Do not broaden permissions or use a different token/route if a remote operation is blocked. Report the exact action and owner decision needed.

## Work Guidance

- Preserve unrelated research and contributor changes. Default-branch execution is not permission to force-push.

## Verification

- Review exact workflow diffs and applicable tool tests; after publication verify the actual Actions run and generated commit.

## Child DOX Index

- [workflows/AGENTS.md](workflows/AGENTS.md) owns `update-progress.yml`, including its three strictly separated jobs.
