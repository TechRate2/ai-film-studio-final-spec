# Content Safety, Rights, Consent and Compliance

## Principle
Creative power does not bypass user consent, provider policy, applicable law or asset rights. Safety checks should be targeted and auditable rather than hidden blanket pipeline changes.

## Identity / voice
For real-person face or voice cloning/conditioning, store provenance/consent or the user assertion required by product policy. Higher-risk impersonation/deceptive contexts require stricter review. Do not silently convert one person's identity into another.

## Minors and sensitive contexts
Apply appropriate policy checks before generation/editing involving minors, sexual content, exploitation, severe abuse or other restricted categories. Block or require user correction where policy requires it.

## Copyright / brand / music
References may teach transferable mechanisms, composition/camera ideas and brand-approved rules, but do not automatically authorize copying protected characters, exact scripts, distinctive expressive sequences, logos or music. Track source/licensing metadata where relevant to commercial export.

## Product/factual claims
Do not infer medical, performance, price, certification or other material product claims from appearance alone. Claims come from user-provided/verified facts.

## Provider moderation
Provider safety/rejection responses are structured errors and must not be bypassed by hidden provider switching. A permitted alternate provider may be used only when the request itself remains allowed and capability/cost policy permits.

## Data lifecycle
Support project/media deletion semantics, credential revocation and retention policies. Deletion of persistent user content must propagate to owned media/derived artifacts according to policy while preserving only legally/operationally required audit metadata.

## Audit
Safety/rights decisions that block or materially alter production produce a `ContentSafetyDecision` with rule/category, affected artifacts and user-actionable next step.
