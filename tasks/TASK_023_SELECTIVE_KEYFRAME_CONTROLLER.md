# TASK-023 — Selective Keyframe Controller

## Goal
Decide whether a visual anchor is worth its cost/risk and emit a source-neutral keyframe need, not automatically generate an image.

## Read first
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`

## Acceptance criteria
- keyframe is never mandatory per shot/segment;
- decision considers identity/product/new-state/composition/action risk, previous accepted frame availability, provider capability, video-failure cost and image cost;
- previous accepted frame may satisfy the need;
- NONE is first-class;
- decision does not itself call ImageProvider;
- source choice is handed to KeyframeSourceRouter/workflow;
- GS14 no-keyframe path passes.

## Binding execution and verification packet

Dependencies: TASK-022. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md`
- `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`
- `schemas/decision_record.schema.json`
- `schemas/keyframe_generation_pack.schema.json`

Requirements: R-013.
Golden coverage: GS14, GS16.

- [ ] Compare a high-risk hero composition with low-risk B-roll and valid previous frame; emit a source-neutral need decision with rationale.
- [ ] Controller itself makes zero image calls; NONE is valid and a visual anchor is not mandatory merely because a storyboard exists.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
