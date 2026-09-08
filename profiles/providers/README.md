# Provider Profiles

ProviderProfile describes **where/how** a model is exposed: endpoints, modalities, duration/resolution availability, pricing, limits, regions, queue/polling/webhook semantics, upstream task identity and idempotency/billing behavior.

It does not describe the creative behavior/bias of a model; that belongs to ModelProfile.

The same model through two providers may require two ProviderProfiles while sharing one model identity where behavior evidence legitimately transfers. Provider-specific behavior that changes model output materially should remain scoped in benchmark evidence rather than being guessed.

Runtime pricing/limits must come from currently verified provider configuration, not historical evidence snapshots.
