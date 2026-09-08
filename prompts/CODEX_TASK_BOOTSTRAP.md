# Codex Task Bootstrap

Work on exactly one canonical task.

1. Read `AGENTS.md`, `spec/00_SPEC_LOCK.md`, `governance/AI_CODING_PROTOCOL.md`.
2. Read the assigned `tasks/TASK_...md` and only its linked specs/schemas/playbooks.
3. Inspect the implementation repository and report reality vs acceptance criteria before edits.
4. Propose the smallest vertical implementation plan.
5. Implement real production behavior; test doubles only in tests.
6. Run task tests + affected golden scenarios.
7. Audit for SPEC_LOCK/provider/cost/continuity/versioning violations.
8. Update traceability with exact implementation/test refs.
9. Do not mark complete if any acceptance criterion fails.

If a canonical change appears necessary, stop that change and produce an ADR/spec-change proposal instead of silently redesigning.
