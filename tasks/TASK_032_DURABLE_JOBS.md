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

## Binding execution and verification packet

Dependencies: TASK-029. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/job.schema.json`
- `schemas/event_envelope.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-026, R-027, R-028, R-056, R-059, R-069, R-084.
Golden coverage: GS03, GS10, GS22, GS24, GS27.

- [ ] Implement every legal job transition and rejection of illegal transitions; outbox state/events, lease fencing and restart reconciliation are durable.
- [ ] Inject crash before send, after send before task ID, during polling and during cancellation; duplicates/late callbacks cannot resubmit, release children or assume refund.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
