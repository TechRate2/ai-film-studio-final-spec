# Example — Contextual Shot Revision

Chain: `SHOT05 → SHOT06 → SHOT07`, all accepted.

User says:
> Shot 6 động tác kiếm nhanh quá. Làm chậm hơn, giữ nguyên khuôn mặt, góc máy, ánh sáng và đoạn kết để nối shot 7.

## EditIntentClassifier
Semantic intent: slower sword movement; preserve identity/camera/light/outfit/weapon/end-state. Per `spec/17_SHOT_REVISION_VERSIONING.md`, first evaluate deterministic retiming against speech, end timing and continuity. Classify the actual cheapest affected modality using the normative RevisionRequest contract; a motion keyword alone does not authorize video generation. If retiming cannot preserve the constraints, propose a video revision.

## Revision inputs
- Shot06 original UniversalVideoSpec
- original compiled prompt + refs
- Project Canon
- incoming Continuity Baton from Shot05
- outgoing target from accepted Shot07
- user semantic diff

## Result
Create `SHOT06/v2`; never overwrite v1. Show incremental cost before paid generation.

## QA
Check both `Shot05 → Shot06v2` and `Shot06v2 → Shot07`.

Show an incompatible outgoing state before acceptance. Creating/rejecting a draft v2 does not invalidate accepted Shot07. If the user accepts v2 and its exit state is incompatible with Shot07, mark Shot07 and only affected dependents `STALE`. Do not silently regenerate them.
