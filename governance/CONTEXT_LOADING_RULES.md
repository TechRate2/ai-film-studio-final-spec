# Context Loading Rules

Large context is not automatically better context.

## Coding agent context
Always load: AGENTS + SPEC_LOCK + active task + task-linked docs/schemas + relevant repository code. Load other specs only when a concrete dependency is discovered.

## Runtime Director context
Build scoped ActiveContextPack from current request, active entities, relevant canon/relationships/knowledge, needed evidence/skills, current continuity and provider/model decision. Do not dump the complete project/series/research library.

## Handoff
At session end persist concise task/repository reality and exact unresolved blockers in repo/issue/PR, not in hidden model memory. A new coding session should be able to resume from committed artifacts.

## Conflict resolution
When two loaded docs appear contradictory, apply authority order rather than averaging them.
