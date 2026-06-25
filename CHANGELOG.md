# Changelog

All notable changes to Nerva OS are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-06-18

Initial public release of Nerva OS — your operating system for running a business with AI.

### Added

- **37 specialist skills** bundled in `skills/` covering sales, marketing, finance, operations, research, admin, and AI-native workflows
- **Safety layer** at `safety/` — constitution template and guardrail system that defines what the assistant can and cannot touch
- **Workspace template** at `workspace/` — pre-built `CLAUDE.md` brain file, `memory/` folder, and `_inbox/` ready to copy into the buyer's `~/my-assistant/` workspace on first run
- **Paste-prompt installer** at `SETUP-PROMPT.md` — single prompt the buyer pastes into Claude Code; Claude runs the entire install end-to-end with plain-English narration
- **Manual install guide** at `INSTALL.md` — step-by-step backup for buyers who want to install by hand or troubleshoot
- **Buyer-facing README** at `README.md` — landing copy, pricing tiers, license summary, and support contact
- **Proprietary EULA** at `LICENSE` — single-business-use license with Apache 2.0 carve-out for upstream skills
- **Tutorials and onboarding flow** — first-run skill triggers a 7-question intake on first `hello` and writes the answers into `memory/USER.md`
- **Automation directory stub** at `automation/` — reserved for v2 scheduled engines (morning shift, weekly wrap, follow-up sweeps)
- **Visuals directory stub** at `visuals/` — reserved for screenshots, diagrams, and marketing assets
- **Docs directory stub** at `docs/` — reserved for buyer-facing how-to guides
- **`.gitignore`** — protects buyer-specific memory files, inbox contents, environment variables, and OS cruft from accidental commits

### Notes

- Engineering Pack (56 additional skills for technical workflows) is sold as a separate upsell and not included in this release.
- v1 is fully manual — there are no scheduled engines yet. Automation arrives in v2.

---

[0.1.0]: initial release
