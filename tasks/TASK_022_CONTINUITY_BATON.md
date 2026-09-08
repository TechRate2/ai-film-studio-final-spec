# TASK-022 — Continuity Baton

## Goal
Persist accepted output state and cross-shot QA.

## Read first
- `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Real output frame/video captured
- Core visual/audio state tracked
- Next shot receives baton

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
