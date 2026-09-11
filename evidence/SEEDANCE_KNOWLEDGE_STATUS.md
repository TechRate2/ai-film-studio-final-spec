# Seedance Knowledge Status

## Current provider-document refresh, 2026-09-11

The complete public AtlasCloud reference-to-video request pages were retrieved for [2.0](https://www.atlascloud.ai/docs/more-models/bytedance/seedance-2.0-reference-to-video/generateVideo) and [2.5](https://www.atlascloud.ai/docs/more-models/bytedance/seedance-2.5-reference-to-video/generateVideo). This supersedes the earlier retrieval limitation for this provider only. Both pages are documentation evidence, not account execution proof.

For 2.5, the page distinguishes reference/edit/extend operations. Prompt-implied operation must agree with parameters; an explicit hint can catch parameter errors before task creation but does not prevent later prompt disagreement. Editing requires one source video, adaptive aspect and duration -1. The page identifies 4k-esr as enhancement of native 1080p, not native 4K. These are provider-scoped compiler facts, not inherited 2.0 behavior or measured quality.

For 2.0, the separate page describes 4–15-second requests, up to nine images/three videos, and audio references requiring visual input. It warns that a repeated seed does not guarantee identical results. Parameter names and exposure must be checked independently for each version.

[Billing documentation](https://www.atlascloud.ai/docs/billing/model-billing) describes a non-generating calculate endpoint with account-adjusted estimates; token-billed video settles on actual output. An estimate is not an upper bound. [Failure documentation](https://www.atlascloud.ai/docs/billing/refunds) describes release on terminal provider failure; a local timeout is not proof of that terminal state. Preserve spec/44 reconciliation and bounded liability.

Account entitlement, immutable deployed version, current account price, Vietnamese dialogue quality, practical reference ceiling and accepted-second reliability remain UNKNOWN here. Zero project samples were generated. No bundled runtime claim is promoted; model profiles remain independent, PARTIAL and non-routable. TASK-030, spec/37 and the provider expansion template must qualify actual routes before use.

## Source inspection, 2026-09-08
Inspected `https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills/blob/main/skills/seedance-2-5-skill/references/model-profile.md`, returned Git blob `3b9ba23388da5d58777c1ec9ae573ea69f4e1fed`.

The source reports Seedance 2.0 experiments and documentation claims dated 2026-08-03. It describes reference binding, timing drift, composition conflict and overloaded-event omissions. It does not establish this project's exact provider/account/endpoint or a complete inspectable sample ledger. Therefore the bundled profile is PARTIAL, its runtime claims remain UNKNOWN and it is not routable. Prior MEASURED labeling overstated what the repository could substantiate. Do not turn the reported event-count anecdote into a fixed generation ceiling or discard hard composition constraints because an image is reported to dominate text.

The same source explicitly labels Seedance 2.5 behavior unmeasured and separates announced features from executable exposure. The 2.5 profile remains independent and non-routable. Launch claims do not establish endpoint availability, pricing, reference ceilings, audio control or reliability.

No paid sample or account entitlement was tested during this audit. Integration must inspect exact current provider docs and run explicitly authorized probes through Durable Jobs/PaidAttemptGuard. Record model/provider/account scope, source versions, sample count, input/output hashes and failures before promotion. Historical source inspection is not an API guarantee.

## Primary-source refresh, 2026-09-09

Seedance 2.0 now also has a primary-source pointer to the Seedance Team technical report, `https://arxiv.org/abs/2604.14148` (2026-04-15). Its reported scope does not establish this project's current endpoint or overwrite the existing claim-local third-party provenance.

The official Seedance 2.5 announcement was inspected at `https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5`, publication date **2026-07-31**. It describes longer generation, expanded references and targeted editing. These are model-native announced capabilities, not this project's measurements. The profile gains a primary-source pointer, not a runtime support promotion.

The announcement's API-coming-soon wording is historical. Newer search extracts for `https://docs.byteplus.com/en/docs/ModelArk/1520757` and `https://docs.byteplus.com/en/docs/ModelArk/2298881` mention 2.5, but opening the pages returned only JavaScript shells (updated 2026-09-08). Current exact API/model-ID availability and account entitlement remain unresolved here. Do not assert current API absence from the old launch article or infer a callable request contract from a search snippet.

Both profiles remain PARTIAL, non-routable and independent, with UNKNOWN runtime claims and zero project samples. Profile-level source discovery does not replace claim-local evidence, and inspection time does not imply model verification. See `evidence/MARKET_FEASIBILITY_REVIEW.md` for market context, limitations and the proposed comparative evidence plan. This refresh spends no credits and does not complete TASK-030 or qualify 2.5.
