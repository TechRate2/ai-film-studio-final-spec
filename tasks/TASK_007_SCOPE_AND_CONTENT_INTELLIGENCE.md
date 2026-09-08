# TASK-007 — Scope and Content Intelligence

## Goal
Infer short/long/series and content mode with adaptive depth.

## Read first
- `spec/03_SCOPE_AND_CONTENT_INTELLIGENCE.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Series intent creates durable canon mode
- Short avoids series overhead
- Scope independent from genre

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-006. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/03_SCOPE_AND_CONTENT_INTELLIGENCE.md`
- `schemas/scope_decision.schema.json`

Requirements: R-003, R-041.
Golden coverage: GS01, GS05, GS12.

- [ ] Compare a short serialized teaser and longer one-off B-roll request: scope follows continuity/complexity, not just seconds or genre labels.
- [ ] Round-trip all content modes including PRODUCT_DEMO; genre/provider changes do not rewrite scope history. Record why minimal or expanded context is necessary.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
