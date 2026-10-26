---
name: topy-weekly-review
description: 'The weekly operating review on TOPY.AI: record the week''s KPI actuals with sources, read goal health from the board, settle the decisions that are due, and save a one-page weekly memo with next week''s three priorities as tasks. Use when the user says things like "run my weekly CEO review"; "weekly review"; "Friday review"; "are we on track this week?"; "what should I focus on next week?"; "write the weekly memo". Needs the TOPY MCP server.'
license: MIT
metadata:
  category: core
  tier: core
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-weekly-review/SKILL.md
---
# Weekly CEO review

Once a week the founder spends ten minutes on one question: is the company on the right track, and what do I need
to decide? This skill gets the week's numbers into TOPY first (with sources), reads goal health from the operating
board, works out what drifted and why, and writes a one-page memo in the fixed CEO format. Next week's priorities
become tasks; nothing is saved without the founder's yes.

## When to use
- "Weekly review", "Friday review", "are we on track?", "write the weekly memo" (CEO-J04).
- Before a board or investor update (then hand off to `topy-investor-relations`).
- Not for: today's brief (`topy-daily`); a single big decision (`topy-decision-memo`); quarter-end scoring (`topy-okrs`).

## Before you start
- The project (`projects_list` if unknown). The window: the last 7 days unless the founder says otherwise.
- Ask one question first: "What was the most important thing that happened this week, in your words?"

## Workflow
1. **Collect actuals.** `kpis_list`: for each active KPI with `weekly` cadence (or a monthly one whose period just ended) with no value for this period, get the actual from a cofounder report, a connected source or the founder. Preview `kpi_value_record` per value with `period_date` (the period's end date), `actual_value` and `metadata_json.source` (`stripe`, `ga4`, `ledger`… or `founder` when they said it); confirm on a yes. Writing the same period again replaces the value (`replaced: true`): say so. No number → leave it stale and say so.
2. **Read health.** `operating_board_get` and `objectives_list` (status `active`): each objective's `health`, `health_reason` and `key_results`. Health is TOPY's deterministic rule (expected vs actual, ±5% / 20% thresholds); don't override it.
3. **Read the week.** `ceo_briefs_list` (this week's daily briefs, for trend), `decisions_list` (decided in the window, and any whose review date passed), `risks_list` (open, rose or high), `growth_experiments_list` (ended, needing a call), `journal_entries_list` (wins, blockers).
4. **Find the drift.** For every `off_track` objective: the likely cause (from records, not guesses) and either a corrective action or an explicit "accept the drift" decision. For `at_risk`: what would turn it. Blockers seen twice are a pattern.
5. **Decisions.** D0/D1 calls inside an agreed budget can be logged with `decision_create` (options and rationale). Anything that changes a goal, a KR target, pricing, headcount or spend beyond budget is D2: draft it for the founder (`topy-decision-memo`), never decide it here. At most three decisions for the founder.
6. **Next week's three priorities.** Each traces to an objective, risk or blocker; one owner; a measurable outcome by next Friday; at least one addresses the worst-health goal. Name what you are deliberately not doing.
7. **Show the memo** (below) and let the founder edit it.
8. **Save (only with a yes).**
   - Memo: preview `ceo_brief_create` with `brief_type: "weekly"`, `title` "Weekly memo, week of <date>", `content`, `payload_json` (numbers with `source`/`as_of`, the health snapshot), `status: "final"`.
   - Priorities: one `task_create` each with `title`, `cycle_id` (the objective it serves), `task_type: "action"`, `priority`, `due_at`, and `details.owner_role` or `assignee_user_id`.
   - Optionally the week as a journal entry: `journal_entry_create` with `entry_type` "weekly_review", `wins`, `blockers`, `next_actions`.
   Each is a preview first; confirm only after the founder agrees. A scheduled agent's standing permission may cover `kpi_value_record`, `task_create`, `ceo_brief_create` and `decision_create`, nothing else.

## Output
```
## Week of <date> — <project>: 🟢 on track / 🟡 at risk / 🔴 needs you
**Numbers:** <3-5 KPIs: actual vs target (source, as of)>
**Progress:** <outcomes with evidence>
**Drift:** <goal> — <cause> — <what I've done or propose>
**Please decide:** <0-3 items, each with recommendation and alternative>   (or "Nothing needs you.")
**Next week:** 1. <priority> — <owner>, done when <outcome> (serves <objective>) 2. … 3. …
**Not doing:** …
```
One page, under 250 words.

## Example
> **Week of 8 Feb — Lumen Labs: 🟡 at risk**
> **Numbers:** MRR £15.4k vs £17.1k expected (stripe); signups 140 vs 160 (ga4); runway 11.2 months (ledger).
> **Drift:** "£20k MRR in Q1" at risk — annual-plan uptake 31% vs 60% target; pricing page B goes live Monday (in budget).
> **Please decide:** extend the beta by two weeks? Recommended: yes; alternative: launch with known gaps.
> **Next week:** 1. Pricing page B live — CRO, done when live with tracking. 2. Beta blockers cleared — CTO, done when progress ≥ 80%. 3. 5 customer calls — founder.

## Quality bar
- [ ] Every number in the memo was recorded or read this session and shows its source.
- [ ] Every off-track objective has a corrective action or an explicit accept decision.
- [ ] No goal or target changed; D2 items are drafted for the founder.
- [ ] Exactly three priorities, each with owner, outcome and the objective it serves.
- [ ] Nothing saved without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; KPI actuals always carry `source` (`founder` when the founder said it). Never fill a stale KPI with an estimate.
- Goal and KR target changes are D2: a preview and the founder's yes, never under a standing permission.
- Don't close risks or experiments here; hand off to their skills.

## Related skills
- `topy-daily` — the daily briefs this review rolls up.
- `topy-operating-board` — the board behind the health.
- `topy-kpi-dashboard` — KPI definitions, owners and thresholds.
- `topy-okrs` — quarter-end scoring of the same objectives.
- `topy-decision-log`, `topy-founder-journal` — where decisions and reflections are kept.
- `topy-investor-relations` — turn the month into an investor update.
