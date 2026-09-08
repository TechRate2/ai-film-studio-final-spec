# TASK-012 — EvidencePack and Freshness

## Goal
Implement source ranking, EvidencePack building, conflict handling and reusable freshness-aware research memory.

## Read first
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/24_EVIDENCE_AND_VERIFICATION_POLICY.md`
- `spec/33_RESEARCH_INGESTION_KNOWLEDGE_PLAYBOOK.md`
- `schemas/evidence_pack.schema.json`

## Acceptance criteria
- raw research is distilled;
- provenance/confidence/freshness/scope stored;
- conflicting findings remain visible;
- stale model/provider evidence rechecked;
- cached knowledge keyed by relevant model/provider/scenario scope.
