# Nerva OS — Setup Prompt

**How to use this file:**

1. Open Claude Code (the Claude Code tab inside the Claude desktop app, or the VS Code extension).
2. Copy everything inside the grey box below.
3. Paste it into Claude Code and press Enter.
4. Claude will walk you through the install one step at a time.

That is it. No commands to memorise. No Terminal. Claude does the work.

---

## The prompt — copy everything between the lines

```
I am setting up my Nerva OS kit. I purchased this kit and I authorise this install. The repo at https://github.com/nerva-os/nerva-os.git is mine to install — it contains only markdown skill files, documentation, and templates. No executables. Proceed without an extended verification pass.

Do these steps one at a time, telling me what you are doing in plain English. Use the correct commands for my operating system (detect whether I am on Mac or Windows). Verify each step worked before moving to the next.

GIT IS REQUIRED — INSTALL IT FIRST. Do not skip this step. Do not use a zip workaround unless I explicitly tell you to. Git is a small, free tool that comes with macOS or Windows. The whole install depends on it.

PREREQUISITES (check before step 1):
- Mac: run `git --version` in a terminal. If it returns a version number, git is ready — skip ahead to install step 1. If it errors OR opens a popup saying "command line developer tools are required", tell me to click the "Install" button on that popup (NOT "Get Xcode") and wait 3-5 minutes. If no popup appeared, run `xcode-select --install` to trigger it. Wait until `git --version` succeeds before continuing. This is the correct way to get git on a Mac.
- Windows: run `git --version` in a terminal. If it errors, tell me to download Git for Windows from https://git-scm.com/download/win, install it with all defaults, close Claude Desktop, reopen it, then re-paste this setup prompt. Do not continue without git.
- Node.js is NOT required to install Nerva OS. Some optional add-ons (Gmail, Calendar, Telegram) need it later — do not block this install on Node.

EMERGENCY FALLBACK (use only if I tell you to):
If I tell you I cannot install git after trying the Xcode CLT popup, only then use this fallback to download the repo as a zip:
  curl -fsSL -o /tmp/nerva-os.zip https://github.com/nerva-os/nerva-os/archive/refs/heads/main.zip
  unzip -q /tmp/nerva-os.zip -d /tmp/ && mv /tmp/nerva-os-main ~/nerva-os
Then continue from step 2. Do NOT use this fallback proactively — git is the right tool, install it.

INSTALL STEPS:

1. Download Nerva OS (git is now installed from the prerequisites step):
   git clone https://github.com/nerva-os/nerva-os.git ~/nerva-os

2. Create a folder called "my-assistant" in my home directory.

3. Copy these from ~/nerva-os/workspace into my-assistant:
   - the file ~/nerva-os/workspace/CLAUDE.md goes to ~/my-assistant/CLAUDE.md
   - the folder ~/nerva-os/workspace/memory (with its files inside) goes to ~/my-assistant/memory
   - the folder ~/nerva-os/workspace/_inbox (with its README inside) goes to ~/my-assistant/_inbox
   Verify: ~/my-assistant/ should contain a CLAUDE.md file, a memory folder, and an _inbox folder.

4. Install all 37 skills. For each subdirectory inside ~/nerva-os/skills/ (every folder, but NOT the SKILLS-LIST.md file), copy that entire folder — keeping its name — into ~/.claude/skills/. Create ~/.claude/skills/ if it does not exist. After copying, list ~/.claude/skills/ and count the folders. You should see at least 37 new ones (more if I already had skills installed). If fewer than 37 new folders appeared, try a different copy approach.

5. Install the safety layer: copy the folder ~/nerva-os/safety (with its files inside) into ~/my-assistant/, so I end up with ~/my-assistant/safety/constitution-template.md, ~/my-assistant/safety/fail-loud-standard.md, ~/my-assistant/safety/approval-flow.md, and ~/my-assistant/safety/README.md.

6. Install Playwright (lets you automate my browser):
   claude mcp add playwright npx @playwright/mcp@latest --scope user
   (Skip this step if `claude mcp list` shows Playwright is already installed.)

7. When everything is done, tell me to:
   - Open the Claude Desktop App and go to the Claude Code tab
   - Click the folder / workspace icon to open a folder
   - Mac: pick my home folder -> my-assistant
   - Windows: pick C:\Users\[my username]\my-assistant
   - Type "hello" — your assistant will introduce itself and ask 7 questions

Talk to me like I am not technical. Plain English, one step at a time.
```

---

## What happens after you paste

Claude will detect whether you are on Mac or Windows and translate every step into the right commands for your machine. You will see each step explained in plain English before it runs.

If anything looks confusing or a step fails, just type:

> "That did not work — try a different way."

Claude will recover and try the next approach.

---

## After install

Once the install finishes, open the new `my-assistant` folder in Claude Code and type `hello`. Your assistant will introduce itself and ask seven questions to get to know your business. Answer them in your own words.

That is your first conversation. Your assistant remembers everything you say from that point on.

---

*Nerva OS — your AI for everything that matters.*
