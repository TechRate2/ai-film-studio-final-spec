# Selective Keyframes and External Workflow

## Two independent decisions
1. `SelectiveKeyframeController`: Is a keyframe useful?
2. `KeyframeSourceRouter`: Where should it come from?

## Keyframe source enum
`AUTO_INTERNAL | EXTERNAL_ASSISTED | USER_SUPPLIED | PREVIOUS_ACCEPTED_FRAME | NONE`

## High-value cases
First appearance of important identity, exact product/prop, important outfit change, complex environment establishing state, costly/high-risk composition, major transition/hero frame, or action pose where visual anchoring improves reliability.

## Low-value cases
Generic B-roll, simple continuation, previous accepted frame already anchors state, or provider benchmark shows reliable direct generation.

## External Assisted flow
1. Agent creates `KeyframeGenerationPack`.
2. UI shows purpose, reference roles, copy-ready prompt and required refs.
3. User creates image in ChatGPT/Gemini/Flux/other tool.
4. User uploads image.
5. Keyframe Validator checks identity/composition/locks/aspect/continuity.
6. Accepted image enters project state.
7. If incorrect, Agent produces a minimal correction patch.

External keyframes are first-class artifacts and do not incur internal image generation cost.
