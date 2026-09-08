# TASK-004 — Artifact Versioning and Currency

## Goal
Implement CURRENT/STALE/MISSING/BLOCKED plus dependency-aware invalidation.

## Read first
- `spec/17_SHOT_REVISION_VERSIONING.md`
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
- Only affected downstream goes stale
- Versions preserved
- Subtitle-only change does not stale raw video

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
