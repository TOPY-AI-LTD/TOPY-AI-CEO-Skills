---
name: topy-unit-economics
description: 'Work out what one customer is worth and costs to win: CAC, contribution margin, LTV, payback, net revenue retention and cohorts, then name the one thing to fix first. Use when the user says things like "what''s our CAC and LTV?"; "are our unit economics good enough to scale?"; "how long does it take to pay back a customer?"; "investors asked for our LTV to CAC ratio"; "should we spend more on ads?"; "read our cohort retention".'
license: MIT
metadata:
  category: finance
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-finance/skills/topy-unit-economics/SKILL.md
---
# Unit economics

Answers the question behind "should we grow faster?": does each customer bring in more than they cost to
win and serve, and how quickly does the money come back? The skill computes the core ratios with the
working shown, reads retention by cohort rather than by average, and turns the result into one priority:
fix margin, fix retention, fix acquisition cost, or scale. Rules of thumb are given as such; the company's
own trend matters more than any benchmark.

## When to use
- "CAC", "LTV", "payback", "LTV:CAC", "cohorts", "should we spend more on growth".
- Before raising spend, before a raise (investors will ask), or when growth is costing more than expected.
- Not for: the full company model (use `topy-financial-model`); changing price or packaging (use
  `topy-pricing-decisions`); running the experiments that test a fix (use `topy-growth-experiments`).

## Before you start
- Ask one question at a time: billing model and ARPA; what goes into cost of revenue; sales and marketing
  spend by month including people; new customers by month; churn and expansion, or cohort data.
- Ask the segment: unit economics for a self-serve SMB product and an enterprise contract should never be
  blended into one number.
- No TOPY tools are needed. Never ask for payment-processor or bank logins; exports are enough.

## Workflow
1. **Define the unit and the period.** Unit = customer (account), not user, unless the company bills per
   user. Use monthly figures; annual contracts are converted to monthly. Segment by plan, channel or customer
   size where they differ.
2. **Compute margin per customer.**
   - `ARPA = revenue in month ÷ paying customers`.
   - `gross margin % = (revenue − cost of revenue) ÷ revenue`. Include hosting, payment fees, support and
     onboarding labour, third-party APIs and AI inference; leaving them out flatters every later ratio.
   - `gross profit per customer per month = ARPA × gross margin %`.
3. **Compute CAC.**
   - `blended CAC = (sales + marketing spend, incl. salaries and tools) ÷ new customers` for the same period.
   - `paid CAC = paid media spend ÷ customers attributed to paid` (shows whether paid channels work).
   - Lag: if the sales cycle is ~2 months, divide this month's new customers into spend from 2 months ago.
   - Early on, founder-led sales has a hidden cost: put a notional cost on founder time, labelled.
4. **Compute payback, LTV and the ratio.**
   - `CAC payback (months) = CAC ÷ gross profit per customer per month`.
   - `LTV = gross profit per customer per month ÷ monthly customer churn` (cap lifetime at e.g. 36-60
     months; with little history, churn estimates are fragile, so state the cap).
   - With expansion, a revenue-based version: `LTV ≈ ARPA × GM% ÷ (revenue churn − expansion rate)` only
     while revenue churn exceeds expansion; otherwise use the capped lifetime.
   - `NRR = (starting MRR + expansion − contraction − churned MRR) ÷ starting MRR` for a cohort over 12
     months.
5. **Worked example.** ARPA 80, gross margin 75%, monthly churn 4%, blended CAC 600.
   | Metric | Working | Result |
   |---|---|---|
   | Gross profit / customer / month | 80 × 0.75 | 60 |
   | CAC payback | 600 ÷ 60 | 10 months |
   | Average lifetime | 1 ÷ 0.04 | 25 months |
   | LTV | 60 ÷ 0.04 | 1,500 |
   | LTV:CAC | 1,500 ÷ 600 | 2.5 |
6. **Read against rules of thumb** (common in subscription businesses; not law, and they differ by segment):
   LTV:CAC of about 3 or more; CAC payback under about 12 months for self-serve/SMB, longer tolerated for
   enterprise with low churn; software gross margin of roughly 70%+ (services-heavy and hardware lower);
   NRR above 100% means the installed base grows without new customers. Compare first with the company's own
   trend: improving from 1.8 to 2.5 matters more than missing 3.
7. **Read the cohorts.** Build a table: signup month × months since signup, % of customers (or revenue)
   still active. Illustrative shape:
   | Cohort | M0 | M1 | M3 | M6 | M9 |
   |---|---|---|---|---|---|
   | Jan | 100% | 82% | 68% | 61% | 59% |
   | Apr | 100% | 85% | 72% | 66% | — |
   | Jul | 100% | 88% | 76% | — | — |
   A curve that flattens (Jan levels off near 60%) means a retained core; a curve that keeps sliding to zero
   means retention is the problem, whatever the averages say. Newer cohorts retaining better = product or
   onboarding improvements are working.
8. **Run the lever table.** Change one lever at a time against the example:
   | Lever | Change | Payback | LTV | LTV:CAC |
   |---|---|---|---|---|
   | Churn | 4% → 3% | 10.0 | 2,000 | 3.3 |
   | Price (no churn change) | ARPA +10% → 88 | 9.1 | 1,650 | 2.75 |
   | CAC | −20% → 480 | 8.0 | 1,500 | 3.1 |
   | Gross margin | 75% → 80% | 9.4 | 1,600 | 2.7 |
9. **Pick what to fix first** with this order:
   1. Gross margin below ~50% on a software product → fix cost to serve or price before anything else.
   2. Cohort curves never flatten → fix retention/activation; do not scale acquisition into a leaky bucket.
   3. Payback above the threshold for the segment → fix CAC (channel mix, conversion) or price.
   4. All three healthy and improving → scale spend in steps, re-measuring CAC at each step (CAC usually
      rises as cheaper channels saturate).
   State the one fix, the metric that would prove it, and hand price changes to `topy-pricing-decisions`
   and tests to `topy-growth-experiments`.
10. **Burn efficiency** (company level, optional): `burn multiple = net burn ÷ net new ARR` in the same
    period; lower is better, and a rising trend is a warning even when growth looks fine.

## Output
```
Unit economics: <company> · segment <x> · period <months> · prepared <date>
| Metric | Formula | Inputs | Result | Trend (last 3-6 months) |
Cohort table + one-line reading (flattening? newer cohorts better?)
Lever table: lever | change | payback | LTV | LTV:CAC
Fix first: <one fix> · proof metric <x> · target <y> by <date> · hand-off <skill>
Assumptions and gaps: <list, labelled>
```

## Quality bar
- Every ratio shows its formula and inputs; cost of revenue includes support and third-party costs.
- Segments with different economics are not blended.
- CAC includes salaries and tools, and states the lag used.
- LTV states the lifetime cap; rules of thumb are labelled as such.
- The output ends with one fix, not a list of ten.

## Guardrails
- Never invent metrics, benchmarks or cohort data; illustrative tables are labelled illustrative.
- Do not present LTV as cash in the bank: it is a projection that depends on churn holding.
- Not accounting advice: revenue recognition and cost allocation questions go to the company's accountant.
- Customer-level data is personal or confidential: work with aggregates.

## Related skills
- `topy-pricing-decisions` — when the fix is price, packaging or the value metric.
- `topy-financial-model` — CAC and churn as drivers of the revenue build.
- `topy-runway` — what the growth spend does to burn and runway.
- `topy-growth-experiments` — test the chosen fix and track it.
