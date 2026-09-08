# TASK-029 — Degrade Planner

## Goal
Implement explicit fallback when requested capability unsupported.

## Read first
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No silent degrade
- Reference priorities applied
- Audio can move to post

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
