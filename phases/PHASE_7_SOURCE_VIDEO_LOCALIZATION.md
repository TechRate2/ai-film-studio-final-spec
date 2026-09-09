# Phase 7 — Source Video Localization Release

## Entry
TASK-043 and Phase 6 CORE release evidence must already pass. Execute TASK-044, TASK-045, TASK-046 in order. A customer need not create a Studio video to use this separate workspace. Keep the extension disabled until its gate passes; core remains independently usable.

## Exit gate
- R-089–R-096 are IMPLEMENTED with exact implementation/test references, not document references as substitutes.
- GS29–GS33 pass their deterministic assertions; shared CORE GS01–GS28 regressions pass. Review source-preservation, forbidden-call counters, atomic locks, concurrency, cancellation and reconciliation evidence.
- Separately authorized real samples prove the exposed operation/language/voice/provider matrix. Prioritize vi↔en and vi↔zh; do not advertise a missing direction or voice. Record sample IDs, model/version, entitlement, date, failures, all spend, latency and human assessments under the benchmark rubric.
- Non-editor vi/en UI exercise completes upload, language/mode selection, sentence correction, style/voice change, video speed, AI alignment, undo and export. Dubbing-without-mouth-change disclosure appears before approval.
- Subtitle-only produces zero TTS/image/video/lip-sync submissions. All modes produce zero image/video/lip-sync submissions. AI review creates zero unplanned paid voice attempts.
- Actual rendered output and subtitle files pass coverage, timing, font/script, audio-policy and provenance QA; sidecar-only needs no video generation/export. Restore/deletion and mixed-language/no-speech cases are exercised.
- Unsupported language/overlap/separation/naturalness cases are visible limitations or BLOCKED options. A polished demo, schema pass or successful provider response is insufficient for release.

Canonical authority: `spec/47_SOURCE_VIDEO_LOCALIZATION.md`, `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`. Ordinary CI is offline; real media tests require explicit credentials and budget authorization. No application proof exists in this specification repository.
