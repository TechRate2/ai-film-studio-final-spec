# TASK-045 — Multi-speaker Dubbing and Original-Video Retiming

## Goal
Implement this bounded vertical localization capability under spec/47, preserving the already accepted main studio.

## Binding execution and verification packet

Dependencies: TASK-044. Follow `tasks/00_IMPLEMENTATION_ORDER.md`; Phase 6 must already pass.

## Read first
- `spec/09_DIALOGUE_VOICE_LOCALIZATION.md`
- `spec/18_COST_SPEND_ATTEMPT_POLICY.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/47_SOURCE_VIDEO_LOCALIZATION.md`
- `schemas/localization_project.schema.json`
- `schemas/composition_timeline.schema.json`
- `schemas/voice_profile.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-091, R-092, R-095.
Golden coverage: GS29, GS30, GS31, GS32.

## Acceptance criteria

- [ ] Verify TASK-044 and prior core safety gates; enable first-attempt TTS only through matching per-variant/per-segment/voice authorization and exact provider-language capability. AtlasCloud is a candidate, not a built-in assumption of supported dubbing.
- [ ] Bind speakers to stable VoiceProfile versions. Reject unknown/unsupported speaker-language assignments at the affected boundary. Demonstrate a two-speaker turn exchange, ambiguous overlap and a user correction without switching unrelated voices.
- [ ] Keep subtitle and spoken forms separate. Plan duration, pauses and pronunciation before TTS. Implement ordered fit options and human review for impossible natural fit; do not truncate, change factual meaning or buy repeated TTS from a failed fit.
- [ ] Implement rational SOURCE-to-TARGET mapping using probed PTS, source-complete contiguous spans and round-once semantics. Tests cover 1x/1.25x/0.8x, piecewise speed boundaries, crossing cues, VFR, start offset and long-duration drift.
- [ ] Video speed change remaps original audio/cues/speech windows; voice speed changes only the chosen audio playback. Respect target locks, policy bounds and pitch; uploaded accepted voice can bypass TTS. Verify undo/revert stales only affected artifacts.
- [ ] Preserve original audio and source bytes; select supplied stems or explicit separation/MUTE_SOURCE policy. Detect bleed, duplicated speech, clipping and missing background; separation failure never silently mutes everything.
- [ ] Run GS30/GS31 deterministic fixtures plus separately budgeted real ASR/TTS/background samples for launch language pairs. Record all attempts/costs and subjective reviewers; unavailable credentials make the real criterion BLOCKED, not DONE.
- [ ] For every criterion record exact code/report path, assertion, result and Golden subsection. PARTIAL/BLOCKED is required for missing evidence; no screenshots, schemas or test fixtures stand in for real-provider gates. No paid call runs in ordinary CI. Commit a versioned checkpoint and update traceability only from real implementation evidence.
