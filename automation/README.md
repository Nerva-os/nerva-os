# Automation

**This directory is reserved for v2.**

Nerva OS v1 is a fully manual assistant — you start every conversation, and your assistant responds. That is intentional. Most non-technical owners want to feel the assistant's behaviour before letting it run on its own schedule.

v2 adds scheduled automation engines so your assistant can do work for you while you sleep.

---

## What is coming

The first automation engines on the roadmap:

- **Morning shift** — every weekday at 7am, your assistant scans your inbox, drafts replies, and posts a one-page brief to your `_inbox/` for review
- **Weekly wrap** — every Monday at 6am, your assistant pulls finance, pipeline, marketing, and ops data into a consolidated weekly briefing
- **Follow-up sweeps** — every day at 8am, your assistant checks who is overdue for a quote follow-up and either drafts the message or sends it, depending on the safety rules you set

Every Nerva OS engine is built around the same handful of guarantees. The order varies by job — the guarantees do not.

- **Single-instance lock** — only one copy of an engine can run at a time, with a stale-lock timeout that cleans itself up
- **Dedupe marker** — a permanent record of every completed job so re-runs skip what's already done
- **Background launch** — the engine releases the foreground immediately so you can keep working
- **Sealed report** — every run posts a status message, even if there's nothing to report (no silent endings)
- **Job log** — every run leaves a full trace in `automation/logs/` so you can audit what your assistant did
- **Honest failure** — if a step breaks, the engine names what went wrong, where, and what got done before the break

These guarantees sit on top of the [`fail-loud-standard`](../safety/fail-loud-standard.md) — the standard governs every skill and engine in Nerva OS.

---

## Before you turn anything on

Automation crosses a line. A manual assistant can only do what you ask. A scheduled assistant acts on its own — using the boundaries you set.

Before v2 ships, read [`../safety/constitution-template.md`](../safety/constitution-template.md). The constitution is where you define what your assistant is allowed to do, which accounts it can touch, and who it can email without asking. Get this right first. Everything else builds on top of it.

---

*Nerva OS — your business and personal AI assistant.*
