---
name: topy-financial-model
description: Build a driver-based, three-statement-lite startup model (revenue build, headcount, costs, P&L, cash flow, simple balance sheet) with an assumptions sheet, scenarios and checks. Use when the user says things like "build a financial model for my startup"; "I need 3-year projections for investors"; "turn my business plan numbers into a model"; "are my revenue projections realistic?"; "what happens to cash if we hire 4 people next quarter?"; "make a base, downside and upside case". Uses TOPY when it is connected.
license: MIT
metadata:
  category: finance
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-financial-model/SKILL.md
---
# Financial model

Builds the model a founder actually runs the company on: a few drivers on one assumptions sheet feed a
monthly revenue build, a headcount plan and costs, which roll into a P&L, a cash flow and a simple balance
sheet. Change a driver and everything moves. The model is honest about what is known (actuals), what is
believed (assumptions with sources) and what is hoped (upside case). With TOPY connected it starts from the
business plan's financial section and flags where model and plan disagree.

## When to use
- "Financial model", "projections", "3-year forecast", "do our numbers add up", "base/downside case".
- Before a raise (the model backs the deck and the ask), before a big hiring decision, or yearly budgeting.
- Not for: a quick runway check (use `topy-runway`); deep CAC/LTV diagnosis (use `topy-unit-economics`);
  changing figures in the saved plan (use `topy-plan-revision`).

## Before you start
- Ask one question at a time: how the company makes money; actuals available; the 3-5 drivers the founder
  thinks matter; current team and hires planned; cash and committed funding; the model's purpose (raise,
  budget, decision).
- With TOPY connected, read first: `plans_list` to find the current plan, then `plan_get` to read the
  financial projections, pricing, team, milestones and funding requirement. Record the plan's headline
  figures (revenue by year, headcount, burn, raise) to compare against at the end.
- Without TOPY, ask for the latest projections, deck numbers or bookkeeping export.
- Never ask for bank or accounting-system logins; exports and totals are enough.

## Workflow
1. **Lay out the tabs.** Assumptions → Revenue build → Headcount → Costs → P&L → Cash flow → Balance
   sheet-lite → Scenarios → Checks. Inputs live only on Assumptions (one colour); every other cell is a
   formula. Monthly columns for 24 months, then annual to year 3 (or 5 if investors ask).
2. **Write the assumptions sheet.** Columns: driver | value | unit | source | confidence (actual / evidence
   / assumption) | owner. Typical drivers: new customers or leads per month, conversion rates, price/ARPA,
   churn, expansion, payment terms, gross-margin costs per unit, salaries and start months, employer
   on-costs (ask the accountant for the local rate), rent and tools, marketing spend, tax and VAT timing.
3. **Build revenue from drivers, never from a growth % alone.** Pick the build that matches the model:
   | Model | Revenue build |
   |---|---|
   | Subscription (B2B/B2C) | customers_t = customers_t−1 + new_t − churned_t; MRR = customers × ARPA (+ expansion) |
   | Sales-led B2B | new deals = reps ramped × quota attainment ÷ average deal size; or pipeline × win rate |
   | Marketplace | GMV = orders × AOV; revenue = GMV × take rate |
   | E-commerce / D2C | orders = traffic × conversion (+ repeat orders); revenue = orders × AOV − returns |
   | Usage / API | active accounts × usage per account × price per unit |
   Worked example (subscription, 3% monthly churn, ARPA 100):
   | Month | Opening | New | Churned (3%) | Closing | MRR |
   |---|---|---|---|---|---|
   | 1 | 200 | 20 | 6 | 214 | 21,400 |
   | 2 | 214 | 22 | 6 | 230 | 23,000 |
   | 3 | 230 | 24 | 7 | 247 | 24,700 |
   Where new customers come from marketing, tie them to spend: `new = spend ÷ CAC` (CAC from
   `topy-unit-economics`), so cutting spend cuts growth in the model too.
4. **Build headcount.** One row per role: start month, salary, on-cost %, equipment. `monthly cost = salary
   ÷ 12 × (1 + on-cost %)`. Sales roles get a ramp (e.g. 0% / 50% / 100% quota over their first 3 months; an
   assumption to label). Take roles from `topy-hiring-plan` if one exists.
5. **Build costs.** Cost of revenue (hosting, payment fees, third-party/API or AI inference costs, support,
   delivery) scales with volume; operating costs (people, marketing, tools, rent, professional fees) are
   stepped or fixed. `gross margin % = (revenue − cost of revenue) ÷ revenue`.
6. **Roll up the P&L.** Revenue − cost of revenue = gross profit − operating costs = EBITDA − depreciation
   − interest − tax = net income. Keep it to about 15-25 lines.
7. **Turn profit into cash.** Cash ≠ profit. Adjust for: annual prepayments (cash in month 1, revenue
   spread over 12), customer payment terms (`receivables = revenue × days to pay ÷ 30`), supplier terms,
   VAT/sales tax collected and paid on a schedule, capex, tax credits received later (UK: R&D relief lands
   months after the year end; model it in the month expected, as an assumption), equity and debt raised.
   `closing cash = opening cash + operating cash flow + investing cash flow + financing cash flow`.
8. **Balance sheet-lite.** Cash, receivables, fixed assets; payables, deferred revenue, debt; equity. It is
   there to prove the model is internally consistent, not to impress.
9. **Scenarios and sensitivity.** Flex only the 3-5 drivers that matter: base (best evidence), downside
   (e.g. new customers −30%, churn +50%, raise 3 months late), upside (only with evidence). Run a
   sensitivity: which single driver moves month-18 cash most for a ±20% change? That driver gets the
   founder's attention and a validation test.
10. **Run the checks.** Balance sheet balances every month; cash never goes negative without a flag; sum of
    segments = total; no hard-coded numbers outside Assumptions; month-over-month growth, gross margin and
    revenue per employee compared with the company's own actuals (and benchmarks only if the founder cites a
    source); headcount × salary matches the people-cost line.
11. **Compare with the saved plan.** List each headline figure: plan vs model, difference, reason. If the
    plan must change (a revenue line, the raise, headcount), hand the list to `topy-plan-revision`, which
    previews the change across every section before anything is applied.

## Output
```
Model: <company> · <currency> · prepared <date> · actuals to <month>
Assumptions: driver | value | unit | source | confidence | owner
Summary (annual): revenue | gross margin % | opex | EBITDA | net burn | closing cash | headcount
Monthly (24 months): revenue build, headcount, P&L, cash flow (as tabs or tables)
Scenarios: scenario | changed drivers | month-18 cash | zero-cash month | revenue year 2
Top sensitivity: driver | ±20% effect on month-18 cash
Checks: list with pass/fail
Plan vs model: figure | plan | model | difference | reason
```

## Quality bar
- Every input sits on the assumptions sheet with a source and confidence label.
- Revenue is built from drivers; growth is never just a typed percentage.
- Cash flow differs from profit wherever timing differs, and shows the zero-cash month in each scenario.
- The checks pass, and the balance sheet balances.
- Differences from the saved plan are listed, not silently overwritten.

## Guardrails
- The skill only reads TOPY. Changes to plan figures go through `topy-plan-revision`, which takes two calls:
  a preview shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never
  confirm for the user.
- Never invent actuals, benchmarks, market data or customer numbers; projections are labelled projections.
- Not tax or accounting advice: tax, VAT, payroll on-costs, R&D credits and revenue recognition need the
  company's accountant.
- Do not present the upside case as the plan; investors and the founder should see base and downside.

## Related skills
- `topy-runway` — burn, zero-cash date and the cut plan from this model.
- `topy-unit-economics` — CAC, LTV and payback that drive the revenue build.
- `topy-hiring-plan` — the headcount tab.
- `topy-plan-revision` — carry changed figures through the saved plan.
- `topy-fundraising-strategy` — the raise the model must fund.
