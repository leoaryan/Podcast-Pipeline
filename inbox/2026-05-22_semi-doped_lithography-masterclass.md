---
title: "Lithography Masterclass"
channel: "Semi Doped"
source_type: podcast
published: 2026-05-22
source_url: https://www.semidoped.fm/2570635/episodes/19222215-lithography-masterclass
transcript_url: https://www.buzzsprout.com/2570635/19222215/transcript.vtt
audio_url: https://www.buzzsprout.com/2570635/episodes/19222215-lithography-masterclass.mp3
author: "Vikram Sekar and Austin Lyons"
---

# Lithography Masterclass

- **Channel:** Semi Doped
- **Published:** 2026-05-22
- **Source:** https://www.semidoped.fm/2570635/episodes/19222215-lithography-masterclass
- **Transcript:** https://www.buzzsprout.com/2570635/19222215/transcript.vtt

## Transcript

**Vikram Sekar [00:00:00]:** The main idea of making masks and making transistors smaller came about because this guy, I think he was working for TI, came about uh and he was looking at a microscope and he was like, wait a minute.

**Vikram Sekar [00:00:13]:** If I can flip the microscope over and shine light from the other side, it gets smaller.

**Austin Lyons [00:00:23]:** Hello everyone, and welcome to another semi-dope podcast.

**Austin Lyons [00:00:25]:** I'm Austin Lines with Chipstrat, and with me is Vic Shaker from Vic's newsletter.

**Austin Lyons [00:00:30]:** Hey Vic, what's going on, man?

**Vikram Sekar [00:00:32]:** Yeah, I don't, not that much.

**Vikram Sekar [00:00:34]:** Other than like everybody's panicked about uh the 13F from that situational awareness hedge fund, and uh there was this sell-off in optics, and everybody freaked out.

**Vikram Sekar [00:00:45]:** I'm like, what's what's going on?

**Vikram Sekar [00:00:47]:** First of all, I I still don't really know what a 13F is.

**Vikram Sekar [00:00:50]:** I guess it's like a hedge fund has to report some holdings that you know they hold and what they sell and what they bought.

**Vikram Sekar [00:00:58]:** I think something like that.

**Austin Lyons [00:00:59]:** Yeah, yeah, yeah.

**Vikram Sekar [00:01:00]:** And uh Leopold Ashenbrenner, is that how you pronounce his name?

**Vikram Sekar [00:01:04]:** Sorry if I got that wrong.

**Vikram Sekar [00:01:05]:** I have no idea.

**Vikram Sekar [00:01:06]:** It's too many syllables.

**Vikram Sekar [00:01:08]:** Um yeah, I mean, he he I guess he made a lot of money and converted like a few million into a billion or something, and then now everybody's following him for the latest stock tips.

**Vikram Sekar [00:01:19]:** And when everybody looks at his 13F, they panic, and there's this whole sell-off.

**Vikram Sekar [00:01:23]:** Apparently, he shot optics and short AMD Intel and he sold in.

**Vikram Sekar [00:01:28]:** I don't know.

**Vikram Sekar [00:01:29]:** Yeah, so it's like everything is down in the semi-market because of some some hedge fund thingy.

**Vikram Sekar [00:01:34]:** I it's this is what's happening.

**Vikram Sekar [00:01:36]:** It's funny.

**Austin Lyons [00:01:37]:** I mean, so if if I'm him, I wake up and look and go, wow, I can buy a few puts because on this 13F, it doesn't talk, I don't think it talked about like the size of his puts or anything.

**Austin Lyons [00:01:47]:** So he can just buy a few puts at some point in time, drive the price down.

**Austin Lyons [00:01:52]:** Could he use that to then buy the price?

**Austin Lyons [00:01:54]:** I mean, that's market manipulation, but on the other hand, it's like people are trading on public data and on vibes, you know.

**Austin Lyons [00:02:00]:** So just like he could throw people off his trail, right?

**Austin Lyons [00:02:03]:** Like just buy a little tiny amount of puts in like everything, and you wouldn't know what he's investing in.

**Vikram Sekar [00:02:08]:** Yeah, I don't know.

**Vikram Sekar [00:02:10]:** I think Leopold listens to this podcast.

**Vikram Sekar [00:02:12]:** If you do, just let us know.

**Vikram Sekar [00:02:14]:** Maybe you can come explain to us what a 13F is, because I don't know about you, man.

**Vikram Sekar [00:02:19]:** I have no idea what all this stuff is.

**Vikram Sekar [00:02:21]:** So I'm happy to learn from the best.

**Austin Lyons [00:02:23]:** Yes, Leopold, you're welcome anytime.

**Austin Lyons [00:02:25]:** All right.

**Austin Lyons [00:02:26]:** So today we're gonna talk lithography.

**Austin Lyons [00:02:28]:** So I thought it'd be really interesting to talk about the economic challenges of lithography, modern EUV lithography, especially, um, because you know, ultimately, incentives drive outcomes, and there are challenges with the increasing cost of lithography, the increasing cost of fabs.

**Austin Lyons [00:02:49]:** And you you start to see, you know, TSMC uh can afford the next process node, and and Intel and Samsung are trying to be stay in the race or be in the race.

**Austin Lyons [00:03:02]:** Um there aren't that many other competitors.

**Austin Lyons [00:03:04]:** And from afar, if you're like a semi-tourist, as they like to say on X, um, you might say, like, hey, TSMC is crushing it, you know, why aren't more people in this game?

**Austin Lyons [00:03:13]:** And of course, as you start to unpack it, you realize that um costs are a barrier to let people enter.

**Austin Lyons [00:03:20]:** And so then you start pulling on the thread and you ask, well, what cost?

**Austin Lyons [00:03:23]:** And one of those major contributors to the capex needed to participate is modern EUV.

**Austin Lyons [00:03:30]:** And so, um, yeah, what do you think?

**Austin Lyons [00:03:33]:** Should we talk EUV?

**Vikram Sekar [00:03:35]:** Yeah, that's that's a great topic for today.

**Vikram Sekar [00:03:38]:** I think it ties in tangentially to what is happening uh to the market today and why people think that we are not in an unconstrained uh trajectory upwards.

**Vikram Sekar [00:03:53]:** And this basically stems from the recent Gavin Baker interview that I put in in one of our daily semi-doped uh daily updates on Substack.

**Vikram Sekar [00:04:03]:** So if anybody is not subscribed to the Substack, I recommend it.

**Vikram Sekar [00:04:06]:** It's free.

**Vikram Sekar [00:04:07]:** You know, you can go get subscribed on that, uh, semidope.com.

**Vikram Sekar [00:04:11]:** But the idea that Gavin said uh you know floated in that interview was we are not in a bubble because TSMC is basically holding back the entire industry by not creating enough chips for everybody, by controlling their level of capex spend on tools that require um, you know, DUV and EUV.

**Vikram Sekar [00:04:35]:** And most famously, I think TSMC is not pro-EUV.

**Vikram Sekar [00:04:40]:** They think the tools are too expensive and that they want to stay on DUV with multi-patterning as far as they can manage to do so.

**Vikram Sekar [00:04:50]:** And we'll talk about what DUV with multi-patterning means in this episode.

**Vikram Sekar [00:04:55]:** But this is where we are right now.

**Vikram Sekar [00:04:57]:** Tools cost a lot.

**Vikram Sekar [00:04:59]:** I think an EUV machine costs something to the tune of uh$400 million, and that's just one machine, and you need to run many of them to produce the chips at scale that we need, and that's that scale is continuously increasing.

**Vikram Sekar [00:05:13]:** So it really comes down to is EUV the only way forward?

**Vikram Sekar [00:05:19]:** Um, and then there is uh Hyper Nae UV, which is like extremely amazing.

**Vikram Sekar [00:05:26]:** I don't even know if those are in production yet.

**Vikram Sekar [00:05:28]:** I don't think so.

**Vikram Sekar [00:05:29]:** But those are gonna cost close to a billion dollars.

**Vikram Sekar [00:05:32]:** That's insane.

**Austin Lyons [00:05:33]:** Yes, totally.

**Austin Lyons [00:05:34]:** So we'll yes, we'll unpack all this for everyone when you're like, what's DUV?

**Austin Lyons [00:05:37]:** What's UV?

**Austin Lyons [00:05:38]:** Why does it cost so much?

**Austin Lyons [00:05:39]:** That's what this episode's all about.

**Austin Lyons [00:05:41]:** Lithography, masterclass, hopefully, to set the stage for hopefully even future conversations around lithography, some startups that are out there.

**Austin Lyons [00:05:50]:** And actually, you know, I just saw ASML shared a roadmap.

**Austin Lyons [00:05:54]:** Um, I think it was IMEC had a conference.

**Austin Lyons [00:05:56]:** It's going on like right now, the ITF World Conference.

**Austin Lyons [00:05:59]:** And ASML showed some of their roadmap and how they think they're gonna be able to bring the cost per exposure down.

**Austin Lyons [00:06:05]:** And it would be nice to unpack this, but before we get to all of those nitty-gritty details, we want to educate our listeners on some of the some of the fundamentals.

**Austin Lyons [00:06:14]:** So let me throw out some numbers.

**Austin Lyons [00:06:16]:** So uh a brief I want to set one thing.

**Vikram Sekar [00:06:20]:** I want to say one thing for Austin before Austin.

**Vikram Sekar [00:06:22]:** So most of this stuff, Austin is actually the expert because he um actually spent time working on uh this kind of lithography stuff in a clean room, which is something I can't say I have done.

**Vikram Sekar [00:06:35]:** Uh I've measured wafers and measured transistors, uh, that kind of stuff.

**Vikram Sekar [00:06:40]:** So I've handled completed silicon wafers, but I've never actually done lithography myself.

**Vikram Sekar [00:06:46]:** And you have.

**Vikram Sekar [00:06:47]:** So this is a this is a cool thing.

**Vikram Sekar [00:06:49]:** You can tell us a little bit more rather than just what you can read on the internet, perhaps.

**Vikram Sekar [00:06:53]:** It's it's interesting what it looks like inside a clean room.

**Vikram Sekar [00:06:56]:** I'm excited to hear.

**Austin Lyons [00:06:57]:** Yes, yes.

**Austin Lyons [00:06:58]:** So, well, thank you for mentioning that.

**Austin Lyons [00:06:59]:** So, yes, when I was in grad school, uh, I worked at the University of Illinois or Bana Champaign in doing research as a research assistant, making graphene-based transistors.

**Austin Lyons [00:07:10]:** So I was in a lab with Professor Eric Popp, he's at Stanford now, and he studies 2D materials.

**Austin Lyons [00:07:16]:** So we were studying our people on our team were studying carbon nanotubes, and then I got to work in graphene.

**Austin Lyons [00:07:21]:** And so, yes, I got to be in a clean room with you know silicon wafers, um, etching, you know, depositing, doing lithography.

**Austin Lyons [00:07:30]:** And in fact, I even got to do e-beam lithography because we were trying to make you know very precise, kind of one-off little uh nanoelectronic systems.

**Austin Lyons [00:07:40]:** And it didn't matter that the throughput of e-beam is really low, which we're not gonna talk about e-beam lithography much here, but it's just a cool thing that I got to experience.

**Austin Lyons [00:07:48]:** And in fact, when I first started, we were mechanically exfoliating graphene, which means we were taking um basically tape, and mechanically we get graphite, like layers of pencil lead essentially, and then we take like literally like clear tape, um, and then stick it on top of the graphite and then pull it off, and then take it under a microscope and look, and you can kind of like figure out how many layers of graphene you have there.

**Austin Lyons [00:08:16]:** And so I'd just scan around, you know, I'm I'm like doing some of this stuff in a bunny suit and then going back into the lab and moving this thing around, you know, and just thinking like, oh, what am I doing with my life?

**Austin Lyons [00:08:26]:** I'm trying to find single layer graphene, that's what I'm doing.

**Austin Lyons [00:08:28]:** But of course, um, once you find single layer graphene, then we would make trans, we'd pattern the transistors right there on it and then take measurements and publish it because it was a hard thing to do.

**Austin Lyons [00:08:39]:** And so we kind of had an advantage that we knew how to do it.

**Austin Lyons [00:08:43]:** Um, I won't I won't talk too much more.

**Austin Lyons [00:08:45]:** We eventually did chemical chemical vapor deposition um to create graphene using like uh copper foil essentially, and then we could grow graphene, and it wasn't as pristine and pure, but it was more scalable.

**Austin Lyons [00:08:58]:** And anyway, uh good memories.

**Austin Lyons [00:09:01]:** I spent a lot of time.

**Vikram Sekar [00:09:02]:** Yeah, it's amazing stuff.

**Vikram Sekar [00:09:03]:** I I bet it was a great experience doing all this stuff.

**Vikram Sekar [00:09:06]:** At the time, it's probably frustrating as all hell as all research is, but then looking back at it, it's like, ah, I don't mind doing that again now.

**Vikram Sekar [00:09:13]:** At least like going into a clean room and like pottering around would be nice.

**Vikram Sekar [00:09:17]:** Totally, man.

**Austin Lyons [00:09:18]:** It was like it was challenging in that you had to, you couldn't just do the research, you had to do a lot of exploration to figure out how to even make the thing before then you could actually measure it and do the research.

**Austin Lyons [00:09:30]:** Um, and so yes, it was frustrating at the time because you'd spend all this time a whole day and then you get to the end and be like, oh, that didn't work, you know.

**Austin Lyons [00:09:36]:** But yes, looking, looking back now, it's like, oh, how fun was that?

**Austin Lyons [00:09:40]:** How much intellectual freedom there to just be like, you know, your research professor says, Hey, go make this thing.

**Austin Lyons [00:09:45]:** And you're like, Well, I guess I gotta read and experiment and try to figure out how to make it and then measure it, and then see if our hypothesis was correct, you know?

**Vikram Sekar [00:09:53]:** Yes, yes, yeah.

**Vikram Sekar [00:09:54]:** It's nice.

**Vikram Sekar [00:09:54]:** Okay.

**Vikram Sekar [00:09:55]:** Now we're good, now we're good.

**Vikram Sekar [00:09:56]:** Now, you know, we hit carbon nanotubes already, like research that's never made it out of the lab.

**Vikram Sekar [00:10:01]:** You spend time doing that.

**Vikram Sekar [00:10:02]:** Awesome.

**Vikram Sekar [00:10:03]:** Now let's talk about stuff we can actually make.

**Austin Lyons [00:10:06]:** Yes.

**Austin Lyons [00:10:06]:** Okay, so let's talk about.

**Austin Lyons [00:10:08]:** Okay, so um, have you heard of Rocks Law, by the way?

**Vikram Sekar [00:10:12]:** I have not.

**Austin Lyons [00:10:13]:** Okay, so so uh this is a you know, a quote unquote law, just like Moore's law.

**Austin Lyons [00:10:19]:** It's it's really an observation, um, named after Arthur Rock, and he was uh an early investor in Intel, maybe um kind of one of the founders of the venture capital industry, if you will.

**Austin Lyons [00:10:29]:** But um, the the observation was that the cost of a semiconductor fab doubles every four years.

**Austin Lyons [00:10:37]:** So, you know, it gets more and more expensive.

**Austin Lyons [00:10:39]:** So now this is interesting.

**Austin Lyons [00:10:40]:** This is related to Moore's law, where Moore's law said that the number of transistors in an integrated circuit doubles every two years.

**Austin Lyons [00:10:49]:** And so if the cost of a fab doubles every four years, that's slower than the number of transistors doubling every two years.

**Austin Lyons [00:10:56]:** And so what that means is that Moore's law is really like an economic statement that says for roughly the same price, we can get more transistors per dye area, per chip, per unit area over time.

**Austin Lyons [00:11:10]:** And that's good, that's really what drove the industry was that economic realization that for the same dollars, you could get more compute over time.

**Austin Lyons [00:11:17]:** We are getting to the point where the cost of fabs is getting so high that that, you know, we've seen decades ago really, Moore's law, the number of transistors doubling, shrinking for physical reasons, but also from an economic perspective, actually the cost of transistors flatlining and potentially even coming up the cost per transistor.

**Austin Lyons [00:11:40]:** And again, the question is well, what's driving that fundamental change to some of these important economic scaling laws that we've seen for decades?

**Austin Lyons [00:11:50]:** And lithography is a big contributor.

**Austin Lyons [00:11:52]:** Like you said, low NA EUV tools used to cost around 250 million.

**Austin Lyons [00:11:57]:** Um, now high NA is coming out around 400 million.

**Austin Lyons [00:12:00]:** And give or take, you know, these numbers change over time, and it probably depends per customer.

**Austin Lyons [00:12:06]:** Um, but you can back some of this stuff up out of uh ASML's reports because they only sell uh you know they don't sell many of these per year.

**Austin Lyons [00:12:14]:** But anyway, yes, the rumored hyper NA, which would be a future tool, could cost anywhere from 600 to 800 million.

**Austin Lyons [00:12:20]:** Potentially, if the Strait of Hormuz stays closed, maybe a billion dollars because that's driving everything up.

**Austin Lyons [00:12:26]:** Yep.

**Austin Lyons [00:12:27]:** Um, so which means the lithography, all of these tools, like you said, and we'll get into it.

**Austin Lyons [00:12:33]:** Um, you know, you might need 15 tools to open up a new fab.

**Austin Lyons [00:12:37]:** So I think I'd seen some CNBC coverage where it uh it said that Intel's 18A fab in Arizona, Fab 52, needed 15 EU V machines.

**Austin Lyons [00:12:46]:** So imagine that, you know, half a billion dollars a pop and you need 15 of them.

**Austin Lyons [00:12:51]:** That is no joke.

**Austin Lyons [00:12:52]:** And that's why uh a brand new fab costs on the order of 20, 30 billion dollars.

**Austin Lyons [00:12:58]:** So I just wanted to quick paint the picture of the enormous CapEx cost to just build one new fab to try to stay in this race.

**Austin Lyons [00:13:08]:** And of course, that ultimately means the cost per wafer will have to go up too, because you only can do so many wafer starts per month, say tens of thousands of wafer starts per month or a hundred thousand, and you need to amortize the cost of all those tools over that fixed number of wafers.

**Vikram Sekar [00:13:26]:** Okay, cool.

**Vikram Sekar [00:13:27]:** So let me back up a little bit and you know quickly frame it uh in a way that you know I usually process things.

**Vikram Sekar [00:13:36]:** So one of the biggest problems of modern lithography is cost, and that primarily stems from having to make smaller and smaller transistors.

**Vikram Sekar [00:13:46]:** And we have gone from um deep ultraviolet, which is what we'll refer to as DUV, uh, to eventually extreme ultraviolet, which is what EUV stands for.

**Vikram Sekar [00:13:59]:** And then we have within EUV, we have uh several levels of numerical aperture.

**Vikram Sekar [00:14:05]:** I think we should define what that is, you know, going forward next, so that we actually have all these basic terms in place.

**Vikram Sekar [00:14:11]:** So we have low numerical aperture or low Nae UV and high Na uh EUV and then hyper Nae UV.

**Vikram Sekar [00:14:21]:** And the higher you go from low to high to hyper, you can make smaller and smaller transistors, right?

**Vikram Sekar [00:14:29]:** Yes.

**Vikram Sekar [00:14:30]:** So basically higher the numerical aperture, the smaller the transistors, the smaller the feature sizes you can make.

**Vikram Sekar [00:14:38]:** And now what you need is regardless of whether you choose a deep ultraviolet or an extreme ultraviolet machine, you're gonna have to need like at least 10 or 20 of them in a fab.

**Vikram Sekar [00:14:48]:** And if each of them costs like, I don't know, half a billion dollars, and you want to put in 10 of them, you're spending five billion dollars in just these EOV machines.

**Vikram Sekar [00:14:58]:** And then not only that, you have to put a whole lot of other infrastructure like cooling, uh like clean rooms are difficult because you would have to have the vacuum the HVAC systems that pulls out all of the dust particles from the air.

**Vikram Sekar [00:15:12]:** And so, based on the how many dust particles you can find per unit volume, these clean rooms have different classifications, right?

**Vikram Sekar [00:15:20]:** So you've got class one, class ten, class hundred.

**Vikram Sekar [00:15:24]:** Um, and I think the higher the number, you've got more particles per cubic volume of air.

**Vikram Sekar [00:15:30]:** So all of this stuff takes like an enormous amount of money and time to build.

**Vikram Sekar [00:15:35]:** And if you actually, this is like another point, if you look at like the TSMC's construction of their uh fabs, it's actually critical machines are suspended on pistons, like entire factory floors are suspended on pistons so that it's immune to like earthquakes and stuff.

**Vikram Sekar [00:15:51]:** So it is very expensive to build a fab and takes uh years, it takes years.

**Vikram Sekar [00:15:56]:** I it could take three to five years, uh, you know.

**Vikram Sekar [00:15:58]:** So this is why we can't simply add chip capacity willy-nilly, right?

**Vikram Sekar [00:16:02]:** Totally, totally.

**Austin Lyons [00:16:03]:** And not only that, if if you haven't seen a fab, I'd encourage people to figure out how to get on a fab tour if they can somehow.

**Austin Lyons [00:16:10]:** I know it's very difficult, but I've never been in one.

**Austin Lyons [00:16:13]:** Vic Vic wants to go.

**Austin Lyons [00:16:15]:** Um, I I actually had the good fortune recently of getting to go to Intel's uh Fab 52 and tour it.

**Austin Lyons [00:16:22]:** But a fab, you also need a so not only do you not want the machines to move around even a tiny bit from earthquakes, but even from like passing traffic and stuff, because of course we're making transistors on like the atomic scale, nanometer scale, and so you just you don't want all that any sort of mechanical wiggling and movement.

**Austin Lyons [00:16:41]:** But you also uh these EUV machines, they have like big power sources, and those uh to the in the light source, like a lot of that actually goes in the um subfab floor.

**Austin Lyons [00:16:54]:** So there's a floor beneath, like the main floor where the tool sits, and they have all this equipment underneath it.

**Austin Lyons [00:17:00]:** And then, of course, you know, there's like a floor above it, and you've got you've got to flow all that air through.

**Austin Lyons [00:17:05]:** And so I just also wanted to illustrate that it's not just like um like data centers where you're just like, oh, find some real estate, slap a building up, throw some racks in, and you're good.

**Austin Lyons [00:17:14]:** But yes, it takes uh even from a construction and HVAC perspective, building a fab is is no joke.

**Vikram Sekar [00:17:22]:** And it goes beyond that because if you look at Intel fabs and the way they've built it in the past, they had this copy exactly method, which means they copy exactly.

**Vikram Sekar [00:17:32]:** This is not something that they mess around with.

**Vikram Sekar [00:17:35]:** They use like similar plumbing.

**Vikram Sekar [00:17:39]:** I've heard that they even use the same brand of paint because they do not want anything to go wrong.

**Vikram Sekar [00:17:45]:** Because if small things happen and change the way a fab functions, you can't get the yield up.

**Vikram Sekar [00:17:51]:** And if you can't get the yield up after spending$20 billion, you can't make enough wafers, which means you can't sell them and make a profit.

**Vikram Sekar [00:17:58]:** So Intel decided to copy exactly, and that actually slowed a lot of stuff down for them.

**Vikram Sekar [00:18:03]:** That's a different story, but really, that's how difficult it is to build a fab.

**Vikram Sekar [00:18:06]:** Really, I mean that's that's insane.

**Austin Lyons [00:18:09]:** Totally, totally.

**Austin Lyons [00:18:10]:** So, all right, going back, you mentioned DUV and EUV, and so let's tell listeners a little bit.

**Austin Lyons [00:18:16]:** So, back in the DUV days, the light source that was used um had uh a wavelength that eventually made its way to 193 nanometers.

**Austin Lyons [00:18:28]:** And I guess even zooming out even further, so lithography at the end of the day, for those who don't know, I think everyone probably does these days because ASML is an awesome company and everyone wants to invest or has invested, and so at a high level understands what lithography is.

**Austin Lyons [00:18:40]:** But we're talking about ultimately being able to expose light to sort of, and I put in quotes, uh draw, you know, the shape of transistors or the shape of areas that you want to etch away that you will leave parts of the transistor, but etch away other parts of the surface of the chip.

**Austin Lyons [00:18:59]:** And so ultimately, to make transistors smaller and smaller, um, you can either make the wavelength of ultimately you need to make the wavelength of light smaller and smaller.

**Austin Lyons [00:19:10]:** Um, but there's also something which we can get into, which is the numerical aperture, the mirrors that you talked about making on changing the numerical aperture, but just focusing on making the wavelength of the light smaller.

**Austin Lyons [00:19:22]:** You know, the canonical example here is like writing with a Sharpie, you're gonna draw like fat lines.

**Austin Lyons [00:19:28]:** And if you can write with a fine tip marker, a fine tip pen, you can ultimately make a lot thinner lines and you could draw smaller precision features.

**Austin Lyons [00:19:38]:** So that's what the industry was trying to go to from deep DUV, um, deep ultraviolet lithography, to EUV, which uses 13.5 nanometer light.

**Austin Lyons [00:19:51]:** So ultimately you're going in order of magnitude smaller from the fat marker down to the fine-tip pen.

**Vikram Sekar [00:19:57]:** Yeah.

**Vikram Sekar [00:19:58]:** So this whole relationship that you main you mentioned here, where you want a smaller wavelength of light, but you want a higher numerical aperture.

**Vikram Sekar [00:20:08]:** This is governed by what uh is known as the Raleigh criterion, which means that the smallest dimension you can make on a wafer is literally proportional to the you know wavelength, but inversely proportional to the numerical aperture.

**Vikram Sekar [00:20:23]:** There is also a constant factor here that's often called K1, which we won't get into here, but think of it as another knob which you can use by designing the masks that you know selectively allow light or don't allow light in regions.

**Vikram Sekar [00:20:41]:** You know, they do all kinds of tricks on those masks to improve this proportionality factor K1.

**Vikram Sekar [00:20:46]:** We won't get into it, but these are the factors.

**Vikram Sekar [00:20:50]:** So there are some bunch of tricks, then there's the wavelength, and then there's a numerical aperture.

**Vikram Sekar [00:20:54]:** So the smaller the wavelength you go, the better.

**Vikram Sekar [00:20:57]:** And to Austin's point here, deep ultraviolet lithography was most uh famously you know ended at what is called uh argon fluoride lithography, is that right?

**Vikram Sekar [00:21:10]:** At 193 nanometers.

**Vikram Sekar [00:21:12]:** And then there was a like a quantum leap down to 13.5 nanometers with ultra EUV with extreme ultraviolet.

**Vikram Sekar [00:21:22]:** So that's a big change.

**Vikram Sekar [00:21:23]:** That's like more than a 10x change, right?

**Vikram Sekar [00:21:26]:** And going down another 10x hasn't happened yet, but we will get to how that can happen at the end of this episode.

**Vikram Sekar [00:21:32]:** But yes, so keep going.

**Vikram Sekar [00:21:34]:** Let's let's go with it.

**Austin Lyons [00:21:35]:** Okay, yeah, let's let's let's talk about DUV for a second.

**Austin Lyons [00:21:38]:** Um, so do you want to explain like where the 193 nanometer light comes from with argon fluoride?

**Vikram Sekar [00:21:47]:** Yeah, there was a whole uh there was a whole evolution to that as well.

**Vikram Sekar [00:21:50]:** It's not like we we just landed up there right, you know, when we started lithography.

**Vikram Sekar [00:21:56]:** Like in the 1980s, it was mostly like Like what was called eyeline lithography, which had a wavelength of like 365 nanometers.

**Vikram Sekar [00:22:06]:** Then over the years, people realized like, wait, we've got to make this better.

**Vikram Sekar [00:22:11]:** Um, and then they came up with um you know krypton fluoride uh lithography, KRF lithography that went to you know 248 nanometers.

**Vikram Sekar [00:22:20]:** So just by changing the kind of uh light source that you're shining through and the wavelengths of the light source, you could get better features.

**Vikram Sekar [00:22:26]:** So this was like going through the 90s, you could have like 248 nanometers.

**Vikram Sekar [00:22:31]:** That evolved to like uh argon fluoride lithography, where they went to you know 193 nanometer, and that was pretty cool, but then uh that lasted all the way through the 2000s, let's say.

**Vikram Sekar [00:22:45]:** And kind of they kind of ran out of light sources.

**Vikram Sekar [00:22:48]:** They did try some other light sources uh along the way, but they didn't really like work out for various reasons.

**Vikram Sekar [00:22:55]:** Um, and then they were kind of stuck with like argon fluoride for a while, but then like they thought about it and were like, how do we improve numerical aperture?

**Vikram Sekar [00:23:03]:** Somehow we have to improve it.

**Vikram Sekar [00:23:05]:** And the the answer was extreme, actually.

**Vikram Sekar [00:23:08]:** It's amazing.

**Vikram Sekar [00:23:08]:** If you come to think of the history of lithography, it's insane.

**Vikram Sekar [00:23:12]:** Some smart guy came up with the idea and said, How about we put water on the wafer?

**Vikram Sekar [00:23:18]:** Like, we let's just put water on it.

**Vikram Sekar [00:23:19]:** Like, what do you mean you're gonna put water?

**Vikram Sekar [00:23:20]:** So, yeah, that's literally what they did.

**Vikram Sekar [00:23:23]:** They put extremely pure water on top of the mask and then put the light through the water onto the mask.

**Vikram Sekar [00:23:30]:** And that came to be called like immersion lithography.

**Vikram Sekar [00:23:32]:** So that actually helped scale transistors further by just like putting water on the wafer.

**Vikram Sekar [00:23:37]:** It's like insane, right?

**Vikram Sekar [00:23:39]:** So the the history of lithography is amazing.

**Vikram Sekar [00:23:42]:** I wanted to tell you the way it all started, I don't know if you know this, but the way it all started was in the early days, uh I I forget the name of this guy, but you know, uh look out on semi-doped.

**Vikram Sekar [00:23:57]:** We'll we'll have a poll post on this thing.

**Vikram Sekar [00:24:00]:** The main idea of making masks and making transistors smaller came about because this guy, I think he was working for TI, came about uh and he was looking at a microscope, and he was like, wait a minute, if I can flip the microscope over and shine light from the other side, it gets smaller, right?

**Vikram Sekar [00:24:19]:** Everybody knows you look the wrong way at these things, like stuff gets smaller.

**Vikram Sekar [00:24:22]:** I'm like, this is it.

**Vikram Sekar [00:24:22]:** Like I'm gonna turn the microscope upside down and shine light through the wrong end, and everything gets smaller.

**Vikram Sekar [00:24:28]:** And that that's how all of lithography came about by turning the optics in lithography came about because this one guy had the idea to turn the microscope upside down.

**Vikram Sekar [00:24:37]:** So that's how it all started, right?

**Vikram Sekar [00:24:39]:** And then we've been continuously going down the path of these various laser materials, down to putting immersion lithography with water, and ultimately coming down to like extreme ultraviolet lithography, which is an engineering feat that is uh an achievement for like humankind.

**Vikram Sekar [00:24:56]:** That's how big it is.

**Vikram Sekar [00:24:56]:** We'll talk about it too, but yeah.

**Austin Lyons [00:24:58]:** Yes, yes.

**Austin Lyons [00:24:59]:** So, yeah, Vic, you make some interesting points here, which optical lithography, it's all about light sources and about the optics, about the mirrors, about how do you bend the light.

**Austin Lyons [00:25:10]:** And so when you talk about uh yeah, the guy having the insight of like, oh, when I look at a microscope, it makes small things seem bigger.

**Austin Lyons [00:25:18]:** So if I flip that lens, I could make big things seem smaller.

**Austin Lyons [00:25:22]:** What an amazing way to take a big mask and make it smaller to be patterned.

**Austin Lyons [00:25:27]:** And then ultimately, uh, you know, when you're talking about, you know, moving through um various materials uh and getting unlocking smaller wavelengths, we're talking about lasers.

**Austin Lyons [00:25:39]:** These are light sources to shine through the optics that we've been talking about.

**Austin Lyons [00:25:43]:** And ultimately, the industry was just playing with like, what are different materials that can lase at lower and shorter and shorter wavelengths?

**Austin Lyons [00:25:51]:** Um, and this actually leads me to, you know, we got to argon fluoride, 193 nanometer, um, and the industry sort of stuck for a while, waiting to figure out what's that next way of unlocking even lower, even shorter wavelengths, um, ultimately EUV as we know it today, which we'll get into.

**Austin Lyons [00:26:10]:** Um, but in the meantime, the industry came up with this nice trick called multi-patterning.

**Austin Lyons [00:26:17]:** And I thought I'd explain it really quickly because there's also economic trade-offs to multi-patterning.

**Austin Lyons [00:26:23]:** So, multi-patterning is ultimately about like the question is how do you draw smaller than the single wavelength features?

**Austin Lyons [00:26:32]:** How would, for example, um, here, let me let's let's come up with an analogy.

**Austin Lyons [00:26:37]:** Let's say you're drawing the lines on a football field, like an American football field, you know, the end zone, zero-yard line, 10 yard line, 20-yard line, so on and so forth.

**Austin Lyons [00:26:47]:** And maybe you have a machine that is like, I don't know, really fat and it can only draw a line every 10 yards, you know, the 10-yard line, 20 yard line.

**Austin Lyons [00:26:56]:** Well, then maybe the coach comes to you and says, Oh, hey, we also need uh markers at the five-yard line and the 15-yard line and the 25-yard line.

**Austin Lyons [00:27:04]:** And at first you're like, well, wait, my machine, it can only print them every 10 yards.

**Austin Lyons [00:27:08]:** Like, how am I gonna possibly do that?

**Austin Lyons [00:27:10]:** And then some clever person comes up and says, Oh, well, just draw 10, 20, 30, 40, and then go back to start and scooch it over five yards and draw five, 15, 25, 35.

**Austin Lyons [00:27:23]:** And ultimately, when you're it takes twice as many steps, but instead of having to get a new machine that can now print every five yards, zero, five, ten, fifteen, twenty, you just draw them every 10 yard space, and then you offset by five yards, and then you draw 15, 20, 20.

**Austin Lyons [00:27:39]:** So when you zoom out and you're done, you're like, wait a minute, now I've drawn lines every five yards, even though I didn't have to get a new machine.

**Austin Lyons [00:27:45]:** And that's like a very crude analogy for what's going on in multi-patterning, which is drawing features in step one that are only spaced at the distance that you can comfortably make, and then coming back in with another step and drawing a second set of features and just offsetting it.

**Austin Lyons [00:28:03]:** And so the amazing thing is with a trick like multi-patterning, you can unlock shorter dimensions between the drawn features, but of course, the uh economic cost to this is it takes twice as many steps or it decreases your throughput by half.

**Vikram Sekar [00:28:21]:** Awesome.

**Vikram Sekar [00:28:22]:** So I love the analogy, by the way.

**Vikram Sekar [00:28:23]:** That's like a super cool way to understand it.

**Vikram Sekar [00:28:26]:** Um so what you're saying is basically you can do uh a coarse etch, scooch it over, do a coarse etch again, and what you're left with is like a fine etch.

**Vikram Sekar [00:28:38]:** Because you can now by scooching over somewhere in between the last two etches, you can get a you know finer spot, you know.

**Vikram Sekar [00:28:46]:** And uh if I remember the right, this terminology is called litho h, litho etch.

**Vikram Sekar [00:28:50]:** So you'll see this as L-E-L-E, right?

**Vikram Sekar [00:28:53]:** Is this the same thing I'm talking about?

**Vikram Sekar [00:28:55]:** Yes, exactly.

**Vikram Sekar [00:28:56]:** You you nailed it.

**Vikram Sekar [00:28:57]:** Okay, cool, cool.

**Vikram Sekar [00:28:58]:** Now, I think that people have taken this to more than two levels of litho h, right?

**Vikram Sekar [00:29:03]:** They've gone to like triple patterning and even quad patterning, which is all cool and all because now we you're stuck with two problems.

**Vikram Sekar [00:29:12]:** One, it becomes increasingly difficult to even align masks between the yard lines.

**Vikram Sekar [00:29:17]:** Like, okay, like when you had to align the mask at like the 15-yard line, it was okay, okay, whatever, it was between 10 and 20.

**Vikram Sekar [00:29:23]:** But now you want to align it at, you know, 12, 14, 16, 18.

**Vikram Sekar [00:29:28]:** And you're like, okay, that's the problem.

**Vikram Sekar [00:29:30]:** The second problem is you're going to run through four different quad patterning steps, which each one takes the same time, so it's kind of scales linearly.

**Vikram Sekar [00:29:39]:** And now it takes four times as much time to make that one lithography step.

**Vikram Sekar [00:29:45]:** Um, and I'm not sure like how many levels this can be applied to quad patterning, but you know, making a transistor isn't like one etching step or one lithography step.

**Vikram Sekar [00:29:55]:** There are many of them.

**Vikram Sekar [00:29:56]:** And if you have to quad pattern on multiple steps, it adds up a whole lot of time.

**Vikram Sekar [00:30:00]:** And the throughput decreases, which means uh the cost per transistor goes up, or you don't get enough amortization of your original 20 billion investment.

**Vikram Sekar [00:30:11]:** And now we are at like a crossroads here.

**Austin Lyons [00:30:13]:** Yes, yes.

**Austin Lyons [00:30:14]:** And um, case in point, I know SMIC had to, which is the fab in China, um, they're not allowed to get EUV, and so they were able to take DUV and use tricks like quad patterning to get to you know seven nanometer class and then five nanometer class transistors, um, which I wanted to point out, by the way, because it's related to lithography.

**Austin Lyons [00:30:39]:** Um nowadays, when we're talking about making transistors, it's no longer just like two-dimensional transistors, but it's really three-dimensional transistors with thin fets that have these fins.

**Austin Lyons [00:30:49]:** We should find some pictures and you know, people go Google it, and ribbon fets.

**Austin Lyons [00:30:53]:** Um, and so now you've got these three-dimensional shapes.

**Austin Lyons [00:30:56]:** So it's also making a transistor actually takes on the order of like 60 or 70 or 80 steps because you have to pattern and etch and deposit material um kind of over and over and over to build up this 3D-shaped transistor.

**Austin Lyons [00:31:12]:** Um, so it's not only which, but but there's a kind of a marketing thing that um, like you know, the semiconductor tourists, for lack of a better word, which just means you're new to semis, it's no shade.

**Austin Lyons [00:31:23]:** We have a I was a semi-tourist at one point.

**Austin Lyons [00:31:25]:** You're welcome.

**Austin Lyons [00:31:26]:** Everybody's welcome into semiland.

**Austin Lyons [00:31:27]:** We love it.

**Austin Lyons [00:31:28]:** That's this podcast exists for you.

**Austin Lyons [00:31:30]:** Um very inclusive.

**Austin Lyons [00:31:31]:** Yeah, exactly.

**Austin Lyons [00:31:33]:** When a fab says we make two nanometer transistors or 1.8 nanometer transistors, it's not the smallest dimension, this you know, critical dimension, like we talked about before, the distance between any two really close lines is not two nanometers.

**Austin Lyons [00:31:49]:** It used to be, you know, like back when they were 90 nanometers uh and 180 nanometers and 45 nanometers, that was a lot closer, but it became a marketing term.

**Austin Lyons [00:31:59]:** And so actually, something that's called two nanometers, the smallest dimension may still be on the order of like 30 nanometers.

**Vikram Sekar [00:32:07]:** Yeah, yeah.

**Vikram Sekar [00:32:08]:** So it's not exactly two, but that's how we now call it because it's somehow the equivalent of two.

**Austin Lyons [00:32:16]:** Correct, correct, yeah, correct, right?

**Austin Lyons [00:32:18]:** It's like the equivalent of like when you think about like transistor density and whatnot.

**Austin Lyons [00:32:23]:** But I'll say it's important because you know, naturally, when we say 13.5 nanometer um EUV wavelength, someone might go, oh well, that's still way too big to draw two nanometer lines.

**Austin Lyons [00:32:36]:** But it's it's not exactly.

**Austin Lyons [00:32:38]:** So you might think then, oh, if we went from big fat marker DUV to fine-tip sharpie EUV, we must not have to multi-pattern anymore, right?

**Austin Lyons [00:32:48]:** And actually, your intuition is correct, but from a resolution perspective, we don't have to, but actually from a yield perspective, the industry um can still need to rely on some multi-patterning.

**Austin Lyons [00:33:03]:** Um, and there's a really nice graphic from Fred Chen's Substack.

**Austin Lyons [00:33:06]:** He wrote a nice article on it.

**Austin Lyons [00:33:07]:** We'll link to it in the show notes.

**Austin Lyons [00:33:09]:** But ultimately, we are getting so small that when you're shining very short wavelength light um at a certain dose, there's only really so many photons that are that are hitting there, and you can only control them so precisely, and you've got like resist chemist chemistry going on, and there might be some ideally there's not there might be some impurities or even dopants in the way, and so you end up getting like this stochastic nature.

**Austin Lyons [00:33:35]:** When you draw with the Sharpie, you don't actually get a very fine line, but if you zoom in, there's some little dots around the edges and stuff.

**Austin Lyons [00:33:43]:** Um, think of I don't know, maybe like spraying with a spray paint can or something.

**Austin Lyons [00:33:47]:** It's like not a perfect line, you know.

**Vikram Sekar [00:33:49]:** I'm I'm looking at the picture and I was thinking of spray paint exactly.

**Vikram Sekar [00:33:52]:** So if you didn't you always nail these analogies, and I was like, I'm gonna nail the spray paint analogy.

**Austin Lyons [00:33:56]:** I'm I stole it from you.

**Austin Lyons [00:33:57]:** I'm I'm sorry.

**Austin Lyons [00:33:58]:** Yeah, so ultimately, yeah, that's what they do is basically you might draw with the spray paint twice to get a better defined line, especially as you're starting to go in three dimensions.

**Austin Lyons [00:34:10]:** Um, so I just wanted to throw that in there to mention that yes, we now we've jumped up to these, you know,$300 million,$400 million EUV tools, but it the throughput isn't just immediately solved because there's still some multi-pattering that may have to happen.

**Austin Lyons [00:34:26]:** Um and there's other things about the power of the light source and the dose, but we won't get into those now because we're really starting to get into the weeds.

**Austin Lyons [00:34:33]:** Um but okay, what do you say we jump in?

**Austin Lyons [00:34:36]:** Should we talk about high NA next?

**Austin Lyons [00:34:40]:** Um, or do you have anything else to add here that's useful at a high level?

**Vikram Sekar [00:34:45]:** I think that we should conclude before we talk about NA, we should talk about how we can generate light at 13.5 nanometers in UV.

**Vikram Sekar [00:34:56]:** Because we mentioned that these were like laser light sources based on argon fluoride lasers.

**Vikram Sekar [00:35:02]:** But um it's quite different when it comes down to 13.5 nanometer UV, and that is where the hardest uh innovation actually was um holding back the industry from going to this for a very long time.

**Vikram Sekar [00:35:18]:** And fundamentally, what in a simple way, it's far more complex than I'm explaining it, but in a simplest way, it is basically tin droplets uh that you know fall through a chamber, and you hit it with um laser light and it gets activated, and then you hit it again with a laser light.

**Vikram Sekar [00:35:38]:** Remember, you have to hit a falling tin droplet that's about 50 micron in size twice as it falls through this you know chamber, and the second time it gives you an explosion of 13.5 nanometer light.

**Vikram Sekar [00:35:50]:** And that keeps happening precisely.

**Vikram Sekar [00:35:52]:** Uh, ASML has an awesome video on their website where you can see these tin droplets falling.

**Vikram Sekar [00:35:58]:** It's it's an animation, you can't really see this thing.

**Vikram Sekar [00:36:01]:** But then these droplets are falling, and these like laser sources are like continuously hitting the droplets, and you see these explosions of EUV light.

**Vikram Sekar [00:36:08]:** That is then it goes through like a mirroring, it goes through like 13 different mirrors because it has to be focused ultimately onto the wafer.

**Vikram Sekar [00:36:15]:** And then ultimately it lands up on the wafer where it hits a mask and then it selectively exposes or doesn't expose stuff.

**Vikram Sekar [00:36:22]:** But this whole power that this you went, you the one of the big problems is that you went through all this trouble to get extreme ultraviolet light by you know shooting thin lasers, but then you reflect it through so many mirrors, and at each reflection you lose some power.

**Vikram Sekar [00:36:38]:** Like less, like a single digit percentage of the actual generated EUV power actually gets to the wafer.

**Vikram Sekar [00:36:44]:** It's a big loss because of these mirrors.

**Vikram Sekar [00:36:46]:** There's literally no way around it, or so we think.

**Vikram Sekar [00:36:49]:** But yeah, that's what I wanted to talk about because now that we've finished talking about how lasers entirely work and how light sources work, numerical aperture is a good transition to get into right now.

**Austin Lyons [00:36:59]:** Yes, no, this is good.

**Austin Lyons [00:37:01]:** You I tried, I almost skipped over EUV entirely, uh, at least low N at EUV.

**Austin Lyons [00:37:05]:** So it's a good introduction, which is we were stuck at DUV, we tried multi-patterning.

**Austin Lyons [00:37:10]:** In the meantime, the industry was trying to work on EUV.

**Austin Lyons [00:37:13]:** And as Vic talked about, you know, ultimately we're trying to find a light source that has a much shorter wavelength.

**Austin Lyons [00:37:18]:** And, you know, there work had been done that show that showed with tin you could um basically induce a plasma, like that's why you hit it twice ultimately, and that plasma would generate 13.5 nanometer wavelength light.

**Austin Lyons [00:37:33]:** But there was a lot of engineering challenges and optics challenges around, okay, great.

**Austin Lyons [00:37:38]:** Yes, when we're under vacuum, we can generate a plasma and we and it will emit this really low wavelength light, short wavelength light.

**Austin Lyons [00:37:46]:** But how do we ultimately harvest all that light?

**Austin Lyons [00:37:49]:** How do we reflect it back and then use, you know, with mirrors, like aim it?

**Austin Lyons [00:37:54]:** Ultimately, you need to like gather this light because it's just gonna shoot in any direction, presumably from the tin droplets.

**Austin Lyons [00:38:00]:** And you need to gather it all, and then you need to like get it to where it needs to be, to where the mask is ultimately.

**Austin Lyons [00:38:06]:** And in in while you're doing that, you're trying to focus all the light.

**Austin Lyons [00:38:09]:** And like Vic said, there's a lot of losses.

**Austin Lyons [00:38:12]:** Every time light hits a mirror, it's not gonna all bounce perfectly exactly in the direction that you want.

**Austin Lyons [00:38:18]:** There's gonna be some scattering and some loss.

**Austin Lyons [00:38:20]:** And so then ultimately you end up losing so much light in the process that you don't have enough to like uh expose the photoresist.

**Austin Lyons [00:38:29]:** And so then the question is that the industry was working on for a long time is not only how do we just make all this work and repeatedly, but also how do we increase the light source so that we ultimately, by the time we harvest all this light, get it exactly where we need to, get it focused all the way down, we still have enough to actually expose the photoresist and draw the transistor.

**Austin Lyons [00:38:49]:** So that, of course, that's why we're stuck at DUV for a while, because this is an amazing engineering feat.

**Austin Lyons [00:38:54]:** And of course, it takes, read the book Focus by Martin something, I don't remember his last name, but it's about ASML.

**Austin Lyons [00:39:00]:** And what's really interesting is it talks about the entire supply chain and all the co-innovation needed.

**Austin Lyons [00:39:05]:** For example, famously from Zeiss with their mirrors.

**Austin Lyons [00:39:09]:** Um it's so it's it's no joke to even build the laser uh produced plasma light source, but then you have all the optics, and of course, there's something called a scanner.

**Austin Lyons [00:39:20]:** We won't talk about it a ton, but ultimately the mask, you're patterning, you don't want to just pattern one, you don't pattern like one die or one chip, you pattern a die on the chip, and then you like we talked about before, it's like a checkerboard pattern on a big dinner plate.

**Austin Lyons [00:39:34]:** You need to draw these transistors for every checkerboard square.

**Austin Lyons [00:39:38]:** So you need some like um mechanical, you know, mechatronics that ultimately move the everything around so that you can repeatedly print all of this.

**Austin Lyons [00:39:50]:** So there's a ton of engineering to make this even possible.

**Vikram Sekar [00:39:53]:** Yeah, that's insane.

**Vikram Sekar [00:39:55]:** That's what 39.5 nanometer EUV make.

**Vikram Sekar [00:39:58]:** It's an incredible feat of engineering.

**Vikram Sekar [00:40:00]:** And um we are here today because ASML took 20 years to develop this.

**Vikram Sekar [00:40:09]:** And uh the the whole question of how come ASML landed up with this uh is another interesting question because uh this technology was actually developed in the United States.

**Vikram Sekar [00:40:22]:** And at some point it was sold to ASML, and at that time the United States government didn't actually come in and say, no, this is critical technology, we want to hold it.

**Vikram Sekar [00:40:34]:** You know, the US government has blocked many such things before, like including like protecting 5G technology.

**Vikram Sekar [00:40:39]:** They've done all of this stuff.

**Vikram Sekar [00:40:40]:** Even now, they have like there's so much export control.

**Vikram Sekar [00:40:42]:** This was like before the day of export control.

**Vikram Sekar [00:40:45]:** So we, as you know, from the United States have handed over the uh keys to the kingdom to ASML like a few decades ago.

**Vikram Sekar [00:40:56]:** And to kudos to them, they spent like 20 years developing it.

**Vikram Sekar [00:40:59]:** And there's an enormous supply chain that goes into ASML's uh machines that all need to come together to make this work.

**Vikram Sekar [00:41:06]:** So it's it's built on a massive amount of effort.

**Vikram Sekar [00:41:10]:** But I just wanted to point out that this was actually US technology at one point.

**Austin Lyons [00:41:14]:** Totally.

**Austin Lyons [00:41:15]:** Yeah, that's a good, a great history lesson there.

**Austin Lyons [00:41:18]:** Of course, we should write more about that history sometime.

**Austin Lyons [00:41:20]:** Um, okay, so we're running long, but let me blow through.

**Austin Lyons [00:41:24]:** So, okay, wow, it's an engineering marvel to get 13.5 nanometer light, but we want to make transistors smaller.

**Austin Lyons [00:41:30]:** What do we do?

**Austin Lyons [00:41:31]:** Okay, like we talked about with the Raleigh criterion, um, you ultimately have two big knobs that you can turn.

**Austin Lyons [00:41:38]:** One is the wavelength of light, but if you're like, dude, we spent so long to get here, we're not just gonna turn that all of a sudden.

**Austin Lyons [00:41:45]:** Just 13.5 was hard enough.

**Austin Lyons [00:41:47]:** The other um knob is the numerical aperture, which ultimately has to do with like the size of mirrors.

**Austin Lyons [00:41:54]:** Um, and so that's where we get into high NA and extreme, like extreme NA or whatever it was called, hyper NA.

**Austin Lyons [00:42:01]:** Um, but but but maybe really quick, the industry's trying to move from 0.33 numerical aperture in low NA to 0.55 in high NA, which makes features on the order of like one and a half, 1.7 times smaller possible.

**Austin Lyons [00:42:17]:** But there's a catch.

**Austin Lyons [00:42:18]:** There's always a catch in engineering, there's always trade-offs.

**Austin Lyons [00:42:21]:** You need bigger mirrors.

**Austin Lyons [00:42:22]:** When you have bigger mirrors, you've got these steeper light angles ultimately as they bounce in, and you have something called anamorphic optics that come into play.

**Austin Lyons [00:42:31]:** Um, and I won't get way in into how that works and what that means, other than to say you ultimately end up can you can only pattern an area that's like half the size of what you could with low NA.

**Austin Lyons [00:42:44]:** They call this the half field.

**Austin Lyons [00:42:45]:** So basically, now instead of your$250 million machine printing an area, you've got you know a$400 million machine printing half the area.

**Austin Lyons [00:42:53]:** Of course, that sounds horrible.

**Austin Lyons [00:42:56]:** Now you need, you're telling me I need, okay, Mr.

**Austin Lyons [00:42:58]:** Salesman, I just bought a$250 million machine from you, and now you say I need not only your$400 million machine, but I need two of them, right?

**Austin Lyons [00:43:05]:** That's crazy.

**Austin Lyons [00:43:06]:** So what um ASML has done a ton of amazing engineering where they've said, yes, we can only do a smaller size, but what if we speed up like the scanner and the mechatronics to go even faster to make up for it?

**Austin Lyons [00:43:17]:** So it's like, sure, we we keep this the area is gonna be smaller, but we're just gonna move that thing around the wafer even faster.

**Austin Lyons [00:43:23]:** And again, um ASML has all these amazing videos on YouTube where they show like how fast they're accelerating and moving this stuff, and it's crazy.

**Austin Lyons [00:43:32]:** It's like fighter jet style acceleration, but with nanometer precision, moving things perfectly around, stopping and reversing, like it's crazy that it all works.

**Austin Lyons [00:43:41]:** But again, things are expensive, there's more trade offs, there's a lot more innovation that needed to happen.

**Austin Lyons [00:43:46]:** And ultimately, even with the proposed hyperNA, even bigger mirrors, there's even more trade offs, um, even with stuff like photo resist.

**Austin Lyons [00:43:56]:** Um, so I'll probably just leave it at that and we won't do dive on high end.

**Austin Lyons [00:44:00]:** Or hyperNA, but just trying to illustrate that like not only are there economic challenges, but there's also just like engineering challenges, probably presumably reliability challenges.

**Austin Lyons [00:44:10]:** So then we'll leave you with this.

**Austin Lyons [00:44:13]:** The question is: well, instead of the mirrors, could we make the wavelength smaller?

**Austin Lyons [00:44:17]:** How could we make the wavelength smaller?

**Vikram Sekar [00:44:20]:** Yeah, I want to add one more thing about the mirrors that's like an engineering challenge, but then we're going to go and talk about how to go even smaller wavelengths, right?

**Vikram Sekar [00:44:30]:** These mirrors are not simple.

**Vikram Sekar [00:44:31]:** You just, it seems like, what's the big deal going from low NA?

**Vikram Sekar [00:44:35]:** You just have to make a bigger mirror.

**Vikram Sekar [00:44:36]:** Make a bigger mirror.

**Vikram Sekar [00:44:37]:** What's the problem?

**Vikram Sekar [00:44:38]:** These are not ordinary mirrors because they are actually made up of multiple layers of 40, there's like 40 or 50 layers of alternating layers of very thin molybdenum and silicon layers.

**Vikram Sekar [00:44:52]:** They are layered like this, and it is insanely smooth.

**Vikram Sekar [00:44:56]:** And I read this book, Chip War by Chris Miller.

**Vikram Sekar [00:45:00]:** It's a good book, I recommend it.

**Vikram Sekar [00:45:02]:** It talks through a lot of history, and a lot of what I've said here is from that book.

**Vikram Sekar [00:45:07]:** And I have a quote here from that book.

**Vikram Sekar [00:45:09]:** It says, if the mirrors in the EUV system were scaled to the size of Germany, their biggest irregularities would be a tenth of a millimeter.

**Vikram Sekar [00:45:20]:** Think about that.

**Vikram Sekar [00:45:21]:** Think about how flat those mirrors are.

**Vikram Sekar [00:45:23]:** Yeah.

**Vikram Sekar [00:45:24]:** And we're going to put up a picture here, and you'll see like, you know, how how smooth it is.

**Vikram Sekar [00:45:30]:** It is very difficult to even hold this thing.

**Vikram Sekar [00:45:32]:** And I feel like I wouldn't even want to breathe on it, like at this level.

**Vikram Sekar [00:45:37]:** I don't know.

**Vikram Sekar [00:45:37]:** They probably have protection, protective gear.

**Vikram Sekar [00:45:39]:** But making bigger mirrors isn't easy.

**Vikram Sekar [00:45:41]:** It is an incredible engineering feat to make irregularities a tenth of a millimeter when the mirror scale is the size of Germany.

**Vikram Sekar [00:45:50]:** That's that's really flat, right?

**Vikram Sekar [00:45:52]:** So that's very smooth surface.

**Vikram Sekar [00:45:56]:** So it's not simple that we can go from a 0.55 Na, which is like hyper Na, to like 0.75 like next year.

**Vikram Sekar [00:46:04]:** You know, if we are used to like the incredible pace of AI.

**Vikram Sekar [00:46:07]:** Everybody's like, oh, what's the big deal?

**Vikram Sekar [00:46:09]:** Like we can go to like 3.2T, 6.4T, 12.8T networking, right?

**Vikram Sekar [00:46:13]:** No problem.

**Vikram Sekar [00:46:13]:** Like, when are we gonna get there?

**Vikram Sekar [00:46:15]:** Like, you know, two years, three years, what's the time frame?

**Vikram Sekar [00:46:17]:** No, no, this stuff is difficult.

**Vikram Sekar [00:46:18]:** You cannot make a mirror that simply, that easily.

**Vikram Sekar [00:46:21]:** So that's where we are right now.

**Vikram Sekar [00:46:24]:** And now the question is, what's next?

**Vikram Sekar [00:46:26]:** Like a machine costs a billion dollars, and now you tell me like this is only half field, and now I need two billion dollar machines.

**Vikram Sekar [00:46:34]:** It's just like the economics is exploding.

**Vikram Sekar [00:46:37]:** Something is going wrong.

**Vikram Sekar [00:46:38]:** And so this is where we have new ideas to go where no human has gone before.

**Austin Lyons [00:46:45]:** Totally.

**Austin Lyons [00:46:45]:** So, okay, transitioning here, people will say you could never compete with ASML.

**Austin Lyons [00:46:51]:** It took the industry so long to figure out this 13.5 nanometer light, and they have a supply chain like they have a relationship with Zeiss, the only person in the world who can make these perfect mirrors.

**Austin Lyons [00:47:00]:** Why would Zeiss sell their mirrors to you, dumb startup?

**Austin Lyons [00:47:03]:** Of course they're not, because they don't want to um make ASML mad, right?

**Austin Lyons [00:47:07]:** And so now you're gonna have to go get another person to be the next AS or the next Zeiss, you're gonna be the next ASML.

**Austin Lyons [00:47:14]:** It's never gonna happen, right?

**Austin Lyons [00:47:15]:** And so some startups are saying, okay, hold the phone.

**Austin Lyons [00:47:19]:** Let's just like forget all that.

**Austin Lyons [00:47:20]:** Let's just think simple from um first principles.

**Austin Lyons [00:47:23]:** Could we get a smaller wavelength light?

**Austin Lyons [00:47:26]:** Um, how do we tackle the optics?

**Austin Lyons [00:47:29]:** How do we tackle the integration, the mechatronics, all that stuff?

**Austin Lyons [00:47:32]:** So one startup, X Lite, out of um California, and I think uh Pat Gelsinger is on their board maybe now, maybe he's the chairman of the board or something.

**Austin Lyons [00:47:42]:** Um what they're trying to do is they're saying, hey, what if we use free electron lasers as the light source?

**Austin Lyons [00:47:50]:** So we'll replace LPP, laser-produced plasma, that's the tin droplet, shooting it with the laser machine gun and all the magic that happens.

**Austin Lyons [00:47:58]:** Um, but what if we start by using this different light source that can ultimately, which by the way, a free electron laser, um, it essentially like, think of it as like accelerating electrons to like near light speed.

**Austin Lyons [00:48:11]:** You've got these undulators that like wiggle them, you can get this coherent light.

**Austin Lyons [00:48:15]:** It can ultimately scale down to like one nanometer, sub-1 nanometer.

**Austin Lyons [00:48:18]:** But what if we start by using this new technology but still producing 13.5 nanometer light so that it can plug in to existing ASML scanners and ASML optics?

**Austin Lyons [00:48:32]:** So, what if we could generate light in a new fashion?

**Austin Lyons [00:48:35]:** You know, by the way, FEL has a much higher total power source.

**Austin Lyons [00:48:41]:** So you can what you could ultimately do is have higher dose, which is better for yield.

**Austin Lyons [00:48:45]:** But actually, what X Lite's trying to do is say, what if we use um one free electron laser and we can actually split the beam and feed many EUV scanners?

**Austin Lyons [00:48:56]:** So they're ultimately trying to decouple the light source from the scanner.

**Austin Lyons [00:49:00]:** So what if you could buy um, you know, 10 scanners and feed it with one light source?

**Austin Lyons [00:49:06]:** Or obviously maybe they would have to have two light sources, one as a backup in case one doesn't work.

**Austin Lyons [00:49:11]:** Um, but you get the gist.

**Austin Lyons [00:49:12]:** And so that's the approach they're trying to take is say, hey, what if we build one massive free electron laser next to the fab and pipe the light into all of your ASML scanners?

**Austin Lyons [00:49:22]:** You can amortize the cost of your FEL across all those scanners.

**Austin Lyons [00:49:27]:** Um, and then ultimately it there will be some integration, but we're not gonna ask everyone to change, not only the optics, but the photo resists, and we're not gonna ask anyone else in the industry to change.

**Austin Lyons [00:49:38]:** We are just going to decouple the light source.

**Vikram Sekar [00:49:42]:** That's fancy.

**Vikram Sekar [00:49:43]:** Yeah.

**Vikram Sekar [00:49:43]:** I haven't looked into X Lite, so I'm actually learning on the fly right now.

**Vikram Sekar [00:49:47]:** That's amazing.

**Vikram Sekar [00:49:48]:** One of the things that you can do with a laser source that has a higher output power is that tell me if I'm wrong, if you can get more light onto a wafer, the throughput actually increases, doesn't it?

**Vikram Sekar [00:50:00]:** Not only yield, but the throughput grows up.

**Austin Lyons [00:50:03]:** Correct, correct, correct.

**Austin Lyons [00:50:04]:** The throughput, exactly, exactly.

**Austin Lyons [00:50:06]:** You it um, you know, whatever.

**Austin Lyons [00:50:09]:** If you only need like a small flashlight to shine on something and now you got really powerful light, you could get the same amount of light by actually taking your really powerful light and shining it for less long, exposing it for less long, right?

**Austin Lyons [00:50:21]:** You just like it.

**Vikram Sekar [00:50:22]:** How many photons get in?

**Austin Lyons [00:50:23]:** Yeah.

**Austin Lyons [00:50:24]:** Exactly, exactly, exactly.

**Austin Lyons [00:50:25]:** There, so so therefore you can increase the throughput, but you could say, okay, well, hey, the yield maybe isn't that great at this the way the industry is doing it now.

**Austin Lyons [00:50:35]:** So we'll shine it for just a little bit longer than we need to, and you'll get even more extra photons, right?

**Austin Lyons [00:50:41]:** So you can, you know, have a higher dose, um, but ultimately have a so both better yield and better throughput.

**Vikram Sekar [00:50:48]:** So who would be the end customer of uh X Lite?

**Vikram Sekar [00:50:51]:** Would it be ESML?

**Austin Lyons [00:50:53]:** No, it would be the Fab.

**Austin Lyons [00:50:55]:** So the Fab would be buying, and then the crazy thing, and I wrote about it on Chipstrat, you can go check it out, is the business model here is ultimately selling light sort of like a utility, like photons as a service.

**Austin Lyons [00:51:10]:** So um you might ask, like, okay, well, if why would TSMC go build an FEL from some startup and then they'd have to go like re-jigger, you know, and work with ASML to say, we don't want your um LPP like light sources, we just want your scanner part.

**Austin Lyons [00:51:28]:** And like that seems like a lot of risk and a lot of effort for TSMC.

**Austin Lyons [00:51:31]:** But what if, and a lot of CapEx, by the way, what if um X Lite came in and they said, we will pay to build this utility right next to your fab, just like you get electricity delivered, just like you get water delivered, and even um just like you buy gas.

**Austin Lyons [00:51:46]:** So like uh these fabs, they will buy inputs like gas in sort of this consumption-based way.

**Austin Lyons [00:51:52]:** Let us build uh the FEL, the light source, and then um we will just charge you for what you consume.

**Austin Lyons [00:51:59]:** So it's on our books, we take the CapEx hit, and then we'll just charge you.

**Austin Lyons [00:52:03]:** So if you want to just spin up um three scanners, fine.

**Austin Lyons [00:52:07]:** We'll feed you three scanners.

**Austin Lyons [00:52:09]:** Now, of course, um X Lite wants to ultimately have you spin up as many scanners as possible, but X Lite, there's a way that X Lite can take a lot of the risk and uh do a lot of the upfront investment, and then they will just sell light to TSMC over time.

**Austin Lyons [00:52:24]:** And by the way, then once they build that relationship, not only could they sell you 13.5 nanometer light, but maybe for a premium later, once you and the industry are ready, they could sell you one nanometer light.

**Austin Lyons [00:52:36]:** So it's a very interesting business model.

**Vikram Sekar [00:52:39]:** So the optics and stuff still comes from ASML, but then you've got this uh free electron laser sitting on premises in TSMC, just like supplying light.

**Vikram Sekar [00:52:49]:** So exactly.

**Vikram Sekar [00:52:50]:** You they count the number of photons you use and charge you for it?

**Vikram Sekar [00:52:53]:** Is that the whole business model?

**Austin Lyons [00:52:55]:** Yep, presumably.

**Austin Lyons [00:52:56]:** How they how they do that, how they you know track how much light you're consuming, it would be also very interesting to know.

**Austin Lyons [00:53:03]:** But that's that's exactly it's like your electricity bill at the end of the month is gonna be your light bill, your light for lithography.

**Vikram Sekar [00:53:10]:** Amazing.

**Vikram Sekar [00:53:10]:** So, what what other ways are there to make uh one nanometer wavelength of light?

**Austin Lyons [00:53:15]:** All right, so one more that we'll hit on today.

**Austin Lyons [00:53:17]:** Substrate is another startup.

**Austin Lyons [00:53:19]:** They're also in California, in San Francisco, and um they are throwing out the playbook and also taking a different approach.

**Austin Lyons [00:53:26]:** And instead of FELs, they're saying, hey, what if we use X lay X-ray lithography?

**Austin Lyons [00:53:31]:** Historically, um X X-rays were generated by big synchrotrons, um, football stadium size, you know, particle accelerators essentially.

**Austin Lyons [00:53:44]:** Um, but there's actually precedent.

**Austin Lyons [00:53:46]:** And in those, again, you you speed up these particles, they get super high energy.

**Austin Lyons [00:53:49]:** Super high energy means really short wavelength, and you can ultimately control and use it as a light source.

**Austin Lyons [00:53:56]:** Um, there's actually the industry has actually explored using X-rays as a light source.

**Austin Lyons [00:54:01]:** And again, if you Google chipstrat substrate, you'll find this.

**Austin Lyons [00:54:06]:** I wrote about the history, but IBM did a ton of work.

**Austin Lyons [00:54:09]:** So, again, a lot of this early research happening in the United States, IBM did a ton of work here to see could this be a path forward for the industry?

**Austin Lyons [00:54:17]:** And they actually made um uh synchrotron or an X-ray light source um that fit on a truck.

**Austin Lyons [00:54:25]:** So it's a bit of a myth that it has to be massive.

**Austin Lyons [00:54:27]:** They figured out a way to make it a lot smaller.

**Austin Lyons [00:54:30]:** And this is the approach that Substrate's taking, which says, hey, ultimately I'd I'd phrase it this way.

**Austin Lyons [00:54:38]:** Hey, uh IBM and a bunch of other people back in the 80s and 90s, they explored X-ray lithography, and it was a working prototype.

**Austin Lyons [00:54:46]:** Um, it wasn't economical yet, but a lot has changed in 30 years.

**Austin Lyons [00:54:52]:** Uh uh, not only about light sources, but um with photoresists and with optics and everything else that it takes to build a light source and a scanner and do lithography.

**Austin Lyons [00:55:04]:** What if we went back and revisited from first principles and we took a stab at X-ray again and said, hey, given all that we've learned in the last 30 years, could it now be economically possible to do lithography using um X X-ray, you know, particle accelerator-based X-ray lithography?

**Vikram Sekar [00:55:24]:** Yeah, I wanted to just step back one minute and just quickly explain what a synchrotron is.

**Vikram Sekar [00:55:30]:** The idea of a synchrotron is that you accelerate a charged particle in a ring, right?

**Vikram Sekar [00:55:37]:** In a circle or an ellipse or something like that.

**Vikram Sekar [00:55:40]:** And as the charged particle that is continuously being accelerated turns around and changes angle, it spits out X-rays as it uh turns around.

**Vikram Sekar [00:55:54]:** That's that's basically how a synchrotron works.

**Vikram Sekar [00:55:57]:** And typically, in the past, you know, like you mentioned, they these are really big uh installations, particle accelerators tend to be really big, depending on what energy you have to accelerate them to.

**Vikram Sekar [00:56:09]:** And uh I think they the invention for making tabletop uh synchrotrons has been around already like 20, 30 years.

**Vikram Sekar [00:56:17]:** So it's not something that you really need uh a whole lot of like space to do.

**Vikram Sekar [00:56:24]:** So that's one thing.

**Vikram Sekar [00:56:25]:** So that's very important because people shouldn't be like, oh, what do you mean?

**Vikram Sekar [00:56:29]:** You need a football field, we don't have that kind of space, so we can't do X-ray lithography.

**Vikram Sekar [00:56:32]:** No, no.

**Vikram Sekar [00:56:32]:** I think it I think it's it can be done in a smaller way.

**Vikram Sekar [00:56:36]:** But the one thing that I uh learned when I wrote about this, it's on my sub stack too, about uh substrate and x-ray lithography, is that it's very difficult to like actually focus X-rays.

**Vikram Sekar [00:56:49]:** So, you know, we spoke about the mirrors for EUV lithography, but you can't do that for like um X-rays because they go through things, you can't reflect them.

**Vikram Sekar [00:56:59]:** That's a big problem.

**Vikram Sekar [00:57:00]:** So the optics for X-rays is uh a challenge, it really is a challenge.

**Vikram Sekar [00:57:06]:** So one of the ways that you can do is uh do this is that you have to do what is called proximity printing.

**Vikram Sekar [00:57:12]:** Because, you know, like we mentioned uh earlier, the the the inverted microscope approach means that you could scale down a mask, you could put the mask on the big end of the microscope, and then the other end you know scales down, let's say five times.

**Vikram Sekar [00:57:24]:** Uh that is called um you know uh reductive printing or something.

**Vikram Sekar [00:57:29]:** I forgot the exact term.

**Vikram Sekar [00:57:30]:** Basically, you can reduce the magnification factor by a factor of five because you've got this inverted uh microscope approach.

**Vikram Sekar [00:57:38]:** But uh that by the way, it came to me, the person who did that was Jay Lethra.

**Vikram Sekar [00:57:42]:** Um and so he's the guy who came up with this idea.

**Vikram Sekar [00:57:45]:** It came to me later.

**Vikram Sekar [00:57:46]:** But uh yeah, so you can't do that with X-rays because you there is no optics that works for this.

**Vikram Sekar [00:57:53]:** So you have to do proximity printing, which means that you have got to make masks the same critical dimension as the stuff that you are patterning.

**Vikram Sekar [00:58:02]:** So the masks are actually very fine.

**Vikram Sekar [00:58:04]:** And so for this purpose, the mask making is significantly harder when you're using X-ray lithography because you don't have the optics for them.

**Vikram Sekar [00:58:11]:** So there are a whole lot of challenges that require to be solved.

**Vikram Sekar [00:58:14]:** So it's not just like, oh, we've got X-rays now that go to one nanometer.

**Vikram Sekar [00:58:18]:** So just let's just just swap out uh, you know, the the LPP 13.5 nanometer source for a one nanometer X-ray, and then voila, you can like print, you know, 0.1 nanometer transistors gate all around or whatever it is.

**Vikram Sekar [00:58:34]:** It doesn't work that way.

**Vikram Sekar [00:58:35]:** So once you change the wavelength, everything changes.

**Vikram Sekar [00:58:37]:** And that's where we are now.

**Vikram Sekar [00:58:39]:** And there's this startup called Substrate that's working on this.

**Vikram Sekar [00:58:42]:** They made quite a splash sometime back because they feel that not only can they make smaller transistors and continue to scale Moore's law, but X-ray lithography can be significantly cheaper, and that you don't need to spend uh one billion dollars for an EOV machine anymore.

**Vikram Sekar [00:59:03]:** Which means that in most people now with far lesser capital investment, going back to the whole economics angle that we started with in this podcast, can make more fabs.

**Vikram Sekar [00:59:15]:** And then if this technology is held within US soil this time and not given away, maybe all of manufacturing will come back to US soil if we can make X-rays work.

**Vikram Sekar [00:59:29]:** And now we can own all of the supply chain uh you know required to make uh I don't think we can own the supply chain, but if we can at least make wafers on US soil and have so many fabs that we don't rely on anybody else, that would really propel the chipmaking industry like we have never seen before.

**Vikram Sekar [00:59:48]:** So that is the case for making X-ray lithography on US soil.

**Austin Lyons [00:59:54]:** Totally, man.

**Austin Lyons [00:59:55]:** There's so many implications.

**Austin Lyons [00:59:56]:** We have to have a full episode on this.

**Austin Lyons [00:59:58]:** Hopefully, we'll talk to them.

**Austin Lyons [00:59:59]:** Because, first of all, it's good that you point out that there's lots of engineering that has to happen, not only with the light source, but with the optics.

**Austin Lyons [01:00:06]:** There's implications for the mask.

**Austin Lyons [01:00:08]:** How do you draw a mask at such small dimensions?

**Austin Lyons [01:00:10]:** Maybe it's e-beam, there's gonna be a cost to that, right?

**Austin Lyons [01:00:14]:** So there's lots of technical questions to get answered.

**Austin Lyons [01:00:16]:** But to your point, the implications are very profound.

**Austin Lyons [01:00:19]:** If, in fact, it can reduce, ultimately reduce the cost.

**Austin Lyons [01:00:23]:** Um, hey, could global foundries make two nanometer chips?

**Austin Lyons [01:00:27]:** Could Texas instruments, why not?

**Austin Lyons [01:00:29]:** So, what are the implications that I think it's super interesting of these legacy fabs, trailing edge fabs, now being able to make even smaller transistors at the cost of maybe their trailing edge nodes?

**Austin Lyons [01:00:42]:** Tons of implications.

**Austin Lyons [01:00:44]:** What does that mean for fabless design companies?

**Austin Lyons [01:00:47]:** Where, you know, you're like, well, yeah, maybe we'd make our own chip, but that's pretty expensive.

**Austin Lyons [01:00:52]:** And I don't know, probably we can't amortize$100,000 per wafer across what how many weights?

**Austin Lyons [01:01:00]:** We only need five wafers or something, but what if all of a sudden, again, it was you know the cost of a 90 nanometer chip that you can now buy wafers for$10,000 instead of$100,000, but get two nanometer you know transistors.

**Austin Lyons [01:01:12]:** Yeah, crazy implications.

**Austin Lyons [01:01:13]:** And then to your point, the geopolitical implications are fascinating too.

**Austin Lyons [01:01:17]:** So that's why I get excited.

**Vikram Sekar [01:01:20]:** Ultimately, you know what will happen ultimately what Jerry Sanders said.

**Vikram Sekar [01:01:23]:** Real men will have fabs again.

**Austin Lyons [01:01:25]:** Totally, totally.

**Austin Lyons [01:01:26]:** So that even that, like, why did every company at the start of semiconductors have a fab?

**Austin Lyons [01:01:33]:** Well, because ultimately, if you're vertically integrated, you're gonna get a better product.

**Austin Lyons [01:01:36]:** If you can co-design across the fabrication, across the design and the fabrication, if you can design, but also design for manufacturability all in the same house, you're just gonna go faster, you're gonna build a better product.

**Austin Lyons [01:01:48]:** But ultimately the cost, because of Rock's Law, got so big that people had to drop out because they couldn't afford a billion dollars for the next fab,$2 billion,$4 billion,$8 billion.

**Austin Lyons [01:01:58]:** Everyone has to drop out because, like the Global Foundries or the TIs, like they just can't, they don't have enough volume or high enough ASPs to amortize that cost.

**Austin Lyons [01:02:08]:** So it's just dropping off.

**Austin Lyons [01:02:09]:** But yes, in an ideal world, some of these players would still love to build, design, and build their own chips.

**Austin Lyons [01:02:18]:** And then, of course, from a wafer allocation perspective, you own your own destiny.

**Austin Lyons [01:02:23]:** Like, there's just so many amazing implications.

**Austin Lyons [01:02:26]:** So I know everyone gets super hung up on like the technology is impossible.

**Austin Lyons [01:02:30]:** Who dares think that they can take on ASML and Zeiss and all that crap?

**Austin Lyons [01:02:34]:** But I'm more excited about all the positive implications that will happen that will benefit all of us.

**Vikram Sekar [01:02:41]:** If you've been watching this on YouTube, you'll notice that I've been drinking from this lens cup.

**Vikram Sekar [01:02:46]:** So now that it's over, I guess our episode is two.

**Vikram Sekar [01:02:50]:** We've spoken a lot about lithography.

**Vikram Sekar [01:02:52]:** So let's let's get on with it.

**Austin Lyons [01:02:54]:** Totally.

**Austin Lyons [01:02:54]:** Okay, that's it for today.

**Austin Lyons [01:02:56]:** Everyone, thanks for listening.

**Austin Lyons [01:02:57]:** Thanks for hanging with us.

**Austin Lyons [01:02:58]:** Uh, we hope you're enjoying Semi Dopes.

**Austin Lyons [01:03:00]:** Please tell your friends about it, pass it along.

**Austin Lyons [01:03:02]:** If they want to learn about lithography, send this to them.

**Austin Lyons [01:03:06]:** Send us questions, comments on the YouTube, subscribe at semidope.com to our Substack that we've started.

**Austin Lyons [01:03:12]:** And thanks, as always, uh for joining us in this journey.
