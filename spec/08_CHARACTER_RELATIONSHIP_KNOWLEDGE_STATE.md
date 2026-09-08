# Character, Relationship and Knowledge State

## CharacterRegistry
Each recurring character stores: ID/name/aliases, role, canonical visual refs, face/body/hair, default outfit + variants, voice identity, personality, motivations/flaws, relationships, weapons/props, abilities, special traits and current story state.

## Entity resolution
Aliases, titles and pronouns should resolve to existing entities when supported by context. Extras/background crowds do not become persistent characters unless promoted by story use.

## Character Knowledge State
Track separately: `knows`, `believes`, `suspects`, `misunderstands`, `hides`, `wants`, `fears`. A character must not act on information they do not possess.

## Relationship Graph
Track evolving trust, affection, fear, resentment, authority/power, secrets and unresolved conflict. Numeric values are optional implementation details; prompts use human-readable relational state.

## Knowledge access and alias ambiguity
Knowledge entries identify proposition_id, stance, acquisition event, valid story position and source version. `knows` must have an authorized acquisition path (observation, disclosure or established prior knowledge); beliefs/suspicions may be false and do not become world truth. Misunderstands records the believed proposition and its correction relationship. Hides is deliberate concealment, not lack of knowledge. Wants/fears are motivations, not factual assertions. Author-only hidden truth may be used by planning but must not be supplied as known to a character's dialogue/performance context.
Check access at the scene's story position, including flashbacks and parallel scenes. A later discovery must not leak backwards. Alias resolution is project-scoped; duplicate names/titles return candidate IDs and evidence, and unresolved pronouns do not mutate canon. Relationship edges are directional, versioned and story-positioned. A ten-character registry is supported without attaching ten identities to every shot.
