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
