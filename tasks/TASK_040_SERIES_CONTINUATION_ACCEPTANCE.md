# TASK-040 — Series Continuation Acceptance

## Goal
Prove multi-episode canon/reference/voice/knowledge/continuity behavior with recurring cast.

## Read first
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `evals/GOLDEN_SCENARIOS.md`

## Acceptance criteria
- GS05 passes into Episode 2;
- no re-upload of valid canonical refs required;
- active context scoped;
- character knowledge asymmetry remains correct;
- voice/pronunciation/outfit/injury/prop state persists;
- retcons/selective staleness behave correctly.

## Binding execution and verification packet

Dependencies: TASK-039. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md`
- `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md`
- `spec/32_LONG_FORM_SERIES_PLAYBOOK.md`
- `schemas/episode_snapshot.schema.json`
- `schemas/active_context_pack.schema.json`
- `schemas/character.schema.json`

Requirements: R-031, R-085.
Golden coverage: GS05, GS27.

- [ ] Continue Episode 2 with at least 10 registered characters and only the relevant active subset, preserving voice, props, injury, knowledge and unresolved promises.
- [ ] Restart with no chat; flashback, alias collision, late reveal and retcon must not leak knowledge or require valid canonical refs to be reuploaded.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
