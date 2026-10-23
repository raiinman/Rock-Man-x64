# Approved repository documentation automation

## Purpose

Own the single user-approved living-tracker workflow without expanding project infrastructure or publication permissions.

## Ownership

- `workflows/AGENTS.md` owns the exact updater trigger, credentials, output and race boundaries.
- Root contracts own public content and the user's authorization. Documentation contracts own evidence and tooling.

## Local Contracts

- Only the approved docs-only tracker updater is in scope. No game builds, deployments, services, secret creation, repository settings, branch-protection changes or new workflows.
- Do not broaden permissions or use a different token/route if a remote operation is blocked. Report the exact action and owner decision needed.

## Work Guidance

- Preserve unrelated research and contributor changes. Default-branch execution is not permission to force-push.

## Verification

- Review exact workflow diffs and applicable tool tests; after publication verify the actual Actions run and generated commit.

## Child DOX Index

- [workflows/AGENTS.md](workflows/AGENTS.md) owns `update-progress.yml`.
