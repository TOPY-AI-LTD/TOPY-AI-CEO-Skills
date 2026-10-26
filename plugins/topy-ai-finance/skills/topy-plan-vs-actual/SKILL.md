---
name: topy-plan-vs-actual
description: Explain how far the company is from its business plan, which plan assumptions reality has broken, and turn that into a reforecast and a plan revision the founder approves. Use when the user says things like "how far behind plan are we?"; "plan vs actual"; "which of our plan assumptions were wrong?"; "are we growing as fast as the plan said?"; "should we update the business plan?"; "reforecast the year". Needs the TOPY MCP server.
license: MIT
metadata:
  category: finance
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-plan-vs-actual/SKILL.md
---
# Plan vs actual

A business plan is a set of bets: growth rate, price, churn, hiring dates. Months later reality has voted on each.
This skill reads plan vs actual from TOPY, finds the assumptions reality has broken, explains the gap in plain
words, and proposes what to change: the plan, the targets, or nothing. Nothing in the plan changes until the
founder says yes.

## When to use
- "How far behind plan are we?", "which assumptions were wrong?", "reforecast".
- After `topy-monthly-close` calls a reforecast (a key metric more than 15% off plan), after quarterly planning, or after a big decision (raise, hire, price change).
- Not for: recording the month's actuals (`topy-monthly-close`); carrying an agreed change through the plan text (`topy-plan-revision`); building a model from scratch (`topy-financial-model`).

## Before you start
- The project (`projects_list`) and the plan of record (`plans_list`, latest successful version).
- `financial_scenarios_list`: a `plan` scenario must exist. If not, the plan's financials have not been extracted yet → offer `topy-financial-model`.
- `kpis_list`: actuals exist for the period? If the latest values are older than the KPI's cadence, run `topy-monthly-close` first; comparing against stale actuals misleads.

## Workflow
1. **Read.** `plan_vs_actual_get` with `scenario: plan`, `from`, `to` and `metrics`. Keep `rows` (period, plan, actual, `variance`, `variance_pct`, `source`), `cumulative` and `assumptions_broken`.
2. **Size the gap.** Per metric: month and cumulative `variance_pct`. Band it: within 5% on plan; 5–15% drifting; over 15% off plan. Direction matters: above plan on `net_burn` is bad.
3. **Find the broken assumptions.** Start from `assumptions_broken`, then trace each gap to its driver:

| Gap in | Usual drivers to check |
|---|---|
| `mrr`, `revenue_monthly` | new customers, price/ARPU, churn, launch date slipped |
| `new_customers` | traffic, conversion, sales cycle length |
| `net_burn` | hires earlier or dearer than plan, tool and ad spend |
| `cash_balance` | burn plus revenue gaps, a raise that came later |

   Each broken assumption: plan value, actual value, evidence (the row and its `source`). If the data can't show the driver, say "unknown" and name the figure needed.
4. **Separate timing from trend.** A one-month miss after a slipped launch is timing; three months of the same gap is trend. Only trends justify changing the plan.
5. **Recommend one path:**
   - **Accept the gap**: timing only, cumulative under 15%. Log it with `topy-decision-log`.
   - **Reforecast**: create a `current` scenario with `financial_scenario_create` (`name: current`, the corrected `assumptions`, `notes` citing the evidence). Preview, then confirm with a yes. The plan scenario stays as it was.
   - **Revise the plan**: write the change as a revision request and run `plan_revise_analyze` (it shows every section and figure affected; it does not change the plan). Hand the apply step to `topy-plan-revision`. Changing a target or goal is D2: hand to `topy-goal-tree`.
6. **Show and ask.** Present the table, the broken assumptions and the recommendation; ask which path the founder wants.

## Output
```
## Plan vs actual — <period> — <project>
| Metric | Plan | Actual | Variance | Cumulative | Source |
Broken assumptions
- <assumption>: plan <x>, actual <y> (evidence)
Timing or trend: …
Recommendation: accept | reforecast | revise plan — why
```

## Quality bar
- [ ] Every number comes from `plan_vs_actual_get` or a KPI value with a `source`.
- [ ] Each broken assumption names plan value, actual value and evidence.
- [ ] Timing and trend kept apart.
- [ ] One recommendation, with the founder's choice still open.
- [ ] No scenario created and no revision started without a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; KPI actuals carry a `source` (`source: founder` when the founder gave it). Never fill a gap with an estimate.
- Goal and target changes are D2: preview and the founder's yes, never under a standing permission.
- Records extracted from the plan carry an `origin`; after a revision, re-extraction leaves founder-edited records alone — say which ones would stay as they are.
- Anything sent outside TOPY is confirmed one send at a time. Money, equity and signatures are recorded and simulated only; an accountant should review a reforecast used with investors or lenders.

## Related skills
- `topy-monthly-close` — records the actuals and flags when a reforecast is due.
- `topy-plan-revision` — apply the agreed change across the plan.
- `topy-financial-model` — scenarios and projections in depth.
- `topy-goal-tree` — when the targets themselves should change.
- `topy-runway` — what the gap does to cash.
