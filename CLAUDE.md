# CLAUDE.md

Claude must treat `AGENTS.md` + `spec/00_SPEC_LOCK.md` as binding.

Use one canonical numbered task per implementation session. Read `governance/AI_CODING_PROTOCOL.md`, inspect repository reality before editing, and load only task-linked docs/schemas plus concrete dependencies discovered in code. Task IDs are not naive execution order; honor `tasks/00_IMPLEMENTATION_ORDER.md`, especially Durable Jobs + SpendAuthorization/PaidAttemptGuard before any real paid Seedance call.

Implement vertically; preserve provider-neutral Director ports, EffectiveCapability resolution, scoped canon/ActiveContextPack, continuity dependencies, artifact currency/versioning, all-source keyframes, CompositionTimeline/FinalMaster and paid-attempt rules. Never create a new paid media attempt automatically after QA rejection or ambiguous timeout.

Before completion run applicable tests/Golden Scenarios, update traceability, and self-audit against canonical requirements. If a future canonical change is genuinely needed, prepare ADR/spec-change proposal instead of silently applying it.
