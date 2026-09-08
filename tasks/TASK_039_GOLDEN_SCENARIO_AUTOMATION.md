# TASK-039 — Golden Scenario Automation

## Goal
Automate behavioral acceptance with fixtures and optional paid smoke tests.

## Read first
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
- Non-paid scenarios CI-capable
- Paid tests explicitly gated
- Regression report readable

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
