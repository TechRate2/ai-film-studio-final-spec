# TASK-041 — UI Review Surfaces

## Goal
Polish artifact/shot/version/revision/keyframe/cost review UX without losing chat-first simplicity or VN/EN localization.

## Read first
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/30_UI_STATE_MACHINE.md`

## Acceptance criteria
- default UI stays simple and chat-first;
- advanced Director details/cost/evidence available progressively;
- version accept/revert consequences clear;
- shot revision input works in supported UI locales;
- Vietnamese and English cover user-facing workspace/review/progress/error states;
- switching UI locale does not change content/output language;
- external keyframe prompt/ref/upload flow remains clear;
- WAITING_USER/BLOCKED/STALE/FAILED_PARTIAL states are actionable, not raw provider logs.

## Required report
- current reality before task;
- files/state/API/UI changes;
- localization and state tests;
- Golden scenarios affected;
- remaining accessibility/provider limitations.

## Binding execution and verification packet

Dependencies: TASK-040. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`
- `spec/30_UI_STATE_MACHINE.md`
- `schemas/event_envelope.schema.json`
- `schemas/revision_request.schema.json`

Requirements: R-023, R-029, R-076.
Golden coverage: GS08, GS09, GS11.

- [ ] Exercise accept/revert/revision/keyframe/cost details and error/reconciliation/stale states in vi/en through real persisted APIs.
- [ ] Reload and out-of-order events preserve version/cost truth; raw provider errors do not replace actionable localized state and no advanced knobs are mandatory.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
