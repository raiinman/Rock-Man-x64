# Spec-driven development: shared project contract

## Assumptions

The assumptions in [the capability map](CAPABILITIES.md#assumptions-recorded-before-specification) apply first. Existing contracts and approvals are reused, not reset. This adoption is documentation-only; it neither starts game implementation nor replaces ongoing owners' work. The canonical public baseline contains no root `SPEC-*.md` module system or `tasks/` directory; existing technical specifications and research plans are retained.

## Objective and measurable success

Apply **scope check -> Specify -> Plan -> Tasks -> Implement** to the existing Rock Man x64 project, while preserving evidence boundaries and its native-game-plus-IDE goal.

For this adoption to be ready:

1. Every mapped in-repository capability has a stable ID, provider-owned contract, explicit scope and existing acceptance reference.
2. Dependency edges are directional and acyclic; runtime interfaces, product acceptance and evidence/reporting are distinguishable.
3. Publicly reproducible documentation checks pass without changing native criteria, acceptance flags, historical observations or preserved research/license files.
4. Private-source command/layout/example gaps are explicitly recorded privately, not filled with generic templates or published implementation.
5. The exact candidate receives privacy/contract review; publication and tracker review remain separate, explicit operations under existing authority.

Completion of this document is not completion of any game roadmap criterion.

## Actual structure and technology

```text
AGENTS.md, DOX-LICENSE           repository contracts and preserved framework license
DOT.md                          public coordination entry point
docs/technical/                 architecture, capability inventory, native service contracts
docs/history/                   chronology, failures, recoveries and validation history
docs/status/dashboard-data.json authoritative reviewed evidence and acceptance
docs/status/tools/              Python standard-library generator and unittest fixtures
docs/status/visuals/             generated and archived original SVG documentation
docs/web/                       vanilla HTML/CSS/ES modules, builder and bounded tests
research/                       reference prose, catalogs, provenance and existing research plans
CAPABILITIES.md, SPEC*.md        adoption map, shared rules and thin module specifications
tasks/                          adoption-only plan and execution checklist
```

The public documentation uses Python 3, Node's built-in test runner, vanilla browser ES modules and static GitHub Pages delivery. It has no package-manager install requirement. The [documented native architecture](docs/technical/architecture.md) uses independently written native C++, Win32/GDI inspection and owned services; the private source tree is not reproduced here. No native language-version, compiler command or dependency version is inferred from this public tree.

## Verified commands and flags

Run from this repository root using already available Python 3 and Node. These exact public documentation commands are the adoption validation surface; they never build or launch the game:

```sh
python3 -B -m unittest discover -s docs/status/tools -p 'test_*.py' -v
node --test docs/web/tests/site.test.mjs
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s docs/web/tests -p 'test_*.py'
python3 -B docs/status/tools/update_tracker.py --check
git diff --check
```

`--check` is read-only. After a separately reviewed authored tracker update, its existing maintenance commands are:

```sh
python3 -B docs/status/tools/update_tracker.py --write
python3 -B docs/status/tools/update_tracker.py --check
```

Only the five generated outputs in [TRACKER.md](docs/status/TRACKER.md#source-and-outputs) may change through generation. The `--refresh-activity` and `--activity-json` paths require actual exact commit metadata as specified there; do not use a local synthetic baseline as a claimed published commit. [Web build operations](docs/web/README.md#build-and-checks) require new output paths outside the source tree and an actual full source revision. No generic web-stack build command or native build command is supplied here.

The private companion records inspected native runners and their limits. Exact commands for another private target must be obtained from that target's verified owner/receipt before execution. Publishing private build paths, source or an incomplete guessed compiler invocation is not a way to satisfy this requirement.

## Style and representative example

- Keep Markdown operational, concise and linked to the nearest owning contract. Describe proposals, source review, synthetic/component checks, platform execution and acceptance separately.
- Follow surrounding code: Python standard-library functions with explicit validation and `unittest`; browser code uses ES-module exports, pure projections and Node built-in tests. Do not introduce dependencies for this adoption.
- Preserve existing source formatting during future bounded edits. Native code style/examples belong in the private companion, not this public repository.

Actual public generator example, from `docs/status/tools/update_tracker.py`:

```python
def need(condition, message):
    if not condition:
        raise Invalid(message)
```

It illustrates fail-closed validation, not a new runtime error API. Documentation-only source is the only implementation example published here.

## Test strategy and evidence levels

- **Specification validation:** stable IDs, exact local links, acyclic typed edges, criterion-ID traceability, explicit assumptions/gaps, no contradictory ownership or unauthorized scope.
- **Public unit/fixture checks:** Python `unittest` for tracker/schema/history/allowlist behavior and artifact/workflow contracts; Node `node:test` for model/render-string and mocked-DOM controls. Fixtures remain test-owned and isolated.
- **Public integration checks:** deterministic generation and artifact consistency. These do not establish actual Actions execution, deployment, browser pixels or native behavior.
- **Native behavior changes:** owning private workstream first demonstrates a genuine behavior-specific RED on the relevant baseline, then the smallest complete GREEN slice, meaningful regression, independent review and exact artifact/evidence retention. Refactors start with characterization. No unchanged native suite is rerun merely to adopt this documentation.
- **Platform/full-product checks:** retain exact executed/not-run distinctions. Compilation, synthetic Windows control checks, visible pixels, actual capture, production runtime and gameplay require their own evidence and applicable authority; none is inferred from another level.

## Always / Ask first / Never

**Always:** read the applicable DOX chain; preserve research, license, history, incomplete work and current owners; update the specification before a behavior change; use the canonical acceptance source; stop at unknown/unsupported behavior; retain failed evidence and precise recovery limits; consult Atlas first for technical gaps and use the existing bounded handoff without duplicate requests.

**Ask first:** resolve consequential ambiguity in behavior, API ownership, original-input use or provenance; obtain any missing execution/publication/access authority; choose a destination before starting different work over an unfinished plan. Existing settled scope and approvals do not need ritual reapproval. A proposed map, task or research reply grants no new authority.

**Never:** publish private source, original bytes/assets, captures, paths, private identities or raw reports; import port/mod/emulator implementation; use a BIOS/emulator runtime in the finished native game; fabricate success, commands, test results, independence or percentages; retry blocked initializer preparation or stopped work; enable S2 through diagnostic acceptance; overwrite incomplete plans, delete task history or mass-close checklists.

## Living specifications and definition of done

Use the owning module specification and existing contract together. A provider updates its boundary before consumers depend on changed behavior. A consequential unresolved requirement blocks that dependent slice, not unrelated authorized work. Prefer the smallest complete vertical slice with an observable checkpoint over a project-wide speculative roadmap.

An implementation slice is done only when its specified behavior and failure paths are met, the genuine RED/GREEN or characterization evidence and relevant regression are retained, actual platform limits are stated, independent review is resolved, DOX/spec/task records agree, and the appropriate existing acceptance owner reviews the result. Publication requires its own exact diff review and verification; a successful local check is not a published change.

## Open questions retained

- Native A0:49 workload/effects/commit obligations and an independent expected-effect basis remain unresolved; follow the existing [handoff](DOT.md), not a newly invented no-op.
- S2 loading/retirement/stop/endpoint gates remain open. Native game boot and complete product acceptance remain unestablished.
- Before any newly selected private implementation slice, confirm its exact current source baseline, full commands/flags, style example, regression target and incomplete-plan destination in the private workspace. The public repository cannot verify those missing details.
- This adoption leaves every pending production roadmap criterion pending and does not prescribe an order for unscoped gameplay implementation.
