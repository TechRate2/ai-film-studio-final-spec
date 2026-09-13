# TASK-037 — Voice, Subtitle, Music, Composition Timeline and Final Master

## Goal
Implement controlled audio routes and deterministic final assembly with production export QA.

## Read first
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/10_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/voice_profile.schema.json`
- `schemas/composition_timeline.schema.json`
- `schemas/final_master.schema.json`

## Acceptance criteria
- at least one real production-supported VoiceProvider/TTS route exists for controlled post voice, even if some video models provide native audio;
- voice identity remains separate from language;
- visual remains unchanged for audio-only/subtitle-only edit unless explicit lip-sync route requires visual work;
- CompositionTimeline persists accepted clip versions, audio/subtitle/transition decisions and export target;
- final assembly reproducible from timeline;
- FinalMaster QA validates duration/aspect/codec, missing/duplicate/corrupt ranges, A/V sync, subtitle timing/safe area and audio integrity;
- output checksum/provenance persisted;
- deterministic no-paid fixes may auto-run; new paid generative media follows authorization/revision rules.

## Binding execution and verification packet

Dependencies: TASK-036. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/10_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/voice_profile.schema.json`
- `schemas/composition_timeline.schema.json`
- `schemas/final_master.schema.json`
- `schemas/qa_report.schema.json`

Requirements: R-051, R-052, R-053, R-057, R-075, R-088.
Golden coverage: GS16, GS17, GS19, GS21, GS27.

- [ ] Compile typed tick/rational timeline with independent voice/music/subtitle/graphics, trims/holds/speed/transitions and version-pinned sources.
- [ ] Reject out-of-bounds ranges, accidental holes/duplicates, stale/unaccepted sources and required UNKNOWN QA; finalization races recheck pins before COMPLETE. Real controlled voice requires explicit safe smoke.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.

## Language and directing regression acceptance (4.5.0)
- [ ] Read `schemas/project_intent.schema.json`; test no-speech zero voice/sync, qualified zh/en native, controlled vi narration, and controlled character speech with sync off/on. Off causes zero additional lip-sync/mouth-animation calls; visible mismatch requires explicit acknowledgment and cannot pass a requested lip-match check. On requires qualified speaker/face association and complete cost authorization before any voice/sync/video dependency.
- [ ] Imported acceptable speech avoids TTS; hybrid audio has one speech owner. New TTS result accepted/pinned before an audio-dependent video; failure or changed preference does not release children or auto-regenerate. Final QA reports actual languages, pronunciation and sync/limitation. Real evidence is required before enabling each route.
