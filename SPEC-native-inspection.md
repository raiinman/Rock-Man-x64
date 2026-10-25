# Specification: native-inspection

## Assumptions and objective

[Shared specification](SPEC.md) applies. Diagnostic assets, offline edits and data-only observation do not control the production runtime or prove game boot. Preserve bounded inspection and source-bound editing while making their actual acceptance limits explicit.

## Provider-owned interface

Existing [asset/rendering](docs/technical/architecture.md#assets-and-rendering), [editor](docs/technical/architecture.md#editor-boundary) and [data-only observer](docs/technical/capability-matrix.md#data-only-observer-boundary) contracts own their behavior. Edits are sidecars, not original-data patches. Capture providers own snapshot meaning and lifecycle; a viewer cannot mint capture or retirement evidence.

- Runtime/data dependency: `original-data-access`, using its inspection boundary only.
- Outputs: diagnostic views, source-bound sidecar edits and explicitly as-of observations within the documented scope.
- Failure/lifecycle limits include stale or unavailable observations, mismatched sidecars and retained state on bounded failures; never substitute a fabricated live sample or a whole-window rollback promise.

## Success and verification

Trace to `roadmap/diagnostic-assets`, `roadmap/offline-editor`, `roadmap/portable-observation`, `inspection/*` and `observation/*`. Preserve separate capture, portable round-trip, synthetic Windows, launcher, pixel and actual-capture-display criteria. Private behavior changes require focused RED/GREEN or characterization plus applicable regression and precise caller-effect limits. Public mock-DOM tests are unrelated to native GUI acceptance.

## Limits and next decision

Existing native workers retain patch ownership. This adoption adds no GUI build/test fact or new editing feature. Exact private source structure, commands and source-style example remain private. Production endpoint integration is blocked on its own contract; even a completed diagnostic viewer cannot satisfy `native-runtime-control` or complete integrated IDE acceptance.
