# TASK-042 — Security, Privacy, Rights, Backup and Observability

## Goal
Harden commercial production semantics around tenant authorization, secrets, media, identity/voice consent, source rights, deletion, callbacks, audit, restore and spend incidents.

## Read first
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `spec/35_DEPLOYMENT_OPERATIONS.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/43_CONTENT_SAFETY_RIGHTS_COMPLIANCE.md`
- `schemas/content_safety_decision.schema.json`

## Acceptance criteria
- tenant/project authorization on APIs, workers and media URLs;
- provider credentials encrypted/protected and never logged;
- callback/webhook authentication/replay protection where applicable;
- real-person face/voice consent/provenance policy represented;
- product/factual claims and copyrighted/music/brand source provenance supported;
- user/project media deletion and retention semantics implemented;
- audit log for paid/destructive/safety-material decisions;
- backup restore tested, not only configured;
- global paid-queue/provider kill switch and spend incident response;
- structured logs correlate project/run/job/attempt/provider/model/cost without leaking secrets/private payloads.
