# TASK-024 — Keyframe Source Workflows (Smart Auto + External + User + Previous)

## Goal
Implement every canonical KeyframeSourceRouter route while keeping keyframe generation selective.

## Execution dependency
The source-routing/domain/UI contract may be designed earlier, but **full task acceptance for `AUTO_INTERNAL` requires TASK-028 ImageProvider port/adapter boundary to exist**. Canonical implementation order therefore executes TASK-024 after TASK-028 and after TASK-032/TASK-033; no billable image path precedes the guard.

## Read first
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/keyframe_generation_pack.schema.json`

## Acceptance criteria
- `AUTO_INTERNAL` calls a real/replaceable ImageProvider through the provider port only after cost policy/authorization when billable;
- `EXTERNAL_ASSISTED` emits copy-ready prompt + exact reference pack + constraints and incurs no internal image generation cost;
- `USER_SUPPLIED` validates imported asset;
- `PREVIOUS_ACCEPTED_FRAME` can reuse the continuity anchor without new image generation;
- `NONE` continues directly;
- validator checks identity/product/outfit/location/composition/aspect/continuity as applicable;
- failed external/user image returns a minimal correction patch, not silent internal fallback;
- all source routes create provenance-compatible artifacts.

## Binding execution and verification packet

Dependencies: TASK-033. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/keyframe_generation_pack.schema.json`
- `schemas/artifact.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-014, R-039, R-049, R-050, R-088.
Golden coverage: GS08, GS14, GS16, GS17, GS27.

- [ ] Exercise all five sources with version-pinned packs, validation and explicit invalid-upload correction; real internal path uses the completed guard.
- [ ] External/user/previous/NONE routes make zero internal image generation calls; stale pack upload and rejected internal image cannot trigger automatic paid fallback.
- [ ] Accept USER_SUPPLIED and PREVIOUS_ACCEPTED_FRAME without inventing a generation prompt; require a real selected source artifact/version and validation contract. Reject missing source pins, rejected/stale parent-frame lineage and generation/source fields on NONE. AUTO_INTERNAL/EXTERNAL_ASSISTED still require a nonempty generation prompt.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
