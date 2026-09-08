# TASK-043 — Beta Release Gate

## Goal
Prove the product is commercially testable against the complete canonical contract, not merely feature-complete by self-report.

## Read first
- `spec/00_SPEC_LOCK.md`
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `spec/34_TEST_AND_EVAL_STRATEGY.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/43_CONTENT_SAFETY_RIGHTS_COMPLIANCE.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md`
- `evals/GOLDEN_SCENARIOS.md`
- `traceability/REQUIREMENTS_TRACEABILITY.csv`

## Acceptance criteria
- all critical traceability requirements have implementation refs + tests and are not PARTIAL/BLOCKED;
- every phase exit gate satisfied with evidence;
- real Seedance vertical slice demonstrates create → durable paid attempt → QA → user shot revision → accepted version → continuity → voice/edit → FinalMaster;
- no critical provider/model/cost/continuity/canon/safety drift;
- backup/restore, deletion, outage/reconciliation and spend-kill-switch tested;
- known provider/model limitations published instead of hidden;
- no production mock/fake fallback;
- release report lists exact remaining non-critical limitations and benchmark dates.

## Binding execution and verification packet

Dependencies: TASK-042. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/00_SPEC_LOCK.md`
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `spec/34_TEST_AND_EVAL_STRATEGY.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/43_CONTENT_SAFETY_RIGHTS_COMPLIANCE.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md`
- `schemas/final_master.schema.json`

Requirements: R-040, R-070.
Golden coverage: GS01, GS03, GS25.

- [ ] Audit every phase and critical requirement against exact implementation/test refs, dates and real safe provider samples.
- [ ] No missing, PARTIAL, BLOCKED or fixture-only evidence satisfies a required real gate; publish limitations and reject release on critical invariant failure.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
