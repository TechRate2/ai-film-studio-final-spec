# Example — External Keyframe Pack

## Decision
SelectiveKeyframeController decides Segment 1 needs a strong establishing keyframe. KeyframeSourceRouter = `EXTERNAL_ASSISTED`.

## UI card
Purpose: lock spacecraft design, Saturn scale, lighting and composition.  
Actions: Copy Prompt / View Required Refs / Upload Generated Image.

## Copy-ready prompt example
```text
Create a photoreal cinematic establishing frame of Odyssey-7 approaching Saturn.

REFERENCE ROLES
Image 1 controls exact Odyssey-7 hull shape/proportions/windows/markings; do not use its background.
Image 2 controls Commander Minh identity and flight suit; he is only faintly visible through cockpit canopy; do not copy original pose/background.

SCENE
Deep black outer space. Saturn occupies about 70% of background. Rings cross diagonally. Odyssey-7 is small in lower foreground to emphasize scale.

LIGHTING
Single plausible sunlight direction from upper-left. Warm rim on Saturn, cold reflected light on ship.

DO NOT
No fantasy nebula, second planet, extra spacecraft, text, logo mutation or artificial lens flare.

SUCCESS
Viewer immediately understands one tiny human spacecraft is approaching an overwhelmingly enormous Saturn.
```

After upload, Keyframe Validator checks identity, ship, Saturn, light, composition, aspect and continuity. Failure produces a minimal correction patch rather than forcing internal paid generation.
