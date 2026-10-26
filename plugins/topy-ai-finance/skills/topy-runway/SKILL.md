---
name: topy-runway
description: Measure burn and runway properly, check whether the company is default alive, and build a tiered cut plan with triggers so the founder decides early instead of in a panic. Use when the user says things like "how much runway do we have?"; "are we default alive or default dead?"; "when do we run out of cash?"; "we need to cut burn, where do we start?"; "what if the fundraise takes six months longer?"; "can we get to profitability on the cash we have?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: finance
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-runway/SKILL.md
---
# Runway and burn

Tells the founder how long the money lasts, whether the company can reach break-even on the cash it has,
and what to cut, in which order, if it cannot. Runway is computed on cash, not profit, and forward-looking,
not just from last month. With TOPY connected the figures come from the company's own records (`runway_get`,
CFO-sourced KPI values); without it, the founder's exports work the same way. The cut plan is written while there is still time to choose: each tier has a
trigger, a saving and a date, so the decision is made once, calmly, and then executed if the trigger fires.

## When to use
- "Runway", "burn", "zero-cash date", "default alive", "cut plan", "what if the raise slips".
- Monthly, as part of the close (`topy-monthly-close`); immediately when a raise is delayed or revenue misses.
- Not for: a full three-statement model (use `topy-financial-model`); deciding the raise amount (use
  `topy-fundraising-strategy`); diagnosing CAC or churn (use `topy-unit-economics`).

## Before you start
- With TOPY connected, read first:
  - `runway_get` (scenario `current`): `cash`, `avg_net_burn_3m`, `runway_months_current`,
    `runway_months_scenario`, `zero_cash_date` and `sources`. Run it again with scenario `plan` for the plan view.
  - `kpi_values_list` for the KPI keys `cash_balance`, `net_burn` and `revenue_monthly` (last 6 periods): the
    trend, and each value's `source` and `period_date`. A value older than the KPI's cadence is stale: say so.
  - `plan_vs_actual_get` (scenario `plan`, metrics `net_burn,revenue_monthly,cash_balance`, last 3-6 months):
    where burn or revenue drifted from the plan, and `assumptions_broken`.
  - If `runway_get` has no cash or burn (no values recorded yet), fall back to manual input below and offer
    `topy-monthly-close` to record the actuals.
- Without TOPY, ask one question at a time: cash today; committed money and its expected date; cash in and cash out per
  month for 3-6 months; expected revenue growth; planned cost changes; the cash floor the founder will not
  go below.
- Ask for one-offs separately (annual prepayments received, a legal bill, equipment) so they do not distort
  the monthly burn.
- TOPY is optional: the method works on exported figures. Never ask for bank logins; balances and statements the founder exports are enough.

## Workflow
1. **Measure burn on cash.**
   - `gross burn = total cash out in the month` (salaries, on-costs, rent, tools, marketing, suppliers, tax).
   - `net burn = cash out − cash in` (cash in = customer receipts, not invoiced revenue).
   - Use a 3-month average and strip out one-offs. If annual prepayments are large, spread them or show
     both views.
2. **Compute runway two ways, and give both current pace and plan.**
   - With TOPY: report `runway_months_current` (cash ÷ 3-month average net burn) and `runway_months_scenario`
     (on the plan's hiring and revenue) side by side; never only one. If they differ by more than 3 months,
     say which plan assumption causes it (from `assumptions_broken`).
   - Trailing: `runway (months) = cash ÷ average net burn (last 3 months)`.
   - Forward: month-by-month cash projection with planned hires and expected revenue; the zero-cash month is
     where cash first goes below zero. Always report the forward figure; the trailing one is a sanity check.
   - Add committed money only in the month it is expected to arrive, and only if contractually committed.
3. **Run the default-alive check.** Hold costs at plan, grow revenue at the expected rate, and find whether
   revenue covers costs before cash runs out.
   `month revenue covers costs: t = ln(costs ÷ revenue today) ÷ ln(1 + monthly growth)`;
   `cash low point = cash − Σ (costs − revenue_t)` over the months until then.
   Worked example: cash 600k, costs 80k/month flat, revenue 30k growing 8% a month.
   - t = ln(80 ÷ 30) ÷ ln(1.08) = 0.981 ÷ 0.0770 = 12.7 → revenue first exceeds costs in month 13.
   - Revenue over months 1-12 = 30k × 1.08 × (1.08¹² − 1) ÷ 0.08 = 30k × 20.50 ≈ 615k; costs = 960k.
   - Cumulative burn ≈ 345k → cash low point ≈ 255k. **Default alive**, with about 3 months of costs spare.
   Same company at 5% growth: t = 0.981 ÷ 0.0488 = 20.1 → month 21; revenue months 1-20 ≈ 30k × 34.72 ≈
   1,042k; costs 1,600k; burn ≈ 558k → low point ≈ 42k. Technically alive, practically not: one bad month
   kills it. Show both, and the growth rate at which the low point hits the founder's cash floor.
4. **Read the runway** (rules of thumb, adjust for how long fundraising takes in the founder's market):
   | Runway (forward) | Status | Action |
   |---|---|---|
   | 18+ months | comfortable | invest in growth; review monthly |
   | 12-18 months | plan | prepare the raise or the path to break-even now |
   | 6-12 months | act | raise now and pre-agree the cut plan; trigger tier 1 if no term sheet by a date |
   | under 6 months | emergency | execute cuts now; bridge from existing investors; talk to creditors early |
5. **List the levers with their arithmetic.** `new runway = cash ÷ (net burn − monthly saving)`.
   | Lever | Monthly saving | Runway gain | Reversible? | Time to effect | Side effect |
   |---|---|---|---|---|---|
   | Collect annual upfront (discount) | cash timing | +x months | yes | 1-3 months | lower revenue per customer |
   | Cut non-people spend (tools, agencies, travel) | | | yes | 1 month | small |
   | Pause unstarted hires | | | yes | immediate | slower roadmap |
   | Pause paid acquisition with payback > N months | | | yes | immediate | slower growth |
   | Reduce contractors | | | partly | 1-2 months | capacity loss |
   | Founder / leadership pay cuts | | | yes | immediate | morale, personal finances |
   | Reduce team | | | no | 1-3 months (notice, consultation) | morale, severance cost |
   | Non-dilutive money (grants, tax credits, revenue-based finance) | cash in | | n/a | weeks to months | conditions |
   Example: net burn 50k, cash 400k → 8.0 months; cutting 10k a month → 400 ÷ 40 = 10.0 months (+2.0).
6. **Write the tiered cut plan.** Each tier: trigger (observable, dated), actions, saving, new runway.
   - Tier 1 (e.g. "no lead investor by <date>"): non-people spend, paused hires, paid channels with long
     payback. Reversible.
   - Tier 2 (e.g. "cash below <x> months on <date>"): contractors, leadership pay, slower roadmap.
   - Tier 3 (e.g. "cash below the floor"): team reduction to reach default alive. Rule of thumb: cut once
     and deep enough to reach default alive, rather than in repeated small rounds that drain morale.
   Protect, in every tier: the revenue engine that works, retention of existing customers, and legal/tax
   payments (payroll taxes, VAT) that cannot be deferred without consequences.
7. **Stress the timing.** Re-run the forward projection with the raise 3 and 6 months late and revenue 20%
   below plan. Report the zero-cash month in each and which tier would fire when.
8. **Record the decision.** This skill only reads TOPY. Missing actuals are recorded through `topy-monthly-close`
   (each value with its `source`); a big plan gap goes to `topy-plan-vs-actual`. The cut plan is a decision: hand it to `topy-decision-memo` for the options and
   trade-offs, and update the model in `topy-financial-model`. If plan figures change, `topy-plan-revision`.

## Output
```
Runway review: <company> · cash as of <date> · prepared <date>
Burn (3-mo avg, one-offs removed): gross <x>/mo · net <y>/mo
Runway: current pace <a> months · on plan <b> months · zero-cash month <month> (source: <runway_get / founder>)
Default alive? yes/no · break-even month <m> · cash low point <z> · growth needed to stay above floor <g%>
Status: comfortable / plan / act / emergency
Levers: lever | saving | runway gain | reversible | time | side effect
Cut plan: tier | trigger (dated) | actions | saving | runway after
Stress test: scenario | zero-cash month | tier that fires
```

## Quality bar
- Burn is on cash, with one-offs removed and committed money only when contractually certain.
- Runway is forward-looking and gives a month, not just a number of months.
- The default-alive check shows its arithmetic and the cash low point.
- Every cut tier has a dated, observable trigger and a computed saving.
- The stress test includes a late raise.
- With TOPY: both current-pace and plan runway shown, every figure with its source and date.

## Guardrails
- Never invent cash, revenue or cost figures; label growth rates and savings as assumptions. With TOPY, cash and
  burn come only from CFO-sourced values (`runway_get` sources or KPI values with a `source`); founder-given
  figures are labelled "source: founder".
- Read-only in TOPY: no writes from this skill; recording actuals happens in `topy-monthly-close` with a
  preview and the founder's yes.
- Not legal, tax or accounting advice. Redundancies need an employment lawyer (consultation and notice rules
  vary by country); deferring tax or supplier payments, director duties when insolvency is possible (e.g.
  wrongful trading in the UK) and creditor negotiations need a lawyer or accountant. Flag these early.
- People decisions are described by role and cost, never by named individuals in shared outputs.
- Do not recommend hiding the cash position from the board or investors; bad news travels best early.

## Related skills
- `topy-monthly-close` — record the month's actuals that feed `runway_get`.
- `topy-plan-vs-actual` — why burn or revenue drifted from the plan.
- `topy-financial-model` — the full monthly model behind the forward runway.
- `topy-fundraising-strategy` — the raise and its latest safe start date.
- `topy-unit-economics` — which growth spend pays back fast enough to keep.
- `topy-hiring-plan` — the hires that pause in tier 1.
- `topy-decision-memo` — write the cut decision with options and trade-offs.
