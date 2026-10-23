# BIOS-only startup baseline

The owner's authorized BIOS reached a visible **Memory Card / CD Player main menu** in one new bounded emulator capture on 2026-10-23. This establishes a functioning firmware-only diagnostic baseline, not native Rock Man x64 boot or clean-room implementation acceptance.

## Scope and result

- Subject: 524,288-byte firmware, SHA-256 `39dcc1a0717036c9b6ac52fefd1ee7a57d3808e8cfbc755879fa685a0a738278`.
- Instrument: installed PCSX-Redux CLI `29142.20261022.44.x64`, executable SHA-256 `9643b4a589c1f5b4eee8294cc04c7aaaf393ff2d439585739a13716eb0600dc1`.
- Fresh private portable profile, interpreter and software renderer, boot animation enabled, two-MiB RAM selection; no disc, injected executable or saved state. External debugger/file-service endpoints were disabled.
- One run completed 900 vertical blanks, with sixteen ordered CPU checkpoints including the initial sample, four captured display images, no observer errors and normal exit code zero. Host elapsed time was 16.046634 seconds. The wall bound was 35 seconds.
- The emulator emitted its shell-reached event at vertical blank 104. This event is distinct from visual identification of the final menu.
- The final converted display image was inspected and shows the main menu. Its SHA-256 is `cdd5f6e993e4e109a7be162e4c4f324e9ab6bdfed43a485b2a9575507c701fcf`.

The observer samples CPU state without injecting guest instructions or rereading MMIO to manufacture load results. Screenshot conversion uses an explicitly recorded RGB555 interpretation; channel layout is not independently calibrated. Vertical-blank samples do not establish every intervening instruction or hardware timing. Firmware, display images, raw output, profile and collector implementation remain private.

The collector uses the emulator's documented [command-line controls](https://pcsx-redux.consoledev.net/cli_flags/), [event API](https://pcsx-redux.consoledev.net/Lua/events/) and [screenshot API](https://pcsx-redux.consoledev.net/Lua/redux-basics/). Instrument API documentation is separate from a behavioral oracle for the game.

## Use and limits

The workbench can inspect the retained menu and checkpoints without rerunning the target. The original calibration and synthetic A0:49 launch locks remain separate and unchanged. This startup did not execute the game, inspect its actual dispatch table, supply its missing GPU history, test the native owner-lifecycle bridge or resolve the blocked initializer. No game implementation was changed.

Treat this capture as firmware behavior inside the identified emulator. Apply the [provenance review workflow](PROVENANCE-REVIEW.md) before implementation use; an independently written collector and a passing run do not certify clean-room provenance.
