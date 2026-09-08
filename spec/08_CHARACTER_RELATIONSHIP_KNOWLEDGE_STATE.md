# Character, Relationship and Knowledge State

## CharacterRegistry
Each recurring character stores: ID/name/aliases, role, canonical visual refs, face/body/hair, default outfit + variants, voice identity, personality, motivations/flaws, relationships, weapons/props, abilities, special traits and current story state.

## Entity resolution
Aliases, titles and pronouns should resolve to existing entities when supported by context. Extras/background crowds do not become persistent characters unless promoted by story use.

## Character Knowledge State
Track separately: `knows`, `believes`, `suspects`, `misunderstands`, `hides`, `wants`, `fears`. A character must not act on information they do not possess.

## Relationship Graph
Track evolving trust, affection, fear, resentment, authority/power, secrets and unresolved conflict. Numeric values are optional implementation details; prompts use human-readable relational state.
