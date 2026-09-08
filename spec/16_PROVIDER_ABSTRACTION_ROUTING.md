# Provider Abstraction, Effective Capability and Routing

## ProviderProfile
Provider identity, API base/region, model exposure, accepted modalities, duration/resolution availability, first/end/reference/continuation exposure, queue/polling/callback behavior, rate/concurrency limits, price model, billing semantics, timeout/idempotency behavior and account restrictions.

## Ports/adapters
Separate `LLMProvider`, `ImageProvider`, `VideoProvider`, `VoiceProvider`, `StorageProvider` interfaces. Search/research may be a separate typed tool boundary.

Provider adapters own transport/auth/submit/status/cancel/result normalization. They do not own story, camera, reference strategy or prompt-behavior reasoning.

## EffectiveCapability
Before routing, intersect model behavior with provider exposure, account entitlement, product policy and project/user policy. `UNKNOWN` is first-class; probe/research/degrade/block rather than guessing.

## Router
Select by required capability, measured scenario quality, reliability, latency, cost, `cost_per_accepted_second` and user/account preference. Never route by marketing label alone.

## Degrade Planner
If capability unavailable: reduce refs by priority, split multi-shot, use stage prompts, move audio to post, use first frame instead of multi-ref, or switch provider/model if policy permits. Every degrade is explicit/provenanced; no silent downgrade.

## Failure fallback
Provider fallback is constrained by paid-state certainty and SpendAuthorization. A charged/produced quality result is never silently replaced by another paid provider attempt.
