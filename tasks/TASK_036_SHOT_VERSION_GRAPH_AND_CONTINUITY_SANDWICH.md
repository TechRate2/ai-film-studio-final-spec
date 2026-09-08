# TASK-036 — Shot Version Graph and Continuity Sandwich

## Goal
Implement version tree plus incoming/outgoing continuity checks.

## Read first
- `spec/17_SHOT_REVISION_VERSIONING.md`
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
- Original version retained
- Middle-shot revision checks both neighbors
- Downstream stale only when needed

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
