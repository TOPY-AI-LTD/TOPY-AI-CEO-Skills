---
name: topy-daily
description: The founder's daily check-in on TOPY.AI — plans being written, changes agents made, risks and experiments that need a call — cleared one approved action at a time. Use when the user says things like "what needs me today?"; "daily check-in"; "anything waiting for me in TOPY?"; "is my business plan done yet?"; "what did my agents change?"; "morning CEO brief". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-daily/SKILL.md
---
# Daily CEO check-in

A five-minute morning brief for a founder using TOPY.AI: what the AI CEO finished overnight, what is still running,
which records need a decision, and what agents changed on their behalf. Reads first; anything that changes data
is offered one item at a time and runs only after the founder says yes.

## When to use
- "What needs me today?", "morning brief", "anything waiting in TOPY?"
- After a long plan generation or revision was started and the founder wants to know if it's done.
- Not for: the weekly review with priorities (`topy-weekly-review`); writing a plan (`topy-business-plan`).

## Before you start
- The project: if unknown, `projects_list` (one project → use it; several → ask). If tools are missing → `topy-connect`.
- Everything in this skill is a read until the founder picks an action.

## Workflow
1. **Plans.** `plans_list` (status `all`). For each plan:
   - `running` or `queued` → `plan_status` with its `plan_id`; report `completed_subtasks/total_subtasks`.
   - `success` since yesterday → "ready" with title and words.
   - `failed` → say so with `error_message`; the credits of a failed generation are refunded automatically. Offer `topy-business-plan` to retry (it costs 50 credits again).
2. **Agent changes.** `agent_actions_list` (limit 20). Group the last 24 hours by tool; flag any entry with `ok: false` and any made under a standing permission (the summary says "standing permission").
3. **Risks.** `risks_list`. Surface open risks (`status` not closed) with `risk_level` high, or `likelihood_score` × `impact_score` in the top band of the scale the project uses; don't list everything.
4. **Experiments.** `growth_experiments_list`. Surface running experiments whose `ended_at` has passed (they need a ship/kill/iterate call) and finished ones with no `result_summary`.
5. **Recent decisions.** `decisions_list`; mention decisions made since yesterday (`decided_at`) so the founder sees what was recorded.
6. **Credits (only if a generation is planned).** `credits_get`; note when the balance is under 50.
7. **Brief and offer.** Write the brief (below), then offer at most three actions, most important first. Run each only after a yes, using the matching skill.

| Finding | Offer |
|---|---|
| Plan ready | summarise it (`topy-business-plan`) or check it like an investor (`topy-investor-ready`) |
| Plan failed | retry after the founder agrees to the cost |
| Experiment overdue | record the result and decision (`topy-growth-experiments`) |
| Risk escalated | update the mitigation (`topy-risk-register`) |
| Agent action failed | show the error; don't retry automatically |

## Output
```
**Today — <project>**
Ready: <plan titles, words>            (or "nothing new")
Running: <plan> <n/m sections>
Needs a call: <up to 3 items, one line each>
Agents changed: <count> (<n> failed)
Next: <the one action you recommend>
```
Under 150 words. No tables unless asked.

## Example
> **Today — Lumen Labs**
> Ready: "Lumen Labs Seed Plan (revised 2026-10-26)", 14,055 words.
> Needs a call: the "Founder-led LinkedIn" experiment ended 3 days ago with no decision; key-person risk is now high.
> Agents changed: 4 (0 failed) — 3 journal entries and 1 decision by your weekly agent.
> Next: record the experiment result (ship, kill or iterate)?

## Quality bar
- [ ] Every "ready"/"running" claim comes from `plans_list`/`plan_status` in this session.
- [ ] At most three items need a call; the rest are summarised in a count.
- [ ] No write ran without the founder's yes.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Don't start a plan generation or retry (50 credits) without stating the cost and getting a yes.
- Never invent figures or progress; if a read fails, say which part is missing.
- Agent changes are reported, not undone, unless the founder asks.

## Related skills
- `topy-weekly-review` — the weekly version with priorities.
- `topy-business-plan` — read, edit or retry a plan.
- `topy-risk-register`, `topy-growth-experiments`, `topy-decision-log` — act on what the brief surfaces.
