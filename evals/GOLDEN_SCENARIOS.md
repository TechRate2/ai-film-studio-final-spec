# Golden Scenarios V4.2

These are behavioral acceptance scenarios, not aesthetic/virality guarantees. Tests may use deterministic fixtures unless explicitly marked as paid-provider smoke.

## GS01 — 30s UGC product
Group same product entity; research only when useful/current; create audience/creative strategy; prefer reliable long generations over mechanical micro-shots; preserve product fidelity; show cost before authorization/paid calls.

## GS02 — Fashion ad
Select camera, fit/fabric proof and pacing appropriate to fashion, not generic cinematic moves. Style/Platform grammar may influence choices without hard-coded fashion pipeline.

## GS03 — 60s xianxia drama
Three active characters, dialogue, action and cliffhanger. Persist identity/outfit/voice; hierarchy story→blocking→camera; dependent segments sequential; compile Seedance-specific stages; accepted output seeds next dependency.

## GS04 — 120s Saturn sci-fi
Use factual research for Saturn/space realism when available; separate Fact Pack from creative strategy; create mini-story rather than sightseeing; selective keyframes; mixed-media optimization allowed; no duplicate paid retry.

## GS05 — 7-character serialized film
Episode 1 uses active subset. Episode 2 resumes canon without re-uploading refs. Character knowledge prevents omniscient dialogue; ActiveContextPack excludes irrelevant full-series state.

## GS06 — Current-news explainer
Research required; Fact Pack with source provenance/freshness; no unsupported factual claims; production may prefer screenshots/charts/B-roll over all-generated video.

## GS07 — Multi-character dialogue
Preserve speaker/voice/eyeline/blocking and choose native/post/S2V route according to effective capability/reliability.

## GS08 — External keyframe
Agent creates copy-ready prompt + exact ref pack, imports external image, validates it and continues with zero internal image generation charge. Invalid image gets correction patch, not silent internal fallback.

## GS09 — Shot revision / Continuity Sandwich
Accepted Shot5→Shot6→Shot7. User: “Make Shot6 sword motion slower, keep face/outfit/light/end state.” Keep v1, create v2, semantic diff only, use incoming Shot5 + outgoing Shot7 target, show incremental cost, stale Shot7 only if necessary.

## GS10 — Spend/timeout safety
Potential upstream creation followed by timeout must not trigger blind second paid task. Reconcile upstream status and enforce spend cap.

## GS11 — Language change
Changing Vietnamese to Chinese after visual acceptance must not regenerate visuals unless chosen lip-sync route truly requires it. Voice identity remains same character identity.

## GS12 — Product factual claim
Ad script must not invent material product claims from image appearance. Claim comes from FACT_SOURCE/user-verified data.

## GS13 — 10-person battle
Planner avoids exact overloaded choreography for all 10 in one generative shot; uses readable wide/group + focused action according to scene purpose.

## GS14 — No-keyframe simple B-roll
Direct generation works without forced storyboard/keyframe.

## GS15 — Provider switch
Same model through provider B exposes different API limits without Director rewrite; EffectiveCapability changes through profile/exposure, not creative branch.

## GS16 — Smart Auto internal keyframe
Controller determines one hero keyframe materially reduces video-failure risk. `AUTO_INTERNAL` uses ImageProvider under authorization, validates image, records provenance/cost, and does not generate keyframes for other low-risk segments.

## GS17 — Controlled voice across languages
Recurring character has VoiceProfile. Episode A Vietnamese and localized variant Chinese use production VoiceProvider/post route while preserving voice identity/proper-name pronunciation; visual media remains current unless explicit lip-sync dependency exists.

## GS18 — Asset ingestion / dedupe / corrupt file
User uploads duplicate character images, valid video, corrupt video and external keyframe. Valid duplicates resolve by hash/entity logic, corrupt media becomes FAILED/actionable, other assets continue, external source provenance is retained.

## GS19 — FinalMaster QA
Accepted shots assemble into CompositionTimeline. Export with intentionally missing audio region/subtitle overflow fails FinalMaster QA without regenerating accepted video. Deterministic repair produces validated master/checksum.

## GS20 — Effective capability mismatch
ModelProfile says reference audio possible in principle, provider/account does not expose it. Runtime resolves UNSUPPORTED/DEGRADED and chooses explicit post-voice/degrade or blocks; never assumes model marketing capability.

## GS21 — Accepted-version revert
Shot6 v2 is accepted and makes Shot7 stale; user reverts accepted version to v1. Dependency graph re-evaluates currency from source versions. No stale paid artifact is regenerated automatically.

## GS22 — Multi-candidate cost authorization
Agent believes two candidates may be useful. Default remains one until plan explicitly shows `candidate_count=2` and total incremental cost. Only authorized count may be submitted.

## GS23 — Rights/consent/source safety
Project includes real-person voice/face reference, licensed brand asset and unverified music. System preserves consent/rights/provenance state, prevents unsupported product claim and surfaces missing commercial-use music rights rather than silently treating all assets as free.

## GS24 — Provider fallback and paid-state certainty
Provider A fails in NOT_SUBMITTED state: same logical authorized attempt may route to allowed provider B within cap. Provider A returns UNKNOWN: system enters RECONCILING. Provider A produced/billed output: provider B cannot be silently called as retry.

## GS25 — Research cache/freshness/stop rule
Two projects ask same stable model question within valid cache window; second reuses evidence. A current/provider-version change invalidates relevant evidence. Research stops once decision confidence/stop condition is met and does not loop for marginal sources.
