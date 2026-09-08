# Effective Capability Resolution and Provider Fallback

## Effective capability
Runtime capability is the intersection of:
`ModelProfile ∩ ProviderProfile ∩ AccountEntitlement ∩ ProductPolicy ∩ Project/UserPolicy`.

A model may support a feature in principle while a provider endpoint/account does not expose it. The Director must reason from `EffectiveCapability`, not model marketing claims.

## Resolution output
For each required feature record:
- requested capability;
- model evidence/status;
- provider exposure/status;
- account/region/policy constraints;
- effective status: `SUPPORTED | UNSUPPORTED | UNKNOWN | DEGRADED`;
- selected route or explicit degrade/block reason.

## Unknown
`UNKNOWN` is valid. High-cost/high-impact unknowns trigger a cheap probe/research when practical; otherwise block or explicitly degrade. Never assume support.

## Fallback ordering
Prefer routes that meet the same intent with lower expected `cost_per_accepted_second`, but preserve hard locks, canon and user constraints. Provider failure fallback follows spend certainty semantics in `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md`.

## Modality requirements
Provider architecture must cover at minimum LLM, image, video, voice/audio and storage ports even when early vertical slices use only one real implementation per modality. The Generalist Director depends on ports/tool contracts, never concrete vendor SDKs.

## Expansion
A new model/provider requires profile + compiler (when model behavior differs) + provider exposure + adapter + probes + benchmark evidence. No Director rewrite is permitted merely to add a provider.
