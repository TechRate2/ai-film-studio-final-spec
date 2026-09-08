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

## Binding execution and verification packet

Dependencies: TASK-005. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md`
- `spec/29_RUNTIME_ORCHESTRATION.md`
- `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md`
- `schemas/decision_record.schema.json`
- `schemas/active_context_pack.schema.json`
- `schemas/event_envelope.schema.json`

Requirements: R-001, R-002, R-026, R-048, R-077, R-078, R-086.
Golden coverage: GS01, GS03, GS04, GS10, GS15, GS18, GS23, GS25.

- [ ] Restart a run with no chat transcript and reconstruct task/tool/context pins and spent loop budgets from durable records.
- [ ] Reject a billable tool request without domain authorization; unknown tool schema and injected reference instructions cannot grant execution rights. Test swapped LLM adapter without Director changes.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
