# Example — Contextual Shot Revision

Chain: `SHOT05 → SHOT06 → SHOT07`, all accepted.

User says:
> Shot 6 động tác kiếm nhanh quá. Làm chậm hơn, giữ nguyên khuôn mặt, góc máy, ánh sáng và đoạn kết để nối shot 7.

## EditIntentClassifier
`intent=CAMERA/ACTION_MOTION`, affected modality=`video`, preserve identity/camera/light/outfit/weapon/end-state.

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

If v2 ends in a state incompatible with Shot07, mark Shot07 `STALE`. Do not silently regenerate it.
