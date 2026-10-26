---
name: topy-plan-templates
description: Choose, copy, build and refine TOPY.AI business plan templates — official ones, the founder's own, AI-built from a requirement or a document — and set a project's defaults. Use when the user says things like "which business plan template should I use?"; "make a template for investor memos"; "turn this document into a template"; "add a section on regulation to my template"; "use this template by default"; "star the SEIS template". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-plan-templates/SKILL.md
---
# Business plan templates

A template is the outline TOPY's writer follows: sections, their purpose and weight. Official templates cover the
common cases (seed plans, SEIS, due-diligence reports…); founders can copy one, have the AI build one from a
requirement or a document, and refine it with the template assistant.

## When to use
- Picking the right template before `topy-business-plan`; a recurring document type (board memo, grant application).
- Not for: editing a written plan (`topy-business-plan`).

## Before you start
- The project. What the document is for: audience (angels, bank, grant body, board), purpose, length.

## Workflow
1. **Look first.** `templates_list` → official templates and the founder's own (`custom`), plus `recommended_template_id`. If an official one fits, use it — fewer custom templates means less to maintain.
2. **Create, if none fits.** `template_create` with `source_type`:
   | source_type | When | Needs |
   |---|---|---|
   | `clone_official` | an official one is close | `source_template_id` |
   | `clone_custom` | copy one of theirs | `source_custom_template_id` |
   | `ai_prompt` | describe what it must cover | `requirement` (and `guided_template_id` to start from) |
   | `upload_file` | a document shows the structure | `upload_text` (+ `requirement`) |
   Give it a `name` and `description`; preview, confirm after a yes.
3. **Refine.** `template_assistant` with the instruction ("add a regulatory section before operations") returns a suggested structure only; show the change; if kept, `template_update` with that `template_json`.
4. **Defaults.** `plan_defaults_set` (template, purpose, audience, style — valid values from `plan_options_get`) so new plans for this project start from it.
5. **Tidy.** `template_star` for favourites; `template_delete` archives (reversible with `template_restore`).

## Output
The template chosen or created (name, id, its sections in one line each) and whether it is now the project default.

## Quality bar
- [ ] An official template was considered before creating one.
- [ ] AI suggestions were shown before `template_update`.
- [ ] Ids came from `templates_list`.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- `template_update` replaces the structure; say what changes.
- Uploaded text is used only to build the structure; don't paste confidential documents without the founder's say-so.

## Related skills
- `topy-business-plan` — write a plan with the template.
