---
name: topy-okrs
description: Turns a startup's strategy into a few quarterly objectives with measurable key results, saved in TOPY as objectives linked to KR KPIs, then scores them at quarter end from recorded actuals and carries the lessons forward. Use when the user says things like "help me set OKRs for next quarter"; "turn our strategy into goals"; "are these good key results?"; "score our OKRs"; "what should the team aim for this quarter?"; "our goals are just a to-do list". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-okrs/SKILL.md
---
# OKRs

Helps a founder translate strategy into a quarter's focus: a few objectives that say what matters, key results that
prove it happened, and a fair way to score them. Two modes: **set** (before the quarter) and **score** (at the end).
With TOPY connected, OKRs are real records: each objective is a quarterly objective under a company goal, each KR is a
KPI with baseline and target, and scoring reads the actuals already recorded. Nothing is kept as loose memory notes.

## When to use
- Before a quarter starts (CEO-J08), or after a raise or pivot when goals need resetting.
- Goals read like task lists, or nobody knows if they were hit.
- End of quarter: scoring, retro, carry-over (CEO-J09).
- Not for: the yearly North Star and company goals (`topy-goal-tree`); ranking initiatives (`topy-prioritization`); KPI definitions and thresholds (`topy-kpi-dashboard`).

## Before you start
- Ask which mode: set or score.
- With TOPY: `projects_list` / `project_get`; `objectives_list` for company goals (`plan_json.level: "company"`) and the current quarter's objectives; `kpis_list` for existing KPIs (reuse them as KRs instead of duplicating); `plans_list` + `plan_get` for the plan's milestones and targets. No company goal yet → run `topy-goal-tree` first.
- Without TOPY: ask for the year's goal, stage, last quarter's goals and results.
- Baselines one at a time; `kpi_values_list` gives the recent trend. Unknown baseline → the first KR is to measure it.

## Workflow
### Set
1. **Strategy in one sentence.** "This year we win by [approach] for [customer], measured by [outcome]." If the founder can't say it, resolve that first.
2. **One to three objectives**, each under a company goal. Qualitative, no number, fits a quarter: "Make onboarding something customers rave about".
3. **Two to four KRs each**: "[metric] from [baseline] to [target] by [date]", one owner, one source. Activities are not KRs; at most one milestone KR per objective (track it with `topy-milestones`). Completeness test: all KRs hit → objective clearly achieved? Necessity test: drop one → anything lost?
4. **Committed or aspirational**, agreed now. Landing ~0.6-0.7 on stretch KRs is a common rule of thumb for well-set stretch.
5. **Calibrate from the trend**: expected end = baseline × (1 + weekly growth)^weeks. Committed near the line, stretch above; more than double the recent rate needs a named new bet.
6. **Health metric per KR**: one number that must not get worse (sign-ups with activation held, revenue with margin held).
7. **Initiatives** under each KR, kept separate so a failing bet can be swapped; check capacity with `topy-prioritization`.
8. **Save (TOPY).** Show the whole set, then on a yes:
   - Each KR: reuse an existing KPI (preview `kpi_update` with the quarter's `target_value`, `baseline_value` and `metadata_json.targets_by_period`, merged into the whole object read with `kpi_get`) or preview `kpi_create` with `name`, `category`, `unit`, `cadence`, `baseline_value`, `target_value` and `metadata_json` {`key` (standard key or `custom.`), `higher_is_better`, `owner_role`, `thresholds`, `origin: {"type": "founder"}`}.
   - Each objective: preview `objective_create` with `cycle_label` (e.g. `2027-Q1`), `period_start`, `period_end`, `objective`, `status: "active"`, `plan_json` {`level: "quarterly"`, `parent_id` (the company goal), `owner_role`, `contributors`, `kr_kpi_ids`, `committed`/`aspirational` per KR, `health_metric`}. Then set `metadata_json.objective_id` on each KR KPI with `kpi_update`.
   Every write is a preview first; confirm only after the founder agrees.
9. **Rhythm.** Weekly actuals and confidence in `topy-weekly-review`; mid-quarter review may change initiatives, not targets.

### Score
10. **Read actuals.** `objective_get` (its `key_results`), then `kpi_values_list` per KR for the value at `period_end`. Missing value → ask the owner for it with a source (record via `topy-kpi-dashboard`); never estimate.
11. **Score each KR 0.0-1.0**: (actual − baseline) ÷ (target − baseline), capped 0-1 (reverse for lower-is-better). Milestone KR: 1 or 0 unless partial credit was agreed. Objective = average (or agreed weights).
12. **Read the scores.** ≥ 0.7 delivered; 0.4-0.6 progress, find what slowed it; < 0.4 ask whether the target, the bet or the execution failed. A committed KR under 1.0 needs a cause.
13. **Close and carry.** Preview `objective_update` with `status: "closed"` and `plan_json` (read whole with `objective_get`, then add `score` and `retro`). KRs to keep go into next quarter's set; KPIs no longer used can be set `status: "retired"` with `kpi_update`. Keep up to three lessons with `memory_create` (`memory_type: "lesson"`).
14. **Delete only mistakes.** `objective_delete` and `kpi_delete` are permanent (KPI delete removes its actuals too): only for duplicates or records made in error, after a clear yes. Prefer `abandoned` / `retired`.

## Output
**Set**
```
Strategy: <one sentence> · Company goal: <title>
Objective 1: <qualitative> · owner <role>
| KR | KPI key | Baseline | Target | Committed/stretch | Owner | Source | Cadence | Health metric |
Initiatives: KR 1.1 → <bets>
Saved: <objective ids, KPI ids> (only after confirmation)
```
**Score**: `Objective | KR | Baseline | Target | Actual (source, date) | Score | Cause | Next quarter`, then three lessons.

## Quality bar
- No more than three objectives; none contains a number; each has a `parent_id`.
- Every KR has baseline, target, owner, cadence, source and a health metric; no KR is a task.
- Existing KPIs reused rather than duplicated.
- Scores use recorded actuals only, with the formula; every committed miss has a cause.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Objectives and KR targets are D2 decisions: always a preview and the founder's yes; never written under a standing permission.
- Numbers only from tools or the founder; actuals carry a `source`. Never invent baselines, actuals or benchmarks.
- Records extracted from the plan carry `origin`; if a KPI or objective has `edited: true`, say so before changing it.
- Don't move targets mid-quarter to improve scores; a changed strategy gets a new, labelled set.
- OKRs are not a performance review; pay and employment questions go to an HR or legal adviser.

## Related skills
- `topy-goal-tree` — the North Star and company goals the objectives sit under.
- `topy-kpi-dashboard` — KPI definitions, thresholds and recording values.
- `topy-prioritization` — initiatives against capacity.
- `topy-weekly-review` — weekly check-ins on the same KRs.
- `topy-plan-revision` — when results mean the plan's targets should change.
