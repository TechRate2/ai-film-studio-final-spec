# Chinese/Public AI Film Workflow Synthesis

**Evidence type:** SYNTHESIS based on public repositories listed in `PUBLIC_SOURCE_MAP.md`; not a claim about proprietary/private studio systems.

Strong recurring public patterns:
- structured script/character/scene state before generation;
- persistent character/scene assets and reference-role mapping;
- previous generated/accepted media used to improve continuity;
- storyboard/shot plans as editable artifacts rather than opaque prompt text;
- human review/checkpoints and result refinement/versioning;
- long-form work divided hierarchically into episodes/scenes/shots;
- provider/model-aware generation constraints;
- resume/project memory and asynchronous jobs.

This canonical design intentionally improves on common public patterns by adding explicit Project Canon + Character Knowledge State, dependency-aware sequential continuity, smallest-sufficient reference packs, selective/external keyframes, UniversalVideoSpec/compiler separation, PaidAttemptGuard, artifact stale propagation and Continuity Sandwich for middle-shot revisions.

Do not turn this synthesis into a rigid “Chinese pipeline.” The Generalist Director remains adaptive by content, scope, evidence and model capability.
