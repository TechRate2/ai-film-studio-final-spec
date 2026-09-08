# TASK-043 — Beta Release Gate

## Goal
Run final acceptance, real-provider benchmarks and publish known limitations.

## Read first
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `evals/GOLDEN_SCENARIOS.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Release gates documented
- Known model limits explicit
- No critical spec violations

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
