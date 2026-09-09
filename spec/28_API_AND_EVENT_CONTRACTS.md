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
`job.state_changed` (typed previous/current DurableJob status; polling is progress, not another state)
`paid_attempt.estimated|approved|submitted|reconciled|charged|failed`
`shot.version_created|qa_completed|accepted|rejected`
`canon.version_created`

## Idempotency
User command retries and network retries must not create duplicate paid attempts. Mutation endpoints accept command/idempotency identity when semantics allow.

## Error contract
Structured errors include code, user-safe message, retryability, paid-state certainty (`NOT_SUBMITTED | SUBMITTED | UNKNOWN | FAILED_UNBILLED_CONFIRMED | BILLED_OR_OUTPUT_PRODUCED`), provider correlation ID where available, and remediation options.

## UI contract
UI reconstructs progress from durable project/job state plus events. Missing websocket/SSE messages cannot be the sole source of truth.

## Mutation and event consistency
Mutations carry command_id, expected resource version and authenticated project scope. A repeated command returns the original effect/result; conflicting payload reuse returns a conflict. The committed state and outbox event are atomic. Sequence is monotonic per project stream; clients deduplicate event_id and refetch durable state on gaps. Event payloads are versioned typed records; job.state_changed carries the canonical job vocabulary. Provider status strings remain adapter metadata only. Retriable error describes recovery of the current command; it never independently authorizes a new billable attempt. Material events link the affected resource version and attempt/authorization where relevant.

Wire payload shape is the versioned resource-event record in schemas/event_envelope.schema.json: resource_type/id/version, message, optional job status transition/error and related IDs. Resource state itself is fetched from durable typed contracts; adapters must not invent competing inline payload shapes. A new payload variant requires a versioned schema change. `run_id=null` is allowed for project mutations outside a run but the field is present.

## Localization commands after the core release
`spec/47_SOURCE_VIDEO_LOCALIZATION.md` defines CreateLocalizationVariant, Get, Check, ApplySafeReview, SynthesizeSelectedSegments and Export. Use `schemas/localization_project.schema.json` and `schemas/localization_review.schema.json` for resources. Every mutation keeps existing command identity, ownership, expected-version and outbox semantics. Resource types localization_project/localization_review fit the existing versioned resource envelope; no alternative inline event body or job state vocabulary. Backend capability/spend checks enforce forbidden media routes independently from the UI.
