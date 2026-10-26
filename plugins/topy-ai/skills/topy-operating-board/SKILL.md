---
name: topy-operating-board
description: Read the TOPY operating board and answer "how are we doing?" — objective health and why, stale KPIs, due and overdue milestones and tasks — with the next step for each red item. Use when the user says things like "how are we doing?"; "what's red on the board?"; "are we on track this quarter?"; "how's revenue right now?"; "which KPIs haven't been updated?"; "what's overdue?". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-operating-board/SKILL.md
---
# Operating board

The founder asks "how are we doing?" and wants the truth now, not at Friday's review. This skill reads TOPY's
operating board — objectives with deterministic health, KPI actuals against expected pace, stale KPIs, due and
overdue milestones and tasks — and turns it into a conclusion, three numbers and the one thing to act on. It
explains health; it never re-judges it.

## When to use
- "How are we doing?", "what's red?", "are we on track?" at any time (CEO-J05).
- As the first read of the daily brief or weekly review (CEO-J02, CEO-J04).
- After a plan finished generating, to fill an empty board from the plan.
- Not for: setting goals (`topy-goal-tree`); diagnosing a metric in depth (`topy-plan-vs-actual`, `topy-alerts`); the full daily routine (`topy-daily`).

## Before you start
- The project: `projects_list` (one → use it; several → ask).
- Scope: whole company, one objective or one KPI. Default: whole company, `as_of` today.

## Workflow
1. **Read.** `operating_board_get` (with `as_of` if asked). Fields: `objectives[]` (`health`, `health_reason`, `key_results[]` with `actual`, `expected`, `target`, `as_of`, `source`), `kpis_stale`, `milestones_due`, `milestones_overdue`, `tasks_open`, `tasks_overdue`, `personas`, `summary`.
2. **Empty board?** If there are no objectives, KPIs or milestones: `plans_list`. A plan with status `success` → offer `plan_operating_extract` (a preview first; it runs as a job and costs no credits), then follow it with `plan_status` using the returned `job_id` and read the board again. No plan → `topy-goal-tree`.
3. **Explain health.** Health is computed by TOPY, not by you: expected = baseline + (target − baseline) × elapsed share of the period; on track ≥ 95% of expected, at risk 80–95% (or a milestone due within 7 days under 70% progress), off track < 80% (or a milestone overdue), unknown = no actual within the KPI's cadence. Quote `health_reason`; don't recompute or soften it.
4. **Unknown is a data problem.** For each entry in `kpis_stale` say "last updated n days ago" and who owns it (`owner_role`); suggest recording the actual (`topy-kpi-dashboard`) or connecting a source (`topy-integrations`). Never fill in a guess.
5. **Rank.** Keep at most three items that change what someone does this week, in this order: off-track objectives, overdue milestones, at-risk objectives, stale KPIs behind a KR, overdue tasks.
6. **Next step per item.**

| Finding | Suggest |
|---|---|
| Objective off track | diagnose the KR (`topy-plan-vs-actual`), then a corrective action or an explicit "accept the gap" decision (`topy-decision-log`) |
| Milestone overdue | mark `missed` with a new date, or update progress (`topy-milestones`) |
| KPI stale | record the actual with its source, or set up a source |
| Task overdue | reassign or re-date it; the owner is in the task |

7. **Answer.** The snapshot below. Offer to go deeper on one item; run any write only through the matching skill and after a yes.

## Output
```
**<project> — <as_of>**: 🟢 on track / 🟡 at risk / 🔴 needs you (<summary counts>)
Numbers: <KPI> <actual> vs expected <expected>, target <target> (<source>, <as_of>) × up to 3
Biggest risk: <one line>
Needs attention: <up to 3 items, each with its next step>
Stale: <n KPIs, oldest n days>
```
Under 120 words unless the founder asks for the full board.

## Example
> **Lumen Labs — 14 Feb 2027**: 🟡 at risk (2 on track, 1 at risk, 1 unknown)
> Numbers: MRR £15.4k vs expected £17.1k, target £20k (stripe, 14 Feb).
> Biggest risk: Q1 revenue objective — "linear pace needs £17.1k by today; actual £15.4k (−10%)".
> Needs attention: Beta launch due in 2 days at 60% → ask the CTO owner for blockers.
> Stale: Activation rate, last updated 25 days ago (CPO).

## Quality bar
- [ ] Every number comes from `operating_board_get` in this session, with its source and date.
- [ ] Health quoted from TOPY, never re-judged.
- [ ] Stale data labelled with its age; nothing estimated.
- [ ] At most three items need attention.
- [ ] No write ran without the founder's yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; a KPI actual always has a `source` (a figure the founder gives is `source: founder`).
- Goal changes are D2: never lower a target or close an objective from here; hand off to `topy-goal-tree` for the founder's decision.
- Records extracted from the plan carry `origin`; extraction skips records the founder edited (`edited: true`) — say how many were skipped.
- Anything sent outside TOPY (W3) is confirmed one at a time; money, equity and signatures are recorded or simulated only.

## Related skills
- `topy-daily`, `topy-weekly-review` — the routines that start from this board.
- `topy-goal-tree` — set or change what the board measures.
- `topy-milestones`, `topy-kpi-dashboard` — act on overdue milestones and stale KPIs.
- `topy-plan-vs-actual` — why a financial KR is behind.
- `topy-integrations` — keep KPIs fresh automatically.
