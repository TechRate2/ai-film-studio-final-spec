# TASK-003 — Project Domain Persistence

## Goal
Implement Project/Episode/Scene/Shot/Artifact core models and migrations.

## Read first
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Persistent IDs and ownership
- Migrations included
- No chat-history-only state

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-002. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `schemas/project_intent.schema.json`
- `schemas/project_canon.schema.json`
- `schemas/character.schema.json`
- `schemas/artifact.schema.json`

Requirements: R-080.
Golden coverage: GS26, GS27.

- [ ] Persist owned project/scene/shot/artifact identities with versioned source links and schema-valid round trips after database restart.
- [ ] Reject cross-project references and stale optimistic writes; include migration/rollback or forward-safe evidence and demonstrate SHORT without artificial Series wrappers.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
