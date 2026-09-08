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

## Binding execution and verification packet

Dependencies: TASK-011. Stable IDs follow `tasks/00_IMPLEMENTATION_ORDER.md`, not numeric order.

Additional mandatory reading (including transitive local schema refs):
- `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md`
- `spec/24_EVIDENCE_AND_VERIFICATION_POLICY.md`
- `spec/33_RESEARCH_INGESTION_KNOWLEDGE_PLAYBOOK.md`
- `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md`
- `schemas/evidence_pack.schema.json`
- `schemas/research_evidence.schema.json`
- `schemas/creative_evidence_graph.schema.json`

Requirements: R-004, R-032, R-045, R-062.
Golden coverage: GS01, GS02, GS04, GS06, GS12, GS25.

- [ ] Link each distilled claim to source/version/scope/freshness and retain contradictions; evidence graph edges reference existing IDs.
- [ ] Reject confident unsupported facts and duplicate-source self-corroboration; expired private evidence does not enter another project or capability truth.
- [ ] For each criterion, record exact implementation/report path, test/assertion, result and applicable Golden subsection. Missing evidence is PARTIAL/BLOCKED, never DONE. Earlier tasks own their deterministic tests immediately; later integration results remain explicitly pending until their gate. No paid provider call is part of ordinary CI.
