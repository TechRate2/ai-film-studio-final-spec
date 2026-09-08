# TASK-029 — Degrade Planner

## Goal
Implement explicit fallback when requested capability unsupported.

## Read first
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No silent degrade
- Reference priorities applied
- Audio can move to post

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-028. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/degrade_decision.schema.json`
- `schemas/effective_capability.schema.json`

Requirements: R-018.
Golden coverage: GS15, GS20.

- [ ] Resolve explicit alternative routes that preserve hard constraints and record quality/cost differences with evidence.
- [ ] Test unknown capability, denied rights, billed output and uncertain timeout; none authorizes silent paid provider fallback.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
