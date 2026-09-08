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
