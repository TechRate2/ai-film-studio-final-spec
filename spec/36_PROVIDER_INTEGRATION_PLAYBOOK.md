# Provider Integration Playbook

## Integration sequence
1. inspect official provider API/billing/error docs;
2. create ProviderProfile with freshness and unknowns;
3. map provider model names to canonical ModelProfile identities;
4. implement transport adapter only;
5. implement submit/status/cancel/result normalization;
6. persist upstream task ID immediately when returned;
7. define timeout/reconciliation behavior;
8. add cost estimator and spend guard integration;
9. run capability probes and golden smoke tests;
10. expose provider only after required capability/reliability gates pass.

## Adapter boundary
Provider adapter handles auth, transport, serialization, polling/webhooks, rate limits and billing metadata. It does not decide story, camera, shot boundaries or model prompting strategy.

## Capability exposure
A provider may expose only a subset of a model's theoretical capabilities. ProviderProfile is authoritative for endpoint availability; ModelProfile is authoritative for measured behavior where scope matches.

## Failure handling
Normalize transport/provider errors into structured retryability and paid-state certainty. Never translate ambiguous submission timeout into automatic resubmission.

## Pricing
Runtime price comes from verified provider configuration/profile. Evidence snapshots are not runtime billing truth.
