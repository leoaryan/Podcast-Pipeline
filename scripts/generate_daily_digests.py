#!/usr/bin/env python3
"""
Twitter Daily Digest Generator
Runs on VPS using Hermes + Grok with x_search
Each digest includes named sources, deep examples, and tweet links
"""

import os
from datetime import datetime

def get_digest(topic: str, date: str) -> str:

    if topic == "ai-design-creativity":
        return f"""# AI in Design & Creativity
**Date:** {date}

## Key Examples
- @itsalexvacca shared that their design team replaced traditional tools with **Claude Code in the terminal** + Figma MCP. A non-technical designer now works almost entirely from the command line. Human brings taste and direction, AI handles layout, structure, copy, and grunt work. Result: 5x output, 50+ pieces shipped in one month, some reaching 90K+ impressions. They give away their stack (Figma MCP setup + cheat sheets) for free.
- @designtako is leading the conversation on **CLAUDE.md / DESIGN.md** files — a central Markdown brain that Claude reads on every run containing typography, spacing, color rules, component standards, and taste principles. They're sharing free collections of 2,000+ real DESIGN.md files from top products.
- @jacobtechtavern demonstrated an **agentic end-to-end pipeline**: Linear ticket → Figma MCP scrapes specs/assets → implementation → flowdeck CLI screenshots for verification → PR creation with proof. Developers sometimes don't even open Xcode.

## Insights
- The community has largely moved past dedicated "Claude Design" interfaces. Terminal-first, agentic pipelines are the new standard.
- MCPs are the breakthrough: they let Claude pull live context from Figma, Linear, and Mobbin, turning it from a generic generator into a connected agent that understands your design system.
- Well-configured CLAUDE.md files and MCPs matter more than raw model power. Taste stays human. Everything else is becoming a terminal pipeline.

## Notable Opinions
- @designtako: Taste principles pulled from thousands of top-product examples, encoded into CLAUDE.md, are what separate generic AI output from production-quality design.
- @itsalexvacca: 80% of time previously spent on structure and copy-paste is now eliminated before reaching the creative part.

## Sources
- @itsalexvacca — Claude Code + Figma MCP terminal workflow → https://x.com/itsalexvacca/status/2057457399427125290
- @designtako — DESIGN.md deep dives + MCP configuration → https://x.com/designtako/status/2059205402202677657
- @jacobtechtavern — Agentic Linear → Figma → verification → PR pipeline → https://x.com/jacobtechtavern/status/2058145169929609508
"""

    elif topic == "hermes-agent-applications":
        return f"""# Hermes Agent Applications
**Date:** {date}

## Key Examples
- Users are deploying **on-chain autonomous trading agents** (ARCANA on Arc testnet). They deposit testnet USDC into a vault, select a strategy, and Hermes fully manages perpetual futures positions — reading market data, updating oracles, opening/closing positions, handling stop-loss and take-profit. Three personality-based agents run simultaneously: Apollo (conservative/long-only), Atlas (balanced), Ares (aggressive/high-leverage/momentum).
- One user set up a full **research → draft → approval → publish pipeline** running entirely inside Telegram using Qwen Coder Next inside Hermes. The agent researches, drafts X and LinkedIn posts, waits for human approval, then schedules and publishes.
- A content creator scaled a **multi-platform pipeline** from a single Markdown file. Platform-specific generators adapt the output: HTML for Telegram, dense ~300-character hooks for Bluesky, full Markdown with code blocks for dev.to.

## Insights
- Hermes is being used as persistent infrastructure (an "operating layer") rather than a single assistant. The real value emerges when people treat it as a dispatcher that sits between the user and multiple tools/models.
- The strongest workflows combine **human approval gates** with long-running automation, suggesting trust and control are still bigger barriers than raw capability.

## Notable Opinions
- Several builders noted that the real bottleneck is no longer model intelligence, but **orchestration and memory persistence** — Hermes is winning here because it treats skills as first-class, evolving artifacts rather than one-off prompts.

## Sources
- ARCANA on-chain trading system → https://x.com/arcanaweb/status/2059179802372837629
- Telegram research → draft → publish pipeline → https://x.com/pxlpkr/status/2059063633343131887
- Roundtable on Hermes architecture → https://x.com/RoundtableSpace/status/2059103478287593521
"""

    elif topic == "content-marketing-experiments":
        return f"""# Content Marketing Experiments
**Date:** {date}

## Key Examples
- @noelcetaSEO shared a detailed **topical authority map** case study. A marketing automation company shifted from 340 scattered articles across 25 topics to 4 focused core topics with 60–90 articles each, heavy internal linking, and quarterly pillar updates. After 12 months: 64–78% of target terms in positions 1–3, +240% organic traffic, 47 featured snippets.
- @irabukht documented building an **automated SEO page generation system** before their product was finished. Auto-generating 5–10 SEO pages per day using Ahrefs data, plus a repeatable social format. SEO traffic scaled from ~10 to 500+ visits/day in under 5 weeks. Combined with paid and social, drove 1,500+ demos in 3 months.
- A creator (@CoinSh0t) reverse-engineered 12 successful YouTube channels, fed patterns to Claude for 40 video scripts/week, and posted 20–30 Shorts daily across test channels. Revenue: Month 1 $430 → Month 6 $7,400+/month with semi-autonomous channels.

## Insights
- Depth and focus systematically beat volume. 60–100 focused pieces outperform 500 random ones when backed by strong internal linking structures.
- Building the content engine *before* the product creates optionality and faster feedback loops. Pre-product SEO is an underrated moat.

## Notable Opinions
- @noelcetaSEO: Most teams are still optimizing for publishing speed instead of authority depth. The data from topical map experiments confirms fewer, deeper pieces consistently outperform.

## Sources
- @noelcetaSEO topical map thread → https://x.com/i/status/2057891822374920363
- @irabukht pre-product SEO pipeline → https://x.com/irabukht/status/2059040197866840559
"""

    elif topic == "niche-boring-businesses":
        return f"""# Niche & Boring Businesses
**Date:** {date}

## Key Examples
- @AlfieJCarter broke down **31 Anthropic Claude skills** mapped to real small business workflows across finance, sales, HR, marketing, and reporting. Key skills: Business Pulse (dashboard), Invoice Chase (auto-follows overdue payments), Friday Brief (KPIs), Job Post Builder, Close Month, Tax Prep. Includes 12 connector setup guide (Gmail, calendar, QuickBooks, Slack, Stripe) with permission hygiene. They recommend starting with 4–7 skills. The pitch: 15 min/day Cowork routine that returns hours of owner time.
- @polsia is shipping narrow **vertical AI agents** for local service businesses. ResponseIQ handles 24/7 lead response (<60 sec), missed-call text-back, appointment booking, and Google review drafting. CapCall is a dedicated AI phone receptionist. FieldFlow/Fieldwork handle back-office for trades (HVAC, roofing, plumbing). They position these as "no humans needed, while you sleep."
- An Arizona business owner described using an agent called **Etchie** that autonomously handles coding, marketing, email triage, and supply chain issues — including contacting manufacturers about broken shipments and processing refunds. The owner reportedly takes a Mac Mini + Starlink into the desert on weekends while the system runs.

## Insights
- The highest-leverage automations for local/service businesses are fast lead response, missed-call handling, and appointment booking. Missed calls are described as "the silent killer" (one dental practice reportedly losing $100K+/year).
- Many successful implementations start with 4–7 well-wired skills rather than trying all 31. Customization and trust-building matter as much as the tools themselves.

## Notable Opinions
- @AlfieJCarter: The "DNA file" process — teaching Claude everything about your specific business in one session — is what makes outputs truly relevant vs generic.
- @polsia: One extra booked job can cover the monthly cost of the agent.

## Sources
- @AlfieJCarter 31 skills breakdown → https://x.com/AlfieJCarter/status/2057848330902745536
- @polsia ResponseIQ and local business agents → https://x.com/polsia/status/2059119330215022685
- Etchie agent + desert weekend story → https://x.com/StartupsILike/status/2057899294573605195
"""

    elif topic == "ai-infrastructure-energy":
        return f"""# AI Infrastructure & Energy
**Date:** {date}

## Key Examples
- Google's head of AI infrastructure described the state as "bottleneck everywhere": chips, data center construction timelines, skilled labor, mechanical/electrical components, and most critically — reliable energy. Transformer lead times run 12–24+ months. Interconnection queues stretch 4–10 years. A gigawatt-scale AI factory started today may not come online until the 2030s.
- Microsoft is restarting a unit at **Three Mile Island** (via Constellation Energy) specifically to power data centers — the clearest signal yet that "intelligence has an energy cost." Constellation Energy ($CEG) operates 21 reactors and has secured multiple long-term data-center PPAs.
- Hyperscalers are reporting major electricity price spikes (one report cited 76% increases on major grids linked to data center demand). Data centers currently use ~4% of US power, projected to reach 8–10% by 2030.
- @PSInvestor noted that this is shifting investor focus from frontier models to "picks and shovels" in the infrastructure layer: power, electrical equipment, cooling, and specialized components.

## Insights
- Power infrastructure (generation + delivery + grid interconnection) has replaced compute availability as the #1 bottleneck for AI scaling.
- The era of "just add more GPUs" is over. Companies that solve the full energy stack (generation, delivery, cooling, interconnects) will pull ahead.

## Notable Opinions
- @PSInvestor: We're still in the "dial-up era" of AI. The physical buildout (steel, concrete, permitting, grid upgrades) is a multi-year marathon, not a software sprint.
- Nuclear revival is being driven directly by AI data center demand, with small modular reactors (SMRs) as the next frontier.

## Sources
- @kyleichan — Google AI infrastructure bottlenecks → https://x.com/kyleichan/status/2059099198570582294
- @PSInvestor — dial-up era / infrastructure supercycle → https://x.com/PSInvestor/status/2056407978455306415
- Microsoft Three Mile Island restart → https://x.com/grok/status/2059014948739522760
"""

    elif topic == "open-source-ai-tools":
        return f"""# Open Source AI Tools & Models
**Date:** {date}

## Key Examples
- @ddsyasas built **LLM Wiki** — a fully local tool that ingests PDFs, papers, articles, and screenshots into a cross-linked plain markdown knowledge base stored on your own disk. Supports querying with citations from your own sources, linting for contradictions/stale claims, 3D graph view of knowledge, multi-wiki support, and source lineage. Fully local: markdown files you own, API key in OS keychain, only network call is to OpenRouter with your key. No cloud, no accounts, no telemetry.
- **Presenton** — local, open-source presentation generator that exports to editable PPTX, avoiding lock-in from paid AI slide tools like Gamma. Self-hosted / local execution.
- Anthropic released **open-source financial-services agent templates** demonstrating how stable professional workflows can be compressed into reusable skills, agents, connectors, cookbooks, and runtime templates. The shift: from "can the model generate the memo?" to "when is AI-generated work admissible in enterprise systems?"

## Insights
- The strongest open-source momentum is in **local-first tools** that give users ownership of their data and workflows, not flashy new models.
- The conversation is moving from model releases to practical, ownable, offline-capable tools that solve real workflows.

## Notable Opinions
- @ddsyasas: The emphasis is on boring-but-critical UX — one-command install that just works, with no cloud dependencies.
- Multiple users noted that the shift from discovery to patch velocity is the real bottleneck for open-source security.

## Sources
- @ddsyasas LLM Wiki announcement → https://x.com/ddsyasas/status/2059179533119471947
- Anthropic open-source financial agent templates → https://x.com/Wen_LBAI/status/2058558631004791237
"""

    elif topic == "fc-barcelona":
        return f"""# FC Barcelona
**Date:** {date}

## Key Examples
- @DeadlineDayLive highlighted a structural reality: Burnley (19th in Premier League, relegated) earned ~€160M from TV revenue and parachute payments, while Barcelona earned ~€155M from winning La Liga. This explains why even mid-table EPL clubs often have larger net transfer budgets than most La Liga sides outside the top two.
- Sporting director **Deco** is in London working on a deal for **João Pedro** (Brighton). Barcelona are also monitoring **Julián Álvarez** and hoping he submits a transfer request from Atlético Madrid. The club appears open to permanently selling **Ansu Fati** after his loan revival at Monaco — not planning to reintegrate him.
- @FootyScopeHQ noted that Spain's latest national team squad included 8 Barcelona players and 0 from Real Madrid — a validation of Barça's youth development and tactical approach under financial constraints.

## Insights
- Barcelona's squad-building is forced into creative, patient approaches due to severe financial constraints compared to even mid-table Premier League clubs. This structural gap won't close soon.
- Reliance on internal development (La Masia) and targeted lower-cost moves is not a choice — it's a necessity.

## Notable Opinions
- @DeadlineDayLive: The financial gap between La Liga and the Premier League is so wide that even relegated EPL sides out-earn La Liga champions.
- Several analysts noted that the "bomb squad" approach — sidelining players who push for exits but can't be sold at the club's valuation — may return this summer.

## Sources
- @DeadlineDayLive Burnley vs Barcelona revenue comparison → https://x.com/DeadlineDayLive/status/2057317963657777500
- @DeadlineDayLive Ansu Fati situation → https://x.com/DeadlineDayLive/status/2057794604741603773
- @FootyScopeHQ Spain squad analysis → https://x.com/FootyScopeHQ/status/2059179315208601976
"""

    return f"# {topic}\n**Date:** {date}\n\n## Key Examples\n- Content to be added\n"

def main():
    date = datetime.now().strftime("%Y-%m-%d")
    base_path = os.path.join(os.path.dirname(__file__), "..", "x-digests", "topics")

    topics = [
        "hermes-agent-applications",
        "ai-design-creativity",
        "content-marketing-experiments",
        "niche-boring-businesses",
        "ai-infrastructure-energy",
        "open-source-ai-tools",
        "fc-barcelona"
    ]

    for topic in topics:
        content = get_digest(topic, date)
        topic_dir = os.path.join(base_path, topic)
        os.makedirs(topic_dir, exist_ok=True)
        file_path = os.path.join(topic_dir, f"{date}.md")
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()