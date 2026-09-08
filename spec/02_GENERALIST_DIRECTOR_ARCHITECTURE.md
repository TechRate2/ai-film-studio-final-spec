# Generalist Director Architecture

## One visible brain
```text
USER INPUT + ATTACHMENTS
        ↓
UNDERSTAND / SCOPE
        ↓
REFERENCE ANALYSIS
        ↓
RESEARCH NEED / EVIDENCE
        ↓
AUDIENCE + RETENTION
        ↓
CREATIVE STRATEGY
        ↓
STORY / MESSAGE
        ↓
CHARACTER / CANON / DIALOGUE
        ↓
PERFORMANCE / BLOCKING
        ↓
CINEMATOGRAPHY / AUDIO / EDITORIAL
        ↓
PRODUCTION STRATEGY
        ↓
SCENE COMPLEXITY / DEPENDENCIES
        ↓
REFERENCE + KEYFRAME STRATEGY
        ↓
UNIVERSAL GENERATION SPEC
        ↓
MODEL INTELLIGENCE + COMPILER
        ↓
PROVIDER ADAPTER
        ↓
PAID ATTEMPT GATE
        ↓
GENERATE → QA → ACCEPT/REVISE
        ↓
FINAL ASSEMBLY
        ↓
OUTCOME/TASTE LEARNING
```

## Director responsibilities
- infer objective, audience and constraints;
- choose adaptive scope depth;
- decide which uncertainty merits research;
- retrieve relevant creative/model skills;
- produce structured artifacts rather than giant prose prompts;
- choose production method per scene;
- resolve dependencies;
- compile model-specific prompts;
- control spend;
- surface review points only when valuable;
- preserve state across sessions/episodes.

## Tool classes
Research/search, file/reference analysis, memory/canon retrieval, creative/story skills, image/video/voice providers, QA/vision evaluators, edit/FFmpeg, cost/benchmark registry and artifact/job scheduler.

## Agentic vs deterministic boundary
Creative decisions may be LLM-driven and adaptive. Once a paid production plan is approved, execution is represented by explicit typed jobs, state transitions and dependency graphs.
