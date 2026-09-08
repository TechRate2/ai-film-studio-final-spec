# Universal Video Spec

The Director never writes provider/model API prompts directly.

## UniversalVideoSpec
### GLOBAL
film/content type, scene, style, premise, camera principle.

### LOCKS
identity, reference roles with positive and negative scope, audio source, supporting cast, continuity and specific negative risks.

### TIME / STAGES
granularity (`none | stages | second-level`), stage list, preferably one primary change per stage and visible end state.

### PERFORMANCE
action, acting/subtext, blocking/eyeline, body state.

### CAMERA
framing, movement, composition and continuity direction.

### AUDIO
dialogue, ambience, SFX and music constraints.

### SUCCESS CONDITIONS
observable end state and critical fidelity requirements.

## Prompt economy
Every line competes for model attention. Avoid adjective stacking and generic giant negative lists. Negatives target observed risks.

## Normative structure and compilation
`schemas/universal_video_spec.schema.json` defines the persisted wire shape, including initial_state, continuity_in/out, negative_risks and timing_granularity. States use typed entity observations plus fact IDs; camera/performance/audio fields remain descriptive where physical precision is unsupported. Empty descriptive objects are not valid substitutes for these sections. No-audio/no-stages are explicit choices, not missing required sections.
Compilation pins UniversalVideoSpec, reference versions, EffectiveCapability snapshot, exact model/provider/profile/compiler versions and a deterministic request hash. Each compiler reports preserved constraints, unsupported requirements, explicit degrades and source-to-request mappings. Critical lock omission blocks submission. The provider adapter may serialize API parameters but cannot reinterpret creative intent. Vendor syntax may occur in compiled provenance only, never as a required Director input.

Timing granularity `none` has no stages. `stages` requires at least one meaningful stage and allows unknown duration hints. `second-level` additionally specifies start_seconds/end_seconds in segment-local time; domain preflight checks ordered nonoverlapping intervals, positive duration and route bounds. Requested timing is intent, not a frame-accuracy guarantee; measured adherence still controls capability and QA.
