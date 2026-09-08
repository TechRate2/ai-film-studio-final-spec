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

## External round trip and source selection
KeyframeGenerationPack pins purpose, target ID/version, composition, camera, lighting, continuity locks, negative risks, reference bundle and observable success conditions. Copy/export includes ordered reference identities and their allowed roles; signed URLs are refreshed on demand without changing source identity. Upload validates hash, dimensions, rights, target version and constraints. An old pack uploaded after canon/revision changes is marked STALE for revalidation rather than attached to the new shot silently. Invalid uploads return an actionable correction patch. NONE requires no prompt or reference bundle; an accepted previous frame retains its original artifact/version provenance. External cost is unknown/user-reported separately; zero internal image calls does not imply all external work was free.

## Machine-checkable invariants
```json
{
  "keyframe_sources": [
    "AUTO_INTERNAL",
    "EXTERNAL_ASSISTED",
    "USER_SUPPLIED",
    "PREVIOUS_ACCEPTED_FRAME",
    "NONE"
  ]
}
```

For source NONE, the compact decision contains only ID, purpose and version-pinned target. No generation prompt or reference bindings are required; if supplied, the prompt is empty and bindings are empty. A non-NONE pack requires its full prompt/reference/composition/continuity/success contract. This distinction is enforced in schema fixtures.
