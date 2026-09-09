# TASK-028 — Provider Ports, Profiles and Adapters

## Goal
Implement provider registry/adapters without contaminating creative/model behavior.

## Read first
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`
- `spec/36_PROVIDER_INTEGRATION_PLAYBOOK.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/provider_profile.schema.json`
- `profiles/providers/PROVIDER_PROFILE_TEMPLATE.yaml`

## Required ports
At minimum: `LLMProvider`, `ImageProvider`, `VideoProvider`, `VoiceProvider`, `StorageProvider`. Search/research connectivity may be a separate tool port.

## Acceptance criteria
- ProviderProfile represents API exposure/billing/limits/region/timeout/idempotency;
- credentials protected;
- submit/status/cancel/results normalized for async providers;
- upstream task identity persisted;
- webhook/callback signatures verified when provider uses callbacks;
- transport errors expose retryability and paid-state certainty;
- no creative/story/prompt-strategy logic in provider adapter;
- a provider can be disabled without corrupting queued project state;
- fake production media fallback prohibited.

## Binding execution and verification packet

Dependencies: TASK-027. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`
- `spec/23_SECURITY_PRIVACY_PROVENANCE.md`
- `spec/36_PROVIDER_INTEGRATION_PLAYBOOK.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/provider_profile.schema.json`
- `schemas/paid_attempt.schema.json`

Requirements: R-016, R-035, R-059, R-065, R-088.
Golden coverage: GS15, GS16, GS17, GS24, GS27.

- [ ] Provide neutral LLM/image/video/voice/storage ports with structured transport outcomes, protected credentials and capability/billing metadata.
- [ ] Do not enable billable submission before jobs/guard pass; authenticated callbacks or trusted polling only, and disable/outage never selects fake media.
- [ ] Validate provider exposure/billing/limit/timeout claims individually. MEASURED provider evidence may live outside model capabilities; unsupported labels, absent sample ledgers or a global profile label cannot promote unrelated UNKNOWN claims.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
