# Public Source Map

This records public sources inspected during architecture research. It does **not** claim access to private studio workflows.

## wanglongxiao/seedance-drama-maker — VERIFIED_SOURCE
https://github.com/wanglongxiao/seedance-drama-maker

Observed public patterns: structured character settings including voice/personality/background; scene definitions and persistent outfit/scene state; dialogue separated from visual description; variable scene duration by complexity; causal adjacent scenes; reference-role mapping into video prompts; a path attaching previous generated video as `reference_video`.

Architecture use: explicit scene/character state and causal handoff; this spec strengthens it with dependency scheduling, canon, revision versioning and cost guards.

## ArcReel — VERIFIED_SOURCE / REPO_REPORTED
https://github.com/ArcReel/ArcReel

Observed public patterns: content mode separated from video generation mode; drama workflow with character/scene/prop extraction, episode planning, structured script, assets, storyboard/reference route, video and final cut; review of costume/spatial relation/eyeline/movement direction; current/stale/missing/blocked artifacts; caution against unconditional retry/requeue; voice style/reference-audio concepts.

## HKUDS/ViMax — REPO_REPORTED + VERIFIED_SOURCE snippets
https://github.com/HKUDS/ViMax

Observed patterns: Idea2Video / Script2Video / Novel2Video; agent loop, session resume, artifact/storyboard previews; long-form reference/continuity/camera emphasis; reference selection and consistency logic.

## pengchengneo/AgentCine — REPO_REPORTED
https://github.com/pengchengneo/AgentCine

Observed patterns: Director agent + skills; observe/think/act/reflect; human checkpoints; short/long/episodic memory; deterministic pipeline option; consistency review and cost ceiling.

## waooAI/waoowaoo — VERIFIED_SOURCE / REPO_REPORTED
https://github.com/waooAI/waoowaoo

Observed patterns: assistant-driven workspace; reference uploads; model-aware aspect/duration/reference roles; first/last/reference modes depending on model; refine an existing result into a new version while retaining original.

## topviewai/ai-video-editor — REPO_REPORTED
https://github.com/topviewai/ai-video-editor

Observed public claims: upload/describe → script/hooks → AI editing → preview/adjust/export; large-scale ad/hook analysis is repository-reported, not independently verified.

## Wan-Video/Wan2.2 — VERIFIED_SOURCE
https://github.com/Wan-Video/Wan2.2

Observed official family capabilities include T2V/I2V/TI2V, speech-to-video and character animate/replacement. Architecture conclusion: a model family may have specialized routes, not one generic endpoint.

## AtlasCloudAI/awesome-seedance-2.5-prompts-skills — VERIFIED_SOURCE for inspected profiles
https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills

Architecture use: universal language / measured bias / capability separation; Seedance 2.0 staged timing/reference notes; Seedance 2.5 must be independently probed.

## Audit qualification
Earlier VERIFIED_SOURCE labels describe historical author-reported inspections; this repository did not pin those source commits or sample records. They are not evidence of current availability, pricing or this product's measurement. During the 4.3 audit only the exact Seedance profile source documented in evidence/SEEDANCE_KNOWLEDGE_STATUS.md was re-inspected. Other links remain historical provenance requiring revalidation for a material runtime decision. Synthesis conclusions do not grant rights or override SPEC_LOCK.
