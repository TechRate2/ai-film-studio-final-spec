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
