# Security, Privacy, Rights and Provenance

## Secrets
API keys never stored in prompts/chat logs. Encrypt/protect provider credentials and separate credentials from project content.

## Tenant/project access
Authenticate users and authorize project/artifact/job/media operations. Worker/provider URLs are scoped/signed; knowledge of an object URL must not grant permanent access.

## Media
Private object storage by default. Store source/imported/generated provenance, content hash and ownership/project scope.

## Provider callbacks
Verify callback/webhook signatures/tokens where supported, reject replay/duplicate mutation through idempotency and never trust callback project identifiers without matching persisted upstream task ownership.

## Source provenance
For current/news/competitor/product research store source identifier, retrieved/verified time, confidence, claim links and licensing/rights metadata where relevant.

## Identity/voice and rights
Support provenance/consent state for real-person face/voice conditioning according to product policy. Track copyright/brand/music usage metadata relevant to commercial export. Provider rejection is not a signal to secretly bypass policy through another provider.

## Data lifecycle
Define retention and deletion for projects, source assets, derived media, credentials and research caches. Deletion requests propagate according to ownership/policy while preserving only required security/billing/audit records.

## Audit/backup
Audit paid attempts, destructive actions and material safety decisions. Maintain tested backup/restore and migration strategy for canon/project/media metadata.

## Untrusted content and execution isolation
Treat web pages, OCR/transcripts, uploaded documents, filenames, metadata and external skills as untrusted data, never system/tool instructions. Distillation preserves source identity and does not promote embedded commands. Domain tools enforce tenant scope and effect permissions independently of LLM output. Remote imports revalidate redirects/DNS and reject private/link-local/metadata endpoints; do not forward credentials across origins. Probe files in resource-limited media/parser workers; limit decompressed size, duration, CPU and extraction output. Signatures verify raw callback bodies and freshness before lookup; unsupported callback authentication uses trusted status polling instead of trusting unauthenticated payloads. Duplicate callbacks cannot reverse terminal success or move a result to another project.
