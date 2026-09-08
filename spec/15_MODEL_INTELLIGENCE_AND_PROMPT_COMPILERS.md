# Model Intelligence and Prompt Compilers

## Layers
UniversalVideoSpec → CapabilityResolver → ModelProfile → ModelPromptCompiler → ReferenceCompiler → Duration/StageCompiler → AudioCompiler → ProviderAdapter.

## ModelProfile
Stores measured behavior: identity/version, reference syntax, practical ref stability, multi-shot/hard-cut support, duration/resolution, native/ref audio, timing adherence, preferred granularity, first/end frame, continuation/editing support, default aesthetic/bias, effective counter-default phrasing, known failures, compile notes, benchmark reliability and `last_verified_at`.

## Unknown is valid
Never inherit behavior from a previous model version without evidence.

## Model ≠ provider
The same model may be exposed differently by multiple providers.

## Probe suite
On integration/version change: reference binding; timing adherence (stages vs timestamps); default behavior baseline; practical reference stability ceiling; native audio/dialogue behavior where relevant.

## Prompt provenance
Every media attempt stores UniversalVideoSpec version, ModelProfile version, compiler version, compiled prompt, refs, provider/model/params, result, cost and QA.

## Evidence-bound profile promotion
Profiles distinguish reported capability from runtime-supported capability. Each claim has status, typed value, exact model version, provider/account/region scope, source locator/version, verified time, sample count and unknown/failure notes. MEASURED requires inspectable sample records with inputs/outputs, route and date; reading a repository that calls itself measured is REPO_REPORTED evidence, not this product's measurement. A family profile is non-routable; choose an exact variant before resolving capabilities. Model release, endpoint, entitlement or policy changes invalidate the corresponding EffectiveCapability snapshot.
