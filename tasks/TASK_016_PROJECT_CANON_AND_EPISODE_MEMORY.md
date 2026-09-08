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
