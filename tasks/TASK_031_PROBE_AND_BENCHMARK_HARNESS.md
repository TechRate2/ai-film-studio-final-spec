# TASK-031 — Probe and Benchmark Harness

## Goal
Measure model/provider behavior and feed scenario-scoped evidence into routing.

## Read first
- `spec/37_MODEL_PROBE_PLAYBOOK.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `evals/BENCHMARK_RUBRIC.md`
- `prompts/REAL_PROVIDER_BENCHMARK_PROMPT.md`

## Acceptance criteria
- reference/timing/default/duration/ref-ceiling/audio probes represented;
- exact profile/compiler/provider/input provenance;
- results versioned with sample scope/confidence;
- cost, latency and accepted seconds stored;
- Router can consume measured metrics;
- paid benchmark samples explicitly budgeted, never auto-retried.

## Binding execution and verification packet

Dependencies: TASK-037. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/37_MODEL_PROBE_PLAYBOOK.md`
- `schemas/model_profile.schema.json`
- `schemas/provider_profile.schema.json`
- `schemas/qa_report.schema.json`
- `schemas/cost_estimate.schema.json`

Requirements: R-024, R-036, R-065, R-083.
Golden coverage: GS03, GS04, GS14, GS15.

- [ ] Version samples with exact input/output/route/profile/compiler/cost and human/automated rubric results; failed billed samples remain in aggregate cost.
- [ ] No sample or zero accepted seconds yields unknown/null economics, not perfect acceptance. New paid samples require planned authorization; CI does not call providers.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
