# Provider / Model Expansion Template

Use after Phase 2 for every Wan/Vidu/Kling/Veo/future integration. This is a template, not an extra numbered task.

## Required inputs
- exact model/version;
- provider endpoint/account/region;
- ModelProfile with verification status;
- ProviderProfile exposure/billing/limits;
- UniversalVideoSpec compile mapping;
- probe plan;
- benchmark scenarios;
- cost model.

## Required implementation
1. model profile or update;
2. model-specific compiler only when behavior requires it;
3. provider profile;
4. transport adapter;
5. EffectiveCapability resolution;
6. degrade/fallback rules;
7. paid-attempt/upstream reconciliation behavior;
8. probe + benchmark evidence;
9. traceability and regression tests.

## Forbidden
- Director branch like `if provider == ...` for creative logic;
- copied Seedance bias for an unmeasured model;
- assumed feature support;
- silent fallback or changed spend semantics.

## Exit
Provider-switch golden scenario passes and routing can compare measured quality/reliability/latency/cost_per_accepted_second.
