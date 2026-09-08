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
