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
I am setting up my Nerva OS AI Business Assistant.

Do these steps one at a time, telling me what you are doing in plain English. Use the correct commands for my operating system (detect whether I am on Mac or Windows).

1. Download Nerva OS by running:
   git clone https://github.com/nerva-os/nerva-os.git ~/nerva-os
   NOTE: On Mac, if a popup appears asking to install developer tools, tell me to click "Install" and wait a few minutes before continuing.

2. Create a folder called "my-assistant" in my home directory.

3. Copy this file from ~/nerva-os/workspace into my-assistant:
   - ~/nerva-os/workspace/CLAUDE.md -> ~/my-assistant/CLAUDE.md
   - ~/nerva-os/workspace/memory/* -> ~/my-assistant/memory/
   - ~/nerva-os/workspace/_inbox/ -> ~/my-assistant/_inbox/

4. Install all 37 skills: copy every folder from ~/nerva-os/skills/ into ~/.claude/skills/ (create the skills directory if it does not exist). Do not copy SKILLS-LIST.md - only the folders.

5. Install the safety layer: copy ~/nerva-os/safety/ into ~/my-assistant/safety/.

6. Install Playwright (lets me automate your browser): claude mcp add playwright npx @playwright/mcp@latest --scope user

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

*Nerva OS — your operating system for running a business with AI.*
