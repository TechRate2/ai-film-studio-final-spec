# TASK-028 — Provider Profiles and Adapters

## Goal
Implement provider registry/adapters without contaminating creative/model behavior.

## Read first
- `spec/16_PROVIDER_ABSTRACTION_ROUTING.md`
- `spec/36_PROVIDER_INTEGRATION_PLAYBOOK.md`
- `schemas/provider_profile.schema.json`
- `profiles/providers/PROVIDER_PROFILE_TEMPLATE.yaml`

## Acceptance criteria
- ProviderProfile represents API exposure/billing/limits/timeout behavior;
- credentials protected;
- submit/status/cancel/results normalized;
- upstream task identity persisted;
- transport errors expose retryability/paid-state certainty;
- no creative/story/prompt-strategy logic in provider adapter.
