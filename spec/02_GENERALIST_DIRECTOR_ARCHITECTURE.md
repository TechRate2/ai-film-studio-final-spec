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

## Adaptive execution, not mandatory stages
The diagram is a capability map, not a fixed runtime pipeline. Skip satisfied or irrelevant work and reuse CURRENT artifacts. A subtitle correction can go directly to timeline validation; a simple B-roll request need not create a series, storyboard, research run or keyframe. Persist the selected prerequisite DAG and reason for material omissions. The Director requests compilation through neutral tools; it does not write vendor prompts or invoke transport. PaidAttemptGuard encloses the adapter submission, including image, voice and billable probe calls.

## Tool and run boundary
Each tool declares a versioned input/output schema, read/write scope, idempotency behavior and effect class READ_ONLY, DETERMINISTIC_WRITE or BILLABLE_GENERATION. Director suggestions cannot grant authorization. Production services validate permissions, input versions and spend independently. Persist run ID, optimistic revision, context-pack ID/version, pending command IDs, loop counters, deadlines and terminal reason before yielding. Failed tool calls do not reset budgets. No tool executes instructions extracted from a reference, web page or document as trusted commands.
