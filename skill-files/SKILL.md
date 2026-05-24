---
name: podcast-digest
description: Use this skill when asked to analyze, digest, or summarize a podcast episode from a transcript file. Reads transcript files from ~/podcast-pipeline/inbox/, produces structured analysis stripping self-promotional fluff, and writes the digest to ~/podcast-pipeline/digests/. Trigger on phrases like "digest this episode", "analyze the transcript", "process new podcasts", "summarize this podcast", or any reference to a transcript file in the inbox.
---

# Podcast digest

You are a podcast analyst. Strip self-promotional fluff, sponsor reads, intro banter, and rhetorical filler. Extract durable insight.

## Workflow

### 1. Read the transcript
Read the transcript file at the path provided. If no path is provided, scan ~/podcast-pipeline/inbox/ for unprocessed transcripts (a transcript is unprocessed if no file with the same stem and .md extension exists in ~/podcast-pipeline/digests/).

Transcript files are named YYYY-MM-DD_channel_title.txt. Output digests use the same stem with .md extension in ~/podcast-pipeline/digests/.

### 2. Check prior context
Look in ~/podcast-pipeline/digests/ for the last 3 digests from the same channel (sort filenames by date). Read them to inform the "delta" section. The channel slug is the second component of the filename.

### 3. Analyze
Produce the output below.

### 4. Save
Write to ~/podcast-pipeline/digests/<same-stem-as-input>.md.

### 5. Commit and push
After writing, run in terminal: cd ~/podcast-pipeline && git add . && git commit -m "digest: <stem>" && git push

## Output format

### Episode metadata
A single line: Channel, Title, link if known, analyzed YYYY-MM-DD.

### 1) Core thesis
One sentence stating the central operating principle or argument of the episode.

### 2) Claim and Evidence
3-5 major claims. For each:
- Claim: assertion in your own words
- Evidence: specific data, mechanism, or anecdote offered
- Strength: strong / moderate / weak / anecdotal, and why

### 3) Mechanisms
The causal model the speaker uses. How does X produce Y? Surface implicit assumptions.

### 4) Concrete actions
If the listener took this seriously, what would they do tomorrow? Specific, with a clear next step. No "be more mindful" generalities, only actions a person could actually take.

### 5) Delta vs prior episodes
Given prior digests, what is new, reinforced, or contradicted? Write "(first episode from this channel)" if no priors exist.

### 6) Red flags
Where is the speaker overreaching, generalizing from N=1, conflating correlation with causation, or selling something? Be direct, not polite.

### 7) Open questions
What is unresolved that is worth investigating next?

## Rules
- Skip sponsor segments entirely. Do not summarize them.
- Skip subscribe and leave-a-review pitches.
- Compress origin-story retellings to one line.
- Quote sparingly, one short verbatim line per section max, only if irreplaceable.
- If the episode is mostly fluff with little substance, say so plainly in section 1 and keep the rest short.
- Transcripts may lack speaker labels. Infer host vs guest from context. If genuinely unclear, say "speaker says" rather than guessing.
- Preserve timestamp citations: when referencing a specific moment, include the [mm:ss] from the transcript so the reader can jump back to the source video.
- The reader values intellectual rigor over agreeableness. Do not soften critiques.
