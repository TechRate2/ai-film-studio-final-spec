# Final Canonical Specification Audit — V4.3

Audited base: `main@cf61168bfa8ce8303963f14fd9b45377d8690bfb`. Review branch: `audit/canonical-contract-hardening`. This report assesses the proposed hardened tree; main adoption is determined by Git history, not by the version label in this document. No application was built and no paid API credits were used.

## A. Repository inventory

All **242 original tracked files** were read in full before architectural edits. Truncated display batches were re-read in smaller groups. The pre-edit inventory contains file sizes and SHA-256 identities. Final tree: **252 files**, **204 changed/added paths** (194 modified, 10 added). No original file was deleted. No runtime service, provider implementation or app mock was added.

| Root/group | Base files | Final files |
|---|---:|---:|
| (root) | 6 | 6 |
| .github | 3 | 3 |
| docs | 1 | 2 |
| evals | 2 | 3 |
| evidence | 5 | 8 |
| examples | 4 | 4 |
| governance | 6 | 10 |
| knowledge | 10 | 10 |
| phases | 7 | 7 |
| profiles | 14 | 14 |
| prompts | 7 | 7 |
| schemas | 42 | 43 |
| skills | 39 | 39 |
| spec | 47 | 47 |
| tasks | 46 | 46 |
| traceability | 3 | 3 |

The canonical counts are 47 specs, 43 numbered tasks, 43 schemas (42 existing plus shared values), 28 Golden scenarios, 88 requirements and 7 phase gates. Profiles contain 10 YAML records and four README files; skills contain 38 cards and one README. `evidence/AUDIT_INVENTORY.csv` records every path and classification; `evidence/AUDIT_ISSUE_MATRIX.csv` records the pre-edit issue matrix and resolution. The second pass scanned every final file, rechecked contract references and compared modified logical groups for semantics; it does not claim a second independent reviewer or live application execution. Self-referential audit hashes use the Git tree anchor.

## B. Critical and high findings

The original closure claim was not justified. Three CRITICAL and eleven HIGH issue groups were found, plus two MEDIUM groups. All contract fixes preserve spec/00_SPEC_LOCK.md, which is byte-for-byte unchanged.

| ID | Severity | Finding | Minimal resolution |
|---|---|---|---|
| A01 | CRITICAL | Competing job vocabularies and no transition guards | One durable state family; transition/event/UI projection contract |
| A02 | CRITICAL | No durable authorization linkage, reservation or candidate race semantics | Typed links/certainty; atomic reserve/fence/reconcile and bounded liability |
| A03 | HIGH | Empty provenance and unversioned inputs cannot prove currency | Typed conditional origin provenance and versioned dependency selectors |
| A04 | HIGH | Empty tracks/export allow incompatible execution | Integer rational timebase, typed tracks, validation and QA manifest |
| A05 | HIGH | Cross-module objects mostly untyped | Shared typed records and semantic invariants, explicit creative extension fields |
| A06 | HIGH | MEASURED claims without exact scope/sample evidence | Quarantine unsupported claims; claim-scoped evidence metadata |
| A07 | CRITICAL | Billable image path precedes guard and vertical slice asks QA before QA task | Executable dependency order; safety for every paid modality |
| A08 | HIGH | Audit-only goal contradicts implement/migrate boilerplate | Read-only implementation audit packet with inspectable evidence |
| A09 | HIGH | Tasks missing schema/GS links; orphan tasks; prose cannot prove completion | Per-task read/dependency/negative-test matrix and complete traceability |
| A10 | HIGH | Sparse definitions, repeated genre summaries, weak decision and contraindication logic | Selective skill metadata and practical decision/tradeoff/failure instructions |
| A11 | HIGH | No temporal knowledge source edges, snapshot race or currency rebase semantics | Causal fact observations, scoped version pins, atomic acceptance/retcon rules |
| A12 | HIGH | Budgets not structurally finite; untrusted evidence/tool injection unspecified | Bounded counters across resume, claim provenance, trust and asset fetch boundary |
| A13 | HIGH | Counts/parse pass invalid contracts; closure report overclaims readiness | Structured validator, negative fixtures, reference/coverage/version assertions |
| A14 | MEDIUM | Linear diagram can force stages; examples imply equal duration and combined mode | Optional prerequisite graph, explicit hypothetical durations and exact enum values |
| A15 | MEDIUM | No signal lineage, opt-out or exposure attribution; correlation may bias canon | Versioned scoped learning signals with confounding/forget controls |
| A16 | HIGH | Dialogue text→text only ignores existing speech/lipsync dependencies | Revision uses actual modality dependency rather than unconditional shortcut |

A06 remains empirical at runtime: missing measured evidence is represented as UNKNOWN/non-routable, not fabricated capability. The architecture defect was unjustified promotion; that is corrected. Full detail, authority and dependencies are in the issue matrix.

## C. Exact changes

Stable task IDs and the single canonical tree are retained. SPEC_VERSION is 4.3 because schema hardening affects wire compatibility. ADR-0001 records the owner-authorized Class B correction and migration considerations. The following is the complete changed-path list, including audit evidence; unchanged paths remain in the inventory.

| Exact path | Change | Reason |
|---|---|---|
| `.github/workflows/spec-governance.yml` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `AGENTS.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `MANIFEST.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `README.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `SPEC_VERSION` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `docs/adr/ADR_0001_CANONICAL_CONTRACT_HARDENING.md` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `evals/BENCHMARK_RUBRIC.md` | MODIFIED | Falsifiable scenario fixtures, anchored benchmark rubric and structural counterexamples |
| `evals/GOLDEN_SCENARIOS.md` | MODIFIED | Falsifiable scenario fixtures, anchored benchmark rubric and structural counterexamples |
| `evals/contract_fixtures.json` | ADDED | Falsifiable scenario fixtures, anchored benchmark rubric and structural counterexamples |
| `evidence/AUDIT_INVENTORY.csv` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `evidence/AUDIT_ISSUE_MATRIX.csv` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `evidence/COMPLETENESS_AUDIT_V4_2.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `evidence/FINAL_AUDIT_REPORT.md` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `evidence/PUBLIC_SOURCE_MAP.md` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `evidence/SEEDANCE_KNOWLEDGE_STATUS.md` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `examples/GS03_XIANXIA_60S_WALKTHROUGH.md` | MODIFIED | Clarify illustrative timing and exact enum values; no fixed generation split |
| `examples/GS04_SATURN_120S_WALKTHROUGH.md` | MODIFIED | Clarify illustrative timing and exact enum values; no fixed generation split |
| `governance/CANONICAL_COMPLETENESS_CHECKLIST.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `governance/contract_index.json` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `governance/requirements.txt` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `governance/test_validate_spec.py` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `governance/validate_spec.py` | ADDED | Canonical governance/version/manifest, audit evidence and drift validation |
| `knowledge/filmcraft/ACTION_SCENES.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/COMPOSITION_AND_LENS_LANGUAGE.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/DIALOGUE_SCENES.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/DIRECTING_PRINCIPLES.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/EDITING_GRAMMAR.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/LIGHTING_CONTINUITY.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/OPENING_BODY_ENDING.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/SCENE_BLOCKING.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/SERIES_STORY_LOGIC.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `knowledge/filmcraft/SOUND_DESIGN.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `phases/PHASE_0_CONTRACT_AND_REALITY.md` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |
| `phases/PHASE_2_SEEDANCE_VERTICAL_SLICE.md` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |
| `phases/PHASE_6_BETA_RELEASE.md` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |
| `profiles/images/IMAGE_MODEL_PROFILE_TEMPLATE.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/README.md` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/kling_v3_o3.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/seedance_2_0.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/seedance_2_5.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/veo_3_1.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/vidu_q3.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/wan_2_2_family.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/models/wan_2_6.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/providers/PROVIDER_PROFILE_TEMPLATE.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `profiles/voices/VOICE_MODEL_PROFILE_TEMPLATE.yaml` | MODIFIED | Scoped evidence metadata; no unsupported MEASURED or production routing claims |
| `schemas/active_context_pack.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/artifact.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/artifact_dependency.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/asset_ingestion_record.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/character.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/common.schema.json` | ADDED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/composition_timeline.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/content_safety_decision.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/continuity_baton.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/cost_estimate.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/creative_evidence_graph.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/creative_strategy.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/decision_record.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/degrade_decision.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/dialogue_scene.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/effective_capability.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/episode_snapshot.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/event_envelope.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/evidence_pack.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/final_master.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/generation_plan.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/job.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/keyframe_generation_pack.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/model_profile.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/paid_attempt.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/production_strategy.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/project_canon.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/project_intent.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/provider_profile.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/qa_report.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/reference_binding.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/relationship_edge.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/research_evidence.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/research_plan.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/research_roi_decision.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/revision_request.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/scope_decision.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/shot_version.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/spend_authorization.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/style_dna.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/universal_video_spec.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/user_taste_profile.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `schemas/voice_profile.schema.json` | MODIFIED | Typed cross-module records, shared refs, immutable version/provenance and negative fixtures |
| `skills/README.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/cinematography/action_readability.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/cinematography/camera_language.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/cinematography/dialogue_scene.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/cinematography/product.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/cinematography/vfx_fantasy.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/advertising.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/beauty.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/comedy.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/documentary_explainer.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/drama.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/education.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/fashion.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/food.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/hook_retention.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/horror.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/music_visual.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/news_current.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/product_demo.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/real_estate.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/romance.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/sci_fi.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/storytelling.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/ugc.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/creative/xianxia_wuxia.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/editorial/edit_rhythm.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/editorial/j_l_cuts_audio_bridges.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/performance/blocking.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/performance/multi_character.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/platform/ads.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/platform/reels.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/platform/tiktok.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/platform/youtube_long_form.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/platform/youtube_shorts.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/production/continuity.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/production/cost_first_pass.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/production/generation_length_optimization.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/production/selective_keyframe_policy.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `skills/reference/reference_roles.md` | MODIFIED | Decision-specific retrieval, professional trade-offs, contraindications and generative feasibility |
| `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md` | MODIFIED | Optional prerequisite graph, explicit hypothetical durations and exact enum values |
| `spec/03_SCOPE_AND_CONTENT_INTELLIGENCE.md` | MODIFIED | Read and retained; no identified contract change necessary |
| `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md` | MODIFIED | Bounded counters across resume, claim provenance, trust and asset fetch boundary |
| `spec/05_CREATIVE_STORY_RETENTION.md` | MODIFIED | Selective skill metadata and practical decision/tradeoff/failure instructions |
| `spec/06_REFERENCE_INTELLIGENCE.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md` | MODIFIED | Causal fact observations, scoped version pins, atomic acceptance/retcon rules |
| `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md` | MODIFIED | Causal fact observations, scoped version pins, atomic acceptance/retcon rules |
| `spec/09_DIALOGUE_VOICE_LOCALIZATION.md` | MODIFIED | Revision uses actual modality dependency rather than unconditional shortcut |
| `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md` | MODIFIED | Causal fact observations, scoped version pins, atomic acceptance/retcon rules |
| `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `spec/14_UNIVERSAL_VIDEO_SPEC.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md` | MODIFIED | Quarantine unsupported claims; claim-scoped evidence metadata |
| `spec/17_SHOT_REVISION_VERSIONING.md` | MODIFIED | Revision uses actual modality dependency rather than unconditional shortcut |
| `spec/18_COST_SPEND_ATTEMPT_POLICY.md` | MODIFIED | Typed links/certainty; atomic reserve/fence/reconcile and bounded liability |
| `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md` | MODIFIED | Typed conditional origin provenance and versioned dependency selectors |
| `spec/22_OUTCOME_TASTE_RESEARCH_MEMORY.md` | MODIFIED | Versioned scoped learning signals with confounding/forget controls |
| `spec/23_SECURITY_PRIVACY_PROVENANCE.md` | MODIFIED | Bounded counters across resume, claim provenance, trust and asset fetch boundary |
| `spec/27_DOMAIN_DATA_MODEL.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `spec/28_API_AND_EVENT_CONTRACTS.md` | MODIFIED | One durable state family; transition/event/UI projection contract |
| `spec/29_RUNTIME_ORCHESTRATION.md` | MODIFIED | One durable state family; transition/event/UI projection contract |
| `spec/30_UI_STATE_MACHINE.md` | MODIFIED | One durable state family; transition/event/UI projection contract |
| `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md` | MODIFIED | Quarantine unsupported claims; claim-scoped evidence metadata |
| `spec/32_LONG_FORM_SERIES_PLAYBOOK.md` | MODIFIED | Causal fact observations, scoped version pins, atomic acceptance/retcon rules |
| `spec/40_RESEARCH_ROI_AND_CREATIVE_EVIDENCE_GRAPH.md` | MODIFIED | Bounded counters across resume, claim provenance, trust and asset fetch boundary |
| `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md` | MODIFIED | Integer rational timebase, typed tracks, validation and QA manifest |
| `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md` | MODIFIED | Typed links/certainty; atomic reserve/fence/reconcile and bounded liability |
| `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md` | MODIFIED | Optional prerequisite graph, explicit hypothetical durations and exact enum values |
| `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md` | MODIFIED | Shared typed records and semantic invariants, explicit creative extension fields |
| `tasks/00_IMPLEMENTATION_ORDER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_001_REPOSITORY_REALITY_AUDIT.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_002_CANONICAL_SPEC_EMBEDDING_AND_TRACEABILITY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_003_PROJECT_DOMAIN_PERSISTENCE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_004_ARTIFACT_VERSIONING_AND_CURRENCY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_005_CHAT_FIRST_WORKSPACE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_006_GENERALIST_DIRECTOR_RUNTIME.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_007_SCOPE_AND_CONTENT_INTELLIGENCE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_008_REFERENCE_ANALYZER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_009_ENTITY_GROUPING_AND_LOCKS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_010_DYNAMIC_SKILL_REGISTRY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_011_ADAPTIVE_RESEARCH_CONTROLLER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_012_EVIDENCEPACK_AND_FRESHNESS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_013_CREATIVE_STRATEGY_AND_RETENTION.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_014_STORY_HIERARCHY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_015_CHARACTER_RELATIONSHIP_KNOWLEDGE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_016_PROJECT_CANON_AND_EPISODE_MEMORY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_017_DIALOGUE_VOICE_LOCALIZATION.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_018_PERFORMANCE_CAMERA_AUDIO_EDITORIAL.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_019_PRODUCTION_STRATEGY_ENGINE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_020_SCENE_COMPLEXITY_PLANNER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_021_CONTINUITY_DEPENDENCY_SCHEDULER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_022_CONTINUITY_BATON.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_023_SELECTIVE_KEYFRAME_CONTROLLER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_024_EXTERNAL_KEYFRAME_WORKFLOW.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_025_UNIVERSALVIDEOSPEC.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_026_MODEL_PROFILES_AND_CAPABILITY_RESOLVER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_027_MODEL_PROMPT_COMPILERS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_028_PROVIDER_PROFILES_AND_ADAPTERS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_029_DEGRADE_PLANNER.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_030_SEEDANCE_2_0_VERTICAL_SLICE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_031_PROBE_AND_BENCHMARK_HARNESS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_032_DURABLE_JOBS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_033_COST_AND_PAID_ATTEMPT_GUARD.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_034_MEDIA_QA_AND_DIAGNOSIS.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_035_CONTEXTUAL_SHOT_REVISION.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_036_SHOT_VERSION_GRAPH_AND_CONTINUITY_SANDWICH.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_037_VOICE_SUBTITLE_MUSIC_ASSEMBLY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_038_TASTE_OUTCOME_RESEARCH_MEMORY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_039_GOLDEN_SCENARIO_AUTOMATION.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_040_SERIES_CONTINUATION_ACCEPTANCE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_041_UI_REVIEW_SURFACES.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_042_SECURITY_BACKUP_OBSERVABILITY.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `tasks/TASK_043_BETA_RELEASE_GATE.md` | MODIFIED | Explicit safe dependency/read/schema/requirement/Golden packet and falsifiable acceptance |
| `traceability/PHASE_GATE_MATRIX.csv` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |
| `traceability/README.md` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |
| `traceability/REQUIREMENTS_TRACEABILITY.csv` | MODIFIED | Align phase order, full task/schema/Golden coverage and evidence-only completion |

## D. Architecture verification

VERIFIED below means verified in the specification/schema/task/evaluation contract. It is not proof of live product or provider performance. Every area has implementation acceptance obligations and Golden coverage in the traceability/index.

| Area | Authority/contract | Verified behavior |
|---|---|---|
| Generalist Director | `spec/02_GENERALIST_DIRECTOR_ARCHITECTURE.md` | Single visible brain, neutral typed tools and bounded durable runs |
| Research-first | `spec/04_ADAPTIVE_RESEARCH_INTELLIGENCE.md` | Claim-linked evidence, freshness, contradictions, shared finite budgets and stop states |
| Provider-neutral | `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md` | Director ports → universal intent → compiler → guarded adapter |
| Adaptive scope | `spec/03_SCOPE_AND_CONTENT_INTELLIGENCE.md` | SHORT/LONG_SINGLE/SERIES by complexity/continuity, not seconds alone |
| StyleDNA | `spec/39_STYLE_DNA_AND_GRAMMAR_LAYERS.md` | Mechanisms, transferable/do-not-copy traits and hard-rule precedence |
| Filmcraft skills | `skills/README.md` | 38 selective cards and 10 deeper decision/trade-off knowledge documents |
| Reference Intelligence | `spec/06_REFERENCE_INTELLIGENCE.md` | Same-entity grouping, role isolation, locks/lifetimes and pinned targets |
| Project Canon | `spec/07_PROJECT_CANON_AND_SERIES_MEMORY.md` | Temporal facts, immutable versions and atomic snapshot/retcon commits |
| Character Knowledge | `spec/08_CHARACTER_RELATIONSHIP_KNOWLEDGE_STATE.md` | Acquisition paths, belief/knowledge distinction, story-position access and alias ambiguity |
| ActiveContextPack | `spec/32_LONG_FORM_SERIES_PLAYBOOK.md` | Small relevant context with version pins, knowledge isolation and mandatory-lock budget checks |
| Adaptive segmentation | `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md` | Shots/panels/segments distinct; continuous/segmented/continuation with reasons |
| Continuity DAG | `spec/12_CONTINUITY_DEPENDENCY_SCHEDULER.md` | Accepted CURRENT parents, acyclic owned edges, claim/submit recheck and fencing |
| Continuity Baton | `schemas/continuity_baton.schema.json` | Observed state with body/weather/prop/audio and accepted evidence; identity remains canonical |
| Selective keyframes | `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md` | Five routes; NONE has no fake pack; external failure never buys internal fallback |
| UniversalVideoSpec | `schemas/universal_video_spec.schema.json` | Typed global/locks/time/performance/camera/audio/initial/in/out/success/risk sections |
| ModelProfile | `schemas/model_profile.schema.json` | Exact version, claim evidence, unknowns and sample-scoped promotion |
| ProviderProfile | `schemas/provider_profile.schema.json` | Separate exposure, prices, limits, timeout/idempotency and evidence |
| EffectiveCapability | `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md` | Five-layer intersection with denial/unknown precedence and explicit revalidated degrade |
| SpendAuthorization | `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md` | User action/plan/hash/currency/candidate slots/caps/expiry and atomic reservations |
| PaidAttemptGuard | `schemas/paid_attempt.schema.json` | Logical attempt/authorization/candidate/request snapshot/certainty/cost links |
| No blind paid retry | `spec/18_COST_SPEND_ATTEMPT_POLICY.md` | Auto regeneration OFF; ambiguous submission reconciles; produced output cannot silently fallback |
| Contextual revision | `spec/17_SHOT_REVISION_VERSIONING.md` | Semantic change/preserve diff using actual modality dependencies and incremental authorization |
| Continuity Sandwich | `spec/17_SHOT_REVISION_VERSIONING.md` | All incoming/outgoing pinned requirements, including fan-out |
| ShotVersionGraph | `schemas/shot_version.schema.json` | Immutable versions; accepted pointer and source-pin re-evaluation |
| Artifact dependency currency | `spec/21_JOBS_ARTIFACT_DEPENDENCY_GRAPH.md` | CURRENT/STALE/MISSING/BLOCKED separate from success/acceptance; selective propagation |
| Voice/localization | `spec/09_DIALOGUE_VOICE_LOCALIZATION.md` | Speaker identity, language variants, pronunciation and separable/baked audio dependencies |
| CompositionTimeline | `schemas/composition_timeline.schema.json` | Integer tick/rational FPS tracks, source versions, trims/holds/speed/J-L audio/cues/export |
| FinalMaster | `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md` | Required evidence-bearing QA, source recheck, checksum and deterministic repair derivatives |
| VN/EN UI | `spec/20_CHAT_FIRST_WORKSPACE_UX.md` | Locale separate from output/canon; durable state projections and progressive controls |
| Rights/security | `spec/23_SECURITY_PRIVACY_PROVENANCE.md` | Tenant/media isolation, untrusted ingestion, callbacks, consent/rights, deletion/restore |
| Long-form/series | `spec/32_LONG_FORM_SERIES_PLAYBOOK.md` | 10+ registry, active subset, temporal knowledge and atomic episode continuation |
| Taste/outcome learning | `spec/22_OUTCOME_TASTE_RESEARCH_MEMORY.md` | Scoped attributed signals, uncertainty, correction/disable/deletion and no overfit |

## E. Schema integrity

All 43 schemas pass draft 2020-12 metaschema validation. Local references and JSON pointers resolve offline. Typed records reject unintended extra fields; creative content remains descriptive where exact physical semantics would be false precision. The explicit recursive JSON map is confined to provider-owned request parameters, not Director intent. Critical job/certainty/currency/scope/content/keyframe/lock/lifetime/no-retry values are compared against machine-readable canonical spec sections.

41 positive/negative contract fixtures cover job vocabulary, paid links/certainty, reference isolation, empty UniversalVideoSpec sections, timeline structure/rational speed, imported versus generated provenance, no-paid QA and NONE keyframes. Cross-record ownership, temporal knowledge, atomic transactions and timeline arithmetic require domain tests: GS05/GS19/GS27 specify these and do not pretend JSON Schema alone can enforce them.

## F. Task readiness

Every numbered task has explicit prerequisite, exact canonical/schema reading, linked requirements/Goldens, targeted acceptance and evidence obligations. TASK-001 is report-only. TASK-024 follows provider ports AND jobs/guard. TASK-034 preflight/QA precedes real TASK-030 smoke. Task IDs are stable, not naive numeric execution order. A later phase gate cannot be claimed from an earlier partial demonstration; deterministic tests are owned immediately by each task, not postponed to TASK-039.

| Task | Prerequisite | Requirement count | Golden coverage | Packet verified |
|---|---|---:|---|---|
| TASK-001 | NONE | 1 | GS26 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-002 | TASK-001 | 1 | GS26 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-003 | TASK-002 | 1 | GS26, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-004 | TASK-003 | 2 | GS09, GS11, GS21 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-005 | TASK-004 | 3 | GS08, GS09, GS11 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-006 | TASK-005 | 7 | GS01, GS03, GS04, GS10, GS15, GS18, GS23, GS25 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-007 | TASK-006 | 2 | GS01, GS05, GS12 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-008 | TASK-007 | 6 | GS02, GS03, GS08, GS12, GS18, GS23 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-009 | TASK-008 | 1 | GS02, GS03 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-010 | TASK-009 | 1 | GS02, GS07, GS13 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-011 | TASK-010 | 4 | GS04, GS06, GS25 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-012 | TASK-011 | 4 | GS01, GS02, GS04, GS06, GS12, GS25 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-013 | TASK-012 | 4 | GS01, GS02, GS03, GS04, GS25 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-014 | TASK-013 | 1 | GS03, GS05 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-015 | TASK-014 | 3 | GS05, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-016 | TASK-015 | 5 | GS05, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-017 | TASK-016 | 1 | GS07, GS11, GS17 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-018 | TASK-017 | 2 | GS02, GS03, GS07, GS13 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-019 | TASK-018 | 1 | GS04, GS14 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-020 | TASK-019 | 2 | GS03, GS04, GS13, GS14 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-021 | TASK-020 | 1 | GS03, GS09 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-022 | TASK-021 | 2 | GS03, GS05 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-023 | TASK-022 | 1 | GS14, GS16 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-024 | TASK-033 | 5 | GS08, GS14, GS16, GS17, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-025 | TASK-023 | 1 | GS03, GS04 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-026 | TASK-025 | 3 | GS15, GS20 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-027 | TASK-026 | 2 | GS03 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-028 | TASK-027 | 5 | GS15, GS16, GS17, GS24, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-029 | TASK-028 | 1 | GS15, GS20 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-030 | TASK-034 | 3 | GS01, GS03, GS10 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-031 | TASK-037 | 4 | GS03, GS04, GS14, GS15 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-032 | TASK-029 | 7 | GS03, GS10, GS22, GS24, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-033 | TASK-032 | 11 | GS01, GS04, GS09, GS10, GS16, GS17, GS22, GS24, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-034 | TASK-024 | 2 | GS09, GS10, GS19, GS24 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-035 | TASK-030 | 1 | GS09, GS21 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-036 | TASK-035 | 3 | GS09, GS21 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-037 | TASK-036 | 6 | GS16, GS17, GS19, GS21, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-038 | TASK-031 | 3 | GS01, GS09, GS28 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-039 | TASK-038 | 2 | GS01, GS05, GS08, GS09, GS10, GS15, GS26 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-040 | TASK-039 | 2 | GS05, GS27 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-041 | TASK-040 | 3 | GS08, GS09, GS11 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-042 | TASK-041 | 8 | GS10, GS18, GS23, GS24, GS28 | Reads + targeted positive/negative acceptance + evidence gate |
| TASK-043 | TASK-042 | 2 | GS01, GS03, GS25 | Reads + targeted positive/negative acceptance + evidence gate |

No orphan tasks, schemas or Golden scenarios remain. All 88 implementation requirements remain NOT_STARTED: specification editing is not application implementation. The validator rejects IMPLEMENTED with missing evidence; it cannot establish that a future agent has honestly executed an external test merely from a string path. TASK-043 requires inspection of the actual evidence and real applicable phase gates.

## G. CI and governance verification

Commands run locally with isolated validation dependencies (no provider credentials):

```text
python governance/validate_spec.py --json
python -m unittest discover -s governance -p 'test_*.py' -v
git diff --check
```

Validator: **PASS**, 3040 checks at the final contract pass. The following counts describe assertions, not independent end-to-end application tests.

| Validation family | Checks |
|---|---:|
| required_files | 244 |
| version | 3 |
| spec_numbering | 1 |
| schema_titles | 1 |
| metaschemas | 43 |
| typed_objects | 395 |
| local_refs | 240 |
| invariants | 12 |
| critical_required | 5 |
| traceability | 706 |
| goldens | 2 |
| tasks | 485 |
| task_graph | 47 |
| coverage | 3 |
| phases | 14 |
| profiles | 10 |
| skills | 77 |
| internal_paths | 698 |
| counts | 13 |
| contract_fixtures | 41 |

**13 governance unit tests passed**, comprising the valid-tree baseline and 12 deliberate mutations: missing required file, job vocabulary drift, paid certainty drift, missing authorization, auto-retry enabled, open timeline, broken local ref, missing task reading, unsafe paid order, false IMPLEMENTED, duplicate requirement and unsupported MEASURED promotion. Ordinary CI installs validator dependencies then runs these offline checks. It contains no paid provider test. Hosted GitHub Actions status is separate from local execution and must be read for the pushed commit before claiming hosted CI passed.

A final full-tree pass also inspected schema/property/reference closure, all profile YAML, task/phase order, old state/enum spellings, illustrative duration examples, historical audit/version labels, traceability coverage and SPEC_LOCK immutability. No foundational unresolved contract contradiction was identified after these corrections. This is a bounded evidence-based audit, not a mathematical proof that all possible future bugs are impossible.

## H. Remaining empirical unknowns

| Unknown | Contract handling / evidence required |
|---|---|
| Seedance 2.0 practical behavior on the chosen route | Public experiment report retained as REPO_REPORTED; exact account/endpoint and controlled samples required |
| Seedance 2.5 behavior/exposure | Separate UNKNOWN/PARTIAL profile; no inheritance from 2.0 |
| Wan/Kling/Vidu/Veo exact versions and routes | Family/historical profiles remain non-routable; exact model/provider documentation and probes required |
| Current provider/image/voice prices and billing | Verified price rules, currency, expiry and bounded liability required before spend |
| Account entitlement, region, callback/idempotency/cancel support | Resolve exact account/provider evidence; UNKNOWN cannot authorize blind submit |
| Practical reference ceilings, native audio, identity and duration reliability | Scenario-scoped sample ledger, failures, confidence and source versions; no marketing defaults |
| First-pass acceptance and cost per accepted second | Measure accepted/failed billed samples; unknown/zero denominator remains null |
| Audience retention and outcome learning | Scope/exposure-aware analytics with attribution uncertainty; no virality guarantee |
| Infrastructure scale and real restore/recovery | Implementation load/failure tests and commercial gates, not invented sizing guarantees |

The directly re-inspected public Seedance profile is pinned by returned blob SHA in evidence/SEEDANCE_KNOWLEDGE_STATUS.md. Other historical source maps are explicitly qualified and were not relabeled as freshly verified. These unknowns do not block TASK-001/spec embedding, but do block unqualified live routing and applicable real-provider release gates.

## I. Final verdict

**READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS**

Applies to this hardened specification revision. Begin with TASK-001 against the actual implementation repository, follow the explicit safe order, and keep real provider/paid/release gates blocked until their evidence exists. This verdict does not claim that the application is implemented, live model quality is measured, or unmerged changes are already canonical on main.
