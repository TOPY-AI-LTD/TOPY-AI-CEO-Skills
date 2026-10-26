---
name: topy-goal-tree
description: Turn a founder's ambition into a North Star, up to three Company Goals and this quarter's Objectives with Key Results in TOPY, each with a KPI, an owner and a cadence. Use when the user says things like "I want to reach £1M ARR within a year"; "help me set this year's goals"; "set our company goals"; "what should our North Star be?"; "break this year's goal into quarterly objectives"; "check our goals have KPIs and owners". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-goal-tree/SKILL.md
---
# Goal tree

Every piece of CEO work should hang off a goal, and every goal needs a number, an owner and a date. This skill
turns "I want to get to £1M ARR in a year" into a tree the whole company can steer by: one North Star, at most
three Company Goals for the year, three to five Objectives this quarter, and two to four Key Results each, stored
as real objectives and KPIs in TOPY so health can be tracked from actuals, not opinion.

## When to use
- Day 0: the founder states an ambition, or a business plan has just been generated (CEO-J01).
- Quarterly planning: next quarter's Objectives under the Company Goals (CEO-J08).
- Annual planning: new Company Goals after the year's scenarios (CEO-J20).
- Auditing an existing tree: Objectives without KPIs, KPIs without owners or cadence.
- Not for: scoring a finished quarter (`topy-okrs`); designing a single KPI in depth (`topy-kpi-dashboard`); dated deliverables (`topy-milestones`).

## Before you start
- The project: `projects_list`, then `project_get` (read `metadata_json.north_star` if set).
- `plans_list`: is there a plan of record? Its targets are the reference the goals should match.
- `objectives_list` and `kpis_list`: what already exists. Never create a second tree beside the first.
- Ask one question at a time: the ambition, the deadline, then the limits (cash, hours, what we won't do).

## Workflow
1. **North Star.** One sentence, one metric, stable for the year ("£1M ARR from self-serve SMB customers by Dec 2027"). Check it against the plan of record: if the plan says £400k and the founder says £1M, don't edit either; offer two options — lower the ambition, or revise the plan (`topy-plan-revision`).
2. **Company Goals (≤ 3).** Each is an objective with `cycle_label` "FY2027", `period_start`/`period_end` for the year, `plan_json.level` "company", `plan_json.owner_role` and 1–2 KPIs in `plan_json.kr_kpi_ids`. Together they must explain the North Star; a goal that doesn't is cut.
3. **Quarterly Objectives (3–5).** `cycle_label` "2027-Q1", `plan_json.level` "quarterly", `plan_json.parent_id` = the Company Goal, `owner_role` (CEO, CPO, CMO, CRO, CTO, COO, CFO, CSO), `contributors`. Written as an outcome ("Reach £20k MRR with 60% on annual plans"), not an activity.
4. **Key Results (2–4 per Objective).** Each is a KPI. Reuse an existing KPI from `kpis_list` where its `metadata_json.key` matches (standard keys: `mrr`, `new_customers`, `churn_rate_monthly`, `activation_rate`, `signups`, `cash_balance`, `runway_months`, …; custom ones start `custom.`). Otherwise create it with `kpi_create`: `name`, `category`, `unit`, `baseline_value` (from a recorded actual, or ask), `target_value`, `cadence`, and `metadata_json` `{key, higher_is_better, owner_role, objective_id, targets_by_period, thresholds: {at_risk: 0.95, off_track: 0.80}, origin: {type: "founder"}}`.
5. **Gap check.** Every Objective: ≥ 1 KR with baseline and target; every KPI: owner and cadence; every quarterly Objective: a `parent_id`; no more than 5 Objectives. Fix gaps before saving.
6. **Show the tree** (below) as one card and ask for a yes. Then save, each write a preview first and confirmed only after the founder agrees: Company Goals (`objective_create`), KPIs (`kpi_create`), Quarterly Objectives with `kr_kpi_ids` filled in.
7. **North Star.** Preview `project_update` with the whole `metadata_json` (read first, merge in the North Star) and `memory_create` with `memory_type` "north_star" and a high `importance_score`.
8. **Changing a goal later.** Read it with `objective_get`. Lowering a target, dropping or replacing an objective is a D2 decision: show old vs new, get the founder's yes, then `objective_update` with the whole `plan_json` merged. Prefer `status` "abandoned" over `objective_delete`; delete only a duplicate or a mistake (permanent). Suggest logging the reason in `topy-decision-log`.

## Output
```
**North Star:** <sentence> (metric: <key>, target <value> by <date>)
**Company Goals FY<yyyy>**
1. <goal> — owner <role> — KPI <key>: <baseline> → <target>
**Quarterly Objectives <yyyy-Qn>**
| Objective | Parent | Owner | Key Results (KPI: baseline → target, cadence) |
**Gaps fixed:** … **Open questions:** …
```

## Example
> Founder of Lumen Labs: "£1M ARR in a year." `plans_list` shows a plan targeting £600k ARR. Agent offers: keep £1M and revise the plan, or adopt £600k. Founder keeps £1M and asks for a plan revision later.
> Tree: Company Goals — (1) £1M ARR (CRO, `mrr` £12k → £83k), (2) gross margin ≥ 75% (CFO). Q1: "Reach £20k MRR, 60% annual" (CRO; KRs `mrr` 12k → 20k monthly, `custom.annual_share` 35% → 60%), "Activation to 40%" (CPO; `activation_rate` 22% → 40% weekly).

## Quality bar
- [ ] One North Star; ≤ 3 Company Goals; 3–5 Objectives this quarter.
- [ ] Every Objective has 2–4 KRs, each a KPI with baseline, target, owner and cadence.
- [ ] Every quarterly Objective has a `parent_id`.
- [ ] Baselines come from recorded actuals or the founder (labelled), never guessed.
- [ ] Conflicts with the plan of record raised as options, not silently fixed.
- [ ] Nothing saved without the founder seeing the whole tree and saying yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Goal changes are D2: preview and the founder's yes every time; never written under a standing permission.
- Numbers only from tools; a KPI actual always has a `source` (a figure the founder gives is `source: founder`).
- Records extracted from the plan carry `origin`; before changing one the founder edited (`edited: true`), say so and ask.
- Anything sent outside TOPY (W3) is confirmed one at a time; money, equity and signatures are recorded or simulated only — a professional confirms.
- Deletes are permanent (W4); prefer `status` "abandoned".

## Related skills
- `topy-operating-board` — health of the tree from actuals.
- `topy-okrs` — score the quarter at its end.
- `topy-kpi-dashboard` — design a KPI and its thresholds in depth.
- `topy-milestones` — dated deliverables under an Objective.
- `topy-plan-revision` — when the goals change the plan's numbers.
- `topy-decision-log` — record why a goal changed.
