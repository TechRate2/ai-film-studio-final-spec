# Multimodal Asset Ingestion

## Goal
Make arbitrary user/external assets safe, deduplicated, inspectable and reference-ready before creative/production use.

## Supported asset families
Images, video, audio/voice, documents/scripts, captions/subtitles and externally generated keyframes/media.

## Ingestion state
`UPLOADING → RECEIVED → VALIDATING → PROCESSING → READY`
with terminal/overlay states `FAILED | QUARANTINED | NEEDS_USER_ACTION`.

## Required processing
- MIME/extension/content validation;
- file size/duration/dimensions/media-stream probe;
- content hash + deduplication;
- malware/security scanning where applicable;
- metadata extraction without trusting client metadata;
- thumbnails/proxies/waveforms where useful;
- document/text extraction where supported;
- immutable source provenance and storage identity;
- Reference Analyzer/entity grouping only after validation.

## External assets
Assets created in ChatGPT/Gemini/Flux/Photoshop/other tools are first-class imports. Preserve source label and user-provided provenance; do not pretend internally generated provenance.

## Failure handling
Corrupt/unsupported assets never silently become empty references. Surface actionable reason and preserve other successfully ingested assets.

## Privacy/storage
Private-by-default storage, signed access and tenant/project authorization apply before workers/providers receive asset URLs.
