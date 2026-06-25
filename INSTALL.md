# Nerva OS — Manual Install Guide

**This is the long way.** If you want the easy way, use [`SETUP-PROMPT.md`](SETUP-PROMPT.md) — you paste one prompt and Claude does everything.

This guide is here as a backup in case the paste-prompt method does not work, or you want to understand exactly what is happening on your machine.

**Time required: about 15 minutes.**

If you get stuck at any step, email **support@nerva-os.com**.

---

## Step 1 — Get Your Claude Subscription

Claude is the AI that powers your assistant. You need a Claude Max subscription so you can run Claude Code on your computer.

1. Open your browser and go to: [claude.ai](https://claude.ai)
2. Click **Sign Up** (or **Log In** if you already have an account)
3. Go to **Settings** then **Billing** then **Upgrade Plan**
4. Choose **Claude Max** — about $100 USD/month

> **Why Claude Max?** The free plan does not include Claude Code, the version that runs on your computer and automates tasks. Max unlocks the full feature set Nerva OS needs.

**Done when:** You can log in to claude.ai and see "Max" next to your plan.

---

## Step 2 — Install the Claude Desktop App

The Claude desktop app gives you the Claude Code tab — the panel where your assistant will live.

1. Go to: [claude.ai/download](https://claude.ai/download)
2. Click the download button for your operating system (Mac or Windows)
3. Open the downloaded file and follow the installer prompts
4. Open the Claude app and log in with your Claude account
5. Find the **Claude Code** tab inside the app

**Done when:** The Claude app opens, you are logged in, and you can see the Claude Code tab.

---

## Step 3 — Windows Only: Install Git

**Mac users: skip this step.** Git is already on your Mac (Claude will help install developer tools the first time you need them).

Windows needs Git installed manually:

1. Go to: [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the 64-bit installer
3. Run the installer and accept the default options on every screen
4. Restart your computer when the installer finishes

**Done when:** You restart and Git is installed. You don't need to test it — Claude will use it for you.

---

## Step 4 — Download Nerva OS

This step downloads the kit onto your computer.

1. Open the Claude desktop app and click the **Claude Code** tab
2. Paste this message into Claude Code and press Enter:

   > Please download Nerva OS from `https://github.com/nerva-os/nerva-os.git` into a folder called `nerva-os` in my home directory. Tell me exactly what you are doing as you go.

3. Claude will run the right command for your machine and tell you when it is done.

> **On Mac:** A small popup may ask you to install developer tools. Click **Install** and wait a few minutes. This only happens the first time.

**Done when:** Claude says the kit has finished downloading.

---

## Step 5 — Create Your Assistant Folder

Your assistant needs its own working folder. This is where it stores memory of your business.

Paste this into Claude Code:

> Please create a folder called `my-assistant` in my home directory. Then copy the workspace template from `~/nerva-os/workspace/` into it — the `CLAUDE.md` file, the `memory/` folder, and the `_inbox/` folder.

Claude will create the folder and copy the files.

**Done when:** Claude confirms a `my-assistant` folder exists in your home directory.

---

## Step 6 — Install the 37 Skills

Skills are the specialist abilities your assistant uses to write copy, research markets, send emails, and more.

Paste this into Claude Code:

> Please install all 37 Nerva OS skills by copying every folder from `~/nerva-os/skills/` into `~/.claude/skills/`. If the `~/.claude/skills/` folder does not exist yet, create it. Skip the `SKILLS-LIST.md` file — only copy the folders.

**Done when:** Claude confirms all 37 skill folders have been copied.

---

## Step 7 — Install the Safety Layer

The safety layer keeps your assistant inside the boundaries you set — what it can and cannot do, who it can email, which accounts it can touch.

Paste this into Claude Code:

> Please copy the safety layer from `~/nerva-os/safety/` into `~/my-assistant/safety/`.

**Done when:** Claude confirms the safety folder has been copied.

---

## Step 8 — Connect Playwright (Browser Automation)

Playwright lets your assistant open websites and do tasks in the browser for you — research, form filling, screenshots, lookups.

Paste this into Claude Code:

> Please install Playwright by running:
> `claude mcp add playwright npx @playwright/mcp@latest --scope user`

**Done when:** Claude confirms Playwright is connected.

---

## Step 9 — Open Your Assistant for the First Time

Now you switch from the install workspace to your actual assistant.

1. In the Claude desktop app, click the **folder icon** (or "Open Folder") in the Claude Code panel
2. Navigate to your home directory
3. Pick the **my-assistant** folder
4. Once it loads, type:

   > hello

Your assistant will introduce itself and ask seven questions about your business. Answer them in your own words. This is the moment your assistant becomes yours.

**Done when:** Your assistant greets you by name on the next conversation.

---

## If Something Breaks

Email **support@nerva-os.com** with:

- A screenshot of the message you saw
- Which step you were on
- Mac or Windows

We respond within one business day.

---

*Nerva OS — your AI for everything that matters.*
