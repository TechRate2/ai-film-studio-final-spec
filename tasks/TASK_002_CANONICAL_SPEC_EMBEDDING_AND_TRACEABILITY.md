# TASK-002 — Canonical Spec Embedding and Traceability

## Goal
Embed this spec repo into implementation source-of-truth and wire traceability/CI checks.

## Read first
- `spec/00_SPEC_LOCK.md`
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Canonical docs present
- Traceability tracked
- CI detects missing critical spec files

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-001. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/00_SPEC_LOCK.md`
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `spec/26_IMPLEMENTATION_GOVERNANCE.md`
- `schemas/common.schema.json`

Requirements: R-079.
Golden coverage: GS26.

- [ ] Pin one canonical revision in the implementation repository; validate schemas, refs, contract enums, task graph and traceability with the canonical validator.
- [ ] Demonstrate validation failure after removing a required file or mutating a dangerous enum; do not count mere copies/file existence as enforcement.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.


## Handoff acceptance (R-079 / GS26)
Read `governance/IMPLEMENTATION_HANDOFF.md`.
- [ ] Prove root AGENTS/CLAUDE bridges load from the implementation working directory and resolve exactly one pinned SPEC_ROOT; a fresh session identifies actual instructions and revision.
- [ ] Record environment/stack decisions and real baseline tooling commands before TASK-003; pending service/start commands name their owning task rather than claiming they already run.
- [ ] Establish implementation-side ledger/receipts covering every criterion and current tested revision; distinguish PARTIAL checkpoint commits from COMPLETE acceptance.
- [ ] Wire canonical validation to SPEC_ROOT and separate app CI to IMPLEMENTATION_ROOT. Demonstrate missing bridge, stale spec pin and failing application check cannot yield an accepted task merely because spec CI is green.
