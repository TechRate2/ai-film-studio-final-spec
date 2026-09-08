# TASK-020 — Scene Complexity Planner

## Goal
Produce GenerationPlan with meaningful boundaries and risk/cost.

## Read first
- `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No fixed split rule
- Boundaries have reasons
- Expected acceptance tracked

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-019. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md`
- `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md`
- `schemas/generation_plan.schema.json`

Requirements: R-010, R-083.
Golden coverage: GS03, GS04, GS13, GS14.

- [ ] Map editorial shots to generation segments explicitly; test CONTINUOUS, SEGMENTED and CONTINUATION with state/capability/boundary reasons.
- [ ] Test variable route duration limits and uneven action density; a fixed split/panel rule fails, and unmeasured acceptance probability stays null.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
