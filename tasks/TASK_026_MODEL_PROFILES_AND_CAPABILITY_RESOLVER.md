# TASK-026 — Model Profiles and Capability Resolver

## Goal
Implement profile registry with unknown/verification status.

## Read first
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Model behavior not guessed
- Profile version in provenance
- Unknown capability can block/degrade

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
