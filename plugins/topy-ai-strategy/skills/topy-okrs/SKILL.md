---
name: topy-okrs
description: Turns a startup's strategy into a small set of quarterly objectives and measurable key results, then scores them honestly at the end of the quarter and carries the lessons forward. Use when the user says things like "help me set OKRs for next quarter"; "turn our strategy into goals"; "are these good key results?"; "score our OKRs"; "what should the team aim for this quarter?"; "our goals are just a to-do list". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-okrs/SKILL.md
---
# OKRs

Helps a founder translate strategy into a quarter's worth of focus: a few objectives that say what matters, key results that prove it happened, and a fair way to score them. The skill has two modes: **set** (before the quarter) and **score** (at the end). With TOPY connected, it reads the business plan's milestones so the OKRs serve the plan, and saves the agreed set to project memory so it can be scored later.

## When to use
- Before a quarter starts, or after a funding round or pivot when goals need resetting.
- Existing goals read like task lists ("launch v2", "hire a designer") or nobody knows if they were hit.
- End of quarter: scoring, retro and deciding what carries over.
- Not for: ranking the initiatives that will deliver the OKRs (use `topy-prioritization`), designing the weekly metrics scorecard (use `topy-kpi-dashboard`), or long-range strategy itself (use `topy-decision-memo` or `topy-business-model`).

## Before you start
- Ask which mode: setting new OKRs, or scoring last quarter's.
- With TOPY connected:
  - If you do not know the project, call `projects_list` and ask which one; then `project_get` for stage, market and what the company does.
  - Call `plans_list`, then `plan_get` on the current plan, and pull its milestones, revenue targets and KPIs for the next 12 months. This quarter's OKRs should be a visible step towards them.
  - Call `memories_list` and look for an earlier OKR record (title like "OKRs Q2 2026"). Use it for scoring, or to see what carried over.
- Without TOPY, ask: the company's goal for the year, the stage, last quarter's goals and how they went.
- Then ask for baselines, one metric at a time. If a baseline is unknown, the first key result may be to measure it; say so rather than guessing.

## Workflow
### Set
1. **State the strategy in one sentence.** "This year we win by [approach] for [customer], measured by [outcome]." If the founder cannot say it, OKRs will be a wish list; resolve the strategy first.
2. **Choose one to three objectives.** For a team under about 20 people, one to three is plenty (rule of thumb); one is often best for a team under five. An objective is qualitative, says why it matters, fits a quarter and contains no number: "Make onboarding something customers rave about", not "Increase activation 20%".
3. **Write two to four key results per objective.** Each KR is an outcome that can be measured without debate:
   - Format: "[metric] from [baseline] to [target] by [date]".
   - Owner: one person. Data source: where the number is read.
   - Activities are not KRs. "Launch the referral programme" is a task; "referrals from 5 to 25 new customers a month" is a KR. Allow at most one milestone KR per objective, for genuine one-off outcomes (e.g. "regulatory approval received").
   - Completeness test: if every KR is hit, is the objective clearly achieved? If not, a KR is missing. Necessity test: if one KR is removed, is anything lost? If not, remove it.
4. **Label each KR committed or aspirational.** Committed means the team expects to deliver it fully; missing it needs an explanation. Aspirational means a stretch; a common rule of thumb in OKR practice is that landing around 0.6-0.7 on stretch goals is a sign they were set well. Agree the label before the quarter, not after.
5. **Calibrate targets from the trend.** Project the baseline forward at its recent growth rate: expected end value = baseline × (1 + weekly growth)^weeks in the quarter. A committed target should sit near that line; a stretch target above it. If a target needs more than double the recent rate, ask what new bet makes that plausible and make sure that bet appears in the initiatives.
6. **Add a health metric to each KR.** One number that must not get worse while chasing the KR (sign-ups with activation rate held, revenue with gross margin held, speed with defect rate held). This blocks gaming.
7. **List initiatives under each KR.** The bets the team believes will move the number. Keep them separate from the KR so the team can swap a failing bet without changing the goal. Send the full list through `topy-prioritization` to check capacity.
8. **Decide the cascade.** Under about 15 people, keep OKRs at company level and name owners. Above that, teams may write their own OKRs that support (not copy) the company KRs.
9. **Set the rhythm and scoring rule now.** Weekly: each owner gives current value and a confidence (0-10, or green/amber/red) that the KR will land. Mid-quarter: a review that may change initiatives but not targets, unless the strategy changed. End: scoring as below.
10. **Save it (TOPY connected).** Offer `memory_create` with `title` "OKRs [quarter] [year]", `content` the full set (objectives, KRs with baseline, target, owner, source, label, health metric), and an `importance_score` reflecting that it is a key record. Do not set `expires_at`: the record is needed for scoring. Preview first, show it, and call again with `confirm: true` and the `confirmation` only after the founder agrees.

### Score
11. **Collect actuals.** For each KR, the end value and its source. Ask; do not estimate.
12. **Score each KR from 0.0 to 1.0.** Metric KR: (actual − baseline) ÷ (target − baseline), capped between 0 and 1. Milestone KR: 1 if done, 0 if not, unless partial credit was defined when it was set. Objective score: the average of its KRs (or a weighted average, if weights were agreed at setting).
13. **Read the scores.** 0.7 or more: delivered. 0.4-0.6: real progress, look at what slowed it. Below 0.4: ask which failed, the target (badly calibrated), the bet (wrong initiative) or execution (not done). A committed KR below 1.0 needs a stated cause. A stretch KR at 1.0 every quarter suggests targets are too safe.
14. **Retro and carry-over.** For each KR: keep, change or drop next quarter, and why. Note which KRs turned out to be poor measures of their objective.
15. **Update the record (TOPY connected).** Get the OKR record's id from `memories_list` and propose `memory_update` with `record_id` and the scored `content` appended. Preview, show, confirm only after the founder agrees.

## Output
**Set mode**
```
Strategy: [one sentence]
Objective 1: [qualitative, no number]
| KR | Baseline | Target | Committed / stretch | Owner | Source | Health metric |
Initiatives: KR 1.1 → [bets]; KR 1.2 → [bets]
Rhythm: weekly check-in day; mid-quarter review date; scoring date
```
**Score mode**
| Objective | KR | Baseline | Target | Actual | Score | Cause | Next quarter |
|---|---|---|---|---|---|---|---|
Then three lessons and the carry-over list.

## Quality bar
- No more than three objectives; no objective contains a number.
- Every KR has baseline, target, owner, data source, label and a health metric.
- No KR is a task; at most one milestone KR per objective.
- Stretch and committed targets are distinguishable from the trend line.
- The set visibly serves the business plan's milestones (when TOPY is connected).
- Scores use the formula, and every miss on a committed KR has a cause.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent baselines, actuals or benchmarks; where a number is unknown, make measuring it the first step.
- OKRs are not a performance review. Advise against tying individual pay to stretch KRs, which pushes people to set safe targets; questions about pay or employment terms should go to an HR or legal adviser.
- Do not change targets mid-quarter to make scores look better; a changed strategy gets a new, labelled set.

## Related skills
- `topy-prioritization` — rank the initiatives under each KR against capacity.
- `topy-kpi-dashboard` — the weekly scorecard the KRs are read from.
- `topy-operating-cadence` — where the weekly and quarterly reviews sit in the company rhythm.
- `topy-plan-revision` — when OKR results mean the business plan's targets should change.
