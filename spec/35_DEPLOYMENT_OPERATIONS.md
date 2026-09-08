# Deployment and Operations

Concrete infrastructure follows repository reality, but production semantics are fixed.

## Required components
Application/API, durable worker/job runtime, relational persistence, private object/media storage, queue/event transport where needed, FFmpeg/media worker, secrets management and observability.

## Environments
Local/dev, test, staging and production use separate credentials/storage/data. Paid-provider test usage is explicit and capped.

## Reliability
Jobs persist heartbeat/state/upstream IDs and recover after process restart. Events are replayable/reconstructable from durable state. Provider outages degrade visibly rather than corrupting project state.

## Observability
Structured logs/metrics correlate `project_id`, `run_id`, `job_id`, `attempt_id`, `provider`, `model`, latency, result status and cost. Never log provider secrets or unnecessary private media payloads.

## Backup/restore
Back up database/canon/metadata and media object references according to retention policy. Beta gate requires a tested restore path, not merely backup configuration.

## Migration
Persistent schema migrations are reviewed and reversible/forward-safe where practical. Long-running media jobs must tolerate deploys or be safely resumable.

## Spend incident controls
Ability to disable a provider/model, pause paid queue, enforce global/user/project caps and audit every billable attempt.
