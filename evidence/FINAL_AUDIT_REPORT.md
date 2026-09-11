# Current audit closure — 4.4.2, 2026-09-11

## A. Inventory and inspection scope
Baseline main `1be7e30f0c4ca60a038b00ec03db13172603c380` has 265 inventoried files; all non-self-referential hashes matched before edits. The original full read and subsequent additions remain recorded below and in the inventory. This pass re-read the affected logical groups and current official sources; it does not claim a second fresh line-by-line read of every unchanged file. Final tree: **266 files**, with **22 modified and one added** relative to this baseline. Canonical counts remain **48 specs, 45 schemas, 46 numbered tasks, 8 phases, 33 Goldens and 96 requirements**. There are still 38 skill cards plus their README, ten filmcraft documents and fourteen profile files. No application code or paid samples were created.

## B. Findings
Pre-edit Q01–Q05 are preserved in `evidence/AUDIT_ISSUE_MATRIX.csv`. This pass found no additional CRITICAL issue, two HIGH and three MEDIUM issues. HIGH Q01: QAReport admitted ACCEPTABLE with MAJOR/FATAL or required FAIL/UNKNOWN; four baseline counterexamples reproduced it. HIGH Q03: prompt-implied API operation could disagree with requested mode/parameters without an explicit conformance acceptance case. MEDIUM Q02: negative route estimates were valid; Q04: total-route comparison needed a stronger acceptance case; Q05: older endpoint retrieval evidence was stale. All five are resolved at contract/evidence level. Runtime and media proof remain pending.

## C. Exact files changed
| File | Purpose |
|---|---|
| `MANIFEST.md` | Current canonical version. |
| `README.md` | Active version and current audit entry; preserve historical handoff version. |
| `SPEC_VERSION` | Version 4.4.2 and date. |
| `docs/adr/ADR_0004_QUALITY_AND_ROUTE_PREFLIGHT.md` | New Class B decision, alternatives and review consequences. |
| `spec/11_PRODUCTION_STRATEGY_AND_SCENE_COMPLEXITY.md` | Complete feasible route costs, uncertainty and bounded-liability handoff. |
| `spec/14_UNIVERSAL_VIDEO_SPEC.md` | Prompt/input-mode/parameter agreement before spending. |
| `spec/19_QUALITY_GATES_QA.md` | Acceptance veto, policy-owned required checks and calibrated review. |
| `spec/31_SEEDANCE_PRODUCTION_PLAYBOOK.md` | Provider-scoped conformance and independent output settings. |
| `schemas/production_strategy.schema.json` | Reject negative known route cost; retain null. |
| `schemas/qa_report.schema.json` | Reject contradictory ACCEPTABLE results. |
| `tasks/TASK_019_PRODUCTION_STRATEGY_ENGINE.md` | Falsifiable complete-cost and uncertainty acceptance. |
| `tasks/TASK_027_MODEL_PROMPT_COMPILERS.md` | Falsifiable operation/parameter conformance. |
| `tasks/TASK_034_MEDIA_QA_AND_DIAGNOSIS.md` | Schema and domain acceptance guards, policy completeness/calibration. |
| `evals/GOLDEN_SCENARIOS.md` | GS03/10/14 adversarial variants; current version heading. |
| `evals/contract_fixtures.json` | Thirteen additional positive/negative contract cases. |
| `governance/contract_index.json` | Version, ADR required path and exact fixture index. |
| `governance/test_validate_spec.py` | Two mutations prove removal of new guards is caught. |
| `profiles/models/seedance_2_5.yaml` | Refresh source-discovery note; do not promote runtime claims. |
| `evidence/SEEDANCE_KNOWLEDGE_STATUS.md` | Dated exact-provider endpoint and billing evidence. |
| `evidence/MARKET_FEASIBILITY_REVIEW.md` | Sixteen workflow groups, commercial source comparison, limits and economics. |
| `evidence/AUDIT_ISSUE_MATRIX.csv` | Q01–Q05 findings and resolutions. |
| `evidence/AUDIT_INVENTORY.csv` | Final path identities and affected-group review. |
| `evidence/FINAL_AUDIT_REPORT.md` | This closure; older evidence remains dated below. |

## D. Architecture verification
The sixteen-step current workflow crosswalk is in `evidence/MARKET_FEASIBILITY_REVIEW.md`; the detailed original architecture verification below remains the baseline. Generalist Director, research-first distillation/stop rules, provider neutrality, adaptive scope, StyleDNA, filmcraft retrieval, Reference Intelligence, Project Canon, Character Knowledge and ActiveContextPack remain intact. Adaptive segmentation, Continuity DAG/Baton and optional keyframes including NONE are retained. UniversalVideoSpec compilation is strengthened; independent ModelProfile/ProviderProfile and five-layer EffectiveCapability remain unchanged. SpendAuthorization, PaidAttemptGuard and no blind paid retry are unchanged. Contextual revision, Continuity Sandwich, ShotVersionGraph and artifact currency remain first-class. Voice/localization, CompositionTimeline, FinalMaster, VN/EN UI, rights/security, long-form/series and scoped taste/outcome learning retain their gates. No new visible Director or fixed niche pipeline was introduced. Spec lock is unchanged.

## E. Schema integrity
All 45 Draft 2020-12 schemas validate; 288 local-reference assertions resolve. The dangerous enum/state invariants remain consistent. 126 contract fixtures now include positive review/optional uncertainty and negative acceptance/negative-cost cases. Cross-module shapes stay in the same normative schema tree. Required QA check completeness and media truth require domain/runtime validation; JSON Schema alone cannot prove them.

## F. Task readiness
All 46 task records, prerequisites, required readings and requirement/Golden mappings pass structured validation. Only TASK-019/027/034 acceptance is tightened; their existing R-083, R-017/R-030 and R-020/R-057 mappings cover these cases, so no duplicate requirements or new task IDs were added. Task numbering is not execution order: paid-safety prerequisites still precede real media, and localization follows core release. Every task remains subject to criterion-complete evidence and PARTIAL/BLOCKED reporting. All 96 requirement statuses remain NOT_STARTED. A document cannot guarantee a future coding agent will obey; independent evidence gates must reject false completion.

## G. Exact validation
Offline governance: 4337 assertions PASS, including 45 metaschemas, 288 local-reference assertions, 126 fixtures and all task/phase/traceability/profile checks. All 33 governance tests PASS, including new negative mutations. Final diff whitespace and inventory hash/path checks PASS. Commands: `python governance/validate_spec.py --json`, `python -m unittest discover -s governance -p 'test_*.py' -q`, and `git diff --check`, with dependencies from `governance/requirements.txt`. GitHub checks and branch adoption are verified against the published commit separately; this report does not infer them from local success. No application, media playback, account trial or provider generation is certified.

## H. Remaining empirical unknowns
Current account entitlement/prices, deployed version, practical reference limits, native Vietnamese/dialogue performance, acceptance probability, continuation reliability, revision preservation and evaluator calibration remain unmeasured. Public endpoint documentation is now available for the intended provider, but no runtime claim was promoted. Commercial demos and documentation cannot establish this project's quality/cost superiority. These are scoped integration/release gates, not reasons for endless architecture expansion.

## I. Verdict
**READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS** for staged implementation. Commercial release and advertised model/language capabilities still require their actual acceptance evidence. No promise of universal perfection, autonomous success in all genres or guaranteed profitability is made.

---

> Historical 4.4.1 handoff hardening: `evidence/IMPLEMENTATION_HANDOFF_REVIEW.md` records that governance delta and its 265-file inventory. Earlier audit counts/results below remain historical evidence. Product scope is unchanged from 4.4.0.

> Subsequent 4.4.0 owner-approved scope extension: see `evidence/LOCALIZATION_DESIGN_EVIDENCE.md` for original-video subtitles/dubbing, the 262-file inventory, new release partition and current validation. The 4.3.x findings and counts below are historical core-audit evidence, not the current manifest. No application task is completed by either audit.

# Final Canonical Specification Audit — V4.3.1

Evidence refresh, 2026-09-09: the historical closure counts below describe the 252-file audited tree. A subsequent market/feasibility review adds `evidence/MARKET_FEASIBILITY_REVIEW.md`, bringing the current inventory to 253 files, and refreshes primary Seedance source pointers without changing normative contracts or runtime capability status. A23–A24 are two additional MEDIUM evidence findings; the 22 architecture findings and their severity totals below remain the historical audit result. See the new review for its narrower inspection method, representative market coverage and remaining empirical work. No competitive superiority or commercial release is certified.

Audited base: `main@cf61168bfa8ce8303963f14fd9b45377d8690bfb`. Initial hardening merged as PR #9. Follow-up baseline: `main@538e63e8829af2429fc9b0b6602a544260a2d23b`; review branch: `audit/astra-followup-closure`. This report assesses the proposed hardened tree; main adoption is determined by Git history, not by the version label in this document. No application was built and no paid API credits were used.

## A. Repository inventory

All **242 original tracked files** were read in full before architectural edits. Truncated display batches were re-read in smaller groups. The pre-edit inventory contains file sizes and SHA-256 identities. Final tree: **252 files**, **207 changed/added paths** (197 modified, 10 added). No original file was deleted. No runtime service, provider implementation or app mock was added.

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

The original closure claim was not justified. The initial pass found three CRITICAL, eleven HIGH and two MEDIUM issue groups. The 2026-09-09 counterexample pass added four HIGH and two MEDIUM groups (A17–A22), for 22 groups total: three CRITICAL, fifteen HIGH and four MEDIUM. The earlier green CI did not detect all of these conditions. All contract fixes preserve spec/00_SPEC_LOCK.md, which is byte-for-byte unchanged.

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
| A17 | HIGH | Reusable supplied/accepted assets require a fabricated generation prompt and lack a dedicated selected-source pin; NONE allows irrelevant generation fields. | Route-conditional generation vs reuse vs NONE contracts; selected artifact/version for reuse; fixtures/tasks/GS08/14. |
| A18 | HIGH | SUPPORTED with UNKNOWN layer and unlinked DEGRADED pass structural validation. | Cross-field JSON conditions plus all-layer fixtures; retain limit/expiry revalidation as runtime obligations. |
| A19 | HIGH | Unsupported claim promotion passes even when evidence is UNVERIFIED and samples absent; provider MEASURED checks wrong claim collection. | Claim-local conditional evidence validation; model routability conditional; correct profile-wide sample inspection. |
| A20 | HIGH | Paid attempt may omit shot_id and version_id entirely despite persisted target contract. | Require both nullable links, nonempty identity/hash strings; non-shot case explicitly null; fixture and TASK033. |
| A21 | MEDIUM | Deleting a task packet entry or all negative fixture cases is not guarded by exact index/case-set checks. | Exact task-index/path coverage and pinned fixture IDs, positive/negative gate coverage; mutation tests. |
| A22 | MEDIUM | No direct 0-33 mission completion crosswalk; assistant confused audit closure with implementation tasks. Agent bootstrap lacked explicit specification-maintenance scope. | Add mission-to-existing-evidence crosswalk and correction scope in existing report; no application task execution. Explicit audit mode prevents execution of numbered application packets during this mission. |

A06 remains empirical at runtime: missing measured evidence is represented as UNKNOWN/non-routable, not fabricated capability. The architecture defect was unjustified promotion; that is corrected. Full detail, authority and dependencies are in the issue matrix.

## C. Exact changes

Stable task IDs and the single canonical tree are retained. SPEC_VERSION is 4.3.1 because the follow-up rejects additional invalid records and permits prompt-free reuse with explicit source pins; ADR-0001 includes migration guidance. ADR-0001 records the owner-authorized Class B correction and migration considerations. The following is the complete changed-path list, including audit evidence; unchanged paths remain in the inventory.

| Exact path | Change | Reason |
|---|---|---|
| `.github/workflows/spec-governance.yml` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `AGENTS.md` | MODIFIED | Canonical governance/version/manifest, audit evidence and drift validation |
| `CLAUDE.md` | MODIFIED | Explicit specification-audit scope; numbered tasks remain future application work |
| `CODEX.md` | MODIFIED | Explicit specification-audit scope; numbered tasks remain future application work |
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
| `governance/AI_CODING_PROTOCOL.md` | MODIFIED | Explicit specification-audit scope; numbered tasks remain future application work |
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

### Exact follow-up changes from merged V4.3

No files were added or deleted in this follow-up. The following 32 existing paths were modified. Original 4.3 changes remain represented in the cumulative table above.

| Path | Follow-up reason |
|---|---|
| `AGENTS.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `CLAUDE.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `CODEX.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `MANIFEST.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `README.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `SPEC_VERSION` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `docs/adr/ADR_0001_CANONICAL_CONTRACT_HARDENING.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `evals/GOLDEN_SCENARIOS.md` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `evals/contract_fixtures.json` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `evidence/AUDIT_INVENTORY.csv` | A17–A22: findings, exact inventory, validation and mission completion evidence |
| `evidence/AUDIT_ISSUE_MATRIX.csv` | A17–A22: findings, exact inventory, validation and mission completion evidence |
| `evidence/FINAL_AUDIT_REPORT.md` | A17–A22: findings, exact inventory, validation and mission completion evidence |
| `governance/AI_CODING_PROTOCOL.md` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `governance/contract_index.json` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `governance/test_validate_spec.py` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `governance/validate_spec.py` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `schemas/common.schema.json` | A19: claim-local evidence and routability conditions |
| `schemas/effective_capability.schema.json` | A18/A19: safe capability and evidence resolution |
| `schemas/keyframe_generation_pack.schema.json` | A17: source-conditional generation/reuse/NONE |
| `schemas/model_profile.schema.json` | A19: claim-local evidence and routability conditions |
| `schemas/paid_attempt.schema.json` | A20: explicit nullable target links and nonempty identities |
| `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md` | A17: source-conditional generation/reuse/NONE |
| `spec/15_MODEL_INTELLIGENCE_AND_PROMPT_COMPILERS.md` | A19: claim-local evidence and routability conditions |
| `spec/18_COST_SPEND_ATTEMPT_POLICY.md` | A20: explicit nullable target links and nonempty identities |
| `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md` | A18/A19: safe capability and evidence resolution |
| `tasks/00_IMPLEMENTATION_ORDER.md` | Same canonical tree: patch version, ADR migration or explicit audit scope |
| `tasks/TASK_024_EXTERNAL_KEYFRAME_WORKFLOW.md` | A17: source-conditional generation/reuse/NONE |
| `tasks/TASK_026_MODEL_PROFILES_AND_CAPABILITY_RESOLVER.md` | A18/A19: safe capability and evidence resolution |
| `tasks/TASK_028_PROVIDER_PROFILES_AND_ADAPTERS.md` | A19: claim-local evidence and routability conditions |
| `tasks/TASK_033_COST_AND_PAID_ATTEMPT_GUARD.md` | A20: explicit nullable target links and nonempty identities |
| `tasks/TASK_039_GOLDEN_SCENARIO_AUTOMATION.md` | A21/A22: mapped counterexamples, complete coverage and audit scope |
| `traceability/REQUIREMENTS_TRACEABILITY.csv` | Clarify existing R-016/050/056/058/079; preserve NOT_STARTED implementation statuses |

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
| Selective keyframes | `spec/13_SELECTIVE_KEYFRAME_EXTERNAL_WORKFLOW.md` | Five routes; NONE has no pack/source; user/accepted-frame reuse needs a source pin but no generation prompt; no paid fallback |
| UniversalVideoSpec | `schemas/universal_video_spec.schema.json` | Typed global/locks/time/performance/camera/audio/initial/in/out/success/risk sections |
| ModelProfile | `schemas/model_profile.schema.json` | Exact version, claim evidence, unknowns and sample-scoped promotion |
| ProviderProfile | `schemas/provider_profile.schema.json` | Separate exposure, prices, limits, timeout/idempotency and evidence |
| EffectiveCapability | `spec/46_EFFECTIVE_CAPABILITY_AND_PROVIDER_FALLBACK.md` | Five-layer intersection with denial/unknown precedence and explicit revalidated degrade |
| SpendAuthorization | `spec/44_SPEND_AUTHORIZATION_REPAIR_FALLBACK.md` | User action/plan/hash/currency/candidate slots/caps/expiry and atomic reservations |
| PaidAttemptGuard | `schemas/paid_attempt.schema.json` | Logical attempt/authorization/candidate/request snapshot/certainty/cost links and explicit nullable shot/version targets |
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

85 positive/negative contract fixtures cover job vocabulary, paid links/certainty, reference isolation, empty UniversalVideoSpec sections, timeline structure/rational speed, imported versus generated provenance, no-paid QA, source-specific keyframes, claim-local evidence and contradictory capability records. Every fixture names mapped requirements and Goldens; its ID is indexed so accidental deletion cannot silently reduce coverage. Cross-record ownership, temporal knowledge, atomic transactions and timeline arithmetic require domain tests: GS05/GS19/GS27 specify these and do not pretend JSON Schema alone can enforce them.

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

Validator: **PASS**, 3587 checks at the 4.3.1 final contract pass (the earlier 4.3 pass had 3040). The following counts describe assertions, not independent end-to-end application tests.

| Validation family | Checks |
|---|---:|
| required_files | 244 |
| version | 3 |
| spec_numbering | 1 |
| schema_titles | 1 |
| metaschemas | 43 |
| typed_objects | 395 |
| local_refs | 242 |
| invariants | 12 |
| critical_required | 5 |
| traceability | 706 |
| goldens | 2 |
| tasks | 485 |
| task_graph | 91 |
| coverage | 3 |
| phases | 14 |
| profiles | 10 |
| skills | 77 |
| internal_paths | 724 |
| counts | 13 |
| fixture_integrity | 431 |
| contract_fixtures | 85 |

**22 governance unit tests passed**: a valid-tree baseline, the 12 original deliberate mutations, eight added coverage/condition/mapping mutations and one synthetic provider-evidence shape test. Original mutations: missing required file, job vocabulary drift, paid certainty drift, missing authorization, auto-retry enabled, open timeline, broken local ref, missing task reading, unsafe paid order, false IMPLEMENTED, duplicate requirement and unsupported MEASURED promotion. Ordinary CI installs validator dependencies then runs these offline checks. It contains no paid provider test. Added mutations cover missing/wrong task-index entries, empty/duplicate/negative-deleted fixtures, requirement mapping drift and removed capability/claim conditions. The provider test uses synthetic metadata, not real measurements. Hosted GitHub Actions status is separate from local execution and must be read for the pushed commit before claiming hosted CI passed.

A final full-tree pass also inspected schema/property/reference closure, all profile YAML, task/phase order, old state/enum spellings, illustrative duration examples, historical audit/version labels, traceability coverage and SPEC_LOCK immutability. The follow-up then demonstrated A17–A22 despite the earlier passing checks; those counterexamples and their regression gates are now included. No remaining foundational contradiction was identified within this bounded pass. This is a bounded evidence-based audit, not a mathematical proof that all possible future bugs are impossible.

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


### ASTRA Mission completion crosswalk

These rows track the specification mission, not execution of the 43 application packets. A prior conversational detour produced a standalone TASK-001 reality report; it is not canonical audit evidence, does not change task status, and is not a prerequisite for this mission. No implementation repository is requested by this handoff.

| Mission section | Obligation | Existing evidence / result | Classification |
|---|---|---|---|
| 0 | Audit role and production-contract scope | A–I of this report; AGENTS.md specification-maintenance scope | OK |
| 1 | Full repository read/inventory | 242 base files read before edits; 252 final paths in AUDIT_INVENTORY.csv; unchanged hashes retained | OK |
| 2–3 | Product identity and invariant authority | spec/00–03,15–16,46; R-001–003/016/048/058 | OK |
| 4 | Bounded research/evidence intelligence | spec/04,33,40; research/evidence schemas; GS06/25 | OK |
| 5–6 | Professional creative/filmcraft retrieval | 38 skill cards and 10 knowledge documents; spec/05,10; R-081; GS02/07/13; reviewed again in follow-up | OK |
| 7 | StyleDNA and grammar precedence | spec/39; style_dna and creative_strategy schemas; GS02 | OK |
| 8 | Long-form/series and knowledge separation | spec/07–08,32; scoped canon/character/context/snapshot schemas; GS05/27 | OK |
| 9 | Reference roles, lock/lifetime and isolation | spec/06,41; reference_binding and ingestion schemas; GS08/12/18 | OK |
| 10 | Adaptive segmentation | spec/11; generation_plan; task020; GS03/04/13/14 | OK |
| 11 | Accepted-parent continuity scheduling | spec/12,21,29; baton/dependency/job schemas; GS03/10/27 | OK |
| 12 | All-source selective keyframes | spec/13; A17 source-conditional schema and fixtures; TASK-024; GS08/14/16 | OK |
| 13 | UniversalVideoSpec and compilation | spec/14–16; typed UV schema/stage fixtures; TASK-025–028 | OK |
| 14 | Empirical model/provider knowledge | spec/15,24,37,46; A19 claim conditions; all bundled routes remain non-routable | EMPIRICAL_ONLY facts; OK contract |
| 15–16 | Paid safety, authorization and attempt identity | spec/18,44; A20 explicit target links; attempt/job/auth schemas; GS10/22/24/27 | OK |
| 17 A–G | Previously reported contract defects | A01–09 repaired; A17–21 close residual holes. TASK-001 stays audit-only; other packets have concrete tests | OK |
| 18–20 | Contextual revision, versions and modality selection | spec/17,21,44; revision/shot/dependency schemas; GS09/17/21 | OK |
| 21 | Durable assembly and FinalMaster QA | spec/42; typed timeline/master/QA schemas; GS19/21/27 | OK |
| 22 | Simple VN/EN UX and independent output language | spec/20,30; project_intent/event/revision schemas; GS11 | OK |
| 23 | Professional external round trip | spec/13,41; A17 no invented prompt on reuse; external provenance; GS08/18 | OK |
| 24 | Accepted-second economics and reuse before generation | spec/11,18; production_strategy/cost; TASK-019/020/031; GS04/14 | OK; measured probabilities remain empirical |
| 25 | Golden and benchmark coverage | 28 scenarios, benchmark rubric, 85 mapped contract fixtures; no paid CI | OK contract; future runtime tests pending |
| 26 | Traceability | 88 requirements; no orphan task/schema/Golden; requirement wording clarified without false IMPLEMENTED | OK |
| 27 | Structured governance | Validator, exact task/fixture coverage, local refs, invariant guards and 22 tests; section G | OK |
| 28–29 | Minimal scope and no application implementation | Same 252 files; no new services, skills or application code in follow-up; no paid API call | OK |
| 30–31 | Issue matrix and authority order | A01–22 issue matrix; pre-edit follow-up counterexamples retained; ADR-0001 addendum; SPEC_LOCK byte-identical | OK |
| 32 A–I | Required final report | Sections A–I contain inventory, all high findings, changed paths, 32-area verification, 43-task matrix, tests and unknowns | OK |
| 33 / final principle | Stop at contract closure; defer measured facts | No fabricated provider support or implementation completion; uncertain factual claims stay explicit; no speculative expansion | OK |

## I. Final verdict

**READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS**

Applies to this hardened specification revision. The ASTRA specification mission does not execute numbered application tasks. When the owner separately starts implementation, begin with TASK-001, follow the explicit safe order and keep real provider/paid/release gates blocked until their evidence exists. An application repository is not a prerequisite for completing this specification audit. This verdict does not claim that the application is implemented, live model quality is measured, or unmerged changes are already canonical on main.
