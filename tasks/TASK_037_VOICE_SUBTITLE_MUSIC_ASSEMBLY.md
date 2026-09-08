# TASK-037 — Voice Subtitle Music Assembly

## Goal
Implement audio routes, subtitle/localization and deterministic final assembly.

## Read first
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/10_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Visual unchanged for audio-only edit
- Final timeline reproducible
- Audio provenance persisted

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any
