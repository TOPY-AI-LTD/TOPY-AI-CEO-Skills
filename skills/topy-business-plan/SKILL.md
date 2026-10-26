---
name: topy-business-plan
description: Generate, read, edit, fix, export and template TOPY.AI business plans. Use when the user wants a new business plan for a project, wants to read or change part of an existing plan, fix its formatting, export it to Markdown/Word/PDF, or manage plan templates.
---

# Business plans on TOPY.AI

Follow the shared rules in `topy-ai-ceo` (project first, two-call changes, credits, no invented facts).
Tools are TOPY's MCP tools, or `topy <tool>` in a terminal.

## Write a new plan

1. **Project.** `projects_list`; if the idea has no project yet, use `topy-projects` to create one.
2. **Shape.** `plan_options_get` returns templates, purposes, audiences and styles plus a
   `recommended_template_id`. Use the ids exactly. Say which you picked and why in one line.
3. **Cost.** `plan_estimate`: 50 credits. If `can_generate` is false, stop and give `dashboard_link`
   (page `billing`).
4. **Generate.** `plan_generate` with `template_id` (and `purpose_id`, `audience_id`, `style_id`,
   `language_code` when the user writes in another language, `additional_instructions` for facts the
   user gave you). Show the preview (cost and balance), confirm after the user agrees.
5. **Follow.** `plan_status` with the returned `job_id` (or `plan_id`) every minute or so; about 7 minutes.
6. **Deliver.** `plan_get` gives the summary and section list; summarise the plan's main numbers and
   anything weak. `plan_export` for the Markdown; Word/PDF via the link it returns.

## Read and change a plan

- `plans_list` (newest first), `plan_get` (summary), `plan_get` with `section: <index>` for one section,
  `full: true` for the whole plan (long: only when needed).
- Rewrite part of a section from an instruction: `plan_section_suggest` returns a suggestion only; show
  it, and if the user keeps it, `plan_update` with that `section` index and the Markdown.
- The user's own text: `plan_update` (one `section`, or the whole plan).
- Redo a section from scratch with the writer: `plan_section_regenerate` (section_number is 1-based).
- Broken formatting (diagrams in code blocks, HTML in tables): `plan_fix_markdown` fixes every section
  without changing the content (a job; follow with `plan_status`).
- A change to a figure, milestone, KPI or the team that runs through the plan: use `topy-plan-revision`,
  not section edits.
- Rename or star: `plan_rename`. Archive / restore: `plan_delete` / `plan_restore`.
- A failed generation: `plan_job_retry` (50 credits again; the failed run was refunded).

## Templates

`templates_list` (official and the user's own). `template_create` clones an official or custom template,
or builds one with the AI from a requirement (`ai_prompt`) or a document's text (`upload_file`).
`template_assistant` suggests a change to a custom template (keep it with `template_update`).
`template_star`, `template_delete` / `template_restore`. `plan_defaults_set` sets the project's defaults.

## When something goes wrong

Show TOPY's error as it is (not enough credits, feature needs a plan, not found) and stop; don't retry
blindly. If a plan is still `running`, report progress instead of starting another.
