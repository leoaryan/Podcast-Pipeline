---
title: "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck"
channel: "SemiAnalysis"
guest: ""
published: 2025-09-08
analyzed: 2026-05-26
duration_minutes: 50
topics: [policy-society, engineering]
source_url: "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/"
---

### 1) Core thesis
US export controls are working — China's AI chip production is HBM-constrained, not logic-die-constrained — but enforcement gaps (TSMC die banks, Samsung's pre-ban HBM dump, untargeted CXMT) mean China still has a runway. The HBM bottleneck will bite hard by end of 2025, cutting Ascend production from 805k units this year to ~300k next year unless smuggling or domestic CXMT ramp fills the gap.

### 2) Claim and Evidence

- Claim: Huawei stockpiled 2.9M+ Ascend dies from TSMC before/despite export controls, creating a "Die Bank" that sustains production through 2025.
- Evidence: "Huawei ended up receiving more than 2.9M Ascend die, which can be used for both 910B and 910C." This Die Bank "gets them through 2024 and 2025" and will run out within 9 months of the article date.
- Strength: strong — SemiAnalysis has a track record of semiconductor supply-chain intelligence. The specific quantity claim is sourced but inherently based on proprietary data.

- Claim: Samsung dumped 11.4M HBM stacks into China, including 7M in the one-month gap between the Dec 2, 2024 BIS announcement and the Dec 31 enforcement deadline.
- Evidence: "Samsung alone has directly provided 11.4 million stacks of HBM to China." Combined with other providers, "13 million stacks of HBM" entered China — enough for 1.6M Ascend 910C packages.
- Strength: strong — specific quantities, timeline, and mechanism identified. Samsung's incentive (excluded from Western AI supply chains) creates a clear commercial motive.

- Claim: SMIC is no longer the bottleneck; HBM is. SMIC could produce millions of Ascend dies with single-digit allocation percentages.
- Evidence: Conservative SMIC advanced-node capacity estimate: 45k wpm by end of 2025, 60k in 2026, 80k in 2027. "SMIC only needs small amounts, as low as single digit percentages, of allocation to produce more than a million die." Huawei is also building its own fabs operated by SiCarrier.
- Strength: moderate — wafer capacity and yield estimates are modeled, not observed directly. But the logic holds: if a fab can do 45k wpm, even 5% allocation at reasonable yields produces millions of dies.

- Claim: Without foreign HBM, China's domestic AI accelerator production collapses next year to ~300k Ascend 910Cs.
- Evidence: CXMT projected to produce only ~2M HBM stacks in 2026, sufficient for 250-300k 910C packages. CXMT's HBM production is nascent — they are still converting DRAM lines and lack key tooling.
- Strength: moderate — depends on CXMT ramp projections which could shift with tool stockpiling or yield breakthroughs. The directional claim (sharp production drop) is well-supported by the HBM inventory math.

- Claim: Chinese AI labs (DeepSeek, Alibaba, Moonshot) are compute-constrained, and more chip access would meaningfully accelerate their progress.
- Evidence: DeepSeek R1 received a major update "on a timeline that is like o1 → o3" despite compute limitations. DeepSeek V4 and multimodal models from Alibaba/Moonshot are delayed by scarce compute. "DeepSeek deliberately serving R1 at low speeds to users to preserve compute."
- Strength: moderate — the progress correlation with compute availability is directional but not a controlled experiment. The causality claim is plausible but not proven.

### 3) Mechanisms
The article's causal model is a three-layer bottleneck analysis: logic die production → HBM availability → networking/CPU. Export controls work by targeting the tightest layer. Currently, logic (SMIC capacity + TSMC Die Bank) is loose, HBM is the pinch point, and networking (scale-up switches made at TSMC via shell companies) is being stockpiled but not yet constrained. The implicit theory of export control effectiveness: controls slow the adversary's progress, they don't stop it — China adapts (SiCarrier fabs, CXMT ramp, stockpiling), but adaptation takes years, buying the US time. The article argues for dynamic escalation: tighten controls when domestic production capabilities cross thresholds, but don't preemptively ban chips (H20, B30A) that keep China on the US stack.

### 4) Concrete actions
- If making US export control policy: immediately entity-list CXMT (China's HBM champion, still not listed as of publication). Close the Samsung pre-enforcement gap by coordinating announcement + enforcement dates with allies.
- Close the TSMC shell company loophole — Huawei continues accessing 5nm for datacenter CPUs and networking switches. Require stronger KYC and end-use verification.
- Align Japan/Netherlands export controls simultaneously with US announcements to prevent rush-order stockpiling. Japanese WFE vendors with >40% China revenue share have strong incentives to exploit gaps.
- If investing in AI hardware: model China's Ascend capacity as sharply declining in H1 2026 unless CXMT accelerates or smuggling volumes are significant. This constrains Chinese model deployment capacity.
- Do not ship B30A (Blackwell China SKU) to China — it has >10x the FLOPs of H20 and would "bail them out until domestic production ramps." Only raise the shipped chip quality when China can independently produce something competitive to H20E in volume.

### 5) Delta vs prior episodes
(first episode from this channel)

### 6) Red flags
- The article is an explicit policy advocacy piece dressed as analysis. "The Trump administration needs to solve this failure from the Biden administration immediately" and "By no means should HBM be allowed to be shipped into China" are policy demands, not analysis.
- SemiAnalysis has a commercial interest: their Core Research service sells supply-chain intelligence to investors betting on these exact dynamics. The more dramatic the constraints, the more valuable their proprietary data.
- The production forecasts (805k Ascends in 2025, 300k in 2026) are point estimates derived from models that are not fully disclosed. There's no sensitivity analysis or confidence intervals.
- The HBM smuggling narrative (Faraday + CoAsia) is presented as solved because "revenue numbers returning to normal" — but this is a single data point and the article acknowledges "this does not mean that HBM smuggling has stopped entirely."
- The claim that "export controls have been effective" is contradicted by the article's own data: 805k Ascends this year, a 59% increase from 507k in 2024. Effectiveness is framed as "it would have been worse without controls" — a counterfactual that can't be tested.

### 7) Open questions
- What is the actual yield curve for SMIC's 7nm-class process? The article uses conservative estimates but acknowledges this is the key sensitivity variable.
- Can CXMT accelerate HBM production faster than the 2M stacks estimate? The article acknowledges this is conservative — what would a bullish scenario look like?
- Is there a third path for Chinese AI accelerators that doesn't require HBM at all? The article dismisses GDDR/LPDDR as "not suitable for leading language models with modern reinforcement learning techniques" but doesn't explore whether architecture changes could make them viable.
- How much of the TSMC Die Bank was actually used for Ascend vs. other products? The 2.9M figure is for "Ascend die, which can be used for both 910B and 910C" — but die inventory can sit unused or be reallocated.
