# TASK-001 — Repository Reality Audit

## Goal
Inspect the implementation repository without modifying production code. Map actual code to this spec and produce a gap report.

## Read first
- `AGENTS.md`
- `spec/00_SPEC_LOCK.md`
- `spec/01_VISION_AND_NON_GOALS.md`
- `prompts/REPOSITORY_REALITY_AUDIT_PROMPT.md`

## Audit-only contract
Inspect and report; do not implement, migrate or modify production. Report files and traceability notes are the only deliverables.

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

## Binding execution and verification packet

Dependencies: NONE. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/00_SPEC_LOCK.md`
- `spec/01_VISION_AND_NON_GOALS.md`
- `spec/26_IMPLEMENTATION_GOVERNANCE.md`

Requirements: R-079.
Golden coverage: GS26.

- [ ] Inspect the actual implementation tree, runtime/config, dependencies, migrations, provider boundaries, UI routes and tests; distinguish implemented, partial and absent with exact paths/symbols.
- [ ] Audit reports only: no app code, dependency installation, migration or paid API call. If implementation repository is absent, state that fact and report prerequisites; never fabricate an implementation audit.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
