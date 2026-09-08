# TASK-010 — Dynamic Skill Registry

## Goal
Retrieve only relevant creative/production skills.

## Read first
- `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No full skill dump
- Skills versioned
- No hardcoded pipeline from skill retrieval

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-009. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md`
- `spec/05_CREATIVE_STORY_RETENTION.md`
- `spec/10_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md`
- `schemas/decision_record.schema.json`

Requirements: R-081.
Golden coverage: GS02, GS07, GS13.

- [ ] Index each card’s ID/version/retrieve-when/knowledge link; persist the selected skill versions and bounded context use for a concrete directing decision.
- [ ] An unseen genre retrieves reusable mechanisms without new routing code; irrelevant skills and contradictory embedded commands are excluded.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
