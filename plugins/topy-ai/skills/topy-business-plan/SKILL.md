---
name: topy-business-plan
description: Write a new TOPY.AI business plan (after a credit check), follow it to the end, then read, edit, fix and export it. Use when the user says things like "write a business plan for my project"; "is my business plan ready?"; "show me the financial plan section"; "rewrite the market analysis to be shorter"; "the plan has broken formatting"; "export my plan to Word". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-business-plan/SKILL.md
---
# Business plans

TOPY writes investor-ready business plans section by section (about 7 minutes for ~10,000 words) and keeps them
editable. This skill runs the whole life of a plan: choose its shape, check the cost, generate, follow, deliver, then
read and change it.

## When to use
- A new plan for a project; "is it ready?"; reading, rewriting or fixing sections; exporting.
- Not for: a figure, milestone or hire that changes across the plan (`topy-plan-revision`); an investor-style critique (`topy-investor-ready`).

## Before you start
- The project (`projects_list`; none → `topy-projects` first).
- Generating costs **50 TOPY credits** (a retry costs 50 again; a failed run is refunded automatically).
- Ask for facts the founder wants used (funding amount, pricing, team, traction) — the writer will otherwise make reasonable assumptions and label them.

## Workflow

### A. Write a new plan
1. `plan_options_get` → templates, purposes, audiences, styles and `recommended_template_id`. Use the ids exactly; say in one line which you chose and why (e.g. "SEIS-ready seed plan for angel investors, professional style").
2. `plan_estimate` → if `can_generate` is false, stop and give `dashboard_link` (page `billing`).
3. `plan_generate` with `template_id`, `purpose_id`, `audience_id`, `style_id`, `language_code` (the founder's language, e.g. `zh-TW`), `total_word_count` if asked, and the founder's facts in `additional_instructions`. Show the preview (it states 50 credits and the balance after); confirm only after a yes.
4. Follow with `plan_status` (`job_id` or `plan_id`) every minute or so; report `completed_subtasks/total_subtasks`. Never say "ready" before `status` is `success`.
5. Deliver: `plan_get` → title, words, section list. Summarise the key numbers (raise, revenue targets, break-even, team) in five lines and point out anything that looks weak; offer `topy-investor-ready`.

### B. Read
- `plans_list` (newest first; `view: archived` for archived). `plan_get` gives a summary and section list; `section: <index>` one section's Markdown; `full: true` the whole plan (long — only when needed).

### C. Change
| The founder wants… | Use |
|---|---|
| a section reworded from an instruction | `plan_section_suggest` (suggestion only) → show it → if kept, `plan_update` with that `section` and the Markdown |
| their own text in a section | `plan_update` with `section` and `markdown` |
| a section written again from scratch | `plan_section_regenerate` (`section_number` is 1-based) |
| formatting fixed (diagrams in code blocks, HTML in tables) | `plan_fix_markdown` (a job; follow with `plan_status`) — content unchanged |
| a renamed or starred plan | `plan_rename` |
| a plan archived / back | `plan_delete` / `plan_restore` (archiving is reversible) |
| a failed generation retried | `plan_job_retry` (50 credits again) |
| a running job stopped | `plan_job_cancel` |

### D. Export
`plan_export` → the Markdown; Word and PDF come from the link it returns (the TOPY editor's Download menu).

## Output
- After generation: title, words, section list, five-line summary of the numbers, one suggested next step.
- After an edit: which section changed and a two-line before/after gist.

## Example
"Write a plan for Lumen Labs for SEIS angels." → `plan_options_get` (recommended: business plan template) → `plan_estimate` (120 credits) → preview "Write a new business plan with template … Uses 50 TOPY credits (120 available, 70 after)." → founder: yes → confirm → `plan_status` 4/14 … 14/14 → `plan_get`: "Lumen Labs — Seed Plan", 13,100 words, 14 sections → summary + "Want me to check it like an investor would?"

## Quality bar
- [ ] The cost was stated and agreed before any generation or retry.
- [ ] "Ready" only after `status: success` in this session.
- [ ] Ids came from `plan_options_get`, not guessed.
- [ ] Edits went through suggestion → show → save; nothing overwritten silently.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Don't invent facts for the plan; pass the founder's facts in `additional_instructions` and flag the writer's assumptions as assumptions.
- Show TOPY's errors as they are (not enough credits, plan needed for AI editing, not found) and stop; don't retry blindly.
- `plan_update` replaces text; quote what will be replaced in the preview.

## Related skills
- `topy-plan-revision` — a change that runs through the whole plan.
- `topy-investor-ready` — critique before sending to investors.
- `topy-plan-templates` — shape future plans.
