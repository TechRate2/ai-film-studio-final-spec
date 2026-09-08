# TASK-021 — Continuity Dependency Scheduler

## Goal
Implement DAG scheduling with sequential dependent shots.

## Read first
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
- Dependent child waits for accepted parent
- Independent branches parallelize
- Rejected parent does not release child

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-020. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md`
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `schemas/generation_plan.schema.json`
- `schemas/artifact_dependency.schema.json`
- `schemas/job.schema.json`

Requirements: R-011.
Golden coverage: GS03, GS09.

- [ ] Claim only jobs whose required parents are CURRENT/accepted; persist leases, input pins and DAG validation before submission.
- [ ] Race parent rejection/revision with child claim, independent branches and duplicate worker; no dependent release, cycle or unauthorized double spend.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
