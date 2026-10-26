---
name: topy-monthly-close
description: The founder's monthly close on TOPY.AI — last month's actuals recorded with their source, plan vs actual, runway at current pace and on plan, and a clear call on whether to reforecast or raise. Use when the user says things like "do last month's close"; "monthly close"; "are we ahead or behind plan this month?"; "how much runway do we have after last month?"; "record last month's numbers"; "month-end review". Needs the TOPY MCP server.
license: MIT
metadata:
  category: finance
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-monthly-close/SKILL.md
---
# Monthly close

On the first working day of the month the founder needs three answers: are we ahead of or behind plan, how long does
the cash last, and do we need to change the plan or start raising. This skill gets last month's actuals into TOPY
with their source, reads plan vs actual and runway, makes the call against fixed thresholds, and saves the monthly
review. Twenty to thirty minutes of founder time, most of it confirming figures.

## When to use
- "Monthly close", "month-end", "record last month's numbers", the first working day of the month.
- Before the monthly investor update (then hand off to `topy-investor-relations`).
- Not for: explaining one gap in depth or proposing a plan change (`topy-plan-vs-actual`); a runway cut plan (`topy-runway`); designing KPIs (`topy-kpi-dashboard`).

## Before you start
- The project (`projects_list`) and the month. The `period_date` of a monthly value is the month's last day (e.g. 2027-01-31).
- `kpis_list`: find the finance KPIs by `metadata_json.key` — `revenue_monthly`, `mrr`, `cash_balance`, `net_burn`, `gross_margin`, plus `new_customers` and `churn_rate_monthly`. Missing ones → offer `topy-kpi-dashboard` first.
- `kpi_values_list` per KPI: which already have a value for the month (e.g. synced by `topy-integrations`) and which are missing.
- Ask for missing figures one at a time, and ask where each comes from. Never ask for bank or Stripe logins.

## Workflow
1. **Collect actuals.** For each finance KPI without a value for the month:
   - From the CFO's tools or a connected source: use that figure and that source (`stripe`, `ledger`, `bank`…).
   - From the founder: record it with `source: founder` and say it is founder-reported.
   - No figure at all: leave it empty and list it as missing. Never estimate.
2. **Record.** `kpi_value_record` per figure: `period_date`, `actual_value`, `note`, `metadata_json` `{source, evidence_ref, recorded_by_role: "CEO"}`. Show all figures in one preview table, confirm after the founder's yes. A result with `replaced: true` overwrote an earlier value: say which and what it was.
3. **Plan vs actual.** `plan_vs_actual_get` with `scenario: plan`, the month (and year to date), metrics `mrr,revenue_monthly,net_burn,cash_balance`. Read `rows` (plan, actual, `variance_pct`, `source`), `cumulative` and `assumptions_broken`.
4. **Runway.** `runway_get` with `scenario: plan` and again with `scenario: current`. Report both `runway_months_current` (at the last three months' average burn) and `runway_months_scenario` (on plan), plus `cash`, `avg_net_burn_3m` and `zero_cash_date`.
5. **Make the call** (fixed rules, not judgement):

| Signal | Call | Next |
|---|---|---|
| Any key metric `variance_pct` worse than 15% (month or cumulative) | Reforecast | `topy-plan-vs-actual` (CEO-J21) |
| `runway_months_current` under 9 | Start raise planning | `topy-fundraising-strategy` (CEO-J10) |
| Under 6 months | Both, and a cut plan | `topy-runway` |
| Neither | Carry on | note the one assumption to watch |

   "Worse" means below plan for higher-is-better KPIs and above plan for `net_burn`.
6. **Save the review.** `ceo_brief_create` with `brief_type: monthly`, `title` "Monthly close — <month>", `content` (below), `payload_json` with every figure, its `source` and `as_of`. Preview, then confirm with a yes. A scheduled agent with a standing permission may save the brief; the call itself and any plan change still go to the founder.
7. **Offer next steps**, at most two: the investor update draft (`topy-investor-relations`), the reforecast, or the raise.

## Output
```
## Monthly close — <month> — <project>
Call: carry on | reforecast | raise   (one line why)
| Metric | Plan | Actual | Variance | Source |
Runway: <x> months at current pace, <y> on plan; zero cash <yyyy-mm>
Broken assumptions: …
Missing figures: …
Next: …
```

## Quality bar
- [ ] Every actual has a `source`; founder-given figures are labelled.
- [ ] Runway given both ways, with the date of the cash figure.
- [ ] The call follows the thresholds; any override is stated as the founder's.
- [ ] Missing figures are listed, not filled in.
- [ ] Nothing saved without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; every KPI actual carries a `source`, and a figure the founder gives is recorded as `source: founder`. Financial figures come from the CFO's books or a connected source, never from memory.
- Changing a goal or target is a D2 decision: preview and the founder's yes, never under a standing permission.
- Records extracted from the plan carry an `origin`; say so before changing one the founder has edited.
- Anything sent outside TOPY (an investor update, a shared link) is confirmed one send at a time. Money, equity and signatures are recorded and simulated only; an accountant should check the close before it is used for tax or filings.

## Related skills
- `topy-plan-vs-actual` — explain the gap and propose a plan revision.
- `topy-runway` — burn, levers and the cut plan.
- `topy-fundraising-strategy` — when runway is under nine months.
- `topy-investor-relations` — turn the close into the monthly investor update.
- `topy-integrations` — let Stripe or the ledger record the actuals automatically.
