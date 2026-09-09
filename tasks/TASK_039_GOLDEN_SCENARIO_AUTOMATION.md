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

## Binding execution and verification packet

Dependencies: TASK-038. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `spec/34_TEST_AND_EVAL_STRATEGY.md`
- `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md`
- `schemas/common.schema.json`

Requirements: R-033, R-079.
Golden coverage: GS01, GS05, GS08, GS09, GS10, GS15, GS26.

- [ ] Run deterministic behavioral tests for every Golden and map each assertion to requirements; paid smoke is separately opted in with credentials and capped plan.
- [ ] Tests begin within each earlier task, not deferred here. Mutate critical contracts/fixtures to prove negative assertions catch drift, rather than only asserting schema parsing.
- [ ] Deleting a task-index packet, duplicating its path, deleting/duplicating a fixture, or removing all negative cases fails governance. Preserve fixture-to-requirement/Golden mappings and distinguish schema-record validation from runtime orchestration tests.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
