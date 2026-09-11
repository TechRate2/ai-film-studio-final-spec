# Quality Gates and QA

## Pre-generation gates
### Creative
Purpose/hook/payoff, narrative clarity and retention logic.

### Production
Active characters/refs, canon/current state, provider capability, duration/event density, camera/action feasibility, dialogue/audio feasibility and continuity feasibility.

### Cost
Cheaper equivalent route? Is keyframe justified? Spend cap? Expected accepted-second economics?

## Post-generation QA
Semantic/action correctness, identity/reference fidelity, product/prop fidelity, anatomy/visual corruption, dialogue/audio correctness, continuity, camera and story/end state.

## Severity
`FATAL`: unusable/corrupt/wrong scene.  
`MAJOR`: identity/product/action/end-state failure.  
`MINOR`: acceptable imperfection.

QA failure does not automatically create a paid retry. It produces diagnosis and recommended revision options.

## Human review
Policy may auto-accept high-confidence low-risk results, but users can inspect and override any shot/version.

## Acceptance integrity
`ACCEPTABLE` is forbidden when severity is MAJOR/FATAL or any required check is FAIL/UNKNOWN. `schemas/qa_report.schema.json` enforces this contradiction veto; a high average or fluent diagnosis cannot override it. USER_REVIEW, REVISE and BLOCKED are diagnoses/routes, never permission for a paid generation.

Before accepting a version, the domain service derives the required check set from the pinned policy, artifact modality, user hard constraints and incoming/outgoing continuity. Check names must be unique and complete for that set; a producer/LLM cannot omit a failing check, mark it optional or invent an inapplicability exemption. Missing required evidence yields UNKNOWN and review/block. An optional UNKNOWN does not automatically veto an otherwise valid artifact. A schema-valid report alone does not prove acceptance eligibility, rights, currency or ownership.

Automatic acceptance additionally requires evaluator calibration for the exact declared scope under `evals/BENCHMARK_RUBRIC.md`; self-reported LLM confidence is insufficient. Review the assembled scene as well as individual clips where meaning, speaker turns or continuity depend on their relationship. User preference can accept permitted minor aesthetic imperfections but cannot waive safety, rights, factual hard constraints or silently release a broken dependent shot. Preserve the original QA report and any subsequent review decision separately.
