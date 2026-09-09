# End-to-End Workflow State Machines

## Project run
`DRAFT → UNDERSTANDING → RESEARCHING? → PLANNING → PLAN_READY → AUTHORIZED → PRODUCING → REVIEWING → FINALIZING → COMPLETE`
Overlays: `WAITING_USER | BLOCKED | CANCEL_REQUESTED | FAILED_PARTIAL`.

## Canonical execution
1. ingest/validate assets;
2. understand intent and scope/content mode;
3. group refs/entities and build scoped context;
4. decide research ROI and build EvidencePack if needed;
5. create CreativeStrategy/story/canon/directing artifacts;
6. choose ProductionStrategy and GenerationPlan;
7. resolve effective model/provider capabilities;
8. selective keyframe/source planning;
9. pre-generation creative/production/cost gate;
10. create SpendAuthorization;
11. schedule dependency-aware jobs;
12. generate first attempts;
13. QA and persist observed continuity;
14. user accepts or requests contextual revision;
15. selectively invalidate/recompute dependencies;
16. assemble deterministic timeline;
17. FinalMaster QA/export;
18. commit outcome/taste/series state.

## Shot lifecycle
`PLANNED → READY → AUTHORIZED → GENERATING → QA → READY_REVIEW → ACCEPTED`
Alternates: `BLOCKED | FAILED | RECONCILING | REVISION_DRAFT | STALE`.

## Keyframe lifecycle
`NOT_NEEDED | PLANNED → WAITING_SOURCE/GENERATING → VALIDATING → ACCEPTED`
with `REJECTED | NEEDS_CORRECTION`.

## Revision lifecycle
`INTENT → DIFF → IMPACT_ANALYSIS → COST_PREVIEW → USER_ACTION/AUTHORIZATION → NEW_VERSION → QA → ACCEPT/REJECT`.

## Long-form/series
Episode completion is not `COMPLETE` until accepted outputs are summarized into a versioned episode/canon snapshot and unresolved state is persisted for next episode.

## Optional stages and durable authority
Steps list available capabilities, not a mandatory identical workflow. Reused CURRENT inputs and simple edits may skip satisfied stages. Production jobs use only spec/29 statuses; shot acceptance and artifact currency are orthogonal domain facts. QA can persist an observation for review but only accepted output releases a continuity dependency. A user-approved paid plan authorizes its enumerated first candidates, never an unbounded Director repair loop. Series acceptance commits the episode snapshot transaction before reporting completion.

## LOCALIZATION source-video workflow
After core release, route explicit imported-video translation to `spec/47_SOURCE_VIDEO_LOCALIZATION.md`: ingest → language/transcript analysis → source-context translation → estimate/authorize selected subtitle/dub work → optional controlled TTS/background processing → deterministic alignment/mix → QA/export. Skip nonselected stages; a verified supplied transcript can skip ASR. All stages use existing durable jobs, versioned artifacts, cancellation and spend semantics. No storyboard, Seedance, image generation or lip-sync stage is reachable. Check & align reads a snapshot, applies only safe unlocked deterministic patches as a new version, and lists any separately authorized paid revision. Staleness remains local to dependencies; a late callback cannot replace newer accepted work.
