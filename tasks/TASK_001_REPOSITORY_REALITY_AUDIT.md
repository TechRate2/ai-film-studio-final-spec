# TASK-001 — Repository Reality Audit

## Goal
Inspect the implementation repository without modifying production code. Map actual code to this spec and produce a gap report.

## Read first
- `AGENTS.md`
- `spec/00_SPEC_LOCK.md`
- `spec/01_VISION_AND_NON_GOALS.md`
- `prompts/REPOSITORY_REALITY_AUDIT_PROMPT.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Every current-state claim cites a file/path/symbol
- No production implementation changes
- Creates prioritized gap map

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
