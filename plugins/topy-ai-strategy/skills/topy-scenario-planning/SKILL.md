---
name: topy-scenario-planning
description: Builds a small set of plausible futures around the uncertainties that matter most, tests the company's plans against each, and sets early-warning signals with responses agreed in advance; with TOPY, each scenario is saved as a financial scenario. Use when the user says things like "what if the market turns?"; "plan for different scenarios"; "we don't know if the funding market will recover"; "what's our plan B?"; "stress-test our strategy"; "how do we plan when everything is uncertain?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-scenario-planning/SKILL.md
---
# Scenario planning

Helps a founder plan when the future depends on things nobody can predict. Instead of one forecast, the agent builds a few plausible futures around the two uncertainties that matter most, checks how each option holds up in every one, and sets the signals that show which future is arriving, with responses agreed before they are needed. The method works with any agent and needs no account; with TOPY connected, each scenario is saved as a financial scenario so actuals can later be compared against it, and the triggers become alert rules.

## When to use
- A big commitment (a hire plan, a long lease, a new market, a raise) depends on factors outside the founder's control.
- The external environment is shifting: funding conditions, a platform policy, regulation, a key supplier, a large customer's budget.
- The founder asks "what's plan B?", or the board asks for a downside case.
- Not for: a choice where the main unknowns are inside the company (use `topy-decision-memo`), a single cash-runway calculation (use `topy-runway`), or tracking individual risks over time (use `topy-risk-register`).

## Before you start
- Ask one question at a time:
  1. "What decision or plan are we stress-testing?"
  2. "Over what time horizon?" For most startups, the runway or the next 12-24 months is right; longer horizons rarely change today's actions.
  3. "What keeps you up at night about it?" Collect the founder's worries as raw material.
  4. "What are cash in the bank, monthly net burn and monthly revenue today?"
- If the founder uses TOPY, take current cash, burn and revenue from `topy-runway` (CFO-sourced, with `source`) rather than asking, and read the risk register via `topy-risk-register`. Without TOPY, ask.

## Workflow
1. **Write the focal question.** "Over [horizon], how should we [decision] given we cannot know [uncertainties]?" Keep it tied to a choice the founder must make.
2. **List the driving forces.** Walk through: customers and demand, competitors, technology, regulation and policy, capital markets and funding, costs and suppliers, the wider economy, the team. Aim for ten to twenty forces.
3. **Split them.** *Predetermined*: forces whose direction is fairly clear (an announced regulation, a contract end date); these appear in every scenario. *Critical uncertainties*: forces that could go either way and would change the answer.
4. **Pick two uncertainties.** Score each critical uncertainty 1-5 on impact on the focal question and 1-5 on how unpredictable it is. Take the two highest that are independent: one could be high while the other is low. If two candidates move together (e.g. "funding market" and "investor appetite for our sector"), merge them.
   - If one uncertainty clearly dominates, skip the grid and build three variants of it (low, middle, high) instead.
5. **Define the poles.** For each chosen uncertainty, write two end states specific enough to observe ("seed rounds take 6+ months to close" vs "rounds close within 8 weeks"), not "good" and "bad".
6. **Build the four worlds.** Cross the two uncertainties to get four scenarios. For each write:
   - A memorable name.
   - A five-line story of how we got there from today.
   - What it means for revenue, costs, hiring and fundraising.
   Each scenario must be plausible and internally consistent. Avoid labelling them best, base and worst: that invites the team to plan only for the middle. If one quadrant is implausible, say so and work with three.
7. **Put rough numbers on each.** Use the founder's figures. For each scenario estimate a range for monthly revenue and net burn at the horizon. Runway in months = cash ÷ monthly net burn; compute it per scenario. Use ranges and round numbers; precise figures here are false comfort. Avoid attaching exact probabilities; if the founder wants a weighting, use "more likely / less likely" and say what it is based on.
8. **Test the options.** Build a matrix: rows are the options or current strategy, columns are scenarios, cells are works / survives / fails, with one line why. Then sort every move:
   | Type | Pattern | What to do |
   |---|---|---|
   | No-regret | works or survives in every scenario | do it now |
   | Hedge / option | cheap now, keeps a choice open | buy it if the cost is small |
   | Bet | great in one or two, poor elsewhere | stage it, tie it to a signal |
   | Fatal exposure | fails badly in any plausible scenario | fix or remove first |
   A fatal exposure (for example, running out of cash before a planned raise could close in a slow-funding world) outranks every upside.
9. **Choose early indicators.** For each scenario, two or three observable signals that it is arriving, chosen because they move before the outcome does. Each signal names the source, the threshold and how often to check it ("time from first investor meeting to term sheet in our own process, over 10 weeks for two consecutive raises we hear about, checked monthly").
10. **Agree responses in advance.** For each likely trigger write: if [signal crosses threshold] by [date], then [action], owned by [person], costing [budget]. Example shape: "If net new revenue is below [X] for two consecutive months, freeze the next two hires and extend runway by [N] months." Agreeing now removes delay and status-quo bias when the moment comes.
11. **Save the scenarios in TOPY (connected, with a yes).** For each scenario, `financial_scenario_create` with `name` (the scenario's name, or `conservative` / `optimistic` where it fits), `currency`, `assumptions` (the poles of the two uncertainties and the drivers they change: growth, price, churn, hiring timetable, raise timing), and `notes` ("a scenario, not a forecast"; the story). Then `financial_projections_upsert` with monthly rows `{period_date, metric_name, metric_value, metadata_json}` for `revenue_monthly`, `net_burn` and `cash_balance` (KPI keys), using the mid-point of each range and the range in `metadata_json` (`{"low": …, "high": …, "origin": {"type": "agent"}}`). Never write over the `plan` or `current` scenario. Each write is a preview first; confirm after the founder agrees.
12. **Turn KPI-based triggers into alert rules.** Where a trigger is a KPI crossing a threshold (net new revenue, `runway_months`, `churn_rate_monthly`), hand it to `topy-alerts` to create the rule (KPI, threshold, direction, severity), so the signal is watched rather than remembered. Triggers that are not KPIs (a competitor's move, a regulation) go to the risk register.
13. **Set the review rhythm.** Check indicators monthly; redo the scenarios every six months or when a trigger fires or a predetermined force changes.
14. **Record it.** If the founder uses TOPY, suggest logging each fatal exposure and major trigger in the risk register (`topy-risk-register`) and the pre-agreed responses as decisions (`topy-decision-log`), so they are reviewed rather than forgotten.

## Output
1. Focal question, horizon, and the predetermined forces.
2. Uncertainty ranking table (force | impact | unpredictability | chosen?).
3. The scenario grid: the two axes, four named scenarios, each with story, implications and rough numbers (revenue range, burn range, runway).
4. Options × scenarios matrix and the four-way sort (no-regret, hedges, bets, fatal exposures).
5. Indicators table: scenario | signal | source | threshold | check frequency.
6. Trigger → response table: trigger | action | owner | budget.
7. Review dates.

## Quality bar
- The two axes are genuinely independent and specific enough to observe.
- Each scenario is plausible, consistent and named; none is just "worst case".
- Numbers come from the founder and are shown as ranges; runway is computed per scenario.
- At least one no-regret move is identified, and every fatal exposure has a fix or an owner.
- Every indicator moves before the outcome and has a threshold and a source.
- Every response is specific, owned, budgeted and agreed by the founder.

## Guardrails
- Scenarios are tools for thinking, not forecasts; say so in the output and never present one as the expected outcome.
- Never invent market statistics, macro forecasts or sources; when using a general pattern (for example that fundraising slows in downturns) present it as a rule of thumb, not data.
- Not legal, tax or investment advice. Responses involving layoffs, contract exits, debt or regulatory exposure should be checked with a lawyer or accountant before they are triggered.
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Current figures come only from tools with a `source` or from the founder (labelled "source: founder"); scenario projections are labelled scenarios, never actuals.
- Keep plans that involve people (hiring freezes, cuts) confidential to the founder until they choose to share them.

## Related skills
- `topy-decision-memo` — take a no-regret move or a bet and decide it properly.
- `topy-risk-register` — track fatal exposures and triggers over time.
- `topy-runway` — the detailed burn and runway work behind each scenario's numbers.
- `topy-debiasing` — a pre-mortem when the founder is anchored on one future.
- `topy-financial-model` — the full driver model behind a scenario.
- `topy-alerts` — watch the KPI triggers automatically.
- `topy-competitive-strategy` — when the critical uncertainty is a competitor's behaviour.
