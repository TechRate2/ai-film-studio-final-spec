# TASK-004 — Artifact Versioning and Currency

## Goal
Implement CURRENT/STALE/MISSING/BLOCKED plus dependency-aware invalidation.

## Read first
- `spec/17_SHOT_REVISION_VERSIONING.md`
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
- Only affected downstream goes stale
- Versions preserved
- Subtitle-only change does not stale raw video

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-003. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/17_SHOT_REVISION_VERSIONING.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `schemas/artifact.schema.json`
- `schemas/artifact_dependency.schema.json`
- `schemas/shot_version.schema.json`

Requirements: R-022, R-063.
Golden coverage: GS09, GS11, GS21.

- [ ] On a changed consumed field, stale only its consumers and dependent masters; preserve unrelated media and all historical source bytes/provenance.
- [ ] Test branching DAG, cycles, missing inputs, subtitle-only edit and compatible/incompatible revert; CURRENT never implies accepted.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
