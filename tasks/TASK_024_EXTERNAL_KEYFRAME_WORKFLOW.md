# TASK-024 — External Keyframe Workflow

## Goal
Implement copy prompt/ref pack/upload/validator path.

## Read first
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No internal image charge in external mode
- Imported keyframe validated
- Correction patch supported

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
