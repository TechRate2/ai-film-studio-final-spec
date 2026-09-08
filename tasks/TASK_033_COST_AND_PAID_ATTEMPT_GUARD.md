# TASK-033 — Cost and Paid Attempt Guard

## Goal
Implement cost estimates, approval/spend policy, idempotency and upstream reconciliation for every billable generation.

## Read first
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `schemas/paid_attempt.schema.json`

## Acceptance criteria
- estimated cost visible before applicable paid action;
- project/user/provider/day caps enforced;
- each paid attempt has stable identity/hash/provenance;
- uncertain submission never causes blind second submit;
- polling/recovery of same upstream task is distinguished from new generation;
- actual cost/reconciliation auditable;
- `cost_per_accepted_second` computable.
