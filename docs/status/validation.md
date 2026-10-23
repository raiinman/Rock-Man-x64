# Validation ladder and evidence provenance

A passing check supports only the claim it actually tested. This page defines the evidence categories used throughout the public documentation. The latest numerical results are in [current status](current-status.md).

## Evidence categories

**Static source evidence.** Private identity-pinned original data supports recovered function boundaries, tables, bit layouts and control flow. Static analysis does not show that the original executable ran, that the native replacement is reachable, or that all branches are understood. Original instruction listings and assets are intentionally not reproduced here.

**Synthetic or component evidence.** Native routines can be compared with independently expressed oracles, malformed-input fixtures, bit-basis vectors and failure injection. Such checks establish their stated input and ownership contracts, not source reachability. Synthetic fixtures cannot mint production capabilities.

**Connected native evidence.** A production Session performs translated source steps and genuine owned services until the first unsupported dependency. Its reported stop, known masks, generations and retained obligations matter as much as its exit code. Diagnostic first-scene paths must remain separately labeled.

**Compiler evidence.** Strict Linux builds, sanitizers and Windows PE cross-compilation detect useful classes of errors. A PE file existing is not evidence that Windows launched it. ASan/UBSan checks do not imply LeakSanitizer ran; tracing prevented leak scanning in the recorded environment.

**Actual Windows evidence.** A Windows execution receipt must identify the particular frozen stage and cases. Console checks do not automatically verify GUI rendering, editing prompts, device behavior or gameplay. The last such frozen checkpoint is identified in current status; no new-stage Windows result is implied by later cross-builds.

**Project attestation.** The public pages summarize private receipts and reviewed reports. They are not raw test logs or independently reproducible proof. External readers cannot rerun private Windows cases from this documentation-only repository. No implementation source, private data or executable package is included here to support that claim.

**Design and research.** A specification, public reference survey or scratch prototype is a proposal or bounded investigation until integrated and accepted. Public research references are distinct from private implementation verification; a citation does not certify that this project implements the cited system.

## Acceptance ladder

1. Preserve original inputs and identify the exact source data used.
2. Establish the smallest source behavior and its unknowns by static inspection.
3. Specify native ownership, knownness, refusal and commit policies explicitly.
4. Implement and validate the component against independent checks and malformed inputs.
5. Connect it to real source continuations without synthetic success or reachability shortcuts.
6. Exercise allocation failure, retries, stale ownership and post-commit obligations.
7. Recheck previous profiles, source identities, generated artifacts and preserved releases.
8. Run the exact candidate on Windows and distinguish console, GUI and device coverage.
9. Review the complete result, freeze immutable artifacts and record the accepted boundary.
10. Claim gameplay only after actual end-to-end game behavior is demonstrated.

A later step cannot be inferred from an earlier one. The configuration stage has a frozen 40-case Windows result; the later sealed software-mixer stage has 51 actual Windows comparisons. Its stale summary counters are a retained metadata defect, not a failed or truncated execution. The newer mode-00 candidate has pinned Linux regression/profile and targeted sanitizer evidence, an accepted 13-stage isolated recovery aggregate, and a 69-case unsealed Linux contract. Later actual Windows mode validation passed all 69 cases, with frozen payloads unchanged and acceptance recorded separately. Newer graphics continuations have Linux-only component/connected/regression evidence, not Windows parity or a repeated full-project aggregate. Synthetic Windows supervisor failures remain separate from game execution. Earlier shared-tree logs are not pinned-candidate receipts. See [current status](current-status.md) for exact counts and limits.

## Handling failures and inconclusive runs

Record each command's outcome rather than treating a wrapper's exit code as a summary verdict. The paused aggregate runner ended with exit 0 while two component stages had failed. Both failures remain in the historical record. Corrected-fixture retries later passed, supporting the 22:06 UTC cloud-validation completion without erasing the initial failures.

Missing fixture inputs require a corrected-input rerun before passing acceptance. Copying and hashing fixtures is not that rerun. A transport interruption or uncertain execution must first be reconciled; it is not permission to repeat a potentially completed mutation blindly. Earlier shared-output runs with uncertain ownership are excluded instead of being combined into a convenient aggregate.

Verification should report what was attempted, what target it used, what completed, what was denied or remains uncertain, and what evidence can resolve the uncertainty. Retrying a denied action needs materially new relevant evidence or confirmation that it did not execute, not merely the passage of time.

## Public reproducibility limits

This repository can be reviewed for consistent scope, readable specifications, linked decisions and honest claims. It does not yet offer a public build/test workflow. Commands referring to private source trees would mislead readers and are therefore not presented as public quick-start instructions.

A future public source release would need a separately reviewed distribution boundary, synthetic fixtures, documented toolchains, source-input requirements and an independently usable test procedure. Publication of narrative does not authorize publication of original executable data, assets, previews, private packages or detailed disassembly witnesses.

## Combined-candidate qualification

All four combined Linux phases are separately accepted: the 16-stage aggregate/source-test set, 69-case contract, 19 connected cases and 29 targeted allocation checkpoints. Predecessor tests were not relabeled as combined execution. These phases do not establish combined Windows or release acceptance.

Actual owned capture has a separate four-case Linux/UBSan acceptance: 60 captures and 253 injected allocation failures, with production versus synthetic coverage distinguished. Observed owner fingerprints and source review support bounded non-mutation, not exhaustive private-state introspection. Exporter/frozen-viewer v2 corrections were followed by one accepted actual portable Linux export/import. Windows viewer failed bounded file load at check 37 after 36 passes, with 74 unrun; 24 four-culture trace checks and 33 offline controls test fabricated validator evidence, not native viewer behavior. The IDE's 50 Windows command/state checks remain separate from blocked-before-launch visual QA.
