# TASK-016 — Project Canon and Episode Memory

## Goal
Implement versioned canon snapshots, scoped retrieval and episode-to-episode state continuation.

## Read first
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/project_canon.schema.json`
- `schemas/character.schema.json`

## Acceptance criteria
- Episode N+1 resumes accepted N state;
- world truth and Character Knowledge State remain distinct;
- retcon creates new canon version and selective staleness;
- no full-bible default context dump;
- canonical identity/default appearance/voice remains separate from observed shot state.
