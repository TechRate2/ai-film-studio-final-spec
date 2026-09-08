# CLAUDE.md

Claude must treat `AGENTS.md` + `spec/00_SPEC_LOCK.md` as binding.

Use one canonical task per implementation session. Read `governance/AI_CODING_PROTOCOL.md`, inspect repository reality before editing, and load only task-linked docs/schemas plus concrete dependencies discovered in code. Do not redesign architecture for convenience.

Implement vertically; preserve model/provider separation, scoped canon, continuity dependencies, artifact currency/versioning and PaidAttemptGuard. Never create a new paid media attempt automatically after QA rejection or ambiguous timeout.

Before completion run applicable tests/golden scenarios, update traceability, and self-audit against canonical requirements. If a canonical change is genuinely needed, prepare ADR/spec-change proposal instead of silently applying it.
