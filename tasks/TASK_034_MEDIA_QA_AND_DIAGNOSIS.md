# TASK-034 — Media QA, Diagnosis and Creative/Production Gate

## Goal
Implement pre-generation and post-generation evaluation that can diagnose failure without automatically spending again.

## Read first
- `spec/19_QUALITY_GATES_QA.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/qa_report.schema.json`

## Acceptance criteria
- preflight covers creative purpose, references/canon/continuity, capability/filmability and cheaper route/cost;
- post-QA checks semantic result, identity/product/prop, visual corruption, audio/dialogue, camera/end state and cross-shot continuity as applicable;
- QAReport uses PASS/MINOR/MAJOR/FATAL with evidence/diagnosis;
- QA may recommend repairs but `auto_paid_retry_allowed=false`;
- deterministic non-paid repair can be distinguished from paid media revision;
- user can inspect actionable failure reason and incremental repair cost.

## Binding execution and verification packet

Dependencies: TASK-024. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/19_QUALITY_GATES_QA.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/qa_report.schema.json`

Requirements: R-020, R-057.
Golden coverage: GS09, GS10, GS19, GS24.

- [ ] Use evidence-bearing QA with required checks; accepted pointer changes only after permitted acceptance, never from a raw success response.
- [ ] FATAL/MAJOR/UNKNOWN critical QA yields review/block and zero paid retry calls; deterministic repair is scoped and preserves source history.
- [ ] Reject ACCEPTABLE with MAJOR/FATAL or required FAIL/UNKNOWN at serialization and acceptance boundaries. Domain tests also reject an omitted/duplicated required check, a producer-downgraded required flag and mismatched policy/version. Optional UNKNOWN remains permitted where the actual policy allows it. No accepted-pointer change or dependent release occurs on these failures.
- [ ] Auto-accept is disabled outside the evaluator's calibrated scope; a high self-rating and attractive isolated frames cannot override an assembled-scene continuity or required dialogue failure.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
