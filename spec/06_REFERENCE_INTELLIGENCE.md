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
