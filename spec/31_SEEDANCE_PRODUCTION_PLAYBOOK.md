# Seedance Production Playbook

This playbook separates universal directing intent from Seedance-specific compilation. Runtime facts are governed by the active ModelProfile + ProviderProfile and must be re-probed when versions/providers change.

## Seedance 2.0 reported strategy hypotheses
Use explicit reference bindings (`@imageN` where exposed), concise positive/negative reference scope, staged time structure and visible end states. Avoid overloading a 15s generation with many independent events; the planner may shorten/split only when complexity/reliability justifies it.

## Reference binding
For each ref state both:
- what it controls;
- what it must not leak.

Example: `@image1 defines exact face/hair/body identity only; do not use its background or pose.`

Multiple views of one entity must be declared the same entity rather than treated as separate subjects.

## Timing
Prefer meaningful stages over false frame-perfect second promises when measured model behavior drifts. Each stage has one primary state change and an observable end state when possible.

## Camera
Specify narrative camera intent, start/end framing and movement path. Avoid decorative simultaneous pan+dolly+orbit+zoom instructions. For complex action, action readability outranks camera spectacle.

## Audio
If native audio/dialogue is measured reliable for the exact provider/scenario, use it. Otherwise route controlled voices/post audio. Do not force native dialogue globally.

## Continuity
For dependent shots prefer prior accepted video/tail or last frame when provider supports it, while keeping canonical identity refs as source of truth. Previous generated output is continuity evidence, not the canonical identity definition.

## Preflight
Before submission verify active refs, duration/event density, stage count, exact end state, audio route, provider capability exposure and spend.

## Seedance 2.5
Treat as a separate model profile. Do not inherit 2.0 limits, bias, timing or reference behavior without probes. First probes: ref addressing/stability, stages vs timestamps, default subtitles/music/audio, duration quality curve, first/end/continuation and practical ref ceiling.

## Evidence limit
The included public profile reports experiments but does not supply this project's complete sample ledger or exact account/endpoint scope. These are hypotheses for probes, not measured universal defaults. Never drop a user composition lock because a source says an image always wins; reconcile the conflicting reference or block. Stage count, 15-second examples and reference ceilings are not fixed runtime rules. See evidence/SEEDANCE_KNOWLEDGE_STATUS.md.

The dated AtlasCloud endpoint refresh in that evidence file informs provider-scoped conformance cases, not universal Seedance defaults. TASK-027 must apply spec/14's operation/prompt/parameter agreement to each independently qualified route. Native generation, enhancement, frame rate and container choices are distinct output settings; do not copy one model version's names or behavior into another. Endpoint existence alone does not establish this account's access, Vietnamese performance or acceptance probability.
