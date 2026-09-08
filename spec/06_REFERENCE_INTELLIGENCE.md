# Reference Intelligence

## Automatic roles
Canonical role families include:
`CHARACTER_IDENTITY`, `CHARACTER_OUTFIT`, `PRODUCT_FRONT/SIDE/DETAIL`, `LOCATION`, `PROP_IDENTITY`, `CAMERA_REFERENCE`, `EDITING_PACING_REFERENCE`, `STYLE_REFERENCE`, `MOTION_REFERENCE`, `VOICE_REFERENCE`, `MUSIC_REFERENCE`, `SFX_REFERENCE`, `STORY_STRUCTURE_REFERENCE`, `SCRIPT_SOURCE`, `FACT_SOURCE`, `BRAND_GUIDELINE`.

Roles may be extended as typed metadata; new roles do not create new niche pipelines.

## Entity grouping
Multiple files may represent one entity. Never create separate characters/products because the same entity has front/side/full-body/detail images.

## Lock semantics
- `HARD_LOCK`: exact identity/product/logo/outfit/weapon/critical prop
- `SOFT_LOCK`: location mood/lighting/vibe
- `STYLE_ONLY`
- `MOTION_ONLY`

Every ref instruction states what it controls and what it must not control.

## Reference lifetime
- `PERSISTENT`: face/body/core prop/product
- `EPISODE`: episode outfit/injury/state
- `SCENE`: temporary appearance/prop/weather
- `SHOT`: pose/last-frame/camera motion

## Smallest sufficient pack
Attach only active entities and useful continuity refs. Reference overload is a failure mode.

## Previous-output preference for dependent shots
1. previous accepted video/tail when effective capability supports it;
2. previous accepted last frame;
3. canonical refs + persisted state.

## Document/fact separation
SCRIPT_SOURCE/FACT_SOURCE/BRAND_GUIDELINE are source material, not visual identity references. Product/factual claims are grounded in source facts rather than inferred from appearance.

## Validation
Imported/external refs and keyframes are evaluated against requested roles after asset ingestion and before entering canonical production state.

## Binding identity and lifetime enforcement
ReferenceBinding has its own stable reference_id, a version-pinned source artifact, canonical entity_id when applicable, an explicit target scope ID, role, lock mode, lifetime and positive/negative controls. PRODUCT_FRONT, PRODUCT_SIDE and PRODUCT_DETAIL are three distinct values. Extension roles use an `X_` namespace with a registered versioned interpretation before compilation. HARD_LOCK is a requirement to preserve an attribute, not a promise of pixel identity from a model. If it cannot be satisfied, block or request a user change; never silently weaken it.
Resolve multi-view entities using source/user labels and visual evidence; ambiguity remains unresolved until contextual evidence or user correction disambiguates it. Do not merge lookalikes based only on similarity. Source-file deduplication does not merge different reference roles. Expired scope bindings are excluded even if the file remains available. A camera-only video is distilled into movement/composition descriptors or isolated allowed references; when a provider cannot isolate its influence, omit the raw video, record the limitation and preserve identity locks.

## Machine-checkable invariants
```json
{
  "reference_locks": [
    "HARD_LOCK",
    "SOFT_LOCK",
    "STYLE_ONLY",
    "MOTION_ONLY"
  ],
  "reference_lifetimes": [
    "PERSISTENT",
    "EPISODE",
    "SCENE",
    "SHOT"
  ]
}
```
