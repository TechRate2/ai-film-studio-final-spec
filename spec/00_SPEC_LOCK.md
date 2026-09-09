# SPEC LOCK — Architectural Invariants

**Authority:** Highest.  
**Change policy:** owner approval + ADR required for future canonical changes.

## Product identity
The product is an **AI Creative Director + Autonomous Video Production Studio**, not a prompt generator and not a thin text-to-video wrapper.

## Immutable invariants

### Brain
- One visible **Generalist Director** orchestrates internal tools/skills.
- No hard-coded `if niche == ...` production architecture.
- Short, long and serialized content share one brain with adaptive planning/memory depth.
- The Director can say “I do not know enough” and research before expensive decisions.
- From its first implementation, the Director depends on provider-neutral ports/tool contracts; concrete vendor SDKs do not become brain architecture.

### Research
- Evidence-first when real/current/model-specific/niche-specific evidence can materially improve quality.
- Search is targeted and budgeted, not unlimited.
- Fresh trusted evidence is cached and reused.
- Raw search dumps never go directly to creative generation; research is distilled into `EvidencePack`.
- Research stops when additional evidence is unlikely to change the material decision.

### Memory and canon
- Chat history is not authoritative canon.
- Long-form/series truth lives in persisted Project/Series/Episode/Scene/Shot state.
- Character knowledge, beliefs, secrets, wants/fears and relationships are distinct from audience/world truth.
- Context is scoped to active entities and relevant history through a versioned ActiveContextPack or equivalent contract.
- Canonical identity/default appearance/voice remain source of truth; accepted output is continuity evidence, not identity truth.

### References and assets
- Uploaded/imported media is validated/ingested before becoming production reference state.
- Reference files have explicit roles and lock semantics.
- Smallest sufficient reference pack is preferred.
- Video refs may be motion/camera/style-only and must not leak unrelated identity/story/background.
- Keyframes are selective, never mandatory per shot.
- Internal, external, user-supplied, previous-accepted-frame and no-keyframe routes are first-class.

### Production
- Content mode and generation mode are separate decisions.
- A project may mix T2V, I2V, reference-to-video, continuation, S2V/animate, existing media and mixed media by scene/shot.
- Expensive media generation happens after cheaper reasoning/preflight when those checks can reduce failure risk.
- Final assembly is represented by a durable composition/timeline artifact and a validated FinalMaster.

### Continuity
- Dependent shots are sequential: a child cannot start until its required parent output is accepted.
- Independent branches may run concurrently.
- Accepted real output state is preferred as continuity evidence for the next dependent shot.
- Continuity Baton is persisted after accepted shots.
- Switching/reverting an accepted version re-evaluates downstream currency; it does not silently regenerate stale paid media.

### Model/provider separation
- `ModelProfile`: behavior, prompt bias, capabilities, failures, measured reliability.
- `ProviderProfile`: endpoint exposure, price, limits, regions, queue/billing behavior.
- Runtime uses EffectiveCapability = ModelProfile ∩ ProviderProfile ∩ account entitlement ∩ product/project policy.
- Model-specific prompt logic belongs in compilers/profiles.
- Provider-specific transport belongs in adapters.
- Unknown capability is valid; never guess.

### Paid attempts, authorization and revision
- No silent/automatic paid media regeneration after quality rejection.
- Infrastructure polling/recovery is not a new paid generation attempt.
- A user Create/plan approval may authorize the planned **first attempts** under an explicit SpendAuthorization/hard cap so the product does not ask before every shot.
- Default paid candidate count is 1; multiple candidates must be explicitly planned/costed before authorization.
- After a result was produced/billed, another paid generation is a new attempt/revision and requires applicable user-directed action/authorization.
- User may explicitly create a new shot version; original versions remain immutable.
- Revision reconstructs context from canon, refs, incoming continuity and outgoing target.
- A timeout/unknown submission must reconcile upstream state before any resubmission.
- Deterministic non-paid repairs may auto-run only when they preserve creative intent and do not create a new billable generative task.

### Artifact state
Artifacts use `CURRENT | STALE | MISSING | BLOCKED`.
Changing an upstream input invalidates only affected downstream artifacts. Unaffected successful artifacts are preserved.

### Cost
- Cost is visible/estimated before paid authorization/generation.
- Hard spend caps exist at project/user/day/provider/global scopes as applicable.
- Primary optimization includes `cost_per_accepted_second`.
- Cheapest sufficient production method is preferred; not every second must be generative video.

### UX
- Default experience is chat-first: input + attachments + progress + previews.
- Advanced controls use progressive disclosure.
- Users express intent; system translates intent into pipeline changes.
- Shot-level revision is natural-language driven with version history.
- UI never requires provider prompt syntax knowledge.

### Safety, rights and production code
- Project/media authorization, rights/consent/provenance and provider policy are enforced at production boundaries.
- Provider moderation must not be silently bypassed by hidden switching.
- No demo/mock fallback in production execution.
- Every paid artifact stores spec/profile/compiler/prompt/model/provider/params/refs/result/cost/QA provenance.
- Deterministic tests may use fixtures/test doubles only under test.

## Source-video localization extension (owner-approved, ADR 0002)
After the main studio's Phase 6 gate, a separate LOCALIZATION workflow translates subtitles and/or dubs original video. It shares the one Director and existing infrastructure but never creates video/images or changes faces/lips. Explicit deterministic playback-speed changes, subtitles and audio derivatives are allowed while source media remains immutable. One-click AI checking/alignment preserves user locks, versions and all paid-attempt rules. This does not require a localization customer to create or purchase a generative-video project. See `spec/47_SOURCE_VIDEO_LOCALIZATION.md`.
