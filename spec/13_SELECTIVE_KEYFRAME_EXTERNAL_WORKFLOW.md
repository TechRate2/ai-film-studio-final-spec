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

For source NONE, the compact decision contains only ID, purpose, source strategy and version-pinned project/target. No generation prompt or reference bindings are required; if supplied for compatibility, the prompt is empty and bindings are empty. Generation/composition/source-asset fields are absent. NONE neither creates nor validates a keyframe asset.

For AUTO_INTERNAL and EXTERNAL_ASSISTED, require the full generation prompt/reference/composition/continuity/success contract. For USER_SUPPLIED and PREVIOUS_ACCEPTED_FRAME, require the validation contract and a `source_artifact` artifact/version pin, but do not require or invent an original generation prompt. Validation requirements describe what the asset must satisfy; they do not authorize creation. A user awaiting upload remains in the workflow's waiting state until an actual source can be bound.

The selected reused source must be owned/authorized, ingested and CURRENT. PREVIOUS_ACCEPTED_FRAME selects an actual frame artifact with lineage to an accepted parent video/version; a bare video ID or a frame from a rejected/stale parent is insufficient. Frame extraction is deterministic and retains the parent pin. Canonical identity and incoming/outgoing locks are revalidated independently. Pack/source validation failure cannot call ImageProvider; switching to generation is a separate source decision with applicable authorization. These source-specific shapes are enforced in schema fixtures; ownership, acceptance and lineage are domain checks in GS08/GS14.
