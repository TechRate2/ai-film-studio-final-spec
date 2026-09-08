# TASK-016 — Project Canon, Episode Memory and ActiveContextPack

## Goal
Implement versioned project/series truth and scoped retrieval that survives sessions/episodes without context dumping.

## Read first
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/project_canon.schema.json`
- `schemas/active_context_pack.schema.json`
- `schemas/episode_snapshot.schema.json`

## Acceptance criteria
- canon versioned and distinct from chat transcript;
- ActiveContextPack contains only active/relevant facts/entities/relationships/refs;
- episode acceptance commits a durable snapshot and unresolved threads;
- retcon selectively marks dependencies stale;
- same recurring identity/voice refs are reusable without re-upload;
- source versions included so stale context can be detected;
- full Series Bible is never default input to every shot.

## Binding execution and verification packet

Dependencies: TASK-015. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/project_canon.schema.json`
- `schemas/active_context_pack.schema.json`
- `schemas/episode_snapshot.schema.json`

Requirements: R-006, R-031, R-037, R-046, R-085.
Golden coverage: GS05, GS27.

- [ ] Atomically commit episode/master/canon/voice/state pins and resume a later episode with a small relevant ActiveContextPack.
- [ ] Crash during commit and race a retcon against retrieval; stale version packs reject mutation and missing required locks are not silently truncated.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
