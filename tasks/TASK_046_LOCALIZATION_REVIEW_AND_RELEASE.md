# TASK-046 — AI Check, Alignment, Export and Localization Release

## Goal
Implement this bounded vertical localization capability under spec/47, preserving the already accepted main studio.

## Binding execution and verification packet

Dependencies: TASK-045. Follow `tasks/00_IMPLEMENTATION_ORDER.md`; Phase 6 must already pass.

## Read first
- `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md`
- `spec/28_API_AND_EVENT_CONTRACTS.md`
- `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `spec/47_SOURCE_VIDEO_LOCALIZATION.md`
- `schemas/localization_project.schema.json`
- `schemas/localization_review.schema.json`
- `schemas/composition_timeline.schema.json`
- `schemas/final_master.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-089, R-092, R-093, R-094, R-095, R-096.
Golden coverage: GS29, GS30, GS31, GS32, GS33.

## Acceptance criteria

- [ ] Require TASK-045 and the original TASK-043/Phase 6 proof; run Phase 7 and shared-core regression gates. Record the CORE vs LOCALIZATION requirement sets without treating not-yet-implemented localization as a core prerequisite.
- [ ] Implement one-click diagnostics under bounded analysis allowance, evidence-linked findings, typed safe patches and focused unresolved sentences. Safe application checks expected project/timeline/input versions, user locks and target IDs atomically; arbitrary patch operations or stale proposals fail.
- [ ] AI safe fixes create immutable derivatives and Undo; they cannot change source video speed, source/target words, speaker or voice without a separate explicit user edit. Even a bulk fix cannot invoke image/video/lip-sync or new paid voice. Price and authorize selected TTS revisions separately.
- [ ] Export requested SRT/VTT/ASS and/or video derivative from CURRENT pinned timeline; verify actual cues, language, fonts, soundtrack choice, retimed duration and checksum. A sidecar-only request avoids an unnecessary video master. Concurrent edit during export never promotes a stale result.
- [ ] Test restart, cancel, double-click, late callback, provider outage, unknown submission, source deletion, unauthorized URL/font access and cross-tenant retrieval. Accepted segments are reused; counts/costs persist and duplicate paid submission stays zero.
- [ ] Test vi/en usability with a non-editor: upload, target selection, mode, edit a sentence/voice/font, change speed, use AI check, undo and export without opening a professional timeline. Show clearly that dubbing does not modify mouths.
- [ ] Prove every linked requirement and GS29–GS33 at the required deterministic and real levels. Publish an exact operation/language/voice/provider matrix and known limits; remove unsupported options instead of claiming universal quality. Scope-specific human acceptance and cost/latency measurements are required.
- [ ] Run the applicable CORE regression suite GS01–GS28. No critical shared-core or localization failure can be waived with an attractive demo. Report remaining empirical limits and release only verified language pairs.
- [ ] For every criterion record exact code/report path, assertion, result and Golden subsection. PARTIAL/BLOCKED is required for missing evidence; no screenshots, schemas or test fixtures stand in for real-provider gates. No paid call runs in ordinary CI. Commit a versioned checkpoint and update traceability only from real implementation evidence.
