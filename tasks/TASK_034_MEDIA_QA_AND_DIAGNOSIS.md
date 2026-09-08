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
