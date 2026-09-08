# Phase 5 — Multi-provider Benchmark Expansion

## Goal
Add Wan/Vidu/Kling/Veo/future engines without rewriting the Director.

## Integration rule
Each addition uses `tasks/PROVIDER_EXPANSION_TEMPLATE.md`: ModelProfile + compiler when needed + ProviderProfile + adapter + EffectiveCapability + probes + benchmark evidence + cost semantics.

Initial non-Seedance profiles may be PARTIAL/UNVERIFIED placeholders; they are not routable as measured production truth until provider-specific probes are completed.

## Exit gate per integration
- provider-switch/effective-capability golden scenarios pass;
- same model through different providers can expose different API capabilities;
- unknown capability remains explicit;
- fallback obeys paid-state certainty/SpendAuthorization;
- routing uses measured scenario quality/reliability/latency/cost_per_accepted_second rather than marketing names;
- no new provider-specific branch appears in creative/story logic.
