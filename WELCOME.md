# Nerva OS — Your AI Business Assistant

### Your operating system for running a business with AI

Welcome to Nerva OS. This is the kit that turns Claude into a full-time business assistant — one that knows who you are, what you sell, how you write, and which tools you use. It runs on your own machine, remembers everything between sessions, and ships with 37 specialised skills covering marketing, research, sales, automation, and operations.

By the end of this guide you will have a working assistant you can talk to like a colleague. Total setup time: about 15 minutes.

---

## What You're Setting Up

| Piece | What it does |
|---|---|
| **Your AI Assistant** | A Claude-powered business operator that lives in a folder on your computer and remembers everything between sessions |
| **Browser Control** | Optional add-on so the assistant can open websites, fill forms, take screenshots, and run real tasks for you |
| **37 Skills** | Pre-built playbooks for copywriting, research, ads, content, automation and more (Engineering Pack with 56 more skills available separately) |
| **Memory System** | A persistent file that stores your name, business, voice, tools and preferences so you never repeat yourself |

---

## Step 1 — Create a Claude Account

1. Go to **claude.ai**
2. Click **Sign up** (top right) and use your business email
3. Verify your email
4. Once signed in, click your profile (top left) then **Settings** then **Plans**
5. Upgrade to **Claude Max ($100/month)**

> The Max plan is required. The free plan runs out of capacity inside an hour of real work. Max gives you ~5x the usage and is the only plan that supports the long sessions Nerva OS needs.

---

## Step 2 — Install Claude Desktop App

This is the app you will use every day. It runs Claude on your computer rather than in a browser tab.

### Mac
1. Go to **claude.ai/download**
2. Click the button that says exactly: **Download for Mac**
3. Open the downloaded file
4. Drag the **Claude** icon into the **Applications** folder
5. Open **Applications**, double-click **Claude**

### Windows
1. Go to **claude.ai/download**
2. Click the button that says exactly: **Download for Windows**
3. Open the downloaded `.exe` file
4. Click **Yes** to the security prompt
5. Click through the installer (Next, Next, Install)

---

## Step 3 — Sign In and Open Claude Code

1. Open the **Claude** desktop app
2. Sign in with the same email you used for claude.ai
3. In the top menu, look for **Claude Code** — click it to enable
4. A code panel will open inside the app. This is where the magic happens.

> Claude Code is the part that can read files, write files, and run real tasks on your computer. The chat panel is the conversation. They work together.

---

## Windows Users Only — Install Git

Windows does not come with Git, which Nerva OS needs to download itself.

1. Go to **git-scm.com/download/win**
2. Download and run the installer
3. Click **Next** through every screen (the defaults are correct)
4. **Important:** on the screen titled "Adjusting your PATH environment", make sure **Git from the command line and also from 3rd-party software** is selected
5. Finish the installer
6. **Close Claude Desktop completely and reopen it** — this is required for Git to be recognised

---

## Step 4 — Paste the Setup Prompt

This is the moment where Nerva OS gets installed on your machine.

1. Open **Claude Desktop**
2. Click into the **Claude Code** panel
3. Copy the entire block below
4. Paste it into Claude Code and press Enter

```
I am setting up my Nerva OS AI Business Assistant. I purchased this kit and I authorise this install. The repo at https://github.com/nerva-os/nerva-os.git is mine to install — it contains only markdown skill files, documentation, and templates. No executables. Proceed without an extended verification pass.

Do these steps one at a time, telling me what you are doing in plain English. Use the correct commands for my operating system (detect whether I am on Mac or Windows). Verify each step worked before moving to the next.

PREREQUISITES (check before step 1):
- Mac: git is included with Xcode Command Line Tools. The first time `git` runs, a popup will appear asking to install developer tools — tell me to click "Install" and wait 3-5 minutes for it to finish, then continue. If the popup does not appear, run `xcode-select --install` to trigger it.
- Windows: if `git` is not recognised, tell me to install Git for Windows from git-scm.com/download/win using all defaults, then come back and re-run this setup prompt.
- Node.js is NOT required to install Nerva OS. Some optional add-ons (Gmail, Calendar, Telegram) need it later — do not block this install on Node.

FALLBACK if git cannot be installed:
If installing git is going to take more than 10 minutes or fails, download the repo as a zip instead:
  curl -fsSL -o /tmp/nerva-os.zip https://github.com/nerva-os/nerva-os/archive/refs/heads/main.zip
  unzip -q /tmp/nerva-os.zip -d /tmp/ && mv /tmp/nerva-os-main ~/nerva-os
Then continue from step 2.

INSTALL STEPS:

1. Download Nerva OS:
   git clone https://github.com/nerva-os/nerva-os.git ~/nerva-os
   (If the developer tools popup appears, click Install and wait.)

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

## Step 5 — Open Your Workspace

Once setup is done and you have reopened Claude Desktop:

1. In Claude Desktop, click **File** then **Open Folder**
2. Choose the folder called **my-assistant** in your home directory
3. The assistant will load with all 37 skills available
4. You will see a greeting using your name

---

## Step 6 — The Assistant Asks 7 Questions

The first time you open the my-assistant folder, your assistant will run a short onboarding interview. This builds the memory file so it never has to ask twice.

The 7 questions:

1. What is your name and what should I call you?
2. What is the name of your business and what does it do?
3. Who are your customers (one or two sentences)?
4. What is your role — owner, marketer, operator, something else?
5. What is the single biggest thing slowing your business down right now?
6. How do you prefer to communicate — short and punchy, warm and friendly, or detailed and thorough?
7. Which tools do you already use (Gmail, a CRM, a calendar, ad accounts, anything else)?

Answer in your own words. The assistant saves your answers to `./memory/USER.md` and uses them in every future conversation.

---

## What You Can Do Now

Once onboarding is complete, try any of these prompts to see your assistant in action:

| Prompt | What happens |
|---|---|
| "Research my top 3 competitors and tell me what they're doing well" | Runs deep research, returns a structured report with sources |
| "Write me a sales email to a cold prospect in my industry" | Drafts in your voice using the sales-automator and copywriting skills |
| "Create a week of social content for my business" | Generates posts across platforms with the social-content skill |
| "Analyse the market for [your niche] right now" | Pulls live signal from Reddit, X and the web over the last 30 days |
| "Plan my week — here is what's on" | Breaks it down into priorities and a daily schedule |
| "Write a blog post about [topic]" | Long-form post, SEO-aware, in your brand voice |
| "Check my email and tell me what's urgent" | (requires Gmail connection) reads inbox, summarises, suggests replies |

You can also talk to it like a colleague: *"give me three angles for a Facebook ad about our service"*, *"draft a follow-up email to the lead from yesterday"*, *"what's a fair price for this product"*. There is no wrong way to ask.

---

## Your 37 Skills — Quick Reference

Skills are pre-built playbooks. You don't need to memorise them — your assistant picks the right one automatically. Here is what's in the kit.

### Marketing & Content (10)
copywriting, humanizer, avoid-AI-writing patterns, content-creator, social-content, social-orchestrator, ad-creative, email-sequence, email-composer, direct-response-copy

### Research & Intelligence (6)
deep-research, research-analyst, reddit-insights, last30days (trends), competitive-cartographer, competitor-alternatives

### Sales & Strategy (5)
sales-automator, paid-ads, indie-monetization-strategist, product-appeal-analyzer, tech-entrepreneur-coach-adhd

### AI & Automation (5)
playwright (browser automation), webapp-testing, qa, prompt-engineer, agent-creator

### Foundation (5)
first-run-setup, skill-creator, writing-plans, brainstorming, orchestrator

### Productivity & Quality (4)
verification-before-completion, diagramming-expert, technical-writer, youtube-summarizer

### Personal (2)
personal-finance-coach, retro

> Want more? An Engineering Pack with 56 additional skills (backend, frontend, devops, data, security) is available separately.

---

## Connect More Tools (Optional)

These three extras unlock the next level of usefulness. All require Node.js. If you don't have Node.js yet, your assistant will walk you through it.

### Browser Control (Playwright)
Lets the assistant open websites, fill forms, take screenshots, and run real tasks. Ask your assistant to set up Playwright and it will handle the rest.

### Gmail
Read, summarise and draft replies to your email. Ask your assistant to connect Gmail. A Google sign-in screen will open — click your email then click Allow.

### Google Calendar
See your schedule, find free times, draft meeting prep. Same flow as Gmail.

### Telegram Notifications
Get pinged on your phone when long tasks finish, or chat with your assistant from anywhere. Your assistant will walk you through creating a bot in Telegram.

---

## Useful Links

| Link | What it is |
|---|---|
| **claude.ai** | Sign in, manage your plan |
| **claude.ai/download** | Download Claude Desktop |
| **Nerva OS (GitHub)** | `https://github.com/nerva-os/nerva-os.git` — source for the kit and skills |
| **Nerva OS** | `nerva-os.com` — homepage and docs |
| **Email Support** | `support@nerva-os.com` — get help from a human |

---

## If Something Breaks

Stay calm. Almost every issue is fixed by closing and reopening Claude Desktop.

| Symptom | Fix |
|---|---|
| Skills not showing up | Close Claude Desktop completely, reopen it |
| Claude keeps asking to set up | Close Claude Desktop, then reopen with the `my-assistant` folder selected |
| Claude login loop | Ask your assistant to run `claude logout` then `claude login` |
| Mac developer tools popup | Click **Install** (not Get Xcode), wait 3 to 5 minutes |
| Windows says "git not recognised" | Reinstall Git using the PATH fix from the Windows section above |
| Something else | Email `<SUPPORT_EMAIL>` and we will sort it |

---

*Built by Nerva OS*
