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
