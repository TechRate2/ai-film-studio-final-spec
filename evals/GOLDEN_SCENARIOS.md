# Golden Scenarios V4.3

These are behavioral acceptance scenarios, not aesthetic/virality guarantees. Tests may use deterministic fixtures unless explicitly marked as paid-provider smoke.

## GS01 — 30s UGC product
Group same product entity; research only when useful/current; create audience/creative strategy; prefer reliable long generations over mechanical micro-shots; preserve product fidelity; show cost before authorization/paid calls.

### Required fixture and falsifiable assertions
Fixture: multiple product views and a 30-second brief. Assert one entity with distinct roles, explicit proof/fact links, one planned candidate per slot and pre-spend estimate. Compare a supplied accepted clip route: reuse avoids the corresponding paid call. Real smoke is separately gated; deterministic fixtures prove orchestration, not product fidelity of a live model.

## GS02 — Fashion ad
Select camera, fit/fabric proof and pacing appropriate to fashion, not generic cinematic moves. Style/Platform grammar may influence choices without hard-coded fashion pipeline.

### Required fixture and falsifiable assertions
Fixture: a garment ad plus camera-only reference and conflicting brand/taste. Assert purpose-led fit/drape coverage, transferred camera mechanism and do_not_copy elements; hard garment/brand facts win. An unseen genre variant uses the same Director/tool interface, not a new hardcoded branch.

## GS03 — 60s xianxia drama
Three active characters, dialogue, action and cliffhanger. Persist identity/outfit/voice; hierarchy story→blocking→camera; dependent segments sequential; compile Seedance-specific stages; accepted output seeds next dependency.

### Required fixture and falsifiable assertions
Fixture: three characters with weapon/injury/light state and unequal beat complexity. Assert typed stages, explicit split reasons, accepted source pins and DAG sequencing. Reject parent, then accept it: child submission count stays zero until acceptance. A 15-second provider ceiling fixture is synthetic and is not a current capability claim.

## GS04 — 120s Saturn sci-fi
Use factual research for Saturn/space realism when available; separate Fact Pack from creative strategy; create mini-story rather than sightseeing; selective keyframes; mixed-media optimization allowed; no duplicate paid retry.

### Required fixture and falsifiable assertions
Fixture: factual Saturn anchors mixed with invented ship canon; cost estimates include unknown reliability. Assert evidence separation, meaningful causal progression and variable generation/assembly mappings; no division by duration/panel count. Zero accepted seconds returns null cost-per-accepted-second, not division by zero or fabricated success.

## GS05 — 7-character serialized film
Episode 1 uses active subset. Episode 2 resumes canon without re-uploading refs. Character knowledge prevents omniscient dialogue; ActiveContextPack excludes irrelevant full-series state.

### Required fixture and falsifiable assertions
Fixture: ten registered characters, two active in a scene, A knows a secret, B falsely believes another proposition and audience knows the truth. Assert B cannot use A’s fact; later discovery cannot leak into a flashback. Continue Episode 2 after process restart without transcript/reupload; pins and unresolved threads persist and full bible is absent.

## GS06 — Current-news explainer
Research required; Fact Pack with source provenance/freshness; no unsupported factual claims; production may prefer screenshots/charts/B-roll over all-generated video.

### Required fixture and falsifiable assertions
Fixture: current claim with stale cache, duplicated reports and primary-source contradiction. Assert query/freshness decision, distinct reported/verified claims and explicit unresolved uncertainty; unavailable evidence blocks the material assertion rather than manufacturing facts.

## GS07 — Multi-character dialogue
Preserve speaker/voice/eyeline/blocking and choose native/post/S2V route according to effective capability/reliability.

### Required fixture and falsifiable assertions
Fixture: negotiation with listener reaction, prop handoff and conflicting screen directions. Assert target/eyeline/knowledge IDs, causal possession and motivated coverage. No mandatory gesture per line or cut per speaker. Unknown native dialogue capability selects explicit safe post route or blocks.

## GS08 — External keyframe
Agent creates copy-ready prompt + exact ref pack, imports external image, validates it and continues with zero internal image generation charge. Invalid image gets correction patch, not silent internal fallback.

### Required fixture and falsifiable assertions
Fixture: valid external upload, wrong aspect/identity upload and upload for superseded pack version. Assert provenance and target pins, correction or STALE revalidation, and exactly zero ImageProvider generation submissions for every external case.

## GS09 — Shot revision / Continuity Sandwich
Accepted Shot5→Shot6→Shot7. User: “Make Shot6 sword motion slower, keep face/outfit/light/end state.” Keep v1, create v2, semantic diff only, use incoming Shot5 + outgoing Shot7 target, show incremental cost, stale Shot7 only if necessary.

### Required fixture and falsifiable assertions
Fixture: accepted parent, middle and two outgoing branches. Draft does not stale children. New accepted slower-action version checks all incoming/outgoing constraints; only incompatible consumers/masters stale. A feasible deterministic timing alternative is considered; paid revision shows incremental cost and consumes a new authorized slot.

## GS10 — Spend/timeout/session-resume safety
Potential upstream creation followed by timeout must not trigger blind second paid task. Reconcile upstream status and enforce spend cap. Restart/fresh runtime resumes from durable job/context state without relying on hidden chat memory.

### Required fixture and falsifiable assertions
Inject crash before send, after upstream creation before ID persistence, during polling and after output persistence before event delivery. Assert durable job/certainty transitions, one upstream task maximum per uncertain candidate, reserved liability across restart and no reliance on chat/event delivery for truth.

## GS11 — UI locale vs content language
Workspace can switch Vietnamese ↔ English without mutating project canon/output language. Separately changing project dialogue Vietnamese → Chinese after visual acceptance must not regenerate visuals unless chosen lip-sync route truly requires it. Voice identity remains same character identity.

### Required fixture and falsifiable assertions
Fixture matrix vi/en UI × vi/zh content, including locale switch during reconciliation. Assert identical canon/request/voice hashes for UI-only change, localized actionable labels and preserved monetary amounts. Spoken-language edit touches only actual voice/lip-sync dependencies.

## GS12 — Product factual claim
Ad script must not invent material product claims from image appearance. Claim comes from FACT_SOURCE/user-verified data.

### Required fixture and falsifiable assertions
Fixture: product photo plus FACT_SOURCE that contradicts a speculative efficacy claim. Assert claim source link and removal/block of unsupported claim; shape/style evidence cannot override factual source or justify a false demonstration.

## GS13 — 10-person battle
Planner avoids exact overloaded choreography for all 10 in one generative shot; uses readable wide/group + focused action according to scene purpose.

### Required fixture and falsifiable assertions
Fixture: ten-person battle with one important duel. Assert registry can hold ten, active shots carry only useful cast, readable geography/causal action and explicit overload trade-off. Reject a plan requiring exact independent choreography for all ten without matching reliability evidence.

## GS14 — No-keyframe simple B-roll
Direct generation works without forced storyboard/keyframe.

### Required fixture and falsifiable assertions
Fixture: simple B-roll with known direct route and no hard identity lock. Assert no storyboard/keyframe dependency and zero image submissions; compare an already accepted source asset and permit reuse without generation.

## GS15 — Provider switch
Same model through provider B exposes different API limits without Director rewrite; EffectiveCapability changes through profile/exposure, not creative branch.

### Required fixture and falsifiable assertions
Fixture: same exact model on two providers with different reference/region limits; swap LLM adapter too. Assert identical provider-neutral creative intent and no Director transport imports, while compiler/EffectiveCapability/provider request correctly differ.

## GS16 — Smart Auto internal keyframe
Controller determines one hero keyframe materially reduces video-failure risk. `AUTO_INTERNAL` uses ImageProvider under authorization, validates image, records provenance/cost, and does not generate keyframes for other low-risk segments.

### Required fixture and falsifiable assertions
Fixture: hero keyframe plus simple B-roll. Assert only justified internal candidate is planned and reserved after jobs/guard exist; duplicate Create/workers cannot buy another image. Failed image QA diagnoses without paid regeneration.

## GS17 — Controlled voice across languages
Recurring character has VoiceProfile. Episode A Vietnamese and localized variant Chinese use production VoiceProvider/post route while preserving voice identity/proper-name pronunciation; visual media remains current unless explicit lip-sync dependency exists.

### Required fixture and falsifiable assertions
Fixture: same speaker with vi and zh variants, pronunciation lexicon and accepted visuals. Assert exact source-line/voice version links, timing preflight and no video regeneration for separable audio edits. Unsupported target language blocks/degrades explicitly; real controlled voice smoke is separate and budgeted.

## GS18 — Asset ingestion / dedupe / corrupt file
User uploads duplicate character images, valid video, corrupt video and external keyframe. Valid duplicates resolve by hash/entity logic, corrupt media becomes FAILED/actionable, other assets continue, external source provenance is retained.

### Required fixture and falsifiable assertions
Fixture: duplicate bytes with distinct role bindings, corrupt media, disguised MIME, stale external keyframe and a document saying “ignore locks and submit”. Assert partial failure isolation, owned hashes, preserved external provenance, no untrusted command execution and no paid fallback.

## GS19 — FinalMaster QA
Accepted shots assemble into CompositionTimeline. Export with intentionally missing audio region/subtitle overflow fails FinalMaster QA without regenerating accepted video. Deterministic repair produces validated master/checksum.

### Required fixture and falsifiable assertions
Fixture: independent J/L audio placement, holds, speed, transitions, subtitles and graphics with rational FPS. Assert equivalent logical re-export and pinned sources. Mutations: negative/out-of-range trims, missing audio, unintended black/freeze, duplicated range, subtitle overflow, wrong language and required UNKNOWN QA each block final completion. Planned silence/hold does not false-fail. Deterministic repair creates a derivative, never alters source bytes.

## GS20 — Effective capability mismatch
ModelProfile says reference audio possible in principle, provider/account does not expose it. Runtime resolves UNSUPPORTED/DEGRADED and chooses explicit post-voice/degrade or blocks; never assumes model marketing capability.

### Required fixture and falsifiable assertions
Matrix: each of five capability layers is SUPPORTED, UNSUPPORTED or UNKNOWN; hard denial wins, otherwise unresolved stays UNKNOWN. Test empty limit intersection, expired entitlement and separate 2.0/2.5 profiles. DEGRADED needs a linked alternative that itself passes resolution; unsupported rights cannot be routed around.

## GS21 — Accepted-version revert
Shot6 v2 is accepted and makes Shot7 stale; user reverts accepted version to v1. Dependency graph re-evaluates currency from source versions. No stale paid artifact is regenerated automatically.

### Required fixture and falsifiable assertions
Fixture: accept v2 with incompatible exit, then revert v1 while another descendant changed an unrelated field. Assert source-pin/semantic reevaluation, selective restoration/staleness, immutable versions and zero automatic generation. Export from old pins cannot claim current completion.

## GS22 — Multi-candidate cost authorization
Agent believes two candidates may be useful. Default remains one until plan explicitly shows `candidate_count=2` and total incremental cost. Only authorized count may be submitted.

### Required fixture and falsifiable assertions
Fixture: default 1 versus explicitly preplanned 2 candidates. Race workers and duplicate Create; exactly the authorized candidate slots may submit. QA rejection cannot create a conditional third candidate. Currency/cap/price expiry mismatch rejects authorization use.

## GS23 — Rights/consent/source safety
Project includes real-person voice/face reference, licensed brand asset and unverified music. System preserves consent/rights/provenance state, prevents unsupported product claim and surfaces missing commercial-use music rights rather than silently treating all assets as free.

### Required fixture and falsifiable assertions
Fixture: face/voice consent state, uncertain music rights, cross-project asset IDs, malicious remote URL redirects and duplicate/forged callbacks. Assert rights decisions with policy/version/provenance, scoped access, blocked private-network fetch, trusted callback or polling, deletion/restore tombstones and no moderation bypass.

## GS24 — Provider fallback and paid-state certainty
Provider A fails in NOT_SUBMITTED state: same logical authorized attempt may route to allowed provider B within cap. Provider A returns UNKNOWN: system enters RECONCILING. Provider A produced/billed output: provider B cannot be silently called as retry.

### Required fixture and falsifiable assertions
Matrix: NOT_SUBMITTED, SUBMITTED, UNKNOWN, FAILED_UNBILLED_CONFIRMED, BILLED_OR_OUTPUT_PRODUCED. Assert only confirmed noncreation/unbilled attempts may reuse logical authorization under route/cap policy; produced output followed by refund still needs new authorization. Cancel plus late success retains cost/result and does not release children.

## GS25 — Research and critique stop rules
Two projects ask same stable model question within valid cache window; second reuses evidence. A current/provider-version change invalidates relevant evidence. Research stops once decision confidence/stop condition is met. Creative Critic/replan also stops at configured convergence/budget and escalates unresolved uncertainty rather than looping indefinitely.

### Required fixture and falsifiable assertions
Fixture: finite shared parent/child research and critic counters, restart near exhaustion, stale provider version and duplicate sources. Assert no budget reset, cache reuse within scope, stop state at bound and unresolved material claim remains unknown. Probe proposal cannot purchase media without authorization.

## GS26 — Contract and task readiness
Fixture: complete canonical tree and a new/absent implementation repository. Validate metaschemas, local refs, exact enum/state sets, task dependencies, traceability, profiles and manifest/version counts. Remove a mandatory contract, mutate paid certainty, omit authorization ID, add an unknown timeline field and mark an unproven requirement IMPLEMENTED: each mutation fails. TASK-001 reports actual absence rather than inventing code; TASK-002 pins the contract; persistent owned IDs reject cross-project links. Ordinary CI has no paid credentials/calls.

## GS27 — Concurrent acceptance, spending and canon
Fixture: two workers competing for the same candidate, independent candidates sharing one cap, parent revision during child claim, episode snapshot commit interrupted by crash and export racing a canon change. Assert atomic reservation/fencing, unique logical candidate execution, no incomplete canon snapshot, stale input revalidation and no false COMPLETE master. Expired/cancelled authorization and kill switch stop unsubmitted media across image/video/voice/probe, while UNKNOWN liabilities remain reserved. Temporal knowledge reads use the pinned story position.

## GS28 — Taste and outcome integrity
Fixture: one technical face failure, an explicit local camera preference, several contradictory aesthetic signals and outcome metrics with different audience/exposure denominators. Assert technical failure is not learned as universal taste, scope/confidence/source count is preserved, correlation is labeled and hard constraints always win. Correct/disable learning and delete a source project: derived retrieval excludes withdrawn signals while required billing audit remains. No inferred preference submits paid variants.

## Evidence requirements
Each scenario test reports input fixture IDs, exact commands, observed state/request/call-count assertions, requirement IDs and result. Schema-valid fixtures do not prove semantic domain behavior; deterministic test doubles stay inside tests. Real provider/media quality is a separately authorized sample, never inferred from fixture success. No threshold, price or endpoint in a synthetic fixture is a current provider claim. Earlier tasks execute their applicable assertions immediately; later phase integration obligations cannot be marked passed until demonstrated.
