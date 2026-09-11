# TASK-019 — Production Strategy Engine

## Goal
Choose mixed-media/direct/reference routes by quality and cost.

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
- Can choose non-generative seconds
- Per-scene route allowed
- Cheapest sufficient route documented

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-018. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md`
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `schemas/production_strategy.schema.json`
- `schemas/cost_estimate.schema.json`

Requirements: R-083.
Golden coverage: GS04, GS14.

- [ ] Compare existing media, still+motion, continuation and full generation for the same intent; costs and unknown acceptance estimates are explicit.
- [ ] Select reusable footage when sufficient without buying video; a cheap route cannot drop product truth or hard locks.
- [ ] Compare complete feasible route cost with category breakdown; a lower video unit price can lose when required audio/reference/post costs are higher. Reject negative estimates, preserve UNKNOWN and do not rank it as free. Require a bounded-liability estimate before handing any route to paid execution.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
