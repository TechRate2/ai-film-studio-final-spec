# TASK-006 — Generalist Director Runtime

## Goal
Implement one visible Generalist Director with typed tools, persisted/resumable runs and a clear boundary from deterministic production execution.

## Read first
- `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `governance/CONTEXT_LOADING_RULES.md`

## Acceptance criteria
- one Director, no niche-hardcoded agent branches;
- typed Tool Registry;
- persisted resumable run/checkpoint state;
- scoped context retrieval;
- Director cannot bypass PaidAttemptGuard or directly own provider lifecycle;
- deterministic production jobs remain explicit.

Follow `AGENTS.md` completion/report rules.
