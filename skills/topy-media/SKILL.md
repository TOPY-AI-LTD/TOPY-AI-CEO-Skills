---
name: topy-media
description: List, register, and delete TOPY media assets using TOPY_AI_KEY. Use when the user wants to manage uploaded images or URL-based media for projects and plans.
---

# TOPY Media

## Intent

Manage the user’s media assets for project and plan workflows.

## Allowed operations

- List media
- Register an image by URL
- Delete media

## Route map

- `GET https://topy.ai/api/v1/media`
- `POST https://topy.ai/api/v1/media/url`
- `DELETE https://topy.ai/api/v1/media/{id}`

## API and auth

See [references/auth-and-api.md](../topy-ai-ceo-core/references/auth-and-api.md) for the shared convention.

## Rules

- Before any API call, verify that `TOPY_AI_KEY` is available.
- Use `https://topy.ai/api` as the base URL for all calls.
- Use the media item the user asked for; do not delete by guesswork.
- When registering a URL, preserve the original URL unless the user asked to normalize it.
- Do not use media routes for project or business-plan mutations.

## Failure behavior

- If `TOPY_AI_KEY` is missing, stop and route the user to `topy-init`.
- If the media item is not found, report that directly.
- If upload or registration fails, surface the backend error and stop.
