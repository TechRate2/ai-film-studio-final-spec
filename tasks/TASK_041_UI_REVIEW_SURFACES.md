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
