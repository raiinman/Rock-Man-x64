# Specification: original-data-access

## Assumptions and objective

[Shared assumptions, commands, structure, style, tests and boundaries](SPEC.md) apply. Inspection exports and production media capabilities are different products. Provide bounded read-only original-data access and safe logical export without changing original inputs.

## Provider-owned interface

The existing [media boundary](docs/technical/architecture.md#media-boundary) owns supported raw MODE2/2352 Track 1 input and ISO directory interpretation, immutable views, safe new-directory output and cancellation limits. The [service contract](docs/technical/native-service-contracts.md#session-authority-and-knowledge) owns production Session/media identity and generations. The provider, not an inspector or caller, defines these two distinct interfaces. No source signature is invented publicly.

- Consumers: `native-inspection` uses inspection inputs; `native-startup` requires the retained same-image production owner.
- Runtime module dependencies: none within this map; original inputs remain private and externally supplied.
- Unsupported formats, unsafe/existing destinations, invalid identities and read failures must not become valid data or successful completion.

## Success and verification

Trace to canonical `roadmap/source-inventory`; preserve its exact criterion and existing scope. Meaningful private tests cover supported read-only access, safe export, refusal, cancellation and owned-output cleanup, with original fixtures/authority identified. Integrity is not independent authenticity; an export is not production service authority. Public documentation tests validate only the spec/links, not the data path.

## Limits and next decision

No new importer, decoder, repair feature or input scan is requested. Actual private tree/commands and source examples stay with the owning private target; [SPEC.md](SPEC.md#verified-commands-and-flags) states the public reproducibility limit. Future behavior changes must specify the exact supported input and failure boundary before implementation.
