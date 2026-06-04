---
name: topy-onboarding
description: Create a TOPY project from a website, local file, brainstorm, or direct idea. Use when the user wants to turn an external source or rough concept into a new project record.
---

# TOPY Onboarding

## Intent

Create a new project from one of the supported onboarding sources.

## Allowed operations

- Create a project from a website URL
- Create a project from a local file
- Create a project from brainstormed structure
- Create a project from a direct idea or short prompt
- Start or continue onboarding chat when the user wants a guided flow

## Route map

- `POST /api/v1/projects/website`
- `POST /api/v1/projects/upload`
- `POST /api/v1/projects/from-brainstorm`
- `POST /api/v1/projects/from-idea`
- `POST /api/v1/onboarding/chat/start`
- `POST /api/v1/onboarding/chat/turn`
- `POST /api/v1/onboarding/chat/sessions/{session_id}/complete`

## Inputs

- Website: a URL and any optional notes the user wants preserved
- Local file: the file contents or an attached file
- Brainstorm: the raw brainstorm text and any structured notes
- Idea: the short prompt or problem statement

## Rules

- Normalize source material into the backend payload shape, do not invent fields.
- If the source is a file, read and summarize the file before creating the project.
- If the user has not specified the target project name or scope, infer only from the provided source and keep the payload conservative.
- If onboarding chat is used, keep the chat state consistent and complete the session only when the user is ready.

## Failure behavior

- If validation fails, surface the backend error and stop.
- If the source content is ambiguous or incomplete, ask a clarifying question before creating the project.
