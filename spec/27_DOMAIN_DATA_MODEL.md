# Domain Data Model

This is conceptual/normative; concrete SQL/ORM choices follow repository reality.

## Core hierarchy
`User → Project → [Series?] → Episode → Scene → Shot → ShotVersion → Artifact`

SHORT projects may omit Series/Episode wrappers internally where implementation can preserve the same contracts without fake objects. LONG_SINGLE and SERIES persist richer state.

## Core entities
### Project
id, owner, title, scope, content_mode, objective, language, aspect, duration target, quality policy, spend policy, research policy, current canon version, created/updated.

### Series / Episode
Series stores world-level continuity. Episode stores episode objective/arc, accepted canon snapshot, unresolved threads and active cast.

### Scene
purpose, conflict/change, location/time, active characters, entry state, exit state, dependency edges, editorial intent.

### Shot
scene_id, purpose, generation plan slot, required input state, desired output state, reference strategy, dependency edges, accepted_version_id.

### ShotVersion
immutable version record: parent version, revision intent, UniversalVideoSpec version, compiled prompt, refs, provider/model/params, result artifact, QA, cost and status.

### Artifact
typed media/text/document state with dependencies and `CURRENT | STALE | MISSING | BLOCKED` currency.

### EntityRegistry
Characters, products, props and locations. Aliases resolve to canonical IDs.

### CharacterState
canonical identity + mutable outfit/hair/injury/location/emotion/story state. CharacterKnowledgeState is separate from world truth.

### RelationshipEdge
source/target, trust/affection/fear/resentment/power/secrets and narrative notes.

### ProjectCanonVersion
immutable snapshot/diff of world facts, current facts, rumors, unknowns, retcons, character beliefs and unresolved story threads.

### ReferenceBinding
artifact → entity/role/lock/lifetime + positive control + negative scope.

### ContinuityBaton
accepted real output state transferred to dependent shots.

### GenerationAttempt
each provider submission, including estimate, actual cost, upstream task ID, idempotency key/hash, lifecycle and reconciliation state.

### ResearchEvidence
claim/source/confidence/freshness/scope plus reusable EvidencePack membership.

### VoiceProfile
speaker identity, reference audio/provider ID, timbre, pace, accent, emotional range, language capability and pronunciation dictionary.

## Immutability
Accepted/generated provenance and historical shot versions are never destructively rewritten. Canon changes create new versions. Derived artifacts become stale rather than disappearing.
