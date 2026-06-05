---
name: topy-init
description: Initialize TOPY access by helping the user set and verify TOPY_AI_KEY and the https://topy.ai/api base URL. Use when the key is missing, the environment is not set up, or another TOPY skill needs auth preflight before it can call the API.
---

# TOPY Init

Use this skill to set up access before any non-core TOPY workflow.

## When to use

- The user has not set `TOPY_AI_KEY`
- A TOPY workflow needs auth and the key is missing
- The user asks how to start using TOPY skills
- Another TOPY skill has to stop because auth is not ready

## What to set

- Environment variable: `TOPY_AI_KEY`
- API base URL: `https://topy.ai/api`

## Setup steps

1. Ask the user to add or paste their `TOPY_AI_KEY` from the TOPY dashboard.
2. Tell them to export it in the current shell or add it to their shell profile.
3. Confirm the API base URL they should use.
4. Verify the value is available before returning to the requesting skill.

## Common commands

Temporary for one command:

```bash
TOPY_AI_KEY=tp_... npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --all
```

Current shell session:

```bash
export TOPY_AI_KEY=tp_...
```

Persist for bash:

```bash
echo 'export TOPY_AI_KEY=tp_...' >> ~/.bashrc
source ~/.bashrc
```

Persist for zsh:

```bash
echo 'export TOPY_AI_KEY=tp_...' >> ~/.zshrc
source ~/.zshrc
```

## Rules

- Never guess the key.
- Never continue a non-core TOPY request without `TOPY_AI_KEY`.
- Return to the requesting skill once the key is set.
- If the user does not have a key yet, point them to the TOPY dashboard key page and stop.
