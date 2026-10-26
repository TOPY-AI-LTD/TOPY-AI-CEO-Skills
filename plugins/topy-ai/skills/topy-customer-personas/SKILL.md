---
name: topy-customer-personas
description: Keep the company's customer personas in TOPY — extracted from the business plan, corrected with evidence from research and customers, and compared to decide who to serve first. Use when the user says things like "who is our target customer?"; "update our customer personas"; "pull the personas out of the plan"; "compare our two customer segments"; "we learned something new from customer interviews"; "which persona should we focus on?". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-customer-personas/SKILL.md
---
# Customer personas

Everyone in the company should be able to say who the customer is, what job they are hiring the product for and
why they would say no. This skill keeps those answers as persona records in TOPY: first drafted from the business
plan, then corrected with real evidence — interviews, feedback, usage — so the plan's guess becomes the company's
knowledge. It compares personas when the founder must choose who to serve first.

## When to use
- "Who is our customer?", "update the personas", after a round of customer interviews (CEO-J22).
- After a plan is generated: turn its target segments into persona records.
- Before a GTM plan or a user journey, which hang off personas.
- Not for: mapping stages and drop-off (`topy-user-journey`); storing the research itself (`topy-research-library`); positioning copy (`topy-gtm-plan`).

## Before you start
- The project (`projects_list`). `personas_list` first: update rather than duplicate.
- `research_sources_list` for evidence already stored (interviews, surveys, reports).
- Ask for new evidence in the founder's words; never invent quotes or customers.

## Workflow
1. **Start from the plan (if no personas yet).** `plans_list`; for a `success` plan, preview `plan_operating_extract`, confirm after a yes, follow with `plan_status`, then `personas_list`. Extracted records carry `metadata_json.origin` `{type: "plan", plan_id}`.
2. **Check each persona is usable.**

| Field | Good looks like |
|---|---|
| `name` | a role in context, "Ops lead at a 20–50 person agency" |
| `segment_type` | `b2b` · `b2c` · `prosumer` |
| `jobs_to_be_done` | "when … I want to … so I can …" |
| `pains`, `gains` | specific and ranked, not "saves time" |
| `budget_range`, `decision_cycle_days` | from evidence or labelled assumption |
| `buying_criteria`, `objections` | what makes them buy and what stops them |
| `channels` | where they can actually be reached |
| `narrative` | a short paragraph a new hire can read |

3. **Correct with evidence.** For each claim the evidence changes: read with `persona_get`, show old → new with the source, then preview `persona_update` with `metadata_json` merged whole: `evidence_refs` gets the research source ids or interview notes; set `edited: true` so later plan extractions don't overwrite it. If the persona came from the plan and is being changed against it, say so — the plan may need revising (`topy-business-plan`).
4. **Unvalidated is fine, unlabelled is not.** A field with no evidence stays but is marked "assumption" in `narrative` until evidence arrives.
5. **New persona.** Preview `persona_create` with `metadata_json.origin` `{type: "founder"}` (or "agent") and its evidence.
6. **Compare and choose.** Score each persona 1–5 on pain intensity, ability to pay, reachability (channels), decision speed and fit with the current product. The highest total is the recommendation; ties go to the shorter `decision_cycle_days`. Choosing a different primary persona changes strategy: it is the founder's call (D2); suggest logging it.
7. **Retire.** A persona no longer pursued: say so in `narrative` and `metadata_json` rather than deleting. `persona_delete` only for duplicates or mistakes; it is permanent.

## Output
```
| Persona | Segment | Top job | Top pain | Budget | Cycle (days) | Evidence |
Changes this session: <field: old → new (source)>
Recommendation: serve <persona> first because …; assumptions still to test: …
```

## Example
> Five interviews logged in research sources show agency ops leads buy on a 14-day trial, not the 60-day cycle the plan assumed. Preview: `decision_cycle_days` 60 → 14, objection "needs Slack integration" added, `evidence_refs` = the five source ids, `edited: true`. Founder agrees; confirmed. Agent notes the plan's sales-cycle assumption is now broken and offers a plan revision.

## Quality bar
- [ ] No duplicate personas; each has a job, ranked pains, objections and channels.
- [ ] Every change cites evidence (`evidence_refs`) or is labelled an assumption.
- [ ] Edited records are marked `edited: true`; `metadata_json` sent whole.
- [ ] Comparisons use the stated scoring, not preference.
- [ ] No invented customers, quotes or figures.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools or evidence the founder gives; a KPI actual always has a `source` (`source: founder` for figures the founder states).
- Changing the primary persona is a goal-level (D2) decision: the founder's yes, never under a standing permission.
- Plan-extracted personas carry `origin`; before changing one the founder edited (`edited: true`), say so and ask.
- Anything sent outside TOPY (W3) is confirmed one at a time; money, equity and signatures are recorded or simulated only.
- Keep personal data out of personas: describe roles and segments, not named individuals. Deletes are permanent (W4).

## Related skills
- `topy-user-journey` — stages, touchpoints and KPIs for each persona.
- `topy-research-library` — store the interviews and sources behind the evidence.
- `topy-gtm-plan` — go-to-market for the chosen persona.
- `topy-business-plan` — when evidence contradicts the plan.
- `topy-operating-board` — the persona count on the board.
