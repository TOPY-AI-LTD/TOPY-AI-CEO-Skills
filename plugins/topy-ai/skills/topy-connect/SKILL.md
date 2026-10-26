---
name: topy-connect
description: Connect an AI agent to TOPY.AI's AI CEO through the MCP server (OAuth, or the CLI / an API key without a browser) and pick the project to work on. Use when the user says things like "connect to TOPY"; "set up my AI CEO in this agent"; "sign in to TOPY.AI"; "the TOPY tools are missing"; "TOPY says my sign-in expired"; "which project are we working on?". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-connect/SKILL.md
---
# Connect to TOPY.AI

TOPY.AI is an AI CEO for founders: it writes and revises business plans, drafts SEIS Advance Assurance answers,
and keeps the founder's CEO records (decisions, risks, experiments, investors). Agents reach it through the MCP
server at `https://topy.ai/mcp`. This skill gets the agent connected, proves it with a free read, and picks the
project every other TOPY skill acts on.

## When to use
- A TOPY tool is missing, or a tool says the user must sign in or the sign-in expired.
- The user says "connect TOPY", "set up my AI CEO", "log in to TOPY".
- The account has several projects and the agent doesn't know which `project_id` to use, or the user wants to switch.
- Not for: creating a new project (`topy-projects`); setting up an agent that runs on a schedule (`topy-scheduled-agent`).

## Before you start
- Find out which agent this is and whether it can open a browser. Ask only if you can't tell.
- Never ask for a password. Never ask the user to paste an API key into the chat.
- Don't run a credit-spending or AI-generating tool to "test" the connection: `account_get` and `projects_list` are free reads.
- Track three states: installed (the server is configured), signed in (TOPY accepted the user), verified (a read worked in this session). Only the third counts as connected.

## Workflow

### 1. Check the connection
Call `account_get`.

| Result | Meaning | Next |
|---|---|---|
| Returns an email | Connected and verified | Step 3 |
| Tool does not exist | Server not configured, or the agent needs a reload | Step 2 |
| Says to sign in / key refused | Configured, token missing, expired or revoked | Step 2, sign-in part only |

### 2. Connect
In this order of preference:

1. **OAuth in a browser (preferred).**
   - Claude or ChatGPT (web/desktop): add a custom connector with the URL `https://topy.ai/mcp`, then sign in to TOPY and click **Allow** on the TOPY page.
   - Claude Code: `claude mcp add --transport http topy https://topy.ai/mcp`, then `/mcp` → **topy** → **Authenticate**. With the `topy-ai` plugin installed the server is already declared: only `/mcp` → Authenticate.
   - Codex: `codex mcp add topy --url https://topy.ai/mcp`. Other clients: add a remote (HTTP) MCP server with that URL and approve the sign-in when asked; don't guess menu names.
2. **No browser here (servers, CI, SSH).**
   - Device sign-in: `npx @topy-ai/cli login` prints a link and a code; the user approves it on any device (`topy.ai/oauth/device`). The sign-in renews itself.
   - Or an API key: the user creates one under Dashboard → API keys and puts it in `TOPY_API_KEY` (environment or the client's secret store) — never in a repository or the chat. A read-only key can only read.
   - Configure the local MCP server command `npx -y @topy-ai/mcp` (Claude Code: `claude mcp add topy -- npx -y @topy-ai/mcp`).
3. **Reload.** Many clients load new tools only after a reload. Say the reload step once and wait; don't loop calling tools that aren't loaded.

Call `account_get` again. Only say "connected" when it returns the user's email.

If a TOPY tool later reports the sign-in failed or expired, stop and give the one fix (authenticate again, or replace `TOPY_API_KEY`). Don't search files, keychains or shell history for credentials, and don't fall back to scraping the TOPY website. If the user pastes a key into the chat anyway: don't use or repeat it; tell them to revoke it under API keys and create a new one in `TOPY_API_KEY`.

No TOPY account yet: they can sign up at https://topy.ai.

### 3. Pick the project
Call `projects_list`.
- **One project:** use it; say which. Tools may leave `project_id` out, but say the name.
- **Several:** list them by name and ask which one; remember the answer. If the user later says "my other company", call `projects_list` again rather than guessing.
- **None:** offer `topy-projects` to create one from an idea or a website.
- On an account with several projects, pass `project_id` on every change and name the project when showing a preview. A confirmation for one project is never reused for another.

### 4. Hand off
Suggest one next step the user can just say yes to:

| Situation | Suggest |
|---|---|
| Project has no business plan yet | `topy-business-plan` |
| Plans exist; user wants to know what needs them | `topy-daily` |
| A figure, hire or milestone changed | `topy-plan-revision` |
| Preparing to raise | `topy-investor-ready` |

## Output
At most 120 words:

**Status** — connected as <email>, working on <project>; or the one blocker and its fix.
**Next** — the reload step if needed, then one or two suggested skills in plain words.

## Example
User: "Hook TOPY up in Claude Code."
1. `account_get` → tool doesn't exist.
2. "Run `claude mcp add --transport http topy https://topy.ai/mcp`, then `/mcp` → topy → Authenticate, and click Allow on the TOPY page." The user comes back.
3. `account_get` → founder@lumenlabs.example.
4. `projects_list` → "Lumen Labs" and "Lumen Retail". The user picks Lumen Labs.
> **Status** — connected as founder@lumenlabs.example, working on Lumen Labs.
> **Next** — want to see what needs you today (`topy-daily`), or write the first business plan (`topy-business-plan`)?

## Quality bar
- [ ] `account_get` returned an email in this session before saying "connected".
- [ ] One project is chosen and named.
- [ ] No password or key was requested, echoed or stored.
- [ ] No credit-spending, generating or writing tool was called during setup.
- [ ] A failed setup names exactly one blocker and the user's next action.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user. (This skill only reads.)
- Credentials: OAuth or device sign-in first; API keys only in environment variables or a secret store. A key seen in chat is leaked and must be revoked.
- Don't remove or overwrite the user's other MCP servers; avoid duplicate TOPY entries.
- Tool errors: fix an input problem once and retry; if access is denied, report it and stop. After two failures on the same step, quote TOPY's message.
- Buying credits or plans, API keys and connected apps are handled in the dashboard: give the link from `dashboard_link`. Don't promote upgrades.

## Related skills
- `topy-daily` — the first useful thing once connected.
- `topy-projects` — create a project when there is none.
- `topy-scheduled-agent` — connect an agent that runs on a schedule.
