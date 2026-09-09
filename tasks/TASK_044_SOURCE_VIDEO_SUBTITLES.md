# TASK-044 — Source Video Ingestion, Translation and Subtitle Workspace

## Goal
Implement this bounded vertical localization capability under spec/47, preserving the already accepted main studio.

## Binding execution and verification packet

Dependencies: TASK-043. Follow `tasks/00_IMPLEMENTATION_ORDER.md`; Phase 6 must already pass.

## Read first
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/47_SOURCE_VIDEO_LOCALIZATION.md`
- `schemas/localization_project.schema.json`
- `schemas/composition_timeline.schema.json`
- `schemas/project_intent.schema.json`

Requirements: R-089, R-090, R-091, R-094.
Golden coverage: GS29, GS30, GS32, GS33.

## Acceptance criteria

- [ ] Start only after TASK-043 AND Phase 6 evidence passes. Implement persistence/API/UI for an independent LOCALIZATION project; no generation-project purchase or fake source artifact.
- [ ] Provide upload, auto-detected source language with confidence/override, target language and independent subtitles/dubbing selection. No selection is rejected; initial default is subtitles only. Voice controls are inactive unless dubbing selected; TTS stays disabled until TASK-045 is accepted.
- [ ] Ingest verified source/subtitle files with parser sandbox, source hashes, timebase/PTS, speaker uncertainty and per-segment language. Test silence, mixed language, numbers without word alignment and mismatched supplied SRT; never invent missing words/timestamps.
- [ ] Implement scoped translation/glossary, source vs subtitle vs spoken fields, locks and factual anchors. Preserve source wording and proper nouns/negation/numbers; test a changed glossary affects only relevant segments.
- [ ] Build preview plus editable sentence list, safe style/font controls and sidecar/burn-in options through CompositionTimeline. Verify Vietnamese diacritics and supported script shaping; disclose styling loss for SRT and pre-existing burned captions.
- [ ] Run GS29 with tool-call spies: subtitle-only creates no TTS, cloned voice, lip-sync, image or video attempt including fallback/recovery; mock/test doubles are test-only.
- [ ] Pin project commands/versions and resource events, handle refresh/concurrent edits and per-target cost/partial state; preserve the main Studio path and backward-compatible project defaults.
- [ ] For every criterion record exact code/report path, assertion, result and Golden subsection. PARTIAL/BLOCKED is required for missing evidence; no screenshots, schemas or test fixtures stand in for real-provider gates. No paid call runs in ordinary CI. Commit a versioned checkpoint and update traceability only from real implementation evidence.
