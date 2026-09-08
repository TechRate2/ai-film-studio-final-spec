# TASK-006 — Generalist Director Runtime

## Goal
Implement one visible Generalist Director with typed tools, persisted/resumable/compactable runs and a clear boundary from deterministic production execution.

## Read first
- `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/27_DOMAIN_DATA_MODEL.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `governance/CONTEXT_LOADING_RULES.md`

## Required boundary from day one
The Director depends on provider-neutral ports/tool contracts such as `LLMProviderPort`, research/search tools and typed domain services. A concrete OpenAI/Claude/Gemini SDK must never become the Director's architecture. Early implementation may have one adapter, but brain owns no vendor transport or credentials.

## Acceptance criteria
- one Director, no niche-hardcoded agent branches;
- typed Tool Registry and provider-neutral LLM port;
- persisted resumable run/checkpoint state;
- session compaction produces durable structured refs/source versions + concise summary;
- a fresh process/model session resumes without hidden memory/full transcript dependency;
- scoped context retrieval;
- research/critic/planning loops have explicit budget/stop state and cannot spin indefinitely;
- Director cannot bypass PaidAttemptGuard or directly own provider lifecycle;
- deterministic production jobs remain explicit;
- swapping LLM adapter requires no rewrite of story/continuity/production reasoning;
- test proves concrete vendor client is outside Director domain module.

Follow `AGENTS.md` completion/report rules.
