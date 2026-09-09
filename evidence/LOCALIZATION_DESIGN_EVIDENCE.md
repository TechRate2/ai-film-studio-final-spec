# Source-video localization — design evidence and closure

Date: 2026-09-09. Specification version: 4.4.0. Baseline: main ec25f9d61866530b2395e64b3d62950925bdf9c8 (4.3.1). This is an evidence record, not a second canonical design. Authority: `spec/47_SOURCE_VIDEO_LOCALIZATION.md` and accepted `docs/adr/ADR_0002_SOURCE_VIDEO_LOCALIZATION.md`.

## Owner request and bounded conclusion
The owner explicitly requested a separate subtitle/dubbing function after the main studio, preserving the source video, with automatic language detection, target selection, subtitles/dubbing checkboxes, simple voice/font/speed edits and one-click alignment. This authorizes the documented scope addition. It does not authorize building the application, paid probes, automatic speech regeneration or facial/video modification.

The feasible architecture is shared ingestion, versioned transcript/translation, per-speaker voice binding, optional authorized TTS, deterministic source-time mapping and the existing timeline/export system. Dubbing alone cannot change visible mouth movements; the UI must say so before approval. No design can guarantee perfect translation, voice performance, separation or alignment for every clip. Those are measured release conditions rather than architectural promises.

## Primary-source ledger
Sources retrieved 2026-09-09. Scope is the inspected README/documentation, not a code/security audit, deployment test or paid benchmark. Documentation observations are PARTIAL evidence; runtime quality and account entitlement remain unmeasured. Pin dependency releases and recheck licenses/terms before implementation; source-code and model-weight permissions are separate.

| ID | Primary source | Documented mechanism and useful decision | Limitation / adoption boundary |
|---|---|---|---|
| L-S01 | [VideoLingo](https://github.com/Huanshere/VideoLingo) | Transcription/alignment, subtitle segmentation, terminology and translation refinement followed by dubbing provide a useful staged reference. | Adapt context/glossary and reviewable target wording. Do not interpret its quality slogan as measured accuracy or assume translation languages imply TTS support. Repository advertises Apache-2.0; separately inspect dependent code/models. |
| L-S02 | [pyVideoTrans](https://github.com/jianchang512/pyvideotrans) | ASR, translation, TTS and composition with speaker handling and proofreading demonstrate a practical editable workflow. | Use as workflow evidence, not an embedded production dependency by default. Repository displays GPL-3.0; dependency/distribution decisions require license review. Do not copy automatic regeneration behavior into the paid guard. |
| L-S03 | [WhisperX](https://github.com/m-bain/whisperX) | Word alignment and diarization can improve transcript timing; alignment models depend on language. | README identifies imperfect diarization, weak overlapping-speech handling and words that may not align. Keep nullable timing and uncertain speakers, plus review rather than fabricated precision. Evaluate selected model/version on Vietnamese and target languages. |
| L-S04 | [SoniTranslate](https://github.com/R3gm/SoniTranslate) | Synchronized multilingual dubbing offers another reference for segment/speaker-oriented processing. | Its README distinguishes Apache-2.0 code from separately licensed models. A successful demo is not evidence of our provider cost, exact voice support, source-background fidelity or every language pair. |
| L-S05 | [ElevenLabs Dubbing Studio](https://elevenlabs.io/docs/eleven-creative/products/dubbing/dubbing-studio) | Editable clips and duration choices expose the real tradeoff between fitting a fixed window and natural speaking pace. | Adopt explicit fit choices, history and review. Do not silently regenerate clips or alter the source video to force fit. Documentation describes a vendor product, not guaranteed access through an aggregator. |
| L-S06 | [AtlasCloud audio documentation](https://www.atlascloud.ai/docs/models/audio) | A common asynchronous audio API covers model-specific tasks including speech generation and recognition; poll the submitted prediction. | Preferred candidate because of owner preference, not a qualified end-to-end dubbing system. Verify each exact ASR/TTS model's language, voice, timestamps, billing and account access. Never infer separation, diarization or complete Dubbing Studio support from a TTS listing. |

## Decisions from evidence (architectural inference)
Retain provider-neutral boundaries. First compare matching AtlasCloud operation routes; use another permitted adapter only when measured capability/cost warrants it and authorization covers the route. Do not hardcode a model as universally best. Ordinary ASR/TTS plus deterministic composition is sufficient to implement the scoped function; forced alignment and separation are selectively invoked when useful. Lip-sync is outside this scope and does not add a compulsory charge.

Reuse verified source analysis across language variants; synthesize only requested speech segments. Let subtitle-only users avoid all voice/media-generation costs. Distinguish spoken translation from subtitle wording so reading speed and acting pace can be optimized without corrupting source truth. Keep a bounded fit policy and explicit unresolved cases rather than cycling through paid candidates. Cost is ASR + reasoning/translation + selected separation + authorized TTS + deterministic compute/storage/export; exact tariffs and practical cost per accepted minute require current account pricing and real usage.

One-click alignment has a deliberately narrow, typed patch surface. A useful safe patch can adjust an unlocked cue, accepted speech tempo, gain, fades or allowed style. It cannot change the requested language, wording, speaker, source video speed or buy a new voice result. Those remain explicit edits with a cost preview when applicable. This boundary addresses the main operational risk in copying an otherwise convenient “regenerate everything” workflow.

## Audit delta and implementation truth
The 253-file baseline had a completed full-read audit inventory; unchanged hashes were verified before this extension. This change builds on that completed inspection and rereads affected contracts. It is not represented as a new independent full-repository line-by-line audit. All new files and changed contracts receive a final content/consistency review and offline validation. Historical core audit evidence remains in `evidence/FINAL_AUDIT_REPORT.md`.

Pre-edit findings L01–L05 are recorded in `evidence/AUDIT_ISSUE_MATRIX.csv`: missing later-release scope, under-typed transcript/timing, unsafe potential one-click repairs, missing counterexamples and empirical/tool-license uncertainty. They are resolved as contracts and test obligations, with empirical proof deferred. No implementation requirement is marked completed by this specification work.

Validation and exact changed-file inventory are recorded below at closure.

## Final consistency pass — specification only
262 repository files are inventoried: 48 specs, 45 schemas, 46 numbered tasks (49 files in tasks including index/templates), 8 phase gates, 33 Golden Scenarios in the existing scenario document, 96 requirements, 38 skill cards plus index, 10 filmcraft documents and 14 profile files. Nine files are added; the active canonical tree remains singular. All 96 implementation statuses remain NOT_STARTED. The previous 253-file full audit is preserved; this closure checks the changed/new content and repository-wide references, profiles, invariants, task mappings and fixture behavior.

Critical/high findings: L01 HIGH (release prerequisite cycle), L02 HIGH (source-time and speaker contract missing), L03 CRITICAL (one-click overwrite/paid retry risk), L04 HIGH (missing mode/timing/cost counterexamples). Their required contracts and regression obligations are now present. L05 remains empirical: exact language/model/account quality, cost, overlap and separation reliability, plus dependency-specific licensing review before adoption.

Architecture verification: the one Generalist Director, evidence-first research, provider-neutral compilers, ModelProfile/ProviderProfile distinction, EffectiveCapability UNKNOWN, Project Canon/character knowledge/context, adaptive segmentation, accepted-parent continuity, keyframe NONE/external sources, shot versioning/revision sandwich and paid guard retain their core contracts and existing fixtures. The extension scopes the same Director's tools to original media; it reuses artifact currency, voice profiles, timeline, FinalMaster, ownership and recovery. Style/taste cannot override source truth or rights. Native generated-video language decisions remain distinct from translating an imported source. No new Director, provider service family or mandatory lip-sync stage is introduced.

Task readiness: existing 43 packets retain their dependency graph and mapped proof, with TASK-043 now explicitly CORE-scoped. TASK-044–046 add specific vertical tests, exact reads and Phase 7 acceptance. Validator checks every task's dependencies/paths/requirements/Golden links. This is specification readiness; it cannot prove an unbuilt implementation or prevent dishonest completion without enforcing these gates in the implementation repository.

Schema integrity: 45 Draft 2020-12 metaschemas pass; 288 local-reference assertions resolve; critical mode/no-generation/no-auto-retry invariants agree across spec/schema; 113 positive/negative contract fixtures pass. Source bounds, duplicate IDs, time-map coverage, target ownership and optimistic concurrency remain explicit service-level tests rather than claims that JSON Schema proves cross-record runtime behavior.

Validation commands (offline, no paid media):
```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=../audit_deps python governance/validate_spec.py --json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=../audit_deps python -m unittest discover -s governance -p 'test_*.py' -q
git diff --check
```
The local dependency path was an isolated audit installation of governance/requirements.txt; CI installs that same requirements file normally. Result: validator PASS (4183 assertions), 28 governance tests PASS, whitespace check PASS. Tests include malicious enum changes, missing authorization/snapshot, removal of negative fixtures, mode conditions and relabeling/reordering the later release. These are specification tests, not simulated claims of real dubbing success.

## Exact changed paths and purpose
41 changed/added paths relative to the 4.3.1 baseline:

| Path | Purpose |
|---|---|
| `AGENTS.md` | Updates active version/counts or agent scope for core-first extension. |
| `MANIFEST.md` | Updates active version/counts or agent scope for core-first extension. |
| `README.md` | Updates active version/counts or agent scope for core-first extension. |
| `SPEC_VERSION` | Updates active version/counts or agent scope for core-first extension. |
| `docs/adr/ADR_0002_SOURCE_VIDEO_LOCALIZATION.md` | Records owner approval, alternatives, scope and compatibility. |
| `evals/BENCHMARK_RUBRIC.md` | Adds five behavioral scenarios, typed counterexamples and language-quality benchmark obligations. |
| `evals/GOLDEN_SCENARIOS.md` | Adds five behavioral scenarios, typed counterexamples and language-quality benchmark obligations. |
| `evals/contract_fixtures.json` | Adds five behavioral scenarios, typed counterexamples and language-quality benchmark obligations. |
| `evidence/AUDIT_INVENTORY.csv` | Records source evidence, inventory, pre-edit findings and precise closure limits. |
| `evidence/AUDIT_ISSUE_MATRIX.csv` | Records source evidence, inventory, pre-edit findings and precise closure limits. |
| `evidence/FINAL_AUDIT_REPORT.md` | Records source evidence, inventory, pre-edit findings and precise closure limits. |
| `evidence/LOCALIZATION_DESIGN_EVIDENCE.md` | Records source evidence, inventory, pre-edit findings and precise closure limits. |
| `governance/AI_CODING_PROTOCOL.md` | Checks release partitions, dependencies, schemas, negative fixtures and safe coding handoff. |
| `governance/contract_index.json` | Checks release partitions, dependencies, schemas, negative fixtures and safe coding handoff. |
| `governance/test_validate_spec.py` | Checks release partitions, dependencies, schemas, negative fixtures and safe coding handoff. |
| `governance/validate_spec.py` | Checks release partitions, dependencies, schemas, negative fixtures and safe coding handoff. |
| `knowledge/filmcraft/SOUND_DESIGN.md` | Adds context-sensitive dubbing performance/fit decisions and contraindications. |
| `phases/PHASE_6_BETA_RELEASE.md` | Enforces CORE completion before independent localization development/release. |
| `phases/PHASE_7_SOURCE_VIDEO_LOCALIZATION.md` | Enforces CORE completion before independent localization development/release. |
| `schemas/composition_timeline.schema.json` | Adds optional subtitle appearance fields without breaking legacy styles. |
| `schemas/localization_project.schema.json` | Typed variant/transcript/timing or safe-review record; closed shapes and safety conditions. |
| `schemas/localization_review.schema.json` | Typed variant/transcript/timing or safe-review record; closed shapes and safety conditions. |
| `schemas/project_intent.schema.json` | Adds explicit workflow selection with legacy STUDIO interpretation. |
| `spec/00_SPEC_LOCK.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/01_VISION_AND_NON_GOALS.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/09_DIALOGUE_VOICE_LOCALIZATION.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/20_CHAT_FIRST_WORKSPACE_UX.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/25_ACCEPTANCE_AND_DEFINITION_OF_DONE.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/27_DOMAIN_DATA_MODEL.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/28_API_AND_EVENT_CONTRACTS.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/42_TIMELINE_ASSEMBLY_EXPORT_MASTER_QA.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/45_END_TO_END_WORKFLOW_STATE_MACHINES.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `spec/47_SOURCE_VIDEO_LOCALIZATION.md` | Defines/links the approved original-preserving workflow and shared contract boundaries. |
| `tasks/00_IMPLEMENTATION_ORDER.md` | Enforces CORE completion before independent localization development/release. |
| `tasks/TASK_043_BETA_RELEASE_GATE.md` | Enforces CORE completion before independent localization development/release. |
| `tasks/TASK_044_SOURCE_VIDEO_SUBTITLES.md` | Concrete extension implementation packet, prerequisites, reads and falsifiable acceptance. |
| `tasks/TASK_045_DUBBING_AND_RETIMING.md` | Concrete extension implementation packet, prerequisites, reads and falsifiable acceptance. |
| `tasks/TASK_046_LOCALIZATION_REVIEW_AND_RELEASE.md` | Concrete extension implementation packet, prerequisites, reads and falsifiable acceptance. |
| `traceability/PHASE_GATE_MATRIX.csv` | Maps eight new requirements and separates CORE from LOCALIZATION evidence gates. |
| `traceability/README.md` | Maps eight new requirements and separates CORE from LOCALIZATION evidence gates. |
| `traceability/REQUIREMENTS_TRACEABILITY.csv` | Maps eight new requirements and separates CORE from LOCALIZATION evidence gates. |

## Verdict
READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS

Applies to the specification, including the owner-approved extension. Begin application work only when separately requested, at TASK-001 and the binding safe execution order. Implement the main Studio through TASK-043 before TASK-044–046. Real language/provider and release evidence remains required; neither “100% feasible in every circumstance” nor superior-to-all-products performance is claimed.
