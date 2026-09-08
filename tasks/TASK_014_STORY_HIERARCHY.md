# TASK-014 — Story Hierarchy

## Goal
Implement series/episode/scene/beat planning with scene purpose and exit state.

## Read first
- `spec/05_CREATIVE_STORY_RETENTION.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Every scene has purpose/change/exit
- Long-form hierarchical
- Long-form planning is hierarchical and versioned; simple scripts may remain compact

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-013. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/05_CREATIVE_STORY_RETENTION.md`
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `schemas/project_canon.schema.json`
- `schemas/creative_strategy.schema.json`
- `schemas/generation_plan.schema.json`

Requirements: R-082.
Golden coverage: GS03, GS05.

- [ ] Persist purpose/objective/obstacle/entry/change/exit per scene and map beats to shots and generation segments without one-panel-one-call assumptions.
- [ ] Reorder/retcon a scene and detect causal/knowledge dependencies; a simple request may omit unused hierarchy and a long film cannot rely on one unversioned script blob.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
