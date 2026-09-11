# Market, production pain and feasibility review

> Latest review: 2026-09-11, specification 4.4.2. The new workflow audit below supersedes the earlier endpoint-retrieval limitation and QA-contract assessment. Earlier sections preserve their dated evidence, not current execution claims.

## 2026-09-11 workflow quality and cost audit

### Scope and conclusion

Baseline main: `1be7e30f0c4ca60a038b00ec03db13172603c380`, tree `a4d8d731f741e7a154cf123da5edeb99869109c6`, version 4.4.1. All 265 inventoried paths were reconciled; every non-self-referential hash matched the preceding full audit. This pass re-read the relevant Director, research, creative, production, compiler, QA, spend, benchmark and task contracts and inspected current official sources. It is a continuation of the recorded whole-repository audit, not a claim that all files were newly reread line by line or that the application was run.

Two HIGH gaps are confirmed: contradictory QA could be stored as ACCEPTABLE, and prompt-implied API operation did not have an explicit preflight conformance case. Three MEDIUM gaps concern negative route cost, complete-route cost comparison and stale provider-source discovery. The pre-edit Q01–Q05 matrix records authority, impact and minimal fixes. Changes preserve the Generalist Director and existing task graph; no additional agent/service or application feature is warranted.

The system should maximize accepted creative value within constraints, not model settings, number of searches, reasoning tokens or generated candidates. The contract now better prevents avoidable errors. Whether its Director makes better films or spends less than competitors remains a measured implementation question.

### Current commercial evidence and limits

Sources in this subsection were inspected 2026-09-11. Product pages establish public capabilities; documentation establishes stated behavior. Neither establishes a project's acceptance probability. Embedded examples and demonstrations were identified, but no full video playback, frame/audio evaluation, competitor account run or paid comparison was performed. Published examples are selected successes without a complete attempt/cost denominator.

| Source | What was verified | Design implication — our inference |
|---|---|---|
| [Topview](https://www.topview.ai/) and [Canvas](https://www.topview.ai/canvas) | Public positioning includes conversational scene planning, model selection, editable shots, drama and reference analysis. | These are market expectations, not unique proof of our advantage. Compare the effort to finish and revise an accepted project. |
| [Runway workflow Agent](https://help.runwayml.com/hc/en-us/articles/53645211363475-Building-and-running-Workflows-with-Agent) | Documents estimated-credit approval and automatic execution settings; acknowledges a completed workflow can have missing node outputs. | Job completion must not equal accepted project completion. Preserve per-artifact QA and FinalMaster gates. |
| [LTX Studio](https://ltx.io/studio) | Public workflow joins scripts, reusable character/object/location Elements, storyboards, timeline and sound. | Keep project-level state and editable assembly; storyboards remain selective in this product. |
| [Runway image-to-video guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) | Gen-4.5-oriented guide pairs prompts with example results, emphasizes motion and explains conflict between image motion cues and requested motion. | Inspect reference/prompt agreement before spending. This is a scoped hypothesis for other models, never an inherited Seedance default. |
| [AtlasCloud reference guide](https://www.atlascloud.ai/blog/case-studies/generative-ai-model-seedance-2-0-a-guide-to-all-round-reference) | A provider-published Seedance 2.0 reference tutorial is available with examples. | Use examples to design controlled probes. The article's fixed identity/motion conditioning ratio has no project calibration and must not become a compiler rule. |
| [ElevenLabs Dubbing Studio](https://elevenlabs.io/docs/eleven-creative/products/dubbing/dubbing-studio) | Documents speaker/clip editing, history and fixed-versus-dynamic timing trade-offs; the page now labels the product maintenance-only. | Reuse the proven interaction pattern, not a dependency on that UI's future development. Preserve timing, translation, speaker and version controls in our separate extension. |
| [WhisperX](https://github.com/m-bain/whisperX) | Maintainer documents overlap, speaker attribution and alignment limitations. | Unknown word times and uncertain speakers require review paths; automatic alignment cannot claim universal precision. |

The earlier 13-product map remains useful category coverage. This refresh is a targeted primary-source investigation of quality/cost decisions, not a worldwide census or an invented competitor ranking. No claim is made that a competitor lacks undocumented continuity, billing or safety protections.

### Seedance and AtlasCloud decisions

`evidence/SEEDANCE_KNOWLEDGE_STATUS.md` contains the dated endpoint and billing findings, including their source links. Exact public endpoint contracts can now be inspected for the owner's intended provider. Their existence removes an information-retrieval gap; it does not qualify an account or prove output quality.

Keep 2.0 and 2.5 profiles and conformance tests independent. Resolve each exact endpoint operation before compiling; distinguish requested generation from provider enhancement. Inspect the account-specific quote for the exact payload and retain its estimate status. None of this authorizes generation or unlocks UNKNOWN capability layers. Vietnamese native dialogue, reference stability and long-sequence acceptance require their own samples.

### Decision-by-decision audit

OK means an existing contract covers the behavior; it does not mean implemented or empirically successful. All numbered implementation packets remain future work. Contract fixes below apply to the existing requirement mappings.

| Step / canonical owner | Decision and durable output | Failure the implementation must catch | Assessment and proof target |
|---|---|---|---|
| Brief and scope — specs 02–03, 20 | Intent, audience, hard constraints, output language and complexity horizon determine scope. | A short multi-episode story is misrouted as disposable B-roll; UI locale changes dialogue. | OK; GS01/05/11. No fixed genre branch or second Director. |
| Ingestion — specs 06, 41, 43 | Validate assets/rights; resolve entities; assign reference role, lock and lifetime. | Camera reference leaks face/background; corrupt upload or untrusted instructions enter Canon. | OK; GS02/18/23; inspect provenance and isolation, not only successful upload. |
| Research — specs 04, 33, 40 | Identify a material uncertainty, reuse fresh evidence or search under shared limits, distill claims. | Repeated-source false corroboration, stale model fact, recursive research budget reset. | OK; GS06/25; decision-linked sources and persisted counters are required. |
| Creative direction — specs 05, 10, 39 and filmcraft | Choose viewer promise, information/emotional progression, performance, motivated camera and payoff. | Generic cinematic adjectives hide missing scene purpose; every beat becomes a fast cut. | OK + EMPIRICAL_ONLY; GS02/07/13; evaluate complete scenes and viewer intent. |
| Canon and context — specs 07–08, 32 | Resolve identity/aliases, world truth, individual knowledge and minimal ActiveContextPack. | A character acts on another character's secret; full Bible is repeatedly submitted. | OK; GS05/27; test asymmetric knowledge and concurrent updates. |
| Production route — spec 11 | Compare reuse/still/motion/full generation and complete-route economics. | Lowest video price wins despite costly required audio/post; UNKNOWN or negative price looks free. | Q02/Q04 fixed; TASK-019, GS04/14 and schema boundary fixtures. |
| Segmentation and references — specs 11–13 | Choose meaningful continuous/segmented/continuation units and the smallest sufficient inputs. | Automatic maximum duration, fixed small chunks, or mandatory keyframes inflate failure/cost. | OK; GS03/08/13/14/16; NONE must produce zero image work. |
| Compile and expose — specs 14–16, 31, 46 | Pin universal intent, independent model/provider evidence, all five capability layers and compiled request. | Prompt implies editing while parameters request reference generation; newer model inherits old syntax. | Q03 fixed; TASK-027 and GS03 conformance variants. Actual adherence is empirical. |
| Audio planning — specs 09, 42 | Decide native audio, controlled voice, narration, ambience/music and subtitle language. | English instruction text silently changes Vietnamese dialogue; unnecessary lip-sync/TTS is purchased. | OK + EMPIRICAL_ONLY; GS07/11/17. Preserve requested language and compare sufficient routes. |
| Authorize and submit — specs 18, 29, 44 | Bind approved slots, request hashes, worst-case liability and durable submission identity. | Estimate is mistaken for a cap; local timeout or disappointing output triggers another paid call. | OK; GS10/22/24/27. Unknown liability blocks; no extra candidates by default. |
| Dependency scheduling — specs 12, 21 | Parent acceptance releases a child with observed Baton plus canonical identity. | Successful upstream task releases an unaccepted or rejected parent. | OK; GS03/09/10; verify actual child call count remains zero. |
| QA and acceptance — spec 19 | Evaluate required conditions and allowed imperfections; persist evidence and permitted acceptance. | Aesthetic mean/self-confidence overrides failed identity or missing required checks. | Q01 fixed; TASK-034, GS10 and negative schema/mutation tests. Calibration remains empirical. |
| Contextual revision — specs 17, 21 | Smallest affected modality, immutable new version, incoming/user/outgoing continuity sandwich. | Subtitle typo spends video; changed ending silently invalidates the next accepted shot. | OK; GS09/11/21; selective STALE propagation and reversible acceptance. |
| Assembly and final export — spec 42 | Compile durable timeline from accepted CURRENT versions; validate full master. | Missing/duplicated ranges, wrong language, audio holes or stale source produce false completion. | OK; GS19; do not infer FinalMaster success from node completion. |
| Learn and recover — specs 22, 29, 35 | Scoped outcome evidence, versioned state, restore and controlled provider upgrades. | Technical failure teaches wrong taste; restart loses liability; new alias silently changes behavior. | OK + EMPIRICAL_ONLY; GS24/27/28; retain confounders and historical snapshots. |
| Separate localization — spec 47 | Source video → transcript/speakers → translation → optional voice/subtitles → deterministic alignment/export. | Forced mouth/video regeneration, bad speaker mapping, stale auto-fix or hidden new TTS. | OK + EMPIRICAL_ONLY; TASK-044–046 after core, GS29–33. Keep source-preserving limits. |

### What higher-quality reasoning should actually change

For a quiet dramatic reveal, the Director may choose a held two-shot, a delayed reaction and silence because the viewer needs to notice who understood the secret. An orbit, several independent gestures and explanatory dialogue could weaken that purpose while increasing generation difficulty. For a product demonstration, exact verified packaging and a readable action may outweigh simulated lens spectacle. These are original illustrative directing decisions, not model-performance claims.

The intelligence loop already has the needed pieces: relevant evidence and skills → explicit intent/constraints → bounded critique of a concrete risk → feasible production route → observable acceptance. Use a more capable reasoning configuration only when it measurably improves decisions enough to justify its latency/cost. Do not prescribe a permanent winning LLM or send the full repository into every turn. A future model/profile/compiler upgrade must preserve the same neutral contracts and pass relevant regression gates.

Research should answer a decision-changing question, such as whether an endpoint accepts the chosen reference mode, rather than collect generic inspiration indefinitely. Prompt refinement before generation can be cheap; repeated paid generations are not an implicit continuation of reasoning. The existing authorization boundary remains binding.

### Cost and empirical qualification

Report generation cost per unique accepted source second separately from total finished-project cost, human intervention time and time to first accepted master. Include failed/rejected spend. Existing media, native sound, external assets and deterministic edits may avoid unnecessary generative stages, but compute/storage/rights costs still exist. A cheaper provider or lower tier is useful only if the required output remains acceptable.

Before claiming an advantage, pre-register representative briefs and acceptance criteria under `evals/BENCHMARK_RUBRIC.md`: exact product demonstration, emotional reaction, multi-speaker Vietnamese dialogue, readable action, reference-isolated camera movement, factual explainer, long-form continuation and source-video localization. Compare matched constraints, recorded human work and all attempted outputs. Perform decision-only and failure/restart tests without paid APIs first; any media comparison requires credentials and an explicit sample/budget gate. Do not tune on selected successes and report them as unseen-test performance.

Open empirical items: account exposure and deployed version, effective pricing, native Vietnamese/pronunciation quality, practical reference ceiling, duration/action reliability, preservation after revisions, QA false-acceptance rate and real user effort versus competitors. These do not justify another speculative architecture layer. They do prevent promises of universal film quality, perfect autonomy or guaranteed cost savings.

### Exact 4.4.2 changes and verification

The change inventory and validation results are recorded in `evidence/FINAL_AUDIT_REPORT.md`; Q01–Q05 are in `evidence/AUDIT_ISSUE_MATRIX.csv`. ADR 0004 records the contract decision. Source discovery leaves profiles PARTIAL/non-routable and all 96 requirement statuses NOT_STARTED. No application, paid generation or competitor trial was executed.

Verdict: **READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS** for staged implementation. This does not certify commercial release, full model qualification or superiority. The next useful progress is implementation and scoped evidence through the existing gates, not indefinite expansion of the specification.

---

## Historical review — 2026-09-09

Review date: 2026-09-09. Baseline: main commit d720f8a8e51dd3c893ccca8b3fd7e7b404db10e7, specification 4.3.1. This is evidence and an evaluation plan, not a second canonical specification or a claim of implemented features. Existing requirements retain their authority. No application implementation, competitor account trial, paid generation or account-entitlement probe was performed.

## Decision

The architecture is a credible build contract for an AI Creative Director and production studio. It does not establish absolute feasibility of arbitrary requested footage, autonomous professional judgment in every genre, commercial profitability, or superiority over present and future products. Those are separate claims requiring scoped evidence. The strongest defensible product thesis is reducing total work and wasted spend required to obtain an acceptable, editable, traceable finished project.

The initial model strategy should retain independent Seedance 2.0 and 2.5 qualification. A planned integration is not an available route. The existing staged implementation order remains binding: the real Seedance 2.0 vertical slice does not certify 2.5, and a 2.5 release promise requires its own endpoint, entitlement, compiler, billing and acceptance evidence. External production/import remains a valid workflow while a particular integration is unqualified; it must be visibly external, with provenance, rather than masquerading as an internal API result.

## Method, coverage and limits

This review builds on the full-repository audit documented in `evidence/FINAL_AUDIT_REPORT.md`, rather than claiming that market research repeats every previous read. The 252-file inventory was compared with current content hashes before edits: the 250 non-self-referential records match the audited content; report and inventory use the documented Git-tree-anchor exception. Model intelligence, provider abstraction, QA, evidence policy, Seedance playbook, deployment, integration, probe, fallback and benchmark contracts were re-read for this review. The whole architecture is mapped by logical group below. Schema and governance validation was rerun; it is structural evidence, not real-media success.

Market coverage is a representative cross-category map of 13 products, not an exhaustive worldwide directory. Public vendor pages establish advertised positioning and documented workflow, not measured reliability or absent private capabilities. A filmmaker interview provides firsthand experience from one production; it cannot establish population failure rates. Search snippets are treated as discovery evidence where full documentation could not be extracted. No competitor is labeled inferior because its private billing or continuity implementation is undocumented.

The report deliberately excludes unsupported pricing comparisons, synthetic market-share estimates and numeric superiority scores. Product pages change; access dates apply to the URLs in the source ledger. Re-check their relevant content before an integration or purchasing decision.

## Competitive map

Each final-column entry is our product-analysis inference, not a vendor claim or a measured gap in that vendor.

| User job | Product | Public evidence inspected | Implication for this project |
|---|---|---|---|
| Conversational production, marketing and short drama | Topview | Chat-driven production, editable canvas, drama tools and asset workflows [S1] | Chat plus generation is already competitive territory; measure completed-project effort and revision integrity. |
| Cinematic creation, ads and reusable workflows | Higgsfield | Tool guide separates Cinema Studio, Marketing Studio and broader workflow/agent tools [S2] | Camera controls and multiple models alone are insufficient differentiation. |
| Agent-assisted creative workflows | Runway | Agent builds workflows; execution can ask before generation with an estimate or use automatic generation mode [S3] | Clearly distinguish initial-run authorization from new post-QA paid attempts; do not equate the competitor's automatic mode with blind quality retries. |
| Script-to-film preproduction and editing | LTX Studio | Script/concept/image/video inputs, storyboards, shot editing and production workspace [S4] | Story structure, reusable characters and integrated tools are not unique claims. |
| Reference-driven scene construction | Google Flow | Public page lists ingredients, frames, extension, editing and Scenebuilder [S5] | Prove continuity across revisions and saved projects, not merely reference input support. |
| Avatar presentation and localization | HeyGen | Translation, voice preservation and lip-sync workflows [S6] | Language and pronunciation acceptance must be evaluated independently from image quality. |
| Enterprise learning and training | Synthesia | Avatar-based training from scripts/materials [S7] | Instructional correctness and maintainability matter more than decorative cinematic movement. |
| Product and performance advertising | Creatify | Product URL to ad workflow [S8] | Product truth, substantiation and editability must survive automated script and asset selection. |
| Podcasts, interviews and recorded content | Descript | Text editing, audio cleanup, clips and an editing assistant [S9] | Reusing recorded footage can be the correct production strategy; generating everything is a disadvantage. |
| Long-to-short repurposing | OpusClip | Highlight selection, reframing and captions [S10] | Preserve the meaning of source speech; a hook score is not demonstrated retention. |
| Music videos and visualizers | Neural Frames | Audio-reactive music-video workflows [S11] | Musical structure, holds and synchronization require more than fast cuts on every beat. |
| Professional postproduction | Adobe Premiere / Firefly | Generative Extend supplies additional footage within editing; generated frames are labeled [S12] | Classify generative extension as potentially billable generation, distinct from deterministic trim/hold/mux. |
| Character animation and motion capture | Krikey AI | Animation from text/video, avatars and a 3D editor [S13] | Where exact motion is essential, imported controlled animation is a legitimate alternative to stochastic video. |

Fashion, food, real estate, travel, education, documentary, comedy, fantasy and UGC are content domains that can use several of these workflow categories. This research does not claim a separate exhaustive vendor census or a validated acceptance benchmark for each domain. A niche name must not create a new autonomous Director or hardcoded pipeline. It should change evidence, grammar, constraints, assets and production decisions through the existing contracts.

## What users actually struggle with

In a firsthand interview, filmmaker Kévin Mendiboure reported 3,229 image/video generations and 242 hours for CATACOMBES. He described three-character reverse-angle dialogue and screen-axis continuity as particularly difficult, and edited while generating to assess connections [S14]. This is one self-reported production, not an average cost or a benchmark of this project's routes.

The following risk register combines that experience, the workflow needs exposed by the product map and adversarial analysis of this repository. Rows without a firsthand source are engineering risk hypotheses, not claims about how frequently users encounter the issue.

| Failure or pain | Existing canonical defense | What implementation must demonstrate |
|---|---|---|
| Attractive clips fail to form a coherent scene | Story purpose, performance, geography, continuity and editorial contracts in specs 05, 10–12 | Judge the assembled scene, including reactions and reverse angles; isolated frame quality cannot pass it. |
| Face, outfit or product drifts between shots | Reference bindings, Canon, Baton, immutable versions; specs 06–08, 12, 17 | Check both canonical identity and observed accepted state. A stronger reference does not guarantee exact pixels. |
| Character knows a secret too early | Scoped knowledge and ActiveContextPack; specs 07–08, 32 | A ten-character scenario must include different beliefs and knowledge, alias collisions and a later reveal. |
| Fixing action alters a good face or ending | Semantic revision, Continuity Sandwich and dependency currency; spec 17 | Compare preserved dimensions and outgoing boundary; failed preservation is visible and never silently accepted. |
| Credits disappear during retries | Authorization, attempt certainty and reconciliation; specs 18, 29, 44 | Crash/timeout/concurrent-click tests establish no duplicate authorized liability. Post-output changes need applicable authorization. |
| Every scene incurs images and storyboard overhead | ProductionStrategy and selective keyframes; specs 11, 13 | A simple request can use NONE. External accepted keyframes produce zero internal image calls. |
| Long clips omit events; tiny clips create seams | Adaptive segmentation; specs 11–12, 31 | Compare route-specific duration and event complexity; choose the longest reliable useful unit, without a fixed duration rule. |
| Camera references contaminate identity or location | Positive control and negative scope; spec 06 | Deliberately conflicting reference fixtures must isolate the requested function. |
| Prompt advice disagrees across model versions | Claim-scoped profiles and compilers; specs 15, 24, 37 | A newer model gets independent evidence; neither long nor short prompts are universally prescribed. |
| Speech is correct in text but wrong in delivery | Voice identity, localization and audio QA; specs 09, 42 | Test speaker attribution, timing, Vietnamese pronunciation and separate UI/output languages. |
| A product label or factual demonstration is wrong | Product truth, rights and QA; specs 05, 06, 19, 43 | Use verified assets/graphics or a different route when exactness is required; realism is not factual validation. |
| A subtitle correction costs another video | Edit classification and durable timeline; specs 17, 42 | Observe zero video generation for subtitle-only, cut-only and deterministic mix corrections. |
| Research becomes an expensive planning loop | Research ROI, evidence distillation and stop conditions; specs 04, 33, 40 | Reuse fresh relevant evidence; stop on bounded budget/low expected gain and expose unresolved uncertainty. |
| Months of project state are lost or become stale | Durable jobs, versioned artifacts, snapshots; specs 21, 29, 32, 35 | Restart, restore and provider-outage drills retain acceptance, liability, Canon and lineage. |
| AI QA approves a polished but incorrect result | Hard-lock veto and calibrated assessment; spec 19 and benchmark rubric | Measure false acceptance and human disagreement; model self-confidence is not calibration. |
| Successful creative choices become bad universal rules | Scoped taste/outcome learning; spec 22 | Retain exposure denominators and confounders; do not infer global taste from a technical rejection. |

These defenses are specification coverage. They remain NOT_STARTED as implementation requirements until concrete execution evidence exists. A rigorous contract improves feasibility by preventing predictable mistakes; it does not remove model uncertainty.

## Seedance evidence and immediate route strategy

The Seedance 2.0 technical report describes multimodal audio-video generation and particular generation/reference limits [S15]. These describe that report's model/platform scope; they are not transferable to every current provider or account. Its existence strengthens primary-source knowledge, while this project's measured acceptance probability remains unknown.

The official Seedance 2.5 launch page is dated **2026-07-31**, regardless of search-result relative dates. It advertises longer single-pass generation, extensions, expanded references and targeted editing. These are announced features, not this project's observed behavior. Its announcement-time statement about forthcoming API access must not be presented as the current availability state [S16].

On 2026-09-09, search retrieval of official BytePlus API/tutorial pages mentions Seedance 2.5; opening those pages returned a JavaScript shell rather than the complete API contract. The tutorial shell gives an update date of 2026-09-08 [S17, S18]. This is a concrete freshness/retrieval limitation: neither API absence nor a usable exact model identifier was established. No endpoint name, entitlement, price or production capability is inferred from that snippet.

| Decision | Seedance 2.0 | Seedance 2.5 |
|---|---|---|
| Product priority | Initial real vertical slice already assigned to TASK-030 | Initial model-family priority from owner; independent qualification required |
| Public knowledge | Primary technical report plus existing third-party observations | Official announcement plus newer API discovery evidence |
| Runtime route in this repo | Non-routable; exact deployment facts absent | Non-routable; exact deployment facts absent |
| Evidence that unlocks use | Versioned API and billing contract, matching account/policy, controlled authorized tests | Same requirements, independently collected; never a copy of 2.0 measurements |
| If route unavailable | Block that route or present a supported alternative within policy | Same; external import is explicit, not fake internal success |
| What is not promised | Guaranteed first-pass identity, action, dialogue or long-form reliability | Guaranteed precision editing, retained pixels or reliable long-form continuation |

The product may prioritize both models without promising simultaneous commercial availability. Implement shared ports once, then qualify each exact route separately. If the owner requires both routes for launch, release remains blocked until both pass; successful 2.0 integration cannot satisfy that commercial condition by renaming a profile.

## Whole-architecture feasibility crosswalk

The classification here concerns architecture, not completed software. OK means the existing contract addresses the risk; EMPIRICAL_ONLY identifies execution-dependent proof. No new Director, service or schema is justified merely by competitor feature lists.

| Canonical group | Assessment | Feasibility boundary |
|---|---|---|
| 00–03: authority, product, Director and adaptive scope | OK | One orchestrator can use modules and neutral ports. Its decision quality requires evaluation on actual briefs. |
| 04–05: research and creative reasoning | OK + EMPIRICAL_ONLY | Bounded research and explicit story decisions are implementable; relevance, humor and retention are not guaranteed. |
| 06–08: references, Canon and character knowledge | OK | Storage/retrieval/isolation are enforceable; generators can still violate the supplied constraints. |
| 09–10: language, performance and filmcraft | OK + EMPIRICAL_ONLY | Professional decision logic exists; accurate speech and subtle acting need language/scene-scoped review. |
| 11–14: strategy, DAG, keyframes and universal intent | OK | Adaptive routes, dependency gating and typed compilation are implementable. NONE must remain a genuine zero-image path. |
| 15–16: model intelligence and providers | OK + EMPIRICAL_ONLY | Independent profiles/compilers support expansion; a new model does not automatically support old features. |
| 17–18: revision, versions and cost | OK | Immutable history and spend fences can be tested deterministically; semantic preservation needs media QA. |
| 19–20: QA and simple UX | OK + EMPIRICAL_ONLY | Progressive controls and user review are feasible. Automatic acceptance requires scoped calibration under the rubric. |
| 21–23: durability, learning and security | OK | Implement and test storage, access, deletion and recovery. Learning quality is not equivalent to storing feedback. |
| 24–26: evidence, acceptance and governance | OK | Task evidence and rejection of unsupported claims are explicit. Green specification CI is not product certification. |
| 27–30: data, API/events, runtime and UI states | OK | Typed contracts resolve core integration ambiguity; actual transactions and event ordering require fault tests. |
| 31–33: Seedance, series and research playbooks | OK + EMPIRICAL_ONLY | Long projects use scoped state and accepted outputs; model reliability over repeated continuation is unknown. |
| 34–38: tests, operations, integration, probes and glossary | OK | Existing gates cover version changes and qualification. Deployment/recovery must be exercised, not inferred from prose. |
| 39–41: style, research ROI and ingestion | OK | Transfer mechanisms without copying protected elements; mixed inputs remain untrusted until validated. |
| 42–43: assembly, final master and rights | OK | Deterministic assembly and rights decisions are enforceable; permission facts must come from actual evidence. |
| 44–46: spend, workflow and capability intersection | OK | Unknown submission stays reconciliatory; all five capability layers and authorization scope govern new spend. |
| Skills and filmcraft knowledge | OK as audited baseline + EMPIRICAL_ONLY | Professional reusable instructions were hardened in the prior audit. Their effect on acceptance requires ablation or controlled comparisons. |

## Upgrade and future-model stress cases

Provider independence is a maintenance strategy, not a prediction of future APIs. The current contracts already require versioned profiles, compiler provenance, re-probing on change, pre-spend capability revalidation and explicit fallback decisions. Use the following review cases to evaluate their implementation; they do not introduce another state vocabulary.

1. A provider reassigns a model alias. Do not overwrite historical profile/compiler snapshots. Resolve the concrete available version and invalidate the affected capability evidence before new spend. If the exact version cannot be established, preserve UNKNOWN.
2. A model adds editing but removes a reference feature. Evaluate each required feature independently; a stronger aggregate benchmark cannot override a missing HARD_LOCK capability.
3. A cheaper route replaces a current provider. Compare accepted-second cost under the same constraints and include failures. A lower advertised unit price alone is insufficient.
4. A provider retires a route while jobs are running. Preserve upstream identity and reconcile submitted work. Availability change does not authorize duplicate generation elsewhere. Accepted artifacts and historical versions remain usable according to their currency and rights.
5. A new compiler or profile regresses quality. Keep the prior proven configuration available where the route remains supported, and preserve the new version's evidence. Any newly paid comparison or rerun still needs a planned authorization; no hidden paid shadow traffic.
6. A release changes only internal reasoning or a skill. Run the relevant non-paid Golden tests and compare decision quality before claiming improvement. More reasoning tokens or longer context are not success metrics.

Whether the implementation handles these cases is a future gate, not something this specification audit has executed. If implementation reveals missing cross-module shapes, use the existing Class B process instead of inventing private incompatible objects.

## How to prove a real advantage

Use `evals/BENCHMARK_RUBRIC.md` as the canonical measurement contract. Before a paid comparison, predeclare the briefs, hard constraints, acceptance criteria, route versions, reference assets, budgets, permitted revisions and evaluator procedure. Compare completed workflows under equivalent rights and assets. Competitor access must be legitimate, and differences in model availability or human intervention must be reported as confounders.

Start with a small cross-category set: a product ad preserving exact packaging; a Vietnamese presenter; a three-person dialogue with reverse angles; a complex action beat; a music-led sequence; an educational explanation with sourced claims; a long-to-short edit of real footage; and a recurring-character episode with a delayed reveal. These are candidate benchmark briefs, not an authorized paid run or a new mandatory filename list. Pre-register sufficient samples and uncertainty targets rather than declaring that one good output proves the category.

Measure generation cost per unique accepted second, full-project cost, human intervention time, time to first acceptable project, rejected paid attempts, preserved-dimension failures after revision, stale dependency detection and final-master failures. Record all samples, including abandoned projects. An unchanged subtitle path should be evaluated by zero video calls, not by a subjective rating. A dialogue scene needs blinded human judgment of geography, intention and timing as well as technical validation.

Report results separately by content complexity, duration, character count, reference quality, route and output language. The same product may excel at constrained advertising and remain unreliable for nuanced drama. Report a confidence interval or uncertainty method where applicable and preserve disagreements. Do not convert a benchmark into a promise about unseen genres or future model releases.

Commercial superiority should mean a demonstrated improvement on selected dimensions for a specified user segment. It should not mean winning every dimension: a professional editor may prefer direct timeline control; a musician may value musical synchronization over dialogue; an enterprise buyer may prioritize governance and repeatable updates. The simple chat workspace can serve these users through different evidence and strategies without requiring different Director architectures.

## Findings, changes and remaining work

The pre-edit matrix identified two MEDIUM evidence issues: stale source coverage for the 2.5 profile, and missing market/feasibility evidence separating architecture from live performance. Minimal fixes are this report, an update to `evidence/SEEDANCE_KNOWLEDGE_STATUS.md`, and primary-source pointers in the two Seedance profiles. No normative schema, task order, capability enum, product behavior or paid policy changes are warranted by this evidence alone. `SPEC_VERSION` remains 4.3.1 because this change does not redefine a contract.

Remaining empirical work includes exact model/provider/account entitlement; current pricing and billing certainty; practical reference ceilings; language and identity acceptance; complex action and continuation reliability; local-edit preservation; calibrated QA; cost/latency distributions; and comparative user effort. The repository contains no measured market-win result. Direct user interviews across niches and legitimate hands-on competitor evaluations would improve the evidence; the current representative desk study is not that research.

Specification verdict retained: **READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS**. This is readiness to proceed through the existing implementation gates. Commercial release and a claim of superiority remain unproven. If a release explicitly requires a capability that its chosen route cannot demonstrate, that capability is a release blocker, even though it was a non-blocking unknown when starting implementation.

## Verification of this evidence refresh

Offline governance validation passed 3,592 assertions, including 43 JSON Schema metaschemas, 242 local reference checks and 85 contract fixtures. All 22 governance mutation tests passed. The final diff passed whitespace checks; 253 inventory paths and non-self-referential hashes were reconciled. These are specification checks, not live provider or comparative product tests.

## Source ledger

All sources accessed 2026-09-09. Unless a publication date is stated, these are live pages with no stable publication date established in this review. Vendor descriptions are attributed claims; they do not establish actual account access or acceptance rates.

- [S1] Topview, *AI Video Agent for Short Films & Marketing Videos*. https://www.topview.ai/
- [S2] Higgsfield, *Which Higgsfield Tool Should You Use*. https://higgsfield.ai/creator-hub/help-center/tools/which-higgsfield-tool-should-i-use
- [S3] Runway Help Center, *Building and running Workflows with Agent*. https://help.runwayml.com/hc/en-us/articles/53645211363475-Building-and-running-Workflows-with-Agent
- [S4] LTX Studio, *The Creative Studio for AI Video Production*. https://website.ltx.studio/
- [S5] Google, *Flow*. https://labs.google/fx/tools/flow
- [S6] HeyGen, *AI Video Translator*. https://www.heygen.com/translate
- [S7] Synthesia, *Create AI Training Videos*. https://www.synthesia.io/learning-and-development
- [S8] Creatify, *Convert Any URL Into a Video Ad*. https://creatify.ai/features/url-to-video
- [S9] Descript, *AI Video Editor*. https://www.descript.com/
- [S10] OpusClip, product homepage. https://www.opus.pro/
- [S11] Neural Frames, product homepage. https://www.neuralframes.com/
- [S12] Adobe, *Extend video length with Generative Extend*. https://www.adobe.com/uk/products/premiere/extend-video.html
- [S13] Krikey AI, *AI Animation App*. https://www.krikey.ai/
- [S14] Ian Dean / Creative Bloq, interview with Kévin Mendiboure, *How a filmmaker turned a 10-year-old unmakeable movie idea into reality with AI*, 2026-06-09. https://www.creativebloq.com/ai/how-a-filmmaker-turned-a-10-year-old-unmakeable-movie-idea-into-reality-with-ai
- [S15] Seedance Team, *Seedance 2.0: Advancing Video Generation for World Complexity*, arXiv:2604.14148, 2026-04-15. Abstract/report metadata inspected; no claim of a full paper reproduction. https://arxiv.org/abs/2604.14148
- [S16] ByteDance Seed, *One-take Creation, Flexible Referencing: Introducing Seedance 2.5*, 2026-07-31. https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- [S17] BytePlus ModelArk, *Create a video generation task*, page shell updated 2026-09-08. Search extract mentions 2.5; complete request contract not retrieved. https://docs.byteplus.com/en/docs/ModelArk/1520757
- [S18] BytePlus ModelArk, *Video generation tutorial*, page shell updated 2026-09-08. Search extract mentions 2.5; full body unavailable in this retrieval. https://docs.byteplus.com/en/docs/ModelArk/2298881
