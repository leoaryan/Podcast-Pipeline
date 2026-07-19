---
title: "Paper Club: Self Improving AI with Harness & Weight Updates"
channel: "Latent Space"
source_type: podcast
published: 2026-07-14
source_url: https://www.youtube.com/watch?v=-m3GyAWG7eM
video_id: -m3GyAWG7eM
---

# Paper Club: Self Improving AI with Harness & Weight Updates

- **Channel:** Latent Space
- **Published:** 2026-07-14
- **Source:** https://www.youtube.com/watch?v=-m3GyAWG7eM

## Transcript

> Speaker attribution is not available from YouTube captions. Turns are labeled generically as Speaker A to avoid false attribution.

### 00:00 - Transcript

**Speaker A [08:26]:** Vibhu Sapra : https://arxiv.org/pdf/2605.27276 Vibhu Sapra : Paper link ^

**Speaker A [18:02]:** Yashash : GDM paper on AutoHarness does some evaluations in this direction if anyone is curious: https://arxiv.org/pdf/2603.03329

**Speaker A [19:07]:** Diane Lin : Reacted to "GDM paper on AutoHarness does some evaluations in this direction if anyone is curious: https://arxiv.org/pdf/2603.03329" with 👍

**Speaker A [20:26]:** Eugene Yan : Reacted to "GDM paper on AutoH..." with 👍

**Speaker A [22:05]:** Vibhu Sapra : Most other stuff seems to get pretty great results on just harness eng Vibhu Sapra : Or just prompt optimization work

**Speaker A [23:18]:** Vibhu Sapra : Loop mentione Vibhu Sapra : So head of their time

**Speaker A [24:24]:** Libor Burian (Burny) : cool

**Speaker A [26:13]:** Umar Khan : what’s the relative magnitude of improvement from harness update, weight update, compared to existing **pretraining** / post **training** methods? Libor Burian (Burny) : what exactly determines if weights or harness gets updated? what yields smaller loss/**benchmark** performance?

**Speaker A [28:40]:** Vibhu Sapra : Replying to "what exactly determi..." Theres a feedback agent in the loop Vibhu Sapra : Replying to "what exactly determi..." Is one of the 3 main contributions on the first page Vibhu Sapra : Replying to "what exactly determi..." “We propose and evaluate a Feedback-Agent that also trains the task-specific agent’s weights, in combination with scaffold updates, to improve performance on arbitrary downstream tasks. The system is task-agnostic: given a task specification and a verifier, it produces both an evolved scaffold and an **RL**-adapted set of Low-Rank Adaptation (LoRA; Hu et al., 2022) weights.” Vibhu Sapra : Replying to "what exactly determi..." Theres more into what goes into feedback agent, etc. Libor Burian (Burny) : Reacted to "“We propose and eval..." with 👍 Yashash : overfitting?

**Speaker A [31:08]:** Madgula Amit : Overfitting can be eliminated by randomising the sequence of problems so that the **llm** doesn’t see any systematic pattern in the list of problems Denis Carabadjac : would be good to see other banchmarks j : is overfitting terrible if its cheaper? Yashash : Reacted to "would be good to s..." with ➕ Colin (Lanzaa) : Reacted to "is overfitting ter..." with 🤔 jingqianli : Replying to "is overfitting terri..." is overfitting terrible if its cheaper? Not really, if it serves the purpose why not. Especially in prod. Denis Carabadjac : Replying to "is overfitting terri..." should be ok, especially swapping adapters is pretty quick Libor Burian (Burny) : interesting: "Across all tasks, the Feedback-Agent begins with scaffold iteration and switches to weight updates once harness progress stalls" j : Reacted to "is overfitting ter..." with 👍 j : Reacted to "should be ok, espe..." with 👍

**Speaker A [33:45]:** Denis Carabadjac : Reacted to "interesting: "Across all tasks, the Feedback-Agent begins with scaffold iteration and switches to weight updates once harness progress stalls"" with 👍 adi : Reacted to "interesting: "Across..." with 👍

**Speaker A [35:09]:** Vibhu Sapra : In prod it really depends on how good of a realistic **benchmark** you can make thats properly representative of the task

**Speaker A [36:22]:** jingqianli : What about SIA-W? jingqianli : How does this work better than just **fine-tuning**

**Speaker A [38:34]:** Anshu Bhatia : For their Claude code and codex optimization baselines, do they do anything to improve them using train set? Even in context examples? Yashash : Replying to "For their Claude c..." Good question! CC and Codex are harnesses themselves - what do they update in this case?

**Speaker A [47:49]:** Diane Lin : is any of the harness update on meta-agent transferrable to similar tasks? Libor Burian (Burny) : mean squared error should increase? i would expect decrease. wondering how its defined Yashash : Reacted to "mean squared error..." with ➕ Eugene Yan : is the overall pattern that harness + weight updates work better than harness only, if you have good **training** data / evals?

**Speaker A [51:23]:** Vibhu Sapra : Replying to "is the overall patte..." It seems that they start weight updates after harness updates stop Eugene Yan : Reacted to "It seems that they..." with ➕ Tumi Nyathi : Reacted to "It seems that they start weight updates after harness updates stop" with ➕ Colin (Lanzaa) : Can the harness improvements be transfered to other models? Did they test this? Yashash : Reacted to "It seems that they..." with ➕ From Sw yx : i wonder how to **inference** this at scale Eugene Yan : Replying to "is the overall pat..." yea so long as you have good evals to hillclimb on, additional **RL** should help on that eval Vibhu Sapra : Replying to "i wonder how to infe..." Was discussed at start - needed to use thinky or **rl** api Vibhu Sapra : Replying to "i wonder how to infe..." Or non os **model** / big **model** and see if gains still made at big scale

**Speaker A [53:37]:** Vibhu Sapra : Side note for those in SF - it looks like the author is doing a paper reading irl today https://luma.com/uamylmoh Vibhu Sapra : Doesn’t look like this paper itself tho Vibhu Sapra : But Kunal (author) is a host Vibhu Sapra : Replying to "Can the harness impr..." One of the related works does this Vibhu Sapra : Replying to "Can the harness impr..." Doesn’t work too well Colin (Lanzaa) : Reacted to "Doesn’t work too ..." with ❤️
