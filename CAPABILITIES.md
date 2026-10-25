# Rock Man x64 capability map

## Assumptions recorded before specification

- This is an adoption layer over the existing architecture, capability inventory, service contracts and tracker, not a new project roadmap or a claim of accepted implementation.
- The product remains the independent native Windows game plus integrated IDE. Bounded startup, inspection and research are not that finished product.
- This public tree contains documentation infrastructure, not the private native source or its original inputs. Private implementation commands, exact source layout and source examples remain private; missing verified details block dependent implementation rather than being guessed.
- Existing ownership, approvals and stopped/gated work carry forward. This map does not authorize new execution, source publication, implementation reuse or a provenance change.

## Stable boundaries

Each ID is stable kebab-case. Root module specifications add workflow and acceptance traceability to existing provider-owned contracts; they do not replace those contracts. The [shared specification](SPEC.md) applies to every module.

| Capability ID | Objective / provider-owned boundary | Existing acceptance reference | Specification |
|---|---|---|---|
| `original-data-access` | Bounded read-only media/file access and safe logical export; distinguishes inspection data from production media ownership | `roadmap/source-inventory` | [Data access](SPEC-original-data-access.md) |
| `native-inspection` | Diagnostic asset inspection, source-bound offline editing and data-only observation; never runtime control | `roadmap/diagnostic-assets`, `roadmap/offline-editor`, `roadmap/portable-observation`, `inspection/*`, `observation/*` | [Inspection](SPEC-native-inspection.md) |
| `native-startup` | Same-owner native services and recovered startup continuations with honest unsupported stops | `roadmap/cd-startup`, `loader/*`, `boot/native-boot` | [Startup](SPEC-native-startup.md) |
| `native-runtime-control` | Separately gated production load/stop/retirement/endpoint lifecycle; S2 remains NO-GO | `s2/*`, `roadmap/live-controller` | [Runtime control](SPEC-native-runtime-control.md) |
| `native-game-delivery` | Existing native game and integrated IDE outcome, beyond startup and diagnostic foundations | Remaining production `roadmap/*` criteria, including `roadmap/end-to-end` | [Product delivery](SPEC-native-game-delivery.md) |
| `reference-research` | Sourced, provenance-qualified reference findings, not runtime implementations or acceptance authority | `roadmap/provenance` is a separate unresolved implementation-review criterion | [Research](SPEC-reference-research.md) |
| `documentation-tracker` | Reviewed evidence, deterministic read-only projections and bounded publication checks | [Tracker upkeep contract](docs/status/TRACKER.md); no added game milestone | [Tracker](SPEC-documentation-tracker.md) |

`analysis-tooling` is a separately owned supporting workstream, not an in-repository native module. Its public reference is the existing [REA capture-feasibility handoff](docs/status/decisions-and-handoff.md#apex-1-response-read-only-windows-capture-feasibility--october-24). That record establishes neither a ready capture adapter nor a native-game dependency. Its implementation plan remains with its owner; this adoption creates no duplicate tooling task or new support claim.

## Directional dependencies

Arrows mean **consumer -> provider**. Providers own their interface and error/ownership semantics; consumers reference, never redefine, them. All listed edges are acyclic.

### Runtime/data interfaces

- `native-inspection -> original-data-access`: immutable inspection input and source-bound identities, per the [media boundary](docs/technical/architecture.md#media-boundary).
- `native-startup -> original-data-access`: the retained production media allocation/reader, not an imported directory masquerading as production authority.
- `native-runtime-control -> native-startup`: **proposed, blocked** integration only. Accepted loading, whole-owner retirement, stop/fault and endpoint contracts are still required; this is not an existing callable API.

There is no runtime import from research, the public tracker or analysis tooling. Diagnostic inspection does not acquire control authority through these edges.

### Product acceptance composition, not runtime imports

- `native-game-delivery -> native-startup`: required native startup acceptance is necessary, not sufficient for the game.
- `native-game-delivery -> native-inspection` and `native-game-delivery -> native-runtime-control`: the integrated IDE requires both diagnostic foundations and separately accepted production interaction.
- Production scene/resource lifecycle, renderer, animation, controls/camera, collision, gameplay, audio, game saves, provenance, packaging and end-to-end criteria remain the existing [roadmap](docs/status/dashboard.md#roadmap--accepted-roadmap-milestones). No new APIs, estimates or implementation tasks are invented for them here.

### Evidence prerequisites and reporting, not execution dependencies

- `native-startup -> reference-research` and `native-game-delivery -> reference-research` apply only when an identified behavioral/provenance question requires that evidence. A reference answer does not satisfy the native test or permission gate.
- `documentation-tracker -> original-data-access`, `native-inspection`, `native-startup`, `native-runtime-control`, `native-game-delivery`, `reference-research`: documentation consumes reviewed evidence about these capabilities; it cannot control or accept them automatically.
- `analysis-tooling` has no native runtime edge. Public coordination may inform investigation feasibility without importing its implementation or changing native acceptance.

## Scope and ownership checks

### Provider-first contract review and implementation eligibility

For a selected, authorized slice, review/specify and validate a provider boundary before implementing a dependent consumer. The dependency order is:

1. `original-data-access` first for runtime/data contracts. Review relevant `reference-research` findings before any decision that depends on them; research is an evidence prerequisite, not a linked runtime library.
2. `native-inspection` and `native-startup` may then proceed independently within their separate approved scopes after their required provider contracts are satisfied.
3. `native-runtime-control` becomes implementation-eligible only after its required startup/lifecycle contract and existing S2 gates are actually resolved. Its position in this order does not resolve those gates.
4. `native-game-delivery` composes separately accepted product requirements; this is acceptance ordering, not a source-level build graph or a commission to implement pending gameplay.

For actual authorized implementation, build/check the required provider slice before its consumer and retain the boundary test at the checkpoint. No native build command or runtime permission is inferred here. `documentation-tracker` can maintain and report any reviewed evidence at every step, including pending/NO-GO results; it does **not** wait for product completion. `analysis-tooling` remains an independent supporting workstream. Independent authorized work need not wait on an unrelated blocked dependency.

The existing [technical inventory](docs/technical/capability-matrix.md) remains the detailed coverage inventory. The map deliberately stops at existing independently reviewable boundaries rather than splitting every unaccepted game feature into invented specifications. Decompose a selected production capability only when its scope, provider contract and acceptance evidence are known.

[Canonical tracker data](docs/status/dashboard-data.json) alone owns acceptance flags, frozen criteria and numeric history. References such as `roadmap/cd-startup` mean checklist ID/item ID, not a new checklist. No map or spec checkbox advances those flags.
