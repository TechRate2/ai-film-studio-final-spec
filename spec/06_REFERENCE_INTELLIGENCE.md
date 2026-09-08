# Reference Intelligence

## Automatic roles
`CHARACTER_IDENTITY`, `CHARACTER_OUTFIT`, `PRODUCT_FRONT/SIDE/DETAIL`, `LOCATION`, `PROP_IDENTITY`, `CAMERA_REFERENCE`, `EDITING_PACING_REFERENCE`, `STYLE_REFERENCE`, `MOTION_REFERENCE`, `VOICE_REFERENCE`, `STORY_STRUCTURE_REFERENCE`.

## Entity grouping
Multiple files may represent one entity. Never create separate characters because the same person has front/side/full-body images.

## Lock semantics
- `HARD_LOCK`: exact identity/product/logo/outfit/weapon/critical prop
- `SOFT_LOCK`: location mood/lighting/vibe
- `STYLE_ONLY`
- `MOTION_ONLY`

Every ref instruction must state what it controls and what it must not control.

## Reference lifetime
- `PERSISTENT`: face/body/core prop/product
- `EPISODE`: episode outfit/injury/state
- `SCENE`: temporary appearance/prop/weather
- `SHOT`: pose/last-frame/camera motion

## Smallest sufficient pack
Attach only active entities and useful continuity refs. Reference overload is a failure mode.

## Previous-output preference for dependent shots
1. previous accepted video/tail if supported;
2. previous accepted last frame;
3. canonical refs + persisted state.

## Validation
Imported/external refs and keyframes are evaluated against requested roles before entering canonical production state.
