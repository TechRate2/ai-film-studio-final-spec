# Runtime Orchestration

## Two planes
**Director plane:** adaptive reasoning, planning, research, tool selection and structured artifact creation.  
**Production plane:** deterministic/durable execution of approved plans, provider jobs, dependencies, retries of polling, QA and assembly.

Do not let an unbounded LLM loop directly own paid execution lifecycle.

## Director run
`CREATED → UNDERSTANDING → RESEARCHING? → PLANNING → PREFLIGHT → WAITING_INPUT/READY → COMPLETED|FAILED|CANCELLED`

Each transition is persisted enough to resume safely.

## Media job
`PLANNED → COSTED → AWAITING_APPROVAL? → QUEUED → SUBMITTING → SUBMITTED → POLLING → SUCCEEDED|FAILED|CANCELLED|RECONCILING`

`RECONCILING` is mandatory when local submission outcome is uncertain but provider may have created a billable task.

## Dependency scheduler
A child is runnable only when all required parent dependencies are accepted/current and spend/provider constraints permit execution. Independent DAG branches may parallelize.

## Checkpoints
Human input is required when: user explicitly chooses revision, external keyframe is requested, spend policy requires approval, an important degrade needs consent, or canon conflict cannot be safely inferred.

## Resume
On restart, reconstruct from durable state and provider upstream IDs. Never restart from chat transcript alone.

## Cancellation
Cancellation stops not-yet-submitted work immediately and attempts provider cancellation where supported; it never lies about already-spent cost.
