# ADR 0002 — Separate localization workspace after the core studio

Status: ACCEPTED FOR SPECIFICATION. Date: 2026-09-09. Contract version: 4.4.0.

## Authority and authorization
The owner explicitly requests a separate subtitle/dubbing function on original uploaded video, optional subtitles and/or dubbing, simple editing, speed changes and one-click AI checking/alignment. The owner explicitly requires implementation after the main studio. This is the approval for this Class C workflow extension; it is not permission to build the application now or spend provider credits. Existing paid-attempt, one-Director, rights, versioning and provider-neutral invariants remain binding.

## Current behavior and problem
Specs 09 and 42 cover voices/localization and timelines inside production. They do not specify the independent source-video workflow, source-time transcript, speaker assignment, drift-safe retiming, a no-generation boundary or extension-specific release gate. Requiring every new critical requirement at TASK-043 would make a later extension a prerequisite of its own prerequisite.

## Decision
Add spec/47, two normative localization records, TASK-044 through TASK-046 and Phase 7. Core requirements R-001 through R-088 and GS01 through GS28 remain the TASK-043/Phase 6 release scope. R-089 through R-096 and GS29 through GS33 belong to the localization release; shared-core regressions still block it. The user can launch a localization project without a generation project, but development starts only after the core release gate passes.

The extension preserves original media and supports subtitles only, dubbing only or both. It has no video/image generation, face modification or lip-sync tool access. Deterministic speed adjustment, subtitle burn-in and audio remux/transcode are permitted derivatives. One visible Director invokes existing neutral tools in a restricted scope; no second autonomous brain or duplicated billing/memory platform is added.

## Alternatives and trade-offs
- Force all requests through generation: rejected; violates independent UX and adds paid/media risk.
- Embed an entire desktop dubbing repository: rejected as default; deployment, licenses, security and retries need independent review. Learn reusable techniques and adapt selected components behind ports only after review.
- Offer automatic lip-sync: excluded by the owner's latest original-video-only scope. Dubbing aligns speech timing, not mouth shapes.
- Promise every language and fully unattended perfection: rejected; language support is per operation/route and uncertain regions require focused review.

## Affected contracts and adoption
Update specs 00, 01, 09, 20, 25, 27, 28, 42, 45, 47; ProjectIntent workflow_kind; CompositionTimeline optional caption styling; localization schemas; implementation order and core gate scope; three new tasks; Phase 7; release-gate traceability; fixtures and CI; evidence and inventory. Existing projects without workflow_kind are interpreted as STUDIO only; new writes provide it. Existing timeline styles retain their old defaults. No backfill may invent source words, timings, speakers or rights. Existing implementations must perform TASK-001 reality analysis before migration.

No independent external review, live-provider qualification or commercial readiness is claimed by accepting this ADR. The expansion closure evidence records actual specification validation and remaining empirical limits.
