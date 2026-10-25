# Specification: native-startup

## Assumptions and objective

[Shared specification](SPEC.md) applies. A bounded accepted startup slice is not native original-game boot. Advance only through independently implemented recovered behavior and genuine same-owner operations, retaining the first unsupported dependency honestly.

## Provider-owned interface

The existing [native service specification](docs/technical/native-service-contracts.md) owns Session/generation identity, knownness, service admission, response/IRQ obligations, microcommit preservation and retry semantics. It remains the detailed specification; this page does not duplicate or replace it.

- Runtime/data dependency: `original-data-access` provides the immutable production image/reader; imported inspection data alone cannot supply authority.
- Consumers: any future `native-runtime-control` integration must meet the provider's lifecycle contract; the product target requires separately reviewed startup evidence.
- Research prerequisite: `reference-research` for specifically identified behavior/provenance gaps, never as an executable runtime dependency.
- Unknown operands, missing/stale authority, unsupported effects or unretired obligations remain explicit stops, not invented successful returns.

## Success and verification

Trace to `roadmap/cd-startup`, `loader/*` and `boot/native-boot`, without changing their distinct criteria. Genuine private tests check connected ownership, actual operations, fault/retry debt and no replay of committed work. Keep static, synthetic, Linux and Windows evidence separate. Native boot requires its own authorized Windows evidence and exact reviewed scope, not a public documentation pass.

## Consequential open boundary

The public [handoff](DOT.md) retains A0:49 workload/effect/commit uncertainty and the missing independent expected-effect basis. Do not invent a no-op, generic callback or GPU readiness to move forward. Initializer execution preparation remains blocked; this task does not retry it. Actual private commands, style and layout must be verified within the selected native slice before implementation.
