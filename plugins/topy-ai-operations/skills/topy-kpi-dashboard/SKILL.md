---
name: topy-kpi-dashboard
description: Choose the north-star metric, the input metrics that drive it and the guardrails, and turn them into a weekly scorecard with owners, targets and red/amber/green rules. Use when the user says things like "what should our north star metric be?"; "we track 40 metrics and none of them help"; "build a weekly scorecard for the leadership meeting"; "which KPIs matter at our stage?"; "set up a KPI dashboard for the board"; "how do I know if we're on track each week?".
license: MIT
metadata:
  category: operations
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-kpi-dashboard/SKILL.md
---
# KPI dashboard

Gives a company one page that says, every week, whether it is on track and where to look if not. It picks
a north-star metric that captures the value customers get and the business captures, breaks it into the
input metrics teams can move, adds guardrails so the inputs are not gamed, and turns all of it into a
scorecard with owners, targets and plain rules for red, amber and green.

## When to use
- Choosing a north star, cleaning up a sprawling dashboard, starting a weekly scorecard, preparing board metrics.
- Not for: setting quarterly goals (use `topy-okrs`); calculating CAC, LTV or payback in depth (use
  `topy-unit-economics`); designing the meeting that reads the scorecard (use `topy-operating-cadence`).

## Before you start
- Ask one question at a time: business model; the main goal for the next 6-12 months; metrics tracked today
  and the system each comes from; who owns which function.
- Ask for numbers only if the founder wants targets set now; the structure can be designed without them.
- This skill does not read or save TOPY data. To track experiments on an input metric, use
  `topy-growth-experiments`.

## Workflow
1. **Pick the north star.** Shortlist 2-3 candidates and test each against five questions:
   - Does it go up only when customers get real value? (Revenue alone can rise while customers churn.)
   - Does it lead revenue rather than lag it by a year?
   - Can it be measured weekly from data the company has?
   - Can most teams see how their work moves it?
   - Is it hard to inflate without helping the business?
   Typical shapes by model (examples, not prescriptions): subscription software → weekly active accounts
   doing the core action, or net new recurring revenue; marketplace → completed transactions where both
   sides return; usage-based → units of core usage by retained customers; services → billable delivered
   work at target margin. Choose one; record why the runner-up lost.
2. **Build the metric tree.** Break the north star into its drivers as a formula where possible, e.g.
   active accounts = new activated accounts + retained accounts - churned accounts; new activated =
   sign-ups × activation rate. Keep 3-6 **input metrics**: each moves within weeks, one team can own it, and
   it has a clear link to the north star.
3. **Add guardrails.** 2-3 metrics that must not get worse while chasing the inputs: gross margin, refund or
   churn rate, support response time, cash burn, quality defects. A guardrail has a floor, not a target.
4. **Separate decision metrics from reporting metrics.** The scorecard holds only metrics someone would act
   on if they changed. Everything else (page views, followers, total sign-ups since launch) moves to an
   appendix or is dropped.
5. **Define every metric** in the definitions sheet: exact formula, inclusions and exclusions, data source,
   time window, refresh time, owner. Two people computing it should get the same number.
6. **Set targets and status rules.** Targets come from the plan, the OKRs or the founder, never invented here.
   Default status rules (adjust per metric):
   - Green: at or above target (or above the guardrail floor).
   - Amber: below target but within a tolerance agreed in advance (e.g. within 10% of target).
   - Red: outside tolerance, or amber three weeks running.
   Use the last 4-8 weeks' trend next to the weekly value so one noisy week does not trigger a panic.
7. **Attach owners and actions.** Each line has one owner. Rule: a red line gets a cause and a next step at
   the weekly meeting; red two weeks in a row gets a named plan with a date.
8. **Lay out the scorecard.** North star on top, inputs next, guardrails last; at most 10-15 lines. Leading
   metrics left of lagging ones in any chart. Weekly columns for the last 8-13 weeks.
9. **Plan the build.** For each metric: where the data lives, who pulls it, manual or automated, by what
   weekday. Start with a spreadsheet filled manually for four weeks before automating; definitions settle first.
10. **Review quarterly.** Drop metrics no one acted on all quarter; revisit the north star only when the
    strategy changes.

## Output
```
KPI dashboard: <company> · <model> · <date>
North star: <name> = <formula> · why: <reason> · runner-up: <name>, rejected because <reason>
Metric tree: <north star> ← <input 1> × <input 2> ... (formula where possible)
Weekly scorecard
| Metric | Type (north star/input/guardrail) | Owner | Target or floor | Tolerance | W-3 | W-2 | W-1 | This week | Status | Note |
Definitions
| Metric | Formula | Includes/excludes | Source | Window | Refreshed | Owner |
Status rules: green/amber/red as defined; red ×2 → plan with date
Build plan: | Metric | Data source | Manual/auto | Who | Due weekday |
Dropped or moved to appendix: <list>
```

## Quality bar
- The north star passes all five tests or the failed one is named with its mitigation.
- Every input metric links to the north star by formula or a stated mechanism.
- At least two guardrails exist, each with a floor.
- Every line has one owner, a definition and a data source; 15 lines at most.
- No target was invented; each has its source (plan, OKR, founder).
- Status rules are written down before the first week, not after.

## Guardrails
- Never invent benchmarks or "industry average" figures; if the founder wants comparisons, ask for a named
  source they trust and label it.
- Present the model examples and tolerances as rules of thumb, not standards.
- Revenue recognition and financial definitions for statutory accounts are an accountant's call; the
  scorecard's management metrics should say they are not audited figures.
- Do not put individual employees' personal performance data on a company-wide scorecard.

## Related skills
- `topy-operating-cadence` — the weekly forum that reads the scorecard.
- `topy-okrs` — quarterly goals that set targets for input metrics.
- `topy-unit-economics` — the economics behind guardrails such as payback and margin.
- `topy-board-meetings` — the board version of the scorecard.
- `topy-growth-experiments` — experiments aimed at a lagging input metric.
