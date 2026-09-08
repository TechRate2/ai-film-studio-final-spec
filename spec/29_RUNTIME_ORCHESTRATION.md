# Runtime Orchestration

## Two planes
**Director plane:** adaptive reasoning, research, planning, tool selection and user-facing explanation.  
**Production plane:** explicit typed state machines, durable jobs, dependencies, cost authorization, provider transport and artifact persistence.

Creative reasoning may be agentic; billable production execution is never an opaque LLM loop.

## Director run state
A run persists request/project IDs, current objective, plan/artifact refs, active task/tool state, decision records, context-pack version and checkpoint summary. Chat transcript may be an input but is not durable source of truth.

## Session resume and compaction
Long sessions periodically compact conversational/reasoning history into durable structured artifacts + concise checkpoint summaries. Compaction must preserve IDs/source versions/unresolved decisions rather than free-form paraphrase alone. A new process/model session reconstructs from Project Canon, ActiveContextPack, artifacts/jobs and checkpoint state; it must not require hidden model memory or the entire historical transcript.

## Bounded agent loops
Research, creative critique, planning and repair reasoning have explicit budgets/stop conditions. If a loop cannot converge, it transitions to targeted research, WAITING_USER, BLOCKED or a documented trade-off; it does not spin indefinitely.

## Production job state
`PLANNED | READY | AUTHORIZED | SUBMITTING | RUNNING | RECONCILING | SUCCEEDED | FAILED | CANCEL_REQUESTED | CANCELLED | BLOCKED`.

## Scheduler
Jobs run only when dependencies, authorization, capability and spend conditions are satisfied. Independent jobs may parallelize; dependency edges constrain children.

## Resume
After restart, recover from durable jobs/upstream task IDs. Events accelerate UI updates but durable state remains authoritative.

## Cancellation
Cancel prevents not-yet-submitted work immediately; submitted provider work follows provider cancel/reconcile semantics and never assumes refund/cancellation unless confirmed.
