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
Per scene/shot choose native model dialogue/audio, reference-audio-conditioned video, controlled TTS + post lip-sync, speech-to-video/character animate, or hybrid native ambience + controlled voices. Choose by benchmarked reliability and cost, not a global default.

## Language and audio dependencies
Use language tags independently for ui_locale, canonical_script_language, dialogue_language and subtitle_language. Provider voice handles map to canonical speaker identity and exact provider/model/version; changing providers cannot silently pick a different voice. Unsupported language/pronunciation remains UNKNOWN or UNSUPPORTED. A translation creates a script variant with source line IDs; it does not overwrite canon. Validate localized duration against the accepted visual window before buying voice or lip-sync. Moving a line may require subtitle/timeline changes; baked native speech or lip motion cannot be removed with a text-only edit. Preserve isolated stems when available; if not available, disclose the extraction/remix limitation before choosing the cheapest valid repair.
