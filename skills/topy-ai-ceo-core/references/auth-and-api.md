# Auth and API Convention

Use this reference for every non-core TOPY workflow.

## Base URL

All API calls should target:

```text
https://topy.ai/api
```

Append the route path to that base URL, for example:

```text
https://topy.ai/api/v1/projects/my?include_pending=true&view=active
```

## Authentication

- Read the user-scoped API key from `TOPY_AI_KEY`.
- Send it as a bearer token.
- Do not invent another key name for the same workflow.

Example:

```http
Authorization: Bearer <TOPY_AI_KEY>
```

## Preflight rule

Before making any non-core TOPY API call:

1. Check whether `TOPY_AI_KEY` is available.
2. If it is missing, stop.
3. Route the user to `topy-init` to set it up.
4. Do not proceed with a partial or guessed auth state.

## Call style

- Keep payloads faithful to the backend schema.
- Use the smallest valid request body.
- Prefer explicit route selection over vague “dashboard” language when calling the API.
- If a route requires a project ID, resolve that first before mutating anything.
