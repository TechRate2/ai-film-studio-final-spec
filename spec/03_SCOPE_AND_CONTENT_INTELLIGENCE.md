# Scope and Content Intelligence

## Scope Intelligence
Automatically infer `SHORT`, `LONG_SINGLE`, or `SERIES` using duration plus recurring cast, continuity horizon, plot complexity, episode language, world rules, locations, relationship persistence and continuation intent.

### Adaptive depth
**SHORT:** request context, minimal refs, creative/shot state.  
**LONG_SINGLE:** project bible, character/location/prop registries, scene/shot continuity.  
**SERIES:** series/world bible, character/relationship graph, character knowledge state, episode ledger, canonical facts, voice/costume/prop/location state and unresolved threads.

## Content Intelligence
Separate from scope:
`DRAMA | UGC | ADVERTISEMENT | NARRATION | DOCUMENTARY | EXPLAINER | MUSIC_VISUAL | VISUAL_FILM | OTHER_GENERALIST`.

Genre/aesthetic is metadata, not architecture. Example: `genre=xianxia`, `content_mode=DRAMA`, `scope=SERIES`.

## Production mode is independent
Per-shot routes can include `DIRECT_T2V`, `IMAGE_TO_VIDEO`, `REFERENCE_TO_VIDEO`, `STORYBOARD_TO_VIDEO`, `CONTINUATION`, `SPEECH_TO_VIDEO`, `CHARACTER_ANIMATE`, `MIXED_MEDIA`.
