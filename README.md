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
| Version | `v0.5.0` |
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
| Morning review | `topy-dashboard`, `topy-projects`, `topy-billing`, `topy-init` | Review active projects, check resource constraints, and confirm the TOPY key and account state before starting expensive work |
| New opportunity intake | `topy-onboarding` | Convert a website, local file, brainstorm, or rough idea into a structured project |
| Business plan creation | `topy-business-plans` | Draft or regenerate the plan for a project, then prepare it for review or export |
| Plan critique and next-step selection | `topy-ai-ceo-core` | Analyze the plan, find weak points, evaluate GTM strategy, test competitor response, and recommend the next move |
| Template design | `topy-templates` | Turn strong plan patterns into reusable templates so future projects start faster |
| Project editing and decisions | `topy-projects` | Update the live project record with the decisions, risks, research, and action items that came out of the review |
| Media and assets | `topy-media` | Attach and manage uploaded or URL-based media that supports the project or plan |

### How the skills fit together

- Use **`topy-dashboard`** when you want the router skill to choose the right workflow.
- Use **`topy-onboarding`** to create the first structured project record from raw input.
- Use **`topy-business-plans`** to create, edit, export, and regenerate the business plan.
- Use **`topy-ai-ceo-core`** to think like the CEO: diagnose the weak points, choose the next step, and pressure-test the strategy.
- Use **`topy-projects`** to keep project decisions, research, and resources synchronized.
- Use **`topy-templates`** to capture a reusable structure once the plan shape is working.
- Use **`topy-billing`** to understand credits, entitlements, and subscription limits before expensive actions.
- Use **`topy-media`** to manage the supporting assets attached to the work.
- Use **`topy-init`** first when the TOPY key is missing or the environment has not been prepared yet.

### Skill map

| Skill | Typical inputs | Typical outputs |
|---|---|---|
| `topy-dashboard` | A broad CEO task, a request to choose the right workflow, or a multi-skill starting point | A routed next step and the right specialist skill |
| `topy-onboarding` | Website URL, local file, brainstorm, or short idea | A structured project record with initial scope and context |
| `topy-projects` | Existing project ID, project metadata, resources, or edits | Updated project records, archived or restored state, and project-level decisions |
| `topy-business-plans` | Project context, plan options, template choices, edits, or export request | A generated, edited, regenerated, or exported business plan |
| `topy-templates` | Template content, structure goals, or refinement request | A reusable business-plan template definition |
| `topy-billing` | Account status, credit questions, entitlements, subscription actions | Credit balance, transaction data, plans, or checkout/portal actions |
| `topy-media` | Image URL, uploaded asset reference, or deletion request | Media registration, listing, or removal actions |
| `topy-init` | Missing key, new environment, or first-time setup | A ready `TOPY_AI_KEY` and confirmed base URL |
| `topy-ai-ceo-core` | A decision, trade-off, plan, market move, crisis, or uncertainty question | A structured decision memo with recommendation, risks, and next steps |

### Typical CEO flow

1. A founder sends a website, file, or rough concept.
2. `topy-onboarding` turns it into a project.
3. `topy-business-plans` creates a first-pass plan.
4. `topy-ai-ceo-core` reviews the plan, identifies weak points, and recommends the next step.
5. `topy-projects` stores the decision trail and supporting research.
6. `topy-templates` captures the reusable structure if the pattern is worth repeating.
7. `topy-billing` verifies that the current account can support more generation or growth.
8. `topy-media` attaches any files or visual assets needed for the plan.
9. `topy-init` is used first whenever the key is missing, expired, or not loaded in the environment.

---

## Product Skill Workflow

The product skills are not separate from the CEO work. They are the operating system the CEO uses every day.

### 1. Start with the project

Use `topy-onboarding` to turn raw material into a structured project:

- website URL
- local file
- brainstorm notes
- rough idea or founder pitch

What you get:

- a project record
- initial scope
- source context
- a base to iterate from

### 2. Shape the plan

Use `topy-business-plans` to create the business plan from that project.

What you get:

- initial plan draft
- edited sections
- regenerated weak sections
- exportable output

### 3. Pressure-test the plan

Use `topy-ai-ceo-core` to act like the CEO and challenge the plan:

- what is weak or missing
- what are the biggest assumptions
- what is the GTM sequence
- what are the weak competitors and likely responses
- what is the next best step

This is where the CEO answers:

- should we continue?
- should we change the plan?
- should we wait?
- should we kill the idea?

### 4. Keep the project live

Use `topy-projects` to record the project state after the decision:

- decisions made
- risks discovered
- research and notes
- updated metadata
- archive or restore actions

### 5. Turn good structure into a template

Use `topy-templates` when a plan shape is repeatable:

- create a template from a strong structure
- refine the template
- reuse it for similar opportunities

### 6. Check limits before expensive actions

Use `topy-billing` before generation-heavy or access-controlled operations:

- credits
- subscriptions
- entitlements
- portal or checkout actions

### 7. Attach supporting assets

Use `topy-media` for files, images, or URL-based assets that belong to the project or plan.

### 8. Initialize access when needed

Use `topy-init` when the environment is not ready yet:

- set `TOPY_AI_KEY`
- confirm `https://topy.ai/api`
- stop any non-core workflow until auth is available

### Why this matters for a CEO

A good CEO workflow is not:

- one prompt
- one plan
- one answer

It is a loop:

1. capture the opportunity
2. turn it into a project
3. generate a plan
4. critique the plan
5. update the project
6. turn the pattern into a template
7. manage credits and constraints
8. keep the supporting assets organized

That is the daily operating loop the TOPY skills are built to support.

---

## Install

Install the full catalog:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills
```

Install all skills without prompting:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --all
```

Install a specific skill:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --skill topy-ai-ceo-core
```

Install the initializer:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --skill topy-init
```

Install for Codex:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --agent codex
```

Use a local checkout:

```bash
npx skills add ./topy-ai-ceo-skills
```

Upgrade installed skills:

```bash
npx skills update
```

Upgrade a single skill:

```bash
npx skills update topy-init
```

---

## Auth and API

All non-core TOPY skills call the live API at:

```text
https://topy.ai/api
```

Use `TOPY_AI_KEY` as the bearer token for those calls. If the key is missing:

1. stop the workflow
2. route the user to `topy-init`
3. ask them to set `TOPY_AI_KEY`
4. resume the original skill only after auth is available

`topy-ai-ceo-core` does not call the TOPY API and does not require the key.

---

## Quick Start

1. Install the repo or the skill you need.
2. If the key is missing, start with `topy-init`.
3. Set `TOPY_AI_KEY` in your shell or agent environment.
4. Ask the agent to use the relevant TOPY skill.
5. If you are unsure, start with `topy-ai-ceo-core`.
6. Use the examples or evals when you want a repeatable prompt pattern.

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
| `topy-init` | Initialize `TOPY_AI_KEY` and confirm the TOPY API base URL |
| `topy-dashboard` | Router skill for TOPY workflows and skill selection |
| `topy-onboarding` | Create projects from website, file, brainstorm, or direct idea |
| `topy-projects` | Inspect, edit, archive, restore, and manage project resources |
| `topy-business-plans` | Generate, inspect, edit, export, and manage business plans |
| `topy-templates` | Create and edit business-plan templates |
| `topy-billing` | Inspect credits, entitlements, subscriptions, and billing flows |
| `topy-media` | List, register, and delete media assets |

---

## Requirements

- A valid `TOPY_AI_KEY`
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
  topy-init/
    SKILL.md
    agents/
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
- `v0.4.3` added the CEO daily workflow across TOPY product skills
- `v0.4.5` documented the `--all` install path for the full skills catalog
- `v0.4.6` expanded the README with the TOPY product skill workflow
- `v0.5.0` added `topy-init`, standardized `TOPY_AI_KEY`, and documented auth preflight
- `v0.5.1` added the upgrade flow for installed skills
- future releases will add new skills, route updates, or installation improvements

---

## License

MIT.
