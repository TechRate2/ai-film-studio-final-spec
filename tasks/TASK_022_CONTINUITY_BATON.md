# TASK-022 — Continuity Baton

## Goal
Persist accepted output state and cross-shot QA.

## Read first
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
- Real output frame/video captured
- Core visual/audio state tracked
- Next shot receives baton

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-021. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/continuity_baton.schema.json`

Requirements: R-012, R-037.
Golden coverage: GS03, GS05.

- [ ] Persist observed accepted entity/prop/body/screen/lighting/weather/emotion/story/audio state plus frame/video evidence and source versions.
- [ ] Rejected/unaccepted output cannot publish a baton; unknown off-screen detail stays null and canonical identity is not replaced by generated drift.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
