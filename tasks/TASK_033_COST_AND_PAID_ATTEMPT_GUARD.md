# TASK-033 — Cost, SpendAuthorization and PaidAttemptGuard

## Goal
Implement estimate/authorization/spend/idempotency/reconciliation semantics for every billable generation.

## Read first
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `schemas/cost_estimate.schema.json`
- `schemas/spend_authorization.schema.json`
- `schemas/paid_attempt.schema.json`

## Acceptance criteria
- estimated project/attempt cost visible before authorization;
- pressing Create/approving plan may authorize planned first attempts up to explicit hard cap, avoiding per-shot confirmation spam;
- default candidate count is 1; multi-candidate cost/count is explicit before authorization;
- project/user/provider/day/global caps enforced;
- every billable logical attempt has stable identity/hash/provenance;
- NOT_SUBMITTED/SUBMITTED/UNKNOWN/FAILED_UNBILLED_CONFIRMED/BILLED_OR_OUTPUT_PRODUCED certainty handled explicitly;
- uncertain submission never causes blind second submit;
- polling/recovery distinguished from new generation;
- any new paid quality retry/revision beyond prior authorization requires user-directed action;
- actual cost/reconciliation auditable and `cost_per_accepted_second` computable.

This task is a prerequisite of any production billable Seedance smoke test.

## Binding execution and verification packet

Dependencies: TASK-032. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/cost_estimate.schema.json`
- `schemas/spend_authorization.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-020, R-021, R-024, R-028, R-054, R-055, R-056, R-066, R-069, R-084, R-088.
Golden coverage: GS01, GS04, GS09, GS10, GS16, GS17, GS22, GS24, GS27.

- [ ] Atomically reserve all applicable caps and one authorized candidate slot; persist linkage/hash/request before transport and reconcile append-only settlement.
- [ ] Race duplicate Create/workers/fallback, exceed cap, expire/cancel, refund after output and ambiguous timeout: no blind resubmit, hidden extra candidate or quality auto-retry.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
