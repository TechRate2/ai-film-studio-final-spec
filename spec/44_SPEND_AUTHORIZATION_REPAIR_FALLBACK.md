# Spend Authorization, Repair and Provider Fallback Semantics

## Goal
Allow efficient autonomous production without asking before every planned shot, while guaranteeing no blind paid retries.

## SpendAuthorization
When user presses Create/approves a plan, create a scoped authorization containing:
- project/run scope;
- approved modalities/providers/models or router policy;
- estimated total and hard cap;
- planned first-attempt count/candidate count;
- expiry/cancellation state.

Planned first attempts within the authorization may execute automatically. This is different from a new retry after a generated result.

## New paid attempt rules
A new billable attempt after a quality result/rejection requires explicit user-directed revision/action unless it was already an explicitly authorized multi-candidate plan.

Default candidate count is one. `candidate_count > 1` must be deliberately planned, costed and visible before authorization.

## Non-paid repair
Deterministic edit, subtitle timing, metadata, muxing, safe transcode or other non-generative repair may run automatically when it preserves creative intent and does not create a new billable generative task.

## Provider submission certainty
Normalize outcome certainty:
- `NOT_SUBMITTED`: provider confirms no task created; same logical authorized attempt may be submitted/retried without treating it as quality retry;
- `SUBMITTED`: upstream task exists; resume/reconcile, do not submit duplicate;
- `UNKNOWN`: reconcile before any resubmission;
- `FAILED_UNBILLED_CONFIRMED`: same logical authorized attempt may be re-executed according to policy;
- `BILLED_OR_OUTPUT_PRODUCED`: any additional generation is a new attempt/revision and requires applicable user authorization.

## Provider fallback
Do not silently switch to another billable provider after a charged/produced result. If initial submission never occurred or was confirmed unbilled, fallback may consume the same authorization only if capability, price ceiling and user/provider policy allow it. Otherwise show the new route and incremental cost.

## Revert/revision
Switching accepted shot versions re-evaluates downstream dependencies; it does not automatically regenerate stale paid artifacts.
