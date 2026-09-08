# Jobs, Artifacts and Dependency Graph

## Artifact states
`CURRENT | STALE | MISSING | BLOCKED`

## Artifact provenance
Every generated/imported artifact records project/version ownership, type/role, upstream inputs, source/provider, spec/profile/compiler/prompt versions, cost, QA and timestamps.

## Dependency invalidation examples
- character design change → affected keyframes/storyboards/videos stale;
- subtitle change → raw video generation remains current;
- voice change → audio/lip-sync may stale while visuals stay current;
- canon fact change → only dependent scenes stale.

## Durable jobs
Media jobs are resumable, cancellable, observable, idempotency-aware, linked to upstream task IDs and separated by modality channels where useful.

## Concurrency
Scheduler respects dependency graph, provider limits, project spend caps and independent branch parallelism.
