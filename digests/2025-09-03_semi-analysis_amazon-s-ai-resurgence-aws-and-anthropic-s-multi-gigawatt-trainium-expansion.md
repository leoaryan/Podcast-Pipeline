---
title: "Amazon's AI Resurgence: AWS & Anthropic's Multi-Gigawatt Trainium Expansion"
channel: "SemiAnalysis"
guest: ""
published: 2025-09-03
analyzed: 2026-05-26
duration_minutes: 35
topics: [business, engineering]
source_url: "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/"
---

### 1) Core thesis
AWS has been losing the AI cloud war to Azure and Google, but the multi-gigawatt Anthropic/Trainium buildout — with Anthropic effectively getting a custom silicon program through Annapurna Labs — will reverse that, pushing AWS back above 20% YoY growth by end of 2025.

### 2) Claim and Evidence

- Claim: AWS's underperformance in AI cloud is driven by its custom EFA networking being slower and harder to use than InfiniBand/Spectrum-X/RoCEv2.
- Evidence: EFA "still lags behind other networking options on performance" and user experience. AWS's time-to-market is slowed by customization requirements for Nvidia systems. ClusterMAX ratings show Azure, CoreWeave, Oracle, Nebius, and Crusoe all outperforming AWS for multitenant GPU clusters.
- Strength: moderate — the performance comparison is directional but no specific latency/throughput benchmarks are cited. ClusterMAX is SemiAnalysis's own product, creating a conflict.

- Claim: Anthropic is the clear outperformer in GenAI for 2025, with revenue surging from $1B to $5B annualized.
- Evidence: Year-to-date revenue growth cited as 5x. Claude 4 described as "by far the most capable model for software engineering." Anthropic raised ~$13B at $183B valuation.
- Strength: moderate — revenue figures are directional estimates, not audited. The $5B annualized figure hasn't been independently confirmed.

- Claim: Trainium2's memory bandwidth per TCO advantage makes it ideal for Anthropic's RL-heavy roadmap, even though it lags NVIDIA on raw FLOPs.
- Evidence: GB200 has 3.85x FP16 FLOPs advantage and 2.75x memory bandwidth advantage over Trainium2. But on TCO per TB/s of memory bandwidth, Trainium2 is "highly competitive." Anthropic's RL workloads are more memory-bandwidth-bound than FLOPs-bound.
- Strength: moderate — the TCO comparison is internally consistent but depends heavily on SemiAnalysis's proprietary cost assumptions, and the claim that RL is memory-bound more than FLOPs-bound is asserted rather than demonstrated with workload data.

- Claim: Anthropic is effectively getting a custom silicon program through Amazon's Annapurna Labs, making it (alongside Google DeepMind) the only lab with hardware-software co-design.
- Evidence: Anthropic "heavily involved in all Trainium design decisions" and "use[s] Amazon's Annapurna Labs as a custom silicon partner." They were involved in the launch of the new NeuronLinkv3 scale-up network and the Teton PDS system architecture.
- Strength: strong — this is a structural claim about the partnership, not a performance claim. The involvement in design decisions is specific and verifiable.

- Claim: Most of Anthropic's inference runs on Google Cloud TPUs, not AWS, because TPUs have "the world's best inference system."
- Evidence: Anthropic's cloud spending is over 2x smaller than OpenAI's, and a large share goes to Google Cloud. "Most of Anthropic's skyrocketing inference needs are served by Google Cloud."
- Strength: weak/strong — the TPU inference quality claim is strong (consistent with known TPU advantages for decode-bound inference), but the spending split between AWS and Google is inferred, not disclosed by either company.

### 3) Mechanisms
The causal model: AI cloud success = securing an anchor customer (market-maker) + competitive hardware TCO. Microsoft won because OpenAI committed exclusively to Azure. AWS lagged because EFA networking was worse and Anthropic split spending with Google. The future reversal depends on Trainium2 being "good enough" where it matters (memory bandwidth per dollar for RL training) even if it loses on peak FLOPs — a classic disruptive innovation play against NVIDIA's over-engineered high end. The mechanism for AWS resurgence: Anthropic's training spend shifts from Google to AWS as the 1.3GW+ of Trainium datacenters come online, while inference stays on Google TPUs.

### 4) Concrete actions
- If evaluating cloud providers for large-scale training: benchmark EFAv4 against InfiniBand and RoCEv2 on your specific model sizes before committing to AWS. Don't assume AWS's general cloud dominance translates to GPU/XPU workloads.
- If building an AI lab's infrastructure strategy: negotiate hardware co-design access with your cloud provider if you're committing at Anthropic's scale. The custom silicon advantage compounds.
- If investing in AI infrastructure: watch for AWS's Q4 2025 revenue growth crossing 20% YoY as the Trainium campuses come online — this is SemiAnalysis's key thesis test.

### 5) Delta vs prior episodes
(first episode from this channel)

### 6) Red flags
- This is an investment thesis disguised as analysis. SemiAnalysis explicitly called this "another out-of-consensus call" and references their Core Research service (for hedge funds) multiple times. The entire framing is about AWS stock performance.
- The claim that 1.3GW of datacenters are being built "for the sole purpose of serving Anthropic's training needs" is extraordinary and unverifiable — satellite imagery can show construction but not contractual commitments.
- The Trainium2 TCO comparison table is described but not shown — the actual numbers are behind a paywall. We're asked to trust the conclusion without seeing the data.
- The article downplays Trainium yield issues as "fairly standard for a new system" without quantifying their severity or impact on the timeline.
- Anthropic's $5B annualized revenue figure has no sourcing. Revenue claims for private companies are notoriously unreliable.

### 7) Open questions
- Will Trainium2 ramp actually meet the Q4 2025 timeline, or will yield and assembly issues push revenue recognition into 2026?
- Can Anthropic maintain its 2025 outperformance if the inference advantage comes from Google TPUs rather than AWS Trainium? The training/inference split means AWS's resurgence depends on Anthropic's training budget, not its total AI spend.
- What happens when the $13B Anthropic funding round is exhausted? The article implies more deals with AWS and Google, but doesn't model the burn rate.
- How does the introduction of Rubin CPX (prefill-specialized chips) change the competitive dynamics for Trainium2's memory bandwidth per TCO advantage?
