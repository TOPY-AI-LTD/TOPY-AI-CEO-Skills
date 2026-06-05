<div align="center">
  <p>
    <img src="https://www.topy.ai/long_logo.svg" alt="TOPY AI CEO" width="420" />
  </p>
  <h1>
    <span style="color:#ff1212;">TOPY AI CEO Skills</span>
  </h1>
  <p style="font-weight: 700; color: #ff1212;">
    Install TOPY dashboard skills with <code>npx skills</code> and use them from Codex, Claude Code, and other skills-aware agents.
  </p>
  <p>
    <a href="https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills" aria-label="GitHub Repository">
      <img alt="GitHub Repo" src="https://img.shields.io/badge/GitHub-TOPY--AI--CEO--Skills-111827?style=for-the-badge&logo=github&logoColor=white" />
    </a>
    <a href="https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/LICENSE" aria-label="MIT License">
      <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-ff1212?style=for-the-badge" />
    </a>
    <a href="https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/actions" aria-label="GitHub Actions">
      <img alt="Build Status" src="https://img.shields.io/badge/Validation-passing-16a34a?style=for-the-badge" />
    </a>
    <a href="https://www.npmjs.com/search?q=skills" aria-label="npx skills">
      <img alt="npx Skills" src="https://img.shields.io/badge/npx-skills-0f172a?style=for-the-badge" />
    </a>
  </p>
  <p>
    <a href="#install">Install</a> ·
    <a href="#available-skills">Available Skills</a> ·
    <a href="#quick-start">Quick Start</a> ·
    <a href="#requirements">Requirements</a> ·
    <a href="#releases">Releases</a>
  </p>
  <p><strong>TOPY AI CEO is the agent-facing surface for user-dashboard workflows plus a general executive core skill for strategy, prioritization, crisis, stakeholders, competition, and debiasing.</strong></p>
</div>

---

## At a Glance

<table>
  <tr>
    <td><strong>Repository</strong><br/>TOPY-AI-LTD/TOPY-AI-CEO-Skills</td>
    <td><strong>License</strong><br/>MIT</td>
    <td><strong>Version</strong><br/>v0.2.0</td>
    <td><strong>Primary Install</strong><br/><code>npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills</code></td>
  </tr>
</table>

---

## Install

Install the full catalog:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills
```

Install a specific skill:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --skill topy-onboarding
```

Install for Codex:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --agent codex
```

Use a local checkout:

```bash
npx skills add ./topy-ai-ceo-skills
```

---

## Quick Start

1. Install the repo or the skill you need.
2. Set `TOPY_API_KEY` in your shell or agent environment.
3. Ask the agent to use the relevant TOPY skill.

Example:

```text
Use $topy-onboarding to create a project from this website.
```

```text
Use $topy-business-plans to generate a business plan for my project.
```

---

## Available Skills

<table>
  <tr>
    <td><strong><code>topy-ai-ceo-core</code></strong><br/>General CEO decision advisor and strategic reasoning core.</td>
    <td><strong><code>topy-dashboard</code></strong><br/>Router skill for TOPY workflows and skill selection.</td>
    <td><strong><code>topy-onboarding</code></strong><br/>Create projects from website, file, brainstorm, or direct idea.</td>
  </tr>
  <tr>
    <td><strong><code>topy-projects</code></strong><br/>Inspect, edit, archive, restore, and manage project resources.</td>
    <td><strong><code>topy-business-plans</code></strong><br/>Generate, inspect, edit, export, and manage business plans.</td>
  </tr>
  <tr>
    <td><strong><code>topy-templates</code></strong><br/>Create and edit business-plan templates.</td>
    <td><strong><code>topy-billing</code></strong><br/>Inspect credits, entitlements, subscriptions, and billing flows.</td>
  </tr>
  <tr>
    <td><strong><code>topy-media</code></strong><br/>List, register, and delete media assets.</td>
    <td><strong>All skills</strong><br/>Designed for user-dashboard workflows only in this release.</td>
  </tr>
</table>

---

## Requirements

- A valid `TOPY_API_KEY`
- Access to the TOPY backend API that powers the route maps in each skill
- `npx skills` available in the user environment

---

## Releases

This repository follows simple semantic version tags.

- `v0.1.0` initial public release
- `v0.1.1` README branding and repo validation workflow
- `v0.2.0` added the general `topy-ai-ceo-core` skill and organized references
- future releases will add new skills, route updates, or installation improvements

---

## Repository Layout

```text
skills/
  topy-ai-ceo-core/
  topy-dashboard/
  topy-onboarding/
  topy-projects/
  topy-business-plans/
  topy-templates/
  topy-billing/
  topy-media/
```

---

## License

MIT.
