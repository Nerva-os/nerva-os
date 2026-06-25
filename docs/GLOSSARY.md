# Glossary — Plain English Tech Terms

This is the dictionary for Nerva OS. Bookmark it. When your assistant says a word you don't know, find it here first.

The Core 12 are the ones you'll meet in your first week. The rest mostly builds on those.

---

## The Core 12

### CLI (Command-Line Interface)
A text window where you type instructions instead of clicking buttons. The black or dark window you see when running `claude` commands. If you've ever opened Terminal on a Mac or PowerShell on Windows, that's a CLI.

### MCP (Model Context Protocol)
Anthropic's standard for plugging tools into your assistant. Think of it as USB ports for AI. Each MCP unlocks new abilities:
- **Xero MCP** → 60 accounting tools
- **GHL MCP** → your CRM
- **Playwright MCP** → control any website in a browser
- **Telegram MCP** → message you on your phone

### Cron task
A scheduled job that runs automatically on a timer. "Every Monday at 9am, send me my open quotes." The schedule is the cron. The thing it runs is the task.

### API (Application Programming Interface)
How one app talks directly to another. Xero has one (which is why we can connect it). Tradify doesn't (which is why we can't fully automate it). Think of it as a vending machine — APIs let your assistant push buttons remotely.

### OAuth
The "Login with Google" pattern. When you click **Allow** in a popup to give your assistant access to something (like Gmail or Xero), that's OAuth. It gives the assistant permission to act on your behalf without you ever sharing your actual password.

### Token
A temporary password the system uses behind the scenes. Like a hotel keycard — it expires, it can be revoked, it's not your real key. Your Xero token refreshes itself every 30 minutes automatically.

### Skill
A small instruction file that gives your assistant specific expertise. The quoting skill knows your rates, T&Cs, and scope formats. The copywriting skill knows how to write sales pages. Nerva OS ships with 37 of these out of the box.

### Agent / Sub-agent
A specialist version of your assistant for one job. The quoting-brain agent handles quotes. The GHL expert handles CRM work. They run in the background while your main assistant keeps the bigger conversation going.

### Webhook
The opposite of an API call. Instead of your assistant asking "anything new?", the other service pings your assistant when something happens. Like a doorbell — you don't watch the door, the bell tells you when someone arrives.

### Localhost
Just your own computer. When you see `http://localhost:3333` (your dashboard) or `localhost:8765` (a sign-in page) — that's something running on YOUR machine, not the internet.

### Markdown
The format used for almost everything in Nerva OS — memory files, notes, your task board. `#` makes a heading. `-` makes a bullet. `**bold**` makes bold. Simple text with a tiny bit of structure.

### Hook
An auto-action the system runs at specific moments. Like "every time the assistant finishes editing a file, run a quality check on it." You set it once, it fires forever.

---

## Nerva OS Terms

### Nerva OS
The kit you bought. A complete AI assistant workspace that lives on your computer, knows your business, and runs 37 specialist skills.

### Workspace
The folder `~/my-assistant/` on your Mac (or `C:\Users\you\my-assistant\` on Windows). It contains your assistant's brain (`CLAUDE.md`), its memory, and the inbox where you drop documents.

### Memory
Files inside `workspace/memory/` where your assistant saves what it learns about you. The big three:
- `USER.md` — who you are, what your business does
- `SETUP.md` — what's connected and what isn't
- `MEMORY.md` — notes, preferences, and corrections it remembers across sessions

### The Inbox
The folder `workspace/_inbox/` where you drop documents (sent emails, brand guides, pricing sheets) for your assistant to learn from. Drop it, then say "process the inbox".

### Constitution
The safety document at `safety/constitution-template.md` — your standing orders for the assistant. What it can do on its own. What needs your say-so. The things it never does without you. Edit this once, your assistant honours it forever.

### Fail-Loud Standard
The rule that says: if anything goes wrong, tell the user. Never silently skip. Never claim success when something errored. Lives in `safety/fail-loud-standard.md`.

### Engineering Pack
The paid add-on with 56 deeper skills (Postgres, Terraform, Kubernetes, etc.) for buyers who need them. v1 of Nerva OS ships the 37 most useful general-business skills.

---

## Other Terms You'll Hear

### LLM (Large Language Model)
The AI brain itself. Claude, GPT, Gemini are all LLMs. Nerva OS runs on Claude.

### Prompt
What you type to the AI. Could be one sentence ("write me an email") or a paragraph. The clearer the prompt, the better the answer.

### Repo (Repository)
A folder of code stored on GitHub or similar. Nerva OS itself is a repo. So is the engineering pack.

### Git
The tool that downloads and updates repos. When you ran the setup prompt, `git clone` is what pulled Nerva OS onto your computer.

### GitHub
The website where most code repos live. Like Dropbox, but for code.

### npm / npx
Two helper tools that come with Node.js. They install little add-ons. You'll never call them directly — your assistant uses them under the hood when adding new MCPs.

### Node.js
A program your computer needs so that some MCPs work. Most installs handle this for you. If something complains about Node.js, your assistant will walk you through installing it.

### Environment Variable (env var)
A setting stored on your computer that programs read from. Things like passwords or API keys live in env vars so they're not hard-coded into files. Lives in a `.env` file usually.

### JSON
A simple text format for structured data. Looks like `{"name": "Victor", "business": "Coverage by Design"}`. You'll see it in config files. Hard to write by hand, easy for computers to read.

### Frontmatter
The little block of settings at the top of a markdown file, between `---` lines. Skills use it to declare their name and description. Looks like:
```
---
name: my-skill
description: What this skill does
---
```

### Tag
A label you stick on a contact, a note, or a record. In your CRM, you might tag a contact `vip` or `repeat-customer`. Tags help you find and group things later.

### Scope
What a tool, skill, or installation applies to. A skill installed with `--scope user` is available everywhere on your computer. A skill installed in one folder is only available in that folder.

### Pipeline
A series of steps that runs in order. Your sales pipeline has stages (Lead → Quoted → Won → Invoiced). A data pipeline has stages too (collect → clean → save).

### Idempotent
A fancy word for "safe to run twice". An idempotent automation won't double-send the same email if you accidentally trigger it twice. Nerva OS automations are designed this way.

### Dry run
Test mode. Pretend to do the thing but don't actually do it. Useful before running anything destructive. "Show me what you would change, but don't change it yet."

### Sandbox
A safe play area where the assistant can experiment without affecting your real data or accounts. The Claude desktop app's Cowork mode runs in a sandbox.

---

## Still confused?

Just ask your assistant. Say "what does <word> mean?" — you'll get a plain-English answer with examples from your business if it can find them.

This glossary will grow as Nerva OS grows. New version → new terms added at the bottom of each section.

---

*Part of [Nerva OS](../README.md)*
