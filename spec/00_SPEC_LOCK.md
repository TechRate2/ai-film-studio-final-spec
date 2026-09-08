# SPEC LOCK — Architectural Invariants

**Authority:** Highest.  
**Change policy:** owner approval + ADR required.

## Product identity
The product is an **AI Creative Director + Autonomous Video Production Studio**, not a prompt generator and not a thin text-to-video wrapper.

## Immutable invariants

### Brain
- One visible **Generalist Director** orchestrates internal tools/skills.
- No hard-coded `if niche == ...` production architecture.
- Short, long and serialized content share one brain with adaptive planning/memory depth.
- The Director can say "I do not know enough" and research before expensive decisions.

### Research
- Evidence-first when real/current/model-specific/niche-specific evidence can materially improve quality.
- Search is targeted and budgeted, not unlimited.
- Fresh trusted evidence is cached and reused.
- Raw search dumps never go directly to creative generation; research is distilled into `EvidencePack`.

### Memory and canon
- Chat history is not authoritative canon.
- Long-form/series truth lives in persisted Project/Series/Episode/Scene/Shot state.
- Character knowledge, beliefs, secrets and relationships are distinct from audience/world truth.
- Context is scoped to active entities and relevant history.

### References
- Reference files have explicit roles and lock semantics.
- Smallest sufficient reference pack is preferred.
- Video refs may be motion/camera/style-only and must not leak unrelated identity/story/background.
- Keyframes are selective, never mandatory per shot.
- External/user-supplied keyframes are first-class.

### Production
- Content mode and generation mode are separate decisions.
- A project may mix T2V, I2V, reference-to-video, continuation, S2V/animate and mixed media by scene/shot.
- Expensive media generation happens after cheaper reasoning/preflight when those checks can reduce failure risk.

### Continuity
- Dependent shots are sequential: a child cannot start until its required parent output is accepted.
- Independent branches may run concurrently.
- Accepted real output state is preferred as continuity evidence for the next dependent shot.
- Continuity Baton is persisted after accepted shots.

### Model/provider separation
- `ModelProfile`: behavior, prompt bias, capabilities, failures, measured reliability.
- `ProviderProfile`: endpoint exposure, price, limits, regions, queue/billing behavior.
- Model-specific prompt logic belongs in compilers/profiles.
- Provider-specific transport belongs in adapters.
- Unknown capability is valid; never guess.

### Paid attempts and revision
- No silent/automatic paid media regeneration after quality rejection.
- Infrastructure polling/recovery is not a new paid generation attempt.
- User may explicitly create a new shot version.
- Revision preserves original version and reconstructs context from canon, refs, incoming continuity and outgoing target.
- A timeout must not cause duplicate paid submission without checking upstream task identity when possible.

### Artifact state
Artifacts use `CURRENT | STALE | MISSING | BLOCKED`.
Changing an upstream input invalidates only affected downstream artifacts. Unaffected successful artifacts are preserved.

### Cost
- Cost is visible/estimated before paid generation.
- Hard spend caps exist at project/user/provider scope.
- Primary optimization includes `cost_per_accepted_second`.
- Cheapest sufficient production method is preferred; not every second must be generative video.

### UX
- Default experience is chat-first: input + attachments + progress + previews.
- Advanced controls use progressive disclosure.
- Users express intent; system translates intent into pipeline changes.
- Shot-level revision is natural-language driven.
- UI never requires provider prompt syntax knowledge.

### Production code
- No demo/mock fallback in production execution.
- Every paid artifact stores spec/profile/compiler/prompt/model/provider/params/refs/result/cost/QA provenance.
- Deterministic tests may use fixtures/test doubles only under test.
