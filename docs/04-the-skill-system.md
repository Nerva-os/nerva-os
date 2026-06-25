# The Skill System

This guide explains how Nerva OS actually does its job. Once you understand this, you'll get sharper results from every conversation.

---

## What a Skill Is

A **skill** is one specialised AI worker your assistant can call on.

Think of your assistant as the head of a small agency. When you ask for something, the assistant figures out which specialist on the team is best for the job and hands it over.

You don't have a one-size-fits-all chatbot. You have 37 specialists. Each one knows a specific job inside out.

**Examples of what a single skill knows:**

- The copywriting skill knows the difference between a headline that sells and a headline that doesn't.
- The research skill knows how to find real data instead of making things up.
- The ad-creative skill knows how to write twenty Facebook ad variations without repeating itself.

That depth is the whole point. Specialists beat generalists.

---

## How Your Assistant Picks One

You don't need to memorise the skills. You just describe what you want in plain English.

**You say:** "Write me a sales email for my new product."
**Your assistant thinks:** That sounds like the **email-composer** skill. Let me use that.

**You say:** "What are my competitors charging?"
**Your assistant thinks:** That sounds like the **competitive-cartographer** skill. Let me use that.

The matching happens silently. You never see it unless you ask.

---

## How to Call One Directly

Sometimes you know exactly which specialist you want. In that case, just name it.

**You say:** "Use the **brainstorming** skill to help me think about this."
**You say:** "Use the **deep-research** skill to dig into this topic."
**You say:** "Use the **retro** skill to review what happened last quarter."

Calling a skill by name forces the assistant to use that specialist. Handy when you've found one you trust.

---

## The 37 Skills, by Category

Here is everything in the box. Each category includes one prompt you can try right now.

### Foundation (5 skills)

The skills that make the whole system work.

| Skill | What it does |
|---|---|
| first-run-setup | Walks you through onboarding the first time you launch |
| skill-creator | Helps you build your own custom skill |
| writing-plans | Turns a fuzzy idea into a structured plan |
| brainstorming | Stress-tests an idea before you build it |
| orchestrator | Coordinates multiple skills for a single big request |

**Try this:** "Use the **writing-plans** skill to plan my product launch."

### Marketing & Content (10 skills)

Anything that involves writing words to sell something.

| Skill | What it does |
|---|---|
| copywriting | Writes landing pages, websites, taglines, value props |
| humanizer | Rewrites AI-sounding text to sound human |
| avoid-ai-writing | Audits and removes 21 common AI writing patterns |
| content-creator | SEO-friendly blog posts and articles |
| social-content | Posts for Instagram, LinkedIn, Twitter, TikTok |
| social-orchestrator | Plans a full week of social posts at once |
| ad-creative | Bulk ad headlines, descriptions, body text |
| email-sequence | Multi-step drip campaigns and welcome series |
| email-composer | One-off emails for sales, customers, partners |
| direct-response-copy | Long-form sales letters and VSL scripts |

**Try this:** "Use the **copywriting** skill to rewrite my homepage headline."

### Research (6 skills)

Skills that find real information instead of guessing.

| Skill | What it does |
|---|---|
| deep-research | Multi-step research with full source citations |
| research-analyst | Market research and trend analysis |
| reddit-insights | Finds what real people are saying on Reddit |
| last30days | Reddit, X, and web from the last 30 days only |
| competitive-cartographer | Maps your competitive landscape |
| competitor-alternatives | Builds "X vs Y" pages for SEO and sales |

**Try this:** "Use the **competitive-cartographer** skill to map my top three competitors."

### Sales & Strategy (5 skills)

Skills for thinking about how the business actually makes money.

| Skill | What it does |
|---|---|
| sales-automator | Sales sequences, cold outreach, follow-ups |
| paid-ads | Strategy for Google, Meta, LinkedIn ads |
| indie-monetization-strategist | Pricing and revenue ideas for small operators |
| product-appeal-analyzer | Tests whether people actually want what you're selling |
| tech-entrepreneur-coach-adhd | A coach for distractible founders |

**Try this:** "Use the **indie-monetization-strategist** skill to suggest three ways I could earn from my email list."

### Automation & Operations (5 skills)

Skills that do real things in real tools.

| Skill | What it does |
|---|---|
| playwright-skill | Drives your browser to do tasks for you |
| webapp-testing | Tests websites and finds bugs |
| qa | Reviews your site or app and reports problems |
| prompt-engineer | Improves prompts so you get sharper results |
| agent-creator | Builds custom AI assistants for repeating jobs |

**Try this:** "Use the **qa** skill to review my website and find anything broken."

### Productivity & Quality (4 skills)

Skills that make your other work sharper.

| Skill | What it does |
|---|---|
| verification-before-completion | Double-checks work before saying it's done |
| diagramming-expert | Builds clear diagrams from messy ideas |
| technical-writer | Writes documentation people actually read |
| youtube-summarizer | Summarises long videos into key takeaways |

**Try this:** "Use the **youtube-summarizer** skill on this video link."

### Personal (2 skills)

For your own life, not just the business.

| Skill | What it does |
|---|---|
| personal-finance-coach | Plans, investing, tax, retirement |
| retro | Reviews what went well and what didn't |

**Try this:** "Use the **retro** skill to review my last three months."

---

## How to Add Your Own

You can build your own skill in about ten minutes.

1. Say to your assistant: "Use the **skill-creator** skill to help me build a new one."
2. It will ask what the skill should do.
3. Describe the job. Be specific.
4. It will write the skill file and save it for you.

Your custom skills sit alongside the 37 we ship with. They work the same way.

**Want more, ready-made?** We sell an **Engineering Pack** with 56 extra specialist skills for developers, technical founders, and anyone running software. Ask your assistant about it when you're ready, or email support@nerva-os.com.

---

## What's NOT a Skill

Most of what you ask your assistant is just a normal conversation. Skills are for specialist jobs.

**These are NOT skill jobs:**

- "What time is it in London?"
- "Explain this concept to me."
- "Help me think through this email I got."
- "What do you think of this idea?"
- "Summarise our last conversation."

For these, the assistant just answers directly. No specialist needed.

A good rule: if it would take a human specialist more than ten minutes, it's probably a skill job.

---

**Next:** If something breaks during all of this, open [09 — Troubleshooting](./09-troubleshooting.md). Most issues have a two-minute fix.
