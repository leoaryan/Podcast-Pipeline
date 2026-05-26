---
title: "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time"
channel: "SemiAnalysis"
guest: ""
published: 2025-08-20
analyzed: 2026-05-26
duration_minutes: 45
topics: [engineering]
source_url: "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/"
---

### 1) Core thesis
GB200 NVL72 needs a 1.6x performance advantage over H100 just to break even on TCO, and reliability problems plus immature software mean no one is running frontier-scale training on it yet — H100 remains the only viable NVIDIA GPU for mega training runs as of mid-2025.

### 2) Claim and Evidence

- Claim: H100 software improvements alone delivered 57% better training throughput over 12 months with zero hardware changes.
- Evidence: GPT-3 175B BF16 MFU went from 34% (Jan 2024) to 54% (Dec 2024). FP8 MFU rose from 29.5% to 39.5% in the same window. Cost to train GPT-3 on 300B tokens dropped from $218k to $162k.
- Strength: strong — reproducible benchmark data across 128 H100s with specific software version tracking, directly from NVIDIA's DGX Cloud Benchmarking scripts on EOS cluster.

- Claim: GB200 NVL72 is not yet usable for frontier-scale training due to reliability and software immaturity.
- Evidence: "Even the most advanced operators at frontier labs and CSPs are not yet able to carry out mega training runs on the GB200 NVL72." NVLink copper backplane remains unreliable; diagnostic and debugging tools for backplane errors are "behind and sub-optimal."
- Strength: strong — SemiAnalysis has direct operator feedback; this isn't speculation but reported operational reality.

- Claim: Scaling GPU count for smaller models (Llama3 70B) shows meaningful MFU degradation due to communication overhead.
- Evidence: FP8 MFU drops 10% going from 64 H100s (38.1%) to 2,048 H100s (35.5%). BF16 drop is only 1-2%, suggesting the communication bottleneck hits lower-precision workloads harder.
- Strength: moderate — data is solid but the root cause analysis is observational; the parallelism configuration (TP=4, PP=2, CP=2) is held constant so the degradation source isn't fully isolated.

- Claim: Llama 3 405B pretraining cost of ~$29M for a single run dramatically exceeds MoE alternatives like DeepSeek ($5M).
- Evidence: BF16 cost of $1.95 per million tokens × 15T tokens = $29.1M. This is 5.8x DeepSeek's publicly stated training cost.
- Strength: strong — straightforward multiplication from benchmarked throughput and known token counts.

- Claim: AI training energy consumption is socially significant but dwarfed by the cost of experiments and failed runs.
- Evidence: GPT-3 175B training = 19 US households' annual energy (FP8). Llama 3 405B = 3,400 households. But "many experiments and many failed training runs" are the real driver of ballooning energy growth.
- Strength: moderate — the household analogy is vivid but obscures that 3,400 households is still a rounding error on US total consumption (~127M households).

### 3) Mechanisms
SemiAnalysis operates with a cost-efficiency lens: the fundamental metric is performance per TCO dollar. They decompose TCO into capex (server + networking + storage) and opex (power), then benchmark actual throughput to produce a cost-per-token figure. The implicit causal model is that GPU buyers are rational economic actors who will benchmark, compare, and negotiate based on these numbers. The article treats software maturity as a predictable learning curve — CUDA/CuDNN/CuBLAS/NCCL optimizations compound over ~24 months post-launch — and treats hardware reliability as an engineering problem that will be solved on a roughly similar timescale. One unstated assumption: that GB200 NVL72's problems are "normal" for a new architecture and not a sign of fundamental design flaws in the copper backplane approach.

### 4) Concrete actions
- If negotiating GPU contracts now: demand pricing at least 10-20% below market average if a provider's MFU benchmarks below reference numbers (e.g., GCP a3-mega was 10-20% worse than average for Llama 70B).
- Use the published TCO numbers ($1.42/hr/GPU H100 baseline, GB200 NVL72 ~1.6x TCO/GPU) as negotiation anchors.
- Plan training budgets assuming 34-57% throughput improvement from software alone over the first year of a new architecture — don't overpay for raw hardware expecting static performance.
- For LLM training project planning: benchmark your specific model at your target cluster size. MFU scales differently for dense vs. MoE, small vs. large models, and FP8 vs. BF16.

### 5) Delta vs prior episodes
(first episode from this channel)

### 6) Red flags
- The article is self-serving: SemiAnalysis sells a ClusterMAX rating system, a Datacenter Industry Model, and Core Research subscriptions. The benchmarking methodology section is framed as a public good while being a product pitch.
- The three "recommendations to NVIDIA" are presented as neutral analysis but position SemiAnalysis as an industry arbiter with standing to demand transparency from NVIDIA — a notable presumption.
- The comparison of Llama 3 405B ($29M) to DeepSeek ($5M) ignores that DeepSeek's $5M figure is widely doubted and likely excludes substantial R&D compute. The article doesn't caveat this.
- No independent verification of GB200 NVL72 reliability claims — all sourced from unnamed "operators" at CSPs and frontier labs. These could be competitors with incentives to downplay Blackwell readiness.

### 7) Open questions
- Will GB200 NVL72 reliability improve enough for frontier training by end of 2025 as claimed, or is the copper backplane a dead-end architecture?
- What is the actual MFU degradation curve beyond 2,048 GPUs? The article hints at further drops but doesn't benchmark at 16k+ GPU scales where frontier training actually happens.
- How does the cost comparison shift when factoring in the engineering time lost to GB200 debugging and reliability workarounds — the article acknowledges this exists but doesn't quantify it.
