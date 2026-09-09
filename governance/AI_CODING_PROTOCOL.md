# AI Coding Protocol — Codex / Claude

## Purpose
Convert vibe coding from open-ended improvisation into controlled spec-driven implementation.

## Session bootstrap
This numbered-task execution protocol applies to application implementation. A canonical specification audit instead follows AGENTS.md's specification-maintenance scope and reports requirement coverage/findings; it does not start TASK-001 or require an application repository.

Every substantial coding session must identify exactly one active task packet. Before edits, the coding agent reads `AGENTS.md`, `spec/00_SPEC_LOCK.md`, this protocol, the task packet and only its linked canonical docs/schemas.

## Mandatory execution loop
1. **Reality** — inspect current implementation files/symbols/tests. Do not infer existence from spec.
2. **Gap map** — map task acceptance criteria to current code.
3. **Plan** — list minimal vertical changes and affected boundaries.
4. **Implement** — persistence/domain/API/UI/tests together where applicable.
5. **Verify** — typecheck/lint/unit/integration/contract tests.
6. **Golden** — run affected golden scenarios.
7. **Self-audit** — compare exact behavior against canonical requirements.
8. **Independent review** — preferably another model/reviewer checks drift, cost and continuity risks.
9. **Traceability** — populate implementation refs/test refs; use PARTIAL rather than false completion.
10. **Commit** — only after acceptance evidence exists.

## Anti-drift
The agent may not redesign architecture because another pattern is fashionable or easier to code. It may propose an ADR, but must not silently implement a canonical change.

## Context discipline
Do not load the entire spec and project into every session. Over-context causes contradictory attention and drift. Use task-scoped retrieval and concise repository-reality notes.

## Cost/safety discipline
No coding shortcut may bypass PaidAttemptGuard, upstream task reconciliation, spend caps, artifact versioning or continuity dependencies.

## No fake completion
Never mark a task complete because code compiles. Completion requires its acceptance criteria and applicable golden scenarios.
