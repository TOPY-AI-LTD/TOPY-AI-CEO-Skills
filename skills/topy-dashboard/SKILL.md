---
name: topy-dashboard
description: Entry point for TOPY.AI Codex workflows using a TOPY API key. Use when the user wants to manage TOPY projects, onboarding, business plans, templates, billing, or media from Codex.
---

# TOPY Dashboard

Use this as the router skill for the TOPY plugin.

## When to use

- The user says "use TOPY" or asks for a TOPY workflow without naming a narrower skill.
- The user wants to work inside the dashboard API from Codex.

## Route to a specialist skill

- Project creation from website, file, brainstorm, or direct idea: `../topy-onboarding/SKILL.md`
- List, inspect, edit, archive, restore, or manage project resources: `../topy-projects/SKILL.md`
- Generate, inspect, edit, or export business plans: `../topy-business-plans/SKILL.md`
- Create, edit, star, or restore templates: `../topy-templates/SKILL.md`
- Inspect credits, entitlements, or subscriptions: `../topy-billing/SKILL.md`
- Manage user media: `../topy-media/SKILL.md`

## Common rules

- Authenticate with `TOPY_API_KEY`.
- Keep payloads faithful to the backend schema.
- Stop on credit or subscription errors instead of trying to bypass them.
- This plugin release is user-dashboard only.
