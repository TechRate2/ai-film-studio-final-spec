# StyleDNA and Grammar Layers

## Purpose
Translate references, genre/platform conventions, brand constraints and user taste into reusable creative mechanisms without copying protected expressive content or hard-coding niche pipelines.

## StyleDNA
A reference-video/image analysis may produce a `StyleDNA` artifact containing:
- narrative structure and hook pattern;
- emotional curve and pacing profile;
- average/relative shot duration pattern;
- shot-scale distribution;
- camera movement profile, height/path and lens feel;
- composition rules and negative-space behavior;
- lighting/color language;
- performance/dialogue/action density;
- transition/editing language;
- audio hierarchy and music-energy curve;
- realism/VFX treatment;
- `transferable_traits`;
- `do_not_copy_elements`.

StyleDNA describes mechanisms, not identities, copyrighted characters, exact dialogue, branded locations or protected story expression.

## Grammar layers
The Director may retrieve and compose:
- `GenreGrammar` — conventions/expectations of genre;
- `PlatformGrammar` — framing, pacing, safe areas, interaction/CTA conventions;
- `BrandGrammar` — hard/soft brand rules, prohibited treatments, visual tone;
- `UserTasteProfile` — learned preferences from accepted/rejected work;
- `StyleDNA` — transferable traits from supplied references.

These are not separate pipelines and never override Project Canon, factual evidence, safety/rights requirements or provider capability truth.

## Conflict precedence
1. safety/rights + explicit user hard constraints;
2. Project Canon and HARD_LOCK references;
3. verified factual/product claims;
4. Brand hard rules;
5. CreativeStrategy/story intent;
6. StyleDNA / genre / platform grammar;
7. learned taste;
8. model/compiler heuristics.

When two lower-priority layers conflict, the Director records a `DecisionRecord` explaining the chosen trade-off.

## Retrieval discipline
Load only grammar/StyleDNA needed for the current creative decision. Do not dump every genre/platform/reference analysis into every shot prompt.
