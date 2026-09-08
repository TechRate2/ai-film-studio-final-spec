# TASK-009 — Entity Grouping and Locks

## Goal
Group same entities and implement lock/lifetime semantics.

## Read first
- `spec/06_REFERENCE_INTELLIGENCE.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Multiple views can map to one entity
- Reference lifetimes implemented
- Smallest sufficient ref pack

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
