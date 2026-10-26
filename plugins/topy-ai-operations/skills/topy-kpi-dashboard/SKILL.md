---
name: topy-kpi-dashboard
description: Choose the north-star metric, the input metrics that drive it and the guardrails, turn them into a weekly scorecard with owners, targets and red/amber/green rules, and with TOPY create them as KPIs and record their values. Use when the user says things like "what should our north star metric be?"; "we track 40 metrics and none of them help"; "build a weekly scorecard for the leadership meeting"; "which KPIs matter at our stage?"; "set up our KPIs in TOPY"; "record this week's MRR". Uses TOPY when it is connected.
license: MIT
metadata:
  category: operations
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-kpi-dashboard/SKILL.md
---
# KPI dashboard

Gives a company one page that says, every week, whether it is on track and where to look if not. It picks a
north-star metric, breaks it into input metrics teams can move, adds guardrails so the inputs are not gamed, and sets
plain rules for red, amber and green. With TOPY connected, the scorecard becomes real KPIs: the operating board
computes their health and the daily brief flags any that go stale.

## When to use
- Choosing a north star, cleaning up a sprawling dashboard, starting a weekly scorecard, preparing board metrics.
- "Record this week's value", "change the MRR target", "set the threshold".
- Not for: setting quarterly goals (`topy-okrs`); CAC, LTV and payback in depth (`topy-unit-economics`); connecting data sources so values arrive automatically (`topy-integrations`).

## Before you start
- Ask one question at a time: business model; the main goal for 6-12 months; metrics tracked today and their source system; who owns which function.
- With TOPY: `kpis_list` first. Extend or fix what exists; don't create a second KPI for the same `key`.
- Without TOPY: the method below works on its own; the scorecard lives in a spreadsheet.

## Workflow
1. **Pick the north star.** Shortlist 2-3 and test each: rises only when customers get value? leads revenue? measurable weekly? most teams can move it? hard to inflate? Record why the runner-up lost.
2. **Build the metric tree** as a formula where possible (active accounts = new activated + retained − churned; new activated = sign-ups × activation rate). Keep 3-6 **inputs**: move within weeks, one owner, clear link to the north star.
3. **Add 2-3 guardrails** with a floor (gross margin, churn, support time, burn).
4. **Drop reporting-only metrics** nobody would act on.
5. **Define every metric**: formula, inclusions, source, window, refresh time, owner. Use the standard keys where they fit: `mrr`, `revenue_monthly`, `cash_balance`, `net_burn`, `runway_months`, `gross_margin`, `cac`, `ltv_cac`, `payback_months`, `churn_rate_monthly`, `nrr`, `new_customers`, `pipeline_value`, `win_rate`, `signups`, `organic_sessions`, `ai_visibility_score`, `activation_rate`, `active_users_weekly`, `pmf_score`, `uptime`, `deploy_frequency`; anything else is `custom.<name>`. Financial KPIs are owned by the CFO and read from its ledger.
6. **Targets and status rules.** Targets come from the plan, the OKRs or the founder, never invented. TOPY's default health: green at ≥ 95% of the expected value for the date, amber 80-95%, red below 80% (reversed when lower is better); unknown when no value within the cadence. Adjust per KPI only with a reason.
7. **Create in TOPY (with a yes).** For each line, preview `kpi_create`: `name`, `category` (`revenue` · `growth` · `product` · `finance` · `operations` · `security`), `unit` (`GBP`, `%`, `count`, `months`), `baseline_value`, `target_value`, `cadence` (`daily` · `weekly` · `monthly` · `quarterly`), `status: "active"`, `metadata_json` {`key`, `higher_is_better`, `owner_role`, `objective_id` (if it is a KR), `targets_by_period` (e.g. `{"2027-03": 20000}`), `thresholds: {"at_risk": 0.95, "off_track": 0.80}`, `curve` if growth isn't linear, `source` (where values come from), `origin: {"type": "founder"}`}. Show all lines together; confirm each only after the founder agrees.
8. **Change a KPI.** Read it from `kpis_list`, merge into the whole `metadata_json` (it is replaced, not merged), then preview `kpi_update`. A target change on a KR is a goal change: say so and get the founder's explicit yes. If the KPI has `metadata_json.edited: true` or `origin.type: "plan"`, say who set it before changing it.
9. **Record values.** Preview `kpi_value_record` with `period_date` (the period's end date), `actual_value`, `note`, and `metadata_json.source` (`stripe`, `ga4`, `ledger`… or `founder` when they told you) plus `evidence_ref` if any. Writing the same period again replaces it (`replaced: true`): say so first. For values that should arrive automatically, use `topy-integrations`.
10. **Owners and actions.** Red gets a cause and a next step at the weekly review; red twice gets a dated plan.
11. **Review quarterly.** KPIs nobody acted on: preview `kpi_update` with `status: "retired"` (keeps history) rather than deleting.

## Output
```
KPI dashboard: <company> · <model> · <date>
North star: <name> = <formula> · why: <reason> · runner-up: <name>, rejected because <reason>
Metric tree: <north star> ← <input 1> × <input 2> …
| Metric | Key | Type (north star/input/guardrail) | Owner | Cadence | Target or floor | Thresholds | Source | Status |
Definitions: | Metric | Formula | Includes/excludes | Source | Window | Owner |
Saved in TOPY: <KPI ids> (only after confirmation)
```

## Quality bar
- The north star passes all five tests or the failed one is named with its mitigation.
- Every input links to the north star; at least two guardrails with floors.
- Every line has one owner, a definition, a cadence and a source; 15 lines at most.
- No duplicate KPI for one `key`; standard keys used where they fit.
- No target invented; each has its source. Every recorded value has a `source`.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools or the founder; a value the founder gives is recorded with `source: founder`. Never estimate a missing value.
- KR targets are D2: a preview and the founder's yes, never under a standing permission. Recording values may run under one.
- Never invent benchmarks or "industry averages"; tolerances and examples are rules of thumb.
- Management metrics are not audited figures; statutory definitions are an accountant's call.
- No individual employees' performance data on a company scorecard.

## Related skills
- `topy-operating-cadence` — the weekly forum that reads the scorecard.
- `topy-okrs` — quarterly goals whose KRs are these KPIs.
- `topy-operating-board` — health computed from them.
- `topy-integrations` — values from Stripe, GA4 and others automatically.
- `topy-unit-economics` — the economics behind margin and payback guardrails.
- `topy-growth-experiments` — experiments aimed at a lagging input.
