# TASK-003 — Project Domain Persistence

## Goal
Implement Project/Episode/Scene/Shot/Artifact core models and migrations.

## Read first
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Persistent IDs and ownership
- Migrations included
- No chat-history-only state

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
