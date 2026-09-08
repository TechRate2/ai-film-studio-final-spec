# TASK-015 — Character Relationship Knowledge

## Goal
Implement CharacterRegistry, aliases, knowledge/belief and relationship state.

## Read first
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
- Aliases resolve
- Characters cannot use unknown facts
- Extras not persistent by default

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-014. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/character.schema.json`
- `schemas/relationship_edge.schema.json`

Requirements: R-007, R-072, R-085.
Golden coverage: GS05, GS27.

- [ ] Use story-positioned proposition/acquisition IDs for knowledge, false belief, suspicion, misunderstanding and concealment; wants/fears remain motivations.
- [ ] Test duplicate aliases, directional relationships and a later revelation viewed in flashback; no omniscient dialogue or cross-character leakage.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
