# TASK-012 — EvidencePack, Freshness and CreativeEvidenceGraph

## Goal
Convert research into ranked, scoped, provenance-carrying reusable evidence rather than raw search dumps.

## Read first
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/24_EVIDENCE_AND_VERIFICATION_POLICY.md`
- `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md`
- `schemas/evidence_pack.schema.json`
- `schemas/research_evidence.schema.json`
- `schemas/creative_evidence_graph.schema.json`

## Acceptance criteria
- source hierarchy/confidence/freshness/scope stored;
- contradictory evidence preserved and surfaced;
- model/provider claims carry provider/version/date scope;
- creative patterns link mechanism/choice/outcome to evidence IDs;
- raw search results are not passed directly as Director truth;
- cache invalidation/expiry supported;
- advanced provenance can explain material decisions.
