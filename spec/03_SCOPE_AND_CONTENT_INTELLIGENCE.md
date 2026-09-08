# Scope and Content Intelligence

## Scope Intelligence
Automatically infer `SHORT`, `LONG_SINGLE`, or `SERIES` using duration plus recurring cast, continuity horizon, plot complexity, episode language, world rules, locations, relationship persistence and continuation intent.

### Adaptive depth
**SHORT:** request context, minimal refs, creative/shot state.  
**LONG_SINGLE:** project bible, character/location/prop registries, scene/shot continuity.  
**SERIES:** series/world bible, character/relationship graph, character knowledge state, episode ledger, canonical facts, voice/costume/prop/location state and unresolved threads.

## Content Intelligence
Content mode is separate from scope and generation mode. Canonical modes:
`DRAMA | UGC | ADVERTISEMENT | PRODUCT_DEMO | NARRATION | DOCUMENTARY | EXPLAINER | MUSIC_VISUAL | VISUAL_FILM | OTHER_GENERALIST`.

`PRODUCT_DEMO` is used when product truth, shape/material/feature proof and visual fidelity are the primary storytelling constraint. It may still use UGC/ad grammar as retrieved skills, but product fidelity is not reduced to a niche-specific hard-coded pipeline.

Genre/aesthetic is metadata, not architecture. Example: `genre=xianxia`, `content_mode=DRAMA`, `scope=SERIES`.

Current-news/factual work is normally represented by a content mode such as `DOCUMENTARY`, `EXPLAINER` or `NARRATION` plus `knowledge_mode=CURRENT/FACTUAL`; do not create a separate hard-coded pipeline merely because information is current.

## Production mode is independent
Per-shot routes can include `DIRECT_T2V`, `IMAGE_TO_VIDEO`, `REFERENCE_TO_VIDEO`, `STORYBOARD_TO_VIDEO`, `CONTINUATION`, `SPEECH_TO_VIDEO`, `CHARACTER_ANIMATE`, `MIXED_MEDIA`.

## Router output
The router must persist the scope decision, content mode, genre/platform tags, memory depth, continuity level, research modes and the factors that materially caused the decision. It must be possible to re-evaluate the decision after user intent or project scale changes without rewriting historical accepted artifacts.
