# TASK-027 — Model Prompt Compilers

## Goal
Implement compiler interfaces and Seedance compiler contract.

## Read first
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`

## Implementation contract
- Inspect repository reality for this capability before editing.
- Preserve `spec/00_SPEC_LOCK.md`.
- Implement vertically when persistence/API/UI are implicated.
- Do not broaden scope to unrelated future architecture.
- Add typed contracts/migrations where required.
- Add structured errors, provenance and observability.
- Update traceability.

## Acceptance criteria
- Reference positive/negative scope compiled
- Compiler version persisted
- No provider transport here

## Required report
- Current reality before this task
- Files changed
- State/schema/API/UI changes
- Tests added and results
- Golden scenarios affected
- Remaining gaps
- Real-provider benchmark risk, if any

## Binding execution and verification packet

Dependencies: TASK-026. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/14_UNIVERSAL_VIDEO_SPEC.md`
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md`
- `schemas/universal_video_spec.schema.json`
- `schemas/model_profile.schema.json`
- `schemas/reference_binding.schema.json`

Requirements: R-017, R-030.
Golden coverage: GS03.

- [ ] Compile and pin request, profiles, compiler version, reference mappings and preserved/degraded constraints; snapshot round trip is reproducible.
- [ ] Missing HARD_LOCK binding or contradictory duration/audio cannot silently disappear; transport stays outside compiler and Director stays outside vendor syntax.
- [ ] Exercise a provider contract whose prompt can imply reference/edit/extend operations. Contradictory prompt/mode/parameters block before submission; consistent requests preserve approved operation, source roles and explicit audio/output choices. Unsupported mode hints are not emitted. Synthetic conformance tests do not assert actual model adherence.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
