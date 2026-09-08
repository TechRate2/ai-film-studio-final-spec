# Production Strategy and Scene Complexity

## Production Strategy
Choose the cheapest method meeting quality: generated video, still/generated image + motion, uploaded footage, screenshots/charts, mixed media, voice/narration, typography or transitions. Not every second must be generative video.

## SceneComplexity inputs
Duration, active character count, identity constraints, action complexity, dialogue/lip-sync, camera complexity, state/location changes, product/prop fidelity, VFX/physics, provider capabilities, benchmark reliability, continuity risk, expected failure cost and editorial rhythm.

## GenerationPlan outputs
Target segment durations, meaningful boundaries + reason, mode (`CONTINUOUS | SEGMENTED | CONTINUATION`), keyframe policy, reference pack, per-segment overrides, dependency graph, sequential/parallel groups, expected cost and expected acceptance probability.

## Split only for meaningful reasons
Location/time change, major camera grammar change, state/reveal boundary, action/VFX overload, new character state, provider duration/capability or measured reliability risk. Never split mechanically at a fixed duration if a reliable longer generation is better.

## Plan semantics and empirical uncertainty
Editorial shots, storyboard panels and provider generation segments are distinct IDs with explicit mappings. One generation may contain several editorial shots; an editorial shot may use continuation segments. Choose CONTINUOUS, SEGMENTED or CONTINUATION from meaningful state transitions and measured route limits, not panel count. Every additional boundary has a reason and entry/exit state; model limits alone do not prove that filling every request to its maximum is best. Compare feasible longer and shorter alternatives including continuity cost, reuse, still+motion and existing footage. Missing acceptance measurements are null/UNKNOWN, never a fabricated probability. A duration target includes trims/transitions/holds and is checked on the final timeline.
Expected cost per accepted second uses planned cost divided by expected usable seconds when evidence supports that estimate. Zero/unknown usable seconds yields null plus reason. Observed metrics include rejected and failed billed samples in the numerator and deduplicate accepted media in the denominator; repeated timeline reuse must not inflate generation acceptance.
