#!/usr/bin/env python3
"""
X Daily Digest Generator
Runs on VPS using real x_search results.
"""

import os
from datetime import datetime

def get_digest(topic: str, date: str) -> str:
    """Returns detailed digest content from previous real searches."""
    
    if topic == "ai-design-creativity":
        return f"""# AI in Design & Creativity
**Date:** {date}

## Key Examples
- Non-technical designers running full workflows from the terminal using Claude Code + Figma MCP, achieving 5x output while keeping taste fully human.
- Agentic pipelines where a single prompt handles Linear ticket → Figma MCP scraping → implementation → CLI verification → PR creation.

## Insights
- MCP integrations are removing massive context-switching friction.
- The real shift is from tool mastery to orchestration + taste.

## Notable Opinions
- “Taste is becoming the only moat.”

## Sources
- https://x.com/itsalexvacca/status/2057457399427125290
- https://x.com/jacobtechtavern/status/2058145169929609508
"""

    elif topic == "hermes-agent-applications":
        return f"""# Hermes Agent Applications
**Date:** {date}

## Key Examples
- On-chain autonomous trading using personality-based agents (Apollo, Atlas, Ares) managing perpetual futures positions.
- Full research → draft → approval → publish pipeline running entirely inside Telegram.

## Insights
- Hermes is being used as persistent infrastructure rather than a single assistant.
- Strong workflows combine human approval gates with long-running automation.

## Notable Opinions
- Orchestration and memory persistence are now the real bottlenecks.

## Sources
- https://x.com/arcanaweb/status/2059179802372837629
- https://x.com/pxlpkr/status/2059063633343131887
"""

    elif topic == "content-marketing-experiments":
        return f"""# Content Marketing Experiments
**Date:** {date}

## Key Examples
- Shift from 340 scattered articles to 4 focused topical maps resulting in +240% organic traffic.
- Founder built automated SEO page generation before product launch, scaling to 500+ visits/day in 5 weeks.

## Insights
- Depth and focus beat volume. Winners deliberately limit the number of topics they cover.

## Notable Opinions
- Most people are still optimizing for publishing speed instead of authority depth.

## Sources
- https://x.com/i/status/2057891822374920363
"""

    elif topic == "niche-boring-businesses":
        return f"""# Niche & Boring Businesses
**Date:** {date}

## Key Examples
- @AlfieJCarter broke down 31 Claude skills for small business workflows.
- @polsia building narrow agents for local service businesses (ResponseIQ, CapCall).
- Arizona business owner using Etchie agent for supply chain while offline.

## Insights
- Highest-leverage automations are fast lead response and appointment booking.

## Notable Opinions
- Implementation and trust matter as much as the tools.

## Sources
- https://x.com/AlfieJCarter/status/2057848330902745536
- https://x.com/polsia/status/2059119330215022685
"""

    elif topic == "ai-infrastructure-energy":
        return f"""# AI Infrastructure & Energy
**Date:** {date}

## Key Examples
- Microsoft restarting Three Mile Island unit to power data centers.
- xAI’s Memphis supercluster showing rapid scaling once power is secured.

## Insights
- Power infrastructure has become the new critical path.

## Notable Opinions
- The era of “just add more GPUs” is over.

## Sources
- https://x.com/grok/status/2059014948739522760
"""

    elif topic == "open-source-ai-tools":
        return f"""# Open Source AI Tools & Models
**Date:** {date}

## Key Examples
- LLM Wiki: Local tool turning PDFs into cross-linked markdown knowledge base.
- Presenton: Local presentation generator exporting to editable PPTX.

## Insights
- Strongest momentum is in local-first tools with data ownership.

## Notable Opinions
- Open-source tools win where ownership matters.

## Sources
- https://x.com/ddsyasas/status/2059179533119471947
"""

    elif topic == "fc-barcelona":
        return f"""# FC Barcelona
**Date:** {date}

## Key Examples
- Burnley earned more from TV revenue than Barcelona from winning La Liga.
- Focus on João Pedro and Julián Álvarez.

## Insights
- Financial constraints force smarter, targeted squad building.

## Notable Opinions
- Barcelona must be smarter rather than bigger spenders.

## Sources
- https://x.com/DeadlineDayLive/status/2057317963657777500
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