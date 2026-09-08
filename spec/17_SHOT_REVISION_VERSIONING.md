# Shot Revision and Versioning

## ContextualShotRevision
User may revise a shot in natural language.

Pipeline:
1. classify edit intent;
2. load accepted/original shot spec;
3. load original compiled prompt and refs;
4. load Project Canon and active entity state;
5. load incoming Continuity Baton;
6. load outgoing expected state if a next accepted dependency exists;
7. create semantic revision diff;
8. choose cheapest affected modality;
9. compile revised request;
10. show incremental cost;
11. submit new paid attempt only after user action/approval policy;
12. QA against revision intent and continuity;
13. preserve all versions;
14. user chooses accepted version.

## EditIntentClassifier examples
Unrendered dialogue text → text only; already spoken dialogue → affected voice/subtitle/lip-sync dependencies; voice → audio when separable; subtitle → subtitle only; music → audio mix; color/grade → post-process; cut/timing → edit; camera/action → video revision; identity/outfit → ref/video; composition → keyframe/video; story fact → canon update + selective downstream invalidation.

## ShotVersionGraph
Never overwrite. `shot_id` has `versions[]` and `accepted_version_id`.

## Continuity Sandwich
Revision must satisfy previous accepted exit state + requested change + next accepted start state where applicable. If impossible, mark affected downstream artifacts STALE and surface the consequence.

## Immutable revisions and fan-out
RevisionRequest pins project, base shot version, canon/context versions, original compiled request and all incoming/outgoing dependency versions, not only a linear neighbor. The semantic diff declares changed/preserved fields and affected modalities. For slower motion first consider authorized deterministic retiming if it preserves speech, end timing and continuity; otherwise propose a new video attempt. The classifier is dependency-aware, not a hardcoded keyword→billable-route table.
Creating a draft does not invalidate accepted downstream media. Only acceptance of a changed output/canon fact changes the current dependency view. New results retain their own immutable inputs; accepting/reverting changes a separate pointer and audit event. Historical status/QA may have append-only events without rewriting historical media or request payloads. A version created from a stale base requires rebase/revalidation before spend and acceptance. Changed outgoing requirements are shown before authorization and checked after generation. If incompatible after acceptance, stale only the affected dependencies and derived masters; never conceal or regenerate them.
