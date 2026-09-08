# Test and Evaluation Strategy

## Layers
1. schema/contract tests
2. pure domain unit tests
3. repository/service integration tests
4. orchestration/job/idempotency tests
5. UI/API behavioral tests
6. golden scenario tests
7. opt-in real-provider smoke/benchmark tests

## Deterministic tests
Use fixtures/test doubles only in test environment. Never create production fallbacks that return fake generated media.

## Critical invariants to test directly
- dependent child cannot run before accepted parent;
- character cannot use unknown canon fact;
- reference negative scope is preserved through compiler;
- subtitle/audio-only changes do not stale unaffected raw video;
- rejected QA does not submit another paid generation;
- uncertain submission enters reconciliation rather than blind retry;
- shot revision preserves old version and downstream stale propagation is selective;
- external keyframe mode makes no internal image-generation call;
- provider switch does not change Director creative logic.

## Golden scenarios
Every task declares affected GS IDs. CI runs non-paid deterministic portions. Paid smoke tests require explicit credentials/budget gate and never run by default on every commit.

## Model benchmarks
Record scenario, exact profile/compiler/provider versions, inputs, seed/options where available, raw output IDs, human/automated scores, cost, latency and accepted seconds.

## Regression policy
A known accepted behavior becoming materially worse blocks release unless documented/owner-approved with evidence.
