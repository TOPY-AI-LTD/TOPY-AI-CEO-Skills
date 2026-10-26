---
name: topy-user-journey
description: Map the customer journey for each persona in TOPY, tie every stage to a KPI and the experiments working on it, and find the stage where most customers drop out. Use when the user says things like "map our customer journey"; "where do we lose most customers?"; "which stage drops off the most?"; "draw the user journey for our main persona"; "link our experiments to the funnel"; "update the journey for small agencies". Needs the TOPY MCP server.
license: MIT
metadata:
  category: strategy
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-user-journey/SKILL.md
---
# User journey

A persona says who the customer is; a journey says how they move from never having heard of you to paying and
staying, and where they fall out. This skill builds that journey in TOPY for each persona, hangs the right KPI and
the running experiments on each stage, and reads the numbers to find the one stage worth fixing first.

## When to use
- "Map the customer journey", "where do we lose people?", "which stage is weakest?"
- After personas exist (`topy-customer-personas`), and each quarter when the funnel numbers move.
- Not for: defining who the customer is (`topy-customer-personas`); running one experiment (`topy-growth-experiments`); the channel plan (`topy-gtm-plan`).

## Before you start
- The project (`projects_list`). `personas_list`: no persona → run `topy-customer-personas` first. Pick one persona per journey; `persona_get` for its pains, channels and buying criteria.
- `journeys_list`: a journey for this persona may exist; update it rather than create a second.
- `kpis_list` and `growth_experiments_list`: what can be linked to stages.

## Workflow
1. **Stages.** Default five, renamed to fit the business: Discover → Evaluate → Start (sign-up/trial) → Value (activation) → Pay & stay. B2B with sales adds Qualify and Close. Keep 4–7 stages.
2. **Fill each stage** with the founder, one stage at a time, starting from the persona's fields:

| Field | What goes in | Example |
|---|---|---|
| `name` | stage name | "Evaluate" |
| `touchpoints` | where it happens | `["pricing page", "demo call"]` |
| `user_goal` | what the customer wants here | "Know it works with Shopify" |
| `pains` | what stops them | `["no case study for my niche"]` |
| `emotion` | one word | "sceptical" |
| `kpi_ids` | the KPI measuring this stage | `signups`, `activation_rate`, `win_rate`, `churn_rate_monthly` |
| `experiment_ids` | experiments acting on this stage | from `growth_experiments_list` |

   A stage without a KPI is a blind spot: list it and offer `topy-kpi-dashboard` to create one.
3. **Save.** `journey_create` with `persona_id`, `name`, `stages`, `metadata_json` `{origin: {type: "founder"}}` (or `agent`); for an existing one, `journey_get`, merge, then `journey_update` with the whole `stages` array (it replaces the old one). Preview, confirm after a yes. If `metadata_json.origin.type` is `plan` and the founder has edited the journey, say what would change before writing.
4. **Link experiments.** For each experiment tied to a stage, `growth_experiment_update` its `metadata_json` with `journey_stage` (read, merge, send the whole object). Preview and confirm.
5. **Find the drop-off.** `kpi_values_list` for each stage KPI over the same period. Stage conversion = next stage's volume ÷ this stage's volume where both are counts; for rate KPIs compare against target. The biggest drop is the stage with the lowest conversion relative to its target. Missing data → say which stage is unmeasured; never estimate it.
6. **Recommend one action** on the weakest stage: an experiment (`topy-growth-experiments`), a GTM change (`topy-gtm-plan`), or a quarterly objective (`topy-goal-tree`, a D2 change the founder approves).

`journey_delete` only for a duplicate or a mistake: permanent, two calls.

## Output
```
## Journey — <persona>
| Stage | Goal | Pains | KPI (latest, source) | Experiments |
Biggest drop-off: <stage> — <conversion> vs <target>
Blind spots: <stages with no KPI or data>
Next: <one action>
```

## Quality bar
- [ ] One persona per journey; 4–7 stages.
- [ ] Every stage has a KPI or is listed as a blind spot.
- [ ] Drop-off figures come from KPI values with a `source`.
- [ ] `stages` and `metadata_json` sent whole on update.
- [ ] Nothing saved without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; KPI actuals carry a `source` (`source: founder` when the founder gave it). Never invent customer quotes, pains or conversion rates; label assumptions.
- Goal changes are D2: preview and the founder's yes, never under a standing permission.
- Records extracted from the plan carry an `origin`; say so before changing one the founder has edited.
- Nothing is sent outside TOPY from this skill; customer-facing changes go through the matching cofounder and are approved one at a time.

## Related skills
- `topy-customer-personas` — who each journey is for.
- `topy-growth-experiments` — test a fix on the weakest stage.
- `topy-gtm-plan` — channels per stage.
- `topy-kpi-dashboard` — create the KPI a stage is missing.
