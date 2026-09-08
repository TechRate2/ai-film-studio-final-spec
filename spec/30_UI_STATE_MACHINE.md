# UI State Machine

The default UI remains chat-first while rendering structured production state.

## Project experience states
`DRAFT → UNDERSTANDING → RESEARCH/PLANNING → PLAN_READY → PRODUCING → REVIEWING → FINALIZING → COMPLETE`
with overlays `WAITING_USER`, `BLOCKED`, `FAILED_PARTIAL`.

## Composer
Natural-language input + attachments. Optional lightweight controls: duration/aspect/language/budget/quality. Advanced provider/keyframe controls are hidden by default.

## Progress
Show human labels such as: Hiểu yêu cầu, Research, Kịch bản, Nhân vật, Production plan, Keyframe cần upload, Video 3/8, QA, Ghép âm thanh. Do not expose internal logs as the primary UX.

## Shot card states
`PLANNED | BLOCKED | GENERATING | READY_REVIEW | ACCEPTED | REVISION_DRAFT | STALE | FAILED`.
Shot card exposes preview, version history, cost, QA summary, Accept and natural-language revision input.

## Revision UX
User says what to change. Before paid video revision, UI presents interpreted change/preserve set and incremental cost. A new version never erases the old one.

## External keyframe UX
Card provides purpose, copy prompt, reference bundle, upload slot and validation/correction feedback.

## Advanced Director details
Optional drawer can show evidence, CreativeStrategy, shot plan, UniversalVideoSpec, model/compiler decision, reference mapping, continuity and cost rationale.

## Projection, not competing persistence
UI labels are projections of canonical run/job/artifact/acceptance records, not alternate worker states. AUTHORIZED/SUBMITTING/RUNNING project to producing; RECONCILING shows recovery; SUCCEEDED projects to review only after output/QA exists; CANCEL_REQUESTED remains cancelling until confirmation. STALE/BLOCKED/MISSING artifacts override any completed preview label. Persist locale as user preference; render the same resource IDs, amounts and authorization meaning in vi/en. Out-of-order events cannot roll back accepted versions or show false completion. Locale changes and refreshes are read-only for production state.
