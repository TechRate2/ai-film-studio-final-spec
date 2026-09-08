# TASK-018 — Performance Camera Audio Editorial

## Goal
Implement structured directing passes for blocking/camera/audio/edit.

## Read first
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
- Dialogue scenes include blocking
- Camera has narrative function
- Editorial decisions separate from execution

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-017. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/10_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md`
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `schemas/universal_video_spec.schema.json`
- `schemas/dialogue_scene.schema.json`

Requirements: R-009, R-081.
Golden coverage: GS02, GS03, GS07, GS13.

- [ ] For dialogue and action fixtures persist playable intention, body/prop positions, eyelines, narrative camera function and audio/editorial decision.
- [ ] Compare a motivated hold with a cut/move alternative; reject contradictory screen geography and excessive simultaneous choreography without measured support.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
