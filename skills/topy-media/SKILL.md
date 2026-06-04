---
name: topy-media
description: List, register, and delete TOPY media assets. Use when the user wants to manage uploaded images or URL-based media for projects and plans.
---

# TOPY Media

## Intent

Manage the user’s media assets for project and plan workflows.

## Allowed operations

- List media
- Register an image by URL
- Delete media

## Route map

- `GET /api/v1/media`
- `POST /api/v1/media/url`
- `DELETE /api/v1/media/{id}`

## Rules

- Use the media item the user asked for; do not delete by guesswork.
- When registering a URL, preserve the original URL unless the user asked to normalize it.
- Do not use media routes for project or business-plan mutations.

## Failure behavior

- If the media item is not found, report that directly.
- If upload or registration fails, surface the backend error and stop.
