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

## Intersection algorithm
Resolve each requested feature against all five layers with versioned evidence: any hard denial makes the route UNSUPPORTED; otherwise any unresolved relevant layer yields UNKNOWN; only all affirmative constraints with nonempty limit intersection yield SUPPORTED. Null entitlement is UNKNOWN, not unlimited. Intersect sets, numeric ranges and regions using the same declared units. DEGRADED describes an explicit alternative with a linked DegradeDecision; resolve that alternative again and preserve hard constraints. Neither majority vote nor high confidence can override a denial. Pin the resulting snapshot and revalidate before spend; changed route/cost/input outside authorization requires a new user action.

The schema rejects SUPPORTED with any non-affirmative layer and requires a nonempty `degrade_decision_id` for DEGRADED. A denied layer cannot be hidden behind UNKNOWN. These record-local checks do not prove numeric/set intersections, current entitlement, rights or the linked alternative's safety: the resolver and pre-spend gate must test those against pinned source versions. A schema-valid snapshot alone never authorizes a paid call.
