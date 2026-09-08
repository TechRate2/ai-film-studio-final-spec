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

## Binding execution and verification packet

Dependencies: TASK-041. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `spec/35_DEPLOYMENT_OPERATIONS.md`
- `spec/41_MULTIMODAL_ASSET_INGESTION.md`
- `spec/43_CONTENT_SAFETY_RIGHTS_COMPLIANCE.md`
- `schemas/content_safety_decision.schema.json`
- `schemas/asset_ingestion_record.schema.json`

Requirements: R-034, R-059, R-060, R-061, R-067, R-068, R-086, R-087.
Golden coverage: GS10, GS18, GS23, GS24, GS28.

- [ ] Prove tenant access, secrets/callback/import isolation, consent/rights decisions, deletion/retention and backup restore including media dependencies.
- [ ] Inject prompt/URL import attacks and replay/cross-project callback; revoked/deleted content stays unavailable after restore and kill switch stops unsubmitted spend.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
