# TOPY AI CEO Skills

Agent skills for TOPY dashboard workflows, published for `npx skills` install flows.

## Install

Install the full catalog:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills
```

Install a specific skill:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --skill topy-onboarding
```

Install for Codex:

```bash
npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills --agent codex
```

## Available Skills

- `topy-dashboard` - router skill for TOPY workflows
- `topy-onboarding` - create projects from website, file, brainstorm, or idea
- `topy-projects` - inspect and edit existing projects
- `topy-business-plans` - generate, edit, export, and manage business plans
- `topy-templates` - create and edit business-plan templates
- `topy-billing` - inspect credits, entitlements, and subscriptions
- `topy-media` - list, register, and delete media assets

## Requirements

- A valid `TOPY_API_KEY`
- Access to the TOPY backend API used by the skill route maps

## Repository Layout

```text
skills/
  topy-dashboard/
  topy-onboarding/
  topy-projects/
  topy-business-plans/
  topy-templates/
  topy-billing/
  topy-media/
```

## License

MIT.
