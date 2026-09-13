# TASK-017 — Dialogue Voice Localization

## Goal
Implement structured dialogue, VoiceBible, pronunciation and localization.

## Read first
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Voice identity separate from language
- Proper nouns stable
- Subtitle-only edits do not regenerate video

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-016. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/17_SHOT_REVISION_VERSIONING.md`
- `schemas/dialogue_scene.schema.json`
- `schemas/voice_profile.schema.json`

Requirements: R-008.
Golden coverage: GS07, GS11, GS17.

- [ ] Create language variants with speaker identity, pronunciation/source line IDs and timing constraints; provider handles remain scoped mappings.
- [ ] Distinguish subtitle typo, unrendered text and baked spoken dialogue; only actual voice/lip-sync dependencies invalidate accepted visuals.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.

## Language and directing regression acceptance (4.5.0)
- [ ] Resolve `schemas/project_intent.schema.json` studio_audio under spec/09 precedence, preserving original script and linked localized lines. Test literal quoted-script ambiguity, mixed explicit per-line language, no speech, inherited language, and conflicting UI/chat edits. Reject vi/vi-VN native selection under studio-audio-v1 and never turn locale into speech language.
- [ ] Prove resolution=NEEDS_CONFIRMATION cannot reach a paid plan; accepted language changes use versioned selective dependencies and cannot reuse stale authorizations. This task validates planning without submitting paid media.
