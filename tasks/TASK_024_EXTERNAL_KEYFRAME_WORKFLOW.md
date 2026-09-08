# TASK-024 — Keyframe Source Workflows (Smart Auto + External + User + Previous)

## Goal
Implement every canonical KeyframeSourceRouter route while keeping keyframe generation selective.

## Read first
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/20_CHAT_FIRST_WORKSPACE_UX.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/keyframe_generation_pack.schema.json`

## Acceptance criteria
- `AUTO_INTERNAL` calls a real/replaceable ImageProvider only after cost policy/authorization when billable;
- `EXTERNAL_ASSISTED` emits copy-ready prompt + exact reference pack + constraints and incurs no internal image generation cost;
- `USER_SUPPLIED` validates imported asset;
- `PREVIOUS_ACCEPTED_FRAME` can reuse the continuity anchor without new image generation;
- `NONE` continues directly;
- validator checks identity/product/outfit/location/composition/aspect/continuity as applicable;
- failed external/user image returns a minimal correction patch, not silent internal fallback;
- all source routes create provenance-compatible artifacts.
