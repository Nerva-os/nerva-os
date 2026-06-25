---
name: humanizer
description: Rewrite AI-generated text to sound natural, conversational, and human. Use when text reads like a robot wrote it — too polished, too symmetrical, too predictable. Trigger phrases include "humanize this", "make this sound human", "this sounds AI", "tone this down". Differs from `avoid-ai-writing` (which catches patterns before they happen) — `humanizer` fixes text that has already been written.
---

# Humanizer

You rewrite AI-flavoured text so it reads like a human wrote it.

## When to use

- The user pastes a block of text that sounds AI-generated and says "humanize this" or "make this sound human"
- The user finishes a draft and asks "does this sound AI?"
- The user is preparing copy for a public audience (social posts, emails, ad copy, sales pages) and wants it to land naturally

## What "human" actually means

Humans write asymmetrically. They:
- Vary sentence length wildly (a short one. Then one that runs on with sub-clauses and asides because the thought is still forming)
- Trail off sometimes
- Use contractions, fragments, and the occasional sentence-starting "And"
- Repeat words on purpose when emphasis matters
- Skip the wind-up. They start mid-thought
- Drop the optional words ("that", "really", "very")
- Use specific concrete nouns over abstract ones (a "rusted 2018 Hilux" beats "an old vehicle")

AI-flavoured text does the opposite. It hedges, balances, lists in threes, says "moreover" and "furthermore", and never starts a sentence with "And".

## How to fix it

1. Read the original out loud in your head. Where does it feel mechanical?
2. Cut every "moreover", "furthermore", "in addition", "it is worth noting", "additionally"
3. Break long balanced sentences into uneven shorter ones
4. Replace abstract phrases with concrete ones
5. Strip filler ("really", "very", "in order to", "due to the fact that")
6. Let one or two paragraphs start with a single-word punch ("Here's why.")
7. Read it again. Cut anything that still sounds robotic.

## What you return

The rewritten text only, no commentary. If the user wants a side-by-side diff or a list of changes, they will ask.

## When NOT to use this

- Technical documentation that needs to be precise
- Legal copy
- Anything the user explicitly says should stay formal
