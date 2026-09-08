# TASK-011 — Adaptive Research Controller

## Goal
Implement research-need detection, ResearchROI/budget, routing and stop conditions.

## Read first
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/33_RESEARCH_INGESTION_KNOWLEDGE_PLAYBOOK.md`
- `spec/24_EVIDENCE_AND_VERIFICATION_POLICY.md`

## Acceptance criteria
- current/factual/model uncertainty can trigger research;
- simple/high-confidence tasks may skip;
- budgets and confidence stop endless search;
- results are provenance-scoped and do not become raw prompt dumps;
- fresh cached evidence is reused.
