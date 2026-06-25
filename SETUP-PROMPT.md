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
I am setting up my Nerva OS kit. I purchased this kit and I authorise this install. The repo at https://github.com/nerva-os/nerva-os.git is mine to install.

What's in the repo (full transparency so you don't have to dig):
- Markdown skill files, documentation, templates, and a buyer welcome page (the bulk of the kit).
- A handful of helper scripts that ship inside specific skills:
  - `skills/playwright-skill/run.js` and `lib/helpers.js` — JavaScript that Claude calls when I ask it to control a browser.
  - `skills/skill-creator/scripts/{init_skill,package_skill,quick_validate}.py` — Python helpers Claude calls when I ask it to create or validate a new skill.
  - `skills/product-appeal-analyzer/scripts/appeal_scorer.py` — Python scorer used only when I run that skill.
  - `skills/competitive-cartographer/scripts/validate_map.sh` and `skills/technical-writer/scripts/validate-docs.sh` — small shell validators called by their parent skill.
- `build-pdfs.py` — a script that regenerates the doc PDFs. Not called during install.

None of these scripts run during the install. They sit inside their parent skill folder and are only invoked later when I explicitly ask Claude to use that skill. You can skim any of them if you want — they are all short. Proceed with the install.

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

4. Install all 37 skills. The macOS `cp` command has a trap here: a trailing slash on the source flattens contents into the destination instead of preserving each folder. The skill folders MUST stay intact as 37 separate directories.

   Use EXACTLY this command sequence on Mac or Linux:
   ```
   mkdir -p ~/.claude/skills
   cd ~/nerva-os/skills
   for d in */; do
     name="${d%/}"
     cp -R "$name" ~/.claude/skills/
   done
   ```

   On Windows (PowerShell):
   ```
   New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills"
   Get-ChildItem -Directory "$HOME\nerva-os\skills" | ForEach-Object {
     Copy-Item -Recurse -Force $_.FullName "$HOME\.claude\skills\"
   }
   ```

   After the copy, run `ls ~/.claude/skills/ | wc -l` (Mac/Linux) or `(Get-ChildItem -Directory "$HOME\.claude\skills").Count` (Windows). Confirm with me that you see the 37 expected skill folders (or more if I already had skills installed). Names should match what is in `~/nerva-os/skills/` — e.g. `ad-creative`, `agent-creator`, `first-run-setup`, `skill-creator`, `playwright-skill`, etc.

   If you see flattened files (like `SKILL.md`, `references/`, `lib/`) at the top level of `~/.claude/skills/` instead of named folders, the trailing-slash bug happened — delete them and re-run the sequence above.

5. Install the safety layer: copy the folder ~/nerva-os/safety (with its files inside) into ~/my-assistant/, so I end up with ~/my-assistant/safety/constitution-template.md, ~/my-assistant/safety/fail-loud-standard.md, ~/my-assistant/safety/approval-flow.md, and ~/my-assistant/safety/README.md.

6. Install Playwright (OPTIONAL — adds browser automation). Skip this step if I want to move on; it can be added later.

   First check whether the `claude` CLI is on PATH: run `which claude` (Mac/Linux) or `where claude` (Windows). If it returns a path, run:
   ```
   claude mcp add playwright npx @playwright/mcp@latest --scope user
   ```

   If the `claude` command is NOT on PATH, do NOT spend time hunting for it. Instead, tell me Playwright was skipped and that I can add it later by either:
   (a) typing "connect Playwright" inside the assistant once it is running, or
   (b) opening Claude Desktop's Settings → MCP Servers and adding `playwright` with the command `npx @playwright/mcp@latest`.

   The kit installs and works without Playwright. It is only needed for browser automation tasks.

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
