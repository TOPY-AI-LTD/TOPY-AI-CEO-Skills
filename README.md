<div align="center">
  <p>
    <img src="https://www.topy.ai/long_logo.svg" alt="TOPY AI CEO" width="420" />
  </p>
  <h1>
    <span style="color:#ff1212;">TOPY AI CEO Skills</span>
  </h1>
  <p style="font-weight: 700; color: #ff1212;">
    A public skill catalog for CEO-level decision support, strategy, prioritization, crisis response, stakeholder management, competitive analysis, debiasing, and quantitative trade-offs.
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
    <a href="#one-line">One Line</a> ·
    <a href="#fit-check">Fit Check</a> ·
    <a href="#why-this-exists">Why This Exists</a> ·
    <a href="#core-capabilities">Core Capabilities</a> ·
    <a href="#ceo-daily-loop">CEO Daily Loop</a> ·
    <a href="#install">Install</a> ·
    <a href="#auth-and-api">Auth and API</a> ·
    <a href="#product-skill-workflow">Product Skill Workflow</a> ·
    <a href="#examples">Examples</a> ·
    <a href="#repository-structure">Structure</a>
  </p>
</div>

---

## One Line

**AI can give advice quickly. TOPY AI CEO Skills are designed to decompose trade-offs, expose hidden assumptions, predict competitive reactions, and keep high-stakes decisions grounded in actual constraints.**

---

## At a Glance

| Field | Value |
|---|---|
| Repository | `TOPY-AI-LTD/TOPY-AI-CEO-Skills` |
| License | `MIT` |
| Version | `v0.6.0` |
| Primary install | `npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills` |

---

## Fit Check

If you regularly face decisions like these, this skill set is a good fit:

| Scenario | Typical Questions |
|---|---|
| Strategic decisions | Enter a new market, build or buy, continue or stop? |
| Resource allocation | Which initiatives deserve scarce time, budget, and attention? |
| Crisis response | What do we do in the next 2 hours, 24 hours, and 2 weeks? |
| Stakeholder management | How do we align board, investors, leadership, and partners? |
| Competitive moves | If we launch, cut price, or expand, how will others respond? |
| Uncertainty | What evidence would change the answer, and how confident are we? |

---

## Why This Exists

Generic AI advice often looks polished but stops before the hard part:

- it names a framework but does not choose the right one
- it recommends action without showing the trade-off
- it overstates certainty when the evidence is weak
- it ignores who can block the decision
- it does not model competitor response
- it does not separate reversible tests from irreversible bets

TOPY AI CEO Core is the opposite: it forces the reasoning into a structured memo, then points to the smallest useful playbook for the task.

---

## What Makes It Different

### 1. Decision classification

It starts by naming the decision type:

- Type 1: irreversible or costly-to-reverse
- Type 2: reversible experiment
- Crisis: time-critical response
- Strategic bet: long-horizon uncertainty
- Operating design: org, process, OKR, KPI, or capacity question
- Capital decision: runway, budget, or investment choice
- Stakeholder decision: board, investor, employee, or partner alignment
- Competitive move: pricing, launch, position, or market entry

### 2. Trade-off discipline

It does not stop at "what should we do?"
It also shows:

- what we are giving up
- what happens if we do nothing
- what evidence would change the answer
- what makes the move reversible or irreversible

### 3. Bias and uncertainty checks

The skill explicitly calls out:

- anchoring
- confirmation bias
- sunk cost
- availability bias
- overconfidence
- status quo bias
- planning fallacy
- framing effects

### 4. Competitive and stakeholder realism

Good decisions fail when the world reacts.
This skill asks:

- who supports the move
- who resists it
- who needs to hear it first
- how competitors are likely to respond
- what the second round of the game looks like

### 5. Quantitative support

When the decision needs a calculation, the package includes small helper utilities for:

- weighted decision matrices
- ICE scoring
- expected value
- Monte Carlo simulation
- NPV and IRR
- Bayesian updates

---

## Core Capabilities

### Structured decision memo

The default output shape is a short memo with:

1. the real question
2. context and constraints
3. stakeholders
4. options and trade-offs
5. recommendation
6. risks to monitor
7. next steps

### Strategy and prioritization

Use this when the problem is choosing among competing paths with limited resources.

### Operating model and capital planning

Use this when the decision is about how the company runs, how metrics work, or how money should be raised or deployed.

### Crisis and stakeholder handling

Use this when timing matters and the sequence of communication is part of the solution.

### Competitive and market moves

Use this when the right answer depends on how competitors, customers, or the market are likely to react.

### Debiasing and uncertainty

Use this when confidence is too high, the evidence is incomplete, or the decision has hidden assumptions.

### Quantitative tools

Use this when a structured calculation is better than a narrative answer.

---

## CEO Daily Loop

The real value of the TOPY skill set comes from using the reasoning core together with the product workflow skills around it. A CEO can move through the day like this:

| Moment | Skill(s) | What you do |
|---|---|---|
| Morning review | `topy-ceo-workspace` | Weekly or daily review of decisions, risks and experiments; the three priorities to work on |
| New opportunity intake | `topy-projects` | Turn a website or a rough idea into a TOPY project; brainstorm ideas |
| Business plan creation | `topy-business-plan` | Write the plan after a credit check, follow it, summarise its numbers, export it |
| Plan critique and next-step selection | `topy-ai-ceo-core`, `topy-fundraising` | Find weak points, test GTM and competitor response, review it like an investor |
| The company changes | `topy-plan-revision` | Carry a new figure, milestone, KPI or hire through every affected section as a new version |
| Fundraising | `topy-fundraising` | SEIS Advance Assurance answers, investor pipeline, investor updates |
| Decisions and records | `topy-ceo-workspace` | Record the decisions, risks, research and experiments that came out of the review |

### How the skills fit together

- **`topy-ai-ceo`** is the entry point: how to reach TOPY, the shared rules, and which skill fits.
- **`topy-projects`** turns an idea or a website into a TOPY project and explores ideas.
- **`topy-business-plan`** writes the plan (after a credit check), edits and fixes it, exports it and manages templates.
- **`topy-plan-revision`** carries a change — funding, price, milestone, KPI, team — through every affected section as a new version.
- **`topy-fundraising`** reviews the plan like an investor, drafts SEIS Advance Assurance answers and keeps the investor pipeline and updates.
- **`topy-ceo-workspace`** keeps decisions, risks, the journal, GTM plans, growth experiments and research, and runs the weekly CEO review.
- **`topy-ai-ceo-core`** thinks like the CEO without touching your account: trade-offs, priorities, crises, competition.

### Typical CEO flow

1. A founder shares a website or an idea — `topy-projects` makes it a project.
2. `topy-business-plan` writes the first plan and summarises its numbers.
3. `topy-fundraising` reviews it like an investor; `topy-ai-ceo-core` pressure-tests the strategy.
4. The company changes — `topy-plan-revision` updates every affected section as a new version.
5. `topy-ceo-workspace` records the decisions behind it and runs the weekly review.

---

## Product Skill Workflow

The product skills work through TOPY's own tools — the same 90+ tools TOPY offers to Claude, ChatGPT and the
`topy` CLI — so plans, figures and records stay in the founder's TOPY account. Every change is previewed first
and runs only after the user confirms it; generating a plan costs 50 TOPY credits and the preview shows the
balance. The full tool list is at [topy.ai/developers](https://topy.ai/developers).

---

## Install

**Claude Code plugin** (skills and the TOPY MCP server together):

```bash
/plugin marketplace add TOPY-AI-LTD/TOPY-AI-CEO-Skills
/plugin install topy-ai-ceo@topy-ai
```

**Skills only** (Claude Code, Codex and other agents):

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --all
npx @topy-ai/ceo skills install        # the same product skills, from the TOPY CLI
npx skills update                      # upgrade later
```

---

## Auth and API

The product skills need TOPY connected, in one of these ways — no key is pasted into a prompt:

1. **MCP connector** (recommended): add `https://topy.ai/mcp` in Claude or ChatGPT, or
   `claude mcp add --transport http topy https://topy.ai/mcp`, and sign in to TOPY when asked.
2. **CLI**: `npm i -g @topy-ai/ceo && topy login`; the skills fall back to `topy <tool>` commands.
3. **API key**: create one under Dashboard → API keys and export `TOPY_API_KEY` for the CLI.

`topy-ai-ceo-core` does not call TOPY and needs none of these.

---

## Quick Start

1. Install the plugin or the skills.
2. Connect TOPY (MCP connector, or `topy login`).
3. Ask in plain words, or name the skill:

```text
Use $topy-business-plan to write a business plan for my TOPY project.
```

```text
Use $topy-plan-revision: we are raising £250k instead of £200k and hiring a CTO in Q2 2027.
```

```text
Use $topy-ai-ceo-core to prioritize five initiatives and explain the opportunity cost of delay.
```

---

## Examples

The core skill package includes example prompts that show what good output should look like:

- [market-entry.md](skills/topy-ai-ceo-core/examples/market-entry.md)
- [crisis-response.md](skills/topy-ai-ceo-core/examples/crisis-response.md)
- [prioritization.md](skills/topy-ai-ceo-core/examples/prioritization.md)
- [fundraising.md](skills/topy-ai-ceo-core/examples/fundraising.md)

There is also a lightweight eval suite for repeatable checks:

- [evals/evals.json](evals/evals.json)

---

## Available Skills

| Skill | Purpose |
|---|---|
| `topy-ai-ceo` | Entry point: connect TOPY, shared rules, pick the right skill |
| `topy-business-plan` | Generate, read, edit, fix, export plans; templates |
| `topy-plan-revision` | Revise a whole plan for a change, as a new version |
| `topy-fundraising` | Investor-ready review, SEIS Advance Assurance, investor pipeline and updates |
| `topy-ceo-workspace` | Decisions, risks, journal, GTM plans, experiments, research; weekly review |
| `topy-projects` | Projects from ideas or websites; ideas and brainstorms |
| `topy-ai-ceo-core` | CEO-level reasoning without the TOPY account |

---

## Requirements

- For the product skills: TOPY connected (MCP connector, `topy login`, or `TOPY_API_KEY`)
- For `topy-ai-ceo-core`: nothing

---

## Repository Structure

```text
.claude-plugin/          Claude Code plugin and marketplace manifests
.mcp.json                the TOPY MCP server (https://topy.ai/mcp)
skills/
  topy-ai-ceo/           SKILL.md, agents/openai.yaml (Codex)
  topy-business-plan/
  topy-plan-revision/
  topy-fundraising/
  topy-ceo-workspace/
  topy-projects/
  topy-ai-ceo-core/      SKILL.md, agents/, examples/, references/, scripts/
evals/
README.md
CHANGELOG.md
LICENSE
```

---

## Releases

This repository follows simple semantic version tags.

- `v0.1.0` initial public release
- `v0.1.1` README branding and repo validation workflow
- `v0.2.0` added the general `topy-ai-ceo-core` skill and organized references
- `v0.3.0` rewrote `topy-ai-ceo-core` into an original, organized executive playbook
- `v0.3.1` removed packaging artifacts and added a scripts ignore rule
- `v0.4.0` expanded the core references, examples, and eval suite
- `v0.4.1` removed the TOPY-specific example set from the core package
- `v0.4.2` expanded the README into a fuller landing page and usage guide
- `v0.4.3` added the CEO daily workflow across TOPY product skills
- `v0.4.5` documented the `--all` install path for the full skills catalog
- `v0.4.6` expanded the README with the TOPY product skill workflow
- `v0.5.0` added `topy-init`, standardized `TOPY_AI_KEY`, and documented auth preflight
- `v0.5.1` added the upgrade flow for installed skills
- `v0.6.0` product skills rebuilt on TOPY's MCP server and CLI; Claude Code plugin
- future releases will add new skills, route updates, or installation improvements

---

## License

MIT.
