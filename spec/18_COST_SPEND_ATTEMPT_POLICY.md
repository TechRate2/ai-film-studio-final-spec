# Cost, Spend and Paid Attempt Policy

## Cost hierarchy
Typical relative cost: LLM/search << image/keyframe << video. Spend low-cost intelligence before expensive media when it can improve acceptance.

## Cost accounting
Track research, LLM, image, video, voice, edit/compute, storage/bandwidth separately. Primary metric: `cost_per_accepted_second`.

## PaidAttemptGuard
Each paid attempt stores attempt_id, artifact/shot/version, provider/model, upstream_task_id, idempotency key if available, prompt/reference hashes, estimate, actual cost, status and timestamps.

## Retry semantics
- Polling/recovering an already-created upstream task may be automatic.
- A **new paid media attempt** is never silently created after quality rejection.
- User may explicitly request a new version/revision.
- Failed submission with uncertain upstream state must be reconciled before resubmission.

## Spend caps
Configurable per project, user, day, provider and attempt type.

## UI
Show estimated project cost before paid production and incremental cost before revisions.
