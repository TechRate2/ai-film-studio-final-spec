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
