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

## Binding execution and verification packet

Dependencies: TASK-035. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md`
- `spec/17_SHOT_REVISION_VERSIONING.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `schemas/shot_version.schema.json`
- `schemas/continuity_baton.schema.json`
- `schemas/artifact_dependency.schema.json`

Requirements: R-019, R-038, R-063.
Golden coverage: GS09, GS21.

- [ ] Preserve immutable version graph and atomically change accepted pointer with baton/currency; handle branching incoming/outgoing constraints, not only linear neighbors.
- [ ] Accept incompatible v2, then revert v1; evaluate affected descendants and stale masters without overwriting history or automatically spending.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
