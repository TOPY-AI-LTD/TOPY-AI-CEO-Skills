---
name: topy-templates
description: Create, edit, star, unstar, archive, and restore TOPY business-plan templates using TOPY_AI_KEY. Use when the user wants to manage template definitions or the template assistant.
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

- `GET https://topy.ai/api/v1/projects/{pid}/business-plan/custom-templates`
- `POST https://topy.ai/api/v1/projects/{pid}/business-plan/custom-templates`
- `PATCH https://topy.ai/api/v1/projects/{pid}/business-plan/custom-templates/{tid}`
- `DELETE https://topy.ai/api/v1/projects/{pid}/business-plan/custom-templates/{tid}`
- `POST https://topy.ai/api/v1/projects/{pid}/business-plan/custom-templates/{tid}/restore`
- `PATCH https://topy.ai/api/v1/projects/{pid}/business-plan/official-templates/{tid}`
- `POST https://topy.ai/api/v1/projects/{pid}/business-plan/template-assistant`

## API and auth

See [references/auth-and-api.md](../topy-ai-ceo-core/references/auth-and-api.md) for the shared convention.

## Rules

- Before any API call, verify that `TOPY_AI_KEY` is available.
- Use `https://topy.ai/api` as the base URL for all calls.
- Keep template payloads aligned with the backend schema and the selected project.
- Preserve official-template metadata unless the user explicitly asks to star or unstar it.
- Use the template assistant for guided edits when the user wants help refining structure or wording.

## Failure behavior

- If `TOPY_AI_KEY` is missing, stop and route the user to `topy-init`.
- If the template is missing or archived, surface that state and ask whether to restore or replace it.
- If the payload is malformed, stop and request the missing fields.
