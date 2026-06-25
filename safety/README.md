# Nerva OS — Safety Layer

This folder is the safety layer for Nerva OS. It is the standing instructions for every skill, agent, and automation the assistant runs. If a request and a rule in here disagree, the rule wins.

## What's in this folder

- **`constitution-template.md`** — the file you customise. Lists what the assistant can do on its own, the things it never does without you, and how the rules change (only you can change them). **This is the only file in the safety layer most buyers will edit.** Fill in the placeholders to match your business.
- **`fail-loud-standard.md`** — the rule that says automations never go quiet. If something errors, you hear about it. If a list comes back empty, the assistant checks why before assuming it's nothing. Every item in a list ends up in one of three buckets: handled, needs your review, or could not be done.
- **`approval-flow.md`** — how the assistant decides whether to act, ask, or hand off. A decision tree first, with examples after. Default: draft first, you decide what gets sent.

## Why this exists

An assistant with access to your inbox, calendar, files, and tools is powerful — and powerful tools can do things you would not have chosen. The safety layer is what makes that power safe. It draws the boundary clearly, makes the assistant respect it, and routes anything that touches the boundary back to you for a yes or no.

The three files work together:
1. **Constitution** sets the boundary.
2. **Fail-loud standard** makes sure you hear about it when something goes sideways inside that boundary.
3. **Approval flow** routes any work that touches the boundary to a person before it happens.

## How the assistant loads this on every session

At the start of every session, the assistant reads:
1. `safety/constitution-template.md` (or your filled-in copy) — your business-specific boundary.
2. `safety/fail-loud-standard.md` — how errors must be reported.
3. `safety/approval-flow.md` — when to act, when to ask, when to hand off.

These rules are loaded for the full session. Every skill the assistant runs and every automation it triggers respects them. The assistant may not soften, weaken, or work around them.

## Where to customise

You only need to edit one file to align Nerva OS with your business: **`constitution-template.md`**.

Inside it, fill in:
- `<YOUR_NAME>`, `<YOUR_BUSINESS>`, `<YOUR_APPROVAL_EMAIL>`, `<YOUR_PHONE>` — workspace identity.
- The section on **what needs your say-so** — anything specific to your business the assistant must never do alone.
- The section on **how to change these rules** — who reviews and when.

If you want a guided walkthrough, ask your assistant: "walk me through setting up my safety rules." It will take you through each section one question at a time.

The other two files (`fail-loud-standard.md` and `approval-flow.md`) are platform-level standards that apply to every Nerva OS install. You should not need to change them.

## Who can edit these files

Only a person. The assistant may never rewrite, weaken, or narrow the safety layer. If it thinks a rule is wrong or in the way, it tells you and waits — it does not change the rule.

---

*Part of Nerva OS.*
