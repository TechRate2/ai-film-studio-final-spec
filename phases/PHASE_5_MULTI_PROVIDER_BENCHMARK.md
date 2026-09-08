# Phase 5 — Multi-provider Benchmark Expansion

## Goal
Add Wan/Vidu/Kling/Veo/future engines without rewriting the Director.

## Integration rule
Every addition goes through ModelProfile + compiler + ProviderProfile + adapter + probes + benchmark evidence.

## Exit gate
- provider switch golden scenario passes;
- routing uses measured scenario quality/reliability/cost rather than marketing names;
- same model through different providers can expose different API capabilities;
- unknown capability remains explicit;
- `cost_per_accepted_second` can influence routing;
- no new provider-specific branch appears in creative/story logic.
