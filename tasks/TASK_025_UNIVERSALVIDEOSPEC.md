# TASK-025 — UniversalVideoSpec

## Goal
Implement provider-neutral generation contract.

## Read first
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Director never writes provider prompt directly
- Stage/end-state supported
- Prompt economy explicit

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-023. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `schemas/universal_video_spec.schema.json`
- `schemas/reference_binding.schema.json`

Requirements: R-015.
Golden coverage: GS03, GS04.

- [ ] Validate complete UniversalVideoSpec including typed initial/in/out state, timing, performance, camera, audio, negative risks and bindings.
- [ ] Malformed/empty required sections and leaked vendor syntax obligations fail preflight; no-audio/no-stages remains representable without fake content.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
