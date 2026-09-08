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

## Atomic authorization and liability ledger
Authorization binds authenticated user action, project/run, plan hash/version, currency, expiry, allowed route policy and enumerated logical candidate slots. `candidate_count` defaults to 1 in planning and is explicit in persisted authorization; each slot has candidate_index, target/version and maximum liability. Extra candidates must be predetermined, not conditional on QA failure. Workers cannot increase slots, caps or expiry. Reapproval creates a new authorization/version; it does not mutate historical consent.
Before any billable network call, atomically validate the authorized slot, active policy/capability/input snapshot and all applicable project/user/day/provider/global caps; reserve worst-case cost and claim a unique submission record under fencing. Enforce uniqueness for command_id and (authorization_id, logical_attempt_id, candidate_index, active execution). Two workers, duplicate Create and fallback race cannot reserve/submit the same candidate twice. Costs/FX/price versions are explicit; an unknown price or unbounded liability blocks paid submission. Estimate is not a cap. Current spend plus outstanding reservations must remain within every applicable cap.
Persist request/hash/idempotency key before sending; persist upstream identity immediately on response. Crash after sending but before identity persistence is UNKNOWN: reconcile via provider idempotency/status lookup, never blindly retry. If the provider cannot establish non-creation, remain BLOCKED/RECONCILING with reserved liability and a user-actionable incident; user pressure is not evidence of no charge. Confirmed unbilled failure may release reservation and retry the same authorized logical candidate according to policy with a new attempt_id and predecessor link. An idempotency key is scoped to an exact provider/account/request; never reuse it for a changed request.
Settlement is append-only, currency-consistent and idempotent. BILLED_OR_OUTPUT_PRODUCED takes precedence even if another response says failed; no automatic fallback. Refund or zero invoice does not erase produced-output history or authorize quality regeneration. Late charges update actual cost and pause further spend if a cap is exceeded; no absolute promise can prevent a provider from misbilling. Cancellation/expiry/kill switch revoke unsubmitted reservations but retain uncertain/submitted liability until reconciliation. Non-paid deterministic repair may still consume compute budget, tracked separately from generation authorization.

## Machine-checkable invariants
```json
{
  "paid_certainty": [
    "NOT_SUBMITTED",
    "SUBMITTED",
    "UNKNOWN",
    "FAILED_UNBILLED_CONFIRMED",
    "BILLED_OR_OUTPUT_PRODUCED"
  ]
}
```
