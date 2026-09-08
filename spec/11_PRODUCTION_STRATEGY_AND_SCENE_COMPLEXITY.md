# Production Strategy and Scene Complexity

## Production Strategy
Choose the cheapest method meeting quality: generated video, still/generated image + motion, uploaded footage, screenshots/charts, mixed media, voice/narration, typography or transitions. Not every second must be generative video.

## SceneComplexity inputs
Duration, active character count, identity constraints, action complexity, dialogue/lip-sync, camera complexity, state/location changes, product/prop fidelity, VFX/physics, provider capabilities, benchmark reliability, continuity risk, expected failure cost and editorial rhythm.

## GenerationPlan outputs
Target segment durations, meaningful boundaries + reason, mode (`CONTINUOUS | SEGMENTED | CONTINUATION`), keyframe policy, reference pack, per-segment overrides, dependency graph, sequential/parallel groups, expected cost and expected acceptance probability.

## Split only for meaningful reasons
Location/time change, major camera grammar change, state/reveal boundary, action/VFX overload, new character state, provider duration/capability or measured reliability risk. Never split mechanically at a fixed duration if a reliable longer generation is better.
