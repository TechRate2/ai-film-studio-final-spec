# Acceptance and Definition of Done

## Feature Definition of Done
A feature is complete only when applicable:
- persistent state/schema + migration implemented;
- domain/service logic complete;
- API/event contract complete;
- required chat-first UI path complete;
- authorization/error states actionable;
- provenance/cost/DecisionRecords captured where material;
- structured logs/metrics added;
- unit/integration/contract tests pass;
- affected Golden Scenarios pass;
- traceability implementation/test refs populated;
- no production TODO/mock fallback bypasses canonical safety/cost/continuity behavior;
- docs/profile evidence updated.

`PARTIAL` is not DONE. A task may be BLOCKED on real-provider evidence instead of pretending success.

## Release gates
### Gate A — Brain Proof
Diverse scenarios produce materially different credible strategies using provider-neutral Director ports, evidence/scoped context and no expensive-video dependency.

### Gate B — Safe Seedance Vertical Slice
Real end-to-end: input/ingestion → research/refs/creative plan → production plan → Durable Jobs + SpendAuthorization → UniversalVideoSpec/compiler/provider → real generation → QA → contextual revision/versioning → continuity → voice/audio → CompositionTimeline → FinalMaster QA/export.

### Gate C — Production Hardening
Restart/timeout/cancel/outage/callback/stale/revert/spend-cap failure injection does not duplicate paid attempts or corrupt state.

### Gate D — Long-form/Series
Multi-character episode continuation preserves canon, Character Knowledge/relationships, voices, scoped context and accepted continuity.

### Gate E — Multi-provider
New providers/models integrate through profiles/compilers/adapters/probes/EffectiveCapability without Director rewrite.

### Gate F — Commercial Beta
All critical CORE traceability requirements have implementation + test evidence; CORE Golden Scenarios pass at their required deterministic/paid levels; rights/privacy/deletion/backup/restore/observability/spend controls are proven; known model/provider limitations are published.

## Release-scoped requirements
The release_gate column in `traceability/REQUIREMENTS_TRACEABILITY.csv` is binding: CORE applies to R-001–R-088, LOCALIZATION to R-089–R-096. TASK-043/Phase 6 must satisfy CORE and GS01–GS28; it does not wait for TASK-044–046. Phase 7 starts only after that gate and requires all LOCALIZATION requirements plus regression of the shared CORE contracts and GS29–GS33. Do not relabel a missing core requirement as extension work. Task files, exact release ID sets and order are pinned in governance/contract_index.json and checked by CI. A passed spec fixture is never implementation evidence.
