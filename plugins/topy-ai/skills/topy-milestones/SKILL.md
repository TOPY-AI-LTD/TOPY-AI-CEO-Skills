---
name: topy-milestones
description: Create, track, complete and miss milestones in TOPY — product, revenue, funding, hire, launch and compliance deadlines — each tied to an objective with an owner, a due date and evidence. Use when the user says things like "when is the beta going live?"; "remind me of the annual accounts deadline"; "add a milestone for our first paying customer"; "what milestones are due this month?"; "we shipped the beta, mark it done"; "we're going to miss the launch date". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-milestones/SKILL.md
---
# Milestones and compliance calendar

A milestone is a verifiable change of state with a date: "Beta live", "first paying customer", "CTO hired",
"confirmation statement filed". This skill keeps them in TOPY under the objective they serve, tracks progress,
closes them with evidence, and handles misses honestly — a new date and a reason, not a quiet edit. Compliance
deadlines go in the same list (`milestone_type` compliance) so the daily brief surfaces them in time.

## When to use
- Adding or checking dated deliverables (CEO-J13 product bets, CEO-J12 hires).
- Statutory and contract deadlines: annual accounts, confirmation statement, VAT, insurance, renewals (CEO-J23).
- "We shipped it" / "we'll miss it".
- Not for: open-ended work items (tasks, via `topy-weekly-review`); setting the objectives themselves (`topy-goal-tree`); a hiring plan's roles and budget (`topy-hiring-plan`, which writes hire milestones).

## Before you start
- The project (`projects_list`). `milestones_list` (filter by status or due date) to avoid duplicates; `objectives_list` to pick the objective.
- Ask, one at a time: what will be observably true, by when, who owns it.
- Compliance dates come from the founder or an official source (Companies House, HMRC letter, the contract). Never infer a statutory date from memory.

## Workflow
1. **Shape it.** A good milestone is binary and observable ("Beta open to 50 external users"), not an activity ("work on beta").

| Field | What goes in |
|---|---|
| `name` | the state change |
| `milestone_type` | `product` · `revenue` · `funding` · `hire` · `launch` · `compliance` · `other` |
| `status` | `planned` (default) or `in_progress` |
| `due_date` | the date it must be true |
| `progress` | 0–100 |
| `details` | `{objective_id, owner_role, evidence_ref, cost_gbp, salary_gbp, start_month, origin: {type: "founder"}}` |

2. **Create.** Preview `milestone_create`, show it, confirm after a yes. A scheduled agent with a standing permission may create milestones within its daily cap; nothing else.
3. **Compliance calendar.** One milestone per deadline with `milestone_type` compliance and an `owner_role` (usually CFO). Say it will appear in the brief 30, 7 and 1 days before; add "to be confirmed by your accountant" to `details`.
4. **Track.** `milestones_list` with status `planned`/`in_progress`. TOPY flags a milestone due within 7 days under 70% progress as at risk and an overdue one as off track. Update `progress` only from what the owner reports, via `milestone_get` then `milestone_update` with `details` merged whole.
5. **Complete.** `status` done, `completed_at`, `progress` 100, and `details.evidence_ref` (a link, a record id, a document). No evidence → ask for it before marking done.
6. **Miss.** Set `status` missed and keep the original `due_date`; create the replacement milestone with the new date and `details` noting the reason. If a missed milestone puts an objective off track, that is a goal question for the founder (`topy-goal-tree`); log the call in `topy-decision-log`.
7. **Superseded and delete.** A milestone made obsolete by a plan change → `status` superseded. `milestone_delete` only for duplicates or mistakes; it is permanent.

## Output
```
| Milestone | Type | Due | Owner | Objective | Progress | Status |
Due in 7 days: … · Overdue: … · Compliance next 90 days: …
```
After a write: the record as saved, and "Saved" only when the tool result confirms it.

## Example
> "The beta will slip two weeks." `milestones_list` finds "Beta open to 50 users", due 16 Feb, 60%. Preview: mark it `missed` (reason: auth rework) and create "Beta open to 50 users" due 2 Mar, owner CTO, same objective. Founder agrees; both confirmed. Agent notes the Q1 activation objective may now be at risk and offers `topy-goal-tree`.

## Quality bar
- [ ] Each milestone is a binary, observable state with a due date and an owner.
- [ ] Each is tied to an objective (`details.objective_id`) or the founder said it stands alone.
- [ ] Done only with evidence; misses keep history (missed + new milestone).
- [ ] Compliance dates are sourced, never inferred.
- [ ] `details` sent whole on update.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; a KPI actual always has a `source` (a figure the founder gives is `source: founder`).
- Goal changes are D2: moving a milestone that changes an objective's target needs the founder's yes; never under a standing permission.
- Milestones extracted from the plan carry `origin`; before changing one the founder edited (`details.edited: true`), say so.
- Anything sent outside TOPY (W3) is confirmed one at a time; money, equity and signatures (hire costs, funding) are recorded or simulated only.
- Not legal or tax advice: statutory deadlines should be confirmed by an accountant or lawyer. Deletes are permanent (W4).

## Related skills
- `topy-goal-tree` — the objectives milestones hang under.
- `topy-operating-board`, `topy-daily` — where due and overdue milestones surface.
- `topy-hiring-plan` — hire milestones with cost and start month.
- `topy-decision-log` — record why a date moved.
