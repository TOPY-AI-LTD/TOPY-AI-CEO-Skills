---
name: topy-templates
description: Create, edit, star, unstar, archive, and restore TOPY business-plan templates. Use when the user wants to manage template definitions or the template assistant.
---

# TOPY Templates

## Intent

Manage official and custom business-plan templates for a project.

## Allowed operations

- List custom templates
- Create a custom template
- Edit a custom template
- Archive and restore a custom template
- Star or unstar an official template
- Use the template assistant to refine template content

## Route map

- `GET /api/v1/projects/{pid}/business-plan/custom-templates`
- `POST /api/v1/projects/{pid}/business-plan/custom-templates`
- `PATCH /api/v1/projects/{pid}/business-plan/custom-templates/{tid}`
- `DELETE /api/v1/projects/{pid}/business-plan/custom-templates/{tid}`
- `POST /api/v1/projects/{pid}/business-plan/custom-templates/{tid}/restore`
- `PATCH /api/v1/projects/{pid}/business-plan/official-templates/{tid}`
- `POST /api/v1/projects/{pid}/business-plan/template-assistant`

## Rules

- Keep template payloads aligned with the backend schema and the selected project.
- Preserve official-template metadata unless the user explicitly asks to star or unstar it.
- Use the template assistant for guided edits when the user wants help refining structure or wording.

## Failure behavior

- If the template is missing or archived, surface that state and ask whether to restore or replace it.
- If the payload is malformed, stop and request the missing fields.
