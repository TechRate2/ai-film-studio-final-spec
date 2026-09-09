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

## Binding execution and verification packet

Dependencies: TASK-025. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md`
- `spec/37_MODEL_PROBE_PLAYBOOK.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/model_profile.schema.json`
- `schemas/provider_profile.schema.json`
- `schemas/effective_capability.schema.json`

Requirements: R-016, R-058, R-065.
Golden coverage: GS15, GS20.

- [ ] Resolve all five capability layers with denial/unknown precedence, limit intersections, exact version/route evidence and entitlement expiry.
- [ ] Seedance 2.5 cannot inherit 2.0 values; family/unverified profiles cannot be production routes, and a declared degrade must itself resolve safely.
- [ ] Reject a SUPPORTED snapshot when any of the five layers is UNKNOWN/UNSUPPORTED, an unlinked DEGRADED result, and SUPPORTED claims backed only by REPO_REPORTED/UNVERIFIED/SYNTHESIS. Accept documented scoped capability without falsely calling it measured. Verify sample provenance/freshness and linked alternative resolution separately from JSON validity.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
