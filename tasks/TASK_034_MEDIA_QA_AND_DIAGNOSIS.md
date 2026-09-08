# TASK-034 — Media QA and Diagnosis

## Goal
Implement preflight/post-generation QA without automatic paid retry.

## Read first
- `spec/19_QUALITY_GATES_QA.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Severity classification
- Failure diagnosis/recommendation
- QA does not auto-regenerate

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
