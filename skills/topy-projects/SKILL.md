---
name: topy-projects
description: List, inspect, edit, archive, restore, and manage project resources in TOPY. Use when the user wants to change or review an existing project record.
---

# TOPY Projects

## Intent

Work with existing project records and their attached project resources.

## Allowed operations

- List the current user’s projects
- Inspect a project
- Edit project metadata
- Archive or restore a project
- Read or edit project resources

## Route map

- `GET /api/v1/projects/my?include_pending=true&view=active`
- `GET /api/v1/projects/{project_id}`
- `PATCH /api/v1/projects/{project_id}`
- `DELETE /api/v1/projects/{project_id}`
- `POST /api/v1/projects/{project_id}/restore`
- Project resources under `/api/v1/projects/{project_id}/...`

## Resource groups

- Research sources
- Decisions
- Journal entries
- GTM plans
- Memory nodes
- Risks
- Investor contacts
- Investor updates
- Growth experiments

## Rules

- Resolve the project explicitly before mutating anything.
- Preserve existing structured data unless the user asked for a replacement.
- Keep resource edits inside the resource type the user named.
- Do not use this skill for business-plan generation, template editing, billing, or media operations.

## Failure behavior

- If the project is missing or inaccessible, surface that directly.
- If the payload does not match the backend schema, stop and ask for the missing fields.
