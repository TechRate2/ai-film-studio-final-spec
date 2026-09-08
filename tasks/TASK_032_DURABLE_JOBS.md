# TASK-032 — Durable Jobs

## Goal
Implement resumable/cancellable/observable media execution that survives process restarts.

## Read first
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`

## Acceptance criteria
- job state durable;
- upstream task IDs persisted as soon as known;
- process restart resumes polling rather than resubmitting;
- cancellation semantics explicit;
- dependency/rate/spend limits respected;
- ambiguous submission enters RECONCILING;
- events are not sole source of truth.
