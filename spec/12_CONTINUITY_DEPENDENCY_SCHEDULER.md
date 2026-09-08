# Continuity Dependency Scheduler

## Core rule
`DEPENDENT → SEQUENTIAL`  
`INDEPENDENT → MAY PARALLELIZE`

A dependent child cannot start until required parent output is accepted.

## Continuity Baton
Persist after each accepted shot: character identities, current outfit/hair, props + state, injuries/body state, location, position/screen side, movement direction, eyeline, lighting/time/weather, emotional state, story state, music/ambience, last accepted frame and last accepted video.

## Cross-shot QA
Compare N vs N-1 for identity, outfit, props, location, injury/state, eyeline, position, movement direction, lighting/time, emotional/story state and audio state.

## Dependency graph
Shots/scenes form a DAG. Only dependency edges block execution.

## Continuity Sandwich for revision
When revising a middle shot, use incoming accepted state from previous dependency + current revision intent + outgoing state required by an already accepted next dependency. If revised output cannot satisfy the next accepted shot start state, mark that next shot STALE; do not hide the break.

## Acceptance, concurrency and dependency currency
Reject cycles, self-edges, unknown IDs and cross-project edges before scheduling. Edges identify consumed source versions and semantic fields (identity, outfit, exit pose, voice, etc.). Check all required parents are accepted and CURRENT when claiming work and again immediately before submission. Claim with a durable lease/fencing token; a stale worker cannot submit, accept or commit after losing ownership. Independent branches share atomic spend reservations.
Accepting a version commits the accepted pointer, QA decision, observed baton and dependency currency update in one transaction. QA PASS is not acceptance by itself. Auto-accept is permitted only by recorded low-risk acceptance policy; UNKNOWN critical checks require review. A rejected/corrupt/unaccepted parent never emits an accepted baton. Baton unknowns remain null with observation evidence; do not hallucinate off-screen states.
An input change during an in-flight child quarantines its result as STALE pending compatibility review. It does not cancel billing retroactively. Propagate staleness only across consumed fields; a compatible rebase records the new source pins and comparison evidence while preserving historical provenance. Reverting reevaluates actual source pins and observed interfaces, not version numbers alone. No acceptance/revert/stale operation submits media.

`observed_state` in the Baton is the normalized state consumed by compilation; the summary characters/props/story_state fields are derived projections and must agree on overlapping entity/fact IDs. Disagreement fails validation, not precedence guessing. Character knowledge_entries is the causal record; compact knows/believes/etc lists are projections at the requested story position and cannot introduce facts absent from entries.
