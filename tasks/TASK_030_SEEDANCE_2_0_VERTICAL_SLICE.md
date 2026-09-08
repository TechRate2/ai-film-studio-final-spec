# TASK-030 — Seedance 2.0 Real Vertical Slice

## Goal
Connect one **real** Seedance provider through canonical planning/compiler/job/spend/QA/revision/finalization flow.

## Mandatory prerequisites
TASK-019..029 (using the canonical non-numeric order that places TASK-024 after TASK-028) plus **TASK-032 Durable Jobs and TASK-033 SpendAuthorization/PaidAttemptGuard plus TASK-024 guarded keyframes and TASK-034 QA must be implemented before the first billable Seedance submission**.

## Exposure restriction
This phase uses controlled internal/staging test projects and approved test assets. Do **not** expose arbitrary public/commercial user traffic merely because a paid provider path works. Public beta requires TASK-042 rights/security/privacy/operations and TASK-043 release gate.

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
- GS01 and GS03 controlled real smoke path;
- QA-triggered automatic paid regeneration impossible;
- accepted output can seed dependent next shot.

A successful API response alone does not complete this task; Phase 2 exit additionally requires Tasks 034–037.

## Binding execution and verification packet

Dependencies: TASK-034. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/universal_video_spec.schema.json`
- `schemas/paid_attempt.schema.json`
- `schemas/artifact.schema.json`
- `schemas/qa_report.schema.json`

Requirements: R-030, R-040, R-069.
Golden coverage: GS01, GS03, GS10.

- [ ] Run controlled explicitly budgeted GS01/GS03 real attempts through already validated jobs, guard, compiler and QA; preserve exact upstream outputs and costs.
- [ ] No credentials/budget means BLOCKED for real smoke, not success with fixtures. Phase 2 completion additionally requires revision/timeline/voice evidence from later tasks.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
