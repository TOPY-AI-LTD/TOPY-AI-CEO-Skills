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
    <a href="#install">Install</a> ·
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
| Version | `v0.4.2` |
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

## Install

Install the full catalog:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills
```

Install a specific skill:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --skill topy-ai-ceo-core
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
4. If you are unsure, start with `topy-ai-ceo-core`.
5. Use the examples or evals when you want a repeatable prompt pattern.

Examples:

```text
Use $topy-ai-ceo-core to evaluate a market entry decision with trade-offs and a recommendation.
```

```text
Use $topy-ai-ceo-core to prioritize five initiatives and explain the opportunity cost of delay.
```

```text
Use $topy-ai-ceo-core to handle a crisis response plan with immediate containment and stakeholder sequencing.
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
| `topy-ai-ceo-core` | Recommended starting point for CEO-level reasoning |
| `topy-dashboard` | Router skill for TOPY workflows and skill selection |
| `topy-onboarding` | Create projects from website, file, brainstorm, or direct idea |
| `topy-projects` | Inspect, edit, archive, restore, and manage project resources |
| `topy-business-plans` | Generate, inspect, edit, export, and manage business plans |
| `topy-templates` | Create and edit business-plan templates |
| `topy-billing` | Inspect credits, entitlements, subscriptions, and billing flows |
| `topy-media` | List, register, and delete media assets |

---

## Requirements

- A valid `TOPY_API_KEY`
- Access to the TOPY backend API that powers the route maps in each skill
- `npx skills` available in the user environment

---

## Repository Structure

```text
skills/
  topy-ai-ceo-core/
    SKILL.md
    agents/
    examples/
    references/
    scripts/
  topy-dashboard/
  topy-onboarding/
  topy-projects/
  topy-business-plans/
  topy-templates/
  topy-billing/
  topy-media/
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
- future releases will add new skills, route updates, or installation improvements

---

## License

MIT.
