# TASK-011 — Adaptive Research Controller

## Goal
Implement evidence-first research need detection with ROI/budget/stop logic instead of unconditional browsing.

## Read first
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/33_RESEARCH_INGESTION_KNOWLEDGE_PLAYBOOK.md`
- `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md`
- `schemas/research_plan.schema.json`
- `schemas/research_roi_decision.schema.json`

## Acceptance criteria
- factual/current/model/provider/creative/reference research routes are distinct decisions;
- controller outputs SKIP/USE_CACHE/SEARCH/PROBE/BLOCK_FOR_EVIDENCE;
- query/source/cost/latency budget and explicit stop condition;
- fresh high-confidence cached evidence can avoid new research;
- material uncertainty can force research/probe before expensive generation;
- endless search loop impossible under configured budget;
- decision and rationale persisted.

## Binding execution and verification packet

Dependencies: TASK-010. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/33_RESEARCH_INGESTION_KNOWLEDGE_PLAYBOOK.md`
- `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md`
- `schemas/research_plan.schema.json`
- `schemas/research_roi_decision.schema.json`

Requirements: R-004, R-044, R-073, R-078.
Golden coverage: GS04, GS06, GS25.

- [ ] Persist finite research budgets and consumed counters across restart, critic re-entry and nested searches; use a valid cache without another query.
- [ ] Force current/version changes, contradictory sources and budget exhaustion; paid probe proposals cannot bypass authorization and unknown facts cannot become supported.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
