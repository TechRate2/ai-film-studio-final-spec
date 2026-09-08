# Research ROI and Creative Evidence Graph

## ResearchROIController
Research is a decision, not a default loop. Estimate expected value from:
- material uncertainty;
- consequence of being wrong;
- probability useful evidence exists;
- expected impact on creative/model/provider decision;
- freshness requirement;
- query/source cost and latency.

The controller outputs `SKIP | USE_CACHE | SEARCH | PROBE | BLOCK_FOR_EVIDENCE`, a budget and stop condition. Numeric scoring is optional; reasoning factors and provenance are mandatory.

## Stop rule
Stop when another search is unlikely to change the decision materially. Endless browsing is a defect.

## CreativeEvidenceGraph
Store reusable evidence-backed relationships such as:
`audience/context → mechanism → creative choice → observed/expected outcome`.

Example relationships can link a hook mechanism, camera treatment, proof pattern or pacing decision to evidence IDs, niche/platform scope, confidence, freshness and observed outcome. The graph is retrieval memory, not universal truth.

## Evidence separation
- factual claims require evidence suitable for factual truth;
- creative patterns may use broader observed examples but remain scoped/hypothetical;
- model/provider capability requires official evidence or controlled probes whenever practical.

## Decision provenance
Important Director choices should link to the evidence/skill/taste/profile inputs that materially influenced them. Advanced UI may expose this rationale without dumping raw search results.

## Decision and evidence graph integrity
Questions and claims have stable IDs. Graph edges link existing nodes/evidence and record scope, confidence and whether the outcome is EXPECTED or OBSERVED. A reused source cannot self-corroborate through a graph cycle. EvidencePack claims each link to ResearchEvidence IDs and freshness; a bare confident sentence is not evidence. Cache keys include source/profile/version, provider/endpoint where relevant, scenario, locale and policy scope. Retrieval never crosses private projects without authorization. Source disagreement and stale entries remain inspectable but excluded from confident capability resolution. A cinematography observation distinguishes measured cut times from estimated lens feel and uncertainty; no guessed focal length becomes an empirical constraint.
