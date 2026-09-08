# Cost, Spend Authorization and Paid Attempt Policy

## Cost hierarchy
Typical relative cost: LLM/search << image/keyframe << video. Spend low-cost intelligence before expensive media when it can improve acceptance.

## Cost accounting
Track research, LLM, image, video, voice, edit/compute and storage/bandwidth separately. Primary metric: `cost_per_accepted_second`.

## Estimate → authorization → attempt
1. build CostEstimate for planned production;
2. user Create/plan approval creates scoped SpendAuthorization/hard cap;
3. planned first attempts execute within authorization;
4. every paid provider submission becomes a PaidAttempt linked to the authorization/logical attempt.

This avoids confirmation before every planned shot without permitting blind retries.

## Candidate policy
Default candidate count is 1. Multiple candidates must be deliberately planned and costed before authorization; the Agent may not silently request N outputs “for quality.”

## PaidAttemptGuard
Each paid attempt stores attempt_id, artifact/shot/version, logical attempt ID, authorization ID, provider/model, upstream_task_id, idempotency key if available, prompt/reference hashes, estimate, actual cost, status, paid-state certainty and timestamps.

## Retry/recovery semantics
- Polling/recovering an already-created upstream task may be automatic.
- Confirmed NOT_SUBMITTED/FAILED_UNBILLED_CONFIRMED logical submission may be retried within existing authorization according to provider policy.
- `SUBMITTED` means resume/reconcile the same upstream task.
- `UNKNOWN` means reconcile before resubmission.
- After output/charge, another generative media attempt is a new revision/attempt and needs applicable user-directed authorization.
- QA never auto-creates a new paid media attempt.

## Spend caps
Configurable per project, user, day, provider and global/attempt type as product scale requires.

## UI
Show estimated project cost before authorization, spent/remaining cap during run and incremental cost before paid revisions.

## Enforced policy
`AUTO_MEDIA_REGENERATION = OFF` is fixed product policy, not a configurable quality mode. It applies to image, video, voice, lip-sync and any billable generative repair/probe. QAReport requires `auto_paid_retry_allowed=false`. A paid-state result alone does not authorize a new call. Polling is automatic only within bounded rate/time policy and the existing upstream task identity.

## Machine-checkable invariants
```json
{
  "auto_paid_retry_allowed": false
}
```
