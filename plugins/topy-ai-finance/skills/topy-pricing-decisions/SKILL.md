---
name: topy-pricing-decisions
description: 'Make the CEO-level pricing call: what to charge for, how to package it, whether to raise or cut prices, the break-even maths for each option, and a test plan saved as a decision and an experiment. Use when the user says things like "should we raise our prices?"; "are we charging for the right thing?"; "per seat, usage or flat fee?"; "a big customer wants a 30% discount, should we give it?"; "how many customers can we lose if we put prices up?"; "should we add a cheaper plan?". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: finance
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-pricing-decisions/SKILL.md
---
# Pricing decisions

Pricing is one of the fastest levers a CEO has on margin and runway, and one of the easiest to get wrong by
instinct. This skill frames the pricing question as a decision with options (including leaving prices as
they are), computes what each option needs to be true to pay off, picks the value metric and packaging,
and turns the choice into a controlled test with rules agreed in advance. With TOPY connected, the decision
is saved to the decision log and the test to the growth experiments board. Page design and pricing-page
copy belong to the marketing team's tools, not here.

## When to use
- "Raise prices?", "discount?", "right value metric?", "new plan?", "test a price".
- When margins or unit economics are weak, when moving up- or down-market, or before a raise.
- Not for: diagnosing CAC/LTV first (use `topy-unit-economics`); a general decision write-up on another
  topic (use `topy-decision-memo`); running non-pricing growth tests (use `topy-growth-experiments`).

## Before you start
- Ask one question at a time: current plans and prices; mix of customers and revenue per plan; margin;
  churn and conversion; the goal; what customers compare against and its cost.
- Ask for the last 10-20 pricing reactions in customers' own words (won, lost, churned, negotiated).
- With TOPY connected, nothing needs reading first; the skill writes at the end with `decision_create` and
  `growth_experiment_create`. Without TOPY, the same outputs are returned as text.
- Never ask for payment-processor logins; plan and revenue totals are enough.

## Workflow
1. **State the decision and the options.** One sentence ("Raise the Team plan from 49 to 59 for new
   customers?") and 3-4 options, always including do-nothing (e.g. raise for all; raise for new only;
   add a higher tier instead; keep price, change the metric).
2. **Check the value metric before the number.** A good metric grows with the value the customer gets, is
   predictable for them, and is hard to game. Options: per seat, per active unit (location, project,
   vehicle), usage/credits, transactions, outcome-based, flat. Mismatch signs: one customer gets 10× the
   value of another at the same price; customers share logins to avoid seats; bills swing unpredictably.
3. **Anchor on value and alternatives.** `customer's next-best alternative cost < your price < value to the
   customer`. Estimate value with the customer's own numbers (hours saved × their hourly cost, revenue
   gained, cost avoided). Competitors' prices are a data point, not a target. Never invent willingness-to-pay
   figures; label estimates.
4. **Compute the break-even for each option.**
   - Revenue break-even of a price rise p (as a fraction): `share of customers that must stay = 1 ÷ (1 + p)`.
     +20% → 1 ÷ 1.2 = 83.3%: revenue is flat if no more than 16.7% leave because of the rise.
   - Gross-profit break-even (better): with contribution margin m, `break-even volume change = −p ÷ (m + p)`.
     m = 70%, +10% price → −0.10 ÷ 0.80 = −12.5%: profit holds if volume falls by less than 12.5%.
   - Discount d: `volume increase needed = d ÷ (m − d)`. m = 70%, 10% off → 0.10 ÷ 0.60 = +16.7% more volume
     just to stand still; 30% off → 0.30 ÷ 0.40 = +75%.
   | Option | Price change | Margin | Break-even volume change | Evidence it will hold |
   |---|---|---|---|---|
   | Raise for new customers | +20% | 70% | −22.2% | win/loss notes, comparison with alternatives |
   | 10% discount for annual | −10% | 70% | +16.7% (or cash-timing gain) | renewal rates |
   | Do nothing | 0 | 70% | — | current churn and conversion |
   (−0.20 ÷ 0.90 = −22.2%.)
5. **Read the signals** (rules of thumb, the company's own data wins): very high trial-to-paid or close rate
   with little negotiation suggests underpricing; most customers crowding into the cheapest plan suggests the
   next plan lacks a clear trigger; high churn should be fixed before a rise, since rises speed up churners.
6. **Decide packaging.** 2-4 plans; each higher plan has one named upgrade trigger (more seats or usage, a
   security or admin need, support level); the plan most customers should buy is designed first; features
   some customers refuse to pay for become add-ons. Enterprise "contact us" only when needs genuinely differ.
7. **Design the test.** Prefer, in order: new customers only (cohort split by signup date), a new plan offered
   alongside the old, a geography or segment test, sales-quoted price tests. Write before starting:
   hypothesis; metric (conversion, ARPA, gross profit per visitor or per lead); guardrails (churn, refunds,
   support tickets); sample or duration (until at least ~100 conversions per arm or 2 full sales cycles, as
   a rule of thumb); success rule; stop rule. Showing different prices to similar people can be restricted;
   check local consumer law.
8. **Plan the rollout to existing customers** if the test succeeds: notice period (check contracts and local
   law), the reason given, a path (lock the old price with annual prepay, or a grandfathering window with an
   end date), support FAQ, and a 60-day watch on churn and downgrades.
9. **Save it in TOPY (when connected).**
   - `decision_create`: title, options considered, the chosen option, break-even maths, what would reverse
     it, review date.
   - `growth_experiment_create`: hypothesis, metric, guardrails, success and stop rules, start and end dates.
   Each is two calls: first call returns a preview, shown to the user; second call with `confirm: true` and
   the `confirmation` only after they agree.
10. **Flow into the plan.** If the new price changes the plan's revenue, pricing or financial sections, list
    the figures and hand them to `topy-plan-revision`.

## Output
```
Pricing decision: <company> · <product/plan> · prepared <date>
Decision: <one sentence> · goal <x>
Options: option | price change | break-even volume change | evidence | risk
Recommendation: <option> · value metric <x> · packaging table: plan | for whom | price | trigger to upgrade
Test plan: hypothesis | metric | guardrails | sample/duration | success rule | stop rule | dates
Rollout (existing customers): notice | reason | path | watch metrics
Saved in TOPY: decision <id or "not saved"> · experiment <id or "not saved">
Plan figures affected: <list or "none">
```

## Quality bar
- Do-nothing is an option and has its own numbers.
- Every option shows the break-even maths with the margin used.
- The value metric is chosen before the price.
- Success and stop rules are written before the test starts.
- Existing customers get notice, a reason and a path.

## Guardrails
- Changes in TOPY take two calls: `decision_create` and `growth_experiment_create` each return a preview
  first, shown to the user; call again with `confirm: true` and the `confirmation` only after they agree.
  Never confirm for the user.
- Never invent willingness-to-pay data, competitor prices, customer quotes or benchmarks; label estimates.
- Not legal advice: price-change notice terms, consumer protection rules on price display and reference
  prices, and price discrimination rules vary by country; check with a lawyer for consumer products or
  regulated sectors.
- Never coordinate prices with competitors or use their non-public pricing.

## Related skills
- `topy-unit-economics` — the margin, churn and payback the break-even maths uses.
- `topy-decision-memo` — a fuller write-up when the pricing call is contested.
- `topy-growth-experiments` — run and close the price test.
- `topy-decision-log` — review the saved decision on its review date.
- `topy-plan-revision` — carry the new price through the saved plan.
