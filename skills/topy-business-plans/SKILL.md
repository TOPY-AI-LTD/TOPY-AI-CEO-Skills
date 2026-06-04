---
name: topy-business-plans
description: Generate, inspect, edit, regenerate, and export TOPY business plans. Use when the user wants to work on a plan lifecycle for a specific project.
---

# TOPY Business Plans

## Intent

Handle the full business-plan workflow for a project, including job creation, plan editing, section regeneration, and exports.

## Allowed operations

- List available templates and parameters
- Start plan generation
- Check job progress
- Inspect plan detail
- Edit plan content and metadata
- Regenerate sections
- Export markdown, DOCX, or print view
- Update plan preferences

## Route map

- `GET /api/v1/projects/business-plan/options`
- `GET /api/v1/projects/{pid}/business-plan/options`
- `POST /api/v1/projects/{pid}/business-plan/jobs`
- `GET /api/v1/projects/{pid}/business-plan/jobs/{job_id}`
- `GET /api/v1/projects/{pid}/business-plan/jobs/latest`
- `POST /api/v1/projects/{pid}/business-plan/jobs/{job_id}/cancel`
- `POST /api/v1/projects/{pid}/business-plan/jobs/{job_id}/retry`
- `GET /api/v1/projects/{pid}/business-plan`
- `GET /api/v1/projects/{pid}/business-plan/{plan_id}`
- `PATCH /api/v1/projects/{pid}/business-plan/{plan_id}`
- `PATCH /api/v1/projects/{pid}/business-plan/{plan_id}/meta`
- `DELETE /api/v1/projects/{pid}/business-plan/{plan_id}`
- `POST /api/v1/projects/{pid}/business-plan/{plan_id}/restore`
- `GET /api/v1/projects/{pid}/business-plan/{plan_id}/export/markdown`
- `GET /api/v1/projects/{pid}/business-plan/{plan_id}/export/docx`
- `GET /api/v1/projects/{pid}/business-plan/{plan_id}/export/print`
- `POST /api/v1/projects/{pid}/business-plan/{plan_id}/subtasks/{subtask_no}/regenerate`
- `POST /api/v1/projects/{pid}/business-plan/{plan_id}/ai/section-edit`
- `PATCH /api/v1/projects/{pid}/business-plan/preferences`

## Rules

- Check credit balance before starting a generation job if the amount is not already known.
- Do not start generation if the user does not have enough credits.
- Keep template and parameter selections aligned with the backend options payload.
- Treat job state as authoritative; do not fabricate completion.
- Use the plan detail routes for edits and exports, not the onboarding routes.

## Failure behavior

- If the job is queued or running, report the current state instead of retrying blindly.
- If the backend says credits are insufficient, stop and surface that message.
