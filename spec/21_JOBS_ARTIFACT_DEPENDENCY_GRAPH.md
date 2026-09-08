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

## Versioned artifacts
Every artifact has project_id, artifact_id, version_id, currency, acceptance and immutable provenance. Provenance discriminates INTERNAL_GENERATED, EXTERNAL_IMPORTED and DETERMINISTIC_DERIVED; imported assets may have unknown external tools/costs but retain uploader/source/hash/rights assertions. Internally paid media requires attempt, authorization, exact spec/profile/compiler/request/ref/result hashes and QA links before acceptance. Pending artifacts have explicit pending provenance; completion validates the stronger generated/imported contract. Source media is never overwritten by proxies, transcodes or corrections.
Currency is orthogonal to job status and acceptance: a successful job may produce rejected or stale media. MISSING means the required bytes/record are unavailable; BLOCKED means a prerequisite/policy prevents use; STALE means consumed inputs changed; CURRENT means dependencies have been validated. Recompute in this order MISSING, BLOCKED, STALE, CURRENT, preserving all diagnostic reasons. CURRENT alone does not imply accepted. Final export requires both.

## Machine-checkable invariants
```json
{
  "artifact_currency": [
    "CURRENT",
    "STALE",
    "MISSING",
    "BLOCKED"
  ]
}
```

DIRECTOR_AUTHORED is the provenance origin for reasoning/planning text and structured decisions; these are not paid-media attempts. They retain model/provider/source/cost attribution under reasoning budget. INTERNAL_GENERATED describes generated media with paid-attempt linkage. Request snapshots validate against the shared request_snapshot contract; embedded provider parameters are intentionally opaque typed JSON owned by the adapter. They never replace the provider-neutral spec or grant execution permission. Snapshot IDs/hashes and attempt provider/model IDs must agree.
