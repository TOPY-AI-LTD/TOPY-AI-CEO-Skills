# Changelog

## v0.1.0

- Initial public release of TOPY AI CEO skills
- Added dashboard router skill and specialist skills for onboarding, projects, business plans, templates, billing, and media

## v0.1.1

- Added TOPY logo branding to the README
- Added GitHub Actions validation for `npx skills add . --list`

## v0.2.0

- Added `topy-ai-ceo-core` as a general executive decision skill
- Organized the strategy, crisis, competitive, and debiasing references into focused files

## v0.3.0

- Rewrote `topy-ai-ceo-core` into an original, cleaner executive playbook
- Consolidated the quantitative utilities into a single helper script
- Added focused examples for market entry, crisis, prioritization, and fundraising

## v0.3.1

- Removed an accidental Python bytecode artifact from the package
- Added a scripts-level ignore rule for bytecode caches

## v0.4.0

- Expanded every core reference into a fuller executive playbook
- Added TOPY-specific examples and a lightweight eval suite
- Moved the core examples into the skill package where they belong

## v0.4.1

- Removed the TOPY-specific example set from the core package
- Cleaned up the remaining TOPY wording in the eval suite

## v0.4.2

- Rewrote the README into a fuller landing page and usage guide

## v0.4.3

- Added a CEO daily workflow section across the TOPY product skills
- Explained how `topy-ai-ceo-core` works with projects, templates, plans, and billing

## v0.4.5

- Documented the `--all` install path for the full skills catalog

## v0.4.6

- Expanded the README with the TOPY product skill workflow

## v0.5.0

- Added the `topy-init` setup skill for `TOPY_AI_KEY`
- Standardized non-core TOPY skills on `https://topy.ai/api`
- Added auth preflight rules so non-core skills stop and route to init when the key is missing

## v0.5.1

- Documented the `skills update` upgrade path for installed skills

## v0.6.0

- Rebuilt the product skills on TOPY's remote MCP server (https://topy.ai/mcp) and the `topy` CLI
  (`@topy-ai/ceo`): `topy-ai-ceo`, `topy-business-plan`, `topy-plan-revision`, `topy-fundraising`,
  `topy-ceo-workspace`, `topy-projects`. Changes are previewed and confirmed; no key in prompts.
- Removed the REST-only skills they replace (`topy-init`, `topy-dashboard`, `topy-onboarding`,
  `topy-projects`, `topy-business-plans`, `topy-templates`, `topy-billing`, `topy-media`).
- Added a Claude Code plugin (`.claude-plugin/`) with the TOPY MCP server (`.mcp.json`).

## v0.7.0

- 42 skills in six plugins: core (`topy-ai`, with the MCP server), strategy, fundraising, finance,
  operations and leadership, plus the `topy-ai-all` bundle; Claude Code and Codex marketplaces,
  `skills.json` and a Pi package
- New `@topy-ai/skills` installer for Claude Code, Codex, Pi, Cursor, Gemini CLI and 15 other agents
- `topy-ai-ceo` is now `topy-connect`; `topy-fundraising` split into `topy-investor-ready`,
  `topy-seis`, `topy-investor-relations` and the fundraising plugin; `topy-ceo-workspace` split into
  one skill per record plus `topy-daily` and `topy-weekly-review`; `topy-ai-ceo-core` is now
  `topy-ceo-advisor`, routing to the focused strategy and leadership skills
- The CLI is now `@topy-ai/cli` and the local MCP server `@topy-ai/mcp`; `@topy-ai/ceo` is deprecated
