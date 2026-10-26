---
name: topy-gtm-plan
description: Build and keep the project's go-to-market plan in TOPY (positioning, channels, activation, retention, pricing, sales motion, funnel targets, launch) and hand plan-wide changes to topy-plan-revision. Use when the user says things like "write our go-to-market plan"; "how are we going to get customers?"; "update the GTM, we're dropping paid ads"; "which channels should we focus on?"; "set funnel targets for next quarter"; "plan the launch". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-gtm-plan/SKILL.md
---
# Go-to-market plan

A go-to-market plan answers one question concretely: who buys, why, how they find out, how they start, why they stay, and what that adds up to. This skill builds that plan from what TOPY already knows about the project (profile, business plan, research, experiments), keeps it as a GTM record the founder can update as the market answers back, and spots when a GTM change has to be carried through the business plan as well.

## When to use
- A new project, or a plan that says "marketing" without saying how.
- A channel, segment, price or sales motion is changing.
- Quarter planning: new funnel targets.
- Not for: rewriting the business plan for a change (`topy-plan-revision`); a single channel test (`topy-growth-experiments`); the pricing decision itself (`topy-pricing-decisions`); executing campaigns (the CMO).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- Read first: `gtm_plans_list` (update an existing plan rather than starting a parallel one), `project_get`, `plans_list` and `plan_get` (the marketing, sales and financial sections), `research_sources_list`, `growth_experiments_list` (what was already tried and learned).
- Ask, one at a time, only for what those do not answer.
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Positioning and value proposition
- `positioning`: for [segment] who [problem], [product] is a [category] that [key benefit]; unlike [main alternative], it [difference]. The alternative is often a spreadsheet or doing nothing, not a competitor.
- `value_proposition`: the outcome in the customer's words and the proof (a result, a customer, a number the founder has).
- One beachhead segment first. A plan aimed at "SMEs" is not a plan.

### 2. Channels
- `acquisition_channels`: a short list of strings. Pick one or two primary channels to concentrate on, and at most two to test, each tied to where the beachhead segment already spends attention.
- Match channel to deal size: under ~£100 a year needs self-serve and low-cost channels (SEO, product-led, community); over ~£5k a year can carry outbound and founder-led sales.
- Channels already killed in `growth_experiments_list` stay out unless something material has changed; say so.

### 3. Activation and retention
- `activation_strategy`: the steps from sign-up to first value and the "aha" moment, e.g. `["import first client list", "send first reminder within 10 minutes"]`.
- `retention_strategy`: why they come back and what happens when they stop.

### 4. Pricing and sales motion
- `pricing_strategy`: model, value metric, tiers and price points as the founder has set them, e.g. `{"model": "per location", "tiers": [{"name": "Starter", "price_gbp_month": 49}]}`. A new or changed price is a decision: use `topy-pricing-decisions`.
- `sales_motion`: self-serve, inside sales, founder-led, partner or channel, with who does it and how many hours a week.

### 5. Funnel targets
Work back from the revenue goal the founder gives: revenue ÷ average revenue per customer = customers; ÷ close or conversion rate = qualified leads or trials; ÷ lead rate = visitors or contacts. Store in `funnel_targets`, e.g. `{"period": "2027-Q1", "new_customers": 30, "trials": 250, "visitors": 8000, "assumptions": {"trial_to_paid": 0.12, "visit_to_trial": 0.03}, "source": "founder figures Oct 2026"}`. Every rate is either the founder's real figure or labelled an assumption to test.

### 6. Launch plan
`launch_plan`: phases with dates, owner and the gate to move on, e.g. `{"phases": [{"name": "Private beta", "from": "2026-11-15", "gate": "10 active clinics"}, {"name": "Public launch", "from": "2027-01-20"}]}`.

### 7. Save
- New plan: preview `gtm_plan_create` (`name` defaults to "Primary GTM"), show the full plan, confirm with `confirm: true` and the `confirmation` only after the founder agrees.
- Change: `gtm_plan_get`, preview `gtm_plan_update` with only the changed fields. List fields and `metadata_json` are replaced whole, so send the complete new list. For a major pivot, keep history: create a new record (e.g. "GTM v2, Nov 2026") instead of overwriting, and log the reason with `topy-decision-log`.
- `gtm_plan_delete` only when the founder asks to remove an abandoned draft; say it is permanent and cannot be undone, then follow the two-call rule.
- GTM tools are not covered by standing permissions: a scheduled agent cannot write them.

### 8. Check against the business plan
Compare the GTM with the plan's marketing, sales, pricing and financial sections. Any mismatch in a figure, price, channel, target or launch date that the plan relies on goes to `topy-plan-revision`, which analyses the change across the plan and writes a new plan version, keeping the original. Do not edit plan sections from this skill.

## Output
Sections in order: Positioning · Value proposition · Channels (primary / testing) · Activation · Retention · Pricing · Sales motion · Funnel targets (table `Stage | Target | Rate | Real or assumed`) · Launch phases · Open questions · Changes for `topy-plan-revision`.

## Example
Founder of Quillmoor (a fictional booking tool for independent driving instructors): "We're dropping Google Ads; update the GTM."
- `gtm_plans_list` → "Primary GTM" with channels `["google_ads", "seo", "instructor_facebook_groups"]`. `growth_experiments_list` shows the ads test killed (cost per paid instructor £140 vs £45 target).
- Proposed update: channels `["instructor_facebook_groups", "seo", "driving_school_partnerships"]` (the last one marked as a test); funnel targets recomputed from the founder's goal of 60 new instructors in Q1 with their real 9% trial-to-paid rate.
- Preview shown; founder agrees; confirmed. The business plan's marketing budget still assumes £2k a month of ads, so that change is listed for `topy-plan-revision`.

## Quality bar
- [ ] One beachhead segment, named concretely.
- [ ] One or two primary channels, each with a reason it reaches that segment.
- [ ] Funnel targets add up from the revenue goal, and every rate is marked real or assumed.
- [ ] Nothing contradicts a killed experiment without saying why.
- [ ] Mismatches with the business plan listed for `topy-plan-revision`.
- [ ] Every write was previewed and confirmed only after a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent conversion rates, market sizes, customers or prices; label assumptions as assumptions and cite sources from the research library.
- Never edit the business plan from here; plan-wide changes go through `topy-plan-revision`, which keeps the original version.
- Deletes are permanent (risk W4).
- Pricing, advertising and outreach must follow consumer, data-protection and marketing law: say when a lawyer should look.

## Related skills
- `topy-plan-revision` — carry a GTM change through the business plan.
- `topy-growth-experiments` — test the channels marked as tests.
- `topy-pricing-decisions` — set or change the price.
- `topy-research-library` — evidence behind segment and market claims.
