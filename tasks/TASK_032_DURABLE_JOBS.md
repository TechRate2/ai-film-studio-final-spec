# TASK-032 — Durable Jobs

## Goal
Implement resumable/cancellable/observable media execution that survives process restarts and is safe enough to precede the first real paid video task.

## Read first
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`

## Acceptance criteria
- job state durable;
- upstream task IDs persisted as soon as known;
- process restart resumes polling rather than resubmitting;
- cancellation semantics explicit and provider-aware;
- dependency/rate/spend limits respected;
- ambiguous submission enters RECONCILING;
- provider callback/webhook path is idempotent and authenticated where applicable;
- events are not sole source of truth;
- failure injection proves restart/timeout/callback duplication do not create duplicate media jobs.

This task is a prerequisite of any production billable Seedance smoke test.
