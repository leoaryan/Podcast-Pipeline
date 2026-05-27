---
title: "Scaling the Memory Wall: The Rise and Roadmap of HBM"
channel: "SemiAnalysis"
guest: ""
published: 2025-08-12
analyzed: 2026-05-27
duration_minutes: 45
topics: [engineering]
source_url: "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/"
---

### 1) Core thesis
HBM is the single most critical supply chain bottleneck in AI computing — its manufacturing complexity (TSVs, 3DIC stacking, specialized packaging) creates a structural oligopoly where SK Hynix dominates, and every AI accelerator roadmap depends on HBM scaling in layers, bandwidth, and stacks per package.

### 2) Claim and Evidence

- Claim: HBM supply is so concentrated that a single supplier dispute could take down the entire AI accelerator supply chain.
- Evidence: The Hanmi/SK Hynix dispute: Hanmi had 100% share of TC bonders at SK Hynix until Hynix ordered from Hanwha at a *higher* price. Hanmi retaliated by pulling field service teams. "Without service, it would be months if not weeks before Hynix was unable to ship its marquee products. Longer-term it would threaten the entire accelerator supply chain as Micron and Samsung would not quickly be able to fill the capacity void" [~line 81]. Hynix placated Hanmi with a small order to restore service.
- Strength: strong — this is a reported near-miss with named companies and specific tools. The dependency chain is specific and verifiable.

- Claim: HBM yields are "well below" what memory manufacturers are accustomed to, but high pricing makes it margin-accretive for SK Hynix and Micron — not Samsung.
- Evidence: For an 8-layer stack at 99% per-layer yield, total yield is ~92%. For 12-layer: ~87%. Hybrid bonding for 16+ layers introduces entirely new yield challenges. Samsung's yields are "even worse" than SK Hynix and Micron, and "ironically, their low yields tighten up the total DRAM wafer supply, leading to higher pricing" [~line 68].
- Strength: moderate — the yield math is simplified and absolute numbers aren't disclosed, but the directional claims about relative vendor positions are consistent with public reporting.

- Claim: Architecture follows memory: every generation of HBM capacity increase is immediately consumed by larger models, longer contexts, and bigger KV caches, ensuring HBM remains the bottleneck.
- Evidence: A100: 80GB HBM2E → Rubin Ultra: 1,024GB HBM4E. "Parkinson's Law" dynamic where "techniques once deployed to squeeze models into tight budgets... are relaxed as soon as new HBM space appears, until the memory wall is hit again and efficiency tricks must be rediscovered" [~line 129]. Most LLM inference is memory-bandwidth-bound, not compute-bound.
- Strength: strong — this dynamic is well-established in ML systems. Every major model release since GPT-3 has pushed context lengths and parameter counts to fill available memory.

- Claim: Hybrid bonding for HBM is perpetually "next generation" — the goalposts keep shifting, and JEDEC's relaxation to 775µm stack height makes it less urgent.
- Evidence: Samsung "promotes the most aggressive technology implementations in attempts to catch up, only to expectedly fail on execution" [~line 104]. HBM3E 12-high fits within 720µm with conventional bumps. JEDEC increased the limit to 775µm, buying time. TSMC's experience with hybrid bonding in logic took years to reach volume production despite clear performance benefits.
- Strength: moderate — the "goalpost shifting" claim is specific and consistent with public roadmap changes, but the economic analysis comparing hybrid bonding cost vs. yield loss is behind the paywall.

- Claim: China is building domestic HBM capacity aggressively, with CXMT's TSV capacity expected to match Micron's by end of 2025.
- Evidence: CXMT HBM2 8-high entering mass production H1 2025. $200B in planned semiconductor subsidies over 5 years, with "a material portion going towards HBM." Huawei's affiliates (XMC, SJSemi) developing parallel HBM capacity at R&D scale. Sanctioned HBM is still re-exported through intermediaries (CoAsia, Faraday, SPIL) where end users desolder and reclaim HBM from GPU packages [~line 86].
- Strength: moderate — CXMT's capabilities are hard to independently verify, but the re-export desoldering claim is specific. The subsidy figure is consistent with Chinese government announcements.

### 3) Mechanisms
The bottleneck cascades through three layers: (1) TSV tooling is the rate-limiting step converting DDR capacity to HBM — etch, deposition, plating, grinding, and bonding tools are specialized and supply-constrained. (2) Packaging (CoWoS, MR-MUF, TC bonding) is a second chokepoint where SK Hynix's proprietary MR-MUF process with NAMICS material gives them a thermal and throughput advantage over competitors' TC-NCF approaches. (3) The shoreline problem: HBM must sit adjacent to the compute die's edge, so more HBM stacks require either larger compute dies or architectural tricks (memory controller offload, repeater PHYs). The third-order effect: as accelerators scale to TB-scale HBM per chip, the BOM shifts heavily toward memory vendors, particularly SK Hynix, making NVIDIA's gross margins dependent on HBM pricing.

### 4) Concrete actions
- If modeling AI infrastructure supply chains: treat HBM bonder tool availability (Hanmi, Hanwha, ASMPT, Besi) as a leading indicator for accelerator production capacity — not just wafer starts.
- If evaluating accelerator roadmaps: Rubin Ultra's 1TB HBM4E target is ambitious but physically achievable within the relaxed 775µm JEDEC spec without hybrid bonding. Hybrid bonding is a 2027+ problem.
- For inference infrastructure planning: KVCache offload to DDR/NVMe is already standard practice — don't assume all context fits in HBM. Agentic workloads shift cache from NVMe to DDR due to write-cycle limits on NAND.
- If tracking China semiconductor progress: CXMT's HBM2 mass production in H1 2025 is the milestone to watch, not Huawei's lab-scale efforts. HBM2 is a generation behind but closes the capability gap for domestic AI accelerators.

### 5) Delta vs prior episodes
This is the earliest SemiAnalysis article in the digest archive. Later articles (Sep 2025) reinforce the memory-wall dynamic: the Rubin CPX piece builds on the same shoreline/bandwidth analysis to justify NVIDIA's prefill-specialized GDDR7 chip. The Amazon/Trainium article applies the same TCO-per-bandwidth framing to evaluate custom silicon. What's new here vs. later articles: the detailed HBM manufacturing process flow (TSV, bumping, MR-MUF vs. TC-NCF), the Hanmi near-disruption, and the China HBM re-export pathway are not revisited in subsequent digests. The later articles focus more on system architecture than memory supply chain.

### 6) Red flags
- This is a subscriber-gated article and the free portion ends mid-analysis: "The rest of this piece will discuss OpenAI's ASIC project, shoreline area challenges... custom base dies for HBM..." The most novel claims are behind the paywall.
- The "explosive bit demand" chart and all numerical forecasts reference SemiAnalysis's proprietary Accelerator Model — a paid product. Without the model, readers can't verify the demand projections.
- The Micron "30% lower power consumption" claim is presented as fact but noted as "yet to be verified" — this is a vendor marketing claim, not independently tested.
- The yield analysis is simplified to the point of being potentially misleading: "99% per-layer yield → 92% for 8-layer" ignores that yield is not independent across layers and that non-critical defects accumulate nonlinearly.
- The article is heavily supply-side focused (manufacturing process, vendor dynamics) with little analysis of what happens if demand shifts — e.g., if inference moves to smaller models or if algorithmic advances reduce KVCache pressure.

### 7) Open questions
- What happens if CXMT's HBM2 reaches volume production and China's domestic accelerators become competitive? The article notes HBM supply concentration as a vulnerability but doesn't explore the scenario where China adds meaningful supply.
- The article mentions custom base dies for HBM4 as "revolutionary" but the analysis is paywalled. What specifically changes — memory controller integration, PHY customization, protocol changes?
- Samsung's HBM qualification struggles are mentioned but not explained. Is this a process problem, a design problem, or a customer (NVIDIA) certification problem?
- How does the KVCache offload architecture hold up as models move to million-token contexts? The "prefill speed < transfer rate to DDR" assumption may break at extreme context lengths.
