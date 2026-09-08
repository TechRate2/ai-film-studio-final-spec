# Provider Abstraction and Routing

## ProviderProfile
Provider identity, API base/region, model exposure, accepted modalities, duration/resolution availability, first/end/reference/continuation exposure, queue/polling behavior, rate/concurrency limits, price model, billing semantics, timeout/idempotency behavior and account restrictions.

## Adapters
Separate `LLMProvider`, `ImageProvider`, `VideoProvider`, `VoiceProvider`, `StorageProvider` interfaces.

## Router
Select by required capability, measured scenario quality, reliability, latency, cost, `cost_per_accepted_second` and user/account preference. Never route by marketing label alone.

## Degrade Planner
If capability unavailable: reduce refs by priority, split multi-shot, use stage prompts, move audio to post, use first frame instead of multi-ref, or switch provider/model if policy permits. Every degrade is explicit/provenanced; no silent downgrade.
