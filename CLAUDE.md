# CLAUDE.md

Claude must treat `AGENTS.md` + `spec/00_SPEC_LOCK.md` as binding.

For a specification-audit assignment, follow the specification-maintenance scope in AGENTS.md; inspect numbered packets for readiness without executing application tasks or treating absent application code as an audit blocker.

Use one canonical numbered task per implementation session. Read `governance/AI_CODING_PROTOCOL.md`, inspect repository reality before editing, and load only task-linked docs/schemas plus concrete dependencies discovered in code. Task IDs are not naive execution order; honor `tasks/00_IMPLEMENTATION_ORDER.md`, especially Durable Jobs + SpendAuthorization/PaidAttemptGuard before any real paid Seedance call.

Implement vertically; preserve provider-neutral Director ports, EffectiveCapability resolution, scoped canon/ActiveContextPack, continuity dependencies, artifact currency/versioning, all-source keyframes, CompositionTimeline/FinalMaster and paid-attempt rules. Never create a new paid media attempt automatically after QA rejection or ambiguous timeout.

Before completion run applicable tests/Golden Scenarios, update traceability, and self-audit against canonical requirements. If a future canonical change is genuinely needed, prepare ADR/spec-change proposal instead of silently applying it.

## Implementation handoff
Before application work, follow `governance/IMPLEMENTATION_HANDOFF.md`: establish actual roots and loaded instructions, pin the canonical revision, verify prerequisites and preserve criterion-complete evidence/checkpoints. This does not start application tasks during a specification audit.
