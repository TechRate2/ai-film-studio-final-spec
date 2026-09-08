# Project Canon and Series Memory

## Canon is source of truth
Persist immutable world facts, current facts, retconned facts, unknowns, rumors, audience knowledge, per-character knowledge/beliefs and unresolved story threads.

## Memory layers
1. UserTasteProfile
2. Series/Project State
3. Episode State
4. Scene State
5. Shot State

## Retrieval rule
Never load the full series bible by default. Hydrate only active characters, relevant relationship edges, unresolved events, current location/prop/outfit/voice state, recent canonical summary and exact dependencies.

## Episode transition
On episode acceptance: generate canonical summary; commit accepted character/relationship/plot changes; persist unresolved hooks; store last accepted visual/audio states; version the canon snapshot.

## Retcon/update
When user changes a fact: create a new canon version, mark affected downstream artifacts STALE through dependency graph, and never silently regenerate paid media.

## Temporal canon and atomic commits
Fact IDs are stable and refer to versioned propositions, not free-text chat assertions. Track valid story position (episode/scene/beat) separately from recorded_at. World truth, audience disclosure and each character's knowledge access are separate records. Corrections preserve superseded versions with causal source IDs. Canon patches use expected_base_version; concurrent edits reject stale writes and request rebase instead of last-write-wins.
Episode acceptance atomically pins accepted master/timeline, canon version, state/relationship/voice versions and unresolved threads. The episode commit has an idempotency key. A crash either commits the complete snapshot or none. Later revisions create a new snapshot; historical episodes retain their original pins. Long-single films use the same scene/checkpoint semantics without artificial episode overhead.
