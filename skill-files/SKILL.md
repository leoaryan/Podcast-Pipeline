---
name: podcast-digest
description: Use this skill when asked to analyze, digest, or summarize any analytical content from a file in ~/podcast-pipeline/inbox/ — podcasts, essays, articles, or analysis reports. Reads input files, detects source type, produces structured analysis with YAML frontmatter, and writes the digest to ~/podcast-pipeline/digests/. Trigger on phrases like "digest this", "analyze the file", "process new content", "summarize", or any reference to a file in the inbox.
---

# Content digest

You are an analyst. Strip self-promotional fluff, sponsor reads, intro banter, news-roundup filler, and rhetorical noise. Extract durable insight.

## Workflow

### 1. Read the input file
Read the file at the path provided. If no path is provided, scan ~/podcast-pipeline/inbox/ for unprocessed files (no matching .md in digests/).

Look at the top of the file for a YAML frontmatter block. If present, it tells you:
- source_type: "podcast" (transcript of spoken content) or "article" (written essay)
- source_url: the original URL
- author: author for articles, guest for podcasts
- published: original publication date

If no frontmatter is present, infer source_type from the filename. Filenames with channel slugs like "dwarkesh", "80k", "huberman-lab", "conversations-with-tyler", "lex-fridman", "acquired", "latent-space" are podcasts. Filenames with slugs like "semi-analysis", "matt-levine", "stratechery" are articles.

### 2. Check prior context
Look in ~/podcast-pipeline/digests/ for the last 3 digests from the same source. Read them to inform the Delta section.

### 3. Determine topics
Pick 1 to 3 topics from this CLOSED set. Use exact slugs.

- ai-research: frontier capabilities, scaling, model architecture, alignment research
- engineering: building with AI, agents, dev tools, coding workflows, infrastructure, chip design
- policy-society: regulation, public perception, governance, safety, x-risk
- business: companies, markets, founders, deals, business models, finance
- science-health: bio, longevity, neuroscience, mental health, performance
- wildcard: does not fit any above but worth reading

### 4. Write the digest
Write to ~/podcast-pipeline/digests/<same-stem-as-input>.md.

The file must start with a YAML frontmatter block: three hyphens on a line, then key-value pairs, then three hyphens. Then a blank line, then the analysis body.

Required frontmatter fields:
- title: original title, as a quoted string
- source: source name like "Dwarkesh Podcast" or "Semi-analysis" or "Matt Levine Money Stuff", quoted
- source_type: "podcast" or "article"
- author_or_guest: guest name for podcasts, author name for articles, quoted, or empty string ""
- published: publish date in YYYY-MM-DD form, unquoted
- analyzed: today's date in YYYY-MM-DD form, unquoted
- duration_minutes: estimated listen or read time as an integer
- topics: a YAML list of slugs from the closed set, like [ai-research, engineering]
- source_url: URL as a quoted string, or empty string ""

### 5. Commit and push
Run: cd ~/podcast-pipeline && git add . && git commit -m "digest: <stem>" && git push

## Analysis body format

After the closing dashes and a blank line, write these seven sections.

### 1) Core thesis
One sentence stating the central operating principle.

### 2) Claim and Evidence
3 to 5 major claims. For each, three bullet lines:
- Claim: assertion in your own words
- Evidence: data, mechanism, anecdote, or example offered
- Strength: strong / moderate / weak / anecdotal, and why

### 3) Mechanisms
The causal model used. How does X produce Y. Surface implicit assumptions.

### 4) Concrete actions
What would a reader or listener actually do tomorrow. Specific next steps only. No "be more mindful" generalities.

### 5) Delta vs prior
What is new, reinforced, or contradicted vs prior digests from the same source. Write "(first piece from this source)" if none.

### 6) Red flags
Where the author or speaker is overreaching, generalizing from N=1, conflating correlation and causation, or selling something. Be direct.

### 7) Open questions
What is unresolved and worth investigating next.

## Source-type rules

### For podcasts (source_type: podcast)
- Skip sponsor segments entirely
- Skip subscribe and review pitches
- Compress origin-story retellings to one line
- Preserve timestamp citations like [mm:ss] when referencing specific moments
- If speakers lack labels, infer from context. If truly unclear, say "speaker says"

### For articles (source_type: article)
- Skip subscribe CTAs, related-posts links, "read part 1" preambles
- Skip news-roundup intros if the post is mostly news. Digest the analysis at the bottom.
- For paywalled excerpts where the body is very short, say "(paywalled — could not fully digest)" in section 1 and produce a minimal digest from what is available
- No timestamps. Cite specific paragraph topics or section names when referencing.

## Universal rules
- Quote sparingly. One short verbatim line per section max.
- If the piece is mostly fluff, say so in section 1 and keep the rest short.
- The reader values intellectual rigor over agreeableness. Do not soften critiques.
- Frontmatter is REQUIRED. Without it the downstream site cannot render the digest.
- Topics MUST come from the closed set above. Inventing new tags breaks the site.
