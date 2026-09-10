# Implementation handoff — one canonical entry

This guide operationalizes `spec/26_IMPLEMENTATION_GOVERNANCE.md`. It does not replace task packets, change product scope or claim perfect coding-agent compliance. The owner must separately request application implementation. During a specification audit, inspect these instructions without executing numbered application tasks.

## 1. Establish the two roots
Identify IMPLEMENTATION_ROOT and SPEC_ROOT as actual paths, plus the pinned canonical Git commit/tree and SPEC_VERSION. They may be the same root only if the owner intentionally chooses that layout. For a separate implementation repository, prefer one read-only pinned checkout/submodule under a clearly documented directory, such as vendor/ai-film-studio-spec. An exact versioned copy is acceptable if TASK-002 records the upstream commit and verifies content integrity; do not maintain several editable spec copies.

A link pasted into chat is not proof that every file is available. Confirm file access, manifest/index counts and required reading. Do not silently use a cached older zip. Resolve missing content before implementing the affected task. On adoption of a newer spec, diff revisions and identify affected tasks/schemas/migrations; old COMPLETE receipts are not automatically current under new requirements.

At IMPLEMENTATION_ROOT, install concise AGENTS.md and CLAUDE.md bridges that give the real SPEC_ROOT and explicitly require its AGENTS.md, SPEC_LOCK, this guide, implementation order and active task. Preserve legitimate existing project instructions and report conflicts instead of overwriting them. CODEX.md is supplementary; never assume its filename alone is automatically discovered. Inspect applicable nested/override instructions without exposing personal secrets. Root bridges must not auto-import the entire specification into every session.

Discovery proof: start a fresh coding-agent session from the actual working directory. Ask it to identify loaded instruction sources, canonical revision, active task, prerequisite status and the files it will read. Verify those paths/content rather than accepting a generic “I read everything.” Add a project CI check that root bridges and the pinned revision exist; separately run the canonical validator with its --root pointing to SPEC_ROOT. Do not run that validator against an unrelated application root or misinterpret it as application tests.

## 2. First run and environment ownership
Begin TASK-001 with a reality report. If no application exists, record an empty/absent implementation accurately; TASK-001 remains audit-only. TASK-002 establishes the canonical embedding, implementation evidence ledger, minimal repository tooling/CI and the choices needed for the subsequent foundation tasks. Later tasks implement product capabilities.

Before TASK-003, record a concise implementation-environment decision: existing stack or justified chosen language/framework versions, database/migration tool, package manager/lockfile, test runner, local/staging configuration and exact available bootstrap commands. Do not invent working start commands before application scaffolding exists. Mark later worker/storage/browser commands pending with the task that supplies them. Once present, document executable install/start/stop/test commands and verify them in a clean environment. Respect existing repo conventions where compatible.

Maintain one runtime readiness table, with operation, selected route/version, configuration variable names (no secret values), owner task, documentation/probe evidence, budget and readiness. Include Director LLM/structured tools, research/search, media ingestion/storage, image/video, ASR/TTS/alignment, deterministic assembly and observability. A coding assistant subscription is not proof of a runtime API credential. An aggregator's TTS listing is not proof of complete dubbing, diarization or a particular language.

AtlasCloud remains the intended initial candidate, subject to spec/36 integration gates. Qualify Seedance 2.0 and 2.5 independently; UNKNOWN cannot become supported by preference. Unavailable providers disable only affected paid paths; tests may use clearly isolated doubles. No fake production fallback. LLM/search/ASR and local compute can also cost money: record their authorization/budget separately from paid media. All real billable media obey TASK-032/033 prerequisites and existing spend policy.

## 3. Task selection and full-criterion receipt
Use governance/contract_index.json execution_order/depends_on together with tasks/00_IMPLEMENTATION_ORDER.md and phase gates. Select the next eligible incomplete task, not the next numeric ID. A prerequisite is accepted evidence, not a file existing or a checkbox ticked. Phase 5 uses the provider expansion template; Phase 3 re-verifies prior tasks. TASK-044 waits for TASK-043/Phase 6.

In the implementation repository keep one versioned task ledger and one receipt per task, with append-only evidence/history. Do not change the specification repository's implementation statuses merely to simulate progress. Receipt fields:
- task ID and canonical task path; spec commit/tree/version;
- implementation repository and tested commit/tree; later receipt-only commits may reference that tested tree;
- task state from governance/TASK_STATE_MACHINE.md, prerequisite task and phase evidence;
- **every** acceptance criterion, including non-checkbox prose, with exact quoted requirement or stable source location, implementation symbols/routes/migrations, test assertion and PASS/FAIL/NOT_RUN result;
- every mapped Golden subsection, deterministic vs required real-provider level and evidence; later integration obligations stay explicitly pending until their owning gate;
- command, environment/version, time, exit code and accessible sanitized log/report; actual media/sample IDs where required;
- review findings, unresolved blockers, known failures, changed files and next eligible action;
- spend used/remaining and outstanding submitted/uncertain upstream work, without credentials.

No screenshot alone proves persistence or cost safety; no passing unit test proves a user journey. UI tasks exercise browser interaction through API/domain/storage and relevant job/event boundaries, including loading/error/cancel/reload states. Test-only spies verify forbidden paid calls without replacing required real-provider proof. Reuse existing canonical schema fixtures and add implementation tests of relational/transactional behavior; never duplicate incompatible private wire shapes.

## 4. Resume, correction and promotion
At session start read the ledger, receipt, Git status/log and applicable instructions; reconcile claims with the current tree. Run the smallest existing baseline check relevant to the active capability. Resume incomplete work; do not redo accepted generation, drop blocked criteria or treat chat memory as evidence. A near-context-limit checkpoint records exact next actions and pending jobs. Mark partial commits explicitly; never merge/release them as COMPLETE merely because they are committed.

Changing relevant code, schema, dependencies or compiler/profile invalidates affected test evidence. Re-run only necessary tests plus required gates; preserve failed attempts/logs. A failed assertion is a defect to investigate, not permission to delete it. Reviewer findings are tied to the candidate diff; a material fix needs re-review of the affected finding. Preserve user changes and never reset the working tree merely to get green CI.

When every current task criterion passes, update task and requirement evidence accurately, make an acceptance checkpoint and report the next eligible task. Follow the session's authorization for continuing; do not infer unlimited paid tests or platform permissions from “build all.” Stop for actual blocking inputs/access/budget, with the concrete blocker and completed evidence. A new session can then resume without an architect reconstructing the conversation.

## 5. Owner-facing handoff prompt
Use `prompts/MASTER_IMPLEMENTER_PROMPT.md` after supplying the actual implementation folder and this canonical checkout. Keep the original 46 task packets, safe dependency order and eight phase gates. Do not ask the agent to rewrite the product or digest the whole canonical tree on every step. The goal is demonstrated progress, not an unbounded run or a self-reported percentage.
