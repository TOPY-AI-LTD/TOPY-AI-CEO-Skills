---
name: topy-daily
description: The founder's daily brief on TOPY.AI, built from the operating board (goal health, stale KPIs, milestones due, overdue tasks) plus running plans and agent changes, in five lines or fewer and saved as a daily brief. Use when the user says things like "what needs me today?"; "daily check-in"; "morning CEO brief"; "anything waiting for me in TOPY?"; "what's due this week?"; "is my business plan done yet?". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-daily/SKILL.md
---
# Daily CEO check-in

A two-minute morning brief for a founder using TOPY.AI. It starts from the operating board (goals green, amber or
red; KPIs gone stale; milestones due; overdue tasks), adds what finished or failed overnight, and keeps only what
changes today's actions. Five lines or fewer, every number with its source. The brief is saved as a daily CEO brief
so the weekly review can see the trend.

## When to use
- "What needs me today?", "morning brief", "anything waiting in TOPY?", "what's due this week?"
- A scheduled morning run (CEO-J02), or after a long plan generation the founder is waiting on.
- Not for: a deeper look at one goal or KPI (`topy-operating-board`); the weekly review with priorities (`topy-weekly-review`).

## Before you start
- The project: if unknown, `projects_list` (one project → use it; several → ask). If tools are missing → `topy-connect`.
- Everything is a read until the founder picks an action, except saving the brief (step 6).

## Workflow
1. **Board.** `operating_board_get` (with `as_of` if given). Take: `summary` (on_track / at_risk / off_track / unknown), each objective's `health` and `health_reason`, `kpis_stale`, `milestones_due`, `milestones_overdue`, `tasks_overdue`. Health is computed by TOPY; never re-judge it.
2. **Key numbers.** `kpis_list`; pick at most three: the north-star KPI and the KRs of any at-risk or off-track objective. Quote actual vs target with `source` and as-of date. A KPI past its cadence with no value is "stale since <date>", never a number.
3. **Dates.** `milestones_list` (status `planned` or `in_progress`) for anything due in the next 7 days with `progress` under 70%, and `compliance` milestones due within 30 days. `tasks_list` (status `todo` or `in_progress`) for tasks due today.
4. **Overnight.** `plans_list` → for `running`/`queued` call `plan_status`; report finished or failed plans (a failed generation is refunded automatically; a retry costs 50 credits). `agent_actions_list` (limit 20): count the last 24 hours, flag `ok: false`. `risks_list`: only open high risks that changed. `growth_experiments_list`: running tests whose `ended_at` passed. `credits_get` only if a generation is planned.
5. **Rank.** Keep at most three items that need the founder, most important first: off-track goal → overdue milestone or compliance date → failed agent action or plan → stale KPI on a KR → experiment awaiting a call. If nothing needs them, say so.
6. **Save.** Preview `ceo_brief_create` with `brief_type: "daily"`, `title` "Daily brief <date>", `content` (the brief), `payload_json` (each number with `source` and `as_of`, plus the board `summary`), `status: "final"`. Confirm after a yes; a scheduled agent with a standing permission may save it without a preview.
7. **Offer.** One action per item, run only after a yes, using the matching skill.

| Finding | Offer |
|---|---|
| Goal off track | open it with `topy-operating-board`; diagnose before acting |
| Milestone due or overdue | update progress or mark missed (`topy-milestones`) |
| KPI stale | record the value with a source (`topy-kpi-dashboard`) |
| Plan ready / failed | summarise (`topy-business-plan`) / retry after the founder agrees to the cost |
| Experiment overdue | record the result and decision (`topy-growth-experiments`) |
| Agent action failed | show the error; don't retry automatically |

## Output
```
<🟢/🟡/🔴> <project> — <n on track, n at risk, n off track> · <KPI actual vs target (source)> · <n> need you
1. <item> → <what I suggest / already handled>
2. …
3. …
Next: <the one action you recommend>   (or "Nothing needs you today.")
```
Five lines or fewer, about 120 words. No tables unless asked.

## Example
> 🟡 Lumen Labs — 2 on track, 1 at risk · MRR £15.4k vs £17.1k expected (stripe, 14 Feb) · 2 need you
> 1. "Beta launch" due Sunday at 60% → ask the CTO for blockers?
> 2. Activation rate stale since 20 Jan → record this week's value?
> Agents: 4 changes overnight, 0 failed. Next: record activation so Q1 health is real.

## Quality bar
- [ ] Health and numbers come from `operating_board_get`/`kpis_list` this session, each with source and date.
- [ ] Stale KPIs are labelled stale, never filled in.
- [ ] Five lines or fewer; at most three items need a call.
- [ ] The brief was saved only after a yes (or under a standing permission).

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; if a read fails, say which part is missing. Never estimate a KPI.
- Don't start a plan generation or retry (50 credits) without stating the cost and getting a yes.
- The brief reports; it never changes goals or targets (D2: founder only).
- Agent changes are reported, not undone, unless the founder asks.

## Related skills
- `topy-operating-board` — drill into a goal, KPI or milestone.
- `topy-weekly-review` — the weekly memo built from these briefs.
- `topy-milestones`, `topy-kpi-dashboard` — act on dates and stale numbers.
- `topy-risk-register`, `topy-growth-experiments`, `topy-business-plan` — act on what the brief surfaces.
