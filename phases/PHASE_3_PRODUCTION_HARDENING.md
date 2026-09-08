# Phase 3 — Production Hardening

## Goal
Make real paid generation safe and recoverable.

## Focus
Durable jobs, cancellation, upstream task reconciliation, idempotency, spend caps, artifact currency/dependencies, provider failure handling, observability, security and backup/restore.

## Exit gate
- GS08–GS10 and relevant failure-injection tests pass;
- process restart resumes submitted jobs without duplicate billing;
- uncertain submit enters RECONCILING;
- global/project/user/provider spend caps work;
- paid-attempt audit trail complete;
- backup restore path demonstrated.
