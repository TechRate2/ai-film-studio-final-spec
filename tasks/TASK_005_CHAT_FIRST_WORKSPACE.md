# TASK-005 — Chat First Workspace

## Goal
Implement the minimal chat-first project workspace, global VN/EN UI locale, uploads, progress and artifact previews without exposing pipeline complexity.

## Read first
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/30_UI_STATE_MACHINE.md`
- `spec/27_DOMAIN_DATA_MODEL.md`

## Acceptance criteria
- one primary composer surface;
- global `ui_locale` supports Vietnamese and English;
- UI locale is independent from script/dialogue/subtitle/output language;
- switching UI locale does not mutate project creative state;
- project-scoped persisted uploads;
- progressive advanced controls;
- progress reconstructable from durable state/events;
- shot/artifact preview states represented without fake completion;
- external-keyframe/revision surfaces can be added without redesigning workspace.

Follow `AGENTS.md` task protocol and report exact UI/API/state/test evidence.

## Binding execution and verification packet

Dependencies: TASK-004. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`
- `spec/30_UI_STATE_MACHINE.md`
- `schemas/project_intent.schema.json`
- `schemas/event_envelope.schema.json`

Requirements: R-023, R-029, R-076.
Golden coverage: GS08, GS09, GS11.

- [ ] Exercise vi/en composer, attachment, progress, blocked/error and preview states through persisted API data; reload reconstructs the same project.
- [ ] Locale-only mutations leave canon, request hashes, voices and output language unchanged; reconnect with duplicate/out-of-order events cannot show false completion.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
