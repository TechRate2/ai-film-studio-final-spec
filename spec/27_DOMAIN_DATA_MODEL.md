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

## Shared contract rules
JSON Schema draft 2020-12 is normative for wire structure; `schemas/common.schema.json` contains shared value records, not a service. IDs are nonempty project-scoped opaque strings. Versions are immutable IDs or explicitly declared positive integers. Timestamps are RFC3339 UTC; costs use a declared currency and fixed-decimal arithmetic at runtime (never binary float for ledger comparisons). Null means unknown/not applicable as documented, never zero cost or unsupported by implication. Domain referential, temporal and transaction constraints below cannot be replaced by JSON parsing.
Closed records reject misspelled fields. Free creative semantics live in explicit descriptive text/list fields or a documented typed extension map; extensions cannot carry new execution commands or silently change normative behavior. Schema revisions preserve the same canonical tree, bump SPEC_VERSION and require migration compatibility for persisted projects.

Cross-object validation additionally enforces unique IDs within arrays, owned/resolvable references, source-pin/version agreement, required knowledge acquisition paths, graph acyclicity and timeline arithmetic. These are application domain tests specified in GS05/GS19/GS27; metaschema/fixture validation alone cannot prove them. Keyframe source NONE needs only an ID/target/reason decision; it does not require a generation prompt, pack, camera or image dependency.

The shared schema also defines Scene, Shot (including the accepted-version pointer), DirectorRun checkpoint and ToolContract records. Scene/shot entry/exit states and story_position are durable; the lightweight SHORT path may omit episode_id using null. DirectorRun is a reasoning lifecycle, not a second production-job vocabulary. Task implementations validate these definitions at their storage/tool boundaries.

## Localization extension records
ProjectIntent.workflow_kind distinguishes STUDIO and LOCALIZATION (legacy absence means STUDIO; new writes provide it). LocalizationProject is a versioned target-language variant referencing immutable source analysis, source-time segments/words, nullable acoustic speaker assignments, glossary, VoiceProfile artifact pins, explicit time-map spans and manual locks. LocalizationReview binds findings and a closed safe-patch list to the exact project/timeline/input versions. `schemas/localization_project.schema.json` and `schemas/localization_review.schema.json` are normative; use the same Artifact currency and DurableJob state system. Full semantic invariants and lifecycle are in `spec/47_SOURCE_VIDEO_LOCALIZATION.md`.
