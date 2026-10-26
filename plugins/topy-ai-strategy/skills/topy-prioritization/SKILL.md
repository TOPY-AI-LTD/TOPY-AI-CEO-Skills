---
name: topy-prioritization
description: Ranks a startup's competing initiatives against one goal and the team's real capacity using RICE, ICE or cost of delay, draws the cut line and writes down what the company will not do. Use when the user says things like "we have too many priorities"; "what should we focus on this quarter?"; "rank these projects for me"; "help me say no to things"; "RICE score our roadmap"; "everything feels urgent". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-prioritization/SKILL.md
---
# Prioritization

Gives a small team a ranked, capacity-checked list of what to work on and, just as important, an explicit list of what it will not do. The agent ties every initiative to one goal, scores it with a method that fits the situation, fills the team's real capacity from the top down and draws the line. When TOPY is connected, it reads the go-to-market plan and earlier priority calls, and can save the result as a decision.

## When to use
- Quarter or month planning; a roadmap or backlog that has outgrown the team.
- After a funding round, a big customer loss or a strategy change, when old priorities may no longer fit.
- The founder says "everything is urgent", "we're spread too thin", or asks what to cut.
- Not for: a single choice between a few options (use `topy-decision-memo`), setting the goal itself (use `topy-okrs`), or ranking marketing ideas only (a CMO skill does that better).

## Before you start
- With TOPY connected:
  - If you do not know the project, call `projects_list` and ask which one; then `project_get` for stage and market.
  - Call `gtm_plans_list`; if a plan exists, read it with `gtm_plan_get` and take its funnel targets and channels as candidate goals and initiatives.
  - Call `decisions_list` and look for the last prioritization or roadmap decision. Items that were deliberately cut last time should not reappear without a new reason.
- Without TOPY, ask: the single most important outcome for the period, and what was decided last time.
- Then collect, one question at a time: the list of initiatives (ask for in-flight work and upkeep too, not only new ideas), who works on what, the length of the period, and any hard dates (contract, launch, compliance deadline).

## Workflow
1. **Fix the goal first.** One outcome for the period, ideally a number with a date ("reach 40 paying customers by 30 June"). If the founder gives three goals, ask which one wins when they conflict. If there is no goal, stop and run `topy-okrs` first; ranking without a goal is opinion.
2. **Clean the list.** Merge duplicates; split anything larger than about half the period into a first slice; rewrite vague items as outcomes ("improve onboarding" → "new users reach first report in one session"). Put three kinds of work in separate lanes before scoring:
   - *Mandatory*: legal, security, compliance, contractual commitments. Not scored; capacity is reserved first.
   - *Keep the lights on*: support, bug fixing, routine operations. Estimated, reserved, not scored.
   - *Discretionary*: everything else. This is what gets ranked.
3. **Measure capacity.** Available person-weeks = people × weeks in the period × focus factor. Use the team's own history for the focus factor; if there is none, a common rule of thumb is that only 60-70% of time goes to planned project work after meetings, support and interruptions. Subtract the mandatory and upkeep lanes. Keep a buffer of roughly 15-20% (rule of thumb) for the unexpected.
4. **Pick the scoring method.**
   | Situation | Method |
   |---|---|
   | Early stage, little data, a quick first sort of up to ~20 items | ICE |
   | Reach can be counted (users, accounts, deals affected) | RICE |
   | Timing matters: deadlines, seasonal windows, competitor races | Cost of delay (CD3) |
   Use one method per list; mixing methods makes scores incomparable.
5. **Score with written scales.** Agree the scales before scoring:
   - *RICE* = Reach × Impact × Confidence ÷ Effort. Reach: customers or accounts affected in the period. Impact: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal. Confidence: 100% (data from customers), 80% (strong signals), 50% (a hunch). Effort: person-weeks.
   - *ICE* = Impact × Confidence × Ease, each 1-10. Anchor confidence: 8-10 needs customer data or a past result, 5-7 needs an analogous case, 1-4 is opinion.
   - *CD3* = cost of delay per week ÷ duration in weeks. Cost of delay is the value lost each week the item is not done (revenue, a deal at risk, a window closing). Note the urgency profile: steady, fixed date, or expedite.
   Write a one-line reason for each impact and confidence score. Flag scores the founder gave without evidence.
6. **Adjust for structure.** Move an item up if it unblocks a higher-ranked one or is a prerequisite for the main bet; note the dependency in the table. Do not boost an item because it is cheap if it does not serve the goal.
7. **Draw the line.** Sort by score, add effort down the list and stop where cumulative effort reaches the discretionary capacity. Everything below is out for this period. As a rule of thumb, a team under about ten people should not run more than two or three major initiatives at once; if the line admits more, prefer finishing over starting.
8. **Test the top.** Ask: "If only the top three get done, does the goal move?" If not, the scores are measuring the wrong thing; revisit impact scores against the goal.
9. **Check the edge.** For the five items nearest the line, change the most uncertain input by one step. Items that cross the line are "edge cases": the founder decides them, with the trade-off spelled out.
10. **Write the not-doing list.** Every item below the line, with the reason and a revisit trigger ("revisit if three customers ask", "revisit next quarter"). Saying no explicitly is part of the output.
11. **Write the stop list.** For each in-flight item, ask: "Knowing what we know now, would we start this today?" If no, propose stopping it, and state what finishing would cost versus what stopping frees up. Past effort is not a reason to continue.
12. **Save it (TOPY connected).** Offer to record the call with `decision_create`: `title` (e.g. "Priorities for Q3"), `context` (goal and capacity), `options_considered` (the ranked list with scores), `decision` (the items above the line and the stop list, as the founder approved them), `rationale` (why the top items win, and the edge-case calls), `impact_scope` (teams or areas affected). Preview first, show it, then `confirm: true` with the `confirmation` only after the founder agrees.

## Output
1. Goal and capacity: the goal, available person-weeks, reserved lanes, buffer.
2. Ranked table:
   | # | Initiative | Serves goal by | Score inputs | Score | Effort (pw) | Cumulative | In / out | Note |
   |---|---|---|---|---|---|---|---|---|
3. Edge cases for the founder to decide, with the trade-off.
4. Not-doing list: item | reason | revisit trigger.
5. Stop list: in-flight item | cost to finish | what stopping frees.
6. One paragraph: what the team should say when someone asks for something on the not-doing list.

## Quality bar
- One goal; every ranked item states how it serves it.
- Scales were written before scoring; every impact and confidence score has a reason.
- Capacity uses the team's real numbers, with mandatory and upkeep work reserved first.
- The cut line falls where capacity runs out, not where the list feels comfortable.
- The not-doing and stop lists exist and have reasons.
- Edge cases near the line are flagged, not hidden.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent reach, revenue, effort or customer demand; mark founder estimates as estimates.
- Not legal or regulatory advice: when an item is in the mandatory lane because of law or contract, suggest the founder confirms the obligation with a lawyer.
- Scores are a thinking aid, not the decision. The founder may override a ranking; record the override and the reason.
- Do not reprioritize work owned by other people without the founder agreeing who tells them.

## Related skills
- `topy-okrs` — set the goal the ranking serves.
- `topy-decision-memo` — when one edge case deserves a full decision.
- `topy-weekly-review` — check each week that the team is working above the line.
- `topy-gtm-plan` — the go-to-market plan that many initiatives come from.
- `topy-growth-experiments` — run the low-confidence items as experiments first.
