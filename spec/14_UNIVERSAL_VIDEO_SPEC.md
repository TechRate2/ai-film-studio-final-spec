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
