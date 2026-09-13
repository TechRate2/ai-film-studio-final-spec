# Dialogue, Voice and Localization

## DialogueScene
Structured fields: speaker, listener/reaction target, spoken line, emotion, subtext, pace, pause, eyeline, intent and unresolved turn. Dialogue is separate from visual description.

## VoiceBible
Per recurring speaker: voice_id, provider voice ID if applicable, reference audio, timbre/profile, pace/pitch/register, accent, emotional range, language support and pronunciation lexicon.

Voice identity and language are separate.

## Localization
Maintain a canonical script language. Localized variants preserve meaning, personality, formality/relationship, timing, lip-sync constraints and proper-noun pronunciation.

## Pronunciation Lexicon
Persist names, places, invented terms and domain terms. Recurring names must not change pronunciation across episodes.

## Audio route selection
Within the approved Studio language/voice/sync policy below, per scene/shot choose native model dialogue/audio, reference-audio-conditioned video, controlled TTS + post lip-sync, speech-to-video/character animate, or hybrid native ambience + controlled voices. Choose by benchmarked reliability and cost, not a global default.

## Language and audio dependencies
Use language tags independently for ui_locale, canonical_script_language, dialogue_language and subtitle_language. Provider voice handles map to canonical speaker identity and exact provider/model/version; changing providers cannot silently pick a different voice. Unsupported language/pronunciation remains UNKNOWN or UNSUPPORTED. A translation creates a script variant with source line IDs; it does not overwrite canon. Validate localized duration against the accepted visual window before buying voice or lip-sync. Moving a line may require subtitle/timeline changes; baked native speech or lip motion cannot be removed with a text-only edit. Preserve isolated stems when available; if not available, disclose the extraction/remix limitation before choosing the cheapest valid repair.

## Original-video localization boundary
The standalone LOCALIZATION workflow follows `spec/47_SOURCE_VIDEO_LOCALIZATION.md`. It reuses voice identities and timelines but explicitly excludes the lip-sync/video-generation options available to STUDIO. Route by workflow_kind before exposing tools. TTS availability at an aggregator does not establish access to a vendor's complete dubbing, transcript-editing or voice-cloning API. AtlasCloud is the owner's intended initial integration candidate; verify exact route, language, billing and entitlement independently. Do not promote a language or provider claim from this preference.

## Studio language preference contract (ADR 0005)
`schemas/project_intent.schema.json` defines `studio_audio`; it is a provider-neutral preference snapshot, not an authorization or selected provider route. Fields: policy_version, speech_mode, dialogue_language, language_origin, subtitle_language, voice_method, lip_sync_requested, accept_unsynced_visible_speech, resolution. Script language and original dialogue remain in their existing canonical records; language variants retain source line IDs. `ProjectIntent.language` is a legacy content hint, not an independent authority to override studio_audio/dialogue variants.

New STUDIO projects propose Mandarin Chinese (`zh-CN`) only when speech is needed and no explicit/inherited language exists. Initial controls display that preset even with Vietnamese UI or request prose; no claim about model superiority follows. Preserve an existing project's/episode's language unless the user explicitly changes it. A no-speech request resolves speech_mode=NONE, null dialogue_language, voice_method=NONE and both lip flags false; do not invent a speaker to satisfy a default. Subtitle language defaults to null (Off). Speech modes NARRATION and DIALOGUE distinguish off-screen narration from character speech; mixed scenes resolve in per-shot plans under the approved snapshot.

Explicit user output-language instructions (including named line-language exceptions) outrank the preset; inherited canon outranks a new-project preset. A clearly later deliberate edit updates the preference and preview as a versioned command. Simultaneous conflicting explicit UI/chat/script locks, unclear quoted-script language intent or ambiguous requests set resolution=NEEDS_CONFIRMATION; ask one focused question before paid production. Ordinary Vietnamese descriptive prose is not an explicit demand for Vietnamese speech. A requested translation creates a variant, never overwrites the source script. ui_locale changes no content/voice fields.

### Voice and mouth policy
Initial policy `studio-audio-v1`: zh/en speech proposes NATIVE where qualified, with CONTROLLED available as an explicit costed alternative. Vietnamese language tags (`vi` and subtags, case-insensitive) use CONTROLLED: qualified TTS or validated imported speech. This is an owner-selected launch policy, not a claim that Vietnamese native generation is impossible. Other exposed languages use qualified per-operation routes; unsupported/UNKNOWN selections remain visible but unavailable to spend, never substituted. A future policy change needs evidence and a new policy version; old approved plans remain pinned.

Choosing Vietnamese visibly selects the controlled-voice method and updates the estimate; Create approval authorizes only its enumerated first voice attempts. Reuse acceptable user audio before synthesizing. The optional 'Khớp môi / Lip sync' checkbox is off by default and only relevant to controlled character speech. A natural-language explicit lip-sync request can set it, with the same visible cost preview; ambiguity cannot enable it. NARRATION does not require a talking mouth. NATIVE can include synchronized speech inside the video call; the checkbox governs additional controlled speech-to-mouth operations, not a promise to disable the native model's natural mouth motion.

With controlled speech and lip_sync_requested=false, make zero additional lip-sync/speech-driven mouth-animation calls. Keep requested visual intent: do not silently turn a close-up conversation into B-roll, hide faces, change camera or remove speech. An existing user mouth-match constraint blocks an unsynchronized plan. If visible speech remains without such a guarantee, disclose the expected mismatch and require accept_unsynced_visible_speech=true through explicit user acknowledgment before approval; turning the checkbox off alone is not that acknowledgment. This permits ordinary dubbing as an informed choice, not false 'lip-sync passed' QA. If lip sync is selected, qualify target language, face count/pose/occlusion/speaker association, voice duration and route quality; unsupported multi-speaker synchronization blocks or proposes an explicit alternate, never silently picks the first face.

### Binding and pre-spend checks
New Studio plans must resolve and persist studio_audio before authorization; legacy drafts may omit it until resolved. resolution=NEEDS_CONFIRMATION forbids all media submissions for that plan. UI preview shows dialogue language, subtitle language/Off, native versus controlled voice, optional sync, any unsynchronized-mouth limitation and itemized total (video, voice, sync, image/post when used). Plan/request hashes pin these choices and the actual per-line language/voice/audio assets. Check ProjectIntent scope, actual DialogueScene languages, VoiceProfile capability, UV audio and compiled request against the same snapshot. A changed language, voice method, sync or source-line text invalidates only affected estimates/authorization/derived assets; no automatic paid replay. Read-only estimates/preview never authorize synthesis.

Only explicit accepted line variants may differ from the project default. Mixed-language scripts retain line tags and undergo per-line route qualification; the compiler cannot translate every line to the project default. Final QA evaluates spoken language/pronunciation, intended speaker, sync requirement or recorded limitation and subtitle language independently.

## Machine-checkable invariants
```json
{
  "studio_default_dialogue_language": "zh-CN",
  "studio_default_subtitle_language": null,
  "studio_lip_sync_default": false,
  "studio_audio_policy_version": "studio-audio-v1"
}
```
