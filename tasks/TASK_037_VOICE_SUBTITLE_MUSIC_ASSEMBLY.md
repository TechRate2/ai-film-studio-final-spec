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
