# TASK-030 — Seedance 2.0 Real Vertical Slice

## Goal
Connect one **real** Seedance provider through canonical planning/compiler/job/spend/QA/revision/finalization flow.

## Mandatory prerequisites
TASK-019..029 plus **TASK-032 Durable Jobs and TASK-033 SpendAuthorization/PaidAttemptGuard must be implemented before the first billable Seedance submission**. Do not bypass this dependency because task number 030 is lower.

## Read first
- `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md`
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `profiles/models/seedance_2_0.yaml`

## Acceptance criteria
- real paid path, no production mock fallback;
- UniversalVideoSpec → Seedance compiler → provider adapter provenance stored;
- explicit positive/negative reference bindings;
- stage/end-state compilation and measured duration rules;
- durable upstream task identity and restart-safe polling;
- cost estimate + SpendAuthorization before submit;
- ambiguous timeout enters reconciliation, never duplicate submit;
- GS01 and GS03 real smoke path;
- QA-triggered automatic paid regeneration impossible;
- accepted output can seed dependent next shot.

A successful API response alone does not complete this task; Phase 2 exit additionally requires Tasks 034–037.
