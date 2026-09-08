# TASK-038 — Taste Outcome Research Memory

## Goal
Implement user taste, revision evidence and model/research memory.

## Read first
- `spec/22_OUTCOME_TASTE_RESEARCH_MEMORY.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- No overfit from single signal
- Revision reasons captured
- Profile update requires evidence

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-031. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/22_OUTCOME_TASTE_RESEARCH_MEMORY.md`
- `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md`
- `schemas/user_taste_profile.schema.json`
- `schemas/decision_record.schema.json`
- `schemas/research_evidence.schema.json`

Requirements: R-025, R-071, R-087.
Golden coverage: GS01, GS09, GS28.

- [ ] Persist source-attributed scoped taste/outcome signals with confidence, independent evidence counts and versioned correction/disable controls.
- [ ] Technical QA rejection cannot become global aesthetic preference; one signal cannot create high-confidence global taste, and deletion removes owned learning inputs.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
