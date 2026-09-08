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
