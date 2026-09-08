# TASK-023 — Selective Keyframe Controller

## Goal
Decide whether a keyframe is justified.

## Read first
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Keyframe not mandatory
- Risk/cost drives decision
- Previous frame may satisfy need

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
