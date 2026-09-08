# TASK-039 — Golden Scenario Automation

## Goal
Turn canonical behavioral scenarios into regression gates that prevent future Codex/Claude/provider changes from violating product semantics.

## Read first
- `evals/GOLDEN_SCENARIOS.md`
- `spec/34_TEST_AND_EVAL_STRATEGY.md`
- `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md`

## Acceptance criteria
- all non-paid deterministic scenarios runnable in CI with fixtures/test doubles only in test environment;
- paid/provider smoke tests explicitly opted in and capped;
- core invariants (no silent paid retry, dependent sequencing, version preservation, scoped context, capability resolution, artifact currency) have deterministic assertions;
- Smart Auto internal keyframe, controlled voice, asset-ingestion failure, final-master QA, provider fallback certainty and accepted-version revert scenarios covered;
- test report maps failures to requirement IDs;
- production code cannot substitute test fake media fallback.
