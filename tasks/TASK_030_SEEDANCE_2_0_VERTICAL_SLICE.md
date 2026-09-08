# TASK-030 — Seedance 2.0 Vertical Slice

## Goal
Connect one **real** Seedance provider end-to-end through canonical planning/compiler/cost/QA/revision flow.

## Read first
- `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md`
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `profiles/models/seedance_2_0.yaml`

## Acceptance criteria
- real provider paid path, no production mock fallback;
- UniversalVideoSpec → Seedance compiler → provider adapter provenance stored;
- explicit reference positive/negative bindings;
- stage/end-state compilation;
- cost/approval guard before submission;
- GS01 and GS03 real smoke path;
- no QA-triggered automatic paid regeneration.
