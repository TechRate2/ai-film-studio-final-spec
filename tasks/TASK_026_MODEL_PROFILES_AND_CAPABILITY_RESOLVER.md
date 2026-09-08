# TASK-026 — Model Profiles and Effective Capability Resolver

## Goal
Resolve what the system can actually do from measured model behavior plus provider/account/policy exposure.

## Read first
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/37_MODEL_PROBE_PLAYBOOK.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/model_profile.schema.json`
- `schemas/effective_capability.schema.json`

## Acceptance criteria
- ModelProfile never conflated with ProviderProfile;
- `EffectiveCapability = model ∩ provider ∩ account ∩ product policy ∩ project/user policy`;
- UNKNOWN is representable and never guessed as supported;
- material unknown can trigger probe/research/degrade/block;
- profile/version/probe provenance persisted;
- Seedance 2.5 does not inherit 2.0 bias automatically.
