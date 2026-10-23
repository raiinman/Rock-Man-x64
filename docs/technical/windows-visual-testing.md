# Windows visual-testing readiness

This page maintains the project's Computer Use setup and verification procedure. It distributes no desktop runtime, game code, original inputs or private test evidence.

## Tools and ownership

| Component | Role | Maintenance |
|---|---|---|
| Computer Use plugin | Supported desktop-app access, screenshots and interaction | Install and enable through the desktop app's plugin interface |
| App-provided JavaScript/CUA session | Hosts the documented desktop-control API | Supplied and registered by the app; an installed runtime file alone does not prove tool availability |
| Project validation harness and supervisor | Bounded synthetic command/state checks and owned-process cleanup | Private, separately reviewed and version-pinned; their passes do not establish visual correctness |
| This procedure | Setup, readiness and evidence boundaries | Reviewed Markdown in this repository |

The public repository remains documentation-only. Do not vendor proprietary plugin files, runtime executables, private wrappers, application caches or original game content. A new repository or replacement automation bridge is not needed to repair app-provided tool exposure.

## Supported setup

OpenAI's [Computer Use setup documentation](https://learn.chatgpt.com/docs/computer-use) describes opening Plugins, selecting Computer Use, installing if prompted, enabling it when offered, turning on its server and skill toggles, then selecting Try now. Review app access through Settings > Computer use. Preserve required prompts and existing security policy.

The [plugin documentation](https://learn.chatgpt.com/docs/plugins) says installed plugins can add skills and MCP tools to new chats. This is a supported session setup path, not evidence that an existing long-running task refreshes in place. Keep research and validation sessions intact; do not restart or replace them merely to test a hypothesis.

If setup requires a UI step and the current task has no functioning Computer Use tool or supported setup action, report that boundary. A shell package installation cannot by itself publish a missing app-managed tool into an active task.

## Readiness check before launch

1. Inspect the current task's exposed tools and read the applicable installed Computer Use instructions. Use their current API names; do not assume a cached version describes the current tool contract.
2. Distinguish installed files from registered capabilities. Record whether the documented JavaScript session and desktop-control surface are actually available. An enabled browser surface alone does not establish desktop support.
3. If a registered capability points to a missing bundle version while another version is installed, record a possible registration mismatch. That is a diagnosis, not proof of its cause or permission to rewrite app caches.
4. If tools remain absent, stop before launching the project GUI. Preserve existing evidence and request app/platform-supported registration recovery. Do not spawn internal helpers directly, invent an IPC client or substitute a new screenshot/input route.
5. Once the required tools are available, obtain the separately scoped project-window test authorization, use only its declared inputs and target window, and retain actual observations. Do not inspect unrelated windows.

On Windows, official documentation says Computer Use operates on the active desktop and can move the pointer and type in the foreground. Schedule project UI work so it does not disturb another user's or agent's active research. A bounded console test is a separate activity.

## Evidence and current limit

A reported read-only project capability check found the required desktop-control tools absent despite installed bundle/runtime files. An observed bundle-version mismatch remained a possible registration issue; no supported in-task refresh or repair action was verified. No app was launched for that check, and no visual pass followed.

Synthetic host-function lifecycle checks can exercise create, close and quit behavior without proving actual standalone launcher operation, readable layout, pixel correctness or snapshot display. Missing capability is a prelaunch tooling blocker, not a failed game run. Preserve earlier test results within their original scopes.

## Keeping this procedure current

At each relevant app/plugin update, compare the current official setup guidance and installed instructions with the task's actual tool exposure. Update this page through a reviewed change when those contracts change; avoid repeating successful native tests solely for reassurance. Record observed recovery separately from suggested repair. Never label a setup change successful until the required tools are exposed and the separately authorized verification completes.

[Technical documentation](architecture.md) · [Current status](../status/current-status.md)
