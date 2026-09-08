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
