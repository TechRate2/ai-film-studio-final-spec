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

## DurableJob transition table
The sole production status vocabulary is the enum above and `schemas/job.schema.json`.

| From | Allowed next | Guard/effect |
|---|---|---|
| PLANNED | READY, BLOCKED, CANCELLED | Valid dependencies and input versions; cancel before submission |
| READY | AUTHORIZED, BLOCKED, CANCELLED | Resolve capabilities/rights; bind authorization or non-paid policy |
| AUTHORIZED | SUBMITTING, BLOCKED, CANCELLED | Atomic lease, version check and spend reservation |
| SUBMITTING | RUNNING, RECONCILING, FAILED, CANCEL_REQUESTED | Persist provider task; ambiguous outcome reconciles |
| RUNNING | SUCCEEDED, FAILED, RECONCILING, CANCEL_REQUESTED | Poll/recover same task; persist output before success |
| RECONCILING | RUNNING, SUCCEEDED, FAILED, CANCEL_REQUESTED, BLOCKED | Authoritative upstream evidence; unresolved certainty never resubmits |
| CANCEL_REQUESTED | CANCELLED, SUCCEEDED, FAILED, RECONCILING | Provider confirms cancel or late completion; no assumed refund |
| BLOCKED | READY, RECONCILING, CANCELLED | Revalidate prerequisites; UNKNOWN resumes reconciliation only |
| SUCCEEDED, FAILED, CANCELLED | none | Terminal job immutable; any permitted retry gets a new linked job |

FAILED_UNBILLED_CONFIRMED may allow a new execution record under the same logical candidate and authorization. No status transition back to SUBMITTING exists after possible creation. A new execution after a billed/output result requires a newly authorized candidate/revision. Cancellation stops unsubmitted siblings immediately; late output is retained and cost reconciled without releasing dependent children. Bounded polling exhaustion leaves unresolved liability reserved and visible; it is not evidence of unbilled failure.

## Machine-checkable invariants
```json
{
  "job_status": [
    "PLANNED",
    "READY",
    "AUTHORIZED",
    "SUBMITTING",
    "RUNNING",
    "RECONCILING",
    "SUCCEEDED",
    "FAILED",
    "CANCEL_REQUESTED",
    "CANCELLED",
    "BLOCKED"
  ]
}
```
