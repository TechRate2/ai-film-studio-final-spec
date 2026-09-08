# TASK-008 — Multimodal Ingestion and Reference Analyzer

## Goal
Turn validated image/video/audio/document/external assets into durable artifacts and candidate reference roles without trusting raw uploads.

## Read first
- `spec/06_REFERENCE_INTELLIGENCE.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `schemas/asset_ingestion_record.schema.json`
- `schemas/reference_binding.schema.json`

## Acceptance criteria
- MIME/content/media metadata validation;
- content hash/deduplication and provenance;
- corrupt/unsupported assets fail explicitly rather than becoming empty refs;
- image/video/audio/document/external-keyframe source types represented;
- thumbnails/proxies/text extraction where applicable;
- role candidates persisted only after ingestion READY;
- project/tenant authorization applies to derived media URLs;
- analyzer can distinguish identity/product/location/style/motion/camera/voice/story/fact/brand source roles without attaching everything to every shot.

## Binding execution and verification packet

Dependencies: TASK-007. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/06_REFERENCE_INTELLIGENCE.md`
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `schemas/asset_ingestion_record.schema.json`
- `schemas/reference_binding.schema.json`
- `schemas/artifact.schema.json`
- `schemas/content_safety_decision.schema.json`

Requirements: R-005, R-047, R-062, R-064, R-074, R-086.
Golden coverage: GS02, GS03, GS08, GS12, GS18, GS23.

- [ ] Ingest image/video/audio/document/external assets with partial failure isolation and ownership/version/hash/source provenance; READY requires actual validation.
- [ ] Duplicate bytes may have distinct roles; corrupt inputs and stale-target external uploads cannot become accepted references or trigger internal generation.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
