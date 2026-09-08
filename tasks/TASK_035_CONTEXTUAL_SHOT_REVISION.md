# TASK-035 — Contextual Shot Revision

## Goal
Implement EditIntentClassifier and cheapest affected-modality revision.

## Read first
- `spec/17_SHOT_REVISION_VERSIONING.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Dialogue edit can avoid video regen
- Natural-language revision → semantic diff
- Incremental cost displayed

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-030. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/17_SHOT_REVISION_VERSIONING.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/revision_request.schema.json`

Requirements: R-019.
Golden coverage: GS09, GS21.

- [ ] Reconstruct base request/spec/refs/canon/context and all incoming/outgoing version pins into semantic change/preserve diff and incremental cost.
- [ ] Classify subtitle, voice, mix, timeline, grade, action, identity and canon edits through actual dependencies; drafting a revision alone does not stale accepted children.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
