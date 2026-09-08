# TASK-009 — Entity Grouping and Locks

## Goal
Group same entities and implement lock/lifetime semantics.

## Read first
- `spec/06_REFERENCE_INTELLIGENCE.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Multiple views can map to one entity
- Reference lifetimes implemented
- Smallest sufficient ref pack

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-008. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/06_REFERENCE_INTELLIGENCE.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `schemas/reference_binding.schema.json`
- `schemas/character.schema.json`

Requirements: R-005.
Golden coverage: GS02, GS03.

- [ ] Group front/side/detail views of the same entity while preserving separate bindings and target lifetimes; keep ambiguous lookalikes unresolved.
- [ ] Test camera-only video with conflicting identity/background: compiler input excludes prohibited influence; expired scene/shot references are absent.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
