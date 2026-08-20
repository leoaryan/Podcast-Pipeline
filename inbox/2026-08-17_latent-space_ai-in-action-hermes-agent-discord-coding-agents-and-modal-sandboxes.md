---
title: "AI in Action: Hermes Agent, Discord Coding Agents, and Modal Sandboxes"
channel: "Latent Space"
source_type: podcast
published: 2026-08-17
source_url: https://www.youtube.com/watch?v=DifrNc8mEzs
video_id: DifrNc8mEzs
---

# AI in Action: Hermes Agent, Discord Coding Agents, and Modal Sandboxes

- **Channel:** Latent Space
- **Published:** 2026-08-17
- **Source:** https://www.youtube.com/watch?v=DifrNc8mEzs

## Transcript

> Speaker attribution is not available from YouTube captions. Turns are labeled generically as Speaker A to avoid false attribution.

### 00:00 - Welcome and setup

**Speaker A [00:24]:** Kevin Ball: Hello, happy Friday!

### 01:10 - Exploring the Hermes Agent repository

**Speaker A [01:10]:** Kevin Ball: Alright, I'm just gonna… Kevin Ball: poke around and explore this Hermes agent. I don't know how many people are gonna join or not join, but I've been hearing a lot about Hermes. One of my engineers just set up a Kevin Ball: agentic code review thing using Hermes, so… I pulled down the… Repo. Kevin Ball: And I thought I'd just, like. Kevin Ball: get Pi to… to explore it for me.

**Speaker A [01:55]:** Kevin Ball: It's NVRC is already trying to use Nix, which I don't have. Maybe I'll have to check that out, but let me check out a branch.

**Speaker A [02:08]:** Kevin Ball: Book Manager, create a ticket. Kevin Ball: It's exploring… Then explore this repo and give me… A summary of… Kevin Ball: It's architecture, and what it does. Kevin Ball: And that's it.

**Speaker A [02:39]:** Kevin Ball: We'll see. Might be just the two of us. I don't know if anybody else is coming this week. Kevin Ball: Summer is wild. There's, like, nobody around. Luigi: Oh, yeah, I, I'm sorry, I had to… Yeah, Samir, I sent you a, I muted myself. Kevin Ball: All good. Luigi: They tend to do their stuff on Zoom. But yeah, I, yeah, I… I never…

**Speaker A [03:10]:** Kevin Ball: So yeah, I'm just gonna… Kevin Ball: poke around and see what I can find. I'll live narrate some of it, when it gets going. Kevin Ball: But trying to understand Hermes. Oh, yikes is here, too. Kevin Ball: Hey, Yikes, good to see ya. Luigi: Hermes, yeah, I guess Hermes is… Luigi: I mean, this is what to do, it's just where it's at. Yeah, it's basically a less complicated, Luigi: open claw. Luigi: In their own words.

### 03:43 - Hermes compared with OpenClaw

**Speaker A [03:43]:** Luigi: Could be interesting. Luigi: They have been stacking features and features and features and features. Luigi: Have you… Kevin Ball: Have you played with it at all? yikes: Yeah, I was gonna say less complicated? Luigi: Yeah, supposedly less complicated, yeah. Luigi: No, I've played with it, and I made it do stuff. Luigi: But… yikes: I have one running in my Discord, personally. Kevin Ball: Okay. Luigi: Cool.

### 04:08 - Coding agents through Discord

**Speaker A [04:08]:** Kevin Ball: So what are… tell me about it, because I… all I know is one of my engineers said, this is awesome, and set up an Agentic code review thing with it that has been awesome, legit. But, I have not actually… I just pulled down the repo now, and so I'm like, okay, let me figure this out. yikes: Yeah, I haven't… I would say, at least for me, it… it… yikes: feels like… or, like, I haven't really pushed it to the limit so much, yikes: But the things that I've done with it are… I basically use it like a coding agent, but the interface is via Discord. Luigi: You don't love it. yikes: And then, either to work on other projects, or for it to work on. Luigi: mad. yikes: It's been doing a lot of its own debugging, basically. Kevin Ball: Interesting. What's its, does it just, like, have open access to a virtual machine and any files, or what's the, sort of.

**Speaker A [05:07]:** Kevin Ball: Container **model** and all of that.

### 05:09 - Local, Docker, and Modal sandboxes

**Speaker A [05:09]:** yikes: Well, for me, I have one of them running on Modal. yikes: And then I was actually experimenting. There's… there's a… you can… you can change the setting, there's a setting, for terminal underscore env. yikes: And, so if I set that to local, then it appears to have access to my local file system. If I set it to modal, then it'll spin up a modal sandbox that, has… yikes: a little file system in it, and then I have… I was sort of confusing myself, because I have… yikes: I have my local copy of it, and I can set that to the modal backend, which gives me an ephemeral sandbox to do code stuff in, which is kind of nice, but then I also have an actual deployment of it on modal, because I wanted something that wasn't on my local machine, yikes: to live in Discord and be always on, effectively.

**Speaker A [06:12]:** yikes: But yeah, I think it's just a… it's a configurable environment variable in terms of where the… where the thingy lives. Kevin Ball: And then, you said you're using it as… Kevin Ball: To write code, is it interacting with, like. Kevin Ball: a Git repo that you've already got set up, or it's just dumping things in the file system, or like… yikes: That's what I've generally… I told… have it… I have it, like, cloned down a repo and… and mess around with that. Like, me and… me and my buddy are collaborating on a… yikes: Git repo project, and the… the… when we're, like, pair programming effectively, it's usually just us pinging Hermes in Discord, basically. Kevin Ball: Okay. Kevin Ball: Interesting.

### 06:56 - Heartbeats, gateways, and the Kanban board

**Speaker A [06:56]:** yikes: I haven't experimented with, like, the heartbeat type thing, where you can kind of make it more claw-like. I believe it has that functionality, and it all… it also has a built-in, like, Kanban board, too, which is kind of cool. I believe if you do Hermes Web or Hermes Gateway, then that'll… that's what'll… Kevin Ball: Do I need Nix installed to run it? Because when I was trying to do, like… Kevin Ball: It's NVRC appears to be trying to load Nix. yikes: I don't have Nix installed, so… Kevin Ball: So… yikes: So, my guess would be no. yikes: I don't think it… and, and… Kevin Ball: Installs… This is all install from… Kevin Ball: What if I want to install from… Meh… Kevin Ball: Source code… I guess this is… oh, maybe that's for the dev environment, but it's got a… Kevin Ball: If I want to… do I trust them? Shall I just, like… Install it here. yikes: Fairly reputable, reputable crew, but…

**Speaker A [08:02]:** Kevin Ball: Yeah, I guess the question is, how hard is it to uninstall? yikes: I have not tried to uninstall it yet, so… Luigi: I installed it, like, last time I used it? Luigi: Easily, but it was, like, two versions ago.

**Speaker A [08:23]:** Kevin Ball: Yeah, interesting. Okay, I think I'm not gonna install it right now, because I have a box that I'm also, like, setting up in the background where it'll… doesn't have anything in… like, I'm on my laptop right now, there's all sorts of… Kevin Ball: Stuff I don't want it to pull out. Luigi: Yeah, that's the reason why I haven't, like, reinstalled it yet. yikes: You can set the… have PI tell you how to set the terminal backend to modal, and then that way it'll stay in the ephemeral sandbox instead of on your machine.

**Speaker A [09:06]:** Kevin Ball: Well, I'm doing it, so what has it got? It's got… Interactive. Luigi: Supposedly, you can still use it with your, OpenAI subscription, so that's very nice. yikes: I usually use it.

**Speaker A [09:23]:** Kevin Ball: I love how OpenAI is just subsidizing us all in these subscriptions. I wonder how long that'll last. Luigi: We can thank, probably, we can, thank St. Peter for that. Luigi: No. Luigi: Because OpenClaw does it, that means Rome's agent probably also can.

**Speaker A [09:44]:** Luigi: But it's, it's hard work maintaining that, like, I think a lot of people in the back end of Noosa are doing a lot of work. yikes: Yeah, that… that Discord is poppin', honestly. They have people in there, like, every day, just hacking on it. It's kinda lit. Luigi: Oh, yeah. Especially the voice call is really active, but it's a wide range of, like, experienced and inexperienced people.

**Speaker A [10:11]:** Luigi: And, well… Luigi: In a way, it also has, like, a lot of overlap with OpenCloud, that's also why they have the Skills Hub. Luigi: Which is, like, For a large part, open claw skills. Kevin Ball: Yeah, interesting. Luigi: So it's created as, like, a common ecosystem in that sense. Kevin Ball: Alright, so it looks like I can just install it, and then, yeah, set it up to be… yikes: Yeah, you can have the… you can set the backend to be either modal, or Docker, or wherever, it's just a config variable. Kevin Ball: Got it. Okay. Kevin Ball: Actually, I don't… I don't hate, Kevin Ball: We're just running it in Docker. yikes: Yeah.

**Speaker A [10:57]:** Kevin Ball: Alright, let's trust them. We'll install it.

### 11:07 - Discord voice calls and TTS

**Speaker A [11:07]:** yikes: Oh, that's one of the… it doesn't work super well, but one of the other things that it's got is it can just hang out in a Discord voice call with you, and then it'll do, like, transcribed TTS. yikes: Kinda… kinda duplex-y sort of stuff. Doesn't work super well, but it's… it's neat. It's interesting. Kevin Ball: So I wonder… Kevin Ball: I'm going to be setting up, so this… I'm just exploring it on my laptop, but we're…

### 11:34 - Production agentic code review

**Speaker A [11:34]:** Kevin Ball: But one of the things that we're looking at… so the agentic code review thing was valuable enough. We wanted to set up something more permanent, because right now it's just running on one of my developers, his own box, and… Kevin Ball: I get a free OWAS plugin? Kevin Ball: Sure. I don't know. Quick setup, go for it.

**Speaker A [12:02]:** yikes: That's for their, their **inference** service, which I think has some amount of free tier, but I don't know if you have to pay first to get to the free tier. Kevin Ball: They have a free tier with some cheap models, I'm just gonna sign up with my LLC email address and see what happens. yikes: Yeah. yikes: But you can also log in with Codex after you've gone through the setup once, too. Kevin Ball: Cool. Oh, they want me to subscribe to a thing, even though it's $0. What? yikes: Yeah, yep, yep. Kevin Ball: I don't want to set that up. Kevin Ball: I'm worried you're gonna charge the hell out of me.

**Speaker A [12:47]:** Kevin Ball: What if I say no? Kevin Ball: Alright, how do I get out of you?

**Speaker A [12:58]:** Kevin Ball: Alright, I just controlled C, we'll see what happens. We'll use Docker.

**Speaker A [13:05]:** Kevin Ball: I don't need Discord right now. Okay.

**Speaker A [13:21]:** Kevin Ball: Let's… oh, you know what, I can use my open router.

**Speaker A [13:30]:** Kevin Ball: Am I gonna have to paste my open router in here? Kevin Ball: Wait, I… what if I have… Alright. Kevin Ball: I'm gonna figure this out. Not screen sharing.

**Speaker A [13:44]:** Kevin Ball: do you know… if I have an open router in an NVRC somewhere, can I just copy that over to this, or just get it in my environment, and then it will do it, or it's going to… yikes: I think you have to configure the… okay, so you've… yeah, just if you… you can… you can… if you paste the open router key in, it won't show up, by the way. Kevin Ball: Oh, that's good. Luigi: Oh, that's nice. Like, you can also… Luigi: I don't know if it's an environment variable for you, or… yikes: But yeah, you should be able to just set the NVAR and be good to go. Kevin Ball: Okay, Kevin Ball: Oh, it's got my… here… OpenAI Codex auth. It's, like, running me through a bunch of different things. yikes: It has a little… it has a good bit of setup at the beginning, just because there's so many services that it can theoretically, but… yikes: Yeah, it should be able to do…

**Speaker A [14:44]:** yikes: STT, TTS, image generation, frickin' web search, blah blah blah blah, all sorts of stuff. yikes: So, there's a little bit of setup to go through. Kevin Ball: Oh man, all of this… Kevin Ball: And I just wanted to understand how it works more than anything. I don't need to do the setup live, that's… that's all annoying. So, let's see, how does it all work? Kevin Ball: Let's just see what GPT and Pi will tell me. yikes: Indeed.

**Speaker A [15:20]:** yikes: Oh, it's telling you how the container thing works.

**Speaker A [15:34]:** Kevin Ball: Yadda yadda yadda. So, what do we got? We have **AI** Agent… Kevin Ball: It's the thing he's generally written in Python, looks like. yikes: Yep. Kevin Ball: We get this, we do a resolver… What is my loop around?

**Speaker A [15:56]:** Kevin Ball: What types of heartbeat… Schedule and background stuff…

**Speaker A [16:30]:** Kevin Ball: And what have we got? We got cron…

**Speaker A [16:40]:** Kevin Ball: Crush Isolated Army sessions, so that… Kevin Ball: Well, that's sort of… so that's interesting. For those who are using Hermes already, like, do you think about it as this is a single agent with a set of, like, shared context, or do you have a bunch of, like, sub-agents or other different… Kevin Ball: Things? Like, what's the… what's the mental **model**? yikes: It's got,

### 17:02 - Profiles as independent agents

**Speaker A [17:02]:** yikes: you can create profiles, and those are kind of how I think of different, agents. Like, I have my… I have my GLM profile, I have my modal backend profile, I have my local terminal profile. yikes: And that's sort of how I organize them. I don't think that's necessarily how you need to organize them, but that's how I've got mine set up. Kevin Ball: Got it. So you've got profiles, which are essentially their own agents, they've got a core prompt, a set of skills, what have you. yikes: Yeah.

### 17:31 - Sessions and durable memory

**Speaker A [17:31]:** Kevin Ball: And they have durable memory of some sort? yikes: Yeah, they have… there… there's… I don't actually use that… use it all that much, how… or, yeah, effectively, how I've been… yikes: how I have been operating it is basically each Discord thread is its own **context window**, yikes: And then… but I know there is a utility for shared memory, I believe it's called Poncho, that… I'm not sure if mine is enabled or not. I think I've seen it create memories once or twice, but not too much. Kevin Ball: Okay…

**Speaker A [18:14]:** Kevin Ball: I'll ask about the memories in a sec, so it's talking about it's got this… Kevin Ball: You can run long commands, okay, sure.

### 18:22 - Kanban dispatch and agent-created skills

**Speaker A [18:22]:** Kevin Ball: There's a Kanban dispatcher. Kevin Ball: That's kinda cool. Kevin Ball: Curator.

**Speaker A [18:40]:** Kevin Ball: Agent created skills. Okay, tell me about…

**Speaker A [18:46]:** Kevin Ball: How do those work, and when are they created? Or what?

**Speaker A [19:08]:** Kevin Ball: Alright, so… it has a tool, Skill Manage.

**Speaker A [19:21]:** Kevin Ball: And it uses this procedural memory, so it learns a thing… Have you? Kevin Ball: Right, it's a skill.

**Speaker A [19:33]:** Kevin Ball: Interesting…

**Speaker A [19:44]:** Kevin Ball: It manages its own skills list. Are these, profile-specific or shared?

**Speaker A [19:56]:** Kevin Ball: Oh, interesting. So the profiles have their own…

**Speaker A [20:02]:** Kevin Ball: Homes, so you could set a bunch of those.

**Speaker A [20:12]:** Kevin Ball: That's interesting. Okay, and then we were talking about memory and shared memory.

**Speaker A [20:26]:** Kevin Ball: Let's poke into that and see what there is.

**Speaker A [20:39]:** Kevin Ball: Bite Rover.

**Speaker A [20:45]:** Kevin Ball: Oh, interesting. So they've just got a bunch of different third-party Kevin Ball: I do have a local memory, which, her profile… Okay…

**Speaker A [21:08]:** Kevin Ball: So they have… It's local memory, which is related to the profile. Kevin Ball: Injected into the session prompt… system prompt at session start, so those are there in every **context window**. Kevin Ball: It's got a searchable conversation hipstery in a SQLite database. Kevin Ball: Okay… Background, self-improvement memory…

**Speaker A [21:45]:** Kevin Ball: So that's after turns, they can run that.

### 21:50 - Pluggable memory providers

**Speaker A [21:50]:** Kevin Ball: And then they have a pluggable memory provider that lets you plug into…

**Speaker A [21:59]:** Kevin Ball: A few different things, interesting.

**Speaker A [22:15]:** Kevin Ball: Huh? Kevin Ball: Okay, and so those memory providers let you have memories that are cross-profile, Something's around that. Kevin Ball: If you want to,

**Speaker A [22:40]:** Kevin Ball: Let's look at orchestration.

**Speaker A [22:48]:** yikes: Yeah, this is why I seemed… I was a little surprised to hear that the pitch for it is a simplified open claw, because to me, it seems like a significantly more opinionated open claw, with a lot more features out of the… yikes: Out… out of the box, at least as far as I can… Kevin Ball: Yeah, it's got a lot of stuff in here. yikes: Yeah, it does. Kevin Ball: Alright, so, what have we got? We have…

**Speaker A [23:21]:** Kevin Ball: Alright, so conceptually, the profiles are the agents, that makes sense. Each one has its own config with **model**, soul, memory, skills, sessions, con jobs. Kevin Ball: You can run them directly.

**Speaker A [23:39]:** Kevin Ball: Kanban lets you, sort of, Do those… okay…

### 23:52 - Short-term subagents and delegation

**Speaker A [23:52]:** Kevin Ball: You can do short-term sub-agents, that's interesting. yikes: I believe I've seen it just decide to delegate like that before. Kevin Ball: Yeah, looks like this is a tool call, but it's probably just available to it, so that's interesting.

**Speaker A [24:15]:** Kevin Ball: This is interesting, because it's using the profiles. I wonder, Kevin Ball: When doing a delegate task, with a profile, does that Kevin Ball: Session, go into that session's profile history. Kevin Ball: Or that, that profile's session history. yikes: My guess is gonna be no, except for the result. Kevin Ball: Yeah, that's… It's kind of an interesting persistence Kevin Ball: **model**, right? Like, if you're… if you're invoking a profile. Kevin Ball: If you're doing stuff with a profile directly, it has a persistent session history, so it's got this, like, long-term memory of the conversations it's had. But you can invoke that same profile as a sub-agent. Kevin Ball: Or, like, an agent can invoke it as a sub-agent. So, like… Conceptually, is that, like. yikes: Oh, I think I see what you're getting at. Kevin Ball: like… If we were to mentally **model** these as actual entities.

**Speaker A [25:16]:** yikes: Well, core delegate task does not take a profile parameter here. Kevin Ball: Oh, interesting. So, yeah, let's see what it does.

**Speaker A [25:36]:** Kevin Ball: Alright, they stay in the parent profile session DB.

**Speaker A [25:42]:** Kevin Ball: Platform sub-agent. Kevin Ball: sets the… Skip memory is true, it's not loading or writing it.

**Speaker A [26:03]:** Kevin Ball: Interesting. Okay, yeah, so if you want to run it using that profile… Use Kanban. Kevin Ball: But didn't it have… I'm gonna go back up to the example of delegate task. It has this delegate Researcher subtask, delegate TestWriter subtask.

**Speaker A [26:28]:** yikes: Yeah, it can vary goal, context, tool sets, role, **model**, and provider via delegation config. yikes: Which I'm not sure… I'm not sure where that is. Kevin Ball: Yeah, where does the delegation… I can live… Kevin Ball: How does that connect with the profiles, if at all? Kevin Ball: Right, because it was showing it as if it was delegating to these, like, alternate roles, profiles. yikes: Yeah, I wonder if Pi is, like, messing with us here. Kevin Ball: I mean, entirely possible.

**Speaker A [27:09]:** yikes: Oh, okay, delegation in a YAML file.

**Speaker A [27:50]:** Kevin Ball: Okay, so that's interesting. Kevin Ball: Can agents themselves create… or, I'll say profiles themselves create new profiles, or does that require a…

**Speaker A [28:07]:** Kevin Ball: I know, I was playing… I've been playing with Nano Claw a bit, because I got the chance to interview the creator, and so then I was like, oh, this is interesting, let me play with it. And it was… it is interesting, it… Kevin Ball: it does a lot of, oh yeah, I can submit up another agent for you to do that.

**Speaker A [28:36]:** Kevin Ball: So, what does it do? Profile can create a profile because it can run the CLI. Kevin Ball: Right, that makes sense.

**Speaker A [28:47]:** Kevin Ball: They are at the machine level.

**Speaker A [29:21]:** Kevin Ball: Okay, interesting.

### 29:44 - Building a mental model of Hermes

**Speaker A [29:44]:** Kevin Ball: So, mental **model** I'm building up is… There's some sort of dispatcher. Kevin Ball: if I want to have it do a bunch of tests, it basically is going to operate via this Kanban. Kevin Ball: style board, and spin things out, and I interact with it probably through a chat client of some sort. yikes: Yeah.

**Speaker A [30:31]:** Kevin Ball: There's a TUI, there's a web interaction…

**Speaker A [30:41]:** Kevin Ball: Set up a messaging gateway, which is all of these things.

**Speaker A [30:57]:** Kevin Ball: Profiles run their own gateways. That's interesting, hold on.

**Speaker A [31:16]:** Kevin Ball: Yeah, harmony's prevents two profiles, so…

### 31:20 - Multi-profile Discord bots

**Speaker A [31:20]:** Kevin Ball: Essentially, each profile you set up becomes its own bot. Kevin Ball: That you're talking to? Kevin Ball: It looks like.

**Speaker A [31:30]:** Kevin Ball: Though you might have a manager that coordinates a bunch of others via Kanban? Kevin Ball: Yeah, because you were saying you were doing multiple profiles. Are you talking to each of them distinctly in your Discord, or how does that work?

**Speaker A [31:45]:** yikes: Well, yeah, so I have… I have, I believe I could if I wanted to. I would just give each profile its own Discord bot **token**. Currently, the two that I have in my Discord is… I have the one yikes: that is running on modal, which technically… yikes: does not share profiles with the one that I have running locally as well, so I kind of have two… yikes: to, folders of profiles, if you will. yikes: It's currently my setup. Kevin Ball: Got it. yikes: But I don't, yeah. Currently, I don't… outside of that differentiation, I don't have, I don't have, like, one profile assigned. yikes: To… although that might actually be easier… yikes: Well, no, because I still need it running… All the time. yikes: Hmm.

**Speaker A [32:47]:** yikes: Yeah, currently I don't have it set, but I presume what I would do is just configure a different Discord **token** for each profile that I wanted to… yikes: Hit separately? Kevin Ball: Got it.

### 33:06 - Failure handling and credential pools

**Speaker A [33:06]:** Kevin Ball: I'm just looking at how it deals with failure and all of that. yikes: It's pretty good about it.

**Speaker A [33:13]:** Kevin Ball: Nice. I think… And with this, I have, like, a reasonable Kevin Ball: mental **model**, all I need… do you guys have any questions or things we should… you'd like to dig into? Kevin Ball: Credential pools is interesting, so let's see…

**Speaker A [33:33]:** Kevin Ball: Gonna rotate through, that's neat.

**Speaker A [34:14]:** Kevin Ball: This looks pretty powerful, I will say. yikes: Yeah, it's got a lot going on, but there are… I… yeah, I kinda… the… I think their opinions are good opinions, basically. It's very opinionated, but… yikes: It's a good team, so… Kevin Ball: Nice. Kevin Ball: Cool, well, I'm… both tired, because I'm still jet-lagged from being in Europe last week, and Kevin Ball: My brain is on the fritz, so I don't have any more questions that I want to dig into right now. Anyone else want to drive something, or poke around with something? Or… Kevin Ball: have a question that I should just ask Pi to figure out right now?

**Speaker A [35:06]:** Kevin Ball: Nope. Alright.

### 35:08 - Wrap-up

**Speaker A [35:08]:** Kevin Ball: Well, maybe we'll call that a session, then. I think… Kevin Ball: summer is going to continue to be sparse, and we've got the World Fair coming up, so folks will be out for that. Kevin Ball: But if folks have things they want to talk about in future ones of these, or just do it like this, let's pick a project and explore it. yikes: Yeah. Kevin Ball: It's a good time. yikes: For sure. Kevin Ball: Alright. Kevin Ball: I'm gonna head out. Take care, y'all. yikes: Later. Luigi: Later.
