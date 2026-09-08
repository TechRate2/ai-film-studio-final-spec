# API and Event Contracts

Concrete route names may adapt to the implementation stack; semantics are canonical.

## Command/query separation
Queries never create paid attempts. Commands that may spend credits declare estimated incremental cost and require the applicable approval/spend policy.

## Core semantic operations
- create/read/update project intent and policy;
- attach/import reference media;
- analyze/group references and approve/correct roles;
- run/resume Director planning;
- fetch artifacts/canon/entities/scenes/shots/versions;
- request keyframe pack/import external keyframe;
- estimate generation cost;
- submit paid generation attempt;
- accept/reject shot version;
- request contextual revision;
- cancel/reconcile job;
- export final composition;
- continue episode/series.

## Event envelope
All asynchronous events carry:
`event_id`, `event_type`, `project_id`, `run_id`, optional `job_id/shot_id/version_id/attempt_id`, `sequence`, `occurred_at`, `payload_version`, `payload`.

## Important event types
`director.started|progress|checkpoint|required_input|completed|failed`
`artifact.created|stale|validated|accepted|rejected`
`job.queued|submitted|polling|completed|failed|cancelled|reconciling`
`paid_attempt.estimated|approved|submitted|reconciled|charged|failed`
`shot.version_created|qa_completed|accepted|rejected`
`canon.version_created`

## Idempotency
User command retries and network retries must not create duplicate paid attempts. Mutation endpoints accept command/idempotency identity when semantics allow.

## Error contract
Structured errors include code, user-safe message, retryability, paid-state certainty (`NOT_SUBMITTED | SUBMITTED | UNKNOWN`), provider correlation ID where available, and remediation options.

## UI contract
UI reconstructs progress from durable project/job state plus events. Missing websocket/SSE messages cannot be the sole source of truth.
