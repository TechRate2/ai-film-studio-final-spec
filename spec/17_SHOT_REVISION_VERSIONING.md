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
Dialogue text → text only; voice → audio only; subtitle → subtitle only; music → audio mix; color/grade → post-process; cut/timing → edit; camera/action → video revision; identity/outfit → ref/video; composition → keyframe/video; story fact → canon update + selective downstream invalidation.

## ShotVersionGraph
Never overwrite. `shot_id` has `versions[]` and `accepted_version_id`.

## Continuity Sandwich
Revision must satisfy previous accepted exit state + requested change + next accepted start state where applicable. If impossible, mark affected downstream artifacts STALE and surface the consequence.
